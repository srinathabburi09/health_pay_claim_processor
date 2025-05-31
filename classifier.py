import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_document_by_content(text: str) -> str:
    prompt = f"""
You are a document classification assistant. Based on the following text extracted from a healthcare document, classify it as one of the following:
•⁠  ⁠"bill"
•⁠  ⁠"discharge_summary"
•⁠  ⁠"id_card"
•⁠  ⁠"unknown"

Text:
{text[:2000]}  # limit to 2000 chars

Respond with only the classification keyword.
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You classify documents based on content."},
            {"role": "user", "content": prompt}
        ]
    )

    classification = response.choices[0].message.content.strip().lower()

    allowed = {"bill", "discharge_summary", "id_card", "unknown"}
    return classification if classification in allowed else "unknown"