# Quando un sistema AI deve continuare a capire

## Un’introduzione accessibile al System Semantic Kernel (SSK)

**Graziano Guiducci**  
MAIOS / D-ND

Articolo accademico companion, versione 0.2 — 13 ottobre 2026

**Stato documentale.** Questa è la revisione accessibile del
[System Semantic Kernel (SSK), corpo stabile 0.12](SYSTEM_SEMANTIC_KERNEL_SSK_WORKING_PAPER_0_12.md).
Accompagna il Paper tecnico, che rimane la fonte canonica per definizioni,
argomentazione e stato delle affermazioni. La
[versione accessibile 0.1](SSK_ACCESSIBLE_ACADEMIC_ARTICLE_0_1_IT.md)
era derivata dal Paper 0.10. La presente 0.2 ne conserva il percorso
introduttivo e integra i sviluppi pertinenti delle versioni 0.11–0.12.
Resta una forma editoriale, non una nuova teoria o una prova indipendente.

## Abstract

I sistemi di intelligenza artificiale vengono sempre più spesso utilizzati in
lavori che durano nel tempo, attraversano sessioni, strumenti, fonti, persone e
rappresentazioni differenti. In questi contesti conservare più testo o più
memoria non garantisce, da solo, continuità. Un sistema può recuperare una
decisione corretta e tuttavia riprendere il lavoro nel modo sbagliato, perché ha
perso la relazione che rendeva quella decisione appropriata: la fonte, il
motivo, le condizioni, la competenza coinvolta o la conseguenza prodotta.

Il System Semantic Kernel (SSK) studia l’organizzazione semantico-relazionale
che mantiene connessi sorgenti, intento, contesto percepito, competenze, azioni,
risultati e conseguenze mentre il campo di lavoro cambia. Memorie, file, prompt,
interfacce, strumenti, sensori e runtime possono rendere disponibili queste
relazioni senza coincidere con esse. **La continuità emerge quando il lavoro
successivo riesce effettivamente a procedere dalle differenze prodotte da quello
precedente**: la loro conservazione, da sola, non è ancora quel risultato.

Questo articolo presenta il modello senza presupporre la terminologia D-ND,
KA o FDLA. Introduce progressivamente il problema della continuità, il ruolo
delle competenze, la correzione delle rappresentazioni che contaminano il
campo, la continuità fra mezzi e riceventi differenti e la nozione funzionale di
consapevolezza sintetica situata. Le formulazioni restano concettuali e legate alle fonti e al loro livello di
evidenza: gli esempi operativi interni discussi nel Paper sono casi
circoscritti, non validazione empirica indipendente né prova di superiorità
universale del modello.

La 0.11 distingue inoltre ciò che consente di conservare le relazioni
importanti da ciò che emerge quando queste relazioni cambiano realmente il
lavoro successivo. La 0.12 approfondisce l'osservazione non identica: una
nuova lettura dello stesso oggetto può rendere visibili rapporti prima nascosti
perché nel frattempo è cambiata la comprensione dell'osservatore.

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

Conservare tutto non è necessario. Occorre rendere raggiungibili le relazioni
la cui assenza cambierebbe il significato del lavoro successivo, e saperle
riconoscere quando tornano pertinenti. La conservazione sostiene il seguito;
non dimostra, da sola, che quel seguito sia capace di utilizzarla.

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

Per questo il problema presenta due aspetti collegati: **recuperare il
perché di una conclusione** e **renderlo operante nel nuovo contesto**.
La prima capacità permette il rientro nella relazione sorgente; la seconda
mostra se quella relazione partecipa al lavoro attuale.

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

La distinzione diventa utile quando lo stesso progetto attraversa **ambienti
riceventi differenti**, cioè sistemi o contesti operativi nei quali quella
relazione deve tornare utilizzabile. Una conversazione con ChatGPT, un ambiente
di coding con accesso al filesystem o un sistema embodied con sensori
possiedono mezzi diversi. Se una
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

Alcune relazioni del SSK provengono dal più ampio framework sorgente D-ND.
Non è necessario conoscere l’intero framework per seguire l’argomento: qui
entra soltanto la funzione che il Paper ha reso operativa nel Kernel.

Il primo termine specifico è **KA, Kernel Assiomatico**.

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

La revisione 0.12 rende esplicito anche il ruolo di **KA e FDLA come
invarianti di coerenza sotto l'autorità dell'autore**. I riceventi possono
apprendere a esercitarne le funzioni in contesti diversi; non ne riscrivono
la sorgente canonica. Questo non aggiunge un supervisore esterno.

Una frase proveniente dalla sorgente può inoltre essere citata correttamente
e ricevere un peso improprio: fedeltà delle parole e pertinenza per la domanda
attuale sono due questioni distinte. Correggere quel peso fa parte della
comprensione in atto.

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

Cambiare visualizzazione non significa ottenere automaticamente una
seconda misura indipendente. Un diagramma dei medesimi dati può però far
emergere una domanda nuova, o suggerire un'azione che renda osservabile una
relazione prima irraggiungibile. **Comprensione trasformata, nuova evidenza
e intervento sull'oggetto** hanno ruoli differenti.

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

Il Paper 0.11 precisa una conseguenza importante: una competenza può
apprendere non solo da un errore, ma anche da un successo o da una nuova
comprensione. Se quella differenza modifica la scelta delle fonti o il
metodo con cui verrà affrontato un caso futuro, il lavoro avrà contribuito
alle condizioni del lavoro successivo. Questa relazione viene descritta
come **lavoro che alimenta il proprio seguito**, non come crescita
automatica del numero di file o delle skill.

### Un evento editoriale documentato nel Paper

Il Paper tecnico (§7) conserva un episodio concreto. Durante la preparazione
di un articolo sul ritorno a un contesto già affrontato, l'operatore ha
richiamato una distinzione decisiva: due informazioni possono essere
singolarmente corrette, ma non essere mai state vere *insieme* nelle
condizioni attribuite loro. Riunirle in una narrazione fluida può quindi
produrre un presente inesistente.

Questa relazione ha cambiato la domanda editoriale e il modo di costruire
l'argomento. Il lavoro ha prodotto un articolo locale e una proposta di
confronto; la competenza Editoriali ha anche **rappresentato un cambiamento
del proprio metodo**, distinguendo meglio la formazione dell'argomento
dalla sua successiva calibrazione per il pubblico.

È un evento interno documentato, non un benchmark indipendente. Il Paper
non registra ancora un successivo esercizio non identico che dimostri
l'assimilazione di quel metodo. Proprio tale distinzione mostra perché
**un artefatto prodotto, una competenza aggiornata e una capacità poi
esercitata** non siano la stessa cosa.


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

La domanda comune è un’altra: **quali relazioni devono rimanere raggiungibili
e come possono partecipare al nuovo lavoro, senza ricostruire tutto né fingere
che nulla sia cambiato?**

Questa domanda diventa particolarmente importante nei sistemi distribuiti.

Se tre agenti ricevono un problema ancora cognitivamente irrisolto e ciascuno
deve ricostruire da solo tutto il campo prima di agire, la distribuzione può
aumentare rumore e lavoro duplicato. Se invece esiste già un risultato
sufficientemente formato, una parte distinta del lavoro può essere trasferita a
un altro ricevente insieme alle relazioni necessarie per comprenderla.

La distribuzione, quindi, non è automaticamente un vantaggio. Dipende
sia dalle relazioni che diventano raggiungibili nel nuovo ambiente,
sia dalla capacità del ricevente di usarle nel proprio lavoro.

### Conservare e continuare: due relazioni diverse

La revisione 0.11 permette di distinguere due relazioni che si sostengono
a vicenda, senza coincidere.

Il **continuum** conserva o rende recuperabili le differenze ancora
causalmente pertinenti: ragioni, fonti, determinazioni, competenze
modificate, conseguenze. Può attraversare memoria, repository e mezzi
diversi: non è necessariamente un archivio unico.

La **continuità** emerge, invece, quando il sistema comincia un nuovo
lavoro dal campo modificato dai risultati precedenti, e quelle differenze
partecipano davvero alla nuova comprensione o al nuovo metodo.

Un esempio: un progetto conserva la nota «la soluzione B non funziona
in queste condizioni». Il continuum ne custodisce la ragione.
La continuità si manifesta se, davanti a un caso successivo pertinente,
il sistema usa quel sapere per scegliere o formare meglio una soluzione.
La nota può essere perfettamente archiviata anche quando il sistema
non sa ancora applicarla.

La capacità di proseguire non coincide dunque con la sola persistenza.
E non richiede che ogni singolo evento cambi la competenza: anche una
determinazione adeguata può continuare invariata.

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

Il campo può contenere relazioni che il sistema non sta percependo.
Una memoria può conservarle e una competenza può essere disponibile
senza diventare pertinente in questo momento. La consapevolezza situata
non coincide quindi con l’intero patrimonio conservato: riguarda la
composizione delle relazioni che effettivamente partecipano all'evento.

Il continuum può mantenere raggiungibile una ragione senza renderla
immediatamente presente nella consapevolezza. Il sistema mostra continuità
quando, in un evento successivo, quella ragione torna pertinente e modifica
concretamente la comprensione o l'azione. Questa differenza è essenziale
per non attribuire al solo archivio una capacità che deve ancora essere
esercitata.

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

La sufficienza permette di continuare senza ripetere sempre lo stesso
lavoro, ma non impedisce di osservare di nuovo quando il campo è cambiato.

Una prima lettura può produrre un'impressione corretta senza rendere
visibili tutte le relazioni pertinenti. Nel secondo incontro, il sapere
acquisito consente di riconoscere legami fra dettagli prima isolati;
un terzo può integrarli in una struttura più chiara. Come davanti a un
quadro, riconoscere un particolare può cambiare il significato degli
altri, anche se il dipinto è rimasto identico.

Questa nuova comprensione non è per ciò stesso una nuova prova esterna.
Il suo valore emerge da ciò che rende possibile comprendere o fare
diversamente. I passaggi non sono un numero obbligatorio: quando un
nuovo attraversamento non cambia più nulla di materialmente pertinente,
anche **nessun cambiamento** è una risultante valida.

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

Nel Paper 0.12 convivono:

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

La revisione 0.12 mantiene inoltre separati il cambiamento
documentato di una competenza e la sua **assimilazione**: soltanto un
esercizio successivo, in una situazione non identica, può mostrare se
il modo di operare è davvero cambiato.

Sono precisamente queste distinzioni a rendere possibile una ricerca
progressiva senza trasformare ogni sviluppo concettuale in un claim empirico.

## 13. Una possibile agenda di ricerca

Il Paper mantiene diverse domande comparative aperte. Per un lettore esterno,
quattro sono particolarmente immediate.

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

**Continuità emergente.** Un cambiamento registrato nella memoria
si traduce in una nuova capacità quando il sistema incontra un altro
problema? Come distinguiamo il riuso effettivo dalla sola disponibilità
del documento?

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
degli agenti, ma descrivere l'organizzazione che rende pertinenti e
raggiungibili sorgenti, intento, contesto percepito, competenze, mezzi,
azioni, risultati e conseguenze. **La continuità emerge quando tale
organizzazione permette al lavoro successivo di procedere dalle relazioni
effettivamente trasformate dal lavoro precedente.**

KA mantiene il campo più ampio della rappresentazione corrente. FDLA corregge
le sostituzioni introdotte dal sistema mentre il lavoro prende forma. Le
competenze possono apprendere, non soltanto essere archiviate. Le
rappresentazioni possono diventare sonde epistemiche senza trasformarsi in
prove. Un risultato sufficientemente formato può diventare il nuovo punto di
partenza senza dover ricostruire l’intero passato.

La distinzione più importante della versione 0.11 è che la continuità
non si trova già pronta nella memoria: emerge quando un lavoro alimenta
un lavoro successivo. La 0.12 approfondisce come una nuova osservazione,
dal campo trasformato dalla comprensione precedente, possa cambiare
la domanda, il metodo e le competenze che proseguiranno.

Questa è la porta d’ingresso al Paper tecnico.

Il [SSK stable body 0.12](SYSTEM_SEMANTIC_KERNEL_SSK_WORKING_PAPER_0_12.md)
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
    Situated Meaning, and Evolution Across Agentic Systems*, corpo stabile 0.12.
    [Paper tecnico canonico](SYSTEM_SEMANTIC_KERNEL_SSK_WORKING_PAPER_0_12.md).

## Provenienza editoriale

Revisione editoriale AI della versione accessibile 0.1, originariamente
derivata dal corpus SSK 0.10. La 0.2 è collegata al
[Paper tecnico SSK 0.12](SYSTEM_SEMANTIC_KERNEL_SSK_WORKING_PAPER_0_12.md)
e al suo stato delle affermazioni. Le aggiunte riguardano il continuum
e la continuità emergente (0.11), l'osservazione da una comprensione
cambiata e il ruolo sorgente di KA/FDLA (0.12). Graziano Guiducci resta
la fonte autoriale del programma di ricerca. I simboli incidentali delle
conversazioni sorgente non diventano leggi o metriche operative. Questa
forma editoriale non equivale a revisione umana indipendente, peer review
o pubblicazione accademica.
