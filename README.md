# Complaint Reply Drafter

**Live URL:** _https://complaint-reply-tool-2.onrender.com

A simple web tool that turns customer complaint messages into professional reply drafts in seconds.

---

## Portfolio Overview
 
Paste a customer complaint → click one button → receive a polite, professional reply draft. The AI acknowledges the issue, avoids blame and over-promising, and suggests a clear next step.

Small Nairobi businesses — shops, courier services, Airbnbs, restaurants — that receive complaints on WhatsApp and need to respond quickly and professionally without spending 15–20 minutes writing each reply.

Poor or slow responses to complaints damage reputation and lose repeat customers. This tool helps small businesses reply faster, stay professional, and protect their brand — even when the owner is busy or not confident writing formal English.

**Stack**  
- Frontend: HTML, CSS, Vanilla JavaScript  
- Backend: Flask (Python)  
- AI: Groq (`openai/gpt-oss-120b`)  
- Deployment: Render  

**Live demo:** _https://complaint-reply-tool-2.onrender.com

---

## What the tool does

1. User pastes a customer complaint into a single text box.
2. Clicks **Generate Reply**.
3. The AI returns a professional draft that:
   - Acknowledges the issue empathetically
   - Does not blame the customer
   - Does not over-promise
   - Offers a clear next step

The interface is deliberately minimal: one text box, one button, reply appears on the same page.

---

## Suggested pricing for a branded version

If a business wants a **branded** version of the tool:

| Package       | What’s included                                                                 | Suggested price (KES)                  |
|---------------|----------------------------------------------------------------------------------|----------------------------------------|
| **Basic**     | Client logo + colours, hosted version, simple custom domain                      | 15,000 – 25,000 one-time               |
| **Standard**  | Branding + custom system prompt for their industry + WhatsApp-friendly short replies | 35,000 – 50,000 one-time            |
| **Pro**       | Everything in Standard + monthly usage reports + simple admin page to edit tone/rules | 70,000 – 100,000 one-time + 5,000–8,000/month |

**Notes for clients:**
- Can be used as a standalone page or embedded on their website.
- Ongoing cost is mainly AI API usage (very low for this volume) + hosting.
- Optional future upgrade: connect to WhatsApp Business API for even faster replies.

---

## Local setup

```bash
# 1. Clone the project
cd complaint-reply-tool

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate   

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set your API key
cp .env.example .env
# Edit .env and add your Groq key

# 5. Run
python app.py
