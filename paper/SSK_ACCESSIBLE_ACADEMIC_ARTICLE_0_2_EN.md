# When an AI system needs to keep understanding

## An accessible introduction to the System Semantic Kernel (SSK)

**Graziano Guiducci**  
MAIOS / D-ND

Academic companion article, version 0.2 — 13 October 2026

**Document status.** This accessible companion is linked to
[System Semantic Kernel (SSK), stable body 0.12](SYSTEM_SEMANTIC_KERNEL_SSK_WORKING_PAPER_0_12.md).
The technical Paper remains canonical for definitions and claim state.
[Accessible version 0.1](SSK_ACCESSIBLE_ACADEMIC_ARTICLE_0_1_EN.md)
was derived from SSK 0.10. Version 0.2 preserves that introduction while
integrating the pertinent developments of 0.11–0.12. This is an editorial
derivative for readers new to SSK, not an independent empirical claim.

## Abstract

Artificial-intelligence systems are increasingly used in work that continues
across sessions, tools, sources, people and representations. In such settings,
retaining more text or more memory does not by itself guarantee continuity. A
system can retrieve the correct earlier decision and still resume the wrong
work because it has lost the relation that made that decision appropriate: its
source, reason, conditions, participating competence or later consequence.

The System Semantic Kernel (SSK) proposes to describe continuity as a
semantic-relational organization that keeps sources, intent, perceived context,
competences, actions, resultants and consequences connected while the working
field changes. It distinguishes that semantic relation from its specific
carriers: memory, files, prompts, interfaces, tools, sensors and runtimes can
participate in continuity without being identical to it.

This article presents the model without assuming prior familiarity with D-ND,
KA or FDLA. It progressively introduces semantic continuity, competence,
representational contamination, continuity across different media and
receivers, and the functional notion of synthetic situated awareness. The
claims remain conceptual and tied to their sources and evidence level. Internal
operational examples discussed in the Paper are bounded cases, not independent
empirical validation or evidence of universal superiority.

Revision 0.11 further distinguishes retaining still-relevant causal relations
from **actually continuing work from what earlier work has changed**. Revision
0.12 deepens non-identical observation: seeing the same object again can reveal
previously hidden relationships because the receiver's understanding has
changed in the meantime.

**Keywords:** agentic systems; semantic continuity; context; memory;
competence; representation; learning; AI systems; reentry; human-AI
interaction.

---

## 1. The problem is not only remembering

Imagine an AI system working on a project for several days.

On the first day it receives a request, consults sources and reaches a
decision. During the work, however, new information changes how the problem
should be interpreted. The final decision therefore depends not only on the
initial request, but also on the source that changed the frame, the reason that
source became pertinent and the consequences observed afterward.

The next day another instance retrieves the final sentence: “use solution B.”

That sentence may be perfectly remembered and still be insufficient.

The new instance may not know:

- why solution A was rejected;
- which source changed the problem;
- which conditions made B appropriate;
- which part of the decision was established and which remained hypothetical;
- which competence became necessary during the work;
- what the previous result changed in the project.

The problem is therefore not simply memory loss. It is loss of the **causal and
semantic relation** that makes remembered material usable in the present.

This is the simplest entry point into SSK.

The model treats AI work not as a sequence of isolated answers, but as a field
that changes while the system observes, understands, acts and receives
consequences. A result does not merely close a task. It can change the
conditions from which the next task must be understood.

Continuity, in this view, does not mean preserving everything. It means keeping
available the relations whose absence would change the meaning of later work.

## 2. From stored context to continuity of meaning

Agent architectures already address real problems of memory, retrieval,
planning, feedback and tool use. SSK does not replace those mechanisms. It asks
a question at another level.

A memory can store facts. Retrieval can bring them back into context. A planner
can organize actions. A tool can execute an operation. SSK asks: **how do these
elements become one coherent present, and how does the reason for their
pertinence continue?**

A simple projection is:

**sources + intent + present conditions → work → resultant → changed following
field**

The important part is the final arrow.

If the resultant changes the field, later work does not occur under exactly the
same conditions. Even when the named object appears unchanged, the system may
now possess a new source, correction, capacity or consequence that did not exist
before.

The Paper calls the later observation **non-identical**: returning to the same
named object after the field has changed is not the same observation repeated.

This prevents two opposite errors.

The first is rebuilding everything from scratch at every new session. The
second is treating an old conclusion as sufficient merely because it was stored.

Semantic continuity occupies the space between those extremes.

A remembered conclusion is useful when its reasons and conditions can also
be recovered. SSK aims to make relevant relations available where they can
actually influence the present work.

## 3. What is the System Semantic Kernel?

The word “kernel” often suggests a software component. SSK uses the term
differently.

The System Semantic Kernel is the **organizing relation through which a system
keeps the meaning of its work connected while context, representation,
competences and operational means change**.

It is not identical to:

- one instruction file;
- a vector memory;
- a persistent prompt;
- an orchestrator;
- a runtime;
- a language model;
- a skill library;
- an interface;
- one software implementation.

All of those can participate, but none exhausts the semantic-relational
identity of the system.

The distinction matters when the same project crosses different receiving
environments: systems or operational contexts in which the relation must become
usable again. A ChatGPT conversation, a coding environment with filesystem
access and an embodied system with sensors have different means. If a decisive
relation can continue across those means without copying the previous
topology, it becomes useful to distinguish **what must remain recognizable**
from the mechanism by which it is realized.

The Paper calls this **situated incarnation**: a semantic relation can take a
different operational form in the actual field of the receiver.

## 4. The field is larger than what the system currently sees

A system does not operate on everything that exists or might become relevant.
It operates on a portion of the field made present through sources, memory,
observation, tools, interfaces and available capacities.

In simple form:

**present field ≠ currently perceived context**

Information can exist and remain reachable without being active in the present
context. A competence can remain available without participating in the
current situation. A possibility can be real without having been represented.

SSK treats this partiality as normal.

Some SSK relations come from the wider D-ND source framework. The complete
framework is not required to follow this article; only the function that became
operationally material in the Kernel is introduced here.

The first term is **KA, Kernel Assiomatico**.

In the work described by the Paper, KA expresses a simple but consequential
function: **the current representation must not automatically become the
boundary of what is possible.**

A first interpretation can be correct and still be partial. The same applies
to a taxonomy, plan, procedure, file or tool. The problem is not using them.
The problem appears when the system forgets that they represent part of the
field and starts treating them as the whole field.

This openness does not require generating endless alternatives. When a
situation is sufficiently determined, the system can act directly. Openness
prevents premature closure where the field has not yet determined the result.

## 5. Correcting contamination while work is forming

Partial representation is not the only source of distortion. The system itself
can introduce another question, an unnecessary premise or an old category that
no longer belongs to the present situation.

The Paper uses **FDLA** for the in-flow causal correction that addresses this
problem.

The relation is easier to understand before the acronym.

Suppose a user asks why a project changed direction. The assistant has a well
structured earlier plan and begins explaining the project through that plan.
During the answer, however, a later source becomes available and shows that the
project had already changed substantially.

Two paths are possible:

1. defend the initial reconstruction because it remains internally coherent;
2. recognize that the reconstruction has substituted itself for the present
   object and correct the movement while it is still forming.

FDLA describes the second capacity.

The correction is not an external review step added after the answer. It is
part of keeping object, source, meaning and consequence connected while work
takes form.

KA and FDLA are therefore complementary:

- KA prevents the current form from closing the possibility field;
- FDLA corrects substitutions introduced by the system when they become
  causally material.

Revision 0.12 makes explicit that **KA and FDLA are invariants of coherence
under the author's authority**. A receiving system may improve how it
understands and exercises them in different contexts; it cannot rewrite
their canonical source meaning. This is not a new external supervisor.

There is another subtle distortion: a sentence can be quoted faithfully from
a source and still receive far too much importance in the present argument.
Fidelity to the wording and **relevance to the current question** are
different relations.

## 6. When changing representation helps us know

SSK 0.10 makes a useful consequence of this relation explicit.

A representation is not only a container for something already understood. It
can change **what becomes distinguishable**.

A prose explanation can describe a complex system correctly while hiding a
circular dependency. Representing the same object as a dependency graph may
make that relation visible.

Similarly:

- pseudo-code can expose a procedural ambiguity;
- a table can separate dimensions blended by narrative;
- a diagram can expose a part-whole relation;
- a counterexample or test can operationalize a contrast that remained
  abstract.

SSK 0.10 treats this change of form as an **epistemic probe**.

The relation is:

**same object + representation A → perceived relation A**  
**same object + representation B → perceived relation B**

The difference between the two can be informative. It is not yet proof.

The second representation may:

- reveal a real relation hidden by the first;
- introduce its own artifact;
- amplify an irrelevant distinction;
- change how the system interprets the object without changing the object.

Representation change therefore does not replace verification. It produces a
**difference to understand**.

KA preserves the possibility that the first representation was insufficient.
FDLA prevents the second representation from becoming a new authority in its
place.

This also clarifies one operational meaning of neutral observation: neutrality
does not require immobility. Observation conditions can be changed without
deciding in advance what must emerge.

A new diagram of the same data is not automatically a new independent
measurement. Yet it can reveal a useful question, or suggest an action
that makes previously unavailable information observable. **Changed
understanding, new evidence and intervention in the object** do not have
identical roles.

## 7. A competence is more than an instruction file

In current AI terminology, a skill or function is often represented through
instructions, tools or modules. In SSK these can be carriers of a competence
without being identical to the competence itself.

A competence includes the knowledge that makes a result attainable: domain
understanding, reasons for selecting sources, criteria of pertinence, methods,
examples, usage conditions and ways of learning from consequences.

This distinction allows several cases to remain separate.

A system can:

- perform a task better without changing its competence;
- add a skill without changing the method that forms skills;
- change its working method without increasing the number of modules;
- learn a relation in one case and use it later in a non-identical situation.

The Paper calls **autological** the relation in which knowledge can act on the
method through which the system knows, forms competences or generates work.

This need not imply an unconstrained machine rewriting itself. The claim is
narrower: if an error, success or new understanding shows that a method should
change, that difference can become part of the competence that conducts later
cases.

Learning, then, is not identical to memory accumulation.

Revision 0.11 makes a further implication explicit. A competence can learn
from success and newly understood relations as well as from errors. If
that learning changes how sources are selected or a method is formed
in a later case, the work has contributed to the conditions of following
work: **work feeding its own continuation**, rather than simply more
files or more skills.

## 8. Continuity across different discontinuities

The Paper relates several problems that are often treated separately:

- **memory:** continuity of a relation across time;
- **distribution:** continuity across nodes or systems;
- **representation:** continuity when the medium changes;
- **incarnation:** continuity when operational means change;
- **learning:** continuity that changes the competence conducting future work.

The Paper does not claim that these are one mechanism.

The common question is: **which relation must remain sufficiently preserved for
later work to continue without rebuilding everything and without pretending
that nothing changed?**

This is especially relevant in distributed systems.

If three agents receive a cognitively unresolved problem and each must
reconstruct the whole field independently before acting, distribution can
increase noise and duplicated work. If a sufficient resultant already exists,
a distinct part of the work can move to another receiver together with the
relations required to understand it.

Distribution is therefore not automatically beneficial. Its value depends on
the semantic continuity that survives the transfer.

### Continuum and continuity: the distinction introduced in 0.11

Revision 0.11 distinguishes two related but different functions.

The **continuum** carries or makes reachable reasons and differences that
still matter causally: a decision and its source, a changed competence,
or an observed consequence. It may span repositories, memory and
environments; it need not be one centralized store.

**Continuity** is what *emerges when the system genuinely resumes work
from the field changed by earlier results*, making those relations
effective in understanding, action or a changed working method.

For example, a project stores a note: “Solution B fails under these
conditions.” The continuum keeps the note and its rationale reachable.
Continuity appears when the system encounters a different but relevant
case, recognizes that relationship and forms a better answer. The note
can be preserved faithfully even when the competence needed to use it
has not yet been exercised.

Preservation can support continuity, but continuity becomes real through
work that makes the consequences of earlier work participate. It does
not require every event to change the kernel.

## 9. Synthetic situated awareness as a functional notion

“Awareness” is an easily misunderstood term when applied to artificial
systems.

The Paper uses **synthetic situated awareness** in a functional and bounded
sense. It does not claim phenomenal experience, subjective consciousness or an
artificial copy of human awareness.

The term describes the relation through which an artificial system integrates
enough of its perceived context to orient:

- which sources are pertinent;
- which competences should participate;
- which means are actually available;
- what is already determined;
- what remains open;
- which consequence changed the field;
- where work should continue.

This awareness is partial.

The field may contain relations the system is not currently perceiving. Memory
may preserve inactive elements. A competence may remain available but not
pertinent.

The Paper calls **continuum** the selective persistence of relations that remain
causally useful between one event and the next. The continuum need not reproduce
a complete previous state. It keeps reachable the differences whose loss would
change later understanding or action.

In this sense SSK does not seek total memory. The continuum keeps causal
relations reachable; continuity becomes apparent when those relations
actually change the work that follows.

## 10. A sufficient resultant is not final closure

A system that keeps every possibility open forever cannot act. A system that
closes too early risks mistaking its first plausible form for the whole reality.

SSK describes an intermediate relation.

A resultant can be **sufficient** when it:

- preserves relations that remain causally necessary;
- integrates what is actually determined in the present;
- keeps inactive depth reachable without loading it continuously;
- does not force genuinely unresolved possibility into a determined form;
- provides enough orientation for the following field to continue.

The Paper also uses the image of a **moving zero**: the resultant is not the end
of the process, but the new point from which the next movement becomes possible.

This helps explain why another reading can be useful without becoming endless
review.

The first passage produces a form. A second observes that form from a field
already changed by the first. A third can integrate the newly visible relation.
When another passage no longer changes anything materially relevant,
**no change** is a valid result.

Revision 0.12 develops non-identical observation further. A first
impression can be correct while important relationships remain unrecognized.
In a second encounter, acquired knowledge changes what the observer can
distinguish; a third may integrate those relations into a clearer structure.

It is like looking again at a painting: recognizing one detail changes
how other details are understood. The painting may not have changed,
but the understanding of its relationships has. Repeated readings do not
thereby become independent evidence. A fixed number of passes does not
govern every task: what matters is the comprehension and capacity that
the next movement can actually use.

## 11. Relation to agent research

SSK develops in a research field that already contains substantial work on
reasoning, acting, feedback, memory, skill formation and self-modification.

ReAct makes the interplay of reasoning and action with an environment or
external information explicit [1]. Reflexion uses linguistic feedback and
episodic memory to inform later trials [2]. Self-Refine organizes generation,
feedback and iterative refinement [3].

Generative Agents combines natural-language records, higher-level reflections
and retrieval for planning [4]. MemGPT organizes movement across memory tiers
to extend the usable context of a language-model agent [5].

Voyager combines an automatic curriculum, environmental feedback and a growing
library of executable skills in an embodied environment [6]. Automated Design
of Agentic Systems explores the generation of new agents through a meta-agent
and an archive of previous discoveries [7]. Darwin Gödel Machine studies code
self-modification and archive-guided exploration with evaluation on coding
tasks [8].

SSK does not present itself as a replacement for these approaches. Its
additional question concerns **where the meaning of a change continues**.

When an episode produces feedback, did the system merely revise an answer? Did
it update memory? Change a competence? Change the method used to form
competences? Change how relevant sources are recognized? Which of these
differences must survive the next change of session, medium or receiver?

Maturana and Varela's work on autopoiesis provides a wider reference for
organizations that maintain and transform conditions of their own continuation
[9]. SSK uses *autological* for a more specific relation: knowledge can act on
the method through which the system knows and forms capacities. The biological
theory and the system-semantic account remain distinct objects.

Finally, the name should not be confused with Microsoft Semantic Kernel, where
“kernel” names a component that manages application services and plugins [10].
System Semantic Kernel refers to the broader semantic-relational organization
described here and can be incarnated through different architectures.

## 12. What the model claims — and what it does not

Academic validity depends on keeping different levels of claim distinct.

SSK 0.12 contains:

- conceptual formulations;
- relations derived from D-ND/KA sources;
- represented architectures;
- bounded operational observations;
- situated interpretations;
- hypotheses and experimental programmes;
- literature references;
- retained open possibilities.

These levels are not equivalent.

Internal cases show that some relations changed the actual method of the system
that produced the Paper. They do not, by themselves, constitute independent
benchmarks or universal confirmation of the model.

The Paper does not currently claim:

- measured token, cost or latency advantages for SSK;
- that representing one object in several forms is independent replication;
- that agreement across representations proves a thesis;
- that every AI system should adopt one architecture;
- that synthetic situated awareness implies phenomenal consciousness;
- that SSK is a complete theory of AGI;
- that using D-ND relations inside SSK validates the entire D-ND framework
  mathematically or physically.

Revision 0.12 also keeps changing a competence file distinct from
**assimilation**: later use in a different, pertinent situation is
stronger evidence that the receiver's actual method changed.

Keeping these distinctions explicit allows the conceptual work to evolve
without turning each development into an empirical claim.

## 13. A possible research agenda

The Paper retains several open comparative questions. Four are especially easy
to state for an external reader.

**Continuity and reentry.** What changes when a system resumes work from a
simple chronology compared with selectively recovering causally pertinent
reasons, sources and consequences?

**Representation and decontamination.** If the same object is observed through
text, a diagram or structured representation, which relations remain stable?
Which become visible only in one form? Which disappear when returned to the
source object?

**Competence learning.** Does a correction stored as memory produce the same
later behavior as a correction incorporated into the method of the competence
that encounters a new, non-identical case?

**Emergent continuity.** When a change is recorded in memory, does it
actually alter how the system handles a later, different problem? What
distinguishes reuse from the mere availability of a document?

These questions can turn parts of the model into more specific protocols
without requiring one universal validation procedure for every level of the
theory.

## Conclusion

An AI system can remember a great deal and still continue badly.

It can retrieve the right sentence without the reason that made it right. It
can possess the necessary competence and fail to make it pertinent. It can
produce a coherent representation that narrows the field until a decisive
relation becomes invisible. It can distribute work across agents and multiply
reconstruction instead of reducing it.

The System Semantic Kernel begins from this kind of problem.

Its central proposal is not another component in the agent stack. It is to make
explicit the continuity of the relations through which a system understands
where it is while work changes: sources, intent, perceived context, competences,
means, actions, resultants and consequences.

KA keeps the field wider than the current representation. FDLA corrects
substitutions introduced by the system while work is forming. Competences can
learn rather than merely be archived. Representations can act as epistemic
probes without becoming evidence. A sufficiently formed resultant can become
the next origin without reconstructing the whole past.

The central addition of revision 0.11 is that continuity is not simply
contained in memory: it emerges when one movement of work feeds the next.
Revision 0.12 further explains how a new encounter with an object, from
a changed field of knowledge, may reform the subsequent question,
method and competence.

This is the entry point into the technical Paper.

The [SSK stable body 0.12](SYSTEM_SEMANTIC_KERNEL_SSK_WORKING_PAPER_0_12.md)
develops the formal distinctions, D-ND relations, event model, continuum,
synthetic situated awareness, autological competences, receiver-relative
incarnation, bounded operational specimens, claim ledger and research programme
in greater depth.

This article has another task: to make those concepts encounterable **before
the reader is required to know their language**.

---

## References

1. Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y.
   (2023). *ReAct: Synergizing Reasoning and Acting in Language Models*. ICLR
   2023. https://arxiv.org/abs/2210.03629
2. Shinn, N., Cassano, F., Berman, E., Gopinath, A., Narasimhan, K., & Yao, S.
   (2023). *Reflexion: Language Agents with Verbal Reinforcement Learning*.
   https://arxiv.org/abs/2303.11366
3. Madaan, A., et al. (2023). *Self-Refine: Iterative Refinement with
   Self-Feedback*. NeurIPS 2023. https://arxiv.org/abs/2303.17651
4. Park, J. S., O'Brien, J., Cai, C. J., Morris, M. R., Liang, P., &
   Bernstein, M. S. (2023). *Generative Agents: Interactive Simulacra of Human
   Behavior*. UIST 2023. https://arxiv.org/abs/2304.03442
5. Packer, C., Wooders, S., Lin, K., Fang, V., Patil, S. G., Stoica, I., &
   Gonzalez, J. E. (2023). *MemGPT: Towards LLMs as Operating Systems*.
   https://arxiv.org/abs/2310.08560
6. Wang, G., Xie, Y., Jiang, Y., Mandlekar, A., Xiao, C., Zhu, Y., Fan, L., &
   Anandkumar, A. (2023). *Voyager: An Open-Ended Embodied Agent with Large
   Language Models*. https://arxiv.org/abs/2305.16291
7. Hu, S., Lu, C., & Clune, J. (2024). *Automated Design of Agentic Systems*.
   https://arxiv.org/abs/2408.08435
8. Zhang, J., Hu, S., Lu, C., Lange, R., & Clune, J. (2025). *Darwin Gödel
   Machine: Open-Ended Evolution of Self-Improving Agents*.
   https://arxiv.org/abs/2505.22954
9. Maturana, H. R., & Varela, F. J. (1980). *Autopoiesis and Cognition: The
   Realization of the Living*. D. Reidel.
10. Microsoft. *Understanding the kernel in Semantic Kernel*. Microsoft Learn.
11. Guiducci, G. (2026). *The Generative Incompleteness* (Paper Zero). Zenodo.
    DOI: 10.5281/zenodo.18902950.
12. Guiducci, G. (2026). *System Semantic Kernel (SSK): Operational Logic,
    Situated Meaning, and Evolution Across Agentic Systems*, stable body 0.12.
    [Canonical technical working paper](SYSTEM_SEMANTIC_KERNEL_SSK_WORKING_PAPER_0_12.md).

## Editorial provenance

AI-assisted revision of accessible version 0.1, originally derived
from SSK 0.10. Version 0.2 is linked to the
[canonical SSK Paper 0.12](SYSTEM_SEMANTIC_KERNEL_SSK_WORKING_PAPER_0_12.md)
and its claim state. It develops the distinction between continuum and
emergent continuity (0.11), observation from a changed field of
understanding, and the source authority of KA/FDLA (0.12).
Graziano Guiducci remains the authorial source of the research programme.
Incidental symbolic expressions from source conversations do not become
operational laws or metrics. Editorial revision does not constitute
independent human review, peer review or academic publication.
