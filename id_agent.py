from .base import BaseAgent
import os
from openai import OpenAI
import json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class id_agent(BaseAgent):
    def process(self, text: str) -> dict:
        prompt = f"""
You are an intelligent ID parser. From the following text extracted from an ID document, return structured JSON like this:

{{
  "type": "id_card",
  "name": string,
  "dob": string (format: YYYY-MM-DD),
  "gender": string (if available),
  "address": string
}}

ID Document Text:
{text[:3000]}
"""

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You extract ID card details."},
                    {"role": "user", "content": prompt}
                ]
            )
            result = response.choices[0].message.content.strip()
            return json.loads(result)
        except Exception as e:
            return {
                "type": "id_card",
                "error": f"Failed to parse ID document: {str(e)}"
            }