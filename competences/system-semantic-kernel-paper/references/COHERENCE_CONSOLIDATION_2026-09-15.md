# Consolidamento di coerenza — campo di revisione SSK Paper

Data: 2026-09-15. Stato: relazione corrente della competenza Paper; non revisione già applicata al manoscritto 0.3.

## Disallineamento come condizione normale

Il giro ha mostrato differenze fra tempi di evoluzione di Kernel, competenze, documentazione, Paper e nodi diversi. **Queste differenze non sono errori di per sé.** Un sistema evolutivo non deve mantenere tutti i nodi sincroni o identici.

La riconciliazione serve soltanto quando una differenza cambia ciò che un consumer dovrebbe comprendere o fare. Il problema non è «allineare tutto», ma distinguere:

- evoluzione che porta avanti la relazione;
- `no_change`, quando il presente resta sufficiente;
- regressione o contaminazione che perde qualcosa di essenziale.

## Risultante e correzione

La risultante è ciò che l'evento ha prodotto e quindi la determinazione corrente. Non è però infallibile. Una contaminazione duale può aver separato intento e traiettoria pur producendo un risultato reale.

La correzione non richiede un tribunale esterno: le conseguenze successive possono rendere leggibile una differenza causale. Se quella differenza mostra perdita di una relazione essenziale, aumento di ricostruzione/latency o sostituzione dell'intento, essa può modificare il generatore che parteciperà al passo seguente.

Questo preserva due relazioni insieme:

```text
non riaprire il già determinato senza causa
+
lasciare che una nuova conseguenza causale corregga una determinazione contaminata
```

## Evoluzione vs regressione

La lettura è contestuale, non numerica:

```text
tendenza evolutiva:
  preserva intento e relazioni essenziali
  + aumenta capacità/possibilità pertinente
  +/o riduce contaminazione, dispersione, ricostruzione

tendenza regressiva:
  perde una relazione necessaria
  o separa intento e risultante
  o aggiunge latency/vincoli senza valore compensante
```

Non trasformare questo schema in un gate. Il nuovo non è automaticamente migliore; un tradeoff può restare aperto e una differenza può essere semplicemente non ancora ordinabile.

## Influenza delle risultanti e contesto sostenibile

Approfondimento del 2026-09-16, dalla nota di Graziano sul possibile peso degradante dei risultati accumulati. La nota resta un'ipotesi operativa; questa formulazione non identifica un meccanismo interno del modello né riporta un esperimento controllato.

Una risultante può orientare il seguito perché porta una determinazione, un metodo o una dipendenza ancora necessaria. La sua salienza documentale è un'altra relazione: lunghezza, ripetizione, recenza e lavoro già speso non aggiungono da soli evidenza. Quando una medesima interpretazione passa attraverso più documenti o repository, la sua migliore raggiungibilità non costituisce corroborazione indipendente. Una nuova osservazione o lettura indipendente mantiene invece il proprio contributo, da attribuire esplicitamente. Separare influenza operativa, ragione epistemica, stato implementativo e autorità evita di promuovere una rappresentazione per la sola circolazione.

Anche la partecipazione di una competenza può confermare una determinazione sufficiente senza cambiarla. Il risultato utile non deve essere forzato verso una modifica per mostrare che una competenza ha agito. Il contesto sostenibile mantiene attive le relazioni necessarie alla decisione presente e raggiungibili le ragioni e le aperture che non richiedono lo stesso livello di attenzione. Questo non equivale né a caricare tutto il patrimonio né a cancellare le possibilità rare per ridurre testo.

Nel lavoro della competenza Paper, riconoscere una perdita concreta prima di aggiungere una protezione: un resoconto che sostituisce il problema, una stessa inferenza citata come più prove, una premessa rara ma necessaria non più raggiunta. Correggere allora la relazione causale e la sua espressione, senza istituire un controllo continuo. Nella prossima revisione del manoscritto ricomporre questa precisazione nelle sezioni 3.3–3.6 su attribuzione, obsolescenza, guide e latenza; il corpo 0.3 resta invariato in questo intervento. I casi descritti sono discriminanti concettuali, non risultati sperimentali o misure di risparmio.

## Ritardo d'incarnazione fra relazione e materializzazione

Il primo attraversamento receiver-grounded di MAIOS Project Kernel ha reso concreta una forma particolare del disallineamento. Una relazione può cambiare nel proprio owner semantico mentre una proiezione o un package precedente continua a rappresentare correttamente lo stato da cui era stato generato:

```text
K_semantic(n+1)
while
materialization = incarnation(K_semantic(n))
```

La semplice differenza temporale non è ancora un errore. Diventa causalmente rilevante quando il consumer pretende o necessita la relazione corrente ma incontra l'incarnazione precedente. In quel caso il problema non si risolve aumentando il peso documentale della nuova relazione: occorre seguire il passaggio che doveva materializzarla e correggere il primo owner/consumer che ne perde il significato.

Nel caso MPK osservato il branch sorgente aveva modificato quattro owner semantici mentre il package committato conservava i corpi precedenti. Un test nativo progettato proprio per confrontare owner corrente e delivery ha fallito in quei quattro subcase. Questo è un **esempio software di differenza fra formazione e materializzazione**. Non dimostra che il modello abbia assimilato i nuovi metodi, che la nuova sorgente sia corretta in assoluto o che esista un meccanismo cognitivo nascosto di stale-result bias.

La relazione approfondisce una distinzione già presente nel Paper:

```text
formazione / comprensione
!= rappresentazione persistente
!= consegna al consumer
!= esercizio
!= assimilazione successiva
```

Essa chiarisce anche il rapporto con l'obsolescenza: una materializzazione precedente può restare genealogicamente valida pur perdendo autorità sul presente. Contrarla o sostituirla richiede che le sue funzioni ancora causali — traduzione, accesso, identità, provenance, recovery o altri effetti — continuino altrove. Il disallineamento non autorizza quindi né sincronizzazione automatica né conservazione eterna dell'intermediario.

## Relazione integrata

```text
campo aperto + intento + determinazioni + condizioni presenti
- interferenza introdotta dall'agente
-> convergenza assonante
-> risultante deterministica non prescritta
-> nuovo zero / campo seguente
-> conseguenze
-> differenza causale riusabile?
   no  -> no_change
   sì  -> modifica del generatore / owner pertinente
```

Il corpo 0.3 contiene già evento accoppiato, campo seguente, nucleo generativo autologico, continuità e causal readback. Una revisione futura deve ricomporre questi nessi nel corpo esistente, non aggiungere un capitolo separato per ogni documento di ritorno.

## Confini

Il repository del Paper è pubblico e accademico. Implementazioni operative/private, runtime e prodotti restano owner distinti; il Paper può ricevere conoscenza senza assorbirne automaticamente stato o claim.

Minima azione resta raccordata al D-ND; nessun funzionale d'azione SSK è definito. Il tempo come consecuzione indica riduzione della ricostruzione semantica, non zero computazione. Il caso MPK qui descritto è un esempio implementativo qualificato, non un esperimento cognitivo né una validazione empirica generale di SSK. Nessun nuovo esperimento, peer review o pubblicazione è selezionato da questo consolidamento.