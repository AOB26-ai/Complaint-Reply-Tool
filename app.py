import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  

app = Flask(__name__)

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_BASE_URL", "https://api.groq.com/openai/v1"),
)

MODEL = os.environ.get("OPENAI_MODEL", "openai/gpt-oss-120b")

SYSTEM_PROMPT = """You are a professional customer service representative writing reply drafts for small businesses in Nairobi (shops, courier services, Airbnbs, restaurants).

When given a customer complaint, write a polite, professional reply that:
1. Acknowledges the issue empathetically and shows you understand the customer's frustration.
2. Does NOT blame the customer or make excuses.
3. Does NOT over-promise or guarantee specific outcomes you cannot control.
4. Offers a clear, concrete next step (e.g. investigating, requesting more details, arranging a callback, processing a refund/return if appropriate).
5. Keeps the tone warm, respectful, and solution-oriented.
6. Is concise — usually 4–8 sentences.

Output ONLY the reply text. No subject lines, no "Dear Customer", no extra commentary."""


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json(silent=True) or {}
    complaint = (data.get("complaint") or "").strip()

    if not complaint:
        return jsonify({"error": "Please paste a customer complaint first."}), 400

    if not os.environ.get("OPENAI_API_KEY"):
        return jsonify({
            "error": "API key not configured. Set OPENAI_API_KEY environment variable."
        }), 500

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Customer complaint:\n\n{complaint}"},
            ],
            temperature=0.5,
            max_tokens=400,
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": f"Failed to generate reply: {str(e)}"}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)