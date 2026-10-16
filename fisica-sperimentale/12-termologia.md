# Capitolo 12 — Termologia

Con questo capitolo si apre la parte del corso dedicata ai fenomeni termici. Fino ad ora la descrizione della natura è stata condotta con le sole grandezze della meccanica (lunghezza, massa, tempo e le loro combinazioni): un corpo era caratterizzato dalla sua posizione, dalla sua velocità, dalle forze che agiscono su di esso. Esiste però un'ampia classe di fenomeni quotidiani — il riscaldamento di una pentola d'acqua, la fusione del ghiaccio, la dilatazione dei binari d'estate, il funzionamento di un motore a scoppio — che non può essere descritta in modo soddisfacente senza introdurre concetti nuovi: la **temperatura**, il **calore**, l'**energia interna**. La **termologia** è la parte della fisica che studia questi concetti a livello macroscopico e costituisce il fondamento della termodinamica vera e propria (che verrà approfondita nei capitoli successivi, con il secondo principio e l'entropia). In questo capitolo definiremo con precisione che cosa si intende per sistema termodinamico e per stato di equilibrio, introdurremo la temperatura attraverso il principio zero, studieremo la dilatazione termica, enunceremo il primo principio della termodinamica come estensione della conservazione dell'energia, analizzeremo le principali trasformazioni, i calori specifici, le transizioni di fase e infine i meccanismi di trasmissione del calore.

## 12.1 Sistema termodinamico

La termodinamica nasce storicamente nel XIX secolo come scienza delle macchine termiche, ma il suo linguaggio si è rivelato di una generalità straordinaria: si applica a gas, liquidi, solidi, miscele reattive, radiazione elettromagnetica, perfino a sistemi biologici. Questa generalità deriva dal fatto che la termodinamica classica è una teoria **macroscopica e fenomenologica**: non fa ipotesi sulla struttura microscopica della materia, ma descrive i sistemi tramite poche grandezze misurabili in laboratorio. Il primo passo, quindi, è fissare con cura il vocabolario: che cosa è un sistema, che cosa lo circonda, quali grandezze ne descrivono lo stato, quanti gradi di libertà possiede.

### 12.1.1 Sistema ed ambiente

Si chiama **sistema termodinamico** una porzione di materia (o di radiazione) che si sceglie di studiare, delimitata da una superficie chiusa, reale o ideale, detta **parete** o **contorno**. Tutto ciò che sta all'esterno del contorno e che può interagire con il sistema costituisce l'**ambiente** (o esterno); l'insieme di sistema e ambiente forma l'**universo termodinamico**. La scelta del contorno è arbitraria e dettata dalla convenienza: in un problema sul motore di un'automobile il sistema può essere la miscela aria-benzina contenuta nel cilindro, mentre in un problema di climatizzazione può essere l'aria di una stanza intera. Una scelta sbagliata del sistema rende i bilanci energetici inutilmente complicati, mentre una scelta oculata li rende quasi immediati.

I sistemi si classificano in base agli scambi che la parete consente con l'ambiente. Un sistema si dice **aperto** quando può scambiare sia energia sia materia con l'esterno (per esempio una pentola d'acqua che bolle senza coperchio, o una turbina attraversata da un flusso di vapore). Si dice **chiuso** quando scambia energia ma non materia: un gas racchiuso in un cilindro con pistone mobile è l'esempio tipico. Si dice infine **isolato** quando non scambia né energia né materia: è un'idealizzazione, approssimata da un thermos ben chiuso o da un calorimetro di buona qualità. Anche le pareti vengono classificate in base agli scambi che permettono: una parete **adiabatica** impedisce lo scambio di calore (pensiamo a uno strato spesso di polistirolo espanso), mentre una parete **diatermica** (o diatermana) lo consente liberamente (una sottile lamina di rame). Una parete può inoltre essere **rigida** o **mobile**: nel secondo caso il sistema può scambiare lavoro meccanico con l'ambiente variando il proprio volume. Infine una parete può essere permeabile o impermeabile alla materia, eventualmente in modo selettivo (membrane semipermeabili).

Per un sistema isolato vale una proprietà fondamentale che verrà formalizzata più avanti: la sua energia totale è costante. Per un sistema chiuso, invece, ogni variazione di energia deve essere giustificata da uno scambio con l'ambiente, sotto forma di lavoro o di calore. Questa distinzione sarà il cuore del primo principio.

### 12.1.2 Grandezze termodinamiche

Lo **stato** di un sistema termodinamico è descritto da un insieme di grandezze macroscopiche, dette **variabili di stato** o **coordinate termodinamiche**: pressione $p$, volume $V$, temperatura $T$, quantità di sostanza $n$, ma anche magnetizzazione, polarizzazione, tensione superficiale, a seconda del sistema. Una grandezza si dice **funzione di stato** quando il suo valore dipende soltanto dallo stato attuale del sistema e non dalla storia con cui il sistema vi è giunto; di conseguenza, la sua variazione fra due stati dipende soltanto dagli stati iniziale e finale. Vedremo che l'energia interna è una funzione di stato, mentre calore e lavoro non lo sono.

Le grandezze termodinamiche si dividono in **estensive** e **intensive**. Una grandezza è estensiva quando è proporzionale alla quantità di materia del sistema: se si uniscono due copie identiche del sistema, il suo valore raddoppia. Sono estensive la massa $m$, il volume $V$, il numero di moli $n$, l'energia interna $U$. Una grandezza è intensiva quando non dipende dall'estensione del sistema e può essere definita punto per punto: pressione $p$, temperatura $T$, densità $\rho$. Dal rapporto fra due grandezze estensive si ottiene una grandezza intensiva: per esempio il **volume specifico** $v = V/m$, il **volume molare** $V_m = V/n$, l'energia interna specifica $u = U/m$. Questa distinzione è importante perché, all'equilibrio, sono le grandezze intensive a essere uniformi in tutto il sistema.

Fra le variabili di stato di un sistema in equilibrio esiste in generale una relazione, detta **equazione di stato**, del tipo
$$f(p, V, T, n) = 0 .$$
L'esempio più noto è l'equazione dei gas perfetti $pV = nRT$, che sarà studiata nel capitolo sulla meccanica dei gas; per solidi e liquidi l'equazione di stato è più complicata e spesso si esprime tramite coefficienti sperimentali (di dilatazione, di compressibilità). L'esistenza dell'equazione di stato implica che, per un sistema semplice a composizione fissata, bastano **due** variabili indipendenti per individuarne lo stato: per questo motivo gli stati di equilibrio si rappresentano come punti in un piano, tipicamente il **piano di Clapeyron** $(V, p)$.

### 12.1.3 Regola delle fasi

Si chiama **fase** una porzione di sistema fisicamente e chimicamente omogenea, separata dalle altre da superfici di discontinuità ben definite. Acqua liquida con cubetti di ghiaccio è un sistema a due fasi; acqua e olio formano anch'esse due fasi liquide distinte; una miscela di gas, invece, costituisce sempre una sola fase perché i gas si mescolano completamente. Si chiama **componente** ciascuna specie chimica indipendente necessaria per descrivere la composizione di tutte le fasi.

Il numero di variabili intensive che si possono variare indipendentemente senza alterare il numero di fasi in equilibrio è detto **varianza** (o numero di gradi di libertà termodinamici) $F$. Gibbs ha dimostrato che, per un sistema con $C$ componenti e $P$ fasi in equilibrio, in assenza di reazioni chimiche,
$$F = C - P + 2 .$$
Il "2" corrisponde alle due variabili intensive pressione e temperatura. Il ragionamento è il seguente: ogni fase è descritta da $p$, $T$ e dalle $C-1$ frazioni molari indipendenti, per un totale di $P(C-1) + 2$ variabili; l'equilibrio richiede che il potenziale chimico di ogni componente sia uguale in tutte le fasi, il che impone $C(P-1)$ vincoli. La differenza fornisce la regola.

Applichiamo la regola a una sostanza pura ($C = 1$). Con una sola fase, $F = 2$: possiamo scegliere liberamente pressione e temperatura (per esempio il vapore acqueo in una regione estesa del piano $pT$). Con due fasi in equilibrio, $F = 1$: fissata la temperatura, la pressione è determinata; è il caso dell'acqua che bolle, la cui temperatura di ebollizione dipende univocamente dalla pressione esterna (a 1 atm è 100 °C, in alta montagna è più bassa). Con tre fasi, $F = 0$: esiste un solo stato, il **punto triplo**, nel quale ghiaccio, acqua liquida e vapore coesistono a valori ben precisi di $p$ e $T$. Proprio questa unicità rende il punto triplo dell'acqua un riferimento metrologico ideale per la temperatura, come vedremo.

### 12.1.4 Pressione

La **pressione** è stata introdotta nella meccanica dei fluidi come il rapporto fra la componente normale della forza esercitata su una superficie e l'area della superficie stessa:
$$p = \frac{dF_\perp}{dA} .$$
Nel Sistema Internazionale si misura in **pascal** ($1\ \mathrm{Pa} = 1\ \mathrm{N/m^2}$). Sono di uso comune anche il **bar** ($10^5\ \mathrm{Pa}$), l'**atmosfera** ($1\ \mathrm{atm} = 101\,325\ \mathrm{Pa}$), il **millimetro di mercurio** o torr ($1\ \mathrm{mmHg} \approx 133{,}3\ \mathrm{Pa}$). In termodinamica la pressione assume un significato ulteriore: è la variabile intensiva coniugata al volume, nel senso che il prodotto $p\,dV$ fornisce il lavoro scambiato dal sistema quando il suo volume varia di $dV$.

Dal punto di vista microscopico, la pressione di un gas sulle pareti del recipiente è il risultato macroscopico degli innumerevoli urti delle molecole contro le pareti: ogni urto trasferisce una piccola quantità di moto, e la forza media per unità di superficie è appunto la pressione. Questa interpretazione verrà sviluppata nella teoria cinetica dei gas. È importante distinguere la **pressione assoluta** dalla **pressione relativa** (o manometrica), che è la differenza rispetto alla pressione atmosferica: un pneumatico gonfiato "a 2 bar" ha in realtà una pressione assoluta di circa 3 bar. Nelle equazioni termodinamiche compare sempre la pressione assoluta.

Perché la pressione sia una variabile di stato ben definita, essa deve essere uniforme nel sistema (a meno del contributo idrostatico, trascurabile per un gas in un recipiente di dimensioni ordinarie). Durante una compressione brusca, con il pistone che si muove rapidamente, si formano invece gradienti di pressione e onde: in quel caso la pressione "del sistema" non è definita e lo stato non può essere rappresentato da un punto nel piano di Clapeyron. Questo punto sarà ripreso nella discussione delle trasformazioni quasi statiche.

### 12.1.5 Mole

La quantità di materia di un sistema si misura, nel SI, in **moli**. Dal 2019 la mole è definita fissando il valore esatto della **costante di Avogadro**:
$$N_A = 6{,}022\,140\,76 \times 10^{23}\ \mathrm{mol^{-1}} .$$
Una mole è dunque la quantità di sostanza che contiene esattamente $N_A$ entità elementari (atomi, molecole, ioni, elettroni, a seconda di come si specifica). Il numero di moli di un sistema contenente $N$ particelle è $n = N/N_A$.

Si chiama **massa molare** $M$ la massa di una mole di sostanza, espressa in $\mathrm{kg/mol}$ (o più spesso in $\mathrm{g/mol}$). Numericamente, la massa molare in grammi per mole coincide con la massa molecolare relativa espressa in unità di massa atomica: l'acqua ha massa molecolare relativa circa 18, quindi $M_{\mathrm{H_2O}} \approx 18\ \mathrm{g/mol} = 0{,}018\ \mathrm{kg/mol}$. Il legame fra massa $m$ di un campione e numero di moli è semplicemente $n = m/M$.

La mole è indispensabile in termodinamica perché molte proprietà dei sistemi, in particolare dei gas, risultano proporzionali al numero di particelle più che alla massa. Per esempio, a parità di pressione e temperatura, una mole di qualunque gas ideale occupa lo stesso volume (circa $22{,}4\ \mathrm{L}$ a 0 °C e 1 atm), indipendentemente dalla massa delle molecole: è la **legge di Avogadro**. Analogamente, vedremo che i calori specifici molari dei solidi tendono, ad alta temperatura, a un valore comune (legge di Dulong e Petit), cosa che non accade per i calori specifici riferiti all'unità di massa. Il passaggio fra la descrizione "per unità di massa" e "per mole" sarà quindi una costante nei capitoli di termodinamica, e conviene abituarsi fin da ora a usare con disinvoltura entrambe le prospettive. Infine, il prodotto $N_A k_B = R$, dove $k_B = 1{,}380\,649 \times 10^{-23}\ \mathrm{J/K}$ è la costante di Boltzmann, definisce la **costante universale dei gas** $R \approx 8{,}314\ \mathrm{J/(mol\,K)}$, che fa da ponte fra la scala microscopica (per particella) e quella macroscopica (per mole).

### Esercizio d'esempio

Un recipiente rigido di volume $V = 5{,}0\ \mathrm{L}$ contiene $m = 64\ \mathrm{g}$ di ossigeno molecolare ($\mathrm{O_2}$, massa molare $M = 32\ \mathrm{g/mol}$). Si chiede di determinare: (a) il numero di moli; (b) il numero di molecole; (c) il volume molare e la densità; (d) la varianza del sistema secondo la regola delle fasi.

**Soluzione.**

(a) Il numero di moli è
$$n = \frac{m}{M} = \frac{0{,}064\ \mathrm{kg}}{0{,}032\ \mathrm{kg/mol}} = 2{,}0\ \mathrm{mol}.$$

(b) Il numero di molecole è
$$N = n N_A = 2{,}0 \times 6{,}022\times10^{23} \approx 1{,}20\times10^{24}.$$

(c) Il volume molare è $V_m = V/n = 5{,}0\times10^{-3}\ \mathrm{m^3}/2{,}0\ \mathrm{mol} = 2{,}5\times10^{-3}\ \mathrm{m^3/mol}$; la densità è
$$\rho = \frac{m}{V} = \frac{0{,}064\ \mathrm{kg}}{5{,}0\times10^{-3}\ \mathrm{m^3}} = 12{,}8\ \mathrm{kg/m^3}.$$
Si noti che $V$, $m$, $n$ sono estensive, mentre $V_m$ e $\rho$ sono intensive: se si raddoppia il sistema (due recipienti uguali affiancati), le prime raddoppiano, le seconde restano invariate.

(d) Il sistema contiene un componente ($C=1$) in una sola fase gassosa ($P=1$), quindi $F = 1 - 1 + 2 = 2$: pressione e temperatura possono essere scelte indipendentemente. Poiché però il volume è fissato e la quantità di gas è nota, l'equazione di stato lega $p$ e $T$, e assegnare una di esse determina l'altra.

### Punti chiave

- Un sistema termodinamico è separato dall'ambiente da una parete; i sistemi sono aperti, chiusi o isolati, le pareti adiabatiche o diatermiche, rigide o mobili.
- Lo stato di equilibrio è descritto da poche variabili macroscopiche legate da un'equazione di stato; per un sistema semplice bastano due variabili indipendenti.
- Le grandezze estensive sono proporzionali alla quantità di materia, quelle intensive no; il rapporto di due estensive è intensivo.
- La regola delle fasi di Gibbs $F = C - P + 2$ fornisce il numero di variabili intensive indipendenti; per una sostanza pura il punto triplo ha varianza zero.
- La pressione è forza normale per unità di superficie, misurata in pascal; nelle equazioni termodinamiche si usa sempre la pressione assoluta.
- La mole è definita fissando $N_A = 6{,}022\,140\,76\times10^{23}\ \mathrm{mol^{-1}}$; vale $n = m/M = N/N_A$ e $R = N_A k_B$.

## 12.2 Principio zero della termodinamica

L'esperienza quotidiana ci dà un'idea intuitiva di "caldo" e "freddo", legata alla sensazione tattile. Questa sensazione, però, è un pessimo strumento di misura: toccando in una stanza un oggetto metallico e uno di legno, entrambi alla stessa temperatura, il metallo sembra più freddo perché sottrae calore alla pelle più rapidamente. Per costruire una grandezza fisica oggettiva e misurabile occorre un fondamento più solido. Questo fondamento è il **principio zero della termodinamica**, così chiamato perché, pur essendo logicamente precedente al primo e al secondo principio, fu formulato esplicitamente solo dopo di essi, negli anni Trenta del Novecento.

### 12.2.1 Equilibrio termodinamico

Un sistema si trova in uno stato di **equilibrio termodinamico** quando le sue variabili di stato non cambiano nel tempo e, contemporaneamente, non vi sono flussi netti di materia o di energia al suo interno o attraverso il contorno. L'equilibrio termodinamico è la contemporanea presenza di tre equilibri parziali. L'**equilibrio meccanico** richiede che non vi siano forze non bilanciate all'interno del sistema e fra sistema e ambiente: la pressione è uniforme (in assenza di campi esterni) e le pareti mobili sono ferme. L'**equilibrio chimico** richiede che non avvengano reazioni chimiche né processi di diffusione che modifichino la composizione delle varie parti. L'**equilibrio termico** richiede che non vi siano scambi di calore fra le varie parti del sistema né fra sistema e ambiente attraverso pareti diatermiche.

Un sistema isolato, lasciato a sé stesso, evolve spontaneamente verso uno stato di equilibrio e vi permane indefinitamente: questo è un fatto sperimentale di grande generalità (un caffè caldo lasciato su un tavolo si raffredda fino alla temperatura della stanza e poi non cambia più). Il tempo necessario per raggiungere l'equilibrio è detto **tempo di rilassamento** e può variare enormemente: frazioni di microsecondo per l'equilibrio di pressione in un piccolo volume di gas, minuti od ore per l'equilibrio termico di un oggetto macroscopico, anni per certi processi di diffusione nei solidi. Solo negli stati di equilibrio le variabili termodinamiche sono ben definite; per questo la termodinamica classica è, in senso stretto, una teoria degli stati di equilibrio.

### 12.2.2 Principio zero della termodinamica

Consideriamo due sistemi $A$ e $B$, ciascuno inizialmente in equilibrio, e mettiamoli in contatto attraverso una parete diatermica rigida e impermeabile, isolando l'insieme dall'ambiente. In generale le variabili di stato di entrambi cambiano finché la coppia non raggiunge un nuovo stato di equilibrio complessivo. Si dice allora che $A$ e $B$ sono in **equilibrio termico** fra loro. Se invece, al momento del contatto, nessuna variabile cambia, i due sistemi erano già in equilibrio termico.

Il principio zero afferma:

> Se due sistemi $A$ e $B$ sono ciascuno in equilibrio termico con un terzo sistema $C$, allora $A$ e $B$ sono in equilibrio termico fra loro.

In linguaggio matematico, la relazione "essere in equilibrio termico con" è **transitiva**; poiché è evidentemente anche riflessiva e simmetrica, essa è una **relazione di equivalenza**. Questo enunciato, che può sembrare banale, non è affatto una verità logica: è un fatto sperimentale. Non tutte le relazioni fisiche godono della transitività (ad esempio, il fatto che $A$ attragga magneticamente $C$ e $B$ attragga $C$ non implica che $A$ attragga $B$). È proprio questa transitività a rendere possibile il funzionamento di un termometro: il sistema $C$ gioca il ruolo di strumento di confronto, e possiamo stabilire se due corpi sono in equilibrio termico senza metterli direttamente in contatto.

### 12.2.3 Temperatura

Ogni relazione di equivalenza suddivide l'insieme degli stati in **classi di equivalenza** disgiunte: tutti gli stati appartenenti alla stessa classe sono in equilibrio termico fra loro. Si definisce allora **temperatura** quella grandezza di stato che assume lo stesso valore per tutti gli stati della stessa classe e valori diversi per classi diverse. In altre parole: due sistemi hanno la stessa temperatura se e solo se sono in equilibrio termico. Questa è la definizione operativa e rigorosa di temperatura offerta dal principio zero.

La temperatura è una grandezza **intensiva**: all'equilibrio è uniforme in tutto il sistema e non dipende dalla sua estensione. Nel SI è una delle sette grandezze fondamentali, con unità di misura il **kelvin** (K). Dal 2019 il kelvin è definito fissando il valore esatto della costante di Boltzmann $k_B = 1{,}380\,649\times10^{-23}\ \mathrm{J/K}$; in questo modo la temperatura è legata direttamente a un'energia, coerentemente con l'interpretazione microscopica secondo cui la temperatura misura l'energia cinetica media di agitazione delle particelle. Per un gas ideale monoatomico, infatti, l'energia cinetica media di traslazione per molecola è $\langle E_k \rangle = \tfrac{3}{2}k_B T$.

È importante sottolineare che il principio zero garantisce l'esistenza della temperatura ma non ne fissa la scala numerica: qualunque funzione monotona dei valori assegnati alle classi sarebbe un'altra temperatura altrettanto lecita. Occorre quindi una convenzione, che si realizza scegliendo una **proprietà termometrica** e dei **punti fissi**.

### 12.2.4 Scale di temperatura

Una **proprietà termometrica** è una grandezza fisica $X$ di un sistema campione che varia in modo riproducibile e monotono con lo stato termico: la lunghezza di una colonna di mercurio, la pressione di un gas a volume costante, la resistenza elettrica di un filo di platino, la tensione di una termocoppia. Scelta la proprietà, si assume una relazione funzionale fra $X$ e la temperatura, solitamente lineare:
$$\theta(X) = a X + b ,$$
e si fissano le costanti assegnando valori convenzionali a due **punti fissi**, cioè stati facilmente riproducibili. Storicamente la **scala Celsius** assegnava 0 °C al punto di fusione del ghiaccio e 100 °C al punto di ebollizione dell'acqua a pressione atmosferica normale. La **scala Fahrenheit**, ancora in uso nei paesi anglosassoni, assegna a questi punti rispettivamente 32 °F e 212 °F, per cui $\theta_F = \tfrac{9}{5}\theta_C + 32$.

Il problema di questo approccio è che termometri basati su proprietà diverse, tarati sugli stessi punti fissi, forniscono in generale letture leggermente diverse nei punti intermedi, perché le varie proprietà non sono esattamente lineari fra loro. Si cerca allora una proprietà che dia una scala il più possibile universale. Si scopre sperimentalmente che i **termometri a gas a volume costante**, nel limite di gas molto rarefatto, forniscono tutti la stessa scala indipendentemente dal gas usato. Si definisce così la **temperatura del gas ideale**:
$$T = 273{,}16\ \mathrm{K}\ \cdot \lim_{p_{tr}\to 0} \frac{p}{p_{tr}} ,$$
dove $p_{tr}$ è la pressione del gas quando il termometro è in equilibrio con acqua al punto triplo. In questa scala si utilizza un **solo punto fisso**, il punto triplo dell'acqua, a cui si assegna storicamente $T_{tr} = 273{,}16\ \mathrm{K}$; il secondo "punto" è lo zero assoluto, dove la pressione del gas ideale si annullerebbe. Con il secondo principio si mostrerà che questa scala coincide con la **scala termodinamica assoluta**, indipendente da qualsiasi sostanza.

La **scala Celsius moderna** è definita a partire da quella kelvin come
$$\theta_C = T - 273{,}15 ,$$
per cui un intervallo di 1 °C coincide con un intervallo di 1 K. Con questa definizione il punto triplo dell'acqua vale 0,01 °C e il punto di ebollizione normale risulta circa 99,97 °C. Lo **zero assoluto** ($0\ \mathrm{K} = -273{,}15\ \mathrm{°C}$) è il limite inferiore della temperatura: non può essere raggiunto in un numero finito di passi (terzo principio), ma i laboratori di criogenia sono arrivati a frazioni di nanokelvin.

### 12.2.5 Termometri

Un **termometro** è un sistema dotato di una proprietà termometrica facilmente leggibile, di capacità termica piccola rispetto al corpo da misurare (per non perturbarlo) e di tempo di risposta breve. Il principio di funzionamento è sempre lo stesso: si mette il termometro in contatto con il corpo, si attende l'equilibrio termico e si legge il valore della proprietà, che per il principio zero indica la temperatura del corpo.

Il **termometro a liquido** (mercurio, ormai vietato in molti paesi, o alcol colorato) sfrutta la dilatazione di un liquido in un bulbo collegato a un capillare sottile: piccole variazioni di volume producono spostamenti apprezzabili del menisco. Il **termometro a gas a volume costante** è lo strumento di riferimento della metrologia classica: un bulbo contenente gas è collegato a un manometro e si regola un serbatoio di mercurio per mantenere costante il volume; la pressione misurata è la proprietà termometrica. È ingombrante e lento, ma accuratissimo. Il **termometro a resistenza** (tipicamente al platino, Pt100) sfrutta l'aumento quasi lineare della resistenza elettrica dei metalli con la temperatura; i **termistori** sono semiconduttori la cui resistenza invece diminuisce fortemente all'aumentare della temperatura, con grande sensibilità su intervalli ristretti. La **termocoppia** sfrutta l'effetto Seebeck: due metalli diversi saldati in due giunzioni a temperature diverse generano una piccola forza elettromotrice (decine di microvolt per kelvin) proporzionale in prima approssimazione alla differenza di temperatura; è robusta, economica e copre intervalli molto ampi. I **pirometri** e le termocamere, infine, misurano senza contatto la radiazione termica emessa dai corpi e sono indispensabili per temperature molto elevate (forni, metalli fusi) o per oggetti in movimento.

Nella pratica di laboratorio la taratura dei termometri segue la **Scala Internazionale di Temperatura** (ITS-90), che specifica una serie di punti fissi (punti tripli, di fusione e di solidificazione di sostanze pure) e gli strumenti interpolanti da usare fra un punto e l'altro, in modo da approssimare al meglio la temperatura termodinamica.

### Esercizio d'esempio

Un termometro a gas a volume costante segna, in equilibrio con acqua al punto triplo, una pressione $p_{tr} = 6{,}80\times10^{3}\ \mathrm{Pa}$. Immerso in un liquido incognito, segna $p = 9{,}35\times10^{3}\ \mathrm{Pa}$. Si chiede la temperatura del liquido in kelvin, in gradi Celsius e in gradi Fahrenheit, assumendo che il gas sia sufficientemente rarefatto da comportarsi idealmente.

**Soluzione.** Nella scala del gas ideale, a volume costante, la temperatura è proporzionale alla pressione:
$$T = 273{,}16\ \mathrm{K}\cdot\frac{p}{p_{tr}} = 273{,}16\ \mathrm{K}\cdot\frac{9{,}35\times10^3}{6{,}80\times10^3} = 273{,}16 \times 1{,}375 \approx 375{,}6\ \mathrm{K}.$$
In gradi Celsius:
$$\theta_C = T - 273{,}15 \approx 102{,}4\ \mathrm{°C}.$$
In gradi Fahrenheit:
$$\theta_F = \tfrac{9}{5}\,\theta_C + 32 = 1{,}8\times102{,}4 + 32 \approx 216{,}4\ \mathrm{°F}.$$
Il liquido è quindi leggermente più caldo dell'acqua bollente a pressione normale: potrebbe trattarsi, ad esempio, di una soluzione salina in ebollizione. Si osservi che, se il gas non fosse abbastanza rarefatto, si dovrebbero ripetere le misure a valori decrescenti di $p_{tr}$ ed estrapolare a $p_{tr}\to0$.

### Punti chiave

- L'equilibrio termodinamico richiede contemporaneamente equilibrio meccanico, chimico e termico; solo all'equilibrio le variabili di stato sono definite.
- Il principio zero afferma la transitività dell'equilibrio termico: due sistemi in equilibrio termico con un terzo lo sono fra loro.
- La temperatura è la grandezza che etichetta le classi di equivalenza dell'equilibrio termico; è intensiva e si misura in kelvin.
- Una scala di temperatura richiede una proprietà termometrica e dei punti fissi; il termometro a gas rarefatto fornisce una scala universale.
- Il kelvin è oggi definito fissando $k_B$; la scala Celsius è $\theta_C = T - 273{,}15$, con intervalli uguali a quelli kelvin.
- I termometri reali (a liquido, a gas, a resistenza, termocoppie, pirometri) differiscono per intervallo, sensibilità, tempo di risposta e invasività.

## 12.3 Dilatazione termica

Quasi tutti i corpi, quando la loro temperatura aumenta, aumentano le proprie dimensioni: è il fenomeno della **dilatazione termica**. Si tratta di un effetto piccolo in termini relativi (per un metallo tipico, qualche decina di micrometri per metro e per grado), ma con conseguenze tecniche importantissime. I giunti di dilatazione dei ponti e delle rotaie, i bimetalli dei termostati, le tolleranze nei motori, le fessurazioni di un vetro sottoposto a uno sbalzo termico, perfino la scelta dei materiali per le otturazioni dentali sono tutti problemi governati dalla dilatazione. Inoltre, come abbiamo visto, la dilatazione dei liquidi è la proprietà termometrica dei termometri tradizionali. In questa sezione ne daremo una descrizione fenomenologica e ne discuteremo l'origine microscopica.

### 12.3.1 Dilatazione lineare

Consideriamo una sbarra sottile di lunghezza $L_0$ alla temperatura $T_0$. Se la temperatura varia di una piccola quantità $dT$, si osserva sperimentalmente che la variazione di lunghezza $dL$ è proporzionale sia alla lunghezza stessa sia alla variazione di temperatura. Si definisce allora il **coefficiente di dilatazione lineare**
$$\lambda = \frac{1}{L}\frac{dL}{dT} ,$$
che rappresenta la variazione relativa di lunghezza per unità di variazione di temperatura e si misura in $\mathrm{K^{-1}}$ (in molti testi è indicato con $\alpha$). Il coefficiente dipende dal materiale e, in generale, anche dalla temperatura; per intervalli di temperatura non troppo ampi si può però considerarlo costante. Integrando fra $T_0$ e $T$ si ottiene $L = L_0 e^{\lambda (T-T_0)}$; poiché in pratica $\lambda\,\Delta T \ll 1$, lo sviluppo al primo ordine fornisce la ben nota legge lineare
$$L = L_0\,(1 + \lambda\,\Delta T), \qquad \Delta L = \lambda L_0 \Delta T .$$

Valori tipici a temperatura ambiente sono: acciaio circa $12\times10^{-6}\ \mathrm{K^{-1}}$, alluminio $23\times10^{-6}\ \mathrm{K^{-1}}$, rame $17\times10^{-6}\ \mathrm{K^{-1}}$, vetro comune $9\times10^{-6}\ \mathrm{K^{-1}}$, vetro borosilicato (Pyrex) $3\times10^{-6}\ \mathrm{K^{-1}}$, quarzo fuso $0{,}5\times10^{-6}\ \mathrm{K^{-1}}$. La lega ferro-nichel chiamata **Invar** ha un coefficiente bassissimo, circa $1\times10^{-6}\ \mathrm{K^{-1}}$, e per questo è usata negli strumenti di precisione e nei pendoli degli orologi. Il fatto che il vetro Pyrex si dilati poco spiega perché sopporti bene gli shock termici: un riscaldamento non uniforme produce dilatazioni differenziali piccole e quindi tensioni interne modeste.

Una conseguenza interessante è il **bimetallo**: due lamine di metalli con coefficienti diversi, saldate lungo tutta la lunghezza, si incurvano al variare della temperatura, perché una delle due tende ad allungarsi più dell'altra. Il raggio di curvatura è inversamente proporzionale alla differenza dei coefficienti e alla variazione di temperatura, e lo spostamento dell'estremità libera può aprire o chiudere un contatto elettrico: è il principio dei termostati di ferri da stiro, scaldabagni e interruttori termici. Un'altra conseguenza riguarda le **tensioni termiche**: se una sbarra è vincolata a mantenere la propria lunghezza mentre la temperatura aumenta, si sviluppa al suo interno uno sforzo di compressione pari a quello che servirebbe per riportare a $L_0$ una sbarra libera dilatata; dalla legge di Hooke si ricava $\sigma = E\,\lambda\,\Delta T$, con $E$ modulo di Young. Per l'acciaio ($E \approx 200\ \mathrm{GPa}$) un aumento di 30 K produce uno sforzo di circa 72 MPa: un valore enorme, ragione per cui le rotaie e i ponti richiedono giunti di dilatazione.

### 12.3.2 Dilatazione cubica

In generale un corpo tridimensionale si dilata in tutte le direzioni e il suo volume aumenta. Si definisce il **coefficiente di dilatazione cubica** (o volumica)
$$\beta = \frac{1}{V}\left(\frac{\partial V}{\partial T}\right)_p ,$$
dove la derivata parziale è calcolata a pressione costante, perché il volume dipende anche dalla pressione. Per piccoli intervalli di temperatura vale analogamente $V = V_0(1+\beta\,\Delta T)$.

Per un solido **isotropo**, cioè con le stesse proprietà in tutte le direzioni, esiste una relazione semplice fra $\beta$ e $\lambda$. Consideriamo un cubo di lato $L_0$: dopo un riscaldamento ogni lato diventa $L_0(1+\lambda\Delta T)$, e il volume
$$V = L_0^3(1+\lambda\Delta T)^3 \approx V_0\,(1 + 3\lambda\,\Delta T) ,$$
avendo trascurato i termini di ordine $(\lambda\Delta T)^2$ e $(\lambda\Delta T)^3$, del tutto irrilevanti. Ne segue $\beta = 3\lambda$. Analogamente per la **dilatazione superficiale** di una lamina si ottiene un coefficiente $2\lambda$. Un risultato talvolta controintuitivo è che un foro praticato in una lastra metallica, al crescere della temperatura, si allarga anziché restringersi: la dilatazione è una trasformazione di similitudine, e il foro si comporta come se fosse fatto dello stesso materiale della lastra. Su questo principio si basa il **calettamento a caldo**: un anello d'acciaio viene riscaldato perché il suo foro si allarghi, viene infilato su un albero e, raffreddandosi, lo serra con grande forza.

Per i **liquidi** ha senso soltanto il coefficiente cubico, dato che un liquido non ha forma propria. I valori sono generalmente più alti di quelli dei solidi: per il mercurio $\beta \approx 1{,}8\times10^{-4}\ \mathrm{K^{-1}}$, per l'alcol etilico circa $1{,}1\times10^{-3}\ \mathrm{K^{-1}}$, per la benzina circa $10^{-3}\ \mathrm{K^{-1}}$ (per questo un serbatoio riempito fino all'orlo in una mattina fresca può traboccare nel pomeriggio). Quando si misura la dilatazione di un liquido in un recipiente occorre tener conto che anche il recipiente si dilata: la dilatazione osservata è la **dilatazione apparente**, con coefficiente $\beta_{app} = \beta_{liq} - \beta_{rec}$.

L'**acqua** presenta un comportamento anomalo di grande importanza: fra 0 °C e 4 °C il suo volume *diminuisce* all'aumentare della temperatura, cioè $\beta<0$, e la densità raggiunge un massimo di circa $1000\ \mathrm{kg/m^3}$ a 3,98 °C. Inoltre, solidificando, l'acqua aumenta il proprio volume di circa il 9%. Queste anomalie hanno conseguenze ecologiche rilevanti: d'inverno l'acqua dei laghi a 4 °C, più densa, si accumula sul fondo, mentre il ghiaccio, meno denso, galleggia e forma uno strato isolante superficiale; così i laghi non gelano completamente e la vita acquatica sopravvive.

Per i **gas** il coefficiente di dilatazione a pressione costante è molto più grande e, nel limite di gas ideale, è lo stesso per tutti i gas: dall'equazione $pV=nRT$ segue $\beta = 1/T$, che a 0 °C vale circa $3{,}66\times10^{-3}\ \mathrm{K^{-1}} \approx 1/273$. È questa universalità che rende il gas rarefatto un termometro ideale.

### 12.3.3 Modello atomico

Perché i corpi si dilatano? La risposta richiede di guardare alla struttura microscopica. In un solido cristallino gli atomi occupano posizioni di equilibrio nel reticolo e oscillano attorno ad esse a causa dell'agitazione termica. L'interazione fra due atomi vicini è descritta da un'**energia potenziale** $U(r)$ funzione della distanza $r$: fortemente repulsiva a piccole distanze (sovrapposizione delle nubi elettroniche), attrattiva a distanze maggiori (legame), con un minimo in corrispondenza della distanza di equilibrio $r_0$. Un esempio classico è il potenziale di Lennard-Jones
$$U(r) = 4\varepsilon\left[\left(\frac{\sigma}{r}\right)^{12} - \left(\frac{\sigma}{r}\right)^{6}\right] .$$

Se la buca di potenziale fosse perfettamente **parabolica** (simmetrica), cioè $U(r) \approx U_0 + \tfrac12 k(r-r_0)^2$, gli atomi oscillerebbero armonicamente attorno a $r_0$ e la distanza media $\langle r\rangle$ resterebbe pari a $r_0$ qualunque fosse l'ampiezza dell'oscillazione: non vi sarebbe alcuna dilatazione. In realtà la buca è **asimmetrica** (anarmonica): sale ripidamente verso le piccole distanze e lentamente verso le grandi. Sviluppando al terzo ordine si scrive
$$U(r) \approx U_0 + \tfrac12 k\,x^2 - g\,x^3 , \qquad x = r - r_0 ,$$
con $g>0$. Quando la temperatura aumenta, l'energia media di vibrazione cresce (dell'ordine di $k_BT$), l'ampiezza delle oscillazioni aumenta e, a causa dell'asimmetria, l'atomo trascorre più tempo dal lato delle distanze maggiori. La distanza media interatomica cresce quindi con la temperatura. Un calcolo di meccanica statistica classica fornisce $\langle x\rangle \approx \tfrac{3g}{k^2}k_B T$, cioè una dilatazione proporzionale alla temperatura e al grado di anarmonicità del potenziale, da cui $\lambda \approx 3 g k_B/(k^2 r_0)$.

Il modello spiega diverse osservazioni qualitative. I materiali con legami forti e buche profonde e strette (diamante, ceramiche, quarzo) hanno costanti elastiche $k$ elevate e piccoli coefficienti di dilatazione; quelli con legami deboli (piombo, polimeri) si dilatano molto di più. Esiste anche una correlazione empirica fra coefficiente di dilatazione e temperatura di fusione: i materiali che fondono a bassa temperatura tendono a dilatarsi molto. Inoltre, a temperature molto basse, gli effetti quantistici "congelano" le vibrazioni e il coefficiente di dilatazione tende a zero, come confermato sperimentalmente. L'anomalia dell'acqua, infine, è dovuta ai legami a idrogeno, che a bassa temperatura impongono una struttura aperta e tetraedrica (tipica del ghiaccio) che si va disgregando fra 0 e 4 °C, permettendo alle molecole di impacchettarsi meglio: questo effetto strutturale prevale sull'ordinaria dilatazione anarmonica.

### Esercizio d'esempio

Una rotaia d'acciaio ($\lambda = 1{,}2\times10^{-5}\ \mathrm{K^{-1}}$, $E = 2{,}0\times10^{11}\ \mathrm{Pa}$) è lunga $L_0 = 25{,}0\ \mathrm{m}$ a $\theta_0 = 0\ \mathrm{°C}$. (a) Quale spazio occorre lasciare fra due rotaie consecutive perché si tocchino appena a $\theta = 45\ \mathrm{°C}$? (b) Se la rotaia fosse completamente vincolata alle estremità, quale sforzo si svilupperebbe a 45 °C? (c) Di quanto varia il volume di un serbatoio d'acciaio da 1,000 m³ nello stesso intervallo?

**Soluzione.**

(a) La variazione di lunghezza è
$$\Delta L = \lambda L_0 \Delta T = 1{,}2\times10^{-5}\ \mathrm{K^{-1}} \times 25{,}0\ \mathrm{m}\times 45\ \mathrm{K} = 1{,}35\times10^{-2}\ \mathrm{m}.$$
Lo spazio da lasciare è dunque circa 13,5 mm (ciascuna rotaia si allunga di 6,75 mm per lato).

(b) Se la rotaia non può allungarsi, la deformazione impedita è $\varepsilon = \lambda\Delta T = 5{,}4\times10^{-4}$, e lo sforzo di compressione vale
$$\sigma = E\varepsilon = 2{,}0\times10^{11}\ \mathrm{Pa}\times 5{,}4\times10^{-4} = 1{,}08\times10^{8}\ \mathrm{Pa} \approx 108\ \mathrm{MPa}.$$
Per una sezione di $7{,}5\times10^{-3}\ \mathrm{m^2}$ la forza assiale sarebbe circa $8\times10^{5}\ \mathrm{N}$: abbastanza per far "sbandare" lateralmente il binario.

(c) Il coefficiente cubico è $\beta = 3\lambda = 3{,}6\times10^{-5}\ \mathrm{K^{-1}}$, quindi
$$\Delta V = \beta V_0 \Delta T = 3{,}6\times10^{-5}\times1{,}000\ \mathrm{m^3}\times45 = 1{,}62\times10^{-3}\ \mathrm{m^3} \approx 1{,}6\ \mathrm{L}.$$
Se il serbatoio fosse pieno di benzina ($\beta\approx 9{,}5\times10^{-4}\ \mathrm{K^{-1}}$), il liquido aumenterebbe di circa 43 L e ne traboccherebbero circa 41 L: la dilatazione del recipiente è trascurabile rispetto a quella del liquido.

### Punti chiave

- La dilatazione lineare segue $\Delta L = \lambda L_0\Delta T$, con $\lambda$ dell'ordine di $10^{-5}\ \mathrm{K^{-1}}$ per i metalli.
- Per un solido isotropo il coefficiente cubico vale $\beta = 3\lambda$ e quello superficiale $2\lambda$; i fori si dilatano come il materiale circostante.
- Una dilatazione impedita genera tensioni termiche $\sigma = E\lambda\Delta T$, molto intense: servono giunti di dilatazione.
- I liquidi hanno $\beta$ maggiori dei solidi; nella misura bisogna considerare la dilatazione apparente dovuta al recipiente.
- L'acqua ha $\beta<0$ fra 0 e 4 °C e densità massima a circa 4 °C, con importanti conseguenze ambientali.
- Microscopicamente la dilatazione è dovuta all'anarmonicità del potenziale interatomico: in una buca simmetrica non ci sarebbe dilatazione.

## 12.4 Primo principio della termodinamica

Il primo principio della termodinamica è l'estensione ai fenomeni termici del principio di conservazione dell'energia, già incontrato in meccanica. In meccanica si era visto che, in presenza di sole forze conservative, la somma di energia cinetica e potenziale si conserva, mentre le forze dissipative (attrito, resistenza viscosa) fanno "sparire" energia meccanica. L'esperienza mostra però che, quando l'energia meccanica diminuisce per attrito, i corpi si scaldano: l'energia non scompare, ma si trasforma in una forma diversa, legata all'agitazione microscopica della materia. Il primo principio rende quantitativa questa osservazione introducendo l'**energia interna** e riconoscendo nel **calore** una modalità di trasferimento di energia, alla pari del lavoro.

### 12.4.1 Lavoro termodinamico

Consideriamo un gas racchiuso in un cilindro chiuso da un pistone mobile di area $A$. Se il gas esercita sul pistone una pressione $p$, la forza sul pistone è $F = pA$; se il pistone si sposta verso l'esterno di un tratto $dx$, il lavoro compiuto dal gas sull'ambiente è
$$\delta W = F\,dx = p A\,dx = p\,dV .$$
Il risultato non dipende dalla forma del recipiente e vale per qualunque deformazione del contorno, purché la pressione sia uniforme sulla superficie mobile. Per una trasformazione finita fra uno stato iniziale $i$ e uno finale $f$ si ha
$$W = \int_{V_i}^{V_f} p\,dV .$$

In questo testo adottiamo la convenzione, tradizionale in ingegneria, secondo cui $W$ è il **lavoro compiuto dal sistema** sull'ambiente: è positivo in un'espansione ($dV>0$) e negativo in una compressione. Altri testi (e la chimica) usano la convenzione opposta: occorre fare attenzione ai segni quando si consultano fonti diverse.

Il simbolo $\delta W$ anziché $dW$ sottolinea un fatto fondamentale: il lavoro **non è una funzione di stato**. Il lavoro infinitesimo non è il differenziale esatto di alcuna funzione, e il lavoro totale fra due stati dipende dal percorso seguito. Nel piano di Clapeyron $(V,p)$ il lavoro è l'**area sottesa** alla curva che rappresenta la trasformazione: percorsi diversi fra gli stessi estremi sottendono aree diverse. Per esempio, per portare un gas da $(V_1,p_1)$ a $(V_2,p_2)$ con $V_2>V_1$ e $p_2<p_1$, si può prima espandere a pressione $p_1$ e poi raffreddare a volume costante (lavoro $p_1(V_2-V_1)$), oppure prima raffreddare a volume costante e poi espandere a pressione $p_2$ (lavoro $p_2(V_2-V_1)$, minore). In un **ciclo** il lavoro netto è l'area racchiusa dalla curva, positiva se il ciclo è percorso in senso orario.

Va anche osservato che la formula $\delta W = p\,dV$ richiede che la pressione del sistema sia definita durante la trasformazione, cioè che questa sia quasi statica. In una trasformazione brusca si usa invece la pressione esterna: $\delta W = p_{est}\,dV$, che è il lavoro effettivamente compiuto contro l'ambiente. Oltre al lavoro di volume esistono altre forme di lavoro termodinamico: il lavoro elettrico, il lavoro magnetico, il lavoro dovuto a un'elica che agita un fluido (lavoro "d'elica" o isocoro), che può essere solo fatto *sul* sistema e mai ricavato da esso.

### 12.4.2 Calore

Due corpi a temperature diverse, messi a contatto attraverso una parete diatermica, raggiungono dopo un certo tempo l'equilibrio termico: il corpo più caldo si raffredda e quello più freddo si scalda, senza che vi sia alcun lavoro macroscopico. Diciamo che fra i due corpi è avvenuto uno scambio di **calore**. Il calore $Q$ è l'energia trasferita fra sistema e ambiente a causa di una differenza di temperatura, attraverso meccanismi microscopici (urti molecolari, vibrazioni reticolari, radiazione) che non sono descrivibili come lavoro di forze macroscopiche.

Storicamente il calore fu interpretato come un fluido indistruttibile, il **calorico**, che passava dai corpi caldi a quelli freddi. Questa teoria spiegava bene la calorimetria, ma non riusciva a giustificare la produzione illimitata di calore per attrito, osservata ad esempio da Rumford nella trivellazione delle canne dei cannoni. Oggi sappiamo che il calore non è una sostanza contenuta nei corpi: un corpo possiede energia interna, non "calore". Il calore, come il lavoro, è energia **in transito** e ha senso solo in relazione a una trasformazione. Anch'esso non è una funzione di stato, e si indica con $\delta Q$ il calore infinitesimo.

Adottiamo la convenzione che $Q$ sia positivo quando il calore è **assorbito** dal sistema e negativo quando è ceduto. Si osservi la coerenza delle convenzioni: sono positivi sia il calore entrante sia il lavoro uscente, cioè le due quantità "naturali" di una macchina termica che assorbe calore e produce lavoro.

L'unità storica del calore è la **caloria** (cal), definita come la quantità di calore necessaria per innalzare da 14,5 °C a 15,5 °C la temperatura di un grammo d'acqua alla pressione atmosferica. In ambito alimentare si usa la "grande caloria" o kilocaloria (kcal). Nel SI, essendo il calore una forma di energia, l'unità è il **joule**.

### 12.4.3 Equivalente meccanico della caloria

Che calore e lavoro siano entrambi energia è stato dimostrato sperimentalmente da **James Prescott Joule** negli anni Quaranta dell'Ottocento con il celebre esperimento del **mulinello**. Un recipiente a pareti adiabatiche contiene una massa d'acqua nota; all'interno ruota un sistema di palette, azionato da pesi che scendono di un'altezza nota. Le palette agitano l'acqua e, per attrito viscoso, ne aumentano la temperatura. Il lavoro fatto sul sistema si calcola dalla variazione di energia potenziale dei pesi (corretta per l'energia cinetica residua e per gli attriti esterni): $W = Mgh$. L'aumento di temperatura dell'acqua permette di calcolare la quantità di calore che sarebbe stato necessario fornire per ottenere lo stesso effetto: $Q = m c\,\Delta T$ in calorie.

Joule osservò che il rapporto fra il lavoro speso e il calore "equivalente" è sempre lo stesso, indipendentemente dal modo in cui il lavoro è fornito (palette, compressione di un gas, corrente elettrica in una resistenza, attrito fra dischi metallici). Questo rapporto costante è detto **equivalente meccanico della caloria**:
$$J = \frac{W}{Q} \approx 4{,}186\ \mathrm{J/cal} .$$
Oggi, con il calore misurato direttamente in joule, $J$ non è più una costante fisica, ma un semplice fattore di conversione: $1\ \mathrm{cal} = 4{,}186\ \mathrm{J}$ (la "caloria termochimica" è definita esattamente come 4,184 J). Il significato concettuale dell'esperimento resta però fondamentale: è possibile produrre in un sistema la stessa variazione di stato fornendo calore oppure fornendo lavoro adiabaticamente, e le due modalità sono quantitativamente equivalenti. Questa è la premessa dell'esistenza dell'energia interna.

### 12.4.4 Energia interna

Consideriamo un sistema racchiuso da pareti adiabatiche e portiamolo da uno stato iniziale $i$ a uno stato finale $f$ fornendogli lavoro in modi diversi (agitazione, compressione, effetto Joule elettrico). L'esperienza, a partire da Joule, mostra che il **lavoro adiabatico** necessario per passare da $i$ a $f$ è sempre lo stesso, qualunque sia il percorso seguito. Ne segue che esiste una funzione dello stato del sistema, detta **energia interna** $U$, la cui variazione è uguale al lavoro adiabatico fatto sul sistema:
$$\Delta U = U_f - U_i = -W_{ad} .$$
(il segno meno deriva dalla convenzione per cui $W$ è il lavoro fatto *dal* sistema). L'energia interna è quindi una **funzione di stato** ed è **estensiva**; come ogni energia potenziale, è definita a meno di una costante additiva, e in termodinamica interessano solo le sue variazioni.

Dal punto di vista microscopico, l'energia interna è la somma delle energie cinetiche di agitazione delle particelle (misurate nel sistema di riferimento del centro di massa) e delle energie potenziali di interazione fra di esse, più eventuali energie di legame chimico e nucleare. Non comprende invece l'energia cinetica del moto d'insieme del sistema né l'energia potenziale dovuta a campi esterni, che sono energie "meccaniche" macroscopiche. Per un gas ideale, in cui le interazioni fra molecole sono trascurabili, l'energia interna è puramente cinetica e dipende solo dalla temperatura: $U = U(T)$. Per un gas reale, un liquido o un solido, l'energia interna dipende anche dal volume, perché la distanza media fra le particelle influisce sull'energia potenziale di interazione.

### 12.4.5 Primo principio della termodinamica

Se ora il sistema non è adiabatico, la variazione di energia interna non coincide più con il lavoro scambiato. Si **definisce** allora il calore scambiato come la differenza:
$$Q = \Delta U + W ,$$
ovvero, nella forma più nota,
$$\Delta U = Q - W .$$
Questo è il **primo principio della termodinamica**: la variazione dell'energia interna di un sistema chiuso è uguale al calore assorbito meno il lavoro compiuto dal sistema. In forma infinitesima, per una trasformazione quasi statica con solo lavoro di volume,
$$dU = \delta Q - p\,dV .$$
Il contenuto fisico del principio è duplice. Da un lato esso afferma l'esistenza della funzione di stato $U$ (che è un risultato sperimentale, non una definizione). Dall'altro estende la conservazione dell'energia a tutti i processi: l'energia di un sistema può cambiare solo per scambi con l'ambiente, sotto forma di calore o di lavoro. Benché $Q$ e $W$ dipendano singolarmente dal percorso, la loro differenza non ne dipende.

Alcune conseguenze immediate. Per un **sistema isolato** $Q = 0$ e $W = 0$, quindi $\Delta U = 0$: l'energia interna di un sistema isolato si conserva. Per una **trasformazione ciclica**, che riporta il sistema allo stato iniziale, $\Delta U = 0$ e quindi $Q = W$: il lavoro netto prodotto da una macchina ciclica è uguale al calore netto assorbito. Ne segue l'impossibilità del **moto perpetuo di prima specie**, cioè di una macchina che produca lavoro ciclicamente senza assorbire energia dall'esterno. Per una **trasformazione adiabatica** $\Delta U = -W$: un gas che si espande adiabaticamente compie lavoro a spese della propria energia interna e si raffredda; per questo il gas che esce da una bomboletta spray la raffredda. Per una trasformazione **isocora** (volume costante) $W=0$ e $\Delta U = Q$: tutto il calore fornito aumenta l'energia interna.

Va sottolineato che il primo principio non dice nulla sulla *direzione* dei processi: non vieta che il calore passi spontaneamente da un corpo freddo a uno caldo, né che un corpo si raffreddi spontaneamente trasformando tutta la sua energia interna in lavoro. Queste limitazioni sono il contenuto del secondo principio della termodinamica, che sarà trattato in seguito.

### Esercizio d'esempio

In un esperimento alla Joule, due masse di $M = 10{,}0\ \mathrm{kg}$ ciascuna scendono di $h = 2{,}00\ \mathrm{m}$ per 20 volte, azionando un mulinello immerso in $m = 1{,}50\ \mathrm{kg}$ d'acqua in un recipiente adiabatico. Si trascurino la capacità termica del recipiente e l'energia cinetica finale delle masse. (a) Quale aumento di temperatura si osserva? (b) Successivamente, all'acqua vengono forniti $Q = 8{,}0\ \mathrm{kJ}$ di calore mentre l'acqua stessa, tramite un pistone, compie un lavoro $W = 0{,}5\ \mathrm{kJ}$ sull'ambiente (si supponga per semplicità che possa farlo). Quanto varia l'energia interna? ($c = 4186\ \mathrm{J/(kg\,K)}$, $g = 9{,}81\ \mathrm{m/s^2}$.)

**Soluzione.**

(a) Il lavoro fatto sul sistema è
$$W_{sul} = 20 \times 2M g h = 20\times 2\times10{,}0\times9{,}81\times2{,}00\ \mathrm{J} = 7848\ \mathrm{J}.$$
Essendo il recipiente adiabatico, $\Delta U = W_{sul}$, e questa variazione di energia interna è la stessa che si otterrebbe fornendo un calore $Q = mc\,\Delta T$. Quindi
$$\Delta T = \frac{W_{sul}}{mc} = \frac{7848\ \mathrm{J}}{1{,}50\ \mathrm{kg}\times4186\ \mathrm{J/(kg\,K)}} \approx 1{,}25\ \mathrm{K}.$$
L'aumento è piccolo: per questo Joule dovette usare termometri sensibilissimi, leggendo frazioni di grado Fahrenheit.

(b) Dal primo principio
$$\Delta U = Q - W = 8{,}0\ \mathrm{kJ} - 0{,}5\ \mathrm{kJ} = 7{,}5\ \mathrm{kJ}.$$
L'energia interna del sistema aumenta di 7,5 kJ: i 0,5 kJ di lavoro ceduti all'ambiente sono energia che il sistema non trattiene.

### Punti chiave

- Il lavoro termodinamico di volume è $\delta W = p\,dV$; nel piano di Clapeyron è l'area sottesa alla curva e dipende dal percorso.
- Il calore è energia trasferita a causa di una differenza di temperatura; come il lavoro, non è una funzione di stato.
- L'esperimento di Joule ha stabilito l'equivalenza fra calore e lavoro: $1\ \mathrm{cal} \approx 4{,}186\ \mathrm{J}$.
- Il lavoro adiabatico fra due stati è indipendente dal percorso: ciò definisce l'energia interna $U$, funzione di stato estensiva.
- Primo principio: $\Delta U = Q - W$ (con $Q$ assorbito e $W$ compiuto dal sistema); in forma differenziale $dU = \delta Q - p\,dV$.
- In un ciclo $Q = W$; in un sistema isolato $U$ si conserva; il moto perpetuo di prima specie è impossibile.
- Il primo principio non stabilisce il verso dei processi: questo è il compito del secondo principio.

## 12.5 Trasformazioni termodinamiche

Si chiama **trasformazione termodinamica** qualunque processo che porti un sistema da uno stato di equilibrio iniziale a uno stato di equilibrio finale. Le trasformazioni si classificano secondo due criteri distinti. Il primo riguarda il *modo* in cui avvengono: lente o brusche, reversibili o irreversibili. Il secondo riguarda la *grandezza mantenuta costante*: pressione (isobara), volume (isocora), temperatura (isoterma), calore scambiato nullo (adiabatica). Per rendere concreti i risultati useremo spesso, come sistema di riferimento, il **gas ideale**, che obbedisce all'equazione di stato $pV = nRT$ e ha energia interna funzione della sola temperatura, $U = n c_V T$ (con $c_V$ calore specifico molare a volume costante, discusso nella sezione 12.6). Lo studio approfondito del gas ideale è rinviato al capitolo sulla meccanica dei gas; qui ne anticipiamo solo quanto basta per rendere quantitative le trasformazioni.

### 12.5.1 Quasi statica

Una trasformazione si dice **quasi statica** quando avviene così lentamente che il sistema attraversa una successione continua di stati di equilibrio. In ogni istante le variabili di stato sono definite e uniformi, e la trasformazione può essere rappresentata da una **curva continua** nel piano di Clapeyron. Il criterio di "lentezza" è relativo: la trasformazione deve durare molto più del tempo di rilassamento del sistema. Per un gas in un cilindro di qualche decimetro, il tempo di rilassamento meccanico è dell'ordine del tempo impiegato dal suono a percorrere il cilindro, cioè del millisecondo; perciò anche il moto di un pistone di motore, che dura qualche millisecondo per corsa, è in prima approssimazione quasi statico per quanto riguarda la pressione (non però per quanto riguarda gli scambi di calore, molto più lenti).

Operativamente, una trasformazione quasi statica si realizza modificando le condizioni esterne per passi infinitesimi: per comprimere un gas quasi staticamente si possono aggiungere sul pistone granelli di sabbia uno alla volta, attendendo ogni volta il nuovo equilibrio. Al contrario, una trasformazione **non quasi statica** (o brusca) porta il sistema attraverso stati di non equilibrio, nei quali pressione e temperatura non sono uniformi: si pensi a un gas che si espande liberamente nel vuoto quando si rompe una membrana (**espansione libera**). Una trasformazione del genere non può essere rappresentata da una curva nel piano $(V,p)$; si indicano soltanto gli stati iniziale e finale, spesso collegati da una linea tratteggiata, e il lavoro va calcolato con la pressione esterna.

### 12.5.2 Reversibile

Una trasformazione si dice **reversibile** quando può essere percorsa in senso inverso, riportando *sia il sistema sia l'ambiente* esattamente nei rispettivi stati iniziali, invertendo semplicemente il verso di una variazione infinitesima delle condizioni esterne. Condizione necessaria per la reversibilità è che la trasformazione sia quasi statica; ma non è sufficiente. Occorre anche che non vi siano **effetti dissipativi** (attriti, viscosità, isteresi, effetto Joule) e che gli scambi di calore avvengano fra corpi a temperature che differiscono solo di quantità infinitesime.

Esempio: un gas in un cilindro con pistone che scorre con attrito può essere compresso quasi staticamente, ma la trasformazione non è reversibile, perché nell'andata e nel ritorno l'attrito dissipa energia in entrambi i casi, e l'ambiente non torna allo stato iniziale. Analogamente, scaldare lentamente un corpo mettendolo a contatto con una sorgente molto più calda è un processo quasi statico per il corpo, ma è irreversibile perché il calore passa attraverso una differenza di temperatura finita. Per riscaldare un corpo reversibilmente bisognerebbe usare una successione infinita di sorgenti, ciascuna a temperatura infinitesimamente superiore alla precedente.

Tutte le trasformazioni reali sono **irreversibili**: la reversibilità è un'idealizzazione, analoga al moto senza attrito della meccanica. È però un'idealizzazione utilissima, perché le trasformazioni reversibili sono quelle per cui si possono scrivere relazioni esatte fra le variabili di stato ($\delta W = p\,dV$ con $p$ del sistema) e, come mostrerà il secondo principio, sono quelle che consentono le massime prestazioni delle macchine termiche.

### 12.5.3 Isobara

Una trasformazione **isobara** avviene a pressione costante. È la condizione tipica di tutti i processi che avvengono a contatto con l'atmosfera (cottura, ebollizione, reazioni chimiche in recipienti aperti) o in un cilindro chiuso da un pistone libero di peso costante. Nel piano di Clapeyron è un segmento orizzontale. Il lavoro è immediato:
$$W = \int_{V_i}^{V_f} p\,dV = p\,(V_f - V_i) .$$
Il primo principio fornisce $Q = \Delta U + p\,\Delta V = \Delta(U + pV)$. Conviene allora introdurre una nuova funzione di stato, l'**entalpia**
$$H = U + pV ,$$
la cui variazione in una trasformazione isobara coincide con il calore scambiato: $Q_p = \Delta H$. Per questo i chimici, che lavorano spesso a pressione atmosferica, tabulano le entalpie di reazione. Per un gas ideale, a pressione costante il volume è proporzionale alla temperatura (**legge di Gay-Lussac**, o di Charles): $V/T = \text{cost}$; riscaldando il gas, esso si espande compiendo lavoro, e il calore necessario è $Q = n c_p \Delta T$, maggiore di quello a volume costante.

### 12.5.4 Isocora

Una trasformazione **isocora** (o isometrica) avviene a volume costante, per esempio in un recipiente rigido. Nel piano di Clapeyron è un segmento verticale. Poiché $dV = 0$, il lavoro di volume è nullo:
$$W = 0 , \qquad \Delta U = Q_V .$$
Tutto il calore scambiato va a variare l'energia interna: è il motivo per cui il calore specifico a volume costante è direttamente legato all'energia interna. Per un gas ideale, a volume costante la pressione è proporzionale alla temperatura: $p/T = \text{cost}$ (seconda legge di Gay-Lussac), principio del termometro a gas a volume costante e spiegazione del pericolo di gettare nel fuoco una bomboletta spray: la pressione cresce con la temperatura fino a far esplodere il contenitore. Il calore scambiato vale $Q = n c_V\Delta T$. Si noti che anche in un'isocora si può fare lavoro *sul* sistema, per esempio con un'elica o con una resistenza elettrica: quello però non è lavoro di volume, e una tale trasformazione è irreversibile.

### 12.5.5 Isoterma

Una trasformazione **isoterma** avviene a temperatura costante. Per realizzarla in modo reversibile il sistema deve essere in contatto con un **termostato** (o serbatoio di calore), cioè un corpo di capacità termica così grande che la sua temperatura non cambia apprezzabilmente scambiando calore, e la trasformazione deve essere abbastanza lenta da mantenere l'equilibrio termico. Per un gas ideale l'isoterma obbedisce alla **legge di Boyle**: $pV = nRT = \text{cost}$, e nel piano di Clapeyron è un ramo di iperbole equilatera. Il lavoro vale
$$W = \int_{V_i}^{V_f} \frac{nRT}{V}\,dV = nRT\ln\frac{V_f}{V_i} .$$
Poiché l'energia interna del gas ideale dipende solo da $T$, si ha $\Delta U = 0$ e quindi
$$Q = W = nRT\ln\frac{V_f}{V_i} .$$
In un'espansione isoterma il gas assorbe dal termostato esattamente il calore che restituisce sotto forma di lavoro; in una compressione isoterma cede al termostato il lavoro ricevuto. Si noti che in un'isoterma c'è scambio di calore senza variazione di temperatura: calore e temperatura sono concetti ben distinti. Lo stesso accade, come vedremo, nelle transizioni di fase.

### 12.5.6 Adiabatica

Una trasformazione **adiabatica** avviene senza scambio di calore: $Q = 0$. Si realizza con pareti adiabatiche oppure con processi così rapidi che il calore non ha tempo di fluire (compressione nel cilindro di un motore diesel, propagazione del suono). Dal primo principio
$$\Delta U = -W .$$
In un'espansione adiabatica il sistema compie lavoro a spese della propria energia interna e si raffredda; in una compressione si scalda. È il principio di funzionamento del motore diesel, in cui l'aria compressa rapidamente raggiunge temperature sufficienti a innescare la combustione del gasolio, e la ragione per cui la pompa della bicicletta si scalda.

Per un gas ideale in una trasformazione adiabatica reversibile, combinando $dU = n c_V dT = -p\,dV$ con l'equazione di stato si ottiene, come mostreremo nel capitolo sui gas, la **legge di Poisson**
$$p V^{\gamma} = \text{cost} , \qquad \gamma = \frac{c_p}{c_V} > 1 ,$$
equivalente a $TV^{\gamma-1} = \text{cost}$. Nel piano di Clapeyron l'adiabatica è più ripida dell'isoterma passante per lo stesso punto, perché in un'espansione adiabatica la pressione diminuisce sia per l'aumento di volume sia per la diminuzione di temperatura. Per l'aria $\gamma\approx1{,}4$. Il lavoro adiabatico si calcola semplicemente da $W = -\Delta U = n c_V (T_i - T_f)$, oppure come $W = (p_iV_i - p_fV_f)/(\gamma-1)$.

È bene distinguere l'adiabatica reversibile da quella irreversibile: l'espansione libera di un gas nel vuoto è adiabatica ($Q=0$) e non compie lavoro ($W=0$), quindi $\Delta U = 0$ e, per un gas ideale, la temperatura finale è uguale a quella iniziale; ma non segue la legge di Poisson, perché non è quasi statica.

### Esercizio d'esempio

Due moli di gas ideale biatomico ($c_V = \tfrac52 R$, $\gamma = 1{,}4$) si trovano a $T_A = 300\ \mathrm{K}$ e $p_A = 2{,}00\times10^5\ \mathrm{Pa}$. Il gas si espande fino a raddoppiare il volume (a) isotermicamente, (b) isobaricamente, (c) adiabaticamente e reversibilmente. Calcolare in ciascun caso $W$, $Q$ e $\Delta U$. ($R = 8{,}314\ \mathrm{J/(mol\,K)}$.)

**Soluzione.** Il volume iniziale è $V_A = nRT_A/p_A = 2\times8{,}314\times300/2{,}00\times10^5 \approx 2{,}49\times10^{-2}\ \mathrm{m^3}$; quello finale $V_B = 4{,}99\times10^{-2}\ \mathrm{m^3}$.

(a) **Isoterma.** $\Delta U = 0$;
$$W = Q = nRT\ln 2 = 2\times8{,}314\times300\times0{,}693 \approx 3{,}46\ \mathrm{kJ}.$$

(b) **Isobara.** $T_B = 2T_A = 600\ \mathrm{K}$.
$$W = p\,\Delta V = 2{,}00\times10^5\times2{,}49\times10^{-2} \approx 4{,}99\ \mathrm{kJ},$$
$$\Delta U = n c_V\Delta T = 2\times\tfrac52\times8{,}314\times300 \approx 12{,}47\ \mathrm{kJ},$$
$$Q = \Delta U + W \approx 17{,}46\ \mathrm{kJ}\quad(= n c_p\Delta T = 2\times\tfrac72\times8{,}314\times300).$$

(c) **Adiabatica.** $T_B = T_A (V_A/V_B)^{\gamma-1} = 300\times 2^{-0{,}4} \approx 227\ \mathrm{K}$. Quindi $Q = 0$,
$$\Delta U = n c_V (T_B - T_A) = 2\times\tfrac52\times8{,}314\times(-72{,}7) \approx -3{,}02\ \mathrm{kJ},\qquad W = -\Delta U \approx 3{,}02\ \mathrm{kJ}.$$
Il confronto mostra che, a parità di volume finale, il lavoro è massimo nell'isobara e minimo nell'adiabatica, in accordo con le aree sottese nel piano di Clapeyron; la pressione finale vale rispettivamente $1{,}00\times10^5$, $2{,}00\times10^5$ e $0{,}76\times10^5\ \mathrm{Pa}$.

### Punti chiave

- Una trasformazione quasi statica è una successione di stati di equilibrio, rappresentabile da una curva nel piano di Clapeyron.
- Una trasformazione reversibile è quasi statica e priva di dissipazioni; tutte le trasformazioni reali sono irreversibili.
- Isobara: $W = p\Delta V$, $Q = \Delta H$ con $H = U + pV$ entalpia.
- Isocora: $W = 0$, $Q = \Delta U$.
- Isoterma del gas ideale: $\Delta U = 0$, $Q = W = nRT\ln(V_f/V_i)$; serve un termostato.
- Adiabatica: $Q = 0$, $\Delta U = -W$; per il gas ideale reversibile $pV^\gamma = \text{cost}$, curva più ripida dell'isoterma.
- L'espansione libera è adiabatica ma irreversibile e non segue la legge di Poisson.

## 12.6 Calore specifico

Quando si fornisce calore a un corpo, in assenza di transizioni di fase, la sua temperatura aumenta. Ma di quanto? L'esperienza quotidiana insegna che corpi diversi rispondono in modo molto diverso: una pentola di ferro vuota sul fuoco diventa rovente in pochi minuti, mentre la stessa pentola piena d'acqua richiede molto più tempo per scaldarsi. In questa sezione introduciamo le grandezze che quantificano questa risposta — capacità termica, calore specifico, calore specifico molare — e i metodi sperimentali per misurarle, cioè la **calorimetria**. Vedremo anche che, a differenza della massa o del volume, queste grandezze dipendono dalla trasformazione con cui il calore viene fornito, il che è una conseguenza diretta del fatto che il calore non è una funzione di stato.

### 12.6.1 Capacità termica

Si definisce **capacità termica** $C$ di un corpo il rapporto fra il calore infinitesimo assorbito e il corrispondente aumento di temperatura:
$$C = \frac{\delta Q}{dT} .$$
Si misura in $\mathrm{J/K}$. La capacità termica è una grandezza **estensiva**: raddoppiando la quantità di materia, raddoppia il calore necessario per ottenere lo stesso aumento di temperatura. Se $C$ è costante nell'intervallo considerato, il calore necessario per variare la temperatura da $T_i$ a $T_f$ è semplicemente
$$Q = C\,(T_f - T_i) ;$$
in generale, quando $C$ dipende dalla temperatura, occorre integrare: $Q = \int_{T_i}^{T_f} C(T)\,dT$.

Poiché $\delta Q$ non è un differenziale esatto, la capacità termica **dipende dalla trasformazione**: occorre sempre specificare in quali condizioni avviene il riscaldamento. Si definiscono in particolare la capacità termica a volume costante $C_V = (\delta Q/dT)_V$ e quella a pressione costante $C_p = (\delta Q/dT)_p$. Dal primo principio, in un'isocora $\delta Q = dU$, per cui
$$C_V = \left(\frac{\partial U}{\partial T}\right)_V ,$$
mentre in un'isobara $\delta Q = dH$ e quindi $C_p = (\partial H/\partial T)_p$. In generale $C_p > C_V$, perché a pressione costante il corpo si dilata e parte del calore fornito viene spesa per compiere lavoro contro l'ambiente. Per solidi e liquidi la differenza è piccola (qualche per cento), perché la dilatazione è modesta; per i gas è invece rilevante. In casi particolari la capacità termica può assumere valori estremi: in un'isoterma $dT = 0$ con $\delta Q \neq 0$, quindi formalmente $C = \infty$; in un'adiabatica $\delta Q = 0$ con $dT\neq0$, quindi $C = 0$. Esistono perfino trasformazioni (ad esempio certe politropiche) in cui $C<0$: il sistema assorbe calore e contemporaneamente si raffredda, perché compie più lavoro di quanto calore riceva.

Il concetto di capacità termica permette di precisare quello di **termostato** o **sorgente di calore**: è un corpo con capacità termica così grande (idealmente infinita) che può scambiare quantità finite di calore senza variare apprezzabilmente la propria temperatura. L'atmosfera, il mare, un grande bagno termostatato sono buone approssimazioni di sorgenti ideali.

### 12.6.2 Calore specifico

La capacità termica dipende dalla quantità di materia; per caratterizzare il *materiale* si divide per la massa, ottenendo il **calore specifico** (o capacità termica specifica)
$$c = \frac{C}{m} = \frac{1}{m}\frac{\delta Q}{dT} ,$$
grandezza intensiva misurata in $\mathrm{J/(kg\,K)}$. La relazione fondamentale della calorimetria, valida quando $c$ è costante e non ci sono transizioni di fase, è
$$Q = m\,c\,\Delta T .$$

L'**acqua** ha un calore specifico eccezionalmente elevato, $c \approx 4186\ \mathrm{J/(kg\,K)}$ (cioè 1 cal/(g K), per definizione storica della caloria). Per confronto: ghiaccio circa 2090, alluminio 900, vetro 840, ferro 450, rame 385, piombo 128 $\mathrm{J/(kg\,K)}$. Le conseguenze sono enormi: le grandi masse d'acqua (mari, laghi) mitigano il clima delle zone costiere immagazzinando calore d'estate e restituendolo d'inverno; l'acqua è il fluido di raffreddamento per eccellenza nei motori e negli impianti industriali; il corpo umano, composto per circa il 60% d'acqua, ha un'inerzia termica che lo protegge da sbalzi rapidi di temperatura.

La misura dei calori specifici si effettua con il **calorimetro**. Il più semplice è il **calorimetro delle mescolanze** (di Regnault): un recipiente con pareti adiabatiche (tipicamente un vaso Dewar) contenente una massa d'acqua nota $m_a$ a temperatura $T_a$. Si introduce un campione di massa $m_x$ preriscaldato a $T_x$ e si attende l'equilibrio alla temperatura $T_e$. Poiché il sistema complessivo è isolato e non compie lavoro, la somma dei calori scambiati è nulla:
$$\sum_k Q_k = 0 \quad\Rightarrow\quad m_x c_x (T_e - T_x) + (m_a c_a + C_{cal})(T_e - T_a) = 0 ,$$
dove $C_{cal}$ è la capacità termica del recipiente, del termometro e dell'agitatore. Questa si esprime spesso tramite l'**equivalente in acqua** del calorimetro, $m^* = C_{cal}/c_a$, cioè la massa d'acqua che avrebbe la stessa capacità termica. Nota $m^*$ (che si misura preliminarmente con una mescolanza di acque a temperature diverse), si ricava $c_x$. Altri calorimetri sfruttano il riscaldamento elettrico (si fornisce un calore noto $Q = VIt$ e si misura $\Delta T$), oppure la fusione del ghiaccio (calorimetro di Bunsen), in cui il calore si deduce dalla massa di ghiaccio fusa.

È importante sottolineare l'ipotesi di temperatura uniforme: $Q = mc\Delta T$ vale per un corpo in equilibrio, mentre durante il transitorio la temperatura non è uniforme. La temperatura di equilibrio di una mescolanza di corpi senza transizioni di fase risulta la **media pesata** delle temperature iniziali con pesi pari alle capacità termiche:
$$T_e = \frac{\sum_k m_k c_k T_k}{\sum_k m_k c_k} .$$

### 12.6.3 Calore specifico molare

Spesso è più significativo riferire la capacità termica alla quantità di sostanza anziché alla massa. Si definisce il **calore specifico molare** (o capacità termica molare)
$$c_m = \frac{C}{n} = M c ,$$
misurato in $\mathrm{J/(mol\,K)}$, dove $M$ è la massa molare. Nei capitoli sui gas, per brevità, il calore specifico molare si indica semplicemente con $c_V$ o $c_p$.

Il vantaggio di questa grandezza emerge chiaramente dai dati sperimentali. Nel 1819 **Dulong e Petit** osservarono che, a temperatura ambiente, il calore specifico molare della maggior parte dei solidi elementari è quasi lo stesso, circa
$$c_m \approx 3R \approx 25\ \mathrm{J/(mol\,K)} .$$
Ad esempio: rame $385\times0{,}0635 \approx 24{,}5$, alluminio $900\times0{,}027 \approx 24{,}3$, piombo $128\times0{,}207 \approx 26{,}5\ \mathrm{J/(mol\,K)}$. I calori specifici per unità di massa differiscono di un fattore sette, quelli molari sono praticamente uguali. La spiegazione viene dal **teorema di equipartizione dell'energia** (discusso nella meccanica statistica): ogni atomo del reticolo è un oscillatore tridimensionale con 3 gradi di libertà cinetici e 3 potenziali, ciascuno dei quali contribuisce in media $\tfrac12 k_BT$ all'energia; l'energia interna molare è quindi $U_m = 3RT$ e $c_m = 3R$. A basse temperature, però, il calore specifico dei solidi diminuisce e tende a zero (proporzionalmente a $T^3$ secondo il modello di Debye): è uno dei fallimenti della fisica classica che portarono alla meccanica quantistica (Einstein, 1907). Elementi leggeri e con legami forti, come il diamante, si discostano dalla legge di Dulong e Petit già a temperatura ambiente.

Per i **gas ideali** il calore specifico molare a volume costante vale $c_V = \tfrac{3}{2}R$ per i gas monoatomici (He, Ar), $\tfrac52 R$ per i biatomici a temperatura ambiente ($\mathrm{N_2}$, $\mathrm{O_2}$, aria), mentre la differenza fra i due calori specifici è data dalla **relazione di Mayer**
$$c_p - c_V = R ,$$
che si dimostra facilmente: in un'isobara di un gas ideale $\delta Q = dU + p\,dV = n c_V dT + nR\,dT$, perché $p\,dV = nR\,dT$ a pressione costante. Il rapporto $\gamma = c_p/c_V$ vale quindi $5/3$ per i monoatomici e $7/5$ per i biatomici, e governa le trasformazioni adiabatiche e la velocità del suono. Questi risultati saranno approfonditi nel capitolo sui gas; qui interessa sottolineare che il calore specifico molare è la grandezza naturale per confrontare sostanze diverse, perché riflette il numero di gradi di libertà microscopici per particella.

### Esercizio d'esempio

Un calorimetro delle mescolanze contiene $m_a = 0{,}300\ \mathrm{kg}$ d'acqua a $T_a = 20{,}0\ \mathrm{°C}$; il suo equivalente in acqua è $m^* = 0{,}040\ \mathrm{kg}$. Si introduce un blocco metallico di massa $m_x = 0{,}250\ \mathrm{kg}$ prelevato da acqua bollente ($T_x = 100{,}0\ \mathrm{°C}$). La temperatura di equilibrio risulta $T_e = 25{,}4\ \mathrm{°C}$. (a) Determinare il calore specifico del metallo. (b) Determinarne il calore specifico molare, sapendo che la massa molare è $M = 63{,}5\ \mathrm{g/mol}$, e confrontarlo con la legge di Dulong e Petit. ($c_a = 4186\ \mathrm{J/(kg\,K)}$.)

**Soluzione.**

(a) Il calore ceduto dal metallo è uguale a quello assorbito da acqua e calorimetro:
$$m_x c_x (T_x - T_e) = (m_a + m^*)\,c_a\,(T_e - T_a).$$
Il secondo membro vale $(0{,}340\ \mathrm{kg})(4186\ \mathrm{J/(kg\,K)})(5{,}4\ \mathrm{K}) \approx 7686\ \mathrm{J}$. Quindi
$$c_x = \frac{7686\ \mathrm{J}}{0{,}250\ \mathrm{kg}\times 74{,}6\ \mathrm{K}} \approx 412\ \mathrm{J/(kg\,K)}.$$

(b) Il calore specifico molare è
$$c_m = M c_x = 0{,}0635\ \mathrm{kg/mol}\times412\ \mathrm{J/(kg\,K)} \approx 26{,}2\ \mathrm{J/(mol\,K)},$$
vicino al valore di Dulong e Petit $3R \approx 24{,}9\ \mathrm{J/(mol\,K)}$, entro circa il 5%. Il metallo è verosimilmente rame (tabulato 385 J/(kg K)): lo scarto è attribuibile alle perdite di calore durante il trasferimento del blocco e all'acqua bollente trascinata con esso, errori sistematici tipici delle misure calorimetriche.

### Punti chiave

- La capacità termica $C = \delta Q/dT$ è estensiva e dipende dalla trasformazione; si distinguono $C_V = (\partial U/\partial T)_V$ e $C_p = (\partial H/\partial T)_p$.
- Il calore specifico $c = C/m$ è intensivo; senza transizioni di fase vale $Q = mc\Delta T$.
- L'acqua ha un calore specifico molto alto (4186 J/(kg K)), con effetti climatici e tecnici rilevanti.
- Nel calorimetro delle mescolanze la somma dei calori scambiati è nulla; la capacità del recipiente si esprime come equivalente in acqua.
- Il calore specifico molare $c_m = Mc$ dei solidi tende a $3R$ (Dulong e Petit), spiegato dall'equipartizione; a bassa temperatura tende a zero.
- Per i gas ideali $c_p - c_V = R$ (relazione di Mayer) e $\gamma = c_p/c_V$ è 5/3 o 7/5.

## 12.7 Transizioni di fase

La materia si presenta comunemente in tre **stati di aggregazione**: solido, liquido e gassoso. Una stessa sostanza può passare da uno stato all'altro variando temperatura e pressione: il ghiaccio fonde, l'acqua evapora, il vapore condensa, la naftalina sublima. Questi passaggi sono detti **transizioni di fase** (o cambiamenti di stato). Hanno una caratteristica che li distingue nettamente dal semplice riscaldamento: durante una transizione a pressione costante la temperatura **resta costante**, anche se il sistema continua ad assorbire o cedere calore. Il calore, in questo caso, non serve ad aumentare l'agitazione termica delle molecole, ma a modificare la struttura della materia, rompendo o formando legami intermolecolari. Lo studio delle transizioni di fase è essenziale in ingegneria: dalle centrali termoelettriche (dove l'acqua viene vaporizzata e condensata) ai frigoriferi (che sfruttano l'evaporazione di un fluido refrigerante), dalla metallurgia (fusione e solidificazione delle leghe) alla meteorologia (formazione delle nubi e delle precipitazioni).

### 12.7.1 Calore latente

Le transizioni prendono nomi specifici: **fusione** (solido → liquido) e **solidificazione** (inversa); **vaporizzazione** (liquido → vapore), che può avvenire come **evaporazione** superficiale a qualunque temperatura o come **ebollizione** in tutto il volume quando la tensione di vapore uguaglia la pressione esterna; **condensazione** (inversa); **sublimazione** (solido → vapore) e **brinamento** (inversa).

Il calore necessario per far cambiare fase a una massa $m$ di sostanza, a temperatura e pressione costanti, è proporzionale alla massa:
$$Q = m\,\lambda ,$$
dove $\lambda$ è il **calore latente** della transizione, misurato in $\mathrm{J/kg}$ (si usa anche il calore latente molare in $\mathrm{J/mol}$). L'aggettivo "latente" è storico: il calore assorbito sembrava "nascondersi" nella sostanza senza manifestarsi come aumento di temperatura. Per l'acqua a pressione atmosferica il calore latente di fusione vale $\lambda_f \approx 3{,}34\times10^5\ \mathrm{J/kg}$ e quello di vaporizzazione $\lambda_v \approx 2{,}26\times10^6\ \mathrm{J/kg}$. Per confronto, scaldare un chilogrammo d'acqua da 0 a 100 °C richiede $4{,}19\times10^5\ \mathrm{J}$: vaporizzarlo richiede più di cinque volte tanto. Questo spiega perché una scottatura da vapore è molto più grave di una da acqua bollente: il vapore, condensando sulla pelle, cede il proprio calore latente.

Le transizioni che richiedono calore (fusione, vaporizzazione, sublimazione) sono **endotermiche**; le inverse sono **esotermiche** e restituiscono la stessa quantità di calore. Il calore latente di vaporizzazione è molto maggiore di quello di fusione perché nel passaggio a vapore le molecole devono essere separate completamente, superando quasi tutta l'energia di coesione, mentre nella fusione si rompe solo l'ordine a lungo raggio del reticolo e le molecole restano vicine. Dal primo principio, in una transizione isobara $Q = \Delta H$, quindi il calore latente è la variazione di entalpia specifica fra le due fasi; poiché nella vaporizzazione c'è un forte aumento di volume, una parte del calore latente (circa 7-8% per l'acqua a 1 atm) serve a compiere il lavoro $p\,\Delta V$ contro l'atmosfera, e il resto aumenta l'energia interna.

L'evaporazione come processo di raffreddamento è onnipresente: il sudore, evaporando, sottrae al corpo il calore latente; l'acqua in una brocca di terracotta porosa resta fresca; nei cicli frigoriferi un fluido evapora a bassa pressione nell'evaporatore, assorbendo calore dalla cella. Si noti infine che la temperatura di transizione dipende dalla pressione: l'acqua bolle a circa 86 °C in cima al Monte Bianco e a circa 120 °C in una pentola a pressione.

### 12.7.2 Diagramma pT

Il comportamento di una sostanza pura si riassume efficacemente nel **diagramma di fase** nel piano pressione-temperatura. Esso è suddiviso in tre regioni (solido, liquido, vapore) da tre curve: la **curva di fusione** (solido-liquido), la **curva di vaporizzazione** o curva della tensione di vapore (liquido-vapore) e la **curva di sublimazione** (solido-vapore). Lungo ciascuna curva coesistono in equilibrio due fasi e, in accordo con la regola delle fasi, la varianza è 1: fissata $T$, la pressione di coesistenza è determinata. Le tre curve si incontrano nel **punto triplo**, a varianza zero, dove coesistono tutte e tre le fasi. Per l'acqua il punto triplo si trova a $T_{tr} = 273{,}16\ \mathrm{K}$ e $p_{tr} = 611{,}657\ \mathrm{Pa}$; per l'anidride carbonica a 216,6 K e 5,18 bar. Poiché la pressione del punto triplo della $\mathrm{CO_2}$ supera quella atmosferica, a pressione ambiente la $\mathrm{CO_2}$ solida ("ghiaccio secco") sublima senza fondere.

La pendenza delle curve di coesistenza è data dall'**equazione di Clausius-Clapeyron**, che si dimostrerà nel capitolo di termodinamica:
$$\frac{dp}{dT} = \frac{\lambda}{T\,(v_2 - v_1)} ,$$
dove $\lambda$ è il calore latente specifico e $v_2 - v_1$ la variazione di volume specifico nella transizione. Per la vaporizzazione e la sublimazione $v_2 > v_1$ e la pendenza è sempre positiva. Per la fusione della maggior parte delle sostanze il liquido è meno denso del solido e la pendenza è positiva (e molto ripida, perché $\Delta v$ è piccolo). L'acqua costituisce un'eccezione: il ghiaccio è meno denso del liquido, $\Delta v<0$, e la curva di fusione ha **pendenza negativa**. Aumentando la pressione, quindi, la temperatura di fusione del ghiaccio diminuisce (di circa 0,0074 K per atmosfera): è l'effetto sfruttato, almeno in parte, nell'esperimento del **rigelo**, in cui un filo metallico caricato con pesi attraversa lentamente un blocco di ghiaccio senza dividerlo.

La curva di vaporizzazione non prosegue indefinitamente ma termina nel **punto critico** ($T_c$, $p_c$): per l'acqua $T_c = 647\ \mathrm{K}$, $p_c = 22{,}1\ \mathrm{MPa}$. Oltre il punto critico non c'è più distinzione fra liquido e vapore: densità e calore latente delle due fasi coincidono, e si parla di **fluido supercritico**. È quindi possibile passare con continuità da liquido a vapore senza transizione di fase, aggirando il punto critico. La curva di fusione, invece, non ha punto critico noto: la differenza di simmetria fra solido cristallino e liquido non può svanire con continuità.

### 12.7.3 Diagramma pV

Nel piano di Clapeyron $(V,p)$ le transizioni di fase si visualizzano tracciando le isoterme di una sostanza reale (le celebri misure di **Andrews** sulla $\mathrm{CO_2}$, 1869). A temperatura sufficientemente alta, sopra $T_c$, le isoterme somigliano a quelle del gas ideale, iperboli $pV\approx\text{cost}$. Al di sotto di $T_c$, partendo da grandi volumi e comprimendo isotermicamente il vapore, la pressione aumenta finché non si raggiunge la **curva del vapore saturo secco**: qui compare la prima goccia di liquido. Da quel punto, continuando a ridurre il volume, la pressione resta costante, pari alla **tensione di vapore saturo** $p_s(T)$, mentre il vapore condensa progressivamente: l'isoterma presenta un **tratto orizzontale** (che è contemporaneamente isobara e isoterma). Quando tutto il vapore è condensato si raggiunge la **curva del liquido saturo**; oltre, il liquido è pochissimo comprimibile e l'isoterma sale quasi verticalmente.

L'insieme dei punti di inizio e fine condensazione forma la **curva di saturazione** (o campana di Andrews), il cui vertice è il punto critico. All'interno della campana coesistono liquido e vapore; a sinistra c'è liquido, a destra vapore surriscaldato (detto **vapore** se $T<T_c$, perché può essere liquefatto per sola compressione), sopra la isoterma critica c'è **gas**, che non può essere liquefatto per sola compressione. L'isoterma critica presenta nel punto critico un **flesso a tangente orizzontale**:
$$\left(\frac{\partial p}{\partial V}\right)_{T_c} = 0, \qquad \left(\frac{\partial^2 p}{\partial V^2}\right)_{T_c} = 0 .$$

All'interno della campana lo stato del sistema bifase è individuato dal **titolo** $x$, frazione in massa di vapore. Per la "regola della leva", il volume specifico della miscela è
$$v = (1-x)\,v_l + x\,v_v ,$$
dove $v_l$ e $v_v$ sono i volumi specifici di liquido e vapore saturi: un punto nel tratto orizzontale divide il segmento in parti inversamente proporzionali alle masse delle due fasi. Il diagramma $pV$ e il diagramma $pT$ sono due proiezioni della stessa superficie $p(V,T)$: le regioni bifase, che nel $pV$ sono aree, nel $pT$ si proiettano su curve, e la linea tripla del $pV$ (un segmento orizzontale a $p_{tr}$) si proietta sul punto triplo. Il modello di **van der Waals**, che sarà discusso con i gas reali, riproduce qualitativamente le isoterme di Andrews e il punto critico.

### Esercizio d'esempio

In un recipiente adiabatico contenente $m_a = 0{,}500\ \mathrm{kg}$ d'acqua a $30{,}0\ \mathrm{°C}$ si introducono $m_g = 0{,}100\ \mathrm{kg}$ di ghiaccio a $-10{,}0\ \mathrm{°C}$. Determinare la temperatura di equilibrio. ($c_a = 4186\ \mathrm{J/(kg\,K)}$, $c_g = 2090\ \mathrm{J/(kg\,K)}$, $\lambda_f = 3{,}34\times10^5\ \mathrm{J/kg}$; capacità del recipiente trascurabile.)

**Soluzione.** Conviene prima verificare se il ghiaccio fonde completamente. Il calore necessario per portare il ghiaccio a 0 °C e fonderlo tutto è
$$Q_1 = m_g c_g (10{,}0\ \mathrm{K}) + m_g\lambda_f = 0{,}100\times2090\times10 + 0{,}100\times3{,}34\times10^5 = 2090 + 33\,400 = 35\,490\ \mathrm{J}.$$
Il calore massimo che l'acqua può cedere raffreddandosi fino a 0 °C è
$$Q_2 = m_a c_a (30{,}0\ \mathrm{K}) = 0{,}500\times4186\times30 = 62\,790\ \mathrm{J}.$$
Poiché $Q_2>Q_1$, tutto il ghiaccio fonde e la temperatura finale $\theta_e$ è sopra 0 °C. Il bilancio è
$$m_g c_g(10) + m_g\lambda_f + m_g c_a(\theta_e - 0) = m_a c_a (30 - \theta_e),$$
$$35\,490 + 418{,}6\,\theta_e = 62\,790 - 2093\,\theta_e \;\Rightarrow\; \theta_e = \frac{27\,300}{2511{,}6} \approx 10{,}9\ \mathrm{°C}.$$
Se invece $Q_2$ fosse risultato minore di $Q_1$, la temperatura finale sarebbe stata esattamente 0 °C con una frazione di ghiaccio non fusa, determinata dal bilancio: è un esempio concreto di sistema bifase a varianza 1 a pressione fissata.

### Punti chiave

- Durante una transizione di fase a pressione costante la temperatura resta costante; il calore scambiato è $Q = m\lambda$.
- Per l'acqua $\lambda_f \approx 334\ \mathrm{kJ/kg}$ e $\lambda_v \approx 2260\ \mathrm{kJ/kg}$; il calore latente coincide con la variazione di entalpia.
- Nel diagramma $pT$ tre curve di coesistenza si incontrano nel punto triplo; la curva di vaporizzazione termina nel punto critico.
- La pendenza delle curve è data dalla Clausius-Clapeyron; per l'acqua la curva di fusione ha pendenza negativa.
- Nel diagramma $pV$ le isoterme subcritiche hanno un tratto orizzontale alla tensione di vapore; la campana di saturazione ha vertice nel punto critico.
- Nella regione bifase lo stato è descritto dal titolo $x$ e vale la regola della leva $v = (1-x)v_l + x v_v$.
- Sopra la temperatura critica il gas non può essere liquefatto per sola compressione.

## 12.8 Trasmissione del calore

Finora abbiamo trattato il calore come una quantità scambiata fra stati di equilibrio, senza chiederci *come* e *con quale rapidità* esso passi da un corpo all'altro. Nella pratica ingegneristica, però, la velocità dello scambio è spesso la questione decisiva: quanto calore disperde una parete in inverno, quanto rapidamente si raffredda un processore, quale spessore di isolante serve per un forno, quanta superficie deve avere un radiatore. Il calore si trasmette attraverso tre meccanismi fisicamente distinti: la **conduzione**, la **convezione** e l'**irraggiamento**. Nei casi reali essi agiscono quasi sempre contemporaneamente, ma è utile studiarli separatamente. La grandezza centrale è la **potenza termica** (o flusso di calore) $\dot Q = dQ/dt$, misurata in watt, e la sua densità per unità di superficie, misurata in $\mathrm{W/m^2}$.

### 12.8.1 Conduzione

La **conduzione** è il trasferimento di calore attraverso un mezzo materiale senza moto macroscopico della materia. Avviene per interazione diretta fra particelle adiacenti: nei gas tramite gli urti fra molecole più veloci (zone calde) e più lente (zone fredde); nei solidi isolanti tramite la propagazione delle vibrazioni reticolari (fononi); nei metalli soprattutto tramite gli elettroni liberi, il che spiega perché i buoni conduttori elettrici sono anche buoni conduttori termici (legge di Wiedemann-Franz).

La legge fenomenologica della conduzione è la **legge di Fourier**: la densità di corrente termica $\vec{q}$ è proporzionale e opposta al gradiente di temperatura,
$$\vec{q} = -k\,\nabla T ,$$
dove $k$ è la **conducibilità termica** del materiale, misurata in $\mathrm{W/(m\,K)}$. Il segno meno esprime il fatto che il calore fluisce dalle zone calde a quelle fredde. Valori tipici: rame 400, alluminio 237, acciaio 50, vetro 0,8, mattone 0,6, acqua 0,6, legno 0,1-0,2, lana di roccia e polistirolo 0,03-0,04, aria ferma 0,026 $\mathrm{W/(m\,K)}$. I migliori isolanti termici sono materiali che intrappolano aria in piccole cavità, impedendone il moto convettivo: lana, piume, schiume, doppi vetri.

Per una **lastra piana** di spessore $L$ e area $A$, con le facce mantenute a temperature $T_1>T_2$, in regime stazionario il gradiente è uniforme e la potenza trasmessa è
$$\dot Q = k A\,\frac{T_1 - T_2}{L} .$$
Questa relazione ha la stessa struttura della legge di Ohm: la differenza di temperatura gioca il ruolo della differenza di potenziale, la potenza termica quello della corrente. Si definisce perciò la **resistenza termica** $R_{th} = L/(kA)$, in $\mathrm{K/W}$, tale che $\dot Q = \Delta T/R_{th}$. L'analogia è potentissima: per una **parete composta** da più strati in serie (intonaco, mattoni, isolante) la resistenza totale è la somma delle resistenze, $R_{tot} = \sum_i L_i/(k_iA)$, mentre per elementi affiancati in parallelo (una finestra in un muro) si sommano le conduttanze. Lo strato con la resistenza più alta (tipicamente l'isolante) domina il comportamento.

Per un **guscio cilindrico** (tubo) di raggi $r_1<r_2$ e lunghezza $\ell$, la potenza attraverso ogni superficie cilindrica è la stessa e si ottiene integrando $\dot Q = -k(2\pi r\ell)\,dT/dr$:
$$\dot Q = \frac{2\pi k \ell\,(T_1 - T_2)}{\ln(r_2/r_1)} .$$
In regime non stazionario la conduzione è descritta dall'**equazione del calore** $\partial T/\partial t = D\,\nabla^2 T$, con $D = k/(\rho c)$ diffusività termica: essa governa, ad esempio, il riscaldamento di un arrosto in forno o la penetrazione dell'onda termica giornaliera nel terreno.

### 12.8.2 Convezione

La **convezione** è il trasporto di calore associato al moto macroscopico di un fluido. Una porzione di fluido riscaldata si sposta trasportando con sé la propria energia interna (più precisamente, la propria entalpia) e la cede altrove. Si distingue la **convezione naturale** (o libera), in cui il moto è causato dalle differenze di densità prodotte dalle differenze di temperatura — il fluido caldo, meno denso, sale per la spinta di Archimede e quello freddo scende — dalla **convezione forzata**, in cui il moto è imposto da agenti esterni (ventilatori, pompe, vento). Sono esempi di convezione naturale i moti dell'aria attorno a un termosifone, le brezze di mare e di terra, i moti del mantello terrestre e della fotosfera solare; sono esempi di convezione forzata il raffreddamento di un processore con ventola, il circuito di raffreddamento di un motore, l'asciugacapelli.

La descrizione dettagliata della convezione richiede la fluidodinamica ed è in generale complessa. Per gli scopi pratici si usa la **legge di Newton del raffreddamento**: la potenza scambiata fra una superficie a temperatura $T_s$ e un fluido a temperatura $T_f$ (lontano dalla superficie) è
$$\dot Q = h A\,(T_s - T_f) ,$$
dove $h$ è il **coefficiente di scambio convettivo** (o di adduzione), in $\mathrm{W/(m^2\,K)}$. Questo coefficiente non è una proprietà del materiale, ma dipende dalla geometria, dal fluido, dalla velocità del flusso e dal regime (laminare o turbolento). Ordini di grandezza: convezione naturale in aria 5-25, convezione forzata in aria 10-200, convezione forzata in acqua 100-10 000, ebollizione e condensazione fino a $10^5\ \mathrm{W/(m^2\,K)}$. Anche qui si definisce una resistenza termica convettiva $R = 1/(hA)$, da sommare in serie a quelle conduttive: la trasmittanza di una parete reale comprende le resistenze liminari interna ed esterna.

Fisicamente, vicino a una superficie solida il fluido aderisce alla parete e forma uno **strato limite** sottile in cui la velocità è bassa e il calore passa per conduzione; all'esterno di esso il fluido rimescolato trasporta l'energia. Aumentare la velocità del fluido assottiglia lo strato limite e aumenta $h$: ecco perché il vento rende più intensa la sensazione di freddo ("wind chill") e perché soffiare sulla minestra la raffredda più rapidamente.

Una conseguenza importante della legge di Newton riguarda il raffreddamento di un corpo di capacità termica $C$ e temperatura uniforme $T(t)$ immerso in un ambiente a $T_f$. Dal bilancio $C\,dT/dt = -hA(T - T_f)$ si ottiene un decadimento esponenziale:
$$T(t) = T_f + (T_0 - T_f)\,e^{-t/\tau}, \qquad \tau = \frac{C}{hA} .$$
L'ipotesi di temperatura uniforme è giustificata quando la resistenza conduttiva interna è piccola rispetto a quella convettiva esterna (numero di Biot piccolo).

### 12.8.3 Irraggiamento

L'**irraggiamento** è la trasmissione di energia mediante **onde elettromagnetiche**. Ogni corpo a temperatura assoluta non nulla emette radiazione, a causa dell'agitazione termica delle cariche che lo compongono. A differenza della conduzione e della convezione, l'irraggiamento **non richiede un mezzo materiale**: è il modo con cui l'energia del Sole raggiunge la Terra attraverso il vuoto interplanetario. A temperatura ambiente la radiazione emessa è concentrata nell'infrarosso (invisibile all'occhio, ma rilevabile dalle termocamere); a temperature di qualche migliaio di kelvin si sposta nel visibile, come nel filamento di una lampadina a incandescenza o in un metallo incandescente.

Si chiama **corpo nero** un corpo ideale che assorbe tutta la radiazione incidente, qualunque sia la lunghezza d'onda. Una buona realizzazione è una cavità con un piccolo foro: la radiazione che entra viene riflessa molte volte all'interno e assorbita quasi completamente. Il corpo nero è anche l'emettitore più efficiente possibile a una data temperatura. La potenza emessa per unità di superficie da un corpo nero obbedisce alla **legge di Stefan-Boltzmann**:
$$\frac{\dot Q}{A} = \sigma T^4 , \qquad \sigma = 5{,}67\times10^{-8}\ \mathrm{W/(m^2\,K^4)} .$$
Per un corpo reale si introduce l'**emissività** $\varepsilon$ ($0\le\varepsilon\le1$): $\dot Q = \varepsilon\sigma A T^4$. La **legge di Kirchhoff** afferma che, all'equilibrio, l'emissività di una superficie è uguale al suo coefficiente di assorbimento alla stessa lunghezza d'onda: un buon assorbitore è un buon emettitore. Per questo le superfici metalliche lucide (bassa emissività) sono usate per ridurre gli scambi radiativi, come nelle pareti argentate dei thermos e nelle coperte isotermiche di emergenza.

La distribuzione spettrale della radiazione di corpo nero, spiegata da Planck nel 1900 con l'ipotesi dei quanti, ha un massimo a una lunghezza d'onda inversamente proporzionale alla temperatura (**legge di Wien**):
$$\lambda_{max}\,T = 2{,}898\times10^{-3}\ \mathrm{m\,K} .$$
Il Sole, con temperatura superficiale di circa 5800 K, ha il massimo attorno a 500 nm (verde-giallo, al centro del visibile); il corpo umano, a circa 310 K, ha il massimo attorno a 9,3 µm, nell'infrarosso. Questo è il principio dei termometri a infrarosso e dei pirometri.

Un corpo a temperatura $T$ in un ambiente a temperatura $T_a$ emette e contemporaneamente assorbe radiazione; la potenza netta scambiata è
$$\dot Q_{netta} = \varepsilon\sigma A\,(T^4 - T_a^4) .$$
Per piccole differenze di temperatura, $T^4 - T_a^4 \approx 4T_a^3(T-T_a)$, e lo scambio radiativo assume la stessa forma della legge di Newton con un coefficiente equivalente $h_r = 4\varepsilon\sigma T_a^3$, che a temperatura ambiente vale circa $6\ \mathrm{W/(m^2\,K)}$ per $\varepsilon\approx1$: confrontabile con la convezione naturale, per cui nei problemi di climatizzazione l'irraggiamento non può essere trascurato. L'**effetto serra** nasce proprio dalla diversa trasparenza dell'atmosfera alla radiazione solare (visibile, che la attraversa) e a quella terrestre (infrarossa, parzialmente assorbita da vapore acqueo e anidride carbonica e riemessa verso il suolo).

### Esercizio d'esempio

Una parete di una stanza ha area $A = 12{,}0\ \mathrm{m^2}$ ed è formata da uno strato di mattoni ($L_1 = 0{,}20\ \mathrm{m}$, $k_1 = 0{,}60\ \mathrm{W/(m\,K)}$) e da uno strato di polistirolo ($L_2 = 0{,}050\ \mathrm{m}$, $k_2 = 0{,}035\ \mathrm{W/(m\,K)}$). I coefficienti convettivi sono $h_i = 8{,}0\ \mathrm{W/(m^2\,K)}$ all'interno e $h_e = 25\ \mathrm{W/(m^2\,K)}$ all'esterno. L'aria interna è a 20 °C, quella esterna a 0 °C. (a) Calcolare la potenza dispersa. (b) Calcolare la temperatura della faccia interna della parete. (c) Stimare la potenza irraggiata netta da una persona (superficie $1{,}8\ \mathrm{m^2}$, $\varepsilon = 0{,}97$, pelle a 307 K) verso la faccia interna della parete, supponendo che la persona sia circondata da superfici a quella temperatura.

**Soluzione.**

(a) Le resistenze in serie (per unità di area, moltiplicate poi per $1/A$) valgono:
$$\tfrac{1}{h_i} = 0{,}125,\quad \tfrac{L_1}{k_1} = 0{,}333,\quad \tfrac{L_2}{k_2} = 1{,}429,\quad \tfrac{1}{h_e} = 0{,}040\ \ \mathrm{m^2K/W}.$$
La somma è $1{,}927\ \mathrm{m^2K/W}$; quindi $R_{tot} = 1{,}927/12{,}0 \approx 0{,}161\ \mathrm{K/W}$ e
$$\dot Q = \frac{\Delta T}{R_{tot}} = \frac{20\ \mathrm{K}}{0{,}161\ \mathrm{K/W}} \approx 125\ \mathrm{W}.$$
Senza polistirolo la resistenza sarebbe $0{,}498/12$ $\mathrm{K/W}$ e la potenza circa 480 W: l'isolante riduce le perdite di quasi quattro volte.

(b) La caduta di temperatura sullo strato liminare interno è $\dot Q/(h_iA) = 125/(8{,}0\times12{,}0) \approx 1{,}3\ \mathrm{K}$, quindi la faccia interna è a circa $18{,}7\ \mathrm{°C} = 291{,}8\ \mathrm{K}$.

(c) La potenza radiativa netta è
$$\dot Q = \varepsilon\sigma A\,(T^4 - T_a^4) = 0{,}97\times5{,}67\times10^{-8}\times1{,}8\times(307^4 - 291{,}8^4)\ \mathrm{W}.$$
Con $307^4 \approx 8{,}883\times10^9$ e $291{,}8^4 \approx 7{,}250\times10^9\ \mathrm{K^4}$, la differenza è $1{,}633\times10^9\ \mathrm{K^4}$, da cui $\dot Q \approx 162\ \mathrm{W}$. È una potenza superiore al metabolismo basale di una persona a riposo (circa 100 W): per questo ci si sente infreddoliti vicino a pareti fredde anche se l'aria è a 20 °C, e l'isolamento migliora il comfort non solo riducendo le dispersioni ma anche alzando la temperatura delle superfici interne.

### Punti chiave

- Il calore si trasmette per conduzione, convezione e irraggiamento; la grandezza chiave è la potenza termica in watt.
- Legge di Fourier: $\vec q = -k\nabla T$; per una lastra $\dot Q = kA\Delta T/L$.
- La resistenza termica $R = L/(kA)$ permette di trattare pareti composte come resistori in serie e in parallelo.
- Convezione: legge di Newton $\dot Q = hA(T_s - T_f)$; $h$ dipende da fluido, geometria e velocità; il raffreddamento di un corpo è esponenziale con $\tau = C/(hA)$.
- Irraggiamento: non richiede mezzo; legge di Stefan-Boltzmann $\dot Q = \varepsilon\sigma AT^4$ e scambio netto $\varepsilon\sigma A(T^4 - T_a^4)$.
- Legge di Kirchhoff: buoni assorbitori sono buoni emettitori; legge di Wien: $\lambda_{max}T = 2{,}898\times10^{-3}\ \mathrm{m\,K}$.
- A temperatura ambiente lo scambio radiativo è confrontabile con la convezione naturale e non va trascurato.
