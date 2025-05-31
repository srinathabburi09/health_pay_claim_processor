from .base import BaseAgent
import os
from openai import OpenAI
import json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class BillAgent(BaseAgent):
    def process(self, text: str) -> dict:
        prompt = f"""
You are an intelligent data extraction agent. Based on the bill text below, extract structured JSON data in this exact schema:

{{
  "type": "bill",
  "hospital_name": string,
  "patient_name": string,
  "ip_no": string or int,
  "total_amount": float,
  "gst": float,
  "total_with_gst": float,
  "services": [{{"name": string, "amount": float}}],
  "company": string,
  "date_of_service": string (format: YYYY-MM-DD to YYYY-MM-DD)
}}

Bill Text:
{text[:3000]}
"""

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a healthcare billing parser."},
                {"role": "user", "content": prompt}
            ]
        )

        try:
            result = response.choices[0].message.content.strip()
            return json.loads(result)
              # ✅ Note: you can also use ⁠ json.loads() ⁠ if you wrap LLM output in triple quotes
        except Exception as e:
            return {
                "type": "bill",
                "error": f"Failed to parse bill content: {str(e)}"
            }