# UX-AI — Rive, interazione osservata e possibilità di costruzione

Fonte dell'operatore, conversazione Codex/TM9 del 7 ottobre 2026:

> aggiungo delle risorse così sai di che parlo, se vedi delle opportunità prendiamole

Risorse selezionate: [Rive](https://rive.app/),
[Treasure Valley Interactive Map](https://rive.app/marketplace/28363-53629-treasure-valley-interactive-map/),
[introduzione ufficiale](https://rive.app/docs/getting-started/introduction)
e [Contra](https://contra.com/). L'operatore fornisce anche
`28363-53629-treasure-valley-interactive-map.riv`.

Questo contributo conserva conoscenza acquisita e possibilità per il
[medium percettivo](UI_MEDIUM_KERNEL_MANIFESTO_2026_10_07.md) e l'
[incarico GPT](UX_AI_CODE_MEDIUM_RESEARCH_ASSIGNMENT_2026_10_07.md).
Non cambia il corpo stabile SSK 0.11. Il sapere di costruzione continuerà
nell'owner UX-AI; il caso non determina l'intera forma della futura UI.

## Che cosa è stato esercitato localmente

Codex carica il file fornito con il runtime ufficiale `@rive-app/canvas`
versione `2.44.0`, raggiunto dal registro npm. L'integrità del pacchetto è
confrontata con quella dichiarata dal registro. JavaScript, WASM e file Rive
sono serviti su loopback; il caricamento automatico di asset CDN e l'apertura
automatica di URL da eventi Rive sono disabilitati.

Identità del file: 2.166.308 byte; SHA-256
`b873a990dc28459f6bcd8d9ab278c1f69e04fff8effbe29c27bf01a72bf4ce13`.
Il file originale conserva questo hash dopo la lettura e l'interazione.

La lettura runtime espone 29 artboard, quattro View Model e l'artboard
principale `MAIN`, con state machine `MainSM` e modello legato `MainVM`.
I modelli espongono queste proprietà:

| View Model | Proprietà |
| --- | --- |
| `MainVM` | `iconNum`, `indexNum`, `propertyOfButtonVM`, `propertyOfTargetingTreasureValleyVM` |
| `ButtonVM` | `clickButtonTrig`, `targetingButtonBool` |
| `TargetingTreasureValleyVM` | `targetingCitiesNum`, `propertyOfTargetingBoiseVM` |
| `TargetingBoiseVM` | `targetingSuburbanNeighborhoodNum` |

Tre osservazioni circoscritte:

- Una selezione con puntatore nella mappa apre una vista di dettaglio;
  la lettura successiva del modello mostra `indexNum` passato da `0` a `6`.
  Si osservano anche notifiche della proprietà di targeting delle città.
- Dopo ricaricamento, il codice imposta `indexNum = 6`; la scena mostra
  il dettaglio. Il codice imposta poi `indexNum = 0` e la scena torna alla
  vista generale. Le letture e le notifiche registrano la sequenza `6, 0`.
- Il valore di selezione e le proprietà di targeting sono distinti. Le due
  modalità di apertura non producono automaticamente la stessa composizione
  dei testi. Un singolo indice non descrive tutto lo stato percettivo.

La sonda locale, i JSON e le immagini restano su TM9 in
`output/playwright/rive-treasure-valley-20261007/`. La sonda legge il file
originale attraverso una route locale; non lo include nei sorgenti pubblicati.
Le durate nella traccia indicano il tempo trascorso dall'avvio della sonda,
non una misura di latenza dell'interazione. Non si dichiara un collegamento
a Codex/harness, una prova di replay deterministico o copertura di tutte
le interazioni della mappa.

## Sapere che cambia il seguito

Il [data binding ufficiale](https://rive.app/docs/runtimes/web/data-binding)
offre valori tipizzati e osservabili fra applicazione e grafica. Il caso
esercitato rende concreto il doppio percorso: azione nella scena verso
proprietà leggibile, proprietà scritta dal codice verso cambiamento della
scena. Il significato di un valore numerico resta da comprendere nel suo
modello e non diventa automaticamente un concetto del kernel.

Per UX-AI emerge una possibilità: mantenere un campo generale percepibile
mentre una relazione entra nel focus, rende disponibili dettagli e può
tornare al contesto. La selezione persistente e l'esplorazione temporanea
possono richiedere proprietà diverse. Il sapere utile comprende come
accoppiarle con lo stato reale, conservarne la provenienza e rendere
ispezionabile ciò che viene mostrato. Questa è una direzione da formare,
non una prescrizione di usare una mappa geografica per il kernel.

La [CLI ufficiale](https://rive.app/docs/cli/overview) documenta una seconda
possibilità: scene descritte in RML, script, sorgenti versionabili,
compilazione, ispezione e rendering locale. Il
[riferimento comandi](https://rive.app/docs/cli/reference/commands) documenta
input e dati simulati, avanzamento controllato e lettura dei valori in JSON.
La [guida per agenti](https://rive.app/docs/cli/agents) collega questi mezzi
al lavoro da prompt. La CLI non è stata installata o esercitata in questo
turno. L'[MCP ufficiale](https://rive.app/docs/editor/ai/mcp) è un altro
ingresso documentato verso il desktop Editor; non è attivo nella sessione.

Le [semantics Web](https://rive.app/docs/runtimes/web/semantics) possono
esporre elementi Canvas tramite un overlay DOM accessibile. Sono opzionali,
sperimentali e richiedono annotazioni nel progetto. Questa semantica di
accessibilità non equivale alla comprensione del kernel. La mappa qui
esercitata non è stata verificata per tastiera o tecnologie assistive.

[Contra](https://contra.com/) e la sua
[comunità Rive](https://contra.com/community/topic/rive) offrono un ingresso
a lavori e autori da cui cercare esempi, ragioni e processi reali. Il suo
[Human Creativity Benchmark](https://contralabs.com/human-creativity-benchmark)
presenta criteri di valutazione professionale: possibili fonti da confrontare
quando aiutano il nostro oggetto, senza sostituire la direzione dell'operatore.
Nessun autore è stato contattato e nessun servizio è stato acquistato.

## Attribuzione e riuso del caso

La pagina della mappa attribuisce il lavoro a **yaroslavna**, originariamente
per il team immobiliare HomeFound Boise. Descrive hover, navigazione, zoom,
ritorno e schede informative; queste dichiarazioni conservano l'attribuzione
all'autrice oltre le interazioni effettivamente esercitate sopra.

La stessa pagina mostra un badge **CC BY** e una descrizione che permette
apprendimento e remix **non commerciali**. Queste indicazioni non convergono
sul riuso commerciale degli asset. La lettura presente prende il caso per
apprendimento; un riuso commerciale richiederà chiarire quei termini.
