
import argparse,json,sys
from pathlib import Path
from .validator import validate
from .template import make_template
from .models import FRAMEWORK_VERSION, PACKAGE_VERSION
from .autonomous import diagnose_text
from .ingest import read_source
from .docx_report import render_docx

def load(path): return json.loads(Path(path).read_text(encoding="utf-8"))

def main():
    ap=argparse.ArgumentParser(prog="harmondeg12d",description=f"Harmondeg 12-D Autonomous Diagnostic System v1.0 ({PACKAGE_VERSION})")
    ap.add_argument("--version",action="version",version=f"%(prog)s {PACKAGE_VERSION}")
    sub=ap.add_subparsers(dest="cmd",required=True)

    p=sub.add_parser("diagnose",help="Autonomously diagnose TXT/DOCX/PDF and generate JSON + DOCX report")
    p.add_argument("source"); p.add_argument("--target",default="User-supplied theory"); p.add_argument("--scope",default="Entire supplied text")
    p.add_argument("--out",required=True)

    p=sub.add_parser("validate",help="Validate a diagnostic JSON file"); p.add_argument("input"); p.add_argument("--strict-meta",action="store_true")
    p=sub.add_parser("report",help="Generate a DOCX report from validated diagnostic JSON"); p.add_argument("input"); p.add_argument("--out",required=True); p.add_argument("--strict-meta",action="store_true")
    p=sub.add_parser("template",help="Write an empty diagnostic JSON template"); p.add_argument("--out",required=True)
    sub.add_parser("spec",help="Print path to machine-readable dimension specification")
    args=ap.parse_args()

    if args.cmd=="diagnose":
        text=read_source(args.source); data=diagnose_text(text,args.target,args.scope)
        out=Path(args.out); out.mkdir(parents=True,exist_ok=True)
        jp=out/"diagnosis.json"; rp=out/"report.docx"
        jp.write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n",encoding="utf-8"); render_docx(data,rp)
        print(rp); return
    if args.cmd=="template":
        Path(args.out).write_text(json.dumps(make_template(),indent=2,ensure_ascii=False)+"\n",encoding="utf-8"); print(args.out); return
    if args.cmd=="spec":
        print((Path(__file__).parent/"spec"/"dimensions.json").resolve()); return
    data=load(args.input); errs=validate(data,strict_meta=getattr(args,"strict_meta",False))
    if errs:
        print("Validation failed:",file=sys.stderr)
        for e in errs: print("- "+e,file=sys.stderr)
        raise SystemExit(2)
    if args.cmd=="validate": print(f"VALID — {FRAMEWORK_VERSION} input conforms to the package schema.")
    else:
        if not str(args.out).lower().endswith(".docx"): raise SystemExit("Report output must be .docx")
        render_docx(data,args.out); print(args.out)
if __name__=="__main__": main()
