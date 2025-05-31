def make_decision(documents: list, validation: dict) -> dict:
    if validation["missing_documents"]:
        return {
            "status": "rejected",
            "reason": "Missing required documents"
        }
    return {
        "status": "approved",
        "reason": "All required documents present and data is consistent"
    }
