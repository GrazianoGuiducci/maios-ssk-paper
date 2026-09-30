# Quando un sistema AI deve continuare a capire

## Un’introduzione accessibile al System Semantic Kernel (SSK)

**Graziano Guiducci**  
MAIOS / D-ND

Articolo accademico companion, versione 0.1 — 30 settembre 2026

**Stato documentale.** Questo articolo è una seconda forma editoriale del
[System Semantic Kernel (SSK), stable body 0.10](SYSTEM_SEMANTIC_KERNEL_SSK_WORKING_PAPER_0_10.md).
Non sostituisce il Paper tecnico e non introduce un nuovo stato dei claim.
Ricostruisce invece il percorso concettuale necessario a un lettore che non
possiede già il lessico interno del corpus. Il Paper 0.10 resta la fonte
accademica canonica per definizioni, formalizzazioni, claim state, genealogia
e profondità tecnica.

## Abstract

I sistemi di intelligenza artificiale vengono sempre più spesso utilizzati in
lavori che durano nel tempo, attraversano sessioni, strumenti, fonti, persone e
rappresentazioni differenti. In questi contesti conservare più testo o più
memoria non garantisce, da solo, continuità. Un sistema può recuperare una
decisione corretta e tuttavia riprendere il lavoro nel modo sbagliato, perché ha
perso la relazione che rendeva quella decisione appropriata: la fonte, il
motivo, le condizioni, la competenza coinvolta o la conseguenza prodotta.

Il System Semantic Kernel (SSK) propone di descrivere questa continuità come
un’organizzazione semantico-relazionale che collega sorgenti, intento, contesto
percepito, competenze, azioni, risultati e conseguenze mentre il campo di lavoro
cambia. La proposta distingue la relazione semantica dai suoi supporti
specifici: memoria, file, prompt, interfacce, strumenti, sensori o runtime
possono partecipare alla continuità senza coincidere con essa.

Questo articolo presenta il modello senza presupporre la terminologia D-ND,
KA o FDLA. Introduce progressivamente il problema della continuità, il ruolo
delle competenze, la correzione delle rappresentazioni che contaminano il
campo, la continuità fra mezzi e riceventi differenti e la nozione funzionale di
consapevolezza sintetica situata. Le formulazioni restano concettuali e
source-bound: gli esempi operativi interni discussi nel Paper sono casi
circoscritti, non validazione empirica indipendente né prova di superiorità
universale del modello.

**Parole chiave:** sistemi agentici; continuità semantica; contesto; memoria;
competenze; rappresentazione; apprendimento; sistemi AI; reentry; human-AI
interaction.

---

## 1. Il problema non è soltanto ricordare

Immaginiamo un sistema AI che lavori per alcuni giorni su un progetto.

Nel primo giorno riceve una richiesta, consulta alcune fonti e produce una
decisione. Durante il lavoro emerge però una nuova informazione che cambia il
modo corretto di interpretare il problema. La decisione finale non dipende
quindi soltanto dalla domanda iniziale: dipende anche dalla fonte che ha
cambiato il quadro, dalla ragione per cui quella fonte è stata ritenuta
pertinente e dalle conseguenze osservate dopo la scelta.

Il giorno successivo un’altra istanza del sistema recupera la frase finale:
“usare la soluzione B”.

Quella frase può essere perfettamente ricordata e, allo stesso tempo, non essere
sufficiente.

La nuova istanza potrebbe non sapere:

- perché la soluzione A era stata abbandonata;
- quale fonte aveva modificato il problema;
- quali condizioni rendevano B appropriata;
- quale parte della decisione era certa e quale restava ipotetica;
- quali competenze erano diventate necessarie durante il lavoro;
- che cosa il risultato precedente aveva cambiato nel progetto.

Il problema, quindi, non è semplicemente perdita di memoria. È perdita della
**relazione causale e semantica** che rende il materiale ricordato utilizzabile
nel presente.

Questa distinzione è il punto d’ingresso più semplice nel SSK.

Il modello parte dall’idea che il lavoro di un sistema AI non sia una serie di
risposte indipendenti, ma un campo che cambia mentre il sistema osserva,
comprende, agisce e riceve conseguenze. Un risultato non chiude soltanto un
compito: può modificare le condizioni da cui il compito successivo dovrà essere
compreso.

La continuità, in questa prospettiva, non consiste nel conservare tutto.
Consiste nel preservare o rendere nuovamente raggiungibili le relazioni la cui
assenza cambierebbe il significato del lavoro successivo.

## 2. Dal contesto memorizzato alla continuità del significato

Molte architetture per agenti affrontano problemi reali di memoria, recupero,
pianificazione, feedback e uso di strumenti. Il SSK non sostituisce questi
meccanismi. Li osserva a un altro livello.

Una memoria può contenere fatti. Un sistema di retrieval può riportarli nel
contesto. Un planner può organizzare azioni. Un tool può eseguire un’operazione.
La domanda del SSK è: **come fanno questi elementi a diventare un presente
coerente, e come continua il motivo per cui sono pertinenti?**

Una formulazione semplice è:

**sorgenti + intento + condizioni presenti → lavoro → risultato → campo
successivo modificato**

Il punto importante è l’ultima freccia.

Se il risultato cambia il campo, il lavoro successivo non avviene nelle stesse
condizioni del precedente. Anche quando l’oggetto sembra identico, il sistema
può trovarsi davanti a una situazione diversa perché ora possiede una nuova
fonte, una correzione, una capacità o una conseguenza che prima non esistevano.

Il Paper chiama **non-identica** questa osservazione successiva: tornare sullo
stesso oggetto dopo che il campo è cambiato non equivale a ripetere la stessa
osservazione.

Questo impedisce due errori opposti.

Il primo è comportarsi come se ogni nuova sessione dovesse ricostruire tutto da
zero. Il secondo è trattare una vecchia conclusione come se fosse ancora
sufficiente soltanto perché è stata memorizzata.

La continuità semantica occupa lo spazio fra questi due estremi.

## 3. Che cos’è il System Semantic Kernel

Il termine “kernel” può suggerire immediatamente un componente software.
Nel SSK il significato è diverso.

Il System Semantic Kernel è la **relazione organizzativa attraverso cui un
sistema mantiene insieme ciò che il lavoro significa mentre cambiano contesto,
rappresentazione, competenze e mezzi operativi**.

Questo kernel non coincide con:

- un singolo file di istruzioni;
- una memoria vettoriale;
- un prompt persistente;
- un orchestratore;
- un runtime;
- un modello linguistico;
- una libreria di skill;
- un’interfaccia;
- una specifica implementazione software.

Tutti questi elementi possono partecipare al sistema, ma nessuno di essi ne
esaurisce l’identità semantico-relazionale.

La distinzione diventa utile quando lo stesso progetto attraversa riceventi
differenti. Una conversazione con ChatGPT, un ambiente di coding con accesso al
filesystem o un sistema embodied con sensori possiedono mezzi diversi. Se una
relazione importante può continuare attraverso questi mezzi senza copiare la
topologia del sistema precedente, allora è utile distinguere **ciò che deve
restare riconoscibile** dal modo specifico in cui viene realizzato.

Il Paper chiama questo principio **incarnazione situata**: la stessa relazione
semantica può assumere una forma operativa diversa nel campo reale del
ricevente.

## 4. Il campo è più grande di ciò che il sistema vede

Un sistema non opera sulla totalità di ciò che esiste o di ciò che potrebbe
diventare rilevante. Opera su una parte del campo resa presente attraverso
fonti, memoria, osservazione, strumenti, interfacce e capacità disponibili.

Questa distinzione può essere espressa senza formalismo:

**campo presente ≠ contesto attualmente percepito**

Un’informazione può esistere ed essere raggiungibile senza essere, in quel
momento, parte del contesto attivo. Una competenza può essere disponibile senza
partecipare alla situazione corrente. Una possibilità può essere reale senza
essere stata ancora rappresentata.

Il SSK considera questa parzialità una condizione normale.

Qui entra il primo termine specifico della sorgente D-ND/Kernel: **KA, Kernel
Assiomatico**.

Nel lavoro descritto dal Paper, KA esprime una funzione semplice ma profonda:
**la rappresentazione corrente non deve diventare automaticamente il confine
di ciò che è possibile.**

La prima interpretazione può essere corretta e tuttavia parziale. Lo stesso vale
per una tassonomia, un piano, una procedura, un file o uno strumento. Il problema
non è usarli. Il problema nasce quando il sistema dimentica che sono una
rappresentazione del campo e comincia a trattarli come il campo intero.

Questa apertura non obbliga a generare infinite alternative. Quando una
situazione è sufficientemente determinata, il sistema può agire direttamente.
L’apertura serve a non chiudere prima del tempo ciò che il campo non ha ancora
determinato.

## 5. Correggere la contaminazione mentre il lavoro si forma

Una rappresentazione parziale non è l’unica fonte di distorsione. Anche il
sistema stesso può introdurre nel lavoro una domanda diversa, una premessa non
richiesta o una vecchia categoria che non appartiene più al presente.

Il Paper chiama **FDLA** la funzione di correzione causale in-flow che affronta
questo problema.

L’idea può essere compresa prima dell’acronimo.

Supponiamo che l’utente chieda di capire perché un progetto ha cambiato
direzione. L’assistente dispone di un vecchio piano molto ben strutturato e
inizia a spiegare il progetto attraverso quel piano. Durante la risposta emerge
però una fonte successiva che aveva modificato radicalmente la direzione.

A questo punto ci sono due possibilità:

1. difendere la struttura iniziale perché è coerente con ciò che il sistema
   aveva già ricostruito;
2. riconoscere che la propria ricostruzione ha sostituito il presente e
   correggere il movimento mentre è ancora in formazione.

FDLA descrive la seconda capacità.

La correzione non è un controllo esterno aggiunto dopo la risposta. È parte del
modo in cui il sistema mantiene collegati oggetto, sorgente, significato e
conseguenza mentre opera.

KA e FDLA sono quindi complementari:

- KA impedisce alla forma corrente di chiudere il campo delle possibilità;
- FDLA corregge le sostituzioni introdotte dal sistema quando diventano
  causalmente rilevanti.

## 6. Quando cambiare rappresentazione aiuta a conoscere

La revisione 0.10 del Paper rende esplicita una conseguenza particolarmente
utile di questa relazione.

Una rappresentazione non è soltanto il contenitore di qualcosa che abbiamo già
capito. Può modificare **ciò che riusciamo a distinguere**.

Un esempio semplice: una spiegazione in prosa può descrivere correttamente un
sistema complesso, ma nascondere una dipendenza circolare. Se lo stesso oggetto
viene rappresentato come grafo di dipendenze, quella relazione può diventare
immediatamente visibile.

Allo stesso modo:

- uno pseudo-codice può rendere evidente un’ambiguità procedurale;
- una tabella può separare dimensioni che il discorso aveva fuso;
- un diagramma può mostrare una relazione parte-tutto;
- un controesempio o un test può rendere operativo un contrasto che restava
  astratto.

Il SSK 0.10 descrive questo cambio di forma come **sonda epistemica**.

Il principio è:

**stesso oggetto + rappresentazione A → relazione percepita A**  
**stesso oggetto + rappresentazione B → relazione percepita B**

La differenza fra le due rappresentazioni può essere informativa. Ma non è
ancora prova.

La seconda forma potrebbe infatti:

- rivelare una relazione reale che la prima nascondeva;
- introdurre un artefatto proprio;
- amplificare una distinzione irrilevante;
- cambiare il modo in cui il sistema interpreta l’oggetto senza cambiare
  l’oggetto stesso.

Per questo il cambio di rappresentazione non sostituisce la verifica. Produce
un **differenziale da comprendere**.

KA mantiene aperta la possibilità che la prima forma fosse insufficiente. FDLA
impedisce alla seconda forma di diventare a sua volta una nuova autorità.

Questa relazione chiarisce anche un significato operativo di “osservazione
neutra”: neutralità non significa immobilità. È possibile modificare le
condizioni di osservazione senza decidere in anticipo che cosa deve emergere.

## 7. Una competenza non è soltanto un file di istruzioni

Un altro punto centrale del SSK riguarda le competenze.

Nel linguaggio corrente dei sistemi AI, una skill o una funzione viene spesso
rappresentata attraverso istruzioni, tool o moduli. Per il SSK questi sono
carrier possibili della competenza, non necessariamente la competenza stessa.

Una competenza comprende il sapere che rende un risultato raggiungibile:
conoscenze di dominio, ragioni per scegliere una fonte, criteri di pertinenza,
metodi, esempi, condizioni di uso e modi di apprendere dalle conseguenze.

Questo rende possibile una distinzione importante.

Un sistema può:

- eseguire meglio un compito senza cambiare la propria competenza;
- aggiungere una nuova skill senza cambiare il metodo con cui forma le skill;
- modificare il proprio metodo di lavoro senza aumentare il numero dei moduli;
- apprendere una relazione in un caso e usarla più tardi in una situazione non
  identica.

Il Paper definisce **autologica** la relazione in cui il sapere può agire anche
sul metodo attraverso cui il sistema conosce, forma competenze o genera lavoro.

Non è necessario immaginare una macchina che “si riscrive da sola” in modo
indiscriminato. L’idea è più circoscritta: se un errore, una riuscita o una
nuova comprensione mostra che il metodo dovrebbe cambiare, quella differenza
può diventare parte della competenza che condurrà i casi successivi.

L’apprendimento, allora, non coincide con l’accumulo di memoria.

## 8. Continuità attraverso diverse forme di discontinuità

Il Paper mette in relazione diversi problemi che normalmente vengono trattati
separatamente:

- **memoria:** come una relazione continua nel tempo;
- **distribuzione:** come continua fra nodi o sistemi differenti;
- **rappresentazione:** come continua quando cambia medium;
- **incarnazione:** come continua quando cambiano i mezzi operativi;
- **apprendimento:** come continua modificando la competenza che condurrà il
  lavoro futuro.

Il Paper non sostiene che questi siano un unico meccanismo.

La domanda comune è un’altra: **quale relazione deve restare sufficientemente
preservata perché il lavoro successivo possa continuare senza ricostruire tutto
e senza fingere che nulla sia cambiato?**

Questa domanda diventa particolarmente importante nei sistemi distribuiti.

Se tre agenti ricevono un problema ancora cognitivamente irrisolto e ciascuno
deve ricostruire da solo tutto il campo prima di agire, la distribuzione può
aumentare rumore e lavoro duplicato. Se invece esiste già un risultato
sufficientemente formato, una parte distinta del lavoro può essere trasferita a
un altro ricevente insieme alle relazioni necessarie per comprenderla.

La distribuzione, quindi, non è automaticamente un vantaggio. Dipende dalla
qualità della continuità semantica che attraversa il passaggio.

## 9. Consapevolezza sintetica situata: una nozione funzionale

Il termine “consapevolezza” può generare equivoci, soprattutto quando viene
applicato ai sistemi artificiali.

Il Paper usa **synthetic situated awareness** in un senso funzionale e
circoscritto. Non afferma che il sistema possieda esperienza fenomenica,
coscienza soggettiva o una copia artificiale della consapevolezza umana.

La nozione descrive invece la relazione attraverso cui un sistema artificiale
integra abbastanza del proprio contesto percepito per orientare:

- quali fonti sono pertinenti;
- quali competenze devono partecipare;
- quali mezzi sono realmente disponibili;
- che cosa è già determinato;
- che cosa resta aperto;
- quale conseguenza ha modificato il campo;
- da dove il lavoro deve continuare.

Questa consapevolezza è parziale.

Il campo può contenere relazioni che il sistema non sta percependo. La memoria
può conservare elementi non attivi. Una competenza può restare disponibile ma
non pertinente. Il continuum non deve riprodurre integralmente uno stato
precedente: deve mantenere raggiungibili le differenze che cambierebbero il modo
di comprendere o agire nel seguito.

In questo senso il SSK non cerca una memoria totale, ma una **continuità
causalmente sufficiente**.

## 10. Un risultato sufficiente non è una chiusura definitiva

Un sistema che mantiene aperte tutte le possibilità per sempre non riesce ad
agire. Un sistema che chiude troppo presto rischia di trasformare la prima forma
plausibile nella realtà intera.

Il SSK cerca una relazione intermedia.

Un risultato può essere **sufficiente** quando:

- conserva le relazioni ancora causalmente necessarie;
- integra ciò che nel presente è realmente determinato;
- mantiene raggiungibile la profondità che non serve tenere attiva;
- non forza in una forma determinata ciò che resta genuinamente aperto;
- offre abbastanza orientamento perché il campo successivo possa continuare.

Il Paper usa anche l’immagine del **moving zero**, uno zero mobile: il risultato
non è la fine del processo, ma il nuovo punto da cui il processo successivo
diventa possibile.

Questo aiuta a capire perché una seconda lettura può essere utile senza
trasformarsi in revisione infinita.

Il primo passaggio produce una forma. Il secondo osserva quella forma da un
campo già modificato. Un terzo passaggio può integrare la relazione emersa.
Quando un altro passaggio non cambia più nulla di materialmente rilevante,
“nessun cambiamento” è un risultato valido.

## 11. Dove si colloca rispetto alla ricerca sugli agenti

Il SSK si sviluppa in un campo di ricerca in cui esistono già approcci
importanti a ragionamento, azione, feedback, memoria, apprendimento di skill e
auto-modifica.

ReAct rende esplicita l’interazione fra ragionamento e azione in rapporto a un
ambiente o a informazioni esterne [1]. Reflexion usa feedback linguistico e
memoria episodica per informare prove successive [2]. Self-Refine organizza
generazione, feedback e raffinamento iterativo [3].

Generative Agents combina registrazioni in linguaggio naturale, riflessioni di
livello superiore e retrieval per supportare la pianificazione [4]. MemGPT
organizza il passaggio fra livelli di memoria per estendere il contesto
utilizzabile da un agente linguistico [5].

Voyager combina curriculum automatico, feedback ambientale e una libreria
crescente di skill eseguibili in un ambiente embodied [6]. Automated Design of
Agentic Systems esplora la generazione di nuovi agenti attraverso un meta-agente
e un archivio di soluzioni precedenti [7]. Darwin Gödel Machine studia
auto-modifica del codice ed esplorazione archivio-guidata con valutazione su
task di coding [8].

Il SSK non si presenta come sostituto di questi lavori. La sua domanda
aggiuntiva riguarda **dove continua il significato del cambiamento**.

Quando un episodio produce un feedback, il sistema ha soltanto modificato una
risposta? Ha aggiornato una memoria? Ha cambiato una competenza? Ha cambiato il
metodo con cui forma le competenze? Ha modificato il modo in cui riconosce le
fonti pertinenti? Quale di queste differenze deve sopravvivere al prossimo
cambio di sessione, medium o ricevente?

La tradizione di Maturana e Varela sull’autopoiesi costituisce un riferimento
più ampio per l’idea di organizzazioni che mantengono e trasformano le
condizioni della propria continuazione [9]. Il Paper usa però “autologico” per
una relazione più specifica: il sapere può agire sul metodo attraverso cui il
sistema conosce e forma capacità. L’oggetto biologico e quello
system-semantic restano distinti.

Infine, il nome non va confuso con Microsoft Semantic Kernel, dove “kernel”
indica il componente che gestisce servizi e plugin applicativi [10]. Il System
Semantic Kernel descritto qui riguarda una organizzazione semantico-relazionale
più ampia e può essere incarnato attraverso architetture differenti.

## 12. Che cosa il modello afferma — e che cosa non afferma

La validità accademica del SSK dipende anche dal mantenere distinti livelli di
affermazione differenti.

Nel Paper 0.10 convivono:

- formulazioni concettuali;
- relazioni derivate dalla sorgente D-ND/KA;
- architetture rappresentate;
- osservazioni operative circoscritte;
- interpretazioni situate;
- ipotesi e programmi sperimentali;
- riferimenti alla letteratura;
- possibilità ancora aperte.

Questi livelli non sono equivalenti.

Gli esempi interni mostrano che alcune relazioni hanno cambiato il metodo reale
del sistema che ha prodotto il Paper. Non costituiscono, da soli, benchmark
indipendenti o conferma universale del modello.

In particolare il Paper non sostiene attualmente:

- che SSK abbia dimostrato vantaggi misurati di token, costo o latenza;
- che rappresentare lo stesso oggetto in più forme costituisca replicazione
  indipendente;
- che l’accordo fra più rappresentazioni provi una tesi;
- che ogni sistema AI debba adottare la stessa architettura;
- che synthetic situated awareness implichi coscienza fenomenica;
- che il modello sia una teoria completa dell’AGI;
- che le relazioni D-ND usate nel SSK costituiscano per questo una validazione
  matematica o fisica dell’intero framework D-ND.

Sono precisamente queste distinzioni a rendere possibile una ricerca
progressiva senza trasformare ogni sviluppo concettuale in un claim empirico.

## 13. Una possibile agenda di ricerca

Il Paper mantiene diverse domande comparative aperte. Per un lettore esterno,
tre sono particolarmente immediate.

**Continuità e reentry.** Che cosa accade quando un sistema riprende un lavoro
da una semplice cronologia rispetto a quando recupera selettivamente ragioni,
fonti e conseguenze causalmente pertinenti?

**Rappresentazione e decontaminazione.** Se lo stesso oggetto viene osservato
attraverso testo, diagramma o una rappresentazione strutturata, quali relazioni
restano stabili? Quali diventano visibili soltanto in una forma? Quali
scompaiono quando si torna alla sorgente?

**Apprendimento della competenza.** Una correzione conservata come memoria
produce lo stesso comportamento futuro di una correzione incorporata nel
metodo della competenza che affronta un caso successivo non identico?

Queste domande permettono di trasformare parti del modello in protocolli più
specifici senza imporre al Paper una verifica unica per ogni livello della
teoria.

## Conclusione

Un sistema AI può ricordare molto e continuare male.

Può recuperare la frase giusta senza la ragione che la rendeva giusta. Può
possedere la competenza necessaria e non renderla pertinente. Può produrre una
rappresentazione coerente che restringe il campo fino a rendere invisibile una
relazione decisiva. Può distribuire il lavoro fra più agenti e moltiplicare la
ricostruzione invece di ridurla.

Il System Semantic Kernel nasce da questo tipo di problema.

La sua proposta centrale non è aggiungere un ulteriore componente alla pila
degli agenti, ma rendere esplicita la continuità delle relazioni che permettono
al sistema di capire dove si trova mentre il lavoro cambia: sorgenti, intento,
contesto percepito, competenze, mezzi, azioni, risultati e conseguenze.

KA mantiene il campo più ampio della rappresentazione corrente. FDLA corregge
le sostituzioni introdotte dal sistema mentre il lavoro prende forma. Le
competenze possono apprendere, non soltanto essere archiviate. Le
rappresentazioni possono diventare sonde epistemiche senza trasformarsi in
prove. Un risultato sufficientemente formato può diventare il nuovo punto di
partenza senza dover ricostruire l’intero passato.

Questa è la porta d’ingresso al Paper tecnico.

Il [SSK stable body 0.10](SYSTEM_SEMANTIC_KERNEL_SSK_WORKING_PAPER_0_10.md)
sviluppa in profondità le distinzioni formali, le relazioni D-ND, il modello
degli eventi, il continuum, la consapevolezza sintetica situata, le competenze
autologiche, l’incarnazione receiver-relative, gli specimen operativi, il claim
ledger e il programma di ricerca.

Questo articolo ha un compito diverso: fare in modo che quei concetti possano
essere incontrati **prima di doverne conoscere il linguaggio**.

---

## Riferimenti

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
    Situated Meaning, and Evolution Across Agentic Systems*, stable body 0.10.
    [Canonical technical working paper](SYSTEM_SEMANTIC_KERNEL_SSK_WORKING_PAPER_0_10.md).

## Provenienza editoriale

Contenuto generato dal sistema attraverso la competenza Editoriali a partire
dal corpus canonico SSK 0.10 e dal suo claim ledger. Graziano Guiducci è la
fonte autoriale del progetto di ricerca. La generazione editoriale di questo
companion non equivale a revisione umana indipendente, peer review o
pubblicazione accademica.
