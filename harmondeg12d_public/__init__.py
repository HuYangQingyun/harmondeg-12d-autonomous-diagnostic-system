__version__ = "1.0.0"
from .autonomous import diagnose_text
from .validator import validate
from .template import make_template
from .ingest import read_source
from .docx_report import render_docx

def load_dimensions_spec():
    import json
    from pathlib import Path
    return json.loads((Path(__file__).parent / "spec" / "dimensions.json").read_text(encoding="utf-8"))
