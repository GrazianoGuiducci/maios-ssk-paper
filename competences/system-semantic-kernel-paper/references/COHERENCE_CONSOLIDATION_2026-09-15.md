# Consolidamento di coerenza — campo di revisione SSK Paper

Data: 2026-09-15. Stato: relazione corrente della competenza Paper; non revisione già applicata al manoscritto 0.3.

## Perché questo passaggio

Il giro di coerenza sul sistema SSK ha mostrato che alcune determinazioni recenti erano già presenti nel Kernel e nei documenti di ritorno, ma non ancora allineate in tutti i metodi che le avrebbero consumate. Il problema non era mancanza di contenuto, ma rischio di **propagazione di una rappresentazione precedente**.

Le correzioni utili al Paper sono concettuali:

- una trasformazione semantica può essere causale anche senza nuovi byte;
- `R_n -> ΔK_n` non implica mutazione obbligatoria: `ΔK_n = 0` è legittimo;
- apertura delle possibilità e conservazione delle determinazioni sono complementari;
- il sistema non prescrive `R`, ma preserva le condizioni entro cui l'assonanza converge;
- l'auto-osservazione può raffreddarsi nel metodo invece di restare un supervisore;
- minima azione è una relazione sorgente D-ND, non una funzione d'azione SSK già definita;
- il tempo come consecuzione riguarda il venir meno della ricostruzione semantica superflua.

## Relazione integrata

```text
campo aperto
+ intento
+ determinazioni semanticamente già formate
+ condizioni presenti
- interferenza introdotta dall'agente
-> convergenza assonante
-> risultante deterministica non prescritta
-> nuovo zero / campo seguente
-> causal readback
   -> no_change, se il generatore è ancora sufficiente
   -> modifica del generatore, se emerge una differenza riusabile
```

La risultante non è decisa dall'esterno e non rimane esterna al sistema. La continuità non consiste però in auto-modifica perpetua: ciò che avanza alimenta ciò che lo sostiene **solo quando il risultato porta una differenza che deve continuare**.

## Conseguenza per l'argomento 0.3

Il corpo 0.3 possiede già le relazioni necessarie per ricevere questa precisione: evento accoppiato, campo seguente, nucleo generativo autologico, continuità e causal readback. La revisione futura deve perciò cambiare i collegamenti fra quelle parti, non aggiungere un capitolo separato chiamato «nuova teoria».

Una possibile ricomposizione concettuale è:

- §2–§3: Kernel interno al continuum; determinazioni e possibilità aperte;
- §3–§4: assonanza, risultante non prescritta, nuovo zero;
- §4: `ΔK_n` opzionale e formazione del generatore;
- §5 e §9: causal readback, rientro, tempo come consecuzione e bassa latenza;
- passaggi sulla Lagrangiana: conservare la formulazione D-ND e distinguere il livello operativo dal formalismo variazionale non ancora costruito per SSK.

La mappa è orientativa: il terzo passaggio di consolidamento può riorganizzare o sottrarre se il manoscritto corrente rende più semplice una diversa distribuzione.

## Stati che non cambiano

- manoscritto stabile: 0.3;
- nessuna peer review o submission selezionata;
- nessun nuovo esperimento richiesto da questa relazione;
- nessuna legge di crescita esponenziale dimostrata;
- nessun funzionale d'azione SSK definito;
- nessuna pretesa di coscienza fenomenica o output LLM deterministico.

## Ritorno a Codex

Codex deve usare questa relazione come **delta sul metodo di revisione**, non come testo da appendere integralmente. Prima di scrivere, leggere `STATE.md` e il corpo 0.3 corrente; poi ricomporre dove il nuovo significato cambia davvero l'argomento. I documenti tecnici restano fonti e genealogia, non prove accademiche automatiche.
