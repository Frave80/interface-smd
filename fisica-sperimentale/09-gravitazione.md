# Capitolo 9 — Gravitazione

La gravitazione è la prima interazione fondamentale della natura a essere stata descritta in forma matematica, ed è storicamente il banco di prova su cui è nata la fisica moderna. Il percorso che va dalle accurate osservazioni astronomiche di Tycho Brahe, alle leggi empiriche di Kepler, fino alla legge di gravitazione universale di Newton è uno degli esempi più limpidi di metodo sperimentale: prima si raccolgono dati, poi si individuano regolarità quantitative (la *cinematica* del moto planetario), infine si formula una legge di forza che, insieme ai principi della dinamica, spiega quelle regolarità e ne prevede di nuove. In questo capitolo si segue proprio questo percorso. La sezione sulla **cinematica gravitazionale** presenta le tre leggi di Kepler come descrizione del moto dei pianeti; la sezione sulla **dinamica gravitazionale** introduce la forza e il campo gravitazionale, l'energia potenziale e, mediante il concetto di energia potenziale efficace, classifica le orbite possibili in funzione dell'energia totale. I risultati hanno applicazioni dirette nella meccanica orbitale dei satelliti artificiali, nel calcolo delle velocità di fuga e nella comprensione di fenomeni come le maree.

## 9.1 Cinematica gravitazionale

All'inizio del XVII secolo Johannes Kepler, analizzando per anni le osservazioni della posizione di Marte raccolte con straordinaria precisione da Tycho Brahe, giunse a formulare tre leggi che descrivono il moto dei pianeti attorno al Sole. Si tratta di leggi **empiriche** e **cinematiche**: descrivono *come* si muovono i pianeti, senza spiegare *perché*. Esse rappresentarono una rottura radicale con la tradizione astronomica precedente, che fin dall'antichità aveva cercato di descrivere i moti celesti con combinazioni di moti circolari uniformi, considerati perfetti. Kepler mostrò che l'orbita di Marte non poteva essere riprodotta entro gli errori sperimentali delle misure di Tycho (pochi primi d'arco) da alcuna combinazione di cerchi ragionevole, e che era invece descritta in modo semplice ed esatto da un'ellisse. Le tre leggi valgono per tutti i pianeti del Sistema Solare e, con le opportune modifiche, per ogni sistema di corpi legati gravitazionalmente: satelliti attorno ai pianeti, stelle doppie, esopianeti. Esse sono valide nell'approssimazione in cui la massa del corpo centrale è molto maggiore di quella del corpo orbitante e si possono trascurare le perturbazioni dovute agli altri corpi.

### 9.1.1 Prima legge di Kepler

La **prima legge di Kepler** (legge delle orbite) afferma: *i pianeti descrivono orbite ellittiche, di cui il Sole occupa uno dei fuochi*.

Un'**ellisse** è il luogo dei punti del piano per i quali la somma delle distanze da due punti fissi, i **fuochi** $F_1$ e $F_2$, è costante e pari a $2a$, dove $a$ è il **semiasse maggiore**. Detti $b$ il **semiasse minore** e $c$ la semidistanza focale, vale $a^2 = b^2 + c^2$. La forma dell'ellisse è descritta dall'**eccentricità** $\varepsilon = c/a$, compresa tra 0 (circonferenza) e 1 (ellisse degenere in un segmento). In coordinate polari con origine in un fuoco, l'equazione dell'ellisse è

$$
r(\theta) = \frac{a(1 - \varepsilon^2)}{1 + \varepsilon\cos\theta},
$$

dove $\theta$ è l'angolo misurato a partire dalla direzione del punto più vicino al fuoco. Il punto dell'orbita più vicino al Sole si chiama **perielio**, a distanza $r_p = a(1 - \varepsilon)$, quello più lontano **afelio**, a distanza $r_a = a(1 + \varepsilon)$; la loro media aritmetica è proprio il semiasse maggiore, $a = (r_p + r_a)/2$, che rappresenta quindi la distanza media "geometrica" del pianeta dal Sole. Per orbite attorno alla Terra si parla di **perigeo** e **apogeo**.

Le orbite dei pianeti del Sistema Solare sono in realtà ellissi poco eccentriche, quasi circolari: l'eccentricità dell'orbita terrestre è circa 0,017, quella di Marte circa 0,093, quella di Mercurio, la più elevata tra i pianeti, circa 0,21. Proprio la relativamente alta eccentricità di Marte permise a Kepler di individuare la forma ellittica. Le comete, invece, possono avere orbite estremamente allungate: la cometa di Halley ha eccentricità circa 0,97. Per la Terra la differenza tra distanza al perielio (circa $1{,}47\times10^{11}\ \mathrm{m}$, all'inizio di gennaio) e all'afelio (circa $1{,}52\times10^{11}\ \mathrm{m}$, all'inizio di luglio) è di circa il 3%: le stagioni non sono dovute a questa variazione, ma all'inclinazione dell'asse terrestre.

Va osservato che la prima legge contiene implicitamente un'altra informazione: l'orbita è **piana**, e il piano dell'orbita passa per il Sole. Come si vedrà, questa proprietà è una conseguenza diretta della conservazione del momento angolare in un campo di forze centrale. A rigore, inoltre, il fuoco dell'ellisse non è occupato dal centro del Sole ma dal **centro di massa** del sistema Sole-pianeta; poiché la massa del Sole è enormemente maggiore di quelle dei pianeti (circa 1000 volte quella di Giove, il più massiccio), la differenza è piccola, ma non nulla ed è misurabile: il Sole oscilla attorno al baricentro del Sistema Solare, che a volte si trova addirittura al di fuori della sua superficie. Questo stesso effetto di oscillazione della stella è uno dei metodi con cui oggi si scoprono i pianeti extrasolari.

### 9.1.2 Seconda legge di Kepler

La **seconda legge di Kepler** (legge delle aree) afferma: *il raggio vettore che congiunge il Sole al pianeta descrive aree uguali in tempi uguali*.

Si definisce **velocità areolare** la rapidità con cui il raggio vettore spazza l'area. In un intervallo infinitesimo $\mathrm{d}t$ il pianeta passa da $\vec{r}$ a $\vec{r} + \mathrm{d}\vec{r}$, e l'area spazzata è quella del triangolo infinitesimo di lati $\vec{r}$ e $\mathrm{d}\vec{r}$:

$$
\mathrm{d}A = \tfrac12|\vec{r}\times\mathrm{d}\vec{r}| \quad\Longrightarrow\quad \frac{\mathrm{d}A}{\mathrm{d}t} = \tfrac12|\vec{r}\times\vec{v}| = \frac{L}{2m},
$$

dove $L = |\vec{r}\times m\vec{v}|$ è il modulo del momento angolare del pianeta rispetto al Sole. In coordinate polari si ha anche $\mathrm{d}A/\mathrm{d}t = \tfrac12 r^2\dot\theta$. La seconda legge di Kepler afferma dunque che la velocità areolare è costante, il che equivale a dire che **il momento angolare del pianeta rispetto al Sole si conserva**.

Una conseguenza immediata è che il pianeta si muove più velocemente quando è vicino al Sole e più lentamente quando è lontano. Al perielio e all'afelio la velocità è perpendicolare al raggio vettore, per cui la conservazione del momento angolare dà semplicemente

$$
r_p v_p = r_a v_a \quad\Longrightarrow\quad \frac{v_p}{v_a} = \frac{r_a}{r_p} = \frac{1 + \varepsilon}{1 - \varepsilon}.
$$

Per la Terra questo rapporto è circa 1,034: la Terra è più veloce in gennaio che in luglio, e infatti l'inverno boreale (dall'equinozio d'autunno a quello di primavera) dura circa una settimana in meno dell'estate boreale.

Dal punto di vista dinamico, la conservazione del momento angolare implica che il momento della forza agente sul pianeta rispetto al Sole sia nullo: $\vec{r}\times\vec{F} = 0$, cioè la forza è sempre diretta lungo il raggio vettore, ossia è **centrale** con centro nel Sole. È questa la prima informazione sulla forza di gravità che si può dedurre dalle leggi di Kepler. Si noti che la seconda legge vale per *qualsiasi* forza centrale, non solo per quella gravitazionale: essa non dice nulla sulla dipendenza della forza dalla distanza. La conservazione del momento angolare spiega anche perché l'orbita sia piana: $\vec{L}$ è un vettore costante e sia $\vec{r}$ che $\vec{v}$ gli sono sempre perpendicolari, per cui il moto si svolge nel piano fisso perpendicolare a $\vec{L}$ passante per il Sole.

### 9.1.3 Terza legge di Kepler

La **terza legge di Kepler** (legge dei periodi), pubblicata alcuni anni dopo le prime due, afferma: *i quadrati dei periodi di rivoluzione dei pianeti sono proporzionali ai cubi dei semiassi maggiori delle loro orbite*:

$$
\frac{T^2}{a^3} = \text{costante (uguale per tutti i pianeti)}.
$$

La legge mette in relazione orbite di pianeti diversi, e non riguarda quindi un singolo moto ma la struttura dell'intero Sistema Solare. Usando come unità il periodo e il semiasse dell'orbita terrestre (l'anno e l'**unità astronomica**, $1\ \mathrm{UA} \approx 1{,}496\times10^{11}\ \mathrm{m}$), la costante vale 1 e la legge diventa semplicemente $T^2 = a^3$. Ad esempio Giove, con $a \approx 5{,}2\ \mathrm{UA}$, ha un periodo $T \approx \sqrt{5{,}2^3} \approx 11{,}9$ anni, in accordo con le osservazioni.

Il significato dinamico della terza legge si coglie facilmente nel caso di orbite circolari, buona approssimazione per i pianeti. Un pianeta di massa $m$ in moto circolare uniforme di raggio $r$ e periodo $T$ ha accelerazione centripeta $a_c = \omega^2 r = 4\pi^2 r/T^2$. Se $T^2 = Cr^3$, la forza necessaria vale

$$
F = m\frac{4\pi^2 r}{T^2} = \frac{4\pi^2}{C}\frac{m}{r^2}.
$$

La forza che il Sole esercita sui pianeti è quindi **inversamente proporzionale al quadrato della distanza** e **proporzionale alla massa del pianeta**. Fu questo il ragionamento con cui Newton, partendo dalle leggi di Kepler, arrivò alla forma della legge di gravitazione universale. Per il principio di azione e reazione, la forza deve essere proporzionale anche alla massa del Sole, per cui $4\pi^2/C = GM_\odot$, e la terza legge assume la forma

$$
T^2 = \frac{4\pi^2}{GM}a^3,
$$

valida anche per orbite ellittiche con $a$ semiasse maggiore. Una trattazione più accurata, che tiene conto del moto del Sole attorno al centro di massa comune, sostituisce $M$ con $M + m$: la "costante" di Kepler non è quindi rigorosamente la stessa per tutti i pianeti, ma le differenze sono piccolissime nel Sistema Solare.

La terza legge ha un'applicazione pratica di enorme importanza: permette di **misurare le masse dei corpi celesti**. Misurando periodo e semiasse dell'orbita di un satellite si ricava la massa del corpo attorno a cui orbita: la massa del Sole si ottiene dall'orbita terrestre, quella di Giove dalle orbite dei suoi satelliti medicei, quella delle stelle doppie dalle loro orbite reciproche, perfino la massa del buco nero al centro della nostra galassia dalle orbite delle stelle che gli ruotano vicino. Per i satelliti artificiali terrestri, la stessa legge determina il raggio dell'**orbita geostazionaria**, quella con periodo pari a un giorno siderale, circa $4{,}2\times10^{7}\ \mathrm{m}$ dal centro della Terra, sfruttata per le telecomunicazioni.

### Esercizio d'esempio

La Luna orbita attorno alla Terra con periodo siderale $T = 27{,}3$ giorni su un'orbita di semiasse maggiore $a = 3{,}84\times10^{8}\ \mathrm{m}$ ed eccentricità $\varepsilon = 0{,}055$. Usando $G = 6{,}67\times10^{-11}\ \mathrm{N\,m^2/kg^2}$, stimare la massa della Terra e il rapporto tra la velocità della Luna al perigeo e all'apogeo. Calcolare infine la velocità areolare.

**Soluzione.** Il periodo in secondi è $T = 27{,}3\cdot86400 \approx 2{,}36\times10^{6}\ \mathrm{s}$. Dalla terza legge

$$
M_T = \frac{4\pi^2a^3}{GT^2} = \frac{4\pi^2\cdot(3{,}84\times10^{8})^3}{6{,}67\times10^{-11}\cdot(2{,}36\times10^{6})^2}\ \mathrm{kg} \approx 6{,}0\times10^{24}\ \mathrm{kg},
$$

in ottimo accordo con il valore accettato $5{,}97\times10^{24}\ \mathrm{kg}$ (la piccola differenza include la massa lunare, trascurata). Dalla seconda legge

$$
\frac{v_p}{v_a} = \frac{1 + \varepsilon}{1 - \varepsilon} = \frac{1{,}055}{0{,}945} \approx 1{,}12.
$$

L'area dell'ellisse è $\pi ab$ con $b = a\sqrt{1 - \varepsilon^2} \approx 3{,}83\times10^{8}\ \mathrm{m}$, per cui la velocità areolare costante vale

$$
\frac{\mathrm{d}A}{\mathrm{d}t} = \frac{\pi ab}{T} \approx \frac{\pi\cdot3{,}84\times10^{8}\cdot3{,}83\times10^{8}}{2{,}36\times10^{6}}\ \mathrm{m^2/s} \approx 1{,}96\times10^{11}\ \mathrm{m^2/s}.
$$

### Punti chiave

- Le leggi di Kepler sono **empiriche** e **cinematiche**, dedotte dalle osservazioni di Tycho Brahe.
- **Prima legge**: orbite ellittiche con il Sole in un fuoco; $r_p = a(1-\varepsilon)$, $r_a = a(1+\varepsilon)$.
- **Seconda legge**: velocità areolare costante, $\mathrm{d}A/\mathrm{d}t = L/(2m)$, equivalente alla conservazione del momento angolare e quindi a una forza centrale.
- Il pianeta è più veloce al perielio: $v_pr_p = v_ar_a$.
- **Terza legge**: $T^2/a^3$ costante; per orbite circolari implica una forza $\propto m/r^2$.
- In forma newtoniana $T^2 = 4\pi^2a^3/(GM)$: permette di misurare le masse dei corpi celesti.

## 9.2 Dinamica gravitazionale

Le leggi di Kepler descrivono il moto dei pianeti ma non ne spiegano la causa. Fu Isaac Newton, nei *Principia* (1687), a mostrare che esse sono conseguenza di un'unica legge di forza, la **legge di gravitazione universale**, combinata con i principi della dinamica. L'aggettivo "universale" esprime la grande intuizione newtoniana: la stessa forza che fa cadere una mela a terra tiene la Luna in orbita attorno alla Terra e i pianeti attorno al Sole. Il confine aristotelico tra fisica terrestre e fisica celeste veniva così abolito. In questa sezione si formula la legge di gravitazione, si introduce il concetto di **campo gravitazionale**, si ricava l'**energia potenziale gravitazionale** e, sfruttando le conservazioni di energia e momento angolare, si studia la forma delle orbite possibili attraverso il metodo dell'**energia potenziale efficace**, arrivando a classificare le traiettorie in base al segno dell'**energia totale**.

### 9.2.1 Forza gravitazionale

La **legge di gravitazione universale** afferma che due punti materiali di masse $m_1$ e $m_2$, posti a distanza $r$, si attraggono con una forza diretta lungo la retta congiungente, di modulo proporzionale al prodotto delle masse e inversamente proporzionale al quadrato della distanza. In forma vettoriale, la forza esercitata da $m_1$ su $m_2$ è

$$
\vec{F}_{12} = -G\frac{m_1m_2}{r^2}\hat{r}_{12},
$$

dove $\hat{r}_{12}$ è il versore diretto da $m_1$ verso $m_2$ e il segno meno esprime il carattere **attrattivo** della forza. La costante $G$ è la **costante di gravitazione universale**:

$$
G \approx 6{,}674\times10^{-11}\ \mathrm{N\,m^2/kg^2}.
$$

Il valore estremamente piccolo di $G$ spiega perché l'attrazione gravitazionale tra oggetti di uso comune sia del tutto impercettibile: due masse di $1\ \mathrm{kg}$ poste a $1\ \mathrm{m}$ di distanza si attraggono con una forza di circa $7\times10^{-11}\ \mathrm{N}$. La gravità diventa dominante solo quando almeno una delle masse è enorme, come per i corpi celesti. La prima misura diretta di $G$ in laboratorio fu realizzata da Henry Cavendish alla fine del XVIII secolo con una **bilancia di torsione**: due piccole sfere fissate alle estremità di un'asta sospesa a un filo sottile venivano attratte da due grandi sfere di piombo, e dalla torsione del filo si ricavava la forza. Poiché, come si vedrà, $g = GM_T/R_T^2$, la misura di $G$ permise di ricavare la massa della Terra, e per questo l'esperimento è stato definito "la pesata della Terra". Ancora oggi $G$ è la costante fondamentale conosciuta con la minore precisione relativa.

Le masse che compaiono nella legge di gravitazione sono **masse gravitazionali**, che misurano l'attitudine di un corpo ad attrarre e a essere attratto. A priori potrebbero essere diverse dalle **masse inerziali** che compaiono in $\vec{F} = m\vec{a}$; gli esperimenti, da Galileo e Newton fino alle moderne bilance di torsione di Eötvös e ai test con satelliti, mostrano che sono proporzionali con precisione di parti su $10^{15}$, e con una scelta opportuna di $G$ uguali. Questa equivalenza è il motivo per cui tutti i corpi cadono con la stessa accelerazione nel vuoto, e sarà il punto di partenza della relatività generale.

La legge, scritta per punti materiali, si estende a corpi estesi sommando (integrando) i contributi di tutte le coppie di elementi di massa. Newton dimostrò il fondamentale **teorema dei gusci**: un guscio sferico omogeneo attrae un punto esterno come se tutta la sua massa fosse concentrata nel centro, mentre esercita forza nulla su un punto interno. Di conseguenza una distribuzione di massa a simmetria sferica (come approssimativamente la Terra o il Sole) agisce all'esterno come un punto materiale posto nel centro. Questo giustifica l'uso della legge per i pianeti trattati come punti.

### 9.2.2 Campo gravitazionale

Per descrivere l'azione della gravità indipendentemente dal corpo che la subisce, si introduce il **campo gravitazionale**. Una massa sorgente $M$ modifica le proprietà dello spazio circostante; una massa di prova $m$ posta in un punto $\vec{r}$ subisce una forza $\vec{F} = m\vec{g}(\vec{r})$, dove

$$
\vec{g}(\vec{r}) = \frac{\vec{F}}{m} = -G\frac{M}{r^2}\hat{r}
$$

è il **campo gravitazionale** generato da $M$ nel punto $\vec{r}$ (con origine nella sorgente). Il campo ha le dimensioni di un'accelerazione, si misura in $\mathrm{N/kg} = \mathrm{m/s^2}$ ed è, per l'equivalenza tra massa inerziale e gravitazionale, proprio l'accelerazione con cui cade un corpo libero in quel punto. Per più sorgenti vale il **principio di sovrapposizione**: il campo totale è la somma vettoriale dei campi delle singole masse.

Sulla superficie terrestre, trattando la Terra come una sfera omogenea di massa $M_T$ e raggio $R_T$, il campo vale

$$
g_0 = \frac{GM_T}{R_T^2} \approx \frac{6{,}67\times10^{-11}\cdot5{,}97\times10^{24}}{(6{,}37\times10^{6})^2}\ \mathrm{m/s^2} \approx 9{,}82\ \mathrm{m/s^2}.
$$

Il valore effettivamente misurato varia tra circa $9{,}78\ \mathrm{m/s^2}$ all'equatore e $9{,}83\ \mathrm{m/s^2}$ ai poli, per lo schiacciamento della Terra e per l'effetto della forza centrifuga dovuta alla rotazione terrestre. Al crescere della quota $h$ il campo diminuisce come $g(h) = g_0R_T^2/(R_T + h)^2 \approx g_0(1 - 2h/R_T)$ per $h \ll R_T$: a $10\ \mathrm{km}$ di quota la diminuzione è di circa lo 0,3%, a $400\ \mathrm{km}$ (Stazione Spaziale Internazionale) è di circa l'11%. Gli astronauti in orbita non sono dunque in "assenza di gravità": sono in caduta libera, come l'intera stazione, e per questo percepiscono l'**assenza di peso**.

All'interno di una sfera omogenea, per il teorema dei gusci, contribuisce solo la massa interna al raggio $r$, che cresce come $r^3$: il campo cresce linearmente con la distanza dal centro, $g(r) = g_0 r/R_T$, ed è nullo al centro.

Un aspetto concettualmente importante è che il campo trasforma l'"azione a distanza" newtoniana in una proprietà locale dello spazio. Nella teoria newtoniana il campo si adatta istantaneamente a ogni spostamento della sorgente; la relatività generale mostra invece che le perturbazioni del campo si propagano alla velocità della luce, come confermato dall'osservazione diretta delle onde gravitazionali.

### 9.2.3 Energia potenziale gravitazionale

La forza gravitazionale è centrale e il suo modulo dipende solo dalla distanza: è dunque **conservativa**. Il lavoro compiuto dalla forza esercitata da $M$ su $m$ quando questa passa dalla distanza $r_A$ alla distanza $r_B$ dipende solo da $r_A$ e $r_B$:

$$
W_{A\to B} = \int_{r_A}^{r_B}\left(-\frac{GMm}{r^2}\right)\mathrm{d}r = GMm\left(\frac{1}{r_B} - \frac{1}{r_A}\right).
$$

Scegliendo lo zero dell'energia potenziale a distanza infinita, convenzione naturale perché lì la forza si annulla, si ottiene l'**energia potenziale gravitazionale**:

$$
U(r) = -\frac{GMm}{r}.
$$

È negativa per ogni distanza finita e cresce (verso lo zero) all'aumentare di $r$: per allontanare le due masse occorre compiere lavoro contro la forza attrattiva. La quantità $-U(r)$ rappresenta il lavoro minimo da fornire per portare $m$ dalla distanza $r$ all'infinito con velocità finale nulla. Si definisce anche il **potenziale gravitazionale** $V(r) = U/m = -GM/r$, energia per unità di massa, misurato in $\mathrm{J/kg}$, legato al campo da $\vec{g} = -\nabla V$.

È istruttivo verificare che questa espressione riproduce la familiare $U = mgh$ vicino alla superficie terrestre. Per $r = R_T + h$ con $h \ll R_T$:

$$
U(R_T + h) - U(R_T) = -GM_Tm\left(\frac{1}{R_T + h} - \frac{1}{R_T}\right) \approx \frac{GM_Tm}{R_T^2}h = mg_0h.
$$

La formula $mgh$ è dunque l'approssimazione al primo ordine dell'espressione esatta, valida finché la quota è piccola rispetto al raggio terrestre. Per un sistema di più masse l'energia potenziale totale è la somma delle energie di tutte le coppie, $U = -\sum_{i<j}Gm_im_j/r_{ij}$: rappresenta il lavoro necessario per costruire la configurazione portando le masse dall'infinito.

### 9.2.4 Orbite planetarie

Si consideri ora un corpo di massa $m$ (pianeta, satellite) in moto nel campo di una massa $M \gg m$, che si suppone fissa. La forza è centrale e conservativa, per cui si conservano sia il momento angolare $\vec{L}$ rispetto al centro, sia l'energia meccanica $E$. La conservazione di $\vec{L}$ implica che il moto è piano e che la velocità areolare è costante: la seconda legge di Kepler è un teorema per qualsiasi forza centrale. In coordinate polari nel piano dell'orbita, la velocità si scompone in una componente radiale $\dot r$ e una trasversale $r\dot\theta$, con $L = mr^2\dot\theta$.

Risolvendo le equazioni del moto (il calcolo completo, tramite la sostituzione $u = 1/r$, porta alla cosiddetta equazione di Binet) si trova che le traiettorie possibili in un campo di forza $\propto 1/r^2$ sono **coniche** con un fuoco nel centro di forza:

$$
r(\theta) = \frac{p}{1 + \varepsilon\cos\theta}, \qquad p = \frac{L^2}{GMm^2},
$$

dove $p$ è il **parametro** della conica e $\varepsilon$ la sua eccentricità, legata all'energia da

$$
\varepsilon = \sqrt{1 + \frac{2EL^2}{G^2M^2m^3}}.
$$

A seconda del valore di $\varepsilon$ l'orbita è una **circonferenza** ($\varepsilon = 0$), un'**ellisse** ($0 < \varepsilon < 1$), una **parabola** ($\varepsilon = 1$) o un ramo di **iperbole** ($\varepsilon > 1$). I pianeti seguono orbite ellittiche, chiuse e periodiche: si ritrova così la prima legge di Kepler come conseguenza della legge di gravitazione. Le orbite paraboliche e iperboliche sono invece aperte: il corpo arriva dall'infinito, passa vicino al centro e si allontana definitivamente, come accade per alcune comete o per le sonde spaziali in sorvolo planetario. Un'importante proprietà delle orbite in campo $1/r^2$ è di essere **chiuse**: l'ellisse si ripete identica a ogni giro. Piccole perturbazioni (altri pianeti, schiacciamento del Sole, effetti relativistici) provocano una lenta rotazione dell'asse dell'ellisse, la **precessione del perielio**, che nel caso di Mercurio ha fornito una delle prime conferme della relatività generale.

Il caso più semplice è l'**orbita circolare** di raggio $r$: la forza gravitazionale fornisce la forza centripeta, $GMm/r^2 = mv^2/r$, da cui la **velocità orbitale**

$$
v_c = \sqrt{\frac{GM}{r}}.
$$

Per un satellite in orbita bassa attorno alla Terra ($r \approx R_T$) si ottiene la **prima velocità cosmica**, $v_c \approx 7{,}9\ \mathrm{km/s}$, con un periodo di circa 84 minuti. Il periodo $T = 2\pi r/v_c = 2\pi\sqrt{r^3/(GM)}$ riproduce la terza legge di Kepler.

### 9.2.5 Energia potenziale efficace

Un metodo potente per analizzare qualitativamente le orbite senza risolvere esplicitamente le equazioni del moto è quello dell'**energia potenziale efficace**. L'energia meccanica del corpo, in coordinate polari, si scrive

$$
E = \tfrac12 m\dot r^2 + \tfrac12 mr^2\dot\theta^2 - \frac{GMm}{r}.
$$

Usando la conservazione del momento angolare, $\dot\theta = L/(mr^2)$, il termine cinetico trasversale si esprime in funzione della sola $r$:

$$
E = \tfrac12 m\dot r^2 + \underbrace{\frac{L^2}{2mr^2} - \frac{GMm}{r}}_{U_{\text{eff}}(r)}.
$$

Il problema bidimensionale si riduce così a un problema **unidimensionale** nella sola coordinata radiale, con una particella che si muove sotto l'azione di un'**energia potenziale efficace**

$$
U_{\text{eff}}(r) = \frac{L^2}{2mr^2} - \frac{GMm}{r}.
$$

Il primo termine, detto **barriera centrifuga**, è positivo e cresce rapidamente per $r \to 0$: rappresenta l'effetto della conservazione del momento angolare, che impedisce al corpo di cadere sul centro se $L \neq 0$. Il secondo termine è l'energia potenziale gravitazionale vera. A grandi distanze domina il termine gravitazionale e $U_{\text{eff}} \to 0^-$; a piccole distanze domina la barriera centrifuga e $U_{\text{eff}} \to +\infty$. La curva presenta quindi un **minimo**, in corrispondenza del raggio

$$
r_0 = \frac{L^2}{GMm^2},
$$

ottenuto imponendo $\mathrm{d}U_{\text{eff}}/\mathrm{d}r = 0$, dove l'energia potenziale efficace vale $U_{\text{eff}}(r_0) = -G^2M^2m^3/(2L^2)$.

Si applicano ora i metodi visti per la statica del punto e i moti unidimensionali. Poiché $\tfrac12 m\dot r^2 \ge 0$, il moto è consentito solo dove $U_{\text{eff}}(r) \le E$. I punti in cui $U_{\text{eff}}(r) = E$ sono **punti di inversione** del moto radiale: lì $\dot r = 0$ e la velocità è puramente trasversale. Corrispondono al perielio e all'afelio dell'orbita. Si osservi che nel moto radiale il punto non si ferma: la velocità trasversale non si annulla mai se $L \neq 0$.

### 9.2.6 Energia totale

L'analisi del grafico di $U_{\text{eff}}$ consente di classificare le orbite in base al valore dell'**energia totale** $E$, e mostra il legame con l'eccentricità visto in precedenza.

Se $E = U_{\text{eff}}(r_0)$, valore minimo, l'unico valore di $r$ permesso è $r_0$: la distanza resta costante e l'orbita è **circolare** ($\varepsilon = 0$). Se $U_{\text{eff}}(r_0) < E < 0$, il moto radiale avviene tra due punti di inversione $r_p$ e $r_a$, la distanza oscilla tra un minimo e un massimo e l'orbita è **ellittica** ($0 < \varepsilon < 1$): è un'**orbita legata**. Se $E = 0$ esiste un solo punto di inversione, il perielio, e il corpo può allontanarsi fino all'infinito, dove arriva con velocità nulla: l'orbita è **parabolica** ($\varepsilon = 1$). Se $E > 0$ il corpo arriva all'infinito con velocità residua non nulla: l'orbita è **iperbolica** ($\varepsilon > 1$). Le orbite con $E \ge 0$ sono **non legate**.

Per un'orbita circolare il legame tra le energie è particolarmente semplice. Dalla relazione $mv^2 = GMm/r$ segue $K = GMm/(2r) = -U/2$, e quindi

$$
E = K + U = -\frac{GMm}{2r} = \frac{U}{2} = -K.
$$

Questo è un caso particolare del **teorema del viriale**. Per un'orbita ellittica si dimostra che l'energia totale dipende solo dal semiasse maggiore:

$$
E = -\frac{GMm}{2a},
$$

indipendentemente dall'eccentricità. Combinando con la conservazione dell'energia si ricava l'**equazione vis-viva**, $v^2 = GM\left(\frac{2}{r} - \frac{1}{a}\right)$, che dà la velocità in ogni punto dell'orbita, strumento base della meccanica orbitale.

Un'applicazione fondamentale è la **velocità di fuga**: la velocità minima che deve avere un corpo lanciato dalla superficie di un pianeta per allontanarsi indefinitamente, cioè per avere $E \ge 0$. Ponendo $E = 0$:

$$
\tfrac12 mv_f^2 - \frac{GMm}{R} = 0 \quad\Longrightarrow\quad v_f = \sqrt{\frac{2GM}{R}} = \sqrt2\,v_c.
$$

Per la Terra $v_f \approx 11{,}2\ \mathrm{km/s}$ (**seconda velocità cosmica**), indipendente dalla massa del corpo e dalla direzione di lancio (trascurando l'atmosfera e la rotazione terrestre). Per la Luna vale solo $2{,}4\ \mathrm{km/s}$, il che spiega perché essa non abbia trattenuto un'atmosfera: le molecole di gas, a temperature ordinarie, hanno velocità quadratiche medie che ne raggiungono una frazione non trascurabile e nel corso di tempi geologici sfuggono. Se un corpo fosse così compatto che $v_f$ superasse la velocità della luce, nemmeno la luce potrebbe sfuggire: è l'idea, anticipata già nel Settecento, del **buco nero**, il cui raggio critico $R_S = 2GM/c^2$ (raggio di Schwarzschild) si ottiene, per una coincidenza, proprio da questo ragionamento classico.

Infine, il concetto di energia totale spiega le **manovre orbitali**: per passare da un'orbita circolare bassa a una più alta occorre *aumentare* l'energia totale (renderla meno negativa), ad esempio con un'accensione dei motori al perigeo che trasforma l'orbita in un'ellisse di trasferimento (**orbita di Hohmann**) e una seconda accensione all'apogeo per circolarizzarla. Paradossalmente, sull'orbita più alta la velocità è minore: il lavoro dei motori ha aumentato l'energia potenziale più di quanto sia diminuita l'energia cinetica.

### Esercizio d'esempio

Un satellite di massa $m = 500\ \mathrm{kg}$ si trova su un'orbita circolare a quota $h = 400\ \mathrm{km}$ sopra la superficie terrestre ($R_T = 6{,}37\times10^{6}\ \mathrm{m}$, $M_T = 5{,}97\times10^{24}\ \mathrm{kg}$, $G = 6{,}67\times10^{-11}\ \mathrm{N\,m^2/kg^2}$). Calcolare velocità orbitale, periodo, energia totale e l'energia minima da fornire per farlo sfuggire all'attrazione terrestre.

**Soluzione.** Il raggio orbitale è $r = R_T + h = 6{,}77\times10^{6}\ \mathrm{m}$ e $GM_T = 3{,}98\times10^{14}\ \mathrm{m^3/s^2}$. La velocità orbitale vale

$$
v_c = \sqrt{\frac{GM_T}{r}} = \sqrt{\frac{3{,}98\times10^{14}}{6{,}77\times10^{6}}}\ \mathrm{m/s} \approx 7{,}67\times10^{3}\ \mathrm{m/s}.
$$

Il periodo è

$$
T = \frac{2\pi r}{v_c} = \frac{2\pi\cdot6{,}77\times10^{6}}{7{,}67\times10^{3}}\ \mathrm{s} \approx 5{,}55\times10^{3}\ \mathrm{s} \approx 92\ \mathrm{min}.
$$

L'energia totale è

$$
E = -\frac{GM_Tm}{2r} = -\frac{3{,}98\times10^{14}\cdot500}{2\cdot6{,}77\times10^{6}}\ \mathrm{J} \approx -1{,}47\times10^{10}\ \mathrm{J}.
$$

Per sfuggire il satellite deve raggiungere $E = 0$: l'energia minima da fornire è quindi $\Delta E = 1{,}47\times10^{10}\ \mathrm{J}$, pari a un aumento di velocità da $v_c$ a $\sqrt2\,v_c \approx 10{,}8\ \mathrm{km/s}$ con un'accensione tangenziale.

### Punti chiave

- **Legge di gravitazione universale**: $\vec{F} = -Gm_1m_2\hat{r}/r^2$, con $G \approx 6{,}67\times10^{-11}\ \mathrm{N\,m^2/kg^2}$ misurata con la bilancia di Cavendish.
- Massa gravitazionale e massa inerziale coincidono sperimentalmente: tutti i corpi cadono con la stessa accelerazione.
- **Campo gravitazionale** $\vec{g} = -GM\hat{r}/r^2$; per distribuzioni sferiche vale il teorema dei gusci.
- **Energia potenziale** $U = -GMm/r$ (zero all'infinito); vicino alla superficie si riduce a $mgh$.
- Le orbite in campo $1/r^2$ sono **coniche** con un fuoco nel centro; si conservano $\vec{L}$ ed $E$.
- **Energia potenziale efficace** $U_{\text{eff}} = L^2/(2mr^2) - GMm/r$: riduce il problema a una dimensione.
- Classificazione: $E<0$ orbite legate (ellisse, cerchio), $E=0$ parabola, $E>0$ iperbole; per l'ellisse $E = -GMm/(2a)$.
- **Velocità di fuga** $v_f = \sqrt{2GM/R} = \sqrt2\,v_c$, per la Terra $11{,}2\ \mathrm{km/s}$.
