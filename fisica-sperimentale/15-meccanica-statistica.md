# Capitolo 15 — Meccanica statistica

La termodinamica descrive i sistemi macroscopici con poche variabili (pressione, volume, temperatura, entropia) e leggi generali, senza fare alcuna ipotesi sulla struttura microscopica della materia. La teoria cinetica dei gas ha mostrato che alcune di queste grandezze possono essere interpretate come medie di proprietà molecolari. La **meccanica statistica**, fondata da Maxwell, Boltzmann e Gibbs nella seconda metà dell'Ottocento, porta questo programma alle estreme conseguenze: considera un sistema composto da un numero enorme di particelle, rinuncia a seguirne il moto individuale (impossibile e del resto inutile) e ne descrive il comportamento collettivo con gli strumenti del calcolo delle probabilità. Le leggi della termodinamica emergono allora come leggi statistiche, valide con certezza pratica grazie al numero gigantesco di particelle in gioco. In questo capitolo introduttivo studieremo due risultati fondamentali: la **distribuzione di Maxwell-Boltzmann**, che descrive come velocità ed energie si distribuiscono tra le molecole di un gas in equilibrio, e l'**interpretazione statistica dell'entropia** data dalla relazione di Boltzmann, che collega il secondo principio al concetto di probabilità e di disordine.

## 15.1 Distribuzione di Maxwell-Boltzmann

Nella teoria cinetica abbiamo usato soltanto valori medi, come la velocità quadratica media $v_{qm} = \sqrt{3k_BT/m}$. In realtà le molecole di un gas non hanno tutte la stessa velocità: gli urti continui ridistribuiscono incessantemente l'energia, e in ogni istante alcune molecole sono quasi ferme, altre molto veloci. Una singola molecola cambia velocità miliardi di volte al secondo, e seguirla è privo di senso; ha invece pieno significato chiedersi quale **frazione** delle molecole abbia, in un dato istante, velocità compresa in un certo intervallo. Per un gas in equilibrio questa frazione è costante nel tempo, anche se le molecole che la compongono cambiano di continuo: si tratta di un **equilibrio statistico** (o dinamico). James Clerk Maxwell ricavò la forma di questa distribuzione nel 1860, con un argomento basato su ipotesi di simmetria; Ludwig Boltzmann la generalizzò al caso di molecole soggette a forze esterne e la giustificò dinamicamente con il suo teorema H. Il risultato, verificato sperimentalmente con grande precisione, è uno dei pilastri della fisica statistica.

### 15.1.1 Velocità

Si definisce la **funzione di distribuzione** $f(\vec v)$ in modo che $f(\vec v)\,d^3v$ sia la probabilità che una molecola abbia velocità con componenti comprese tra $v_x$ e $v_x + dv_x$, $v_y$ e $v_y + dv_y$, $v_z$ e $v_z + dv_z$; equivalentemente, $N f(\vec v)\,d^3v$ è il numero medio di molecole in quell'intervallo. La funzione è normalizzata: $\int f\,d^3v = 1$.

L'argomento di Maxwell si basa su due ipotesi. Prima: **isotropia**, cioè in un gas in equilibrio non ci sono direzioni privilegiate, quindi $f$ può dipendere solo dal modulo della velocità, $f(\vec v) = \phi(v^2)$. Seconda: **indipendenza** delle tre componenti cartesiane, cioè la probabilità di avere un certo $v_x$ non dipende dai valori di $v_y$ e $v_z$, quindi $f(\vec v) = g(v_x)\,g(v_y)\,g(v_z)$. L'unica funzione che soddisfa contemporaneamente $g(v_x)g(v_y)g(v_z) = \phi(v_x^2 + v_y^2 + v_z^2)$ è l'esponenziale di una forma quadratica: $g(v_x) = A\,e^{-\beta' v_x^2}$, con $\beta' > 0$ perché la probabilità deve diminuire per velocità grandi. Normalizzando e imponendo che l'energia cinetica media per componente sia $\tfrac12 k_BT$ (teorema di equipartizione), si ottiene per ciascuna componente una **distribuzione gaussiana** centrata in zero:

$$
g(v_x) = \sqrt{\frac{m}{2\pi k_BT}}\;\exp\!\left(-\frac{m v_x^2}{2k_BT}\right).
$$

La varianza di ciascuna componente è $k_BT/m$: più alta è la temperatura o più leggera la molecola, più larga è la distribuzione. Il valore medio di $v_x$ è nullo, come deve essere in un gas fermo nel suo insieme.

Spesso interessa la distribuzione del **modulo** della velocità $v$, indipendentemente dalla direzione. Nello spazio delle velocità, i vettori di modulo compreso tra $v$ e $v + dv$ occupano un guscio sferico di volume $4\pi v^2\,dv$. Moltiplicando la densità $f$ per questo volume si ottiene la **distribuzione di Maxwell delle velocità**:

$$
F(v)\,dv = 4\pi \left(\frac{m}{2\pi k_BT}\right)^{3/2} v^2 \exp\!\left(-\frac{m v^2}{2k_BT}\right) dv .
$$

La forma di $F(v)$ risulta dalla competizione tra due fattori: il fattore $v^2$, di origine geometrica, che cresce con $v$ perché ci sono "più modi" di avere velocità grandi (il guscio sferico è più ampio), e il fattore esponenziale, che rende improbabili le velocità con energia cinetica molto maggiore di $k_BT$. Ne risulta una curva che parte da zero, raggiunge un massimo e poi decresce rapidamente, con una "coda" asimmetrica verso le velocità alte. Al crescere della temperatura il massimo si sposta verso destra e si abbassa, mentre l'area totale resta pari a 1.

Dalla distribuzione si ricavano tre velocità caratteristiche. La **velocità più probabile**, dove $F(v)$ ha il massimo (si ottiene ponendo $dF/dv = 0$):

$$
v_p = \sqrt{\frac{2k_BT}{m}} = \sqrt{\frac{2RT}{M}} .
$$

La **velocità media**, $\langle v\rangle = \int_0^\infty v\,F(v)\,dv$:

$$
\langle v\rangle = \sqrt{\frac{8k_BT}{\pi m}} \simeq 1{,}128\,v_p .
$$

La **velocità quadratica media**, $v_{qm} = \sqrt{\langle v^2\rangle}$:

$$
v_{qm} = \sqrt{\frac{3k_BT}{m}} \simeq 1{,}225\,v_p .
$$

Vale sempre $v_p < \langle v\rangle < v_{qm}$, a causa dell'asimmetria della distribuzione. Le tre velocità hanno usi diversi: $v_{qm}$ determina l'energia cinetica e la pressione, $\langle v\rangle$ interviene nel calcolo della frequenza degli urti e del flusso di molecole attraverso un foro (effusione), $v_p$ è il valore più "tipico". Per l'azoto a 300 K valgono rispettivamente circa 422, 476 e 517 m/s.

La distribuzione di Maxwell fu verificata direttamente con esperimenti a **fascio molecolare**. Nell'apparato di Stern (1920) e, con maggiore precisione, in quello di Miller e Kusch (1955), un fascio di atomi esce da un forno attraverso una fenditura e attraversa un **selettore di velocità** costituito da dischi (o da un cilindro con scanalature elicoidali) in rotazione: solo gli atomi con una precisa velocità riescono a passare le fenditure allineate in successione. Variando la velocità di rotazione e contando gli atomi trasmessi, si ricostruisce la distribuzione, che risulta in ottimo accordo con la previsione teorica (con un fattore $v$ aggiuntivo dovuto al fatto che le molecole veloci escono dal forno più frequentemente).

La coda ad alta velocità della distribuzione ha conseguenze importanti. Poiché la frazione di molecole con velocità molto superiore a $v_p$ decresce esponenzialmente ma non è mai nulla, in ogni gas esistono molecole capaci di superare barriere energetiche ben maggiori dell'energia media: è il meccanismo dell'**evaporazione** di un liquido al di sotto della temperatura di ebollizione (le molecole più veloci sfuggono dalla superficie, e il liquido si raffredda), della fuga di gas leggeri dalle atmosfere planetarie e dell'aumento rapidissimo delle velocità di reazione chimica con la temperatura.

### 15.1.2 Energia

È spesso più conveniente esprimere la distribuzione in funzione dell'**energia cinetica** $E = \tfrac12 mv^2$. Cambiando variabile, con $v = \sqrt{2E/m}$ e $dv = dE/\sqrt{2mE}$, la frazione di molecole con energia tra $E$ ed $E + dE$ è

$$
F(E)\,dE = \frac{2}{\sqrt\pi}\,\frac{1}{(k_BT)^{3/2}}\,\sqrt{E}\;e^{-E/k_BT}\,dE .
$$

Si noti che questa distribuzione **non dipende dalla massa** delle molecole: a parità di temperatura, gas diversi hanno la stessa distribuzione di energia, anche se hanno distribuzioni di velocità diverse. È la forma statistica del fatto che l'energia cinetica media dipende solo dalla temperatura. L'energia più probabile è $E_p = \tfrac12 k_BT$ (diversa da $\tfrac12 m v_p^2 = k_BT$, perché il cambio di variabile deforma la distribuzione), mentre l'energia media è, come atteso,

$$
\langle E\rangle = \int_0^\infty E\,F(E)\,dE = \frac{3}{2}k_BT .
$$

Il fattore $\sqrt E$ è legato al numero di stati disponibili con una data energia (la "densità degli stati" nello spazio delle velocità), mentre il fattore esponenziale $e^{-E/k_BT}$ è il celebre **fattore di Boltzmann**. Boltzmann mostrò che esso ha validità generalissima: per un sistema in equilibrio termico a temperatura $T$, la probabilità di trovare una particella in uno stato di energia $E$ è proporzionale a $e^{-E/k_BT}$, dove $E$ comprende non solo l'energia cinetica, ma anche quella potenziale in un campo esterno e quella dei gradi di libertà interni. Questa è la **distribuzione di Maxwell-Boltzmann** nella sua forma generale:

$$
P(E) \propto g(E)\,e^{-E/k_BT},
$$

con $g(E)$ numero (o densità) di stati con energia $E$.

Un'applicazione immediata è la **legge barometrica**. Le molecole di un'atmosfera isoterma nel campo gravitazionale hanno energia potenziale $mgz$; la densità numerica alla quota $z$ è quindi proporzionale al fattore di Boltzmann:

$$
n(z) = n(0)\,e^{-mgz/k_BT} = n(0)\,e^{-z/H}, \qquad H = \frac{k_BT}{mg} = \frac{RT}{Mg} .
$$

L'altezza di scala $H$ per l'aria a 288 K è circa 8,4 km: ogni 8 km circa la pressione si riduce di un fattore $e$. La stessa legge fu usata da Jean Perrin (1909) per misurare il numero di Avogadro osservando al microscopio la distribuzione in altezza di piccole particelle colloidali sospese in un liquido: una delle prove decisive della realtà degli atomi.

Il fattore di Boltzmann spiega anche la **legge di Arrhenius** per la velocità delle reazioni chimiche, $k \propto e^{-E_a/k_BT}$: perché una reazione avvenga, le molecole devono superare una barriera di energia di attivazione $E_a$, e la frazione di molecole con energia sufficiente cresce esponenzialmente con la temperatura. Con $E_a \simeq 0{,}5$ eV, un aumento di temperatura da 300 K a 310 K raddoppia circa la velocità di reazione: ecco perché una febbre di pochi gradi altera il metabolismo, e perché i cibi si conservano meglio in frigorifero. Lo stesso fattore governa la popolazione dei livelli energetici atomici e molecolari, la conduzione nei semiconduttori (numero di elettroni eccitati in banda di conduzione), l'emissione termoionica e il "congelamento" dei gradi di libertà vibrazionali discusso nel capitolo 13: quando la spaziatura dei livelli $\Delta E$ è molto maggiore di $k_BT$, il fattore $e^{-\Delta E/k_BT}$ è piccolissimo e il livello eccitato è praticamente vuoto. La distribuzione di Maxwell-Boltzmann è valida finché le particelle si possono considerare **distinguibili** e classiche, cioè quando la distanza media tra le particelle è molto maggiore della loro lunghezza d'onda di de Broglie termica; a temperature molto basse o densità molto alte (elettroni in un metallo, gas atomici ultrafreddi) va sostituita dalle statistiche quantistiche di Fermi-Dirac o di Bose-Einstein.

### Esercizio d'esempio

Per l'ossigeno molecolare ($M = 32{,}0$ g/mol) a $T = 300$ K si calcolino: (a) le tre velocità caratteristiche; (b) il rapporto tra il valore della distribuzione $F(v)$ a $v = 2v_p$ e quello a $v = v_p$; (c) l'energia cinetica media in joule e in elettronvolt; (d) l'altezza di scala di un'atmosfera isoterma di ossigeno a questa temperatura.

**Soluzione.** (a)

$$
v_p = \sqrt{\frac{2RT}{M}} = \sqrt{\frac{2\cdot8{,}314\cdot300}{0{,}032}} \simeq 395\ \text{m/s}, \quad \langle v\rangle = \sqrt{\frac{8RT}{\pi M}} \simeq 446\ \text{m/s}, \quad v_{qm} = \sqrt{\frac{3RT}{M}} \simeq 484\ \text{m/s}.
$$

(b) Poiché $mv_p^2/(2k_BT) = 1$, si ha $F(v) \propto (v/v_p)^2\,e^{-(v/v_p)^2}$. Quindi

$$
\frac{F(2v_p)}{F(v_p)} = \frac{4\,e^{-4}}{e^{-1}} = 4\,e^{-3} \simeq 0{,}20 .
$$

A velocità doppia della più probabile la densità di probabilità è già ridotta a un quinto; integrando la coda si trova che solo il 4,6% circa delle molecole supera $2v_p \simeq 790$ m/s.

(c) $\langle E\rangle = \tfrac32 k_BT = 1{,}5\cdot1{,}381\times10^{-23}\cdot300 \simeq 6{,}21\times10^{-21}$ J $\simeq 0{,}039$ eV.

(d) $H = RT/(Mg) = 8{,}314\cdot300/(0{,}032\cdot9{,}81) \simeq 7{,}9\times10^3$ m.

### Punti chiave

- In un gas in equilibrio le velocità molecolari sono distribuite statisticamente; la distribuzione è stazionaria anche se le singole molecole cambiano continuamente velocità.
- Ogni componente cartesiana della velocità ha distribuzione gaussiana con varianza $k_BT/m$.
- Distribuzione di Maxwell del modulo: $F(v) = 4\pi (m/2\pi k_BT)^{3/2} v^2 e^{-mv^2/2k_BT}$, prodotto di un fattore geometrico $v^2$ e del fattore di Boltzmann.
- Velocità caratteristiche: $v_p = \sqrt{2k_BT/m} < \langle v\rangle = \sqrt{8k_BT/\pi m} < v_{qm} = \sqrt{3k_BT/m}$.
- La distribuzione in energia $F(E) \propto \sqrt E\,e^{-E/k_BT}$ non dipende dalla massa; $\langle E\rangle = \tfrac32 k_BT$.
- Il fattore di Boltzmann $e^{-E/k_BT}$ è generale: legge barometrica, legge di Arrhenius, popolazione dei livelli energetici.
- La statistica classica vale per particelle distinguibili e gas diluiti; altrimenti servono le statistiche quantistiche.

## 15.2 Entropia

In termodinamica l'entropia è definita in modo operativo, attraverso il rapporto $\delta Q_{rev}/T$, e il secondo principio afferma che l'entropia di un sistema isolato non diminuisce. Questa formulazione, per quanto rigorosa, lascia aperta una domanda fondamentale: **perché** l'entropia aumenta? Le leggi della meccanica che governano il moto delle molecole sono reversibili nel tempo: se si invertissero istantaneamente tutte le velocità, ogni molecola ripercorrerebbe a ritroso la propria traiettoria. Come può allora un sistema composto da particelle che obbediscono a leggi reversibili mostrare un comportamento macroscopico irreversibile? La risposta, trovata da Ludwig Boltzmann negli anni Settanta dell'Ottocento, è che il secondo principio non è una legge assoluta della dinamica, ma una legge **statistica**: i processi irreversibili non sono impossibili, sono semplicemente **improbabili** a un livello che sfida ogni immaginazione, perché il numero di configurazioni microscopiche corrispondenti agli stati di equilibrio è incomparabilmente maggiore di quello degli stati ordinati.

### 15.2.1 Relazione di Boltzmann

Per formulare quantitativamente questa idea occorre distinguere due livelli di descrizione. Un **macrostato** è lo stato del sistema descritto dalle grandezze macroscopiche ($p$, $V$, $T$, numero di particelle in ciascuna metà del recipiente, e così via). Un **microstato** è la specificazione completa dello stato di ogni singola particella (in meccanica classica posizione e velocità di ciascuna molecola, entro una certa precisione; in meccanica quantistica lo stato quantico dell'intero sistema). A ogni macrostato corrisponde in generale un numero enorme di microstati diversi, indistinguibili dal punto di vista macroscopico: questo numero si indica con $W$ (o $\Omega$) ed è detto **molteplicità** o **peso statistico** del macrostato.

L'ipotesi fondamentale della meccanica statistica è il **postulato di uguale probabilità a priori**: per un sistema isolato in equilibrio, tutti i microstati accessibili (compatibili con l'energia totale e con i vincoli) sono ugualmente probabili. Ne segue che la probabilità di osservare un certo macrostato è proporzionale al suo numero di microstati $W$. Lo stato di equilibrio è il macrostato più probabile, cioè quello con il massimo $W$.

Boltzmann identificò l'entropia termodinamica con il logaritmo della molteplicità, nella relazione incisa sulla sua tomba a Vienna:

$$
S = k_B \ln W .
$$

La scelta del logaritmo non è arbitraria. L'entropia è una grandezza **additiva**: l'entropia di due sottosistemi indipendenti è la somma delle loro entropie. Il numero di microstati del sistema composto è invece il **prodotto** dei numeri di microstati, $W = W_1 W_2$, perché ogni microstato del primo può combinarsi con ogni microstato del secondo. L'unica funzione che trasforma prodotti in somme è il logaritmo: $S = k_B\ln(W_1W_2) = S_1 + S_2$. La costante di proporzionalità, la costante di Boltzmann $k_B = 1{,}38\times10^{-23}$ J/K, fissa l'unità di misura in modo che l'entropia statistica coincida con quella termodinamica.

Verifichiamo la coerenza con un esempio. Consideriamo l'**espansione libera** di $N$ molecole di gas ideale da un volume $V$ al volume $2V$. In un gas ideale le posizioni delle molecole sono indipendenti; raddoppiando il volume, ogni molecola ha a disposizione il doppio delle posizioni, quindi il numero di microstati aumenta di un fattore $2^N$. La variazione di entropia è

$$
\Delta S = k_B\ln\frac{W_f}{W_i} = k_B\ln 2^N = N k_B\ln2 = nR\ln2,
$$

esattamente il risultato ottenuto in termodinamica integrando $\delta Q_{rev}/T$ lungo un'isoterma reversibile. Più in generale, per un'espansione da $V_1$ a $V_2$ si trova $\Delta S = nR\ln(V_2/V_1)$, e includendo il contributo delle velocità (il cui "volume" nello spazio delle velocità cresce come $T^{3/2}$) si ricostruisce l'intera formula termodinamica dell'entropia del gas ideale.

Da questo esempio emerge anche il significato statistico dell'irreversibilità. La probabilità che, dopo l'espansione, tutte le $N$ molecole si ritrovino spontaneamente nella metà iniziale del recipiente è $(1/2)^N$. Per $N = 4$ molecole è $1/16$, un evento che si osserverebbe spesso; per $N = 100$ è circa $10^{-30}$; per una mole, $N \simeq 6\times10^{23}$, è $2^{-6\times10^{23}}$, un numero così piccolo che non si verificherebbe neppure una volta in tempi enormemente più lunghi dell'età dell'universo. Il secondo principio è "vero" con una probabilità che differisce dalla certezza per quantità del tutto inosservabili. Per sistemi microscopici, invece, le **fluttuazioni** sono rilevanti: il moto browniano di una particella sospesa, il rumore termico nei circuiti elettrici (rumore Johnson) e le violazioni transitorie del secondo principio osservate in esperimenti su singole molecole sono manifestazioni dirette della natura statistica della termodinamica.

La relazione di Boltzmann permette anche di ricavare la temperatura in modo statistico. Due sistemi che si scambiano energia raggiungono l'equilibrio quando l'entropia totale è massima rispetto alla ripartizione dell'energia: ciò avviene quando $\partial S_1/\partial U_1 = \partial S_2/\partial U_2$. Si definisce quindi la temperatura come

$$
\frac{1}{T} = \left(\frac{\partial S}{\partial U}\right)_V ,
$$

relazione coerente con l'equazione fondamentale $dU = T\,dS - p\,dV$. Il calore fluisce dal corpo caldo al freddo perché così facendo l'aumento di molteplicità del corpo freddo supera la diminuzione di quello caldo.

### 15.2.2 Disordine

L'entropia viene spesso descritta come una misura del **disordine** di un sistema. Questa interpretazione, se intesa correttamente, è molto utile: un macrostato "ordinato" è un macrostato che può essere realizzato in pochi modi microscopici, mentre un macrostato "disordinato" è compatibile con moltissime configurazioni. Un mazzo di carte ordinato per seme e valore corrisponde a una sola disposizione, mentre un mazzo "mescolato" corrisponde a quasi tutte le $52! \simeq 8\times10^{67}$ disposizioni possibili: mescolando, si passa quasi certamente da uno stato ordinato a uno disordinato, mai il contrario. Allo stesso modo, un cristallo, in cui gli atomi occupano posizioni regolari, ha entropia minore del liquido corrispondente, in cui gli atomi sono liberi di disporsi in moltissimi modi; e il liquido ha entropia minore del vapore. Per questo nella fusione e nell'evaporazione l'entropia aumenta e occorre fornire calore latente.

Più precisamente, il "disordine" va inteso come **mancanza di informazione**: l'entropia misura quanto poco sappiamo del microstato quando conosciamo soltanto il macrostato. Se conosciamo solo pressione, volume e temperatura di un gas, l'incertezza sulla posizione e velocità di ogni molecola è enorme; più grande è $W$, maggiore è l'informazione che ci manca per specificare il microstato. Questa interpretazione fu resa rigorosa da Claude Shannon (1948), che nella teoria dell'informazione introdusse un'entropia $H = -\sum_i p_i\log p_i$ formalmente identica all'**entropia di Gibbs** $S = -k_B\sum_i p_i\ln p_i$, che a sua volta si riduce a $S = k_B\ln W$ quando tutti i $W$ microstati hanno probabilità $p_i = 1/W$.

Il legame tra entropia e informazione ha conseguenze fisiche concrete. Il celebre **diavoletto di Maxwell** è un essere immaginario che, sorvegliando una porticina tra due scomparti di gas, lascia passare solo le molecole veloci in un verso e quelle lente nell'altro, creando senza lavoro una differenza di temperatura in violazione del secondo principio. La risoluzione del paradosso, maturata nel Novecento (Szilard, Landauer, Bennett), mostra che il diavoletto deve acquisire e memorizzare informazioni sulle molecole, e che **cancellare** un bit di informazione dalla sua memoria richiede la dissipazione di almeno $k_BT\ln2$ di energia sotto forma di calore (**principio di Landauer**): l'aumento di entropia associato compensa esattamente la diminuzione ottenuta separando le molecole. A temperatura ambiente $k_BT\ln2 \simeq 2{,}9\times10^{-21}$ J: un limite fondamentale al consumo energetico dei calcolatori, che i dispositivi attuali superano ancora di vari ordini di grandezza.

L'idea di disordine deve però essere usata con cautela. In alcuni casi l'aumento di entropia accompagna la comparsa di un **ordine apparente**: per esempio, in una soluzione di particelle colloidali dure ad alta concentrazione la fase cristallina, ordinata, ha entropia maggiore della fase disordinata, perché la disposizione regolare lascia a ciascuna particella più spazio per muoversi. Inoltre, sistemi aperti come gli organismi viventi o i cristalli che crescono da una soluzione possono diminuire la propria entropia, purché esportino nell'ambiente un'entropia maggiore: la Terra riceve dal Sole energia "a bassa entropia" (fotoni visibili, a circa 5800 K) e la riemette nello spazio come radiazione infrarossa "ad alta entropia" (circa 255 K), e questo flusso di entropia alimenta tutti i processi ordinati della biosfera.

Infine, l'interpretazione statistica illumina la **freccia del tempo**. Le leggi microscopiche non distinguono passato e futuro, ma l'universo è partito, per ragioni cosmologiche, da uno stato di entropia straordinariamente bassa; da allora l'entropia cresce semplicemente perché gli stati di alta entropia sono enormemente più numerosi. La distinzione tra passato e futuro che sperimentiamo quotidianamente (ricordiamo il passato e non il futuro, le tazze si rompono ma non si ricompongono) è radicata in questo aumento statistico. Per sistemi piccoli e tempi lunghissimi, il **teorema di ricorrenza di Poincaré** garantisce che un sistema isolato torni arbitrariamente vicino al suo stato iniziale; ma per un sistema macroscopico il tempo di ricorrenza supera di un'infinità di ordini di grandezza l'età dell'universo, e la ricorrenza è del tutto irrilevante dal punto di vista fisico.

### Esercizio d'esempio

Un recipiente è diviso in due metà uguali. (a) Si considerino $N = 4$ molecole distinguibili: si elenchino i macrostati (numero di molecole nella metà sinistra), la loro molteplicità e la loro probabilità; si calcoli l'entropia statistica di ciascun macrostato. (b) Per $n = 1{,}00$ mol di gas ideale che si espande liberamente da metà a tutto il volume, si calcoli $\Delta S$ e la probabilità che il gas torni spontaneamente nella metà iniziale.

**Soluzione.** (a) La molteplicità del macrostato con $k$ molecole a sinistra è il coefficiente binomiale $W_k = \binom{4}{k}$:

| $k$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| $W_k$ | 1 | 4 | 6 | 4 | 1 |
| $P_k$ | 1/16 | 4/16 | 6/16 | 4/16 | 1/16 |
| $S_k/k_B = \ln W_k$ | 0 | 1,39 | 1,79 | 1,39 | 0 |

Il macrostato più probabile (distribuzione uniforme, $k = 2$) ha entropia massima; i macrostati "ordinati" ($k = 0$ o $4$) hanno entropia nulla. Con solo 4 molecole, tuttavia, la probabilità di trovarle tutte da una parte è ancora del 12,5% (contando entrambi i lati).

(b) Con $N = nN_A = 6{,}022\times10^{23}$ molecole:

$$
\Delta S = Nk_B\ln2 = nR\ln2 = 1{,}00\cdot8{,}314\cdot0{,}693 \simeq 5{,}76\ \text{J/K}.
$$

La probabilità di ritorno spontaneo è $P = 2^{-N} = 10^{-N\log_{10}2} \simeq 10^{-1{,}81\times10^{23}}$: un numero con circa $1{,}8\times10^{23}$ zeri dopo la virgola. Equivalentemente $P = e^{-\Delta S/k_B}$: ogni diminuzione di entropia macroscopica è soppressa esponenzialmente dal fattore $e^{-\Delta S/k_B}$, con $\Delta S/k_B$ dell'ordine di $10^{23}$.

### Punti chiave

- Il secondo principio ha natura statistica: i processi irreversibili inversi non sono impossibili, ma estremamente improbabili per sistemi macroscopici.
- Un macrostato corrisponde a $W$ microstati; per il postulato di uguale probabilità a priori, l'equilibrio è il macrostato con $W$ massimo.
- Relazione di Boltzmann: $S = k_B\ln W$; il logaritmo garantisce l'additività dell'entropia.
- Nell'espansione libera $W$ aumenta di $2^N$ e $\Delta S = Nk_B\ln2 = nR\ln2$, in accordo con la termodinamica.
- La temperatura si definisce statisticamente come $1/T = (\partial S/\partial U)_V$.
- L'entropia misura il disordine inteso come mancanza di informazione sul microstato (entropia di Gibbs e di Shannon); cancellare un bit costa almeno $k_BT\ln2$.
- I sistemi aperti possono ridurre la propria entropia esportandone nell'ambiente; l'aumento statistico dell'entropia definisce la freccia del tempo.
