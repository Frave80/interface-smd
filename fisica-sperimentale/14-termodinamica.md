# Capitolo 14 — Termodinamica

La termodinamica nasce nell'Ottocento da un problema eminentemente ingegneristico: capire quanto lavoro si possa ottenere da una macchina a vapore e quali siano i limiti invalicabili del suo rendimento. Da questa domanda pratica si è sviluppata una delle teorie più generali e solide della fisica, capace di descrivere motori, frigoriferi, reazioni chimiche, transizioni di fase, fino alla fisica dei buchi neri. Il primo principio, già incontrato, stabilisce che l'energia si conserva e che calore e lavoro sono due modi di scambiarla; esso però non dice nulla sul **verso** in cui i processi avvengono spontaneamente. In questo capitolo studieremo dapprima i **cicli termodinamici** su cui si basano le macchine reali, poi il **secondo principio**, con i concetti di irreversibilità ed entropia, quindi i **potenziali termodinamici**, che permettono di trattare in modo elegante sistemi in condizioni diverse, e infine il **terzo principio**, che riguarda il comportamento della materia in prossimità dello zero assoluto.

## 14.1 Cicli termodinamici

Un **ciclo termodinamico** è una trasformazione (o una successione di trasformazioni) al termine della quale il sistema torna esattamente nello stato iniziale. Poiché l'energia interna è una funzione di stato, in un ciclo $\Delta U = 0$, e il primo principio impone che il lavoro totale compiuto dal sistema sia uguale al calore totale assorbito:

$$
W = Q = Q_{ass} - |Q_{ced}|.
$$

Nel piano di Clapeyron un ciclo quasistatico è una curva chiusa, e il lavoro netto è l'**area racchiusa** dalla curva: positivo se il ciclo è percorso in senso orario (ciclo motore), negativo se percorso in senso antiorario (ciclo frigorifero). La ragione per cui si studiano i cicli è pratica: una macchina utile deve funzionare in modo continuo, ripetendo indefinitamente le stesse operazioni, e quindi il fluido di lavoro deve periodicamente tornare allo stato iniziale. Le macchine termiche reali (motori a combustione interna, turbine a vapore e a gas, frigoriferi, condizionatori, pompe di calore) sono modellate da cicli ideali costituiti dalle trasformazioni studiate nel capitolo precedente.

### 14.1.1 Macchina termica

Una **macchina termica** (o motore termico) è un dispositivo che, operando ciclicamente, assorbe calore da una o più sorgenti a temperatura elevata e produce lavoro meccanico. Nello schema più semplice la macchina scambia calore con due **serbatoi** (o sorgenti, o termostati): assorbe il calore $Q_C > 0$ da una sorgente calda a temperatura $T_C$, produce il lavoro $W > 0$ e cede il calore $|Q_F|$ a una sorgente fredda a temperatura $T_F < T_C$. Il bilancio energetico su un ciclo è $W = Q_C - |Q_F|$.

Il **rendimento** (o efficienza) di una macchina termica è il rapporto tra ciò che si ottiene (il lavoro) e ciò che si spende (il calore assorbito dalla sorgente calda):

$$
\eta = \frac{W}{Q_C} = 1 - \frac{|Q_F|}{Q_C}.
$$

Poiché il calore ceduto non può mai essere nullo (lo stabilisce il secondo principio), il rendimento è sempre strettamente minore di 1. In un'automobile tipica il rendimento del motore è intorno al 25-35%: più di due terzi dell'energia chimica del carburante finisce in calore disperso dal radiatore e dai gas di scarico. Una centrale termoelettrica moderna a ciclo combinato raggiunge circa il 60%. È importante distinguere il concetto di "sorgente" termodinamica, un corpo ideale a temperatura costante, dal combustibile, che in realtà fornisce calore a temperature variabili; nei modelli ideali la sorgente calda rappresenta la camera di combustione o la caldaia, quella fredda l'ambiente o il condensatore.

### 14.1.2 Macchina frigorifera

Una **macchina frigorifera** funziona come una macchina termica percorsa al contrario: assorbendo il lavoro $|W|$ dall'esterno (tipicamente da un motore elettrico), sottrae il calore $Q_F$ a un corpo freddo a temperatura $T_F$ e cede il calore $|Q_C| = Q_F + |W|$ a un corpo caldo a temperatura $T_C$. È il principio di funzionamento di frigoriferi e condizionatori: il calore viene "pompato" dall'interno freddo all'esterno più caldo, contro il suo verso spontaneo, a spese di lavoro.

L'indice di prestazione di un frigorifero non è chiamato rendimento ma **coefficiente di prestazione** (COP, *coefficient of performance*) o **efficienza frigorifera**:

$$
\varepsilon_f = \frac{Q_F}{|W|} = \frac{Q_F}{|Q_C| - Q_F}.
$$

A differenza del rendimento di un motore, il COP può essere (e di solito è) maggiore di 1: un buon frigorifero domestico ha $\varepsilon_f \simeq 3$, cioè per ogni joule elettrico consumato estrae tre joule di calore dalla cella. Ciò non viola alcun principio, perché il lavoro non viene "trasformato" in freddo: serve soltanto a trasportare calore. Nel frigorifero reale il fluido di lavoro (refrigerante) evapora a bassa pressione nell'evaporatore interno assorbendo calore, viene compresso dal compressore, condensa nel condensatore posto sul retro cedendo calore all'ambiente, e infine si espande attraverso una valvola di laminazione, raffreddandosi, per ricominciare il ciclo.

### 14.1.3 Ciclo di Carnot

Il **ciclo di Carnot** (Sadi Carnot, 1824) è il ciclo reversibile che opera fra due sole sorgenti a temperature $T_C$ e $T_F$. Poiché lo scambio di calore reversibile con una sorgente richiede che il sistema sia alla stessa temperatura della sorgente, e poiché fuori dal contatto con le sorgenti non si può scambiare calore, il ciclo è necessariamente composto da **due isoterme e due adiabatiche reversibili**. Per un gas ideale:

1. **A→B espansione isoterma** a $T_C$: il gas assorbe $Q_C = nRT_C\ln(V_B/V_A)$;
2. **B→C espansione adiabatica**: il gas si raffredda da $T_C$ a $T_F$ compiendo lavoro;
3. **C→D compressione isoterma** a $T_F$: il gas cede $|Q_F| = nRT_F\ln(V_C/V_D)$;
4. **D→A compressione adiabatica**: il gas si riscalda da $T_F$ a $T_C$.

Dalle equazioni delle adiabatiche, $T_C V_B^{\gamma-1} = T_F V_C^{\gamma-1}$ e $T_C V_A^{\gamma-1} = T_F V_D^{\gamma-1}$; dividendo membro a membro si trova $V_B/V_A = V_C/V_D$. I logaritmi si semplificano e

$$
\frac{|Q_F|}{Q_C} = \frac{T_F}{T_C} \qquad\Longrightarrow\qquad \eta_{Carnot} = 1 - \frac{T_F}{T_C}.
$$

Il rendimento del ciclo di Carnot dipende **solo dalle temperature delle sorgenti** e non dalla sostanza di lavoro; come vedremo con il teorema di Carnot, è il massimo rendimento ottenibile da qualunque macchina che operi tra le stesse temperature. Per una centrale con vapore a 800 K e condensatore a 300 K, $\eta_{Carnot} = 62{,}5\%$. Il ciclo di Carnot è un'astrazione: le isoterme reversibili richiedono tempi infinitamente lunghi, e quindi una macchina di Carnot avrebbe potenza nulla. Ha tuttavia un valore concettuale enorme come termine di confronto. Percorso in senso inverso diventa un frigorifero ideale con $\varepsilon_f = T_F/(T_C - T_F)$.

### 14.1.4 Ciclo Stirling

Il **ciclo Stirling** (Robert Stirling, 1816) è composto da **due isoterme e due isocore**: espansione isoterma a $T_C$, raffreddamento isocoro da $T_C$ a $T_F$, compressione isoterma a $T_F$, riscaldamento isocoro da $T_F$ a $T_C$. Nelle due isocore il gas cede e riassorbe la stessa quantità di calore, $nc_V(T_C - T_F)$. Se questo calore viene immagazzinato e poi restituito internamente da un **rigeneratore** (una matrice metallica porosa attraverso cui il gas transita, che si scalda quando il gas caldo passa e restituisce il calore quando passa il gas freddo), gli unici scambi con l'esterno avvengono nelle isoterme, e il rendimento ideale coincide con quello di Carnot:

$$
\eta_{Stirling,rig} = 1 - \frac{T_F}{T_C}.
$$

Senza rigeneratore il rendimento è inferiore, perché il calore delle isocore deve essere fornito dalla sorgente calda. I motori Stirling sono a **combustione esterna**: possono funzionare con qualsiasi sorgente di calore (solare, biomassa, calore di scarto, radioisotopi), sono silenziosi e hanno buoni rendimenti, ma hanno bassa potenza specifica e richiedono grandi scambiatori. Trovano applicazione in impianti solari a concentrazione, in sottomarini e, usati in senso inverso, come criorefrigeratori per raggiungere temperature di poche decine di kelvin.

### 14.1.5 Ciclo Otto

Il **ciclo Otto** (Nikolaus Otto, 1876) è il ciclo ideale dei motori a benzina a quattro tempi con accensione comandata. Il fluido (aria e combustibile, modellati come gas ideale biatomico) percorre:

1. **compressione adiabatica** da $V_1$ a $V_2$ (corsa di compressione);
2. **riscaldamento isocoro** (combustione rapidissima innescata dalla candela, a pistone praticamente fermo al punto morto superiore): il gas assorbe $Q_C = nc_V(T_3 - T_2)$;
3. **espansione adiabatica** da $V_2$ a $V_1$ (corsa utile);
4. **raffreddamento isocoro** (apertura della valvola di scarico): il gas cede $|Q_F| = nc_V(T_4 - T_1)$.

Le fasi di aspirazione e scarico si compensano e non compaiono nel ciclo ideale. Detto $r = V_1/V_2$ il **rapporto di compressione**, dalle adiabatiche $T_2 = T_1 r^{\gamma-1}$ e $T_3 = T_4 r^{\gamma-1}$, da cui

$$
\eta_{Otto} = 1 - \frac{T_4 - T_1}{T_3 - T_2} = 1 - \frac{1}{r^{\gamma-1}}.
$$

Il rendimento cresce con il rapporto di compressione: per $r = 10$ e $\gamma = 1{,}4$ si ottiene $\eta \simeq 60\%$. Il valore reale è molto minore (circa 30%) per attriti, perdite di calore attraverso le pareti, combustione non istantanea e fluido non ideale. Il rapporto di compressione non può essere aumentato a piacere: oltre $r \simeq 10$-$12$ la miscela si autoaccende prima della scintilla per la temperatura raggiunta in compressione (fenomeno della **detonazione** o "battito in testa"), dannoso per il motore. Per questo le benzine sono classificate per numero di ottano, un indice della loro resistenza all'autoaccensione.

### 14.1.6 Ciclo Diesel

Il **ciclo Diesel** (Rudolf Diesel, 1893) modella i motori ad accensione spontanea per compressione. Nel cilindro viene aspirata e compressa sola aria, con rapporti di compressione elevati ($r = 15$-$22$), fino a temperature superiori a quella di autoaccensione del gasolio. Il combustibile viene poi iniettato progressivamente e brucia mentre il pistone scende, mantenendo la pressione circa costante. Il ciclo ideale è quindi:

1. **compressione adiabatica** da $V_1$ a $V_2$;
2. **riscaldamento isobaro** da $V_2$ a $V_3$ (combustione): $Q_C = nc_p(T_3 - T_2)$;
3. **espansione adiabatica** da $V_3$ a $V_1$;
4. **raffreddamento isocoro**: $|Q_F| = nc_V(T_4 - T_1)$.

Introdotto il **rapporto di combustione** (o di introduzione) $\beta = V_3/V_2$, si dimostra che

$$
\eta_{Diesel} = 1 - \frac{1}{\gamma}\,\frac{T_4 - T_1}{T_3 - T_2} = 1 - \frac{1}{r^{\gamma-1}}\,\frac{\beta^{\gamma} - 1}{\gamma\,(\beta - 1)}.
$$

Il fattore $(\beta^\gamma - 1)/[\gamma(\beta-1)]$ è sempre maggiore di 1, quindi, **a parità di rapporto di compressione**, il ciclo Diesel ha rendimento minore del ciclo Otto. Nella pratica però il Diesel lavora con rapporti di compressione molto più alti, senza rischio di detonazione perché il combustibile non è presente durante la compressione, e quindi ha rendimenti complessivi superiori (circa 40% nei motori per autotrazione, fino al 50% nei grandi motori navali). Ciò spiega la sua diffusione nel trasporto pesante.

### 14.1.7 Pompa di calore

Una **pompa di calore** è, dal punto di vista termodinamico, identica a una macchina frigorifera: assorbe lavoro per trasferire calore da un ambiente freddo a uno caldo. Cambia lo scopo: mentre il frigorifero serve a raffreddare l'ambiente freddo, la pompa di calore serve a **riscaldare** l'ambiente caldo (per esempio un'abitazione in inverno), prelevando calore dall'aria esterna, dal terreno o da una falda. Il coefficiente di prestazione è quindi definito rispetto al calore ceduto alla sorgente calda:

$$
\varepsilon_{pdc} = \frac{|Q_C|}{|W|} = \frac{|Q_C|}{|Q_C| - Q_F} = 1 + \varepsilon_f .
$$

Il COP di una pompa di calore è sempre maggiore di 1: il calore fornito all'abitazione è la somma del lavoro elettrico e del calore "gratuito" sottratto all'esterno. Il limite ideale (Carnot inverso) è $\varepsilon_{pdc} = T_C/(T_C - T_F)$: per riscaldare a 20 °C (293 K) prelevando da aria a 0 °C (273 K) si avrebbe un COP teorico di circa 14,7; i dispositivi reali raggiungono valori tra 3 e 5. Il COP diminuisce al crescere della differenza di temperatura, ed è per questo che le pompe di calore rendono meglio in climi miti, con sistemi di distribuzione a bassa temperatura (pavimenti radianti) o con sonde geotermiche, dove la sorgente fredda ha temperatura stabile. Rispetto a una caldaia elettrica a resistenza, che ha "COP" pari a 1, una pompa di calore permette di risparmiare due terzi o più dell'energia elettrica: per questo è una tecnologia chiave nella decarbonizzazione del riscaldamento.

### Esercizio d'esempio

Un motore a ciclo Otto ideale con rapporto di compressione $r = 9{,}0$ aspira aria ($\gamma = 1{,}40$) a $T_1 = 300$ K e $p_1 = 1{,}00\times10^5$ Pa. La combustione porta la temperatura a $T_3 = 2000$ K. Si calcolino temperature, rendimento e lavoro per mole, e lo si confronti con il rendimento di Carnot tra le temperature estreme.

**Soluzione.** Compressione adiabatica: $T_2 = T_1 r^{\gamma-1} = 300\cdot9^{0{,}4} \simeq 300\cdot2{,}41 \simeq 722$ K. Espansione adiabatica: $T_4 = T_3/r^{\gamma-1} = 2000/2{,}41 \simeq 830$ K. Calori per mole ($c_V = 20{,}8$ J/(mol K)):

$$
Q_C = c_V (T_3 - T_2) = 20{,}8\cdot1278 \simeq 2{,}66\times10^4\ \text{J/mol}, \qquad |Q_F| = c_V(T_4 - T_1) = 20{,}8\cdot530 \simeq 1{,}10\times10^4\ \text{J/mol}.
$$

Lavoro: $W = Q_C - |Q_F| \simeq 1{,}56\times10^4$ J/mol. Rendimento: $\eta = W/Q_C \simeq 0{,}585$, in accordo con $1 - 9^{-0{,}4} = 1 - 0{,}415 = 0{,}585$. Carnot tra 2000 K e 300 K: $\eta_C = 1 - 300/2000 = 0{,}85$. Il ciclo Otto ha rendimento inferiore perché il calore è assorbito e ceduto a temperature variabili, non solo agli estremi.

### Punti chiave

- In un ciclo $\Delta U = 0$ e $W = Q_{ass} - |Q_{ced}|$; il lavoro netto è l'area racchiusa nel piano di Clapeyron.
- Macchina termica: $\eta = W/Q_C = 1 - |Q_F|/Q_C < 1$.
- Frigorifero: $\varepsilon_f = Q_F/|W|$; pompa di calore: $\varepsilon_{pdc} = |Q_C|/|W| = 1 + \varepsilon_f$; entrambi possono superare 1.
- Carnot (2 isoterme + 2 adiabatiche): $\eta = 1 - T_F/T_C$, indipendente dalla sostanza; Stirling con rigeneratore raggiunge lo stesso valore.
- Otto (2 adiabatiche + 2 isocore): $\eta = 1 - r^{1-\gamma}$, limitato dalla detonazione.
- Diesel (isobara al posto della prima isocora): a pari $r$ rende meno dell'Otto, ma lavora con $r$ più alti.
- I rendimenti reali sono molto inferiori a quelli ideali per attriti, perdite termiche e irreversibilità.

## 14.2 Secondo principio della termodinamica

Il primo principio stabilisce che l'energia si conserva, ma molti processi che lo rispettano non avvengono mai in natura. Un corpo caldo a contatto con uno freddo cede calore finché le temperature si uguagliano, ma non si è mai visto il processo inverso, in cui il corpo freddo si raffredda ulteriormente scaldando quello caldo, pur conservando l'energia. Un blocco che scivola su un piano scabro si ferma trasformando la sua energia cinetica in calore, ma un blocco fermo non si mette spontaneamente in moto raffreddando il piano. Un gas che si espande liberamente nel vuoto non torna mai da solo nel recipiente di partenza. Il **secondo principio della termodinamica** è la legge che stabilisce il verso dei processi naturali: esistono trasformazioni permesse in un senso e proibite nell'altro. Esso ha diverse formulazioni equivalenti, e la sua espressione più generale e quantitativa è data in termini di una nuova funzione di stato, l'**entropia**.

### 14.2.1 Irreversibilità

Una trasformazione si dice **reversibile** se può essere percorsa in senso inverso in modo che sia il sistema sia l'ambiente tornino esattamente nei rispettivi stati iniziali, senza lasciare traccia alcuna nell'universo. Condizioni necessarie per la reversibilità sono che la trasformazione sia **quasistatica** (successione di stati di equilibrio) e che non vi siano **effetti dissipativi**. Ogni trasformazione che non soddisfa queste condizioni è **irreversibile**.

Le principali cause di irreversibilità sono: l'**attrito** e in generale tutte le forze dissipative (viscosità, resistenza elettrica, isteresi magnetica), che trasformano lavoro in calore; lo **scambio di calore con differenza finita di temperatura**; l'**espansione libera** o comunque le trasformazioni con differenze finite di pressione tra sistema e ambiente; il **mescolamento** di sostanze diverse; le **reazioni chimiche** spontanee. Tutti i processi reali sono irreversibili: le trasformazioni reversibili sono idealizzazioni limite, approssimabili con processi molto lenti e senza attriti, ma mai realizzabili esattamente. Ciò nonostante sono strumenti concettuali fondamentali, perché permettono di calcolare grandezze di stato e di stabilire limiti superiori alle prestazioni delle macchine. Un buon criterio pratico: un processo è irreversibile se, guardandone un filmato al contrario, si riconosce immediatamente che "qualcosa non va".

### 14.2.2 Enunciato di Kelvin-Planck

L'**enunciato di Kelvin-Planck** del secondo principio afferma:

> È impossibile realizzare una trasformazione il cui **unico** risultato sia la conversione in lavoro di calore prelevato da un'unica sorgente a temperatura uniforme.

In altre parole, non può esistere una macchina termica ciclica che assorba calore da una sola sorgente e lo trasformi integralmente in lavoro: ogni macchina termica deve cedere parte del calore a una sorgente più fredda, e quindi $\eta < 1$. Una macchina che violasse questo enunciato sarebbe un **moto perpetuo di seconda specie**: potrebbe, per esempio, far navigare una nave estraendo calore dall'oceano, senza consumare combustibile. Si noti il ruolo cruciale della parola "unico": nell'espansione isoterma di un gas ideale il calore assorbito da un'unica sorgente diventa interamente lavoro, ma il gas cambia stato (aumenta di volume), e quindi la conversione non è l'unico risultato. È proprio la richiesta di ciclicità, cioè di riportare il fluido allo stato iniziale, che impone la cessione di calore a una seconda sorgente.

### 14.2.3 Enunciato di Clausius

L'**enunciato di Clausius** afferma:

> È impossibile realizzare una trasformazione il cui **unico** risultato sia il trasferimento di calore da un corpo a temperatura più bassa a un corpo a temperatura più alta.

Il calore fluisce spontaneamente dal caldo al freddo; per farlo andare in senso opposto serve un intervento esterno, tipicamente lavoro, come avviene nel frigorifero. Un frigorifero che funzionasse senza consumare energia (COP infinito) violerebbe l'enunciato di Clausius.

I due enunciati sono **equivalenti**: la violazione dell'uno implica la violazione dell'altro. Supponiamo infatti di avere una macchina che viola Kelvin-Planck, trasformando integralmente in lavoro $W$ il calore $Q$ preso da una sorgente calda. Usiamo questo lavoro per azionare un frigorifero che estrae $Q_F$ dalla sorgente fredda e cede $Q_F + W$ alla calda. Il sistema combinato, nel complesso, preleva $Q_F$ dalla sorgente fredda e cede $Q_F$ alla calda senza altri effetti: viola Clausius. Viceversa, se esistesse un frigorifero "gratuito" che viola Clausius, potremmo affiancarlo a una normale macchina termica in modo da restituire alla sorgente calda tutto il calore che la macchina cede alla fredda: il sistema combinato assorbirebbe calore solo dalla sorgente calda e lo trasformerebbe integralmente in lavoro, violando Kelvin-Planck.

### 14.2.4 Teorema di Carnot

Il **teorema di Carnot** è la prima conseguenza quantitativa del secondo principio:

> (a) Nessuna macchina termica che operi tra due sorgenti alle temperature $T_C$ e $T_F$ può avere rendimento maggiore di quello di una macchina reversibile che operi tra le stesse sorgenti. (b) Tutte le macchine reversibili che operano tra le stesse due sorgenti hanno lo stesso rendimento.

La dimostrazione è per assurdo. Supponiamo che una macchina $X$ abbia rendimento $\eta_X > \eta_R$, dove $R$ è reversibile. Facciamo funzionare $R$ al contrario, come frigorifero, alimentandolo con il lavoro prodotto da $X$, e regoliamo le macchine in modo che $X$ assorba dalla sorgente calda esattamente il calore che $R$ vi restituisce. Poiché $X$ è più efficiente, produce più lavoro di quanto $R$ ne richieda; il surplus di lavoro può essere ottenuto soltanto da calore netto prelevato dalla sorgente fredda: si sarebbe così costruita una macchina che converte in lavoro calore di un'unica sorgente, in violazione di Kelvin-Planck. Quindi $\eta_X \le \eta_R$. Se anche $X$ è reversibile, si può scambiare il ruolo delle due macchine e ottenere $\eta_R \le \eta_X$, da cui l'uguaglianza.

Poiché tutte le macchine reversibili hanno lo stesso rendimento, possiamo calcolarlo con una sostanza qualsiasi: con il gas ideale abbiamo trovato $\eta_{rev} = 1 - T_F/T_C$. Per qualunque macchina reale, quindi,

$$
\eta \le 1 - \frac{T_F}{T_C},
$$

con l'uguaglianza solo nel caso reversibile. Il teorema stabilisce un limite universale, indipendente dalla tecnologia: per migliorare il rendimento si devono aumentare $T_C$ (limitata dai materiali) o diminuire $T_F$ (limitata dall'ambiente).

### 14.2.5 Equazione di Clapeyron

Una notevole applicazione del teorema di Carnot riguarda le **transizioni di fase**. Consideriamo un ciclo di Carnot infinitesimo eseguito con una sostanza in coesistenza liquido-vapore: un'isoterma a $T + dT$ in cui una massa $m$ evapora alla pressione di vapore $p + dp$, assorbendo il calore latente $Q = m\lambda$, e un'isoterma a $T$ in cui la stessa massa condensa alla pressione $p$; le due adiabatiche sono infinitesime. Nel piano di Clapeyron il ciclo è un piccolo rettangolo di base $m(v_v - v_l)$ (variazione di volume specifico tra vapore e liquido) e altezza $dp$; il lavoro è $dW = m(v_v - v_l)\,dp$. Il rendimento di Carnot è $dW/Q = dT/T$, da cui l'**equazione di Clapeyron** (o di Clausius-Clapeyron):

$$
\frac{dp}{dT} = \frac{\lambda}{T\,(v_v - v_l)},
$$

dove $\lambda$ è il calore latente specifico. Essa dà la pendenza della curva di coesistenza nel diagramma $(T,p)$. Per l'evaporazione, approssimando $v_v \gg v_l$ e trattando il vapore come gas ideale, si ottiene $p(T) \propto e^{-\lambda M/(RT)}$: la pressione di vapore cresce esponenzialmente con la temperatura. È questo il motivo per cui l'acqua bolle a temperature più basse in alta montagna e più alte nella pentola a pressione. Per la fusione del ghiaccio, invece, $v_l < v_s$ (il ghiaccio galleggia), quindi $dp/dT < 0$: aumentando la pressione la temperatura di fusione diminuisce leggermente.

### 14.2.6 Scala termodinamica assoluta

Il teorema di Carnot mostra che, per una macchina reversibile, il rapporto $|Q_F|/Q_C$ dipende **solo** dalle temperature delle sorgenti e non dalla sostanza. Kelvin (1848) sfruttò questa universalità per definire una scala di temperatura indipendente dalle proprietà di qualsiasi materiale: la **scala termodinamica assoluta**, in cui il rapporto tra due temperature è per definizione

$$
\frac{T_F}{T_C} = \frac{|Q_F|}{Q_C}\bigg|_{rev}.
$$

Per fissare l'unità basta assegnare un valore a un punto fisso: storicamente si scelse il punto triplo dell'acqua, $T_{tr} = 273{,}16$ K; dal 2019 il kelvin è definito fissando il valore esatto della costante di Boltzmann. In linea di principio, una temperatura incognita si misura facendo funzionare una macchina di Carnot tra il corpo in esame e il punto di riferimento, e misurando i calori scambiati. Poiché il rapporto di Carnot coincide con quello calcolato per il gas ideale, la scala termodinamica coincide con la scala del termometro a gas ideale: ciò giustifica a posteriori l'uso del gas ideale come termometro di riferimento. Inoltre, poiché $|Q_F|$ non può essere negativo né nullo (per Kelvin-Planck), non esistono temperature negative né la temperatura zero è raggiungibile da un ciclo: lo zero assoluto è un limite.

### 14.2.7 Teorema di Clausius

Riscriviamo il risultato di Carnot assumendo il calore con segno (positivo se assorbito dal sistema): per un ciclo reversibile tra due sorgenti $Q_C/T_C + Q_F/T_F = 0$, mentre per uno irreversibile, dato che $\eta < \eta_{rev}$, si trova $Q_C/T_C + Q_F/T_F < 0$. Generalizzando a un ciclo qualsiasi che scambia calore con molte sorgenti, si ottiene il **teorema di Clausius** (o disuguaglianza di Clausius):

$$
\oint \frac{\delta Q}{T} \le 0,
$$

dove $T$ è la temperatura della sorgente con cui il sistema scambia il calore $\delta Q$, e l'uguaglianza vale se e solo se il ciclo è reversibile. La dimostrazione si ottiene immaginando che ogni scambio di calore $\delta Q_i$ avvenga tramite una macchina di Carnot ausiliaria connessa a un'unica sorgente di riferimento: se la somma fosse positiva, il sistema complessivo trasformerebbe in lavoro calore di un'unica sorgente, violando Kelvin-Planck.

### 14.2.8 Entropia

Per un ciclo reversibile $\oint \delta Q_{rev}/T = 0$. Ne segue che l'integrale di $\delta Q_{rev}/T$ tra due stati $A$ e $B$ non dipende dal cammino reversibile scelto: basta considerare due cammini diversi e combinarli in un ciclo. Esiste quindi una **funzione di stato**, l'**entropia** $S$, definita da

$$
dS = \frac{\delta Q_{rev}}{T}, \qquad S_B - S_A = \int_A^B \frac{\delta Q_{rev}}{T}.
$$

L'unità di misura è J/K. Mentre $\delta Q$ non è un differenziale esatto, la divisione per $T$ lo trasforma in uno esatto: $1/T$ è un **fattore integrante**. Per calcolare la variazione di entropia di una trasformazione **irreversibile** si sfrutta il fatto che $S$ è funzione di stato: si immagina una qualunque trasformazione reversibile tra gli stessi stati iniziale e finale e si calcola l'integrale lungo di essa. Per un gas ideale, per esempio, da $\delta Q_{rev} = nc_V\,dT + p\,dV$ si trova

$$
\Delta S = n c_V \ln\frac{T_B}{T_A} + nR\ln\frac{V_B}{V_A}.
$$

Per una transizione di fase a temperatura costante $\Delta S = m\lambda/T$; per il riscaldamento di un corpo di capacità termica costante $\Delta S = C\ln(T_B/T_A)$. Combinando il teorema di Clausius con un ciclo formato da un tratto irreversibile da $A$ a $B$ e un ritorno reversibile, si ricava la **disuguaglianza fondamentale**:

$$
S_B - S_A \ge \int_A^B \frac{\delta Q}{T},
$$

con l'uguaglianza solo per processi reversibili.

### 14.2.9 Principio di aumento dell'entropia

Applichiamo la disuguaglianza a un **sistema isolato**, che non scambia calore: $\delta Q = 0$, quindi

$$
\Delta S_{isolato} \ge 0 .
$$

È il **principio di aumento dell'entropia**: in un sistema isolato l'entropia non può diminuire; resta costante per trasformazioni reversibili e aumenta per quelle irreversibili. Poiché ogni sistema insieme al suo ambiente costituisce un sistema isolato (l'**universo** termodinamico), si può anche scrivere $\Delta S_{univ} = \Delta S_{sist} + \Delta S_{amb} \ge 0$. L'entropia di un singolo sistema non isolato può benissimo diminuire (un frigorifero riduce l'entropia degli alimenti), ma solo a patto che l'ambiente subisca un aumento di entropia almeno uguale.

Esempi: nell'**espansione libera** di $n$ moli di gas ideale da $V$ a $2V$, $T$ resta costante e $\Delta S = nR\ln2 > 0$, mentre l'ambiente non cambia; nello **scambio di calore** $Q$ tra un corpo caldo a $T_1$ e uno freddo a $T_2$, $\Delta S = Q/T_2 - Q/T_1 > 0$ se $T_1 > T_2$. Il principio di aumento dell'entropia è la formulazione più generale del secondo principio: il verso dei processi spontanei è quello che fa crescere l'entropia dell'universo, e l'equilibrio di un sistema isolato corrisponde al massimo dell'entropia compatibile con i vincoli. Esso definisce una "freccia del tempo" termodinamica.

### 14.2.10 Energia degradata

L'aumento di entropia ha una conseguenza pratica immediata: ogni processo irreversibile riduce la possibilità di ottenere lavoro utile. Supponiamo di disporre di un ambiente a temperatura $T_0$ (la sorgente fredda più bassa disponibile). Si dimostra che, a causa di un processo irreversibile che produce una variazione di entropia dell'universo $\Delta S_{univ}$, la quantità di energia che non può più essere trasformata in lavoro, detta **energia degradata** (o energia inutilizzabile), è

$$
E_{deg} = T_0\,\Delta S_{univ}.
$$

Per esempio, se il calore $Q$ passa direttamente da un corpo a $T_1$ a uno a $T_2 < T_1$, prima del passaggio con una macchina di Carnot tra $T_1$ e $T_0$ se ne sarebbe potuto ricavare il lavoro $Q(1 - T_0/T_1)$, dopo il passaggio solo $Q(1 - T_0/T_2)$: la differenza è $QT_0(1/T_2 - 1/T_1) = T_0\Delta S_{univ}$. L'energia non è scomparsa (il primo principio è rispettato), ma si è "degradata" in una forma meno pregiata. Questo concetto, formalizzato in ingegneria come **exergia** (o disponibilità), mostra che non tutte le forme di energia hanno lo stesso valore: il lavoro meccanico ed elettrico sono energia "nobile", interamente convertibile; il calore ad alta temperatura è parzialmente convertibile; il calore a temperatura ambiente non serve a nulla. Ridurre le irreversibilità significa ridurre lo spreco di energia utile.

### Esercizio d'esempio

Un blocco di rame di massa $m_1 = 1{,}00$ kg a $T_1 = 400$ K viene immerso in $m_2 = 2{,}00$ kg di acqua a $T_2 = 290$ K in un recipiente isolato. Calori specifici: rame $c_1 = 385$ J/(kg K), acqua $c_2 = 4186$ J/(kg K). Si calcolino la temperatura di equilibrio, la variazione di entropia dell'universo e l'energia degradata assumendo $T_0 = 290$ K.

**Soluzione.** Bilancio termico: $m_1c_1(T_1 - T_e) = m_2c_2(T_e - T_2)$, da cui

$$
T_e = \frac{m_1c_1T_1 + m_2c_2T_2}{m_1c_1 + m_2c_2} = \frac{385\cdot400 + 8372\cdot290}{385 + 8372} \simeq \frac{154000 + 2427880}{8757} \simeq 294{,}8\ \text{K}.
$$

Variazioni di entropia (lungo riscaldamenti reversibili ideali):

$$
\Delta S_1 = m_1c_1\ln\frac{T_e}{T_1} = 385\ln\frac{294{,}8}{400} \simeq -117{,}4\ \text{J/K}, \qquad \Delta S_2 = m_2c_2\ln\frac{T_e}{T_2} = 8372\ln\frac{294{,}8}{290} \simeq +138{,}5\ \text{J/K}.
$$

$\Delta S_{univ} \simeq +21{,}0$ J/K $> 0$, come richiesto per un processo spontaneo. Energia degradata: $E_{deg} = T_0\Delta S_{univ} \simeq 290\cdot21{,}0 \simeq 6{,}1$ kJ, cioè il lavoro che si sarebbe potuto ottenere sfruttando la differenza di temperatura con una macchina reversibile anziché mescolare direttamente.

### Punti chiave

- I processi reali sono irreversibili (attriti, scambi di calore con $\Delta T$ finito, espansioni libere, mescolamenti).
- Kelvin-Planck: impossibile convertire integralmente in lavoro, ciclicamente, il calore di un'unica sorgente; Clausius: impossibile trasferire spontaneamente calore dal freddo al caldo. I due enunciati sono equivalenti.
- Teorema di Carnot: $\eta \le 1 - T_F/T_C$, con uguaglianza per tutte le macchine reversibili; definisce la scala termodinamica assoluta.
- Equazione di Clapeyron: $dp/dT = \lambda/[T(v_v - v_l)]$ per le curve di coesistenza di fase.
- Teorema di Clausius $\oint \delta Q/T \le 0$; entropia $dS = \delta Q_{rev}/T$ funzione di stato.
- In un sistema isolato $\Delta S \ge 0$: l'entropia dell'universo cresce nei processi irreversibili.
- Energia degradata $E_{deg} = T_0\Delta S_{univ}$: l'irreversibilità distrugge capacità di produrre lavoro.

## 14.3 Potenziali termodinamici

Il primo e il secondo principio, combinati, permettono di scrivere un'unica relazione fondamentale per le trasformazioni reversibili di un sistema semplice (per esempio un fluido) che scambia solo lavoro di volume. Da $dU = \delta Q - \delta W$, con $\delta Q_{rev} = T\,dS$ e $\delta W = p\,dV$, si ottiene l'**equazione fondamentale della termodinamica**:

$$
dU = T\,dS - p\,dV .
$$

Poiché coinvolge solo funzioni di stato, questa relazione vale per qualunque coppia di stati di equilibrio vicini, anche se il processo reale che li collega è irreversibile. Essa mostra che l'energia interna è naturalmente funzione di entropia e volume, $U = U(S, V)$, e che le sue derivate parziali danno temperatura e pressione. Le variabili $S$ e $V$, tuttavia, non sono sempre le più comode: in laboratorio è facile controllare temperatura e pressione, molto meno l'entropia. Per questo si introducono altre funzioni di stato, i **potenziali termodinamici**, ottenute da $U$ mediante una **trasformata di Legendre**, cioè sottraendo o aggiungendo prodotti di variabili coniugate ($TS$, $pV$). Ogni potenziale ha le sue **variabili naturali**, e conoscerlo in funzione di esse equivale a conoscere completamente le proprietà termodinamiche del sistema. Il nome "potenziale" deriva dall'analogia con l'energia potenziale in meccanica: come un sistema meccanico in equilibrio minimizza la propria energia potenziale, un sistema termodinamico in equilibrio, nelle opportune condizioni di vincolo, minimizza il potenziale termodinamico corrispondente.

### 14.3.1 Energia interna

L'**energia interna** $U(S, V)$ è il primo potenziale termodinamico. Dal differenziale $dU = T\,dS - p\,dV$ si leggono immediatamente le **relazioni di stato**:

$$
T = \left(\frac{\partial U}{\partial S}\right)_V, \qquad p = -\left(\frac{\partial U}{\partial V}\right)_S .
$$

Il significato fisico è diretto: in una trasformazione **adiabatica reversibile** ($dS = 0$) la variazione di energia interna è uguale al lavoro fatto sul sistema, $dU = -p\,dV$; in una trasformazione **isocora** ($dV = 0$) la variazione di energia interna è uguale al calore assorbito, $dU = \delta Q_V$, da cui $C_V = (\partial U/\partial T)_V$. Il criterio di equilibrio associato è il seguente: per un sistema a entropia e volume fissati, l'equilibrio corrisponde al minimo dell'energia interna. Questo criterio è il "duale" del principio di massima entropia per un sistema isolato ($U$ e $V$ fissati). In pratica il vincolo di entropia costante è difficile da imporre, e $U$ si usa soprattutto per sistemi isolati o per trasformazioni adiabatiche e isocore. Per il gas ideale $U = nc_VT$ e, esprimendo $T$ in funzione di $S$ e $V$, si ritrova $U \propto V^{1-\gamma}e^{S/(nc_V)}$, da cui derivando si ottiene l'equazione di stato: un esempio di come un potenziale nelle sue variabili naturali contenga tutta l'informazione sul sistema.

### 14.3.2 Entalpia

L'**entalpia** è definita come

$$
H = U + pV, \qquad dH = T\,dS + V\,dp ,
$$

ed è naturalmente funzione di entropia e pressione, $H(S, p)$. Le sue derivate sono $T = (\partial H/\partial S)_p$ e $V = (\partial H/\partial p)_S$. Il significato fisico più importante è che, in una trasformazione **isobara**, la variazione di entalpia è uguale al calore scambiato: $dH = \delta Q_p$, quindi $C_p = (\partial H/\partial T)_p$. Poiché moltissimi processi chimici, biologici e industriali avvengono a pressione atmosferica costante, l'entalpia è la grandezza naturale per esprimere i bilanci di calore: i **calori di reazione**, i **calori latenti** di fusione e di evaporazione e i poteri calorifici dei combustibili sono variazioni di entalpia tabulate.

L'entalpia è centrale anche nell'ingegneria dei **sistemi aperti** con flusso stazionario (turbine, compressori, ugelli, scambiatori): il bilancio energetico di un fluido che attraversa un dispositivo, trascurando energie cinetica e potenziale, si scrive $\dot Q - \dot W_{albero} = \dot m\,(h_{uscita} - h_{ingresso})$, dove $h$ è l'entalpia specifica; il termine $pV$ rappresenta il **lavoro di pulsione** necessario per spingere il fluido dentro e fuori dal dispositivo. Una conseguenza è che in una **laminazione** adiabatica attraverso una valvola, senza lavoro, l'entalpia si conserva: è il processo isentalpico dell'effetto Joule-Thomson. Per un gas ideale $H = nc_pT$, quindi anche l'entalpia dipende solo dalla temperatura e l'espansione di Joule-Thomson non produce variazioni di temperatura.

### 14.3.3 Energia libera di Helmholtz

L'**energia libera di Helmholtz** è definita come

$$
F = U - TS, \qquad dF = -S\,dT - p\,dV ,
$$

con variabili naturali temperatura e volume, $F(T, V)$, e derivate $S = -(\partial F/\partial T)_V$, $p = -(\partial F/\partial V)_T$. Il suo significato fisico emerge considerando un sistema a contatto con un termostato a temperatura $T$. Dalla disuguaglianza di Clausius $\delta Q \le T\,dS$ e dal primo principio si ricava che il lavoro compiuto dal sistema in una trasformazione isoterma soddisfa

$$
W \le -\Delta F ,
$$

con l'uguaglianza solo nel caso reversibile. La diminuzione dell'energia libera di Helmholtz rappresenta quindi il **massimo lavoro** che un sistema può compiere a temperatura costante: è la parte "libera", cioè utilizzabile, dell'energia interna, mentre il termine $TS$ rappresenta una parte "vincolata", che deve necessariamente essere scambiata come calore con il termostato. Il criterio di equilibrio è: per un sistema a $T$ e $V$ costanti, i processi spontanei fanno diminuire $F$, e l'equilibrio corrisponde al minimo di $F$. Questo esprime una competizione tra energia ed entropia: a bassa temperatura prevale la tendenza a minimizzare $U$ (ordine, cristallizzazione), ad alta temperatura prevale la tendenza a massimizzare $S$ (disordine, fusione, evaporazione). L'energia libera di Helmholtz è la grandezza più direttamente collegata alla meccanica statistica, dove si ottiene dalla funzione di partizione come $F = -k_BT\ln Z$.

### 14.3.4 Energia libera di Gibbs

L'**energia libera di Gibbs** (o entalpia libera) è definita come

$$
G = H - TS = U + pV - TS, \qquad dG = -S\,dT + V\,dp ,
$$

con variabili naturali temperatura e pressione, $G(T, p)$, e derivate $S = -(\partial G/\partial T)_p$, $V = (\partial G/\partial p)_T$. Poiché temperatura e pressione sono le variabili più facilmente controllabili in laboratorio e nei processi naturali (un recipiente aperto all'atmosfera e in equilibrio termico con l'ambiente), $G$ è il potenziale più usato in chimica e in scienza dei materiali. Il suo criterio di equilibrio è: **a $T$ e $p$ costanti, i processi spontanei fanno diminuire $G$**, e l'equilibrio corrisponde al suo minimo. La diminuzione $-\Delta G$ è il massimo lavoro utile, diverso dal lavoro di volume contro l'atmosfera, che il sistema può fornire: per esempio il lavoro elettrico di una pila o di una cella a combustibile, la cui forza elettromotrice è $\mathcal{E} = -\Delta G/(zF)$ con $F$ costante di Faraday.

Il segno di $\Delta G = \Delta H - T\Delta S$ decide la spontaneità di una reazione chimica: una reazione esotermica ($\Delta H < 0$) con aumento di entropia ($\Delta S > 0$) è sempre spontanea; una endotermica con diminuzione di entropia non lo è mai; negli altri casi la temperatura decide. Nelle **transizioni di fase**, le due fasi coesistono in equilibrio quando le loro energie libere di Gibbs molari (potenziali chimici) sono uguali; imponendo che restino uguali lungo la curva di coesistenza, $dg_1 = dg_2$, si ritrova elegantemente l'equazione di Clapeyron: $-s_1\,dT + v_1\,dp = -s_2\,dT + v_2\,dp$, da cui $dp/dT = (s_2 - s_1)/(v_2 - v_1) = \lambda/[T(v_2 - v_1)]$.

### 14.3.5 Relazioni di Maxwell

Poiché i potenziali termodinamici sono funzioni di stato, i loro differenziali sono **esatti** e le derivate seconde miste non dipendono dall'ordine di derivazione (teorema di Schwarz). Applicando questa proprietà ai quattro differenziali si ottengono le **relazioni di Maxwell**:

$$
\left(\frac{\partial T}{\partial V}\right)_S = -\left(\frac{\partial p}{\partial S}\right)_V \quad (\text{da } U), \qquad \left(\frac{\partial T}{\partial p}\right)_S = \left(\frac{\partial V}{\partial S}\right)_p \quad (\text{da } H),
$$

$$
\left(\frac{\partial S}{\partial V}\right)_T = \left(\frac{\partial p}{\partial T}\right)_V \quad (\text{da } F), \qquad \left(\frac{\partial S}{\partial p}\right)_T = -\left(\frac{\partial V}{\partial T}\right)_p \quad (\text{da } G).
$$

La loro utilità è enorme: permettono di esprimere derivate che coinvolgono l'entropia, non misurabile direttamente, in termini di derivate di $p$, $V$, $T$, che si ricavano dall'equazione di stato o da misure di dilatazione e compressibilità. Un esempio classico è l'**equazione dell'energia**: da $dU = T\,dS - p\,dV$, a $T$ costante, e usando la relazione di Maxwell da $F$,

$$
\left(\frac{\partial U}{\partial V}\right)_T = T\left(\frac{\partial p}{\partial T}\right)_V - p .
$$

Per il gas ideale $T(\partial p/\partial T)_V = nRT/V = p$, quindi $(\partial U/\partial V)_T = 0$: l'energia interna non dipende dal volume. È esattamente il risultato dell'esperimento di Joule, qui ricavato dalla sola equazione di stato e dal secondo principio. Per un gas di Van der Waals si trova invece $(\partial U/\partial V)_T = an^2/V^2$: l'energia interna aumenta con il volume perché bisogna compiere lavoro contro le forze attrattive. Analogamente si dimostra la relazione generale $C_p - C_V = TV\alpha^2/\kappa_T$, dove $\alpha$ è il coefficiente di dilatazione volumica e $\kappa_T$ la compressibilità isoterma: essa generalizza la relazione di Mayer a qualunque sostanza e mostra che $C_p \ge C_V$ sempre.

### Esercizio d'esempio

Si consideri la combustione dell'idrogeno a $T = 298$ K e $p = 1$ atm: $\text{H}_2 + \tfrac12\text{O}_2 \to \text{H}_2\text{O}$ (liquida), con $\Delta H = -285{,}8$ kJ/mol e $\Delta S = -163{,}3$ J/(mol K). Si calcolino $\Delta G$, il massimo lavoro elettrico ottenibile in una cella a combustibile, il calore scambiato in condizioni reversibili e la forza elettromotrice della cella ($z = 2$, $F = 96\,485$ C/mol).

**Soluzione.** 

$$
\Delta G = \Delta H - T\Delta S = -285{,}8\times10^3 - 298\cdot(-163{,}3) \simeq -285{,}8\times10^3 + 48{,}7\times10^3 \simeq -237{,}1\ \text{kJ/mol}.
$$

Il massimo lavoro utile per mole di idrogeno è $W_{max} = -\Delta G \simeq 237$ kJ. In condizioni reversibili la cella cede all'ambiente il calore $Q = T\Delta S \simeq -48{,}7$ kJ/mol: anche il processo ideale non può convertire in lavoro tutta l'entalpia di reazione, perché l'entropia del sistema diminuisce e deve essere compensata. Il rendimento ideale della cella è $\Delta G/\Delta H \simeq 83\%$, non limitato da Carnot perché non si tratta di una macchina termica. La forza elettromotrice vale $\mathcal{E} = -\Delta G/(zF) = 237{,}1\times10^3/(2\cdot96\,485) \simeq 1{,}23$ V, valore ben noto per la cella idrogeno-ossigeno.

### Punti chiave

- L'equazione fondamentale $dU = T\,dS - p\,dV$ combina primo e secondo principio e vale tra stati di equilibrio qualsiasi.
- I potenziali si ottengono per trasformata di Legendre: $U(S,V)$, $H = U + pV\ (S,p)$, $F = U - TS\ (T,V)$, $G = H - TS\ (T,p)$.
- $\Delta U = Q$ a volume costante, $\Delta H = Q$ a pressione costante; $C_V = (\partial U/\partial T)_V$, $C_p = (\partial H/\partial T)_p$.
- $-\Delta F$ è il massimo lavoro a $T$ costante; $-\Delta G$ il massimo lavoro utile a $T$ e $p$ costanti.
- All'equilibrio il potenziale appropriato ai vincoli è minimo; $\Delta G < 0$ indica un processo spontaneo a $T$ e $p$ costanti.
- Le relazioni di Maxwell derivano dall'esattezza dei differenziali e permettono di calcolare grandezze entropiche dall'equazione di stato.

## 14.4 Terzo principio della termodinamica

Il secondo principio definisce l'entropia solo a meno di una costante additiva: la relazione $dS = \delta Q_{rev}/T$ permette di calcolare **differenze** di entropia tra due stati, ma non il valore assoluto. Per molte applicazioni questo è sufficiente, ma in chimica fisica si pone un problema concreto: per prevedere l'equilibrio di una reazione occorre conoscere la variazione di entropia tra reagenti e prodotti, che sono sostanze diverse, non collegabili tra loro da una trasformazione reversibile semplice. Serve dunque un riferimento comune per le entropie di tutte le sostanze. Inoltre, all'inizio del Novecento, le misure di calori specifici a bassa temperatura rivelavano comportamenti inspiegabili con la fisica classica: i calori specifici dei solidi tendevano a zero al diminuire della temperatura, contro la previsione di Dulong e Petit. Il **terzo principio della termodinamica**, formulato da Walther Nernst tra il 1906 e il 1912 e successivamente precisato da Max Planck, risponde a entrambe le questioni, fissando il comportamento dell'entropia in prossimità dello zero assoluto. A differenza del primo e del secondo principio, che hanno origine classica, il terzo principio ha una giustificazione profonda solo in meccanica quantistica e statistica.

### 14.4.1 Terzo principio della termodinamica

Nernst, studiando le reazioni chimiche tra solidi a temperature via via più basse, osservò che la variazione di energia libera $\Delta G$ e la variazione di entalpia $\Delta H$ di una reazione tendono a coincidere al tendere di $T$ a zero e, inoltre, che si avvicinano l'una all'altra con tangente orizzontale. Poiché $\Delta G = \Delta H - T\Delta S$, questo comportamento implica che anche $\Delta S$ tenda a zero. Ne nasce il **teorema del calore di Nernst**:

> Al tendere della temperatura assoluta a zero, la variazione di entropia associata a qualunque trasformazione isoterma reversibile tra stati di equilibrio tende a zero:
> $$\lim_{T\to0}\,\Delta S_T = 0 .$$

In altre parole, allo zero assoluto tutti gli stati di equilibrio di un sistema (per esempio a pressioni diverse, o in fasi cristalline diverse) hanno la stessa entropia. Le curve isoterme e le curve adiabatiche reversibili, che a temperature ordinarie sono ben distinte, tendono a confondersi nell'avvicinarsi a $T = 0$.

Da questa formulazione discende una conseguenza fondamentale, spesso assunta come enunciato alternativo del terzo principio: il **principio di irraggiungibilità dello zero assoluto**.

> È impossibile raggiungere lo zero assoluto mediante un numero finito di operazioni.

Il ragionamento si capisce con il metodo di raffreddamento per **demagnetizzazione adiabatica**, con cui si raggiungono le temperature più basse. Un sale paramagnetico viene magnetizzato isotermicamente a contatto con un bagno freddo (l'entropia diminuisce perché i momenti magnetici si allineano), poi isolato e smagnetizzato adiabaticamente (l'entropia resta costante e quindi la temperatura scende). Ripetendo il ciclo si scende sempre più in basso. Nel diagramma $(T, S)$ le curve dell'entropia a campo nullo e a campo applicato convergono nello stesso punto a $T = 0$, per il teorema di Nernst: quindi ogni passo successivo produce un abbassamento di temperatura sempre più piccolo, e servirebbero infiniti passi per raggiungere lo zero. Con tecniche di questo tipo, e con raffreddamento laser e evaporativo per gas atomici, si sono raggiunte temperature di frazioni di nanokelvin, ma mai esattamente lo zero.

Il terzo principio ha conseguenze misurabili sul comportamento delle grandezze termodinamiche. Poiché l'entropia a una temperatura $T$ si ottiene come

$$
S(T) - S(0) = \int_0^T \frac{C(T')}{T'}\,dT',
$$

l'integrale deve essere finito, il che impone che **le capacità termiche tendano a zero** per $T \to 0$ (altrimenti l'integrando divergerebbe come $1/T'$ e l'integrale come un logaritmo). È esattamente quanto osservato: nei solidi isolanti a bassa temperatura il calore specifico va come $T^3$ (**legge di Debye**), nei metalli c'è anche un contributo elettronico proporzionale a $T$. Il fallimento della legge di Dulong e Petit è quindi richiesto dal terzo principio. Analogamente, tendono a zero il coefficiente di dilatazione termica e la pendenza delle curve di coesistenza di fase: per esempio la curva di fusione dell'elio-4 diventa orizzontale vicino allo zero assoluto, come richiesto dall'equazione di Clapeyron con $\Delta S \to 0$. Un'ulteriore conseguenza è che il gas ideale classico, la cui entropia contiene un termine $nc_V\ln T$ che diverge per $T \to 0$, è incompatibile con il terzo principio: a temperature bassissime ogni gas deve comportarsi in modo quantistico (o, più realisticamente, condensa).

### 14.4.2 Ipotesi di Nernst-Planck

Il teorema di Nernst afferma che le differenze di entropia si annullano allo zero assoluto, ma non dice quanto valga l'entropia in quel punto. Planck (1911) ne propose una formulazione più forte, nota come **ipotesi di Nernst-Planck** o enunciato di Planck del terzo principio:

> L'entropia di una sostanza pura in forma di **cristallo perfetto** tende a zero quando la temperatura tende allo zero assoluto:
> $$\lim_{T\to0} S = 0 .$$

Questa scelta fissa la costante additiva dell'entropia in modo universale e permette di definire l'**entropia assoluta** (o terza-principio) di ogni sostanza, misurabile per via calorimetrica: si integra $C_p/T$ dal più basso valore di temperatura accessibile (estrapolando con la legge di Debye fino a zero) e si aggiungono i contributi $\Delta H_{tr}/T_{tr}$ di tutte le transizioni di fase incontrate. Le **entropie molari standard** tabulate nei manuali di chimica, per esempio circa 70 J/(mol K) per l'acqua liquida e 189 J/(mol K) per il vapore a 298 K, sono ottenute proprio in questo modo e consentono di calcolare $\Delta S$ e quindi $\Delta G$ di qualunque reazione a partire dai soli dati termici, senza dover misurare costanti di equilibrio.

Il significato microscopico dell'ipotesi diventa chiaro con la relazione di Boltzmann $S = k_B\ln W$, che sarà discussa nel prossimo capitolo: l'entropia è proporzionale al logaritmo del numero di microstati compatibili con lo stato macroscopico. Allo zero assoluto un sistema quantistico si trova nel suo **stato fondamentale**; se questo è unico (non degenere), come avviene per un cristallo perfetto in cui ogni atomo occupa una posizione reticolare ben precisa, allora $W = 1$ e $S = k_B\ln1 = 0$. Il terzo principio è quindi, in ultima analisi, una conseguenza della natura quantistica della materia: in fisica classica le energie possono variare con continuità e il concetto di "numero di stati" perde significato assoluto.

L'ipotesi di Planck ammette eccezioni apparenti ben note, che ne confermano lo spirito. Alcune sostanze conservano un'**entropia residua** a temperature bassissime perché non riescono a raggiungere il vero equilibrio in tempi sperimentali: è il caso del monossido di carbonio solido, le cui molecole CO possono orientarsi indifferentemente come CO oppure OC nel reticolo, "congelando" un disordine con entropia residua prossima a $R\ln2 \simeq 5{,}8$ J/(mol K); oppure del ghiaccio comune, in cui la disposizione degli atomi di idrogeno nei legami a idrogeno ha molte configurazioni equivalenti (entropia residua di Pauling, circa 3,4 J/(mol K)). Anche i vetri, solidi amorfi, sono stati di non equilibrio con entropia residua. In tutti questi casi il sistema non è un cristallo perfetto in equilibrio, e quindi l'ipotesi di Nernst-Planck non si applica: le misure calorimetriche sottostimano l'entropia "vera", e il confronto con il valore calcolato dalla meccanica statistica rivela proprio il disordine congelato.

### Esercizio d'esempio

A bassissima temperatura il calore specifico molare di un solido isolante segue la legge di Debye, $c(T) = A\,T^3$. Per un certo cristallo si misura $c = 0{,}20$ J/(mol K) a $T_1 = 10$ K. Si calcolino l'entropia molare a 10 K, assumendo valida l'ipotesi di Nernst-Planck, e il calore necessario per riscaldare una mole da 0 a 10 K.

**Soluzione.** Dalla misura si ricava $A = c/T_1^3 = 0{,}20/1000 = 2{,}0\times10^{-4}$ J/(mol K$^4$). L'entropia, con $S(0) = 0$:

$$
S(T_1) = \int_0^{T_1}\frac{A\,T^3}{T}\,dT = \frac{A\,T_1^3}{3} = \frac{c(T_1)}{3} = \frac{0{,}20}{3} \simeq 6{,}7\times10^{-2}\ \text{J/(mol K)}.
$$

Il calore:

$$
Q = \int_0^{T_1} A\,T^3\,dT = \frac{A\,T_1^4}{4} = \frac{2{,}0\times10^{-4}\cdot10^4}{4} = 0{,}50\ \text{J/mol}.
$$

Si noti che l'integrale dell'entropia converge solo perché $c \to 0$ per $T \to 0$, come richiesto dal terzo principio; con un calore specifico costante (Dulong e Petit, circa 25 J/(mol K)) l'integrale divergerebbe logaritmicamente.

### Punti chiave

- Il secondo principio definisce l'entropia a meno di una costante; il terzo principio ne fissa il comportamento per $T \to 0$.
- Teorema di Nernst: le variazioni di entropia nelle trasformazioni isoterme tendono a zero per $T \to 0$.
- Principio di irraggiungibilità: lo zero assoluto non si raggiunge con un numero finito di operazioni.
- Conseguenze: capacità termiche, coefficienti di dilatazione e pendenze delle curve di coesistenza tendono a zero (legge di Debye $c \propto T^3$).
- Ipotesi di Nernst-Planck: l'entropia di un cristallo perfetto tende a zero, permettendo di definire entropie assolute dai dati calorimetrici.
- Interpretazione microscopica: stato fondamentale non degenere, $W = 1$, $S = k_B\ln1 = 0$; entropie residue (CO, ghiaccio, vetri) indicano disordine congelato.
