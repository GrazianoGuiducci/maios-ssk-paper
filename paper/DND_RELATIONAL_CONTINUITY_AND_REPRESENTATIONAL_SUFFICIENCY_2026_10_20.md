# Relational continuity and representational sufficiency

## A bounded D-ND contribution to SSK reentry and revision

Date: 20 October 2026. Research and editorial owner: SSK Paper competence + Editoriali. Source: Graziano Guiducci, *D-ND: distinzione relazionale e continuita della risultante*, manuscript 1.0, 20 October 2026, §§2–6. The source manuscript is completed as a working text, not an independently reviewed or academically published result. This development makes the selected contribution readable here without publishing the complete private D-ND corpus.

Integration target: [SSK candidate 0.13](SYSTEM_SEMANTIC_KERNEL_SSK_WORKING_PAPER_0_13_CANDIDATE.md), particularly §§2.2, 3.2, 3.6–3.7 and its claim-state ledger. [Stable 0.12](SYSTEM_SEMANTIC_KERNEL_SSK_WORKING_PAPER_0_12.md) remains unchanged. The D-ND manuscript, this receiving interpretation, a later kernel exercise and academic publication are distinct objects and events.

## 1. The relation already present in SSK, and the added precision

SSK already distinguishes the continuum carrying still-causal relations from continuity emerging when those relations participate in subsequent work. It already explains why keeping only a conclusion can lose the reason for revising it, and why reachable depth need not be continuously active. These are not newly introduced claims.

The D-ND contribution gives one part of that relation an exact, bounded expression: a representation is sufficient for selected continuations only when it does not identify situations whose outcomes those continuations need to distinguish. It also separates sufficient information about selected outcomes from autonomous updating of every detail in the representation.

This is a mathematical account of a declared representation, not a mathematical definition of SSK, of integrative contraction, or of the whole possibility field. SSK's integrative contraction is not renamed compression. A proof that information could support continuation is not evidence that a receiver actually retrieved, understood or used it.

## 2. Exact continuation under declared operations

Let X be a set, h: X → H the observations to preserve, and E a set of labels for deterministic total operations U_e: X → X. For a finite word w=e_1…e_n, let U_w=U_{e_n}∘…∘U_{e_1}; the empty word ε has U_ε=id_X. Write E* for all these words. Define

```text
x ~_(h,E) x'  iff  h(U_w(x)) = h(U_w(x')) for every w in E*.
```

**Proposition.** This is the coarsest equivalence relation that preserves h and is stable under every U_e. On the quotient, both the output h_hat([x])=h(x) and the update U_hat_e([x])=[U_e(x)] are well defined. A representation π: X → Y determines all selected outcomes h∘U_w exactly if and only if

```text
π(x) = π(x')  implies  x ~_(h,E) x'.
```

**Proof.** Equality of all the outputs gives an equivalence relation. The empty word guarantees preservation of h. If x and x' are equivalent, then for every word w the outputs of U_w∘U_e coincide, because applying e and then w is another finite word. Hence U_e(x) and U_e(x') are equivalent. If F is any other h-preserving equivalence stable under the operations, induction on word length shows that x F x' implies U_w(x) F U_w(x') and therefore equality of all h-outputs. Thus F is contained in ~_(h,E). Finally, each output h∘U_w factors through π precisely when it is constant on every fibre of π; applying this to every word proves the last assertion. □

For finite X and finite E, repeatedly refine the h-partition by the blocks of each successor U_e(x). Each strict refinement increases the number of blocks. From k initial blocks, at most |X|−k strict refinements can occur; the stable partition is the equivalence above. This does not supply a finite procedure for arbitrary infinite sets, unknown operations or partially observed states.

The proposition is ordinary mathematics of behavioural quotients, demonstrated here for its precise use. No priority for that mechanism, optimal byte count, general semantic metric or reduction of model latency is claimed.

### Outcomes are not the entire representation

Knowing all h∘U_w does not imply that π itself admits updates S_e with π∘U_e=S_e∘π. For that stronger property, the fibres of π must be stable under every operation. A refinement of the canonical quotient may add information whose successor values π cannot determine.

For example, take X={0,1,2,3}, T(x)=x+1 modulo 4 and h(x)=x modulo 2. Parity predicts all its future parity values. The richer representation π(x)=(h(x),1{x=0}) still predicts all parity values but merges states 1 and 3. Their successors 2 and 0 have different π-values, so π is not autonomously updateable. If both components are selected as future observations, all four states must be distinguished. The earlier parity prediction remains correct.

For SSK reentry this separates three questions: what outcomes an entry can answer, what stored representation it can update, and what a receiver actually does with it. None can inherit the evidence of another by sharing the word continuity.

## 3. A conclusion can lose the distinctions needed to revise it

Assume two identified supports s1 and s2, each sufficient alone under a declared rule. A state is the set of supports still usable:

```text
X = {empty, {s1}, {s2}, {s1,s2}}
C(x) = 1 when x is nonempty; otherwise 0
U_i(x) = x without s_i
```

The value 1 means supported under this rule, not true in the world; 0 is not the negation of the proposition. No probabilities or statistical independence are assumed.

| Available supports | C(x) | C(U_1(x)) | C(U_2(x)) |
| --- | ---: | ---: | ---: |
| none | 0 | 0 | 0 |
| s1 only | 1 | 0 | 1 |
| s2 only | 1 | 1 | 0 |
| s1 and s2 | 1 | 1 | 1 |

The same present conclusion is compatible with different revisions after removing s1. C alone cannot implement that update. For U_1 alone, three classes suffice: empty, {s1}, and the block containing {s2} and {s1,s2}. The representation (C(x),1{s2 in x}) updates as (a,b) → (b,b). When U_2 is also admitted, all four states must be distinguished.

Names alone may still be insufficient: a∨b and a∧b cite the same two supports and agree at a=b=1, but disagree after a=0,b=1. Their inferential role matters. Green, Karvounarakis and Tannen's *Provenance Semirings* (PODS 2007, §§3–4, DOI 10.1145/1265530.1265535) is a direct precedent for alternative and joint contributions. This Boolean example is not a new provenance calculus or an empirical SSK benchmark.

An entry can keep a distinction directly or make its recovery possible from its actual source. A pointer alone does not constitute recovery. What is enough depends on the selected continuation; the model does not prescribe retaining every past detail or pre-enumerating all future questions.

## 4. Founding relation, occurrence and validity

The D-ND manuscript distinguishes a founding assumption, the occurrence of a resultant, and the justification of a derived statement. A source invariant can orient work without certifying every later representation produced by a receiver. Correcting that representation can preserve the founding relation rather than edit it.

For SSK this deepens the existing distinction between operator-owned KA/FDLA invariants and revisable receiver comprehension. It does not redefine those invariants, import a general fallibilist interpretation into every historical source, or add a reviewer above the movement. A textual attribution needs its own correspondence; a derivation needs its stated premises; a measured claim needs evidence of that particular event.

## 5. A bounded source-attribution case

The selected D-ND source comparison is identified by MM_D-ND snapshot 8de33070e65783a30e1c51e4e3037684255f984f. The primary corpus has blob d90b5f975faf78f42994dce0e9495e9a7f040c60; the historical Paper D draft 3 has blob 50ce814a0a0e5b69231908cf8ac9bb8563123482. These are provenance coordinates, not a promise that a public reader has access to the private archive.

At NID 557, dated 30 October 2023 in the corpus, the source continues after “rumore di fondo” with “e deve essere considerata come ciò che è”. Cluster 7 of the historical draft instead inserts further sentences into the attributed quotation, including “Ogni elaborazione successiva introduce entropia”, and dates the NID December 2023. NID 566, dated 1 November 2023, explicitly instructs rereading “prima di generarla”. This temporal qualifier concerns composition before emitting the response, not an already formulated general rule for revising an emitted document.

The comparison establishes a non-literal attribution in the identified draft. It does not establish deceptive intent or the absence of the inserted sentence from every other archive. The manuscript's methodological interpretation is a further present inference: the source's first-impression language coexists with elaboration, rather than universally excluding it. Its stronger language about truth and axiomaticity remains attributed, not silently rewritten.

What changes after the comparison is the use of the derived passage. Its occurrence remains documentable; the literal attribution is withdrawn. A different source supporting the general content would not repair that exact attribution. The correction follows the dependency of the claim instead of invalidating every neighbouring topic.

The question may then change from quotation accuracy to the relation between first impression and rereading. That continuation is motivated by the recovered source relation and the research intent; it is not deduced from the error alone. A task limited to attribution could correctly stop after the correction. This is a documentary case with an interpretive consequence, not a controlled test of agent performance, hidden cognition or autonomous learning.

## 6. Conditions of continuation are not exercised continuity

The three relations proposed in the D-ND manuscript are a reconstructible reference, distinctions sufficient to the considered continuation, and intelligible reasons for the transformation. They expose different possible losses: a formally adequate state may have the wrong referent; an exact quotation may omit the dependency needed for revision; a new question may lack a justified relation to the work from which it claims to continue.

SSK retains its stronger operational question: do those relations actually participate in the following event and change understanding, action or competence when material? A saved guide and a proved quotient make conditions available. An observed subsequent use is a different claim. No automatic inference to assimilation, improved performance or continuous cognition follows from the integration of this note.

## 7. Receiving-competence learning

When revising the SSK argument, preserve the difference between output sufficiency, autonomous state update and exercised continuation. When a source or representation changes, follow the exact dependency before revising a conclusion. A readback validates the represented artifact at its own level; it does not transfer that closure to the next receiver, semantic contraction or empirical claim.

Apply the result where the object makes it useful. Do not turn the quotient into a required SSK architecture, a gate before inquiry, or a demand to inventory all future operations. The Paper competence retains this method through its existing guide; the D-ND and SSK research owners remain distinct.

## Claim boundary

- Mathematical proposition: proved under deterministic total operations and declared observations; no novel-mathematics priority claim.
- Finite cases: fully specified illustrative models; executable checks can verify these cases, not the whole theory.
- Documentary case: bounded textual comparison; present interpretation and historical source remain distinct.
- SSK integration: candidate research development; neither promotion of stable 0.12 nor runtime/assimilation evidence.
- Distribution: this selected research note does not publish the complete D-ND manuscript, private conversations, controller configurations or other owners' records.
