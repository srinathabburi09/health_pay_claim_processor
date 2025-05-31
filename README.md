# health_pay_claim_processor
HealthPay Claim Processor is an AI-powered FastAPI application designed to automate the ingestion, classification, extraction, and structuring of medical claim documents such as:
	•	Hospital bills
	•	Discharge summaries
	•	Patient ID cards
It leverages OpenAI and Google Gemini Pro APIs to intelligently parse unstructured text (PDFs), extract essential information, and output standardized JSON schemas ready for storage or further decision-making workflows like insurance claims or analytics.
classifier.py - GPT-3.5 / Gemini Pro - Classify the document type: bill, discharge_summary, id_card, etc.
BillAgent - GPT-3.5 / Gemini Pro - Extract billing info into structured JSON (e.g., services, amount, GST).
DischargeAgent - GPT-3.5 / Gemini Pro - Extract patient treatment summary (diagnosis, dates, prescription).
IdAgent - GPT-3.5 / Gemini Pro - Extract ID information such as name, DOB, gender, address.

PROJECT ARCHITECTURE:
📁 healthpay_claim_processor_github_ready/
│
├── app/
│   ├── main.py             # FastAPI app entry point
│   ├── api.py              # HTTP endpoint `/process-claim`
│   ├── services/
│   │   ├── classifier.py   # Classifies document content using LLM
│   │   └── agents/
│   │       ├── base.py     # BaseAgent interface
│   │       ├── bill_agent.py
│   │       ├── discharge_agent.py
│   │       └── id_agent.py
│   ├── schemas.py          # Pydantic models for input/output
│   └── utils.py            # Helpers (e.g., PDF parsing)
│
├── requirements.txt        # Dependencies
├── README.md               # Project description, logic, architecture (this file)
└── .env                    # API keys for OpenAI and Gemini (not committed)

Workflow Logic
	1.	User uploads a PDF
	2.	utils.py extracts the raw text
	3.	classifier.py sends text to LLM → returns: "bill", "discharge_summary", "id_card"
	4.	Based on result, the corresponding agent:
	•	BillAgent
	•	DischargeAgent
	•	IdAgent
processes the text
	5.	Extracted info is returned in JSON format via /process-claim API

REQUIREMENTS
fastapi
uvicorn
openai
google-generativeai
python-dotenv
PyMuPDF
pydantic
python-multipart
requests

HOW TO RUN
# Activate virtual env
source .venv/bin/activate

# Run the FastAPI app
python -m uvicorn app.main:app --reload

# Visit docs
http://127.0.0.1:8000/docs

#Environment Variables
OPENAI_API_KEY=your-openai-api-key
GOOGLE_API_KEY=your-gemini-api-key

Sample Output

{
  "type": "bill",
  "hospital_name": "Max Healthcare",
  "patient_name": "Mrs. Nandi Rawat",
  "total_amount": 332602.59,
  "gst": null,
  "services": [
    {"name": "Blood Bank", "amount": 12387.00},
    {"name": "Drugs", "amount": 28286.22}
  ]
}
