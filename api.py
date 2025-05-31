from fastapi import APIRouter, UploadFile, File
from typing import List
from app.services.classifier import classify_document_by_content
from app.services.extractor import extract_text
from app.agents.bill_agent import BillAgent
from app.agents.discharge_agent import DischargeAgent
from app.agents.id_agent import id_agent
from app.services.validator import validate_claim
from app.services.decision import make_decision

router = APIRouter()

@router.post("/process-claim")
async def process_claim(files: List[UploadFile] = File(...)):
    documents = []

    for file in files:
        contents = await file.read()
        text = await extract_text(contents)
        doc_type = classify_document_by_content(text)

        if doc_type == "bill":
            structured = BillAgent().process(text)
        elif doc_type == "discharge_summary":
            structured = DischargeAgent().process(text)
        elif doc_type == "id_card":
            structured = id_agent().process(text)
        else:
            continue

        documents.append(structured)

    validation = validate_claim(documents)
    decision = make_decision(documents, validation)

    return {
        "documents": documents,
        "validation": validation,
        "claim_decision": decision
    }