import fitz

async def extract_text(pdf_bytes: bytes) -> str:
    doc = fitz.open("pdf", pdf_bytes)
    return "\n".join([page.get_text() for page in doc])
