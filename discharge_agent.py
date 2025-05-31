from .base import BaseAgent
import os
from openai import OpenAI
import json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class DischargeAgent(BaseAgent):
    def process(self, text: str) -> dict:
        prompt = f"""
You are an intelligent healthcare document parser. Extract the following discharge summary information from the text and return as JSON:

{{
  "type": "discharge_summary",
  "patient_name": string,
  "diagnosis": string,
  "surgery": string (if mentioned),
  "admission_date": string (format YYYY-MM-DD),
  "discharge_date": string (format YYYY-MM-DD),
  "hospital": string,
  "consultants": [string],
  "prescription": [string],
  "physiotherapy": [string]
}}

Discharge Summary Text:
{text[:3000]}
"""

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You extract structured medical discharge summary data."},
                    {"role": "user", "content": prompt}
                ]
            )
            result = response.choices[0].message.content.strip()
            return json.loads(result)
        except Exception as e:
            return {
                "type": "discharge_summary",
                "error": f"Failed to parse discharge summary: {str(e)}"
            }