# Capitolo 10 — Meccanica dei solidi

Nei capitoli precedenti i corpi estesi sono stati trattati come sistemi di punti, spesso con l'ulteriore idealizzazione del **corpo rigido**, in cui le distanze reciproche tra le parti non cambiano mai. Nessun corpo reale, però, è perfettamente rigido: sotto l'azione di forze esterne ogni solido si deforma, sia pure di quantità spesso minuscole, e queste deformazioni sono essenziali per comprendere come le forze si trasmettono all'interno della materia. La progettazione di una trave, di un albero motore, di un cavo di funivia o di un componente di precisione richiede di sapere di quanto il materiale si deforma e quando smette di comportarsi in modo reversibile. In questo capitolo si affronta il passaggio dalla meccanica di pochi corpi a quella dei **sistemi numerosi**, composti da un numero enorme di atomi, discutendo l'approccio statistico e la classificazione degli stati di aggregazione della materia. Si studiano poi le **proprietà elastiche** dei solidi — trazione, compressione, compressione idrostatica, taglio, contrazione laterale — introducendo i moduli elastici che caratterizzano i materiali e mostrando come essi trovino una spiegazione in un semplice **modello atomico**.

## 10.1 Meccanica dei sistemi numerosi

La meccanica dei sistemi, sviluppata nel capitolo 8, fornisce strumenti generali — centro di massa, equazioni cardinali, teoremi di conservazione — validi per sistemi composti da un numero qualsiasi di punti. Quando però il numero di costituenti diventa enorme, come avviene per qualsiasi porzione macroscopica di materia, cambia radicalmente il modo in cui conviene affrontare il problema. Un centimetro cubo di ferro contiene circa $8\times10^{22}$ atomi; una mole di qualunque sostanza ne contiene $N_A \approx 6{,}022\times10^{23}$ (**numero di Avogadro**). Scrivere e risolvere le equazioni del moto di ciascun atomo è impossibile, e anche se lo fosse produrrebbe una quantità di informazione inutilizzabile. Ciò che interessa sono le proprietà **macroscopiche**: forma, volume, densità, temperatura, pressione, rigidezza. La sezione illustra l'approccio con cui la fisica passa dalla descrizione microscopica a quella macroscopica e come, su questa base, si classificano gli stati della materia.

### 10.1.1 Approccio statistico

Di fronte a un sistema composto da un numero enorme di particelle si possono seguire due strade complementari. La prima è l'approccio **macroscopico** (o fenomenologico): si rinuncia a descrivere i costituenti e si caratterizza il sistema mediante poche grandezze misurabili su scala umana, come volume, pressione, temperatura, sforzo, deformazione, collegate da relazioni empiriche (leggi costitutive) ricavate dall'esperimento. È l'approccio della termodinamica classica, della meccanica dei fluidi e della teoria dell'elasticità. La seconda strada è l'approccio **microscopico** (o statistico): si parte da un modello dei costituenti e delle loro interazioni e si ricavano le grandezze macroscopiche come **valori medi** su un numero enorme di particelle. È l'approccio della **meccanica statistica**, che sarà ripreso nei capitoli dedicati ai gas e alla termodinamica.

Il punto chiave dell'approccio statistico è che, proprio perché il numero di particelle è enorme, le fluttuazioni delle grandezze medie sono piccolissime. Se una grandezza è la somma di $N$ contributi indipendenti, le sue fluttuazioni relative scalano come $1/\sqrt{N}$: per $N \sim 10^{23}$ si ha $1/\sqrt{N} \sim 3\times10^{-12}$, del tutto trascurabile. È per questo che la pressione di un gas in un recipiente, pur essendo il risultato di innumerevoli urti molecolari caotici, è perfettamente stabile e riproducibile; ed è per questo che le leggi macroscopiche, pur derivando da un comportamento microscopico disordinato, sono **deterministiche** a tutti gli effetti pratici. In un certo senso, la complessità del mondo microscopico produce semplicità a livello macroscopico.

Un concetto essenziale è quello di **stato**. Lo **stato microscopico** (microstato) di un sistema è specificato da posizioni e velocità di tutte le particelle; lo **stato macroscopico** (macrostato) da poche grandezze globali. A un medesimo macrostato corrispondono moltissimi microstati diversi: gli atomi di un blocco di metallo a una data temperatura possono essere distribuiti in innumerevoli configurazioni vibrazionali compatibili con la stessa energia totale. Le grandezze macroscopiche sono medie sui microstati compatibili, e il sistema evolve spontaneamente verso i macrostati che corrispondono al maggior numero di microstati, che risultano di gran lunga i più probabili. Questo ragionamento è alla base del concetto di **equilibrio termodinamico** e, più avanti, di entropia.

Per legare le scale microscopica e macroscopica è utile l'**ipotesi del continuo**, già introdotta parlando di densità: si considera un volumetto abbastanza piccolo da poter essere trattato come un punto rispetto alle dimensioni del corpo, ma abbastanza grande da contenere moltissimi atomi. In un cubetto di lato $1\ \mu\mathrm{m}$ di un solido vi sono ancora circa $10^{11}$ atomi, sufficienti per definire con precisione medie locali. Su questa base si definiscono grandezze di campo come la densità $\rho(\vec{r})$, lo sforzo e la deformazione in ogni punto, che variano con continuità nel materiale. L'ipotesi del continuo cade quando le dimensioni in gioco si avvicinano alle distanze interatomiche (frazioni di nanometro), come nelle nanotecnologie, oppure nei gas molto rarefatti, in cui il cammino libero medio delle molecole diventa paragonabile alle dimensioni del recipiente.

Un aspetto fondamentale dell'approccio statistico è il ruolo dell'**energia interna**, introdotta nel capitolo precedente. In un corpo macroscopico fermo, i costituenti non sono immobili: vibrano, ruotano, traslano in modo disordinato. L'energia associata a questi moti è legata alla **temperatura**, che risulta proporzionale all'energia cinetica media per grado di libertà delle particelle. La comprensione dei sistemi numerosi richiede quindi di affiancare alle grandezze meccaniche anche grandezze termiche, ponte verso la termologia e la termodinamica.

### 10.1.2 Stati della materia

La materia ordinaria si presenta in diversi **stati di aggregazione**, tradizionalmente tre: **solido**, **liquido** e **aeriforme** (gas o vapore). A essi si aggiunge il **plasma**, gas ionizzato ad alta temperatura che costituisce la gran parte della materia visibile dell'universo (stelle, nebulose), e una varietà di stati intermedi o esotici (cristalli liquidi, superfluidi, condensati di Bose-Einstein). La distinzione tra gli stati si fonda, dal punto di vista macroscopico, sul comportamento rispetto a forma e volume; dal punto di vista microscopico, sul rapporto tra l'**energia di legame** tra le particelle e la loro **energia di agitazione termica**, dell'ordine di $k_BT$ dove $k_B \approx 1{,}38\times10^{-23}\ \mathrm{J/K}$ è la costante di Boltzmann.

Un **solido** ha forma e volume propri. Le particelle sono legate da forze intense e occupano posizioni di equilibrio fisse attorno alle quali compiono piccole oscillazioni termiche; l'energia di legame è molto maggiore di $k_BT$. Se le posizioni di equilibrio sono disposte in modo regolare e periodico su grande scala, formando un **reticolo cristallino**, il solido è **cristallino** (metalli, sali, ghiaccio, quarzo); se l'ordine è solo a corto raggio, il solido è **amorfo** (vetri, molti polimeri). I solidi resistono sia a variazioni di volume sia a variazioni di forma: sopportano sforzi di trazione, compressione e taglio. Le distanze interatomiche tipiche sono dell'ordine di $0{,}1$–$0{,}3\ \mathrm{nm}$.

Un **liquido** ha volume proprio ma non forma propria: assume la forma del recipiente che lo contiene. Le particelle sono ancora molto vicine, a distanze simili a quelle del solido, per cui i liquidi sono poco comprimibili e hanno densità simili a quelle dei solidi corrispondenti; tuttavia l'energia di agitazione termica è sufficiente a far sì che le particelle cambino continuamente le proprie vicine, scorrendo le une sulle altre. Il liquido possiede ordine a corto raggio ma non a lungo raggio. Macroscopicamente, un liquido in quiete **non sopporta sforzi di taglio**: anche il più piccolo sforzo tangenziale ne provoca lo scorrimento, cioè il flusso. Questa è la definizione operativa di **fluido**.

Un **aeriforme** non ha né forma né volume propri: tende a occupare tutto il volume disponibile. Le particelle sono in media molto distanti (in un gas a condizioni normali la distanza media è circa dieci volte il diametro molecolare) e interagiscono quasi esclusivamente durante brevi urti; l'energia di agitazione termica domina nettamente su quella di legame. I gas sono molto comprimibili e hanno densità circa mille volte inferiori a quelle di liquidi e solidi. Liquidi e gas insieme costituiscono i **fluidi**. Si parla di **vapore** quando l'aeriforme si trova a temperatura inferiore a quella critica e può quindi essere liquefatto per sola compressione.

I passaggi da uno stato all'altro sono le **transizioni di fase**: fusione e solidificazione, vaporizzazione e condensazione, sublimazione e brinamento. Avvengono, a pressione fissata, a temperature ben definite e richiedono lo scambio di una quantità di energia, il **calore latente**, necessaria a modificare l'energia di legame tra le particelle senza variare la temperatura. Queste trasformazioni saranno studiate in dettaglio in termologia.

Va infine sottolineato che la classificazione in stati non è sempre netta. Il vetro, ad esempio, è un solido amorfo che su tempi lunghissimi può mostrare un lento scorrimento; materiali come la pece, il bitume o l'impasto di farina si comportano da solidi sotto sollecitazioni rapide e da liquidi sotto sollecitazioni lente (materiali **viscoelastici**). La distinzione dipende dunque anche dalla scala temporale dell'osservazione rispetto ai tempi di riassestamento microscopico del materiale. Ai fini di questo capitolo interessa il comportamento dei solidi, e in particolare la loro risposta elastica alle sollecitazioni meccaniche.

### Esercizio d'esempio

Il ferro ha densità $\rho = 7870\ \mathrm{kg/m^3}$ e massa molare $M_m = 55{,}8\times10^{-3}\ \mathrm{kg/mol}$. Stimare il numero di atomi in un cubetto di lato $\ell = 1{,}0\ \mathrm{cm}$, la distanza media tra atomi vicini e l'ordine di grandezza delle fluttuazioni relative di una grandezza additiva su questo campione.

**Soluzione.** La massa del cubetto è $m = \rho\ell^3 = 7870\cdot10^{-6}\ \mathrm{kg} = 7{,}87\times10^{-3}\ \mathrm{kg}$. Il numero di moli è $n = m/M_m \approx 0{,}141\ \mathrm{mol}$, quindi il numero di atomi è

$$
N = nN_A \approx 0{,}141\cdot6{,}022\times10^{23} \approx 8{,}5\times10^{22}.
$$

Il volume medio per atomo è $V/N = 10^{-6}/8{,}5\times10^{22} \approx 1{,}18\times10^{-29}\ \mathrm{m^3}$; la distanza media è la radice cubica:

$$
d \approx \left(1{,}18\times10^{-29}\right)^{1/3}\ \mathrm{m} \approx 2{,}3\times10^{-10}\ \mathrm{m} = 0{,}23\ \mathrm{nm},
$$

in accordo con l'ordine di grandezza delle distanze interatomiche nei solidi. Le fluttuazioni relative sono dell'ordine di

$$
\frac{1}{\sqrt{N}} \approx \frac{1}{\sqrt{8{,}5\times10^{22}}} \approx 3{,}4\times10^{-12},
$$

assolutamente inosservabili: le grandezze macroscopiche sono di fatto deterministiche.

### Punti chiave

- I corpi macroscopici contengono un numero enorme di costituenti ($N_A \approx 6{,}022\times10^{23}\ \mathrm{mol^{-1}}$): la descrizione punto per punto è impossibile e inutile.
- L'approccio **macroscopico** usa poche grandezze misurabili e leggi costitutive; quello **statistico** ricava le grandezze macroscopiche come medie su moltissime particelle.
- Le fluttuazioni relative scalano come $1/\sqrt{N}$: per sistemi macroscopici le leggi sono di fatto deterministiche.
- A un **macrostato** corrispondono moltissimi **microstati**; l'equilibrio corrisponde al macrostato più probabile.
- **Solidi**: forma e volume propri, sopportano sforzi di taglio; **liquidi**: volume proprio, forma del recipiente; **aeriformi**: né forma né volume propri.
- Lo stato dipende dal rapporto tra energia di legame ed energia termica $\sim k_BT$; i **fluidi** non sopportano sforzi di taglio in quiete.

## 10.2 Proprietà elastiche

Quando un solido è sottoposto a forze esterne si deforma: si allunga, si accorcia, si piega, si torce, cambia volume. Se, rimosse le forze, il corpo ritorna esattamente alla sua forma e dimensione originaria, il comportamento si dice **elastico**; se invece resta una deformazione permanente si parla di comportamento **plastico**. Per sollecitazioni sufficientemente piccole tutti i solidi si comportano in modo elastico e, in più, **lineare**: la deformazione è proporzionale alla sollecitazione. È la **legge di Hooke**, formulata da Robert Hooke nel XVII secolo con il celebre anagramma *ut tensio, sic vis* ("come l'allungamento, così la forza"). Per descrivere il comportamento elastico in modo indipendente dalle dimensioni del campione si introducono due grandezze: lo **sforzo** (o tensione), forza per unità di superficie, e la **deformazione**, variazione relativa di una dimensione. Il rapporto tra sforzo e deformazione è un **modulo elastico**, proprietà caratteristica del materiale. Per un solido isotropo esistono diversi tipi di sollecitazione, ciascuno con il proprio modulo; si mostrerà però che solo due moduli sono indipendenti.

### 10.2.1 Trazione

Si consideri una sbarra di lunghezza iniziale $L_0$ e sezione trasversale di area $S$, fissata a un estremo e tirata all'altro estremo da una forza $F$ diretta lungo l'asse (sollecitazione di **trazione**). Si definisce **sforzo normale** (o tensione normale) il rapporto

$$
\sigma = \frac{F}{S},
$$

che si misura in pascal ($1\ \mathrm{Pa} = 1\ \mathrm{N/m^2}$); nella pratica ingegneristica si usano spesso il megapascal ($\mathrm{MPa} = \mathrm{N/mm^2}$) e il gigapascal. Si definisce **deformazione longitudinale** (o allungamento relativo) il rapporto adimensionale

$$
\varepsilon = \frac{\Delta L}{L_0}.
$$

Lo sforzo non dipende dalle dimensioni del campione, ma solo da come la forza si distribuisce sulla sezione: una sbarra di sezione doppia, sottoposta alla stessa forza, è sollecitata la metà. Analogamente la deformazione è un rapporto: a parità di sforzo, una sbarra lunga il doppio si allunga il doppio, ma la deformazione relativa è la stessa.

Per sforzi sufficientemente piccoli vale la **legge di Hooke**:

$$
\sigma = E\,\varepsilon \quad\Longleftrightarrow\quad \frac{F}{S} = E\frac{\Delta L}{L_0},
$$

dove $E$ è il **modulo di Young** (o modulo di elasticità longitudinale), caratteristico del materiale, misurato in pascal. Valori tipici: acciaio circa $200\ \mathrm{GPa}$, alluminio $70\ \mathrm{GPa}$, rame $120\ \mathrm{GPa}$, vetro $70\ \mathrm{GPa}$, calcestruzzo $30\ \mathrm{GPa}$, legno (lungo le fibre) $10\ \mathrm{GPa}$, gomma circa $0{,}01$–$0{,}1\ \mathrm{GPa}$. I valori elevati spiegano perché le deformazioni dei metalli in condizioni ordinarie siano dell'ordine dello $0{,}1\%$ o meno.

Riscrivendo la legge di Hooke come $F = (ES/L_0)\Delta L$ si riconosce la forza elastica di una molla, con **costante elastica** equivalente $k = ES/L_0$. La rigidezza di una sbarra cresce quindi con la sezione e diminuisce con la lunghezza: una sbarra lunga è più "cedevole". L'**energia elastica** immagazzinata è $U = \tfrac12 k\Delta L^2$, e per unità di volume vale $u = \tfrac12\sigma\varepsilon = \tfrac12 E\varepsilon^2$.

Il comportamento completo di un materiale sotto trazione si studia con la **prova di trazione**, che registra la **curva sforzo-deformazione**. Il primo tratto è lineare (regime di Hooke) fino al **limite di proporzionalità**; segue un breve tratto ancora elastico ma non lineare fino al **limite di elasticità**; oltre questo valore il materiale entra in **regime plastico**: le deformazioni diventano permanenti e crescono rapidamente con lo sforzo (snervamento). Lo sforzo massimo sopportabile è il **carico di rottura**, oltre il quale il provino si strizza localmente e si spezza. Materiali **duttili** (acciaio dolce, rame, alluminio) presentano un ampio campo plastico prima della rottura e avvisano del cedimento deformandosi; materiali **fragili** (vetro, ghisa, ceramica) si rompono quasi senza deformazione plastica. Nella progettazione si impone che gli sforzi in esercizio restino ben al di sotto del limite elastico, introducendo un **coefficiente di sicurezza**.

### 10.2.2 Compressione

La sollecitazione di **compressione** è l'opposto della trazione: forze dirette lungo l'asse della sbarra ma verso l'interno, che tendono ad accorciarla. Formalmente si descrive con le stesse grandezze, con sforzo e deformazione negativi: $\sigma = -F/S$, $\varepsilon = \Delta L/L_0 < 0$, e in regime elastico vale ancora $\sigma = E\varepsilon$, con lo stesso modulo di Young della trazione per la maggior parte dei materiali omogenei e isotropi.

Il comportamento oltre il campo elastico può però essere molto diverso. Molti materiali fragili, come calcestruzzo, pietra, ghisa, mattoni, resistono molto meglio a compressione che a trazione: il calcestruzzo ha una resistenza a compressione dell'ordine di $30\ \mathrm{MPa}$ ma a trazione solo di $2$–$3\ \mathrm{MPa}$. Per questo nelle strutture in cemento armato le zone tese sono affidate a barre d'acciaio, mentre il calcestruzzo lavora a compressione; e per questo le grandi costruzioni in muratura del passato, come archi e cupole, sono state concepite per lavorare quasi esclusivamente a compressione.

Un fenomeno tipico degli elementi snelli compressi è l'**instabilità a carico di punta** (*buckling*): una colonna lunga e sottile, compressa assialmente, oltre un certo **carico critico** si inflette lateralmente e collassa anche se lo sforzo è ben inferiore al limite di resistenza del materiale. Il carico critico, secondo la teoria di Euler, è proporzionale al modulo di Young e al momento d'inerzia della sezione e inversamente proporzionale al quadrato della lunghezza libera di inflessione. È per questo che pilastri e aste compresse non possono essere troppo snelli. Si tratta di un esempio di come, in un sistema elastico, la posizione di equilibrio possa passare da stabile a instabile al variare di un parametro, in analogia con quanto visto per la statica del punto.

### 10.2.3 Compressione idrostatica

Se un corpo viene immerso in un fluido e sottoposto a una pressione $p$ uniforme su tutta la superficie, esso è sollecitato in modo uguale in tutte le direzioni: si parla di **compressione idrostatica** (o volumetrica). In un solido isotropo questa sollecitazione non cambia la forma del corpo ma solo il suo volume. La deformazione rilevante è la **deformazione volumetrica** $\Delta V/V_0$, e in regime elastico vale

$$
\Delta p = -B\frac{\Delta V}{V_0},
$$

dove $B$ è il **modulo di compressibilità** (o modulo di bulk), misurato in pascal; il segno meno indica che un aumento di pressione provoca una diminuzione di volume. L'inverso $\kappa = 1/B$ si chiama **compressibilità**. Valori tipici: acciaio circa $160\ \mathrm{GPa}$, alluminio $76\ \mathrm{GPa}$, acqua $2{,}2\ \mathrm{GPa}$, aria (a temperatura costante, a pressione atmosferica) circa $10^{-4}\ \mathrm{GPa}$.

Il modulo di compressibilità, a differenza del modulo di Young e del modulo di taglio, è definito anche per i liquidi e per i gas, che pur non avendo forma propria resistono alle variazioni di volume. Il valore elevato di $B$ per l'acqua (una pressione di $10\ \mathrm{MPa}$, quella che si trova a $1000\ \mathrm{m}$ di profondità nel mare, riduce il volume dell'acqua di appena lo $0{,}45\%$) giustifica l'approssimazione di **fluido incomprimibile** usata in idrostatica e idrodinamica. Il modulo di compressibilità determina inoltre la velocità del suono nei mezzi, $v = \sqrt{B/\rho}$ nei fluidi, come si vedrà nello studio delle onde.

Per un solido isotropo si può ricavare $B$ dal modulo di Young e dal coefficiente di Poisson (definito più avanti), considerando che la compressione idrostatica equivale alla sovrapposizione di tre compressioni uguali lungo tre assi ortogonali:

$$
B = \frac{E}{3(1 - 2\nu)}.
$$

### 10.2.4 Taglio

Una sollecitazione di **taglio** si ha quando le forze agiscono parallelamente alla superficie su cui sono applicate. Si immagini un blocco a forma di parallelepipedo con la base inferiore fissata e una forza $F$ tangente applicata sulla faccia superiore di area $S$: gli strati del blocco tendono a scorrere l'uno sull'altro e il parallelepipedo si deforma in un prisma obliquo, senza variazione di volume. Si definisce **sforzo di taglio** (o tensione tangenziale)

$$
\tau = \frac{F}{S},
$$

e **deformazione di taglio** l'angolo $\gamma$ di cui ruotano i lati verticali, che per piccole deformazioni è $\gamma \approx \tan\gamma = \Delta x/h$, dove $\Delta x$ è lo spostamento della faccia superiore e $h$ l'altezza del blocco. In regime elastico

$$
\tau = G\gamma,
$$

dove $G$ è il **modulo di taglio** (o modulo di elasticità tangenziale, o modulo di rigidità). Valori tipici: acciaio circa $80\ \mathrm{GPa}$, alluminio $26\ \mathrm{GPa}$, rame $45\ \mathrm{GPa}$. Per un solido isotropo vale la relazione

$$
G = \frac{E}{2(1 + \nu)},
$$

per cui il modulo di taglio è sempre minore di quello di Young, tipicamente circa il 40% di esso.

Il modulo di taglio è nullo per i fluidi in quiete: è proprio questa la proprietà che li distingue dai solidi. Sollecitazioni di taglio sono presenti in moltissime applicazioni: nei bulloni e nei rivetti che collegano lamiere sovrapposte, nelle travi inflesse in prossimità degli appoggi, negli alberi di trasmissione soggetti a **torsione**. La torsione di un filo o di un albero cilindrico è infatti un taglio distribuito: il momento torcente necessario per ruotare di un angolo $\phi$ un filo di raggio $R$ e lunghezza $L$ è $M = \frac{\pi G R^4}{2L}\phi$. La forte dipendenza da $R^4$ spiega perché fili sottilissimi abbiano costanti di torsione piccolissime, il che rende possibili strumenti sensibilissimi come la bilancia di torsione di Cavendish, e perché gli alberi cavi siano quasi altrettanto rigidi di quelli pieni pur essendo molto più leggeri.

### 10.2.5 Legge di Poisson

Quando una sbarra viene tirata, non solo si allunga ma contemporaneamente si assottiglia: le sue dimensioni trasversali diminuiscono. Viceversa, quando è compressa si allarga. Questo effetto è descritto dalla **legge di Poisson**: in regime elastico la deformazione trasversale $\varepsilon_\perp = \Delta d/d_0$ è proporzionale a quella longitudinale e di segno opposto,

$$
\varepsilon_\perp = -\nu\,\varepsilon,
$$

dove $\nu$ è il **coefficiente di Poisson**, adimensionale e caratteristico del materiale. Valori tipici: acciaio circa $0{,}29$, alluminio $0{,}33$, rame $0{,}34$, vetro $0{,}22$, calcestruzzo $0{,}2$, sughero circa $0$, gomma prossimo a $0{,}5$.

La variazione relativa di volume di una sbarra sottoposta a trazione semplice è, al primo ordine, la somma delle tre deformazioni lineari:

$$
\frac{\Delta V}{V_0} = \varepsilon + 2\varepsilon_\perp = (1 - 2\nu)\,\varepsilon.
$$

Poiché un materiale stabile non può aumentare di volume sotto compressione idrostatica, deve essere $B > 0$ e quindi $\nu \le 0{,}5$. Il valore limite $\nu = 0{,}5$ corrisponde a un materiale **incomprimibile**, il cui volume resta costante: la gomma vi si avvicina molto, ed è per questo che un tappo di gomma, compresso, si allarga vistosamente. Il sughero, con $\nu \approx 0$, non si allarga quando viene compresso, motivo per cui è ideale per tappare le bottiglie: lo si infila facilmente nel collo. In linea di principio $\nu$ può anche essere negativo: esistono materiali artificiali, detti **auxetici**, che si allargano quando vengono tirati, grazie a particolari microstrutture.

Il coefficiente di Poisson completa la descrizione elastica di un solido isotropo: dei quattro parametri $E$, $G$, $B$, $\nu$ soltanto due sono indipendenti, e gli altri si ricavano tramite le relazioni $G = E/[2(1 + \nu)]$ e $B = E/[3(1 - 2\nu)]$. Per materiali anisotropi, come i cristalli singoli, il legno o i compositi a fibre, servono invece più costanti elastiche (fino a 21 nel caso più generale).

### 10.2.6 Modello atomico

Le proprietà elastiche macroscopiche trovano una spiegazione naturale nella struttura microscopica dei solidi. Due atomi vicini in un solido interagiscono con una forza che è **repulsiva** a piccole distanze (per la sovrapposizione delle nubi elettroniche e il principio di Pauli) e **attrattiva** a distanze maggiori (per i legami ionici, covalenti, metallici o di van der Waals). L'energia potenziale di interazione $U(r)$ in funzione della distanza ha quindi la forma caratteristica di una buca: cresce rapidamente per $r \to 0$, presenta un minimo alla distanza di equilibrio $r_0$ e tende a zero per $r \to \infty$. Un modello molto usato è il **potenziale di Lennard-Jones**,

$$
U(r) = 4\epsilon\left[\left(\frac{\sigma_0}{r}\right)^{12} - \left(\frac{\sigma_0}{r}\right)^{6}\right],
$$

con minimo in $r_0 = 2^{1/6}\sigma_0$ e profondità $\epsilon$, l'energia di legame.

Come visto nella statica del punto, attorno al minimo l'energia potenziale si approssima con una parabola, $U(r) \approx U(r_0) + \tfrac12 k(r - r_0)^2$ con $k = U''(r_0)$: per piccoli spostamenti dalla posizione di equilibrio la forza tra gli atomi è **elastica**, cioè proporzionale allo spostamento. Il solido può quindi essere modellizzato come un reticolo di masse (gli atomi) collegate da molle (i legami). È questo il fondamento microscopico della legge di Hooke: la linearità macroscopica tra sforzo e deformazione riflette la forma parabolica del fondo della buca di potenziale interatomica.

Il modello permette di stimare il modulo di Young. Si consideri un reticolo cubico semplice con passo $r_0$. Una sezione di area $S$ è attraversata da $S/r_0^2$ catene di atomi, ciascuna formata da $L_0/r_0$ molle di costante $k$ in serie. Una forza $F$ si ripartisce sulle catene, ciascuna con forza $F r_0^2/S$, e ogni legame si allunga di $\Delta r = Fr_0^2/(Sk)$; l'allungamento totale è $\Delta L = (L_0/r_0)\Delta r$. Ne segue

$$
\frac{F}{S} = \frac{k}{r_0}\frac{\Delta L}{L_0} \quad\Longrightarrow\quad E \approx \frac{k}{r_0}.
$$

Con valori tipici $k \sim 10$–$100\ \mathrm{N/m}$ e $r_0 \sim 0{,}25\ \mathrm{nm}$ si ottiene $E \sim 40$–$400\ \mathrm{GPa}$, proprio l'ordine di grandezza misurato per i metalli. Il modulo elastico è quindi legato alla **curvatura** della buca di potenziale: legami più forti e più "rigidi" producono materiali più rigidi.

Il modello spiega anche i limiti della legge di Hooke. Per deformazioni grandi la buca di potenziale non è più parabolica, ma **asimmetrica**: più ripida dal lato della compressione e più dolce dal lato della trazione. La relazione sforzo-deformazione diventa non lineare, e la forza massima di richiamo, corrispondente al punto di flesso di $U(r)$, fornisce una stima teorica del carico di rottura, che risulta però molto più alta (dell'ordine di $E/10$) dei valori misurati. La discrepanza si spiega con la presenza nei solidi reali di **difetti** — dislocazioni, vacanze, microfratture — che concentrano gli sforzi e permettono lo scorrimento dei piani atomici a sforzi molto minori: la plasticità dei metalli è dovuta al moto delle dislocazioni. L'asimmetria della buca spiega inoltre la **dilatazione termica**: all'aumentare della temperatura gli atomi oscillano con ampiezza maggiore e, poiché la buca è più dolce dal lato delle grandi distanze, la distanza media cresce, e il solido si dilata.

### Esercizio d'esempio

Un cavo d'acciaio ($E = 200\ \mathrm{GPa}$, $\nu = 0{,}29$, carico di snervamento $\sigma_s = 250\ \mathrm{MPa}$) lungo $L_0 = 10\ \mathrm{m}$ e di diametro $d = 8{,}0\ \mathrm{mm}$ sostiene una massa di $m = 800\ \mathrm{kg}$. Calcolare lo sforzo, il coefficiente di sicurezza rispetto allo snervamento, l'allungamento, la contrazione del diametro e l'energia elastica immagazzinata.

**Soluzione.** La sezione è $S = \pi d^2/4 = \pi\cdot(8{,}0\times10^{-3})^2/4 \approx 5{,}03\times10^{-5}\ \mathrm{m^2}$ e la forza $F = mg = 800\cdot9{,}81 \approx 7{,}85\times10^{3}\ \mathrm{N}$. Lo sforzo vale

$$
\sigma = \frac{F}{S} = \frac{7{,}85\times10^{3}}{5{,}03\times10^{-5}}\ \mathrm{Pa} \approx 1{,}56\times10^{8}\ \mathrm{Pa} = 156\ \mathrm{MPa},
$$

con coefficiente di sicurezza $\sigma_s/\sigma \approx 1{,}6$. La deformazione e l'allungamento sono

$$
\varepsilon = \frac{\sigma}{E} = \frac{1{,}56\times10^{8}}{2{,}0\times10^{11}} = 7{,}8\times10^{-4}, \qquad \Delta L = \varepsilon L_0 = 7{,}8\ \mathrm{mm}.
$$

La contrazione del diametro è $\Delta d = -\nu\varepsilon d = -0{,}29\cdot7{,}8\times10^{-4}\cdot8{,}0\times10^{-3}\ \mathrm{m} \approx -1{,}8\ \mu\mathrm{m}$. L'energia elastica è

$$
U = \tfrac12 F\Delta L = \tfrac12\cdot7{,}85\times10^{3}\cdot7{,}8\times10^{-3}\ \mathrm{J} \approx 31\ \mathrm{J}.
$$

### Punti chiave

- **Sforzo** = forza/superficie (Pa), **deformazione** = variazione relativa (adimensionale); il loro rapporto in regime lineare è un **modulo elastico**.
- **Trazione/compressione**: $\sigma = E\varepsilon$ (legge di Hooke), con $E$ modulo di Young; una sbarra equivale a una molla con $k = ES/L_0$.
- La curva sforzo-deformazione mostra regime elastico, snervamento, regime plastico e rottura; materiali duttili e fragili si comportano diversamente.
- **Compressione idrostatica**: $\Delta p = -B\,\Delta V/V_0$; $B$ è definito anche per i fluidi.
- **Taglio**: $\tau = G\gamma$; i fluidi in quiete hanno $G = 0$.
- **Legge di Poisson**: $\varepsilon_\perp = -\nu\varepsilon$, con $\nu \le 0{,}5$; per solidi isotropi $G = E/[2(1+\nu)]$ e $B = E/[3(1-2\nu)]$.
- **Modello atomico**: attorno al minimo del potenziale interatomico la forza è elastica, e $E \approx k/r_0$; asimmetria della buca e difetti spiegano non linearità, plasticità e dilatazione termica.
