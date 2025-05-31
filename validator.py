def validate_claim(documents: list) -> dict:
    missing = []
    required = ["bill", "discharge_summary","id_card"]
    present = {doc["type"] for doc in documents}
    for r in required:
        if r not in present:
            missing.append(r)
    return {
        "missing_documents": missing,
        "discrepancies": []
    }
