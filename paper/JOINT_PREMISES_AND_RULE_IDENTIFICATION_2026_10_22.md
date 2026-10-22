# Joint premises, observed resultants and rule identification

## Bounded knowledge for SSK interpretation and reentry

Date: 22 October 2026. Receiving owner: SSK Paper competence + Editoriali.
Status: operator-selected research supplement and receiving-competence learning.
This develops the [20 October D-ND contribution](DND_RELATIONAL_CONTINUITY_AND_REPRESENTATIONAL_SUFFICIENCY_2026_10_20.md), rather than introducing a second account of continuity. The stable 0.12 manuscript and existing integration candidate 0.13 are unchanged by this supplement. The public receiving text is self-contained; the full D-ND research notes and private operational records are not imported.

The useful addition is a distinction between **preserving the conditions of a consequence** and **identifying those conditions from an observed consequence**. SSK already preserves source roles, occurrence, interpretation and later exercise. The examples below make a particular loss and a particular discriminating question inspectable. They do not define D-ND, SSK, KA or FDLA as a rule engine.

## 1. What the previous contribution established

The existing contribution distinguishes information sufficient for selected outcomes, autonomous updating of a representation, and actually exercised continuity. Its support example already distinguishes alternative reasons from jointly necessary premises. These are acquired relations, not new discoveries in this supplement.

The present development applies them to two different problems:

- **Forward:** with statements, rules and update semantics given, calculate their consequences.
- **Inverse:** with selected consequences observed, determine which rule hypotheses remain compatible and what further information could distinguish them.

An exact solution of the forward problem does not by itself solve the inverse problem. A trace can preserve an occurrence without identifying a mechanism.

## 2. A finite construction preserving joint premises

Let U be a finite set of contextually identified statements. A rule is P -> q, where the nonempty premise set P is a subset of U and q belongs to U. All premises must be jointly available. The rules Q remain fixed during a calculation; premises are not consumed and there is no negation or retraction.

For an initial set R, define a synchronous update:

```text
S_0 = R
S_(n+1) = S_n union {q : (P -> q) belongs to Q and P is a subset of S_n}
```

Write C_Q(R) for its stabilized set. Each strict step adds at least one member of U not previously present, so there are at most |U minus R| strict steps. The resulting set is Q-closed. If Z is any Q-closed set containing R, induction gives S_n subset Z at every step; thus C_Q(R) is the least such set. Extensivity, monotonicity in the initial premises and idempotence follow. This is an elementary finite positive-rule closure, not a claim that arbitrary cognitive or adaptive processes converge.

Take U={a,b,c,d,e} and Q_J={ {a,b}->c, {c}->d }. Then

```text
C_QJ({a}) = {a}
C_QJ({b}) = {b}
C_QJ({a,b}) = {a,b,c,d}
```

Hence C_QJ({a}) union C_QJ({b}) is strictly smaller than C_QJ({a,b}). The joint availability of a and b enables a consequence that neither enables alone; c then becomes a premise for d. If the joint rule is replaced by the two ordinary edges a->c and b->c, the representation falsely makes either premise sufficient: from {a} it reaches {a,c,d}.

The defect belongs to that replacement, not to every graphical representation. A directed hypergraph or an AND-aware graph can preserve a joint requirement. HALP's B-Visit documentation explicitly requires all nodes of an edge's tail before traversal; the documentation was read, but HALP was not installed or executed here [1]. The letters above denote available statements in a specified context, not merely familiar concept names.

### Local closure does not close the inquiry

Adding {d}->e changes Q and yields {a,b,c,d,e} from {a,b}. The earlier result remains the correct closure for the earlier rules. The closure calculation does not explain why a new rule should be introduced or whether it is justified. Retraction, changing meanings, consumable resources or a changing rule set require their own semantics; the fixed-Q argument does not transfer automatically.

## 3. The same observed trace need not identify a rule

Compare Q_J with Q_S={ {a}->c, {c}->d }, using the same universe and synchronous update semantics. Starting from {a,b}, both produce the entire trace

```text
{a,b} -> {a,b,c} -> {a,b,c,d}
```

Here the observation records the successive sets, not rule labels or rule bodies. It cannot determine whether b was necessary for c: the joint and single-premise hypotheses yield identical observed data.

**Exact limit.** Any procedure given only that same observation receives the same input under either hypothesis. It cannot guarantee selection of the true rule hypothesis in both cases. Additional assumptions, a labelled derivation, actual implementation evidence or another observation can change the information available. This is not a general impossibility of identifying rules, nor a statement about hidden LLM cognition.

Now use the initial set {a}:

```text
Q_J: {a}
Q_S: {a} -> {a,c} -> {a,c,d}
```

This input distinguishes the two declared hypotheses. It does not uniquely identify a theory among all possible theories. Both traces were calculated from stipulated models; neither is a measurement of a real cognitive system. In a real receiver, whether an analogous discriminating observation is available, meaningful and authorized is a separate situated question.

Learning Horn formulas through queries has a specific precedent in Angluin, Frazier and Pitt [2]. Only the publisher's abstract and bibliographic metadata were consulted. The closure-input query used here is not automatically their membership query over Boolean assignments; their algorithm, oracles and complexity guarantees are not transferred to SSK.

## 4. Availability is different from selection weight

An optional uniform selection rule over C_Q(R) assigns a probability of 1 to a when the closure is {a}, and 1/4 when the closure is {a,b,c,d}. The statement a remains available under the rules although its relative selection weight decreases.

This elementary counterexample separates membership in a reachable set from a normalized selection distribution. The uniform law is stipulated for illustration. It is not the D-ND possibility field, an SSK competence-ranking rule, or a law of cognition. Without an explicitly selected probability model, no probability need be assigned to possibilities at all.

## 5. What returns to the SSK competence

When a doubt concerns the support of an inference, preserve the source's inferential role: alternative support, joint requirement and an already-derived premise are not interchangeable. A list of sources or edges alone may lose that role. Retain the material relation or make its actual recovery possible from the source; retaining a pointer alone does not establish recovery.

When a doubt concerns how an observed outcome was produced, distinguish the occurrence from the candidate mechanism. Agreement on one output, or even on an unlabelled trace, is not identification. Where the difference matters, seek the smallest additional source relation or observation that separates the live alternatives. Where it does not affect the selected work, qualified continuation or no_change can be sufficient. This is not a demand to invent competing hypotheses or run a test before every movement.

When a receiver uses the Paper for orientation, the Paper supplies explicit reasoning, assumptions and scope. It does not substitute its representation for the actual owner, operation or controller. A proved finite case can improve how a question is formed; it does not certify that an active system has already read, exercised or assimilated the method. The existing competence reference carries this return, rather than a new supervisor, invariant or mandatory pipeline.

A concise receiving formulation is:

> A resultant may be sufficient to preserve what happened without uniquely identifying the rule that produced it. Its useful continuation can consist in making a distinguishing question possible. Preserve the occurrence, retain the attributed alternatives when material, and let their different consequences guide the next situated inquiry without preselecting its conclusion.

This paragraph is the receiving interpretation, not a quotation from the D-ND authorial archive or a derivation of the general origin of questions.

## 6. Verification and claim state

The [standard-library script](checks/verify_joint_premises_and_rule_identification.py) was executed locally by the receiving ChatGPT turn on 22 October 2026. Its [recorded output](checks/joint_premises_and_rule_identification_results.json) verifies the stated joint/single traces, the incorrect edge projection, the changed-rule result, the optional rational weights and the closure properties on all 32 seed sets and all 243 ordered inclusion pairs of the five-statement universe. It also checks that an unseeded two-rule cycle generates no statements.

These checks belong to this receiving script. They are not an independent empirical replication, the separate 512-theory enumeration from earlier preparatory work, a Lab run or a performance benchmark. The proofs and explicit constructions above establish the limited mathematical claims; the enumeration only checks the declared finite cases.

| Relation | Status | What it does not establish |
| --- | --- | --- |
| Positive-rule closure and the AND/edge distinction | Explicit definitions, proof and finite checks | A definition of the D-ND or SSK field |
| Same trace under two rule hypotheses | Constructed and checked counterexample to unique identification from that observation | Impossibility of every identification procedure |
| The {a} contrast | Distinguishes the two stipulated hypotheses | A unique real-world mechanism or all possible theories |
| Availability versus uniform selection weight | Exact conditional example | A prescribed probabilistic ontology |
| Receiving SSK method | Source-qualified interpretive return to an existing competence | Automatic later exercise, assimilation or efficacy |
| Repository reception | Research supplement and discovery/competence links | Manuscript promotion, runtime installation, peer review or academic publication |

## 7. Sources, rights and receiving boundary

The contributing preparatory notes are *D-ND — Dalla relazione fra risultati all'accessibilita inferenziale* and *D-ND — Dalla risultante alle regole: che cosa distingue una ricostruzione?*, both 22 October 2026. This operator-selected public development transfers only their bounded constructions and useful receiving interpretation. It does not reproduce their private source excerpts, task identifiers, controller prompts or other operational records. Their interpretive relation to the D-ND source remains distinct from mathematical proof.

The existing public [20 October receiving development](DND_RELATIONAL_CONTINUITY_AND_REPRESENTATIONAL_SUFFICIENCY_2026_10_20.md), especially sections 2, 3, 6 and 7, supplies the SSK continuity and dependency relation reused here. Canonical manuscript and publication states remain those selected in [STATE](../STATE.md). This supplement neither changes stable 0.12 nor edits or promotes candidate 0.13.

[1] Murali Group, HALP primary documentation, `halp.algorithms.directed_paths.b_visit`, accessed 22 October 2026: https://murali-group.github.io/halp/docs/_build/html/halp.algorithms.html . Read for its stated all-tail-premises traversal semantics, not as a run of the library or a reading of the complete Gallo et al. article.

[2] Dana Angluin, Michael Frazier and Leonard Pitt, *Learning Conjunctions of Horn Clauses*, Machine Learning 9, 147–164 (1992), DOI 10.1023/A:1022689015665: https://link.springer.com/article/10.1023/A:1022689015665 . Publisher abstract and metadata accessed 22 October 2026; full article and algorithm not claimed as read or reproduced.

KA/FDLA remain operator-owned invariants. MM_D-ND, the living Kernel, SSK runtime projects, other repositories, scheduled tasks, products, websites and publication channels are not modified by this receiving contribution.
