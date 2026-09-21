HARMONDEG 12-D AUTONOMOUS DIAGNOSTIC SYSTEM v1.0
Official GitHub Release Package
Package Version: 1.0.0
Research Reference Only

1. WHAT THIS SYSTEM IS

Harmondeg 12-D is an autonomous structural diagnostic system for examining the internal structure, boundaries, dependencies, applicability, and consequence-mapping of human intellectual works.

The system is built from the Harmondeg Twelve-Dimensional Structural Evaluation Framework developed by Qingyun Hu-Yang. Its purpose is structural diagnosis rather than ideological judgment, truth arbitration, popularity ranking, or value endorsement.

The core rule is the Stone Principle:
Identify the structural condition that is present. Do not turn structural diagnosis into a verdict about whether the target is good or bad, desirable or undesirable, acceptable or unacceptable.

The diagnostic sequence is:
Source Material
→ Evidence Intake
→ Semantic Reconstruction
→ D1-D12 Entry Gates
→ Primary and Boundary Tests
→ Evidence Sufficiency
→ Cross-Dimensional Adjudication
→ Score / IE / N/A + Confidence
→ Theory-Boundary Reconstruction
→ Integrated Structural Conclusion
→ Diagnostic Self-Audit
→ Final DOCX Report

A user does not need to pre-fill D1-D12 judgments.

2. THE TWELVE DIMENSIONS

D1  Level Collapse
D2  Scope Overreach
D3  Definition Drift
D4  Observer Ambiguity
D5  Temporal Flattening
D6  Hidden Premises
D7  Category Confusion
D8  Self-Reference Loops
D9  Context Erasure
D10 Language Reification and Infinitization
D11 Operational Viability
D12 Consequence Mapping

Orientation dimensions: D1-D5.
Structural diagnosis dimensions: D6-D10.
Practical evaluation dimensions: D11-D12.

3. SCORING AND EVIDENCE STATES

Scores use an eleven-level scale from -5 to +5.

Positive scores require evidence of active structural management. Mere absence of a defect does not earn a positive score.

0 means the dimension was evaluated and no significant positive or negative structural condition was established.

IE means Insufficient Evidence. The dimension may apply, but the available evidence does not support a reliable determination.

N/A means Not Applicable under the declared target and scope.

Confidence is reported independently as High, Medium, or Low.

The raw sum is only a Supplementary Structural Indicator. It does not determine the integrated diagnosis.

A -5 Critical Failure requires all three:
Core Relevance
Structural Dependence
Failure Consequence

4. CROSS-DIMENSIONAL DISCIPLINE

Related Diagnosis does not imply Duplicate Penalty.

The same evidence may support more than one dimension only when each dimension diagnoses a distinct structural mechanism.

The system distinguishes:
Source Structural Condition
Derived Structural Effect
Associated Structural Condition
Structural Propagation

A propagated effect must not be presented as an independent source defect without evidence.

5. OPERATING MODES

Mode A — Offline / Closed Evidence
The diagnostic run uses only locally supplied source material and available local semantic intelligence.

Mode B — AI-Assisted Closed-Source
A compatible semantic model analyzes a fixed evidence packet without web retrieval.

Mode C — Web / Evidence-Extended
External retrieval is intentional and disclosed. Retrieved material must enter the evidence basis before diagnosis.

Internet access is never implicit.

The result identity is:
Target + Scope + Evidence Basis + Operating Mode + Framework Version.

6. SEMANTIC INTELLIGENCE AND THE CANONICAL CORE

Harmondeg is the diagnostic architecture. Semantic intelligence is replaceable.

Semantic intelligence may be supplied by:
a human analyst,
a compatible language model,
a local model,
a future Harmondeg semantic layer,
or a hybrid process.

The canonical Harmondeg core remains fixed:
D1-D12 identities,
entry gates,
primary tests,
boundary rules,
diagnosis-before-scoring,
the -5 to +5 scale,
0 / IE / N/A,
confidence independence,
Critical Failure conditions,
cross-dimensional adjudication,
the Stone Principle,
D11 work-relative applicability,
D12 neutral consequence mapping,
and the research-reference boundary.

The included deterministic autonomous baseline is deliberately conservative. Where deep semantic distinctions cannot be established reliably, it returns IE rather than manufacturing a conclusion.

7. SUPPORTED INPUT AND OUTPUT

Supported source input:
TXT
DOCX
PDF

PDF input requires the optional pypdf dependency.

Primary output:
diagnosis.json — machine-readable diagnostic state
report.docx — final human-readable report

Client-facing reports are DOCX.

8. INSTALLATION

Recommended:
Python 3.10 or newer.

From the downloaded package directory:

pip install -e .

For PDF input:
pip install -e ".[pdf]"

For DOCX and PDF support:
pip install -e ".[all]"

9. QUICK START

Recommended cross-platform command:

python -m harmondeg12d_public.cli diagnose examples/quick_start/source.txt --target "Quick Start Demonstration" --scope "Entire supplied source" --out output

The system writes:
output/diagnosis.json
output/report.docx

Windows note:
On some Windows Python installations, pip installs harmondeg12d.exe into the Python Scripts directory without adding that directory to PATH. In that case, typing "harmondeg12d" directly may produce a "not recognized" message even though Harmondeg was installed successfully. The recommended "python -m harmondeg12d_public.cli ..." form above does not depend on the Scripts directory being on PATH.

If the Python Scripts directory is already on PATH, the shorter command is also available:

harmondeg12d diagnose examples/quick_start/source.txt --target "Quick Start Demonstration" --scope "Entire supplied source" --out output

Compatibility commands:

python -m harmondeg12d_public.cli validate diagnosis.json
python -m harmondeg12d_public.cli report diagnosis.json --out report.docx
python -m harmondeg12d_public.cli template --out template.json
python -m harmondeg12d_public.cli spec

When the Scripts directory is on PATH, the equivalent short forms are:
harmondeg12d validate diagnosis.json
harmondeg12d report diagnosis.json --out report.docx
harmondeg12d template --out template.json
harmondeg12d spec

10. INCLUDED DEMONSTRATION SAMPLE

The examples/quick_start folder contains:
source.txt — the exact input supplied to the system.
diagnosis.json — the autonomous structured diagnostic result.
report.docx — the corresponding human-readable report.

The sample is included as a direct input/output comparison. Readers can inspect the source first, then compare it with the system-generated diagnostic state and final report.

11. PRODUCT AND COMMERCIAL STRUCTURE

The Harmondeg 12-D product architecture is designed around one canonical diagnostic core with multiple use levels.

Level 1 — Public / Basic Edition
Purpose: introductory structural diagnosis, research reference, demonstration, education, and individual testing.
Core standards remain fixed.

Level 2 — Customized Personal Edition
Purpose: licensed individual use with configurable workflow, reporting, domain vocabulary, and user-side preferences around the canonical core.

Level 3 — Professional Research Edition
Purpose: sustained research, advanced evidence handling, deeper semantic analysis, reproducibility, batch work, calibration, and professional documentation.

Level 4 — Institutional / Enterprise Edition
Purpose: organizational deployment, controlled workflows, auditability, governance integration, role-based use, scalable evidence handling, and institutional reporting.

Professional Diagnostic Service
This is a service layer across product levels rather than a separate fifth framework. It may provide structured diagnostic work for clients who want a completed analysis rather than operating the system independently.

The canonical core is not changed by product level. Commercial customization occurs around workflow, semantic capability, integration, reporting, scale, deployment, and service.

12. USE BOUNDARY AND RESPONSIBILITY

Harmondeg 12-D provides structural reference information.

It does not provide:
legal judgments,
regulatory decisions,
judicial findings,
institutional certification,
automatic truth/falsity verdicts,
ideological approval,
or instructions about what a user must believe or do.

Users remain responsible for interpretation and subsequent use.

There is no intellectual expiration date attached to a diagnostic result, but every result is bounded by the framework version, diagnostic target, declared scope, evidence basis, operating mode, and semantic capability used at the time of analysis. A materially changed source, scope, evidence packet, or system version may justify a new diagnostic run.

13. THEORETICAL BASIS

The framework is a meta-framework for evaluating the structural condition of intellectual works beyond precise quantification.

Its method proceeds from evidence to structural identification, then dimension classification, dependency and severity analysis, scoring, confidence, boundary reconstruction, cross-dimensional adjudication, and integrated conclusion.

The twelve dimensions are not twelve independent rating questions. They are coordinated diagnostic coordinates. Some structural conditions can propagate across dimensions; some dimensions may remain neutral, insufficiently evidenced, or inapplicable.

The framework is designed to preserve uncertainty rather than force completeness. IE is therefore a legitimate diagnostic result.

D11 Operational Viability is relative to the target's own intended practical role. Pure theory should not be penalized for lacking an implementation program it never claims to provide.

D12 Consequence Mapping diagnoses how consequences are identified and traced when principles enter practice. It does not judge whether those consequences are morally good or bad.

14. BOOKS AND REFERENCE CASES

The theoretical foundation is developed in:

The Twelve-Dimensional Structural Evaluation Framework:
A Harmondeg Meta-Framework for Evaluating Human Intellectual Works Beyond Precise Quantification
Volume One

The applied companion volume is:

The Framework in Practice:
Six Structural Diagnostic Case Studies
Volume Two

The six reference case studies are:
1. Kant's Critical Philosophy
2. Rawls's A Theory of Justice
3. Classical Philosophical Theology
4. Quantum Mechanics and Its Interpretive Frameworks
5. The Hard Problem of Consciousness
6. Musk's First Principles Thinking

These cases illustrate application of the framework across philosophy, political theory, philosophical theology, science and interpretation, consciousness studies, and contemporary operational reasoning. They are reference applications, not answer keys that new diagnoses must reproduce.

Readers may search the exact book titles in their local Amazon marketplace.

15. FEEDBACK AND RESEARCH COLLABORATION

The v1.0 release is intended to make the canonical Harmondeg diagnostic method independently executable while preserving evidence discipline and structural neutrality.

Feedback is especially welcome on:
dimension boundaries,
false positives and false negatives,
IE / 0 / N/A distinctions,
cross-dimensional propagation,
semantic reconstruction,
reproducibility,
report clarity,
domain adaptation,
and new blind-test cases.

Harmondeg Institute for Philosophy & Practice
Qingyun Hu-Yang

16. RELEASE STATUS

Framework:
Harmondeg 12-D Autonomous Diagnostic System v1.0

Package:
1.0.0

Status:
Official GitHub Release Package

Research Reference Only.
