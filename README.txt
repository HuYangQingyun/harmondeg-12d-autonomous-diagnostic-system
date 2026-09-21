HARMONDEG 12-D AUTONOMOUS DIAGNOSTIC SYSTEM v1.0 Official GitHub Release
Package Package Version: 1.0.0 Research Reference Only

1.  WHAT THIS SYSTEM IS

Harmondeg 12-D is an autonomous structural diagnostic system for
examining the internal structure, boundaries, dependencies,
applicability, and consequence-mapping of human intellectual works.

The system is built from the Harmondeg Twelve-Dimensional Structural
Evaluation Framework developed by Qingyun Hu-Yang. Its purpose is
structural diagnosis rather than ideological judgment, truth
arbitration, popularity ranking, or value endorsement.

The core rule is the Stone Principle: Identify the structural condition
that is present. Do not turn structural diagnosis into a verdict about
whether the target is good or bad, desirable or undesirable, acceptable
or unacceptable.

The diagnostic sequence is: Source Material → Evidence Intake → Semantic
Reconstruction → D1-D12 Entry Gates → Primary and Boundary Tests →
Evidence Sufficiency → Cross-Dimensional Adjudication → Score / IE /
N/A + Confidence → Theory-Boundary Reconstruction → Integrated
Structural Conclusion → Diagnostic Self-Audit → Final DOCX Report

A user does not need to pre-fill D1-D12 judgments.

2.  THE TWELVE DIMENSIONS

D1 Level Collapse D2 Scope Overreach D3 Definition Drift D4 Observer
Ambiguity D5 Temporal Flattening D6 Hidden Premises D7 Category
Confusion D8 Self-Reference Loops D9 Context Erasure D10 Language
Reification and Infinitization D11 Operational Viability D12 Consequence
Mapping

Orientation dimensions: D1-D5. Structural diagnosis dimensions: D6-D10.
Practical evaluation dimensions: D11-D12.

3.  SCORING AND EVIDENCE STATES

Scores use an eleven-level scale from -5 to +5.

Positive scores require evidence of active structural management. Mere
absence of a defect does not earn a positive score.

0 means the dimension was evaluated and no significant positive or
negative structural condition was established.

IE means Insufficient Evidence. The dimension may apply, but the
available evidence does not support a reliable determination.

N/A means Not Applicable under the declared target and scope.

Confidence is reported independently as High, Medium, or Low.

The raw sum is only a Supplementary Structural Indicator. It does not
determine the integrated diagnosis.

A -5 Critical Failure requires all three: Core Relevance Structural
Dependence Failure Consequence

4.  CROSS-DIMENSIONAL DISCIPLINE

Related Diagnosis does not imply Duplicate Penalty.

The same evidence may support more than one dimension only when each
dimension diagnoses a distinct structural mechanism.

The system distinguishes: Source Structural Condition Derived Structural
Effect Associated Structural Condition Structural Propagation

A propagated effect must not be presented as an independent source
defect without evidence.

5.  OPERATING MODES

Mode A — Offline / Closed Evidence The diagnostic run uses only locally
supplied source material and available local semantic intelligence.

Mode B — AI-Assisted Closed-Source A compatible semantic model analyzes
a fixed evidence packet without web retrieval.

Mode C — Web / Evidence-Extended External retrieval is intentional and
disclosed. Retrieved material must enter the evidence basis before
diagnosis.

Internet access is never implicit.

The result identity is: Target + Scope + Evidence Basis + Operating
Mode + Framework Version.

6.  SEMANTIC INTELLIGENCE AND THE CANONICAL CORE

Harmondeg is the diagnostic architecture. Semantic intelligence is
replaceable.

Semantic intelligence may be supplied by: a human analyst, a compatible
language model, a local model, a future Harmondeg semantic layer, or a
hybrid process.

The canonical Harmondeg core remains fixed: D1-D12 identities, entry
gates, primary tests, boundary rules, diagnosis-before-scoring, the -5
to +5 scale, 0 / IE / N/A, confidence independence, Critical Failure
conditions, cross-dimensional adjudication, the Stone Principle, D11
work-relative applicability, D12 neutral consequence mapping, and the
research-reference boundary.

The included deterministic autonomous baseline is deliberately
conservative. Where deep semantic distinctions cannot be established
reliably, it returns IE rather than manufacturing a conclusion.

7.  SUPPORTED INPUT AND OUTPUT

Supported source input: TXT DOCX PDF

PDF input requires the optional pypdf dependency.

Primary output: diagnosis.json — machine-readable diagnostic state
report.docx — final human-readable report

Client-facing reports are DOCX.

8.  INSTALLATION

Recommended: Python 3.10 or newer.

Before running installation or diagnostic commands, extract the
downloaded ZIP package and open a terminal in, or change the terminal
directory to, the extracted project root:

Harmondeg_12D_Autonomous_Diagnostic_System_v1.0

Windows — Command Prompt or PowerShell: Use cd /d in Command Prompt when
the extracted folder is on another drive.

Example: cd /d C:_12D_Autonomous_Diagnostic_System_v1.0

In PowerShell, the standard cd command may be used: cd
“C:_12D_Autonomous_Diagnostic_System_v1.0”

macOS — Terminal: Example: cd
/path/to/Harmondeg_12D_Autonomous_Diagnostic_System_v1.0

Linux — Terminal: Example: cd
/path/to/Harmondeg_12D_Autonomous_Diagnostic_System_v1.0

The exact path depends on where the user extracted the downloaded
package. Paths containing spaces should be enclosed in quotation marks.

After entering the extracted project root, install the package:

pip install -e .

If the system uses python3/pip3 rather than python/pip, use: pip3
install -e .

For PDF input: pip install -e “.[pdf]”

For DOCX and PDF support: pip install -e “.[all]”

9.  QUICK START

Run the following command from the extracted project root.

Recommended command on Windows:

python -m harmondeg12d_public.cli diagnose
examples/quick_start/source.txt –target “Quick Start Demonstration”
–scope “Entire supplied source” –out output

Recommended command on macOS or Linux:

python3 -m harmondeg12d_public.cli diagnose
examples/quick_start/source.txt –target “Quick Start Demonstration”
–scope “Entire supplied source” –out output

If the command “python” is configured on macOS or Linux, the
Windows-style python command above is also valid.

The system writes: output/diagnosis.json output/report.docx

Windows note: On some Windows Python installations, pip installs
harmondeg12d.exe into the Python Scripts directory without adding that
directory to PATH. In that case, typing “harmondeg12d” directly may
produce a “not recognized” message even though Harmondeg was installed
successfully. The recommended “python -m harmondeg12d_public.cli …” form
above does not depend on the Scripts directory being on PATH.

If the Python Scripts directory is already on PATH, the shorter command
is also available:

harmondeg12d diagnose examples/quick_start/source.txt –target “Quick
Start Demonstration” –scope “Entire supplied source” –out output

Compatibility commands:

python -m harmondeg12d_public.cli validate diagnosis.json python -m
harmondeg12d_public.cli report diagnosis.json –out report.docx python -m
harmondeg12d_public.cli template –out template.json python -m
harmondeg12d_public.cli spec

When the Scripts directory is on PATH, the equivalent short forms are:
harmondeg12d validate diagnosis.json harmondeg12d report diagnosis.json
–out report.docx harmondeg12d template –out template.json harmondeg12d
spec

10. INCLUDED DEMONSTRATION SAMPLE

The examples/quick_start folder contains: source.txt — the exact input
supplied to the system. diagnosis.json — the autonomous structured
diagnostic result. report.docx — the corresponding human-readable
report.

The sample is included as a direct input/output comparison. Readers can
inspect the source first, then compare it with the system-generated
diagnostic state and final report.

11. SOURCE FIDELITY AND INPUT QUALITY

The accuracy and interpretive validity of a Harmondeg 12-D diagnosis
depend materially on the fidelity of the source material supplied to the
system. Input fidelity is part of diagnostic validity.

Whenever possible, users should provide primary-source material in the
original author’s or theory’s own wording, with enough surrounding
context to preserve intended meaning, argumentative structure,
conceptual relations, and the operative use of key terms. Complete
original works, relevant chapters, or continuous primary-source passages
are preferable to reconstructed summaries.

If a summary, paraphrase, excerpt, translation, or secondary
representation is used, it should reproduce the original position as
accurately and completely as possible within the declared scope.
Particular care should be taken with key terminology and expressions.
Changes in wording, including apparently minor changes in temporal,
categorical, modal, causal, definitional, observer-position, or
scope-related language, may change the structural signals detected by
the system and therefore affect the diagnostic result.

The system diagnoses the material actually supplied to it. A result
based on a summary, paraphrase, translation, excerpt, or secondary
representation is therefore a diagnosis of that supplied representation
within the declared scope. It should not automatically be attributed to
the complete original theory, author, work, or body of thought.

For higher-reliability analysis, use primary-source material, preserve
sufficient context, identify the source or edition where practicable,
and define the diagnostic scope explicitly.

12. PRODUCT AND COMMERCIAL STRUCTURE

The Harmondeg 12-D product architecture is designed around one canonical
diagnostic core with multiple use levels.

Level 1 — Public / Basic Edition Purpose: introductory structural
diagnosis, research reference, demonstration, education, and individual
testing. Core standards remain fixed.

Level 2 — Customized Personal Edition Purpose: licensed individual use
with configurable workflow, reporting, domain vocabulary, and user-side
preferences around the canonical core.

Level 3 — Professional Research Edition Purpose: sustained research,
advanced evidence handling, deeper semantic analysis, reproducibility,
batch work, calibration, and professional documentation.

Level 4 — Institutional / Enterprise Edition Purpose: organizational
deployment, controlled workflows, auditability, governance integration,
role-based use, scalable evidence handling, and institutional reporting.

Professional Diagnostic Service This is a service layer across product
levels rather than a separate fifth framework. It may provide structured
diagnostic work for clients who want a completed analysis rather than
operating the system independently.

The canonical core is not changed by product level. Commercial
customization occurs around workflow, semantic capability, integration,
reporting, scale, deployment, and service.

13. USE BOUNDARY AND RESPONSIBILITY

Harmondeg 12-D provides structural reference information.

It does not provide: legal judgments, regulatory decisions, judicial
findings, institutional certification, automatic truth/falsity verdicts,
ideological approval, or instructions about what a user must believe or
do.

Users remain responsible for interpretation and subsequent use.

There is no intellectual expiration date attached to a diagnostic
result, but every result is bounded by the framework version, diagnostic
target, declared scope, evidence basis, operating mode, and semantic
capability used at the time of analysis. A materially changed source,
scope, evidence packet, or system version may justify a new diagnostic
run.

14. THEORETICAL BASIS

The framework is a meta-framework for evaluating the structural
condition of intellectual works beyond precise quantification.

Its method proceeds from evidence to structural identification, then
dimension classification, dependency and severity analysis, scoring,
confidence, boundary reconstruction, cross-dimensional adjudication, and
integrated conclusion.

The twelve dimensions are not twelve independent rating questions. They
are coordinated diagnostic coordinates. Some structural conditions can
propagate across dimensions; some dimensions may remain neutral,
insufficiently evidenced, or inapplicable.

The framework is designed to preserve uncertainty rather than force
completeness. IE is therefore a legitimate diagnostic result.

D11 Operational Viability is relative to the target’s own intended
practical role. Pure theory should not be penalized for lacking an
implementation program it never claims to provide.

D12 Consequence Mapping diagnoses how consequences are identified and
traced when principles enter practice. It does not judge whether those
consequences are morally good or bad.

15. BOOKS AND REFERENCE CASES

The theoretical foundation is developed in:

The Twelve-Dimensional Structural Evaluation Framework: A Harmondeg
Meta-Framework for Evaluating Human Intellectual Works Beyond Precise
Quantification Volume One

The applied companion volume is:

The Framework in Practice: Six Structural Diagnostic Case Studies Volume
Two

The six reference case studies are: 1. Kant’s Critical Philosophy 2.
Rawls’s A Theory of Justice 3. Classical Philosophical Theology 4.
Quantum Mechanics and Its Interpretive Frameworks 5. The Hard Problem of
Consciousness 6. Musk’s First Principles Thinking

These cases illustrate application of the framework across philosophy,
political theory, philosophical theology, science and interpretation,
consciousness studies, and contemporary operational reasoning. They are
reference applications, not answer keys that new diagnoses must
reproduce.

Readers may search the exact book titles in their local Amazon
marketplace.

16. FEEDBACK AND RESEARCH COLLABORATION

The v1.0 release is intended to make the canonical Harmondeg diagnostic
method independently executable while preserving evidence discipline and
structural neutrality.

Feedback is especially welcome on: dimension boundaries, false positives
and false negatives, IE / 0 / N/A distinctions, cross-dimensional
propagation, semantic reconstruction, reproducibility, report clarity,
domain adaptation, and new blind-test cases.

Harmondeg Institute for Philosophy & Practice Qingyun Hu-Yang

17. RELEASE STATUS

Framework: Harmondeg 12-D Autonomous Diagnostic System v1.0

Package: 1.0.0

Status: Official GitHub Release Package

Research Reference Only.
