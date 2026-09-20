
from pathlib import Path
def read_source(path):
    p=Path(path); ext=p.suffix.lower()
    if ext in (".txt",".md"):
        return p.read_text(encoding="utf-8")
    if ext==".docx":
        from docx import Document
        d=Document(str(p))
        return "\n".join(x.text for x in d.paragraphs if x.text.strip())
    if ext==".pdf":
        try:
            from pypdf import PdfReader
        except ImportError:
            raise RuntimeError("PDF input requires pypdf.")
        return "\n".join((page.extract_text() or "") for page in PdfReader(str(p)))
    raise ValueError("Supported source formats: .txt, .docx, .pdf")
