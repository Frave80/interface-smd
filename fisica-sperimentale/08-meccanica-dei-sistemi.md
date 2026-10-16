# Capitolo 8 — Meccanica dei sistemi

Finora si è studiato il moto di un singolo **punto materiale**, un'idealizzazione in cui un corpo è rappresentato da una massa concentrata in un punto geometrico. Questa schematizzazione funziona bene quando le dimensioni del corpo sono trascurabili rispetto alle distanze in gioco e quando non interessano i moti interni (rotazioni, deformazioni, vibrazioni). Nella realtà, però, i corpi sono estesi e composti da moltissime parti che interagiscono tra loro, e spesso si studiano insiemi di più corpi: due auto che si urtano, un razzo che espelle gas, un sistema Terra-Luna. In questo capitolo si passa dunque dal punto al **sistema di punti materiali**, introducendo il concetto di **centro di massa**, generalizzando quantità di moto, momento angolare ed energia, e ricavando le **equazioni cardinali** della dinamica dei sistemi. Il risultato centrale è che il moto complessivo di un sistema è governato soltanto dalle forze *esterne*, mentre le forze *interne* — pur potendo essere enormi — si elidono a coppie nelle equazioni globali per il terzo principio della dinamica. Questi strumenti permettono infine di trattare in modo sistematico gli **urti**, processi di interazione brevi e intensi di fondamentale importanza in fisica e in ingegneria.

## 8.1 Cinematica dei sistemi

Un **sistema di punti materiali** è un insieme di $N$ punti, di masse $m_1, m_2, \dots, m_N$ e posizioni $\vec{r}_1, \vec{r}_2, \dots, \vec{r}_N$, che si considera nel suo complesso. Può essere **discreto**, se composto da un numero finito di masse distinte (un sistema di pianeti, una molecola, due carrelli collegati da una molla), oppure **continuo**, se la massa è distribuita con continuità in una regione dello spazio (una sbarra, una lamina, un volume di fluido). Si dice **rigido** se le distanze reciproche tra i punti restano costanti, **deformabile** altrimenti. Descrivere istante per istante la posizione di ciascun punto richiede $3N$ coordinate, un numero che per corpi macroscopici è astronomico. La cinematica dei sistemi si propone di individuare grandezze globali che riassumano gli aspetti essenziali del moto; la più importante è la posizione del **centro di massa**. Per trattare i sistemi continui occorre inoltre introdurre il concetto di **densità**, che permette di sostituire le somme sui singoli punti con integrali.

### 8.1.1 Centro di massa

Si definisce **centro di massa** (CM) di un sistema discreto il punto geometrico la cui posizione è la media delle posizioni dei punti pesata con le rispettive masse:

$$
\vec{r}_{CM} = \frac{\sum_{i=1}^{N} m_i\vec{r}_i}{\sum_{i=1}^{N} m_i} = \frac{1}{M}\sum_{i=1}^{N} m_i\vec{r}_i, \qquad M = \sum_{i=1}^{N} m_i.
$$

In componenti cartesiane, $x_{CM} = \frac{1}{M}\sum m_i x_i$, e analogamente per $y$ e $z$. Il centro di massa è un **punto geometrico**, non necessariamente occupato da materia: il centro di massa di un anello omogeneo coincide con il suo centro, dove non c'è massa; quello di un boomerang si trova fuori dal corpo.

La definizione è indipendente dall'origine scelta, nel senso che cambiando origine la posizione del CM si sposta esattamente come quella di qualunque altro punto fisso: il CM è un punto ben definito del sistema. Alcune proprietà facilitano il calcolo. La prima è la **proprietà distributiva** (o di composizione): se un sistema è diviso in sottosistemi, il CM complessivo si ottiene trattando ciascun sottosistema come un punto di massa pari alla sua massa totale, collocato nel proprio CM. La seconda riguarda le **simmetrie**: se il sistema ha un piano, un asse o un centro di simmetria materiale (simmetria sia geometrica sia nella distribuzione della massa), il CM giace su di esso. Così il CM di una sfera omogenea è il centro, quello di un cilindro omogeneo il punto medio dell'asse. La terza è che il CM giace sempre all'interno dell'**inviluppo convesso** dei punti del sistema: per due masse sta sul segmento che le congiunge, più vicino alla massa maggiore. Per due punti, infatti, $m_1 d_1 = m_2 d_2$, dove $d_1$ e $d_2$ sono le distanze dal CM: è la stessa relazione della leva in equilibrio, e non è un caso.

Derivando rispetto al tempo la posizione del CM si ottengono la **velocità** e l'**accelerazione del centro di massa**:

$$
\vec{v}_{CM} = \frac{1}{M}\sum_i m_i\vec{v}_i, \qquad \vec{a}_{CM} = \frac{1}{M}\sum_i m_i\vec{a}_i,
$$

valide se le masse sono costanti. La prima relazione, moltiplicata per $M$, dice che $M\vec{v}_{CM} = \sum m_i\vec{v}_i$: la **quantità di moto totale** del sistema è uguale a quella di un punto di massa $M$ che si muova con il centro di massa. Questa identità, apparentemente semplice, sarà la chiave della dinamica dei sistemi.

Il centro di massa coincide con il **baricentro**, cioè con il punto di applicazione della risultante delle forze peso, se il campo gravitazionale è uniforme nella regione occupata dal sistema. Per corpi di dimensioni ordinarie sulla superficie terrestre questa condizione è soddisfatta con ottima approssimazione; non lo è per corpi enormi, come la Luna sottoposta al campo non uniforme della Terra, il che dà origine agli effetti di marea.

È spesso utile introdurre il **sistema di riferimento del centro di massa**, cioè un riferimento con origine nel CM e assi che traslano senza ruotare rispetto a un riferimento inerziale. In esso, per definizione, la quantità di moto totale è nulla: $\sum m_i\vec{v}_i' = 0$, dove gli apici indicano le velocità relative al CM. Le posizioni rispetto al CM, $\vec{r}_i' = \vec{r}_i - \vec{r}_{CM}$, soddisfano $\sum m_i\vec{r}_i' = 0$. Questo riferimento semplifica moltissimo lo studio degli urti e delle rotazioni. Se il sistema è isolato il CM si muove di moto rettilineo uniforme e il riferimento del CM è inerziale; in caso contrario non lo è, ma, come si vedrà, alcuni teoremi continuano a valere in esso in forma semplice.

### 8.1.2 Densità

Per un corpo esteso, in cui la massa è distribuita con continuità, la somma discreta va sostituita con un integrale. Si introduce a tal fine la **densità** (o massa volumica), definita come il rapporto tra la massa $\mathrm{d}m$ contenuta in un volumetto $\mathrm{d}V$ e il volume stesso:

$$
\rho(\vec{r}) = \frac{\mathrm{d}m}{\mathrm{d}V}.
$$

La densità si misura in $\mathrm{kg/m^3}$. Si tratta di un concetto macroscopico: il volumetto $\mathrm{d}V$ deve essere piccolo rispetto alle dimensioni del corpo e alle scale su cui la densità varia apprezzabilmente, ma grande rispetto alle distanze interatomiche, in modo da contenere un numero enorme di atomi e da poter mediare sulla struttura discreta della materia. Questa è l'**ipotesi del continuo**, alla base della meccanica dei solidi e dei fluidi. Un corpo si dice **omogeneo** se la densità è la stessa in ogni punto. Valori tipici: acqua $1000\ \mathrm{kg/m^3}$, alluminio $2700\ \mathrm{kg/m^3}$, acciaio circa $7800\ \mathrm{kg/m^3}$, aria a condizioni normali circa $1{,}2\ \mathrm{kg/m^3}$.

Per corpi in cui una o due dimensioni sono trascurabili si definiscono una **densità superficiale** $\sigma = \mathrm{d}m/\mathrm{d}S$, in $\mathrm{kg/m^2}$, per lamine e gusci sottili, e una **densità lineare** $\lambda = \mathrm{d}m/\mathrm{d}\ell$, in $\mathrm{kg/m}$, per fili e sbarre sottili. La massa totale si ottiene integrando:

$$
M = \int_V\rho\,\mathrm{d}V = \int_S\sigma\,\mathrm{d}S = \int_\ell\lambda\,\mathrm{d}\ell,
$$

a seconda della geometria. Analogamente, la posizione del centro di massa di un corpo continuo è

$$
\vec{r}_{CM} = \frac{1}{M}\int_V\vec{r}\,\rho(\vec{r})\,\mathrm{d}V.
$$

Due esempi chiariscono il metodo. Per una **sbarra omogenea** di lunghezza $L$ e densità lineare costante $\lambda$, disposta lungo l'asse $x$ tra $0$ e $L$, si ha $x_{CM} = \frac{1}{\lambda L}\int_0^L x\lambda\,\mathrm{d}x = L/2$, come suggerisce la simmetria. Se invece la densità cresce linearmente, $\lambda(x) = \lambda_0 x/L$, si ottiene $M = \lambda_0 L/2$ e $x_{CM} = \frac{1}{M}\int_0^L x\frac{\lambda_0 x}{L}\mathrm{d}x = \frac{2}{3}L$: il CM si sposta verso l'estremo più denso. Per una **lamina triangolare** omogenea il CM coincide con il baricentro geometrico, intersezione delle mediane, a un terzo dell'altezza dalla base; per un **cono** omogeneo pieno sta sull'asse a un quarto dell'altezza dalla base; per una **semisfera** piena a $3R/8$ dalla base.

Il concetto di densità si collega anche a quello di **densità relativa**, rapporto tra la densità di un corpo e quella dell'acqua a $4\,^\circ\mathrm{C}$, adimensionale, usata in idrostatica per valutare il galleggiamento. Inoltre, nei corpi compositi si può usare la proprietà distributiva del CM anche per sottrazione: una lamina con un foro può essere vista come lamina piena più una lamina "di massa negativa" della forma del foro, metodo molto comodo nella pratica ingegneristica per calcolare il baricentro di sezioni forate o profilati.

### Esercizio d'esempio

Una lamina quadrata omogenea di lato $a = 0{,}40\ \mathrm{m}$ e densità superficiale $\sigma = 5{,}0\ \mathrm{kg/m^2}$ ha un foro circolare di raggio $R = 0{,}10\ \mathrm{m}$ con centro a $d = 0{,}10\ \mathrm{m}$ a destra del centro del quadrato. Determinare la posizione del centro di massa.

**Soluzione.** Si pone l'origine nel centro del quadrato con asse $x$ verso il foro. La lamina piena ha massa $M_1 = \sigma a^2 = 5{,}0\cdot0{,}16 = 0{,}80\ \mathrm{kg}$ e CM in $x_1 = 0$. Il disco asportato ha massa $M_2 = \sigma\pi R^2 = 5{,}0\cdot\pi\cdot0{,}01 \approx 0{,}157\ \mathrm{kg}$ e CM in $x_2 = 0{,}10\ \mathrm{m}$. Per la proprietà distributiva, trattando il foro come massa negativa:

$$
x_{CM} = \frac{M_1x_1 - M_2x_2}{M_1 - M_2} = \frac{0 - 0{,}157\cdot0{,}10}{0{,}80 - 0{,}157}\ \mathrm{m} \approx -0{,}024\ \mathrm{m}.
$$

Per simmetria $y_{CM} = 0$. Il CM si trova quindi a circa $2{,}4\ \mathrm{cm}$ dal centro, dalla parte opposta al foro, e la massa della lamina forata è $M = 0{,}643\ \mathrm{kg}$.

### Punti chiave

- Il **centro di massa** è la media delle posizioni pesata con le masse: $\vec{r}_{CM} = \frac{1}{M}\sum m_i\vec{r}_i$; è un punto geometrico, non necessariamente materiale.
- Per simmetria materiale il CM giace sui piani, assi o centri di simmetria; vale la **proprietà distributiva** per sottosistemi.
- La quantità di moto totale vale $M\vec{v}_{CM}$; nel **riferimento del CM** è nulla.
- Il CM coincide con il **baricentro** se il campo gravitazionale è uniforme.
- La **densità** $\rho = \mathrm{d}m/\mathrm{d}V$ (e le analoghe $\sigma$, $\lambda$) presuppone l'ipotesi del continuo.
- Per corpi continui $\vec{r}_{CM} = \frac{1}{M}\int\vec{r}\,\mathrm{d}m$; i fori si trattano come masse negative.

## 8.2 Dinamica dei sistemi

Stabilito come descrivere globalmente la posizione e il moto di un sistema, si tratta ora di capire quali leggi ne governano l'evoluzione. La strategia è applicare la seconda legge di Newton a ciascun punto del sistema e poi sommare. In questa operazione è fondamentale distinguere tra **forze interne**, esercitate da un punto del sistema su un altro punto del sistema, e **forze esterne**, esercitate su punti del sistema da corpi che non ne fanno parte. La distinzione dipende dalla scelta del sistema: la forza gravitazionale tra Terra e Luna è interna se il sistema è "Terra + Luna", esterna se il sistema è la sola Luna. Il terzo principio della dinamica garantisce che le forze interne si presentano a coppie uguali e opposte e, nella sua forma forte, che sono dirette lungo la congiungente dei due punti. Grazie a ciò, nelle grandezze globali — quantità di moto e momento angolare totali — le forze interne scompaiono, e si ottengono le due **equazioni cardinali** della dinamica dei sistemi.

### 8.2.1 Quantità di moto

La **quantità di moto totale** di un sistema è la somma vettoriale delle quantità di moto dei singoli punti:

$$
\vec{P} = \sum_{i=1}^{N} m_i\vec{v}_i = M\vec{v}_{CM}.
$$

L'uguaglianza con $M\vec{v}_{CM}$, vista nella sezione precedente, stabilisce che la quantità di moto del sistema è quella che avrebbe un punto di massa pari alla massa totale concentrato nel centro di massa. Sul punto $i$-esimo agiscono la risultante delle forze esterne $\vec{F}_i^{(e)}$ e le forze interne $\vec{F}_{ij}$ esercitate dagli altri punti $j \neq i$. Per la seconda legge:

$$
\frac{\mathrm{d}\vec{p}_i}{\mathrm{d}t} = \vec{F}_i^{(e)} + \sum_{j\neq i}\vec{F}_{ij}.
$$

Sommando su tutti i punti, la doppia somma delle forze interne si annulla, perché per il terzo principio $\vec{F}_{ij} = -\vec{F}_{ji}$ e le forze compaiono a coppie che si elidono. Resta

$$
\frac{\mathrm{d}\vec{P}}{\mathrm{d}t} = \sum_i\vec{F}_i^{(e)} \equiv \vec{R}^{(e)},
$$

dove $\vec{R}^{(e)}$ è la **risultante delle forze esterne**. Utilizzando $\vec{P} = M\vec{v}_{CM}$ con $M$ costante si ha il **teorema del moto del centro di massa**:

$$
M\vec{a}_{CM} = \vec{R}^{(e)}.
$$

Il centro di massa si muove come un punto materiale di massa $M$ sul quale agisca la risultante di tutte le forze esterne. Questo teorema giustifica a posteriori l'uso del modello di punto materiale per corpi estesi: quando si studia la traiettoria di un proiettile, di un'automobile o di un pianeta trattandolo come un punto, si sta in realtà descrivendo il moto del suo centro di massa. L'esempio più spettacolare è quello di una granata che esplode in volo: i frammenti si disperdono in tutte le direzioni, ma, finché nessuno tocca terra e trascurando l'attrito dell'aria, il loro centro di massa continua a percorrere la stessa parabola che avrebbe seguito la granata intatta, perché le forze dell'esplosione sono interne.

Il teorema ha anche un corollario importante: **le forze interne non possono modificare il moto del centro di massa**. Una persona ferma su una superficie perfettamente liscia non può spostare il proprio CM, per quanto si agiti; può camminare solo grazie all'attrito con il suolo, che è una forza esterna. Un'automobile accelera grazie alla forza d'attrito statico che la strada esercita sulle ruote motrici, non grazie al motore in sé, le cui forze sono interne.

Se la risultante delle forze esterne è nulla, il sistema si dice **isolato** (o, più precisamente, non soggetto a forze esterne risultanti) e la quantità di moto totale si conserva: $\vec{P} = \text{costante}$, cioè il CM si muove di moto rettilineo uniforme. Questo è uno dei principi più importanti della fisica, valido anche quando le forze interne sono complicate, dissipative o sconosciute. Su di esso si basa la **propulsione a razzo**: espellendo gas all'indietro, il razzo acquista quantità di moto in avanti, senza bisogno di "spingere" contro alcunché. Lo stesso principio spiega il rinculo di un'arma da fuoco e il moto di una barca quando una persona cammina su di essa.

### 8.2.2 Momento angolare

Il **momento angolare totale** del sistema rispetto a un polo $O$ è la somma dei momenti angolari dei singoli punti:

$$
\vec{L}_O = \sum_i\vec{r}_i\times m_i\vec{v}_i,
$$

dove $\vec{r}_i$ è la posizione del punto $i$ rispetto a $O$. Analogamente il **momento risultante delle forze esterne** è $\vec{M}_O^{(e)} = \sum_i\vec{r}_i\times\vec{F}_i^{(e)}$.

Derivando il momento angolare rispetto al tempo, nel caso di polo fisso, si ottiene $\mathrm{d}\vec{L}_O/\mathrm{d}t = \sum_i\vec{r}_i\times(\vec{F}_i^{(e)} + \sum_{j}\vec{F}_{ij})$. Il contributo delle forze interne si annulla se vale il terzo principio nella **forma forte**: le forze $\vec{F}_{ij}$ e $\vec{F}_{ji}$ sono uguali e opposte *e dirette lungo la retta congiungente*. In tal caso la coppia formata dalle due forze ha braccio nullo e momento nullo: $\vec{r}_i\times\vec{F}_{ij} + \vec{r}_j\times\vec{F}_{ji} = (\vec{r}_i - \vec{r}_j)\times\vec{F}_{ij} = 0$, poiché $\vec{F}_{ij}$ è parallela a $\vec{r}_i - \vec{r}_j$. Questa condizione è soddisfatta dalle forze gravitazionali, elettrostatiche, elastiche e dalle forze di contatto ordinarie.

Se il polo è mobile con velocità $\vec{v}_O$, compare un termine aggiuntivo:

$$
\frac{\mathrm{d}\vec{L}_O}{\mathrm{d}t} = \vec{M}_O^{(e)} - \vec{v}_O\times M\vec{v}_{CM}.
$$

Il termine correttivo si annulla in tre casi: polo fisso ($\vec{v}_O = 0$), polo coincidente con il centro di massa ($\vec{v}_O = \vec{v}_{CM}$, prodotto vettoriale di un vettore con se stesso), polo con velocità parallela a quella del CM. La possibilità di usare il CM come polo, anche quando esso accelera, è uno dei risultati più utili della dinamica dei sistemi.

Un ulteriore risultato fondamentale è il **teorema di König per il momento angolare**: il momento angolare rispetto a un polo $O$ fisso si scompone come

$$
\vec{L}_O = \vec{r}_{CM}\times M\vec{v}_{CM} + \vec{L}'_{CM},
$$

dove il primo termine è il momento angolare "orbitale" del centro di massa, come se tutta la massa vi fosse concentrata, e il secondo, $\vec{L}'_{CM} = \sum\vec{r}_i'\times m_i\vec{v}_i'$, è il momento angolare "proprio" (o di **spin**) calcolato nel riferimento del CM. È la decomposizione che si usa naturalmente per la Terra, che ha un momento angolare orbitale dovuto alla rivoluzione attorno al Sole e uno proprio dovuto alla rotazione attorno al suo asse.

### 8.2.3 Equazioni cardinali

Le due relazioni ricavate costituiscono le **equazioni cardinali della dinamica dei sistemi**:

$$
\text{I:}\quad \frac{\mathrm{d}\vec{P}}{\mathrm{d}t} = \vec{R}^{(e)}, \qquad\qquad \text{II:}\quad \frac{\mathrm{d}\vec{L}_O}{\mathrm{d}t} = \vec{M}_O^{(e)},
$$

con $O$ fisso o coincidente con il CM. Si tratta di sei equazioni scalari che coinvolgono soltanto le forze esterne. Per un sistema generico non bastano a determinarne completamente il moto, perché i gradi di libertà sono $3N$; sono invece **sufficienti per il corpo rigido**, che ha esattamente sei gradi di libertà (tre di traslazione e tre di rotazione). Per questo motivo le equazioni cardinali sono la base di tutta la meccanica del corpo rigido e, in particolare, della statica delle strutture.

Nel caso statico, infatti, le equazioni cardinali forniscono le **condizioni necessarie di equilibrio**: un sistema in quiete deve avere risultante e momento risultante delle forze esterne nulli,

$$
\vec{R}^{(e)} = 0, \qquad \vec{M}_O^{(e)} = 0.
$$

Per un corpo rigido queste condizioni sono anche sufficienti, se il corpo è inizialmente in quiete. Quando la risultante è nulla, il momento risultante è indipendente dal polo, il che consente di scegliere il polo più comodo, ad esempio dove agiscono forze incognite. Queste condizioni si usano quotidianamente in ingegneria civile e meccanica per calcolare le reazioni vincolari di travi, ponti, gru e telai.

Dalle equazioni cardinali discendono le **leggi di conservazione** per i sistemi: se $\vec{R}^{(e)} = 0$ si conserva $\vec{P}$; se $\vec{M}_O^{(e)} = 0$ si conserva $\vec{L}_O$. Le due condizioni sono indipendenti: un sistema soggetto a una coppia di forze ha risultante nulla ma momento non nullo; un sistema soggetto a una forza centrale ha momento nullo rispetto al centro ma risultante non nulla. Un esempio della conservazione del momento angolare in un sistema è la piroetta del pattinatore: quando chiude le braccia riduce la distanza della massa dall'asse e, non essendovi momenti esterni rilevanti attorno all'asse verticale, la velocità angolare aumenta. Lo stesso accade al gatto che cade e riesce a girarsi, o al tuffatore che si raggruppa per compiere più rotazioni.

È importante sottolineare che le equazioni cardinali valgono in un riferimento **inerziale**; nel riferimento del CM, che in generale non è inerziale, la seconda equazione continua a valere scegliendo come polo il CM stesso, perché le forze apparenti di trascinamento, essendo proporzionali alle masse come la gravità uniforme, hanno momento nullo rispetto al centro di massa.

### Esercizio d'esempio

Un uomo di massa $m_1 = 75\ \mathrm{kg}$ si trova a un'estremità di una barca di massa $m_2 = 150\ \mathrm{kg}$ e lunghezza $L = 4{,}5\ \mathrm{m}$, inizialmente ferma in acqua calma. L'uomo cammina fino all'altra estremità. Trascurando l'attrito con l'acqua, di quanto si sposta la barca rispetto alla riva?

**Soluzione.** Le forze esterne orizzontali sono nulle e il sistema uomo + barca è inizialmente fermo: per la prima equazione cardinale il CM resta fermo in direzione orizzontale. Sia $\Delta x_2$ lo spostamento della barca rispetto alla riva; l'uomo si sposta rispetto alla barca di $L$ (verso positivo), quindi rispetto alla riva di $L + \Delta x_2$. La condizione $\Delta x_{CM} = 0$ dà

$$
m_1(L + \Delta x_2) + m_2\Delta x_2 = 0 \;\Rightarrow\; \Delta x_2 = -\frac{m_1 L}{m_1 + m_2} = -\frac{75\cdot4{,}5}{225}\ \mathrm{m} = -1{,}5\ \mathrm{m}.
$$

La barca arretra di $1{,}5\ \mathrm{m}$, mentre l'uomo avanza di $3{,}0\ \mathrm{m}$ rispetto alla riva. Il risultato non dipende da come l'uomo cammina (velocità, accelerazioni, soste), proprio perché sono in gioco solo forze interne.

### Punti chiave

- La **quantità di moto totale** è $\vec{P} = M\vec{v}_{CM}$; le forze interne si elidono per il terzo principio.
- **Teorema del moto del CM**: $M\vec{a}_{CM} = \vec{R}^{(e)}$; le forze interne non modificano il moto del CM.
- Il **momento angolare totale** soddisfa $\mathrm{d}\vec{L}_O/\mathrm{d}t = \vec{M}^{(e)}_O$ se il polo è fisso o coincide con il CM (terzo principio in forma forte).
- **Teorema di König**: $\vec{L}_O = \vec{r}_{CM}\times M\vec{v}_{CM} + \vec{L}'_{CM}$.
- Le **equazioni cardinali** sono sei equazioni scalari, sufficienti per il corpo rigido; in statica danno $\vec{R}^{(e)} = 0$, $\vec{M}^{(e)}_O = 0$.
- Se $\vec{R}^{(e)} = 0$ si conserva $\vec{P}$; se $\vec{M}^{(e)}_O = 0$ si conserva $\vec{L}_O$: condizioni indipendenti.

## 8.3 Relazioni integrali

Come per il punto materiale, anche per i sistemi le equazioni cardinali possono essere integrate nel tempo o nello spazio, ottenendo relazioni integrali che legano direttamente stato iniziale e finale. Le versioni per i sistemi presentano però differenze sostanziali rispetto al caso del singolo punto. Mentre nei teoremi dell'impulso e dell'impulso angolare compaiono soltanto le forze esterne, nel teorema dell'energia cinetica intervengono anche le forze interne: queste, pur avendo risultante e momento nulli, possono compiere lavoro, perché i punti su cui agiscono si spostano in generale in modo diverso. È proprio questo che rende possibile, ad esempio, che un'esplosione metta in moto dei frammenti inizialmente fermi, o che una persona salti spingendo con le gambe. Questa sezione sviluppa le relazioni integrali per i sistemi, introduce la decomposizione dell'energia in un contributo legato al moto del centro di massa e in uno "proprio", e discute il concetto di **energia interna**, che apre la strada alla termodinamica.

### 8.3.1 Impulso

Integrando nel tempo la prima equazione cardinale si ottiene il **teorema dell'impulso per i sistemi**:

$$
\vec{J}^{(e)} = \int_{t_i}^{t_f}\vec{R}^{(e)}\,\mathrm{d}t = \vec{P}_f - \vec{P}_i = M\left(\vec{v}_{CM,f} - \vec{v}_{CM,i}\right).
$$

L'impulso delle sole forze esterne determina la variazione della quantità di moto totale, cioè della velocità del centro di massa. Gli impulsi delle forze interne, uguali e opposti a coppie in ogni istante, si annullano esattamente anche dopo l'integrazione. Questa relazione è particolarmente utile negli urti e nelle esplosioni: durante l'intervallo brevissimo dell'interazione le forze interne sono enormi, mentre le forze esterne ordinarie (peso, attriti) danno impulsi trascurabili; di conseguenza la quantità di moto totale si conserva con ottima approssimazione anche se il sistema non è rigorosamente isolato. È l'**approssimazione impulsiva** applicata ai sistemi. Fanno eccezione le forze esterne a loro volta impulsive, come la reazione di un vincolo fisso contro cui il sistema urta: in quel caso la quantità di moto non si conserva, o si conserva solo nelle componenti perpendicolari alla reazione impulsiva.

### 8.3.2 Impulso angolare

Integrando la seconda equazione cardinale rispetto a un polo fisso, o coincidente con il CM, si ottiene il **teorema dell'impulso angolare per i sistemi**:

$$
\vec{H}_O^{(e)} = \int_{t_i}^{t_f}\vec{M}_O^{(e)}\,\mathrm{d}t = \vec{L}_{O,f} - \vec{L}_{O,i}.
$$

Anche qui compaiono solo i momenti delle forze esterne. Nei problemi d'urto con vincoli, il teorema dell'impulso angolare risulta spesso decisivo: se un corpo rigido è incernierato in un punto fisso $O$ e viene colpito, la reazione impulsiva della cerniera ha momento nullo rispetto a $O$, per cui il momento angolare rispetto alla cerniera si conserva durante l'urto, mentre la quantità di moto totale no. È il caso di un proiettile che si conficca in una porta o in un pendolo balistico rigido. La scelta del polo diventa qui una vera e propria tecnica risolutiva: il polo va messo dove agiscono le forze impulsive incognite.

### 8.3.3 Energia cinetica

L'**energia cinetica** di un sistema è la somma delle energie cinetiche dei suoi punti: $K = \sum_i\tfrac12 m_iv_i^2$. Applicando il teorema dell'energia cinetica a ciascun punto e sommando si ottiene

$$
W^{(e)} + W^{(i)} = \Delta K,
$$

dove $W^{(e)}$ è il lavoro delle forze esterne e $W^{(i)}$ quello delle forze interne. A differenza dei casi precedenti, il lavoro delle forze interne **non è in generale nullo**. Il lavoro di una coppia di forze interne $\vec{F}_{ij} = -\vec{F}_{ji}$ vale infatti $\mathrm{d}W = \vec{F}_{ij}\cdot\mathrm{d}(\vec{r}_i - \vec{r}_j)$: dipende dalla variazione della distanza relativa. Esso è nullo per un **corpo rigido**, in cui le distanze sono fisse, ma non per un sistema deformabile: una molla compressa che si distende tra due carrelli, i muscoli di un atleta, i gas di un'esplosione compiono lavoro interno positivo; gli attriti interni tra parti in moto relativo ne compiono uno negativo.

Un risultato fondamentale è il **teorema di König per l'energia cinetica**. Scrivendo $\vec{v}_i = \vec{v}_{CM} + \vec{v}_i'$ si ottiene

$$
K = \tfrac12 Mv_{CM}^2 + \sum_i\tfrac12 m_iv_i'^2 = K_{CM} + K',
$$

perché il termine misto $\vec{v}_{CM}\cdot\sum m_i\vec{v}_i'$ è nullo, essendo nulla la quantità di moto nel riferimento del CM. L'energia cinetica di un sistema è dunque la somma dell'energia cinetica del centro di massa (come se tutta la massa vi fosse concentrata) e dell'energia cinetica **relativa** al CM. Ad esempio, per una ruota che rotola, $K_{CM}$ è legata all'avanzamento e $K'$ alla rotazione attorno all'asse. Il termine $K'$ è il minimo valore che l'energia cinetica può assumere al variare del riferimento inerziale: nel riferimento del CM l'energia cinetica è minima. Questo ha conseguenze importanti negli urti, perché solo $K'$ può essere convertita in altre forme di energia senza violare la conservazione della quantità di moto.

### 8.3.4 Energia potenziale

Se le forze esterne sono conservative, il loro lavoro si esprime come $W^{(e)}_c = -\Delta U^{(e)}$, dove $U^{(e)}$ è la somma delle energie potenziali dei singoli punti nel campo esterno. Per la forza peso in un campo uniforme si ottiene un risultato molto semplice:

$$
U^{(e)} = \sum_i m_igz_i = Mgz_{CM},
$$

cioè l'energia potenziale gravitazionale di un sistema è quella di un punto di massa $M$ posto nel centro di massa. Per sollevare un corpo esteso, una scala o un'asta inizialmente distesa, il lavoro minimo necessario è $Mg\,\Delta z_{CM}$.

Anche le forze interne possono essere conservative, se dipendono solo dalle distanze relative e derivano da un potenziale. In questo caso si definisce un'**energia potenziale interna** $U^{(i)} = \sum_{i<j}U_{ij}(|\vec{r}_i - \vec{r}_j|)$, somma su tutte le coppie (contando ciascuna coppia una volta sola), tale che $W^{(i)}_c = -\Delta U^{(i)}$. Esempi sono l'energia elastica di una molla che collega due corpi, $\tfrac12 k(\ell - \ell_0)^2$, che dipende solo dall'allungamento e non dalla posizione assoluta, e l'energia gravitazionale mutua di due stelle, $-Gm_1m_2/r_{12}$.

### 8.3.5 Energia propria

Combinando i risultati precedenti, l'**energia meccanica** totale del sistema si può scrivere come $E = K + U^{(e)} + U^{(i)}$. Usando il teorema di König, si può separare un termine legato al moto del sistema "nel suo complesso" e un termine legato alla sua struttura e ai moti interni. Si definisce **energia propria** (o energia intrinseca) del sistema la somma dell'energia cinetica relativa al CM e dell'energia potenziale interna:

$$
E_{\text{propria}} = K' + U^{(i)}.
$$

Si tratta dell'energia che il sistema possiede nel riferimento del proprio centro di massa, indipendentemente dal suo moto d'insieme e dalla sua posizione in un campo esterno. L'energia totale si scrive allora $E = \tfrac12 Mv_{CM}^2 + U^{(e)} + E_{\text{propria}}$. Due sistemi identici, uno fermo e uno in moto rettilineo uniforme, hanno la stessa energia propria; ciò che li distingue è solo il termine $K_{CM}$. L'energia propria è una grandezza che caratterizza lo stato interno del sistema: per un atomo è l'energia degli elettroni legati al nucleo, per una molecola comprende vibrazioni e rotazioni, per una molla compressa tra due blocchi bloccati è l'energia elastica immagazzinata.

### 8.3.6 Energia interna

Per un corpo macroscopico, composto da un numero enorme di atomi e molecole, l'energia propria comprende l'energia cinetica dei moti microscopici disordinati delle particelle e l'energia potenziale delle loro interazioni reciproche. In questo contesto essa prende il nome di **energia interna**, indicata con $U_{\text{int}}$ (o semplicemente $U$ in termodinamica, da non confondere con l'energia potenziale). L'energia interna non è osservabile direttamente nel dettaglio microscopico, ma le sue variazioni sono misurabili macroscopicamente, ad esempio attraverso variazioni di temperatura o cambiamenti di stato.

Il concetto di energia interna risolve il problema apparente della "scomparsa" dell'energia meccanica in presenza di attrito. Quando un blocco scivola su un piano scabro e si ferma, la sua energia cinetica macroscopica non scompare: il lavoro negativo delle forze d'attrito, che sono forze interne al sistema blocco + piano, converte l'energia del moto ordinato del centro di massa in energia dei moti disordinati delle molecole del blocco e del piano, che si riscaldano. Allo stesso modo, in un urto anelastico l'energia cinetica relativa persa si trasforma in deformazioni permanenti, vibrazioni e riscaldamento, cioè in aumento dell'energia interna. Con la definizione di energia interna il bilancio energetico si scrive

$$
\Delta K_{CM} + \Delta U^{(e)} + \Delta U_{\text{int}} = W^{(e)}_{nc} + Q,
$$

dove $Q$ rappresenta lo scambio di energia sotto forma di calore con l'ambiente, concetto che sarà sviluppato in termodinamica. Questa è, in sostanza, una prima forma del **primo principio della termodinamica**.

### 8.3.7 Teoremi di conservazione

Le relazioni integrali portano alle leggi di conservazione per i sistemi, ciascuna con le sue ipotesi.

La **quantità di moto totale** si conserva se la risultante delle forze esterne è nulla (o, nell'approssimazione impulsiva, se le forze esterne non sono impulsive). Le forze interne, di qualunque natura, non la modificano.

Il **momento angolare totale** si conserva rispetto a un polo fisso o al CM se il momento risultante delle forze esterne rispetto a quel polo è nullo, assumendo forze interne centrali (terzo principio in forma forte).

L'**energia meccanica totale** $E = K + U^{(e)} + U^{(i)}$ si conserva se tutte le forze, sia esterne sia interne, che compiono lavoro sono conservative. È una condizione più restrittiva delle precedenti, perché coinvolge anche le forze interne: un sistema isolato conserva sempre $\vec{P}$ e $\vec{L}$, ma conserva l'energia meccanica solo se al suo interno non ci sono processi dissipativi.

L'**energia totale**, che include l'energia interna, si conserva invece sempre in un sistema isolato: è il principio di conservazione dell'energia nella sua forma più generale, che nessun esperimento ha mai smentito.

La differenza tra queste condizioni spiega perché in un urto tra due corpi si conservi sempre la quantità di moto ma non necessariamente l'energia cinetica: tema della prossima sezione.

### Esercizio d'esempio

Due carrelli di masse $m_1 = 2{,}0\ \mathrm{kg}$ e $m_2 = 3{,}0\ \mathrm{kg}$, fermi su un binario orizzontale liscio, sono tenuti uniti da un filo che mantiene compressa tra loro una molla ideale di costante $k = 1500\ \mathrm{N/m}$, accorciata di $x = 0{,}10\ \mathrm{m}$. Il filo viene tagliato. Calcolare le velocità finali dei carrelli e verificare il teorema di König.

**Soluzione.** Le forze esterne orizzontali sono nulle, per cui $\vec{P}$ si conserva ed è nulla: $m_1v_1 + m_2v_2 = 0$. La forza elastica è interna e conservativa, quindi si conserva l'energia meccanica: l'energia potenziale interna $U^{(i)} = \tfrac12 kx^2 = \tfrac12\cdot1500\cdot0{,}01 = 7{,}5\ \mathrm{J}$ si trasforma tutta in energia cinetica:

$$
\tfrac12 m_1v_1^2 + \tfrac12 m_2v_2^2 = 7{,}5\ \mathrm{J}.
$$

Da $v_1 = -\tfrac{3}{2}v_2$ si ha $\tfrac12\cdot2{,}0\cdot\tfrac94 v_2^2 + \tfrac12\cdot3{,}0\,v_2^2 = 3{,}75\,v_2^2 = 7{,}5$, quindi $v_2 = \sqrt{2{,}0} \approx 1{,}41\ \mathrm{m/s}$ e $v_1 \approx -2{,}12\ \mathrm{m/s}$. Il CM resta fermo, $K_{CM} = 0$, e tutta l'energia cinetica è relativa: $K = K' = 7{,}5\ \mathrm{J}$, in accordo con König. Le forze interne hanno compiuto un lavoro $W^{(i)} = 7{,}5\ \mathrm{J}$, pur avendo risultante nulla.

### Punti chiave

- **Impulso** e **impulso angolare** delle sole forze esterne determinano $\Delta\vec{P}$ e $\Delta\vec{L}_O$.
- Nel teorema dell'energia cinetica compare anche il **lavoro delle forze interne**, nullo solo per i corpi rigidi.
- **Teorema di König**: $K = \tfrac12 Mv_{CM}^2 + K'$; l'energia cinetica è minima nel riferimento del CM.
- In un campo gravitazionale uniforme $U^{(e)} = Mgz_{CM}$; le forze interne conservative definiscono $U^{(i)}$.
- L'**energia propria** $K' + U^{(i)}$ è l'energia del sistema nel riferimento del CM; per corpi macroscopici diventa **energia interna**.
- Un sistema isolato conserva sempre $\vec{P}$ e $\vec{L}$, ma l'energia meccanica solo in assenza di dissipazioni interne; l'energia totale si conserva sempre.

## 8.4 Urti

Un **urto** è un'interazione tra due o più corpi che avviene in un intervallo di tempo molto breve rispetto ai tempi caratteristici del moto, durante il quale si scambiano forze intense. Esempi sono la collisione tra palle da biliardo, l'impatto tra veicoli, il rimbalzo di una palla, lo scontro tra particelle subatomiche negli acceleratori, ma anche processi in cui i corpi non vengono a contatto, come la deviazione di una sonda spaziale che passa vicino a un pianeta (fionda gravitazionale). Lo studio degli urti si basa sulle leggi di conservazione: poiché le forze d'urto sono interne al sistema dei corpi che collidono e sono molto più intense delle forze esterne ordinarie, nell'**approssimazione impulsiva** la quantità di moto totale si conserva. Inoltre, poiché l'intervallo d'urto è brevissimo, le posizioni dei corpi non cambiano apprezzabilmente durante la collisione: si confrontano soltanto le velocità immediatamente prima e immediatamente dopo. La conservazione o meno dell'energia cinetica distingue le diverse tipologie di urto.

Si consideri, per fissare le idee, l'urto tra due corpi di masse $m_1$ e $m_2$, con velocità prima dell'urto $\vec{v}_1$ e $\vec{v}_2$ e dopo l'urto $\vec{v}_1'$ e $\vec{v}_2'$. La conservazione della quantità di moto fornisce

$$
m_1\vec{v}_1 + m_2\vec{v}_2 = m_1\vec{v}_1' + m_2\vec{v}_2',
$$

e quindi la velocità del centro di massa $\vec{v}_{CM}$ è la stessa prima e dopo l'urto. Le incognite sono le sei componenti delle velocità finali, mentre questa equazione fornisce tre relazioni: occorrono informazioni aggiuntive sul tipo di urto. Per il teorema di König, l'energia cinetica totale si scrive $K = \tfrac12 Mv_{CM}^2 + K'$; il primo termine non può cambiare durante l'urto, mentre il secondo, l'energia cinetica relativa al CM, può essere in parte o del tutto convertita in energia interna. Per due corpi, $K' = \tfrac12\mu v_{rel}^2$, dove $\mu = m_1m_2/(m_1 + m_2)$ è la **massa ridotta** e $v_{rel} = |\vec{v}_1 - \vec{v}_2|$ la velocità relativa. Si definisce **urto centrale** (o frontale) un urto in cui le velocità sono dirette lungo la retta che congiunge i centri dei corpi: il moto resta unidimensionale. Si definisce invece **obliquo** un urto in cui ciò non accade.

### 8.4.1 Urti elastici

Un urto si dice **elastico** se, oltre alla quantità di moto, si conserva anche l'energia cinetica totale:

$$
\tfrac12 m_1v_1^2 + \tfrac12 m_2v_2^2 = \tfrac12 m_1v_1'^2 + \tfrac12 m_2v_2'^2.
$$

Fisicamente ciò accade quando le forze d'interazione sono conservative e i corpi, dopo essersi deformati durante il contatto, tornano perfettamente alla forma originaria restituendo tutta l'energia elastica accumulata. Urti tra palle d'acciaio, tra palle da biliardo, gli urti tra molecole di un gas ideale, le collisioni tra particelle elementari che non cambiano stato interno sono, con buona approssimazione, elastici.

Nel caso di **urto elastico centrale** unidimensionale, combinando le due leggi di conservazione si ottiene un risultato molto utile. Riscrivendo le equazioni come $m_1(v_1 - v_1') = m_2(v_2' - v_2)$ e $m_1(v_1^2 - v_1'^2) = m_2(v_2'^2 - v_2^2)$ e dividendo membro a membro (escludendo la soluzione banale senza urto), si trova

$$
v_1 + v_1' = v_2 + v_2' \quad\Longleftrightarrow\quad v_1 - v_2 = -(v_1' - v_2').
$$

In un urto elastico centrale la **velocità relativa si inverte**: i corpi si allontanano dopo l'urto con la stessa velocità relativa con cui si avvicinavano. Risolvendo il sistema lineare si ricavano le velocità finali:

$$
v_1' = \frac{(m_1 - m_2)v_1 + 2m_2v_2}{m_1 + m_2}, \qquad v_2' = \frac{(m_2 - m_1)v_2 + 2m_1v_1}{m_1 + m_2}.
$$

Una forma più compatta ed elegante si ottiene nel riferimento del CM: $v_i' = 2v_{CM} - v_i$, cioè ogni velocità si "riflette" rispetto alla velocità del centro di massa.

Alcuni casi particolari, con il bersaglio inizialmente fermo ($v_2 = 0$), sono molto istruttivi. Se le **masse sono uguali**, $v_1' = 0$ e $v_2' = v_1$: i corpi si scambiano le velocità, come si osserva nel pendolo di Newton o nel biliardo, quando la palla battente si ferma e quella colpita parte. Se il **bersaglio è molto più pesante**, $m_2 \gg m_1$, $v_1' \approx -v_1$ e $v_2' \approx 0$: il proiettile rimbalza con velocità quasi invariata in modulo, come una pallina contro un muro. Se il **proiettile è molto più pesante**, $m_1 \gg m_2$, $v_1' \approx v_1$ e $v_2' \approx 2v_1$: il bersaglio leggero viene lanciato al doppio della velocità del proiettile. La frazione di energia cinetica trasferita al bersaglio vale $4m_1m_2/(m_1 + m_2)^2$, ed è massima (pari a 1) per masse uguali: è il principio dei **moderatori** nei reattori nucleari, che usano nuclei leggeri (idrogeno, deuterio, carbonio) per rallentare i neutroni.

Negli **urti elastici obliqui** in due dimensioni le equazioni di conservazione sono tre (due componenti della quantità di moto e l'energia) e le incognite quattro: serve un'informazione in più, ad esempio l'angolo di deviazione di uno dei corpi, che dipende dal parametro d'urto. Un risultato notevole: in un urto elastico tra masse uguali con bersaglio fermo, se l'urto non è centrale, le due velocità finali sono **perpendicolari** tra loro. Lo si ricava osservando che da $\vec{v}_1 = \vec{v}_1' + \vec{v}_2'$ e $v_1^2 = v_1'^2 + v_2'^2$ segue $\vec{v}_1'\cdot\vec{v}_2' = 0$, un fatto ben noto ai giocatori di biliardo.

### 8.4.2 Urti anelastici

Un urto si dice **anelastico** se l'energia cinetica totale non si conserva: parte dell'energia cinetica relativa al CM viene convertita in energia interna, sotto forma di deformazioni permanenti, calore, vibrazioni, suono, oppure, nel caso di particelle, in eccitazione dei livelli interni. La quantità di moto, invece, continua a conservarsi nell'approssimazione impulsiva.

Il caso limite è l'**urto completamente anelastico** (o perfettamente anelastico), in cui i corpi restano uniti dopo l'urto e procedono con la stessa velocità, che coincide necessariamente con quella del centro di massa:

$$
\vec{v}' = \frac{m_1\vec{v}_1 + m_2\vec{v}_2}{m_1 + m_2} = \vec{v}_{CM}.
$$

In questo caso l'energia cinetica relativa al CM viene interamente dissipata e l'energia cinetica persa è la massima compatibile con la conservazione della quantità di moto:

$$
\Delta K = -K' = -\tfrac12\mu\,v_{rel}^2 = -\frac12\frac{m_1m_2}{m_1 + m_2}|\vec{v}_1 - \vec{v}_2|^2.
$$

Esempi sono un proiettile che si conficca in un blocco di legno, due vagoni che si agganciano, una palla di argilla che si schiaccia contro un'altra, due automobili che restano incastrate dopo un tamponamento. Il **pendolo balistico** è lo strumento classico per misurare la velocità di un proiettile: questo si conficca in un blocco appeso a un filo, e dalla misura dell'altezza a cui risale il sistema si ricava la velocità comune subito dopo l'urto (conservazione dell'energia nella fase di risalita) e quindi la velocità del proiettile (conservazione della quantità di moto nella fase d'urto). È importante applicare ciascuna legge solo nella fase in cui vale: l'energia meccanica non si conserva durante l'urto, la quantità di moto non si conserva durante la risalita.

Gli urti intermedi tra quelli elastici e quelli completamente anelastici si caratterizzano mediante il **coefficiente di restituzione** $e$, definito per urti centrali come il rapporto tra la velocità relativa di allontanamento e quella di avvicinamento:

$$
e = -\frac{v_1' - v_2'}{v_1 - v_2}, \qquad 0 \le e \le 1.
$$

Si ha $e = 1$ per l'urto elastico, $e = 0$ per quello completamente anelastico. Il coefficiente di restituzione dipende dai materiali e, in misura minore, dalla velocità d'impatto. Si misura facilmente lasciando cadere una pallina da un'altezza $h$ su un piano rigido fisso e misurandone l'altezza di rimbalzo $h'$: poiché il piano è fermo, $e = v'/v = \sqrt{h'/h}$. Valori tipici: circa 0,9 per una palla da golf su superficie dura, circa 0,75 per una palla da tennis, quasi 0 per un pezzo di argilla. L'energia cinetica relativa persa vale $\Delta K = -(1 - e^2)K'$, formula che interpola tra i due casi limite.

Esistono anche urti **superelastici**, con $e > 1$, in cui l'energia cinetica aumenta perché viene liberata energia interna, come in una reazione esotermica o nell'esplosione di una carica posta tra due corpi. Formalmente un'esplosione è un "urto anelastico rovesciato nel tempo": un corpo inizialmente unico si divide in frammenti, la quantità di moto si conserva e l'energia cinetica aumenta a spese dell'energia interna.

### Esercizio d'esempio

Un proiettile di massa $m = 10\ \mathrm{g}$ si conficca in un pendolo balistico di massa $M = 2{,}0\ \mathrm{kg}$ sospeso a un filo. Il sistema risale di $h = 8{,}0\ \mathrm{cm}$. Calcolare la velocità del proiettile e la frazione di energia cinetica dissipata nell'urto.

**Soluzione.** *Fase di risalita* (energia meccanica conservata, tensione del filo senza lavoro):

$$
V = \sqrt{2gh} = \sqrt{2\cdot9{,}81\cdot0{,}080}\ \mathrm{m/s} \approx 1{,}25\ \mathrm{m/s}.
$$

*Fase d'urto* (completamente anelastico, quantità di moto orizzontale conservata):

$$
mv = (m + M)V \;\Rightarrow\; v = \frac{m + M}{m}V = \frac{2{,}010}{0{,}010}\cdot1{,}25\ \mathrm{m/s} \approx 2{,}5\times10^{2}\ \mathrm{m/s}.
$$

L'energia cinetica iniziale è $K_i = \tfrac12 mv^2 \approx \tfrac12\cdot0{,}010\cdot(251)^2 \approx 316\ \mathrm{J}$, quella subito dopo l'urto $K_f = \tfrac12(m + M)V^2 \approx 1{,}58\ \mathrm{J}$. La frazione conservata è $K_f/K_i = m/(m + M) \approx 0{,}005$: il $99{,}5\%$ dell'energia cinetica viene dissipato in deformazione e calore.

### Punti chiave

- Negli **urti** la quantità di moto totale si conserva (approssimazione impulsiva); $\vec{v}_{CM}$ è la stessa prima e dopo.
- Solo l'energia cinetica relativa al CM, $K' = \tfrac12\mu v_{rel}^2$, può essere dissipata.
- **Urto elastico**: si conserva anche $K$; nel caso centrale la velocità relativa si inverte e $v_i' = 2v_{CM} - v_i$.
- Masse uguali, bersaglio fermo: scambio delle velocità (centrale) o velocità finali perpendicolari (obliquo).
- **Urto completamente anelastico**: i corpi restano uniti con velocità $\vec{v}_{CM}$; si perde tutta $K'$.
- Il **coefficiente di restituzione** $e$ ($0\le e\le1$) caratterizza gli urti intermedi; $e = \sqrt{h'/h}$ per un rimbalzo su piano fisso.
- Nel pendolo balistico si applica la conservazione di $\vec{p}$ nell'urto e dell'energia nella risalita, separatamente.
