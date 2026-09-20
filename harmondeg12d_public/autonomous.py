import re, hashlib
from collections import Counter, defaultdict

DIMS={"D1":"Level Collapse","D2":"Scope Overreach","D3":"Definition Drift","D4":"Observer Ambiguity",
"D5":"Temporal Flattening","D6":"Hidden Premises","D7":"Category Confusion","D8":"Self-Reference Loops",
"D9":"Context Erasure","D10":"Language Reification and Infinitization","D11":"Operational Viability","D12":"Consequence Mapping"}

LIMITERS=("only","within","limited","scope","while","whenever","insofar","does not imply","not establish","exclude","except","under this","at this stage")
UNIVERSALS=("all","always","every","universal","necessarily","must","never","entire","complete")
FIRST=(" i "," me "," my "," myself ","we "," our ")
THIRD=(" he "," she "," they "," observer ","one ")
TEMPORAL=("before","after","while","whenever","then","now","present","past","future","stage","time","persist","continuity")
PRACTICAL=("implement","implementation","deploy","deployment","operational procedure","operational role","put into practice","practical aim","action pathway","intervention","execution mechanism","implementation mechanism")
CONSEQUENCE=("implementation consequence","downstream consequence","operational effect","secondary effect","reversibility","responsibility pathway","distributional consequence","cumulative effect")
PREMISE=("assume","assumption","presuppose","premise","given that","depends on","requires")
CATEGORY=("is a","becomes","identical","same as","constitutes","nothing but","kind of","category","substance","entity")
REP=("means","definition","concept","word","term","symbol","representation","language","equation","model")

def sentences(text):
    text=re.sub(r'\s+',' ',text.strip())
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+',text) if s.strip()]

def hits(ss, terms):
    return [(i+1,s) for i,s in enumerate(ss) if any(t in (" "+s.lower()+" ") for t in terms)]

def ev(hs,n=3):
    return " | ".join(f"S{i}: {s[:260]}" for i,s in hs[:n]) if hs else ""

def scored(score,conf,evidence,obs,impact,rationale,active=False):
    return {"status":"scored","score":score,"confidence":conf,"evidence":evidence or "No decisive passage-level trigger established.",
            "structural_observation":obs,"structural_impact":impact,"score_rationale":rationale,
            "active_management_evidence":active}

def ie(reason): return {"status":"IE","score":None,"confidence":None,"evidence":"","structural_observation":"","structural_impact":"","score_rationale":"","active_management_evidence":False,"rationale":reason}
def na(reason): return {"status":"N/A","score":None,"confidence":"High","evidence":"","structural_observation":"","structural_impact":"","score_rationale":"","active_management_evidence":False,"rationale":reason}

def reconstruct(text):
    ss=sentences(text); low=" "+text.lower()+" "
    terms=re.findall(r"\b[A-Za-z][A-Za-z'-]{3,}\b",text.lower())
    stop=set("this that with from have were been into their there which would could should about these those when then than also only does not are was for and the".split())
    freq=Counter(t for t in terms if t not in stop)
    return {
      "sentence_count":len(ss),
      "key_terms":[w for w,_ in freq.most_common(12)],
      "scope_limiters":hits(ss,LIMITERS),
      "universal_claims":hits(ss,UNIVERSALS),
      "first_person":hits(ss,FIRST),
      "third_person":hits(ss,THIRD),
      "temporal":hits(ss,TEMPORAL),
      "premise_markers":hits(ss,PREMISE),
      "category_markers":hits(ss,CATEGORY),
      "representation_markers":hits(ss,REP),
      "practical":hits(ss,PRACTICAL),
      "consequence":hits(ss,CONSEQUENCE),
      "sentences":ss
    }

def diagnose_text(text,target="User-supplied theory",scope="Entire supplied text",mode="AI-Assisted Closed-Source"):
    r=reconstruct(text); ss=r["sentences"]; d={}
    # D1 conservative: only flag explicit epistemic/ontological or theory/practice transitions
    lvl=[(i+1,s) for i,s in enumerate(ss) if any(x in s.lower() for x in ("epistem","ontolog","metaphys","empirical","normative","descriptive"))]
    d["D1"]=scored(0,"Medium",ev(lvl),"Potential level markers were reviewed; no unsupported cross-level transition is established automatically.","No independent structural effect assigned without a demonstrated transition.","Level vocabulary alone does not satisfy D1.")
    # D2
    if r["scope_limiters"]:
        score=2 if len(r["scope_limiters"])>=2 else 1
        d["D2"]=scored(score,"Medium",ev(r["scope_limiters"]),"Explicit scope-limiting language is present.","The text actively constrains at least part of its claimed range.","Positive score reflects active scope management, not mere absence of overreach.",True)
    elif len(r["universal_claims"])>=3:
        d["D2"]=scored(-1,"Low",ev(r["universal_claims"]),"Multiple broad quantifiers occur without detected local limiters.","A broader scope claim may exceed locally visible support.","Low-confidence candidate only; semantic review is required before stronger scoring.")
    else: d["D2"]=scored(0,"Medium",ev(r["universal_claims"]),"No significant supported-scope/claimed-scope mismatch is established.","No scope defect or active management sufficient for a nonzero score.","Evaluated as 0.")
    # D3 repeated key terms need semantic model; do not invent drift
    d["D3"]=ie("Lexical repetition can be detected autonomously, but operative meaning change cannot be established reliably by the deterministic baseline without a semantic adapter.")
    # D4
    if r["first_person"] and not r["third_person"]:
        d["D4"]=scored(2,"Medium",ev(r["first_person"]),"A stable first-person position is explicitly sustained in the supplied text.","Observer position is actively anchored.","Localized-to-clear observer management is present.",True)
    elif r["first_person"] and r["third_person"]:
        d["D4"]=ie("Multiple observer positions are present, but the baseline cannot determine whether transitions are unacknowledged or legitimate.")
    else: d["D4"]=scored(0,"Medium",ev(r["third_person"]),"No material observer-position ambiguity is established.","No significant observer defect or active management established.","Evaluated as 0.")
    # D5
    if len(r["temporal"])>=2 and r["scope_limiters"]:
        d["D5"]=scored(1,"Medium",ev(r["temporal"]),"Temporal distinctions co-occur with explicit limiting language.","Some active temporal bounding is visible.","Localized active temporal management.",True)
    elif r["temporal"]: d["D5"]=scored(0,"Medium",ev(r["temporal"]),"Temporal structure is present but no flattening is established.","Temporal vocabulary alone is not a defect.","Evaluated as 0.")
    else: d["D5"]=scored(0,"Low","","No material temporal structure is established from the supplied text.","No temporal diagnosis beyond 0 is warranted.","Conservative 0.")
    # D6
    if r["premise_markers"]:
        d["D6"]=scored(1,"Medium",ev(r["premise_markers"]),"The text explicitly marks assumptions/premises or dependency conditions.","Explicit premise disclosure is active structural management.","A disclosed premise is not a hidden premise.",True)
    else: d["D6"]=ie("No explicit premise marker was found, but hiddenness and structural necessity cannot be inferred from absence of markers alone.")
    # D7
    if r["category_markers"]:
        d["D7"]=ie("Category-transition language is present, but the baseline cannot determine whether an adequate bridge is supplied or whether categories are genuinely distinct.")
    else: d["D7"]=scored(0,"Low","","No material category transfer is established by the baseline.","No category defect is asserted.","Conservative 0.")
    # D8 strict loop gate
    loop=[(i+1,s) for i,s in enumerate(ss) if ("because" in s.lower() and "therefore" in s.lower())]
    d["D8"]=scored(0,"Medium",ev(loop),"No explicit P→C→P return edge is reconstructed from the supplied text.","Self-reference alone is not treated as circularity.","Strict loop gate prevents false-positive D8 scoring.")
    # D9
    ctx=[(i+1,s) for i,s in enumerate(ss) if any(x in s.lower() for x in ("context","histor","social","institution","culture","background","condition"))]
    d["D9"]=scored(0,"Low",ev(ctx),"Contextual material may be present or absent, but required-background dependency is not established automatically.","Deliberate abstraction is not treated as erasure.","Conservative 0 unless dependency can be reconstructed.")
    # D10
    if r["representation_markers"]:
        d["D10"]=ie("Representational/conceptual language is present, but identity between representation and represented reality is not established by lexical evidence alone.")
    else: d["D10"]=scored(0,"Low","","No representation–reality collapse is established.","No reification defect is asserted.","Conservative 0.")
    # D11/D12 applicability
    if not r["practical"]:
        d["D11"]=na("No declared or materially detectable practical/operational implementation role is present in the supplied text.")
        d["D12"]=na("No implementation/action pathway entering practice is present under the supplied scope.")
    else:
        if len(r["practical"])>=3:
            d["D11"]=scored(1,"Low",ev(r["practical"]),"A practical role is materially present; implementation language is explicit.","Operational structure is partially articulated.","Positive score is provisional because agents/resources/feedback require deeper semantic reconstruction.",True)
        else:
            d["D11"]=scored(0,"Low",ev(r["practical"]),"A practical role is present but operational completeness is not established.","D11 applies; no significant positive/negative condition is established.","Evaluated as 0.")
        if r["consequence"]:
            d["D12"]=scored(1,"Low",ev(r["consequence"]),"Implementation consequences are explicitly discussed.","Some consequence mapping is active.","Localized positive mapping; deeper completeness requires semantic review.",True)
        else:
            d["D12"]=scored(-1,"Low",ev(r["practical"]),"A practical pathway is present without detected consequence mapping.","Foreseeable consequence structure may be underdeveloped.","Low-confidence local deficiency.")
    # cross-dimensional adjudication
    source=[]; derived=[]; associated=[]; propagation=[]
    neg=lambda k: d[k]["status"]=="scored" and (d[k].get("score") or 0)<0
    # Conservative source/derived adjudication. A relation is emitted only when both
    # nodes are independently established; lexical co-occurrence never creates a defect.
    for k in ("D6","D7","D8","D9","D10"):
        if neg(k): source.append(k)
    for k in ("D1","D2","D3","D4","D5","D11","D12"):
        if neg(k): derived.append(k)
    if neg("D6") and neg("D7"):
        propagation.append({"from":"D6","to":"D7","strength":"Probable Structural Dependency",
                            "basis":"A hidden structurally operative condition and a separately established category transfer coexist."})
    if neg("D7") and neg("D1"):
        propagation.append({"from":"D7","to":"D1","strength":"Structural Association",
                            "basis":"A category transfer and a cross-level transition are independently established."})
    if neg("D1") and neg("D2"):
        propagation.append({"from":"D1","to":"D2","strength":"Structural Association",
                            "basis":"A cross-level transition and a supported/claimed scope mismatch are independently established."})
    negs=[k for k in d if neg(k)]
    for i,k in enumerate(negs):
        for j in negs[i+1:]:
            if k not in source and j not in derived and not any(x["from"]==k and x["to"]==j for x in propagation):
                associated.append([k,j])
    # boundaries
    positives=[k for k,v in d.items() if v["status"]=="scored" and v["score"]>0]
    negatives=[k for k,v in d.items() if v["status"]=="scored" and v["score"]<0]
    ies=[k for k,v in d.items() if v["status"]=="IE"]
    nas=[k for k,v in d.items() if v["status"]=="N/A"]
    key=", ".join(r["key_terms"][:6]) or "No stable key-term set extracted"
    conclusion={
      "theory_position":f"The supplied text is treated as the diagnostic target under the declared scope. Dominant extracted terms include: {key}.",
      "foundational_evidential_basis":f"The run uses only the supplied source ({r['sentence_count']} segmented sentences). No external evidence is introduced.",
      "supported_explanatory_domain":"The supported domain is limited to claims and structural relations recoverable from the supplied source. The autonomous baseline does not extend findings beyond that evidence packet.",
      "application_boundary":"Any dimension requiring semantic distinctions not securely recoverable by the deterministic baseline is marked IE rather than guessed.",
      "major_explanatory_strengths":("Active structural management was detected in: "+", ".join(positives)) if positives else "No dimension received a positive score without explicit active-management evidence.",
      "unresolved_structural_conditions":("Insufficient-evidence dimensions: "+", ".join(ies)) if ies else "No IE dimensions.",
      "evidential_status":f"Closed-source autonomous run. N/A dimensions: {', '.join(nas) if nas else 'none'}. Confidence is reported independently from score.",
      "overall_structural_profile":f"Autonomous profile: positive={positives or 'none'}; negative={negatives or 'none'}; IE={ies or 'none'}; N/A={nas or 'none'}. This profile is structural, not an evaluative verdict.",
      "reference_use_boundary":"Research-reference result only; subsequent interpretation and use remain the user's responsibility."
    }
    audit=self_audit(d)
    return {"framework_version":"Harmondeg 12-D Autonomous Diagnostic System v1.0","target":target,"scope":scope,"operating_mode":mode,
            "external_evidence_used":False,"evidence_basis":"User-supplied source only",
            "evidence_packet_hash":hashlib.sha256(text.encode()).hexdigest(),
            "semantic_reconstruction":{k:v for k,v in r.items() if k!="sentences"},
            "dimensions":d, "cross_dimensional_adjudication":{"source_conditions":source,"derived_effects":derived,"associated_conditions":associated,"propagation":propagation},
            "integrated_conclusion":conclusion,"self_audit":audit}

def self_audit(dims):
    findings=[]
    for k,v in dims.items():
        if v["status"]=="scored" and v["score"]>0 and not v.get("active_management_evidence"):
            findings.append(f"{k}: positive score lacks active-management evidence")
        if k=="D8" and v["status"]=="scored" and v["score"]<0:
            findings.append("D8: negative score requires explicit P→C→P provenance review")
        if k in ("D11","D12") and v["status"]=="scored" and v["confidence"]=="High":
            findings.append(f"{k}: autonomous baseline should not assign High confidence without full implementation reconstruction")
    return {"passed":not findings,"findings":findings}

# attach dimension display names
_old=diagnose_text
def diagnose_text(text,target='User-supplied theory',scope='Entire supplied text',mode='AI-Assisted Closed-Source'):
    x=_old(text,target,scope,mode)
    for k,v in x['dimensions'].items(): v['name']=DIMS[k]
    return x
