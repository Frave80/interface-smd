# Capitolo 23 — Magnetostatica

La magnetostatica studia i fenomeni magnetici prodotti da magneti permanenti e da correnti elettriche stazionarie, cioè costanti nel tempo. Storicamente il magnetismo nasce come disciplina autonoma, legata all'osservazione di minerali capaci di attrarre il ferro e all'uso della bussola nella navigazione; solo nell'Ottocento, con gli esperimenti di Ørsted, Ampère, Biot, Savart e Laplace, si comprese che elettricità e magnetismo sono due aspetti dello stesso fenomeno. In questo capitolo partiamo dalla fenomenologia dei magneti, introduciamo il campo magnetico $\vec{B}$ attraverso la forza che esso esercita sulle cariche in moto (forza di Lorentz), mostriamo come le correnti generino campi magnetici (leggi di Laplace e di Biot-Savart), e ricaviamo le due leggi fondamentali che caratterizzano il campo magnetostatico: il teorema di Gauss, che esprime l'assenza di cariche magnetiche, e il teorema di Ampère, che lega la circuitazione di $\vec{B}$ alle correnti concatenate. Concluderemo con il dipolo magnetico, ponte tra la descrizione macroscopica e quella atomica, e con la formulazione differenziale delle leggi, che prepara il terreno alle equazioni di Maxwell del capitolo successivo.

## 23.1 Magnetizzazione

### 23.1.1 Magnetizzazione

Il primo contatto con il magnetismo è di natura del tutto empirica. Già nell'antichità era noto che un minerale, la **magnetite** (un ossido di ferro di formula $\mathrm{Fe_3O_4}$), possiede la proprietà di attrarre piccoli oggetti di ferro. Un corpo che manifesta spontaneamente e stabilmente questa proprietà prende il nome di **magnete permanente**. Si osserva inoltre che un pezzo di ferro ordinario, inizialmente inerte, posto a contatto o nelle vicinanze di un magnete acquista a sua volta la capacità di attrarre altro ferro: si dice allora che il ferro si è **magnetizzato**. Questo processo, la **magnetizzazione**, può essere temporaneo (il ferro dolce perde quasi subito la proprietà quando si allontana il magnete) oppure duraturo (l'acciaio temprato conserva a lungo la magnetizzazione acquisita, ed è così che si costruiscono gli aghi delle bussole).

L'osservazione sistematica di una sbarretta magnetizzata mostra che l'azione attrattiva non è distribuita uniformemente: essa è massima in prossimità delle estremità e praticamente nulla nella zona centrale. Le regioni in cui l'effetto è concentrato si chiamano **poli magnetici**. Se si sospende la sbarretta in modo che possa ruotare liberamente in un piano orizzontale, essa si orienta spontaneamente lungo una direzione ben definita, approssimativamente nord-sud geografica. Per convenzione si chiama **polo nord** l'estremità che punta verso il nord geografico e **polo sud** quella opposta. Questa è esattamente la bussola, e il fatto che essa funzioni ovunque sulla superficie terrestre ci dice che la Terra stessa si comporta come un grande magnete.

Un fatto sperimentale cruciale, che distingue profondamente il magnetismo dall'elettrostatica, è l'**inseparabilità dei poli**. Se si spezza una calamita a metà nel tentativo di isolare il polo nord dal polo sud, si ottengono due calamite più piccole, ciascuna dotata di entrambi i poli. Ripetendo l'operazione quante volte si vuole, fino alla scala atomica, si ritrovano sempre sistemi con un polo nord e un polo sud. Non esiste, almeno per quanto finora osservato, un **monopolo magnetico** isolato, analogo alla carica elettrica isolata. Questa osservazione suggerisce che la magnetizzazione sia una proprietà distribuita in tutto il volume del materiale, dovuta a piccoli "magneti elementari" orientati ordinatamente: in un pezzo di ferro non magnetizzato essi sono orientati a caso e i loro effetti si cancellano, mentre nel ferro magnetizzato sono allineati e i loro effetti si sommano. Vedremo nel paragrafo sul dipolo magnetico che questi magneti elementari sono in realtà correnti microscopiche legate al moto degli elettroni, come intuito da Ampère.

### 23.1.2 Forza magnetica

Avvicinando tra loro due magneti si osserva che poli dello stesso nome (nord-nord o sud-sud) si respingono, mentre poli di nome opposto (nord-sud) si attraggono. La fenomenologia ricorda quella delle cariche elettriche, ed è per questo che nei primi studi quantitativi, dovuti a Coulomb, si cercò di descrivere l'interazione tra poli con una legge analoga a quella elettrostatica, introducendo delle "masse magnetiche" fittizie. Con bilance di torsione Coulomb trovò che la forza tra due poli molto lontani dagli altri poli dei rispettivi magneti (ad esempio aghi magnetici lunghi e sottili) è inversamente proporzionale al quadrato della distanza. Tuttavia, poiché i poli non possono essere isolati, la forza tra due magneti reali è sempre il risultato delle quattro interazioni tra i poli di uno e quelli dell'altro, e a grande distanza decresce più rapidamente di $1/r^2$, come accade per i dipoli elettrici.

È importante sottolineare che la **forza magnetica** si manifesta solo su alcuni materiali: ferro, nichel, cobalto e loro leghe, detti **ferromagnetici**, sono fortemente attratti dai magneti, mentre la maggior parte delle sostanze (legno, vetro, rame, alluminio, acqua) risente di effetti magnetici talmente deboli da essere percepibili solo con strumenti sensibili. Questa selettività è un'altra differenza rispetto alla forza elettrica, che agisce su qualunque corpo carico. Inoltre un magnete non esercita alcuna forza su una carica elettrica ferma: un elettroscopio carico non viene perturbato dalla vicinanza di una calamita. Come vedremo nella sezione 23.2, la forza magnetica agisce invece sulle cariche in moto, e questa è la chiave per una definizione operativa rigorosa del campo magnetico.

Un esperimento storico fondamentale, eseguito da Ørsted nel 1820, mostrò che un filo percorso da corrente elettrica fa ruotare un ago magnetico posto nelle vicinanze. L'ago tende a disporsi perpendicolarmente al filo, e il verso della deviazione si inverte quando si inverte il verso della corrente. Fu la prima prova diretta che le correnti elettriche producono effetti magnetici. Subito dopo Ampère dimostrò che due fili paralleli percorsi da corrente si attraggono se le correnti sono equiverse e si respingono se sono opposte, senza che alcun magnete sia presente. Si comprese così che la forza magnetica è, in ultima analisi, una forza tra cariche in moto, e che i magneti permanenti non sono altro che sedi di correnti microscopiche.

### 23.1.3 Linee di flusso

Per visualizzare l'azione di un magnete nello spazio circostante si può ricorrere a un esperimento classico: si appoggia un foglio di carta su una calamita a sbarra e vi si cospargono sopra limatura di ferro. Battendo leggermente il foglio, i granelli di limatura, che si magnetizzano e si comportano ciascuno come un minuscolo ago magnetico, si dispongono lungo curve regolari che partono da un polo e arrivano all'altro. Queste curve sono le **linee di flusso** (o **linee di campo**) del campo magnetico. Analogamente si può esplorare la regione attorno al magnete con una piccola bussola: in ogni punto l'ago si dispone tangente alla linea di campo che passa per quel punto.

Per convenzione si orientano le linee di campo in modo che, all'esterno del magnete, escano dal polo nord ed entrino nel polo sud; in ogni punto il verso della linea coincide con quello indicato dal polo nord di un ago di prova. La densità delle linee, ossia il numero di linee che attraversano una superficie unitaria perpendicolare ad esse, è proporzionale all'intensità del campo: le linee sono fitte vicino ai poli, dove l'effetto è intenso, e rade lontano dal magnete.

C'è però una differenza essenziale rispetto alle linee del campo elettrostatico. Queste ultime nascono sulle cariche positive e terminano sulle cariche negative (o all'infinito), e non possono mai essere chiuse. Le linee del campo magnetico, invece, non terminano sui poli: proseguono all'interno del magnete, dal polo sud al polo nord, e si richiudono su se stesse. Le linee di campo magnetico sono quindi **sempre chiuse**. Questa proprietà topologica è la traduzione geometrica dell'inseparabilità dei poli, e verrà formalizzata nel teorema di Gauss per il campo magnetico (sezione 23.4). Nel caso di un filo rettilineo percorso da corrente, la limatura si dispone su circonferenze concentriche centrate sul filo e giacenti in piani perpendicolari a esso: anche qui le linee sono chiuse, e non esiste alcun "polo" da cui escano.

### 23.1.4 Campo magnetico

Le osservazioni precedenti giustificano l'introduzione di un campo vettoriale, il **campo magnetico** $\vec{B}$, che in ogni punto dello spazio descrive l'effetto magnetico prodotto dai magneti e dalle correnti presenti. In prima approssimazione la sua direzione è quella assunta da un ago magnetico di prova e il verso è quello indicato dal polo nord dell'ago. Per una definizione quantitativa serve però una legge di forza: come il campo elettrico è definito dalla forza su una carica di prova ferma, $\vec{E}=\vec{F}/q$, così il campo magnetico si definisce a partire dalla forza su una carica di prova in moto, secondo la relazione di Lorentz che vedremo nella prossima sezione:

$$\vec{F} = q\,\vec{v}\times\vec{B}.$$

L'unità di misura del campo magnetico nel Sistema Internazionale è il **tesla** (T). Dalla relazione precedente si ricava $1\,\mathrm{T} = 1\,\mathrm{N\,s\,C^{-1}\,m^{-1}} = 1\,\mathrm{N\,A^{-1}\,m^{-1}}$. Si usa talvolta anche il gauss (G), unità del sistema CGS, con $1\,\mathrm{G}=10^{-4}\,\mathrm{T}$. Per avere un'idea degli ordini di grandezza: il campo magnetico terrestre in superficie vale circa $5\times10^{-5}\,\mathrm{T}$; un magnete da frigorifero produce qualche millitesla; un buon magnete al neodimio raggiunge in prossimità della superficie $1\,\mathrm{T}$; gli elettromagneti superconduttori delle macchine per risonanza magnetica operano tipicamente tra $1{,}5$ e $3\,\mathrm{T}$, mentre i magneti degli acceleratori come LHC arrivano a circa $8\,\mathrm{T}$.

Il **campo magnetico terrestre** merita un cenno. In prima approssimazione è simile a quello di una grande calamita a sbarra posta al centro della Terra, con l'asse inclinato di circa $10^\circ$ rispetto all'asse di rotazione. Poiché il polo nord dell'ago della bussola punta verso il nord geografico, e poli opposti si attraggono, ne segue che nell'emisfero boreale si trova un **polo sud magnetico**: le linee del campo terrestre entrano nella Terra nell'emisfero nord ed escono nell'emisfero sud. Il campo non è in generale orizzontale: l'angolo che forma con il piano orizzontale si chiama **inclinazione**, mentre l'angolo tra la sua componente orizzontale e il meridiano geografico si chiama **declinazione**. A Milano l'inclinazione è di circa $60^\circ$ e la componente orizzontale vale circa $2{,}2\times10^{-5}\,\mathrm{T}$. L'origine del campo terrestre risiede nelle correnti elettriche del nucleo esterno fuso (meccanismo della geodinamo), a ulteriore conferma che i fenomeni magnetici hanno origine dalle cariche in moto.

Un'ultima osservazione riguarda la sovrapposizione: come il campo elettrico, anche il campo magnetico obbedisce al **principio di sovrapposizione**, ossia il campo prodotto da più sorgenti è la somma vettoriale dei campi prodotti da ciascuna sorgente singolarmente. Ciò deriva dalla linearità delle equazioni che governano il campo, che studieremo nelle prossime sezioni, ed è valido nel vuoto e nei materiali lineari (non nei ferromagneti, il cui comportamento è non lineare).

### Esercizio d'esempio

**Problema.** A Milano il campo magnetico terrestre ha intensità $B = 4{,}6\times10^{-5}\,\mathrm{T}$ e inclinazione $\theta = 61^\circ$ rispetto all'orizzontale. Calcolare la componente orizzontale $B_h$ e quella verticale $B_v$. Un ago di bussola può ruotare solo nel piano orizzontale: quale componente lo orienta? Se un secondo campo orizzontale $B' = 2{,}0\times10^{-5}\,\mathrm{T}$, diretto verso est, viene sovrapposto a quello terrestre, di quale angolo $\alpha$ ruota l'ago rispetto al nord magnetico?

**Soluzione.** Le componenti si ottengono proiettando:
$$B_h = B\cos\theta = 4{,}6\times10^{-5}\cdot\cos 61^\circ \simeq 4{,}6\times10^{-5}\cdot 0{,}485 \simeq 2{,}2\times10^{-5}\,\mathrm{T},$$
$$B_v = B\sin\theta = 4{,}6\times10^{-5}\cdot 0{,}875 \simeq 4{,}0\times10^{-5}\,\mathrm{T}.$$
L'ago orizzontale risente solo della componente $B_h$ (la componente verticale produce un momento che tende a inclinarlo, ma è bilanciato dal vincolo del perno). Sovrapponendo il campo $B'$ verso est, per il principio di sovrapposizione il campo orizzontale risultante forma con il nord un angolo
$$\tan\alpha = \frac{B'}{B_h} = \frac{2{,}0\times10^{-5}}{2{,}2\times10^{-5}} \simeq 0{,}91 \quad\Rightarrow\quad \alpha \simeq 42^\circ$$
verso est. L'intensità del campo orizzontale risultante è $\sqrt{B_h^2+B'^2}\simeq 3{,}0\times10^{-5}\,\mathrm{T}$. Questo è il principio della **bussola delle tangenti**, usata storicamente per misurare correnti tramite il campo che esse producono.

### Punti chiave

- I magneti permanenti presentano due poli, nord e sud; poli omonimi si respingono, poli opposti si attraggono.
- I poli magnetici sono inseparabili: non sono mai stati osservati monopoli magnetici isolati.
- Le linee del campo magnetico sono sempre chiuse: all'esterno vanno da nord a sud, all'interno del magnete da sud a nord.
- Le correnti elettriche producono effetti magnetici (Ørsted) e interagiscono tra loro magneticamente (Ampère): il magnetismo ha origine dalle cariche in moto.
- Il campo magnetico $\vec{B}$ si definisce tramite la forza su una carica in moto, $\vec{F}=q\vec{v}\times\vec{B}$; si misura in tesla, $1\,\mathrm{T}=1\,\mathrm{N\,A^{-1}m^{-1}}$.
- Il campo terrestre vale circa $5\times10^{-5}\,\mathrm{T}$ e nell'emisfero nord ha un polo sud magnetico.
- Il campo magnetico obbedisce al principio di sovrapposizione nel vuoto e nei mezzi lineari.

## 23.2 Forza magnetica

### 23.2.1 Forza di Lorentz

L'evidenza sperimentale mostra che una particella carica in moto in una regione in cui è presente un campo magnetico subisce una forza con caratteristiche molto particolari. Studiando la deflessione di fasci di elettroni (ad esempio in un tubo a raggi catodici avvicinando una calamita) si osserva che: la forza è proporzionale alla carica $q$ e cambia verso se la carica cambia segno; è proporzionale al modulo della velocità $v$; è nulla quando la velocità è parallela alla direzione del campo e massima quando è perpendicolare; è sempre perpendicolare sia alla velocità sia al campo. Tutte queste proprietà sono riassunte dall'espressione vettoriale

$$\vec{F} = q\,\vec{v}\times\vec{B},$$

che prende il nome di **forza di Lorentz** (magnetica). Il suo modulo vale $F = |q|\,v\,B\sin\varphi$, dove $\varphi$ è l'angolo tra $\vec{v}$ e $\vec{B}$; la direzione è perpendicolare al piano individuato dai due vettori e il verso si ottiene con la regola della mano destra per una carica positiva, opposto per una negativa. Questa relazione, letta al contrario, costituisce la **definizione operativa** del campo magnetico: misurando la forza su una carica di prova nota per diverse velocità, si ricavano modulo, direzione e verso di $\vec{B}$.

Quando nella stessa regione sono presenti sia un campo elettrico sia un campo magnetico, la forza totale sulla carica è

$$\vec{F} = q\left(\vec{E} + \vec{v}\times\vec{B}\right),$$

detta **forza di Lorentz generalizzata**. Essa racchiude l'intera interazione elettromagnetica di una carica puntiforme, ed è uno dei pilastri dell'elettromagnetismo classico insieme alle equazioni di Maxwell.

Una conseguenza fondamentale della perpendicolarità tra forza e velocità è che **la forza magnetica non compie lavoro**. Infatti la potenza istantanea è $P = \vec{F}\cdot\vec{v} = q(\vec{v}\times\vec{B})\cdot\vec{v}=0$, perché il prodotto misto con due vettori uguali è nullo. Di conseguenza, per il teorema dell'energia cinetica, un campo magnetico statico non può cambiare il modulo della velocità di una carica, ma solo la sua direzione. Per accelerare particelle (aumentarne l'energia) servono campi elettrici; i campi magnetici servono a curvarne e guidarne la traiettoria. È esattamente questa la divisione dei compiti negli acceleratori di particelle.

### 23.2.2 Moto di cariche

Consideriamo una particella di carica $q$ e massa $m$ che entra con velocità $\vec{v}$ in una regione di campo magnetico uniforme e costante $\vec{B}$, in assenza di altre forze. Scomponiamo la velocità in una componente parallela a $\vec{B}$, $v_\parallel$, e una perpendicolare, $v_\perp$. La componente parallela non dà contributo alla forza e resta quindi costante. La componente perpendicolare subisce una forza di modulo costante $|q|v_\perp B$, sempre ortogonale alla velocità: è la situazione tipica del moto circolare uniforme. Uguagliando la forza di Lorentz alla forza centripeta,

$$|q|\,v_\perp B = m\frac{v_\perp^2}{r}\quad\Rightarrow\quad r = \frac{m v_\perp}{|q| B} = \frac{p_\perp}{|q|B},$$

dove $r$ è il **raggio di Larmor** (o raggio di ciclotrone). Il raggio è proporzionale alla quantità di moto: particelle più veloci o più pesanti descrivono circonferenze più ampie. Il periodo del moto è

$$T = \frac{2\pi r}{v_\perp} = \frac{2\pi m}{|q|B},$$

e la corrispondente pulsazione $\omega_c = |q|B/m$ si chiama **pulsazione di ciclotrone**. Il risultato sorprendente è che il periodo **non dipende dalla velocità**: particelle con la stessa carica specifica $q/m$ compiono un giro nello stesso tempo, indipendentemente dalla loro energia (finché la velocità resta piccola rispetto a quella della luce). Su questo principio si basa il **ciclotrone**, in cui le particelle vengono accelerate da un campo elettrico alternato a frequenza fissa mentre il campo magnetico le fa ruotare in orbite di raggio crescente.

Se entrambe le componenti di velocità sono non nulle, il moto risultante è la composizione di un moto circolare uniforme nel piano perpendicolare a $\vec{B}$ e di un moto rettilineo uniforme lungo $\vec{B}$: la traiettoria è un'**elica cilindrica** con asse parallelo al campo, raggio $r$ e passo $p = v_\parallel T$. Questo moto elicoidale spiega il confinamento delle particelle cariche lungo le linee del campo magnetico terrestre (fasce di Van Allen) e la formazione delle aurore polari, dove le particelle del vento solare, guidate dalle linee di campo, precipitano nell'atmosfera vicino ai poli magnetici.

Il moto in campo magnetico è alla base di strumenti di misura importanti. Nello **spettrometro di massa** ioni di uguale carica e uguale energia vengono fatti entrare in un campo magnetico uniforme: poiché il raggio dipende dalla massa, isotopi diversi colpiscono il rivelatore in punti diversi e possono essere separati. Un'altra applicazione è il **selettore di velocità** (filtro di Wien): un campo elettrico e un campo magnetico perpendicolari tra loro e alla velocità del fascio esercitano forze opposte, che si bilanciano solo per particelle con $v = E/B$; solo queste attraversano il dispositivo senza deviare. Combinando filtro di Wien e spettrometro, J.J. Thomson misurò nel 1897 il rapporto $e/m$ dell'elettrone.

### 23.2.3 Effetto Hall

La forza di Lorentz agisce anche sui portatori di carica che si muovono all'interno di un conduttore. Consideriamo una lastrina conduttrice di larghezza $w$ (lungo $y$) e spessore $d$ (lungo $z$), percorsa da una corrente $I$ lungo $x$, immersa in un campo magnetico $\vec{B}$ diretto lungo $z$. I portatori si muovono con **velocità di deriva** $\vec{v}_d$ e risentono della forza $q\vec{v}_d\times\vec{B}$, diretta lungo $y$. Di conseguenza tendono ad accumularsi su uno dei due bordi laterali della lastrina, mentre sul bordo opposto si crea un difetto di carica. Questa separazione di carica genera un campo elettrico trasversale $\vec{E}_H$, detto **campo di Hall**, che cresce finché la forza elettrica non bilancia esattamente quella magnetica. All'equilibrio, raggiunto in tempi brevissimi,

$$q E_H = q v_d B \quad\Rightarrow\quad E_H = v_d B.$$

Tra i due bordi si misura quindi una differenza di potenziale, la **tensione di Hall**, $V_H = E_H w = v_d B w$. Ricordando che la densità di corrente è $J = n q v_d$, con $n$ densità dei portatori, e che $J = I/(wd)$, si ottiene

$$V_H = \frac{I B}{n q d}.$$

Questa relazione è di straordinaria importanza pratica e concettuale. Dal punto di vista concettuale, il **segno** della tensione di Hall dipende dal segno dei portatori: è grazie all'**effetto Hall** (scoperto da Edwin Hall nel 1879) che si è stabilito che nei metalli la corrente è trasportata da cariche negative, gli elettroni, mentre in alcuni semiconduttori (drogati di tipo p) i portatori si comportano come cariche positive, le lacune. Inoltre la misura di $V_H$ consente di ricavare la densità dei portatori $n$. La quantità $R_H = 1/(nq)$ si chiama **coefficiente di Hall**. Nei metalli $n$ è dell'ordine di $10^{28}$–$10^{29}\,\mathrm{m^{-3}}$ e la tensione di Hall è piccolissima (microvolt), mentre nei semiconduttori, dove $n$ è molto minore, si ottengono tensioni di Hall assai più grandi. Dal punto di vista pratico, poiché a corrente fissata $V_H$ è proporzionale a $B$, una lastrina di semiconduttore costituisce un ottimo sensore di campo magnetico: la **sonda di Hall** è il magnetometro più diffuso in laboratorio ed è presente in innumerevoli dispositivi, dai sensori di posizione nei motori alle bussole elettroniche degli smartphone.

### 23.2.4 Seconda legge elementare di Laplace

Se la forza di Lorentz agisce sui portatori di carica di un conduttore, essa si trasmette, attraverso le interazioni con il reticolo, al conduttore stesso. Ne segue che un filo percorso da corrente immerso in un campo magnetico subisce una forza. Consideriamo un tratto infinitesimo di filo di lunghezza $\mathrm{d}l$ e sezione $\Sigma$, in cui vi sono $n$ portatori per unità di volume, ciascuno con carica $q$ e velocità di deriva $\vec{v}_d$. Il numero di portatori nel tratto è $n\Sigma\,\mathrm{d}l$ e la forza totale è

$$\mathrm{d}\vec{F} = n\Sigma\,\mathrm{d}l\; q\,\vec{v}_d\times\vec{B}.$$

Introducendo il vettore $\mathrm{d}\vec{l}$ orientato come la corrente e ricordando che $I = n q v_d \Sigma$, si ottiene la **seconda legge elementare di Laplace**:

$$\mathrm{d}\vec{F} = I\,\mathrm{d}\vec{l}\times\vec{B}.$$

La forza su un circuito o su un tratto finito di filo si ottiene integrando lungo la linea: $\vec{F}=I\int \mathrm{d}\vec{l}\times\vec{B}$. Nel caso particolare di un tratto rettilineo di lunghezza $L$ in campo uniforme si ha $\vec{F} = I\vec{L}\times\vec{B}$, di modulo $ILB\sin\varphi$. Se il campo è uniforme e il circuito è chiuso, la forza totale è nulla, poiché $\oint \mathrm{d}\vec{l}=0$; tuttavia, come vedremo nella sezione sul dipolo magnetico, può essere non nullo il momento meccanico, ed è proprio su questo che si basano i motori elettrici e gli strumenti a bobina mobile. Per distribuzioni di corrente in volume, la legge si generalizza in $\mathrm{d}\vec{F} = \vec{J}\times\vec{B}\,\mathrm{d}V$.

La seconda legge di Laplace fornisce anche una via sperimentale semplice per misurare $\vec{B}$: la **bilancia di Cotton**, in cui si misura con una bilancia la forza su un tratto orizzontale di filo percorso da corrente nota e immerso nel campo da misurare. Si noti infine che la forza sul filo è dovuta alla forza di Lorentz sui portatori, che non compie lavoro; eppure un motore elettrico compie lavoro meccanico. Il paradosso si risolve osservando che quando il filo si muove, la velocità dei portatori ha anche una componente lungo il moto del filo, e la forza di Lorentz associata frena i portatori, opponendosi alla corrente: è il generatore che mantiene la corrente a fornire l'energia, e il campo magnetico fa solo da intermediario. Riprenderemo questo punto nello studio dell'induzione elettromagnetica.

### Esercizio d'esempio

**Problema.** Un protone ($m = 1{,}67\times10^{-27}\,\mathrm{kg}$, $q = 1{,}60\times10^{-19}\,\mathrm{C}$) accelerato da una differenza di potenziale $\Delta V = 2{,}0\,\mathrm{kV}$ entra perpendicolarmente in un campo magnetico uniforme $B = 0{,}10\,\mathrm{T}$. Calcolare la velocità, il raggio della traiettoria e il periodo di rivoluzione. In una seconda parte, una lastrina di rame ($n = 8{,}5\times10^{28}\,\mathrm{m^{-3}}$) di spessore $d = 0{,}10\,\mathrm{mm}$ è percorsa da $I = 5{,}0\,\mathrm{A}$ nello stesso campo: calcolare la tensione di Hall.

**Soluzione.** Per la conservazione dell'energia $\tfrac12 m v^2 = q\Delta V$, quindi
$$v = \sqrt{\frac{2q\Delta V}{m}} = \sqrt{\frac{2\cdot1{,}60\times10^{-19}\cdot2{,}0\times10^{3}}{1{,}67\times10^{-27}}} \simeq 6{,}2\times10^{5}\,\mathrm{m/s}.$$
Il raggio di Larmor vale
$$r = \frac{mv}{qB} = \frac{1{,}67\times10^{-27}\cdot6{,}2\times10^{5}}{1{,}60\times10^{-19}\cdot0{,}10}\simeq 6{,}5\times10^{-2}\,\mathrm{m}=6{,}5\,\mathrm{cm}.$$
Il periodo, indipendente dalla velocità, è
$$T = \frac{2\pi m}{qB} = \frac{2\pi\cdot1{,}67\times10^{-27}}{1{,}60\times10^{-19}\cdot0{,}10}\simeq 6{,}6\times10^{-7}\,\mathrm{s}.$$
Per la lastrina di rame, i portatori sono elettroni ($|q|=e$):
$$V_H = \frac{IB}{n e d} = \frac{5{,}0\cdot0{,}10}{8{,}5\times10^{28}\cdot1{,}60\times10^{-19}\cdot1{,}0\times10^{-4}}\simeq 3{,}7\times10^{-7}\,\mathrm{V}.$$
La tensione di Hall nel rame è dell'ordine di $0{,}4\,\mu\mathrm{V}$: ecco perché le sonde di Hall si realizzano con semiconduttori, dove $n$ è molto più piccolo.

### Punti chiave

- La forza di Lorentz $\vec{F}=q(\vec{E}+\vec{v}\times\vec{B})$ descrive l'intera interazione elettromagnetica di una carica puntiforme.
- La forza magnetica è perpendicolare alla velocità e non compie lavoro: cambia la direzione ma non il modulo della velocità.
- In campo uniforme una carica descrive una circonferenza di raggio $r=mv_\perp/(|q|B)$, o un'elica se ha componente di velocità lungo $\vec{B}$.
- Il periodo di ciclotrone $T=2\pi m/(|q|B)$ non dipende dalla velocità (in regime non relativistico).
- Nell'effetto Hall la tensione trasversale $V_H = IB/(nqd)$ rivela segno e densità dei portatori e permette di misurare $B$.
- La seconda legge di Laplace $\mathrm{d}\vec{F}=I\,\mathrm{d}\vec{l}\times\vec{B}$ dà la forza su un filo percorso da corrente.
- In campo uniforme la forza netta su un circuito chiuso è nulla, ma il momento meccanico può non esserlo.

## 23.3 Campo magnetico

### 23.3.1 Campo magnetico

Nella sezione precedente abbiamo studiato come un campo magnetico assegnato agisce su cariche e correnti. Ci occupiamo ora del problema inverso: come le correnti generano il campo magnetico. L'esperimento di Ørsted mostra che attorno a un filo rettilineo percorso da corrente un ago magnetico si dispone tangente a circonferenze concentriche con il filo. Le misure quantitative di Biot e Savart (1820) stabilirono che l'intensità del campo prodotto da un filo rettilineo indefinito è direttamente proporzionale alla corrente $I$ e inversamente proporzionale alla distanza $r$ dal filo:

$$B = \frac{\mu_0 I}{2\pi r},$$

relazione nota come **legge di Biot-Savart** per il filo rettilineo. Le linee di campo sono circonferenze giacenti in piani perpendicolari al filo e centrate su di esso; il verso è dato dalla **regola della mano destra**: se il pollice indica il verso della corrente, le dita piegate indicano il verso delle linee di campo.

La costante $\mu_0$ è la **permeabilità magnetica del vuoto**. Nel Sistema Internazionale precedente alla revisione del 2019 il suo valore era fissato per definizione a $\mu_0 = 4\pi\times10^{-7}\,\mathrm{H/m}$ (dove l'henry, H, equivale a $\mathrm{T\,m^2/A}$), come conseguenza della definizione dell'ampere tramite la forza tra fili. Con il nuovo SI, in cui è fissato il valore della carica elementare, $\mu_0$ è diventata una grandezza misurata, il cui valore coincide con $4\pi\times10^{-7}$ entro circa una parte su $10^{10}$, per cui nei calcoli pratici si continua a usare tale valore. Come vedremo nel capitolo successivo, $\mu_0$ è legata alla costante dielettrica del vuoto e alla velocità della luce dalla relazione $\varepsilon_0\mu_0 = 1/c^2$.

È istruttivo notare la struttura della legge di Biot-Savart: il campo decresce come $1/r$, più lentamente del campo di una carica puntiforme ($1/r^2$), esattamente come il campo elettrico di un filo indefinito uniformemente carico. L'analogia non è casuale: in entrambi i casi la sorgente è distribuita lungo una retta infinita. La differenza sta nella direzione del campo: radiale nel caso elettrico, azimutale (tangente alle circonferenze) nel caso magnetico. Questa differenza geometrica è il segno distintivo del magnetismo, legato al prodotto vettoriale presente in tutte le leggi magnetiche.

### 23.3.2 Prima legge elementare di Laplace

Per calcolare il campo prodotto da circuiti di forma arbitraria serve una legge locale, che fornisca il contributo di un singolo elemento di corrente. Laplace, analizzando i dati di Biot e Savart, propose che il tratto infinitesimo $\mathrm{d}\vec{l}$ di un circuito percorso dalla corrente $I$ generi, in un punto $P$ individuato dal vettore $\vec{r}$ che va dall'elemento al punto, il campo

$$\mathrm{d}\vec{B} = \frac{\mu_0}{4\pi}\,\frac{I\,\mathrm{d}\vec{l}\times\hat{r}}{r^2} = \frac{\mu_0}{4\pi}\,\frac{I\,\mathrm{d}\vec{l}\times\vec{r}}{r^3}.$$

Questa è la **prima legge elementare di Laplace** (spesso chiamata anch'essa legge di Biot-Savart in forma differenziale). Il campo elementare è perpendicolare sia a $\mathrm{d}\vec{l}$ sia a $\vec{r}$, decresce come l'inverso del quadrato della distanza e ha modulo $\mathrm{d}B = \frac{\mu_0}{4\pi}\frac{I\,\mathrm{d}l\sin\theta}{r^2}$. Va sottolineato che un elemento di corrente isolato non esiste in magnetostatica, perché la conservazione della carica in regime stazionario impone che le correnti scorrano in circuiti chiusi; la legge elementare ha quindi senso solo una volta integrata su un circuito completo:

$$\vec{B}(P) = \frac{\mu_0 I}{4\pi}\oint \frac{\mathrm{d}\vec{l}\times\hat{r}}{r^2}.$$

Per una carica puntiforme $q$ in moto lento con velocità $\vec{v}$, sostituendo $I\,\mathrm{d}\vec{l}\to q\vec{v}$ si ottiene il campo $\vec{B} = \frac{\mu_0}{4\pi}\frac{q\vec{v}\times\hat{r}}{r^2}$, valido in approssimazione non relativistica.

Applichiamo la legge a due casi fondamentali. Il primo è il **filo rettilineo finito**. Sia $P$ a distanza $R$ dal filo; ogni elemento $\mathrm{d}\vec{l}$ dà un contributo diretto nello stesso verso (azimutale), per cui basta sommare i moduli. Indicando con $\theta$ l'angolo tra $\mathrm{d}\vec{l}$ e $\vec{r}$, si ha $r = R/\sin\theta$ e $l = -R\cot\theta$, quindi $\mathrm{d}l = R\,\mathrm{d}\theta/\sin^2\theta$. Sostituendo,

$$B = \frac{\mu_0 I}{4\pi R}\int_{\theta_1}^{\theta_2}\sin\theta\,\mathrm{d}\theta = \frac{\mu_0 I}{4\pi R}\left(\cos\theta_1-\cos\theta_2\right).$$

Per un filo indefinito $\theta_1\to0$ e $\theta_2\to\pi$, e si ritrova $B=\mu_0 I/(2\pi R)$, a conferma della coerenza tra la legge elementare di Laplace e i risultati sperimentali di Biot e Savart.

Il secondo caso è il **centro di una spira circolare** di raggio $R$. Ogni elemento $\mathrm{d}\vec{l}$ è perpendicolare al raggio vettore diretto verso il centro, la distanza è sempre $R$, e tutti i contributi sono diretti lungo l'asse della spira. Integrando si ottiene immediatamente

$$B = \frac{\mu_0 I}{4\pi R^2}\oint \mathrm{d}l = \frac{\mu_0 I}{2R}.$$

Il campo sull'asse in un punto qualsiasi sarà calcolato nella sezione dedicata al dipolo magnetico. Un **solenoide**, cioè un avvolgimento elicoidale fitto di $N$ spire su una lunghezza $L$, può essere visto come una sovrapposizione di spire: il calcolo (che svolgeremo con il teorema di Ampère) mostra che all'interno di un solenoide lungo il campo è uniforme e vale $B = \mu_0 n I$, con $n=N/L$ numero di spire per unità di lunghezza.

### 23.3.3 Forza tra correnti

Combinando la prima e la seconda legge di Laplace si ottiene la forza che un circuito esercita su un altro. Il caso più semplice e importante è quello di due fili rettilinei indefiniti e paralleli, posti a distanza $d$ e percorsi dalle correnti $I_1$ e $I_2$. Il filo 1 genera, nella posizione del filo 2, il campo $B_1 = \mu_0 I_1/(2\pi d)$, perpendicolare al piano dei due fili. Per la seconda legge di Laplace, un tratto di lunghezza $L$ del filo 2 subisce la forza

$$F = I_2 L B_1 = \frac{\mu_0 I_1 I_2 L}{2\pi d},$$

ossia una forza per unità di lunghezza

$$\frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi d}.$$

Applicando la regola della mano destra si verifica che la forza è attrattiva se le correnti sono equiverse e repulsiva se sono discordi, in accordo con le osservazioni di Ampère. Si noti la differenza con l'elettrostatica, dove cariche dello stesso segno si respingono: qui correnti "dello stesso segno" si attraggono. Per il terzo principio della dinamica, la forza che il filo 2 esercita sul filo 1 è uguale e opposta, come si verifica direttamente scambiando i ruoli dei fili.

Questa relazione ha avuto un ruolo metrologico centrale. Fino al 2019 l'**ampere** era definito proprio così: la corrente costante che, mantenuta in due conduttori rettilinei paralleli, di lunghezza infinita e sezione trascurabile, posti a un metro di distanza nel vuoto, produce tra essi una forza di $2\times10^{-7}$ newton per metro di lunghezza. Sostituendo $I_1=I_2=1\,\mathrm{A}$ e $d=1\,\mathrm{m}$ nella formula si vede che questa definizione equivale a fissare $\mu_0=4\pi\times10^{-7}\,\mathrm{H/m}$. Dal 2019 l'ampere è definito fissando il valore esatto della carica elementare, $e=1{,}602176634\times10^{-19}\,\mathrm{C}$, e la forza tra correnti è diventata uno strumento di misura di $\mu_0$ piuttosto che una definizione.

La forza tra correnti ha conseguenze tecnologiche concrete. Nelle sbarre di distribuzione delle cabine elettriche, durante un cortocircuito possono circolare correnti di decine di migliaia di ampere: le forze elettrodinamiche risultanti sono enormi e i conduttori devono essere ancorati robustamente. Nei solenoidi e nelle bobine ad alto campo le spire, percorse da correnti equiverse, si attraggono tra loro lungo l'asse, mentre la forza radiale tende a far "esplodere" l'avvolgimento verso l'esterno: la progettazione meccanica dei magneti per risonanza o per acceleratori è dominata da questi sforzi. Anche il **pinch effect** nei plasmi, in cui una colonna di plasma percorsa da corrente si contrae per effetto dell'attrazione tra i filetti di corrente paralleli, è una manifestazione dello stesso fenomeno.

Dal punto di vista concettuale, la forza tra correnti è il fenomeno magnetico primario: l'interazione tra magneti permanenti e tra magneti e correnti può essere ricondotta, grazie all'ipotesi delle correnti amperiane microscopiche, all'interazione tra correnti. In questa prospettiva il campo magnetico è l'ente intermedio che trasmette l'azione di una corrente su un'altra, in perfetta analogia con il ruolo del campo elettrico tra cariche.

### Esercizio d'esempio

**Problema.** Due fili rettilinei lunghi e paralleli distano $d = 4{,}0\,\mathrm{cm}$ e sono percorsi da correnti equiverse $I_1 = 10\,\mathrm{A}$ e $I_2 = 20\,\mathrm{A}$. Calcolare: (a) la forza per unità di lunghezza tra i fili; (b) il campo magnetico nel punto medio $M$ del segmento che li congiunge; (c) la posizione del punto, sulla congiungente, in cui il campo totale è nullo.

**Soluzione.** (a) Con $\mu_0 = 4\pi\times10^{-7}\,\mathrm{H/m}$:
$$\frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi d} = \frac{2\times10^{-7}\cdot10\cdot20}{4{,}0\times10^{-2}} = 1{,}0\times10^{-3}\,\mathrm{N/m},$$
attrattiva perché le correnti sono equiverse.

(b) Nel punto medio, a distanza $d/2 = 2{,}0\,\mathrm{cm}$ da ciascun filo, i due campi hanno la stessa direzione ma versi opposti (per la regola della mano destra, tra due fili con correnti equiverse i campi si oppongono). Quindi
$$B_M = \frac{\mu_0}{2\pi (d/2)}(I_2 - I_1) = \frac{2\times10^{-7}}{2{,}0\times10^{-2}}\cdot10 = 1{,}0\times10^{-4}\,\mathrm{T},$$
con il verso del campo generato dal filo 2.

(c) Il campo si annulla tra i fili, a distanza $x$ dal filo 1, quando $\frac{I_1}{x} = \frac{I_2}{d-x}$, ossia
$$x = \frac{I_1 d}{I_1+I_2} = \frac{10\cdot4{,}0}{30}\,\mathrm{cm} \simeq 1{,}3\,\mathrm{cm}.$$
Il punto di campo nullo è più vicino al filo percorso dalla corrente minore.

### Punti chiave

- Un filo rettilineo indefinito genera un campo azimutale $B=\mu_0 I/(2\pi r)$, con verso dato dalla regola della mano destra.
- La prima legge di Laplace $\mathrm{d}\vec{B}=\frac{\mu_0}{4\pi}\frac{I\,\mathrm{d}\vec{l}\times\hat{r}}{r^2}$ permette di calcolare il campo di qualunque circuito, integrandola su circuiti chiusi.
- La permeabilità del vuoto vale $\mu_0\simeq4\pi\times10^{-7}\,\mathrm{H/m}$.
- Al centro di una spira circolare $B=\mu_0 I/(2R)$; in un solenoide lungo $B=\mu_0 n I$.
- Due fili paralleli si attraggono con forza per unità di lunghezza $\mu_0 I_1 I_2/(2\pi d)$ se le correnti sono equiverse, si respingono se sono discordi.
- La forza tra correnti ha definito l'ampere fino al 2019; oggi l'ampere discende dal valore fissato di $e$.

## 23.4 Teorema di Gauss

### 23.4.1 Flusso del campo magnetico

Come per il campo elettrico, anche per il campo magnetico si definisce il **flusso** attraverso una superficie. Data una superficie $S$, orientata scegliendo in ogni punto un versore normale $\hat{n}$, il flusso di $\vec{B}$ attraverso di essa è

$$\Phi_B = \int_S \vec{B}\cdot\hat{n}\,\mathrm{d}S.$$

Se il campo è uniforme e la superficie è piana di area $S$, il flusso si riduce a $\Phi_B = BS\cos\theta$, dove $\theta$ è l'angolo tra il campo e la normale. L'unità di misura del flusso magnetico è il **weber** (Wb), con $1\,\mathrm{Wb} = 1\,\mathrm{T\,m^2}$. Il flusso magnetico ha un'interpretazione geometrica intuitiva: è proporzionale al numero di linee di campo che attraversano la superficie, contate con segno positivo se la attraversano nel verso della normale e negativo nel verso opposto. Per questo motivo il campo magnetico viene talvolta chiamato **densità di flusso magnetico**, e il tesla può essere espresso come $\mathrm{Wb/m^2}$.

Il flusso magnetico è la grandezza protagonista della legge di Faraday-Neumann-Lenz, che studieremo con l'induzione elettromagnetica: una variazione del flusso concatenato con un circuito genera in esso una forza elettromotrice. Questa è una ragione in più per comprenderne a fondo le proprietà già in regime statico.

### 23.4.2 Enunciato e dimostrazione

Il **teorema di Gauss per il campo magnetico** afferma che il flusso del campo magnetico attraverso una qualsiasi superficie chiusa è sempre nullo:

$$\oint_S \vec{B}\cdot\hat{n}\,\mathrm{d}S = 0.$$

Il confronto con il teorema di Gauss per il campo elettrico, $\oint_S\vec{E}\cdot\hat{n}\,\mathrm{d}S = Q_{int}/\varepsilon_0$, è illuminante. Il flusso elettrico uscente da una superficie chiusa è proporzionale alla carica contenuta, perché le linee del campo elettrico nascono e muoiono sulle cariche. Nel caso magnetico il secondo membro è sempre zero perché non esistono "cariche magnetiche" su cui le linee possano iniziare o terminare: ogni linea che entra in una superficie chiusa deve necessariamente uscirne, e il conteggio con segno dà zero.

Una giustificazione formale si ottiene a partire dalla prima legge di Laplace. Consideriamo il campo generato da un singolo elemento di corrente $I\,\mathrm{d}\vec{l}$ posto nell'origine e diretto lungo l'asse $z$. Le sue linee di campo sono circonferenze coassiali con l'asse $z$, e il modulo del campo è costante su ciascuna di esse. Possiamo pensare lo spazio come riempito da sottili "tubi di flusso" toroidali, ciascuno dei quali è una linea chiusa: un tubo che entra in una superficie chiusa deve uscirne trasportando lo stesso flusso, perché lungo un tubo di flusso sottile, con campo tangente alla parete, il flusso attraverso ogni sezione è lo stesso. Il contributo netto di ogni tubo al flusso totale è nullo e, per il principio di sovrapposizione, lo stesso vale per il campo di un circuito qualsiasi, somma dei contributi dei suoi elementi. Una dimostrazione più elegante si ottiene in forma differenziale verificando che la divergenza del campo di Laplace è identicamente nulla, come mostreremo nella sezione 23.7.

È importante sottolineare che il teorema di Gauss magnetico non è una conseguenza specifica della magnetostatica: esso vale anche per campi magnetici variabili nel tempo e costituisce una delle quattro equazioni di Maxwell. La sua validità generale si fonda sul fatto sperimentale dell'assenza di monopoli magnetici.

### 23.4.3 Conseguenze: flusso concatenato

Una conseguenza immediata del teorema è che il flusso del campo magnetico attraverso una superficie aperta dipende solo dal suo contorno e non dalla particolare superficie scelta. Siano $S_1$ e $S_2$ due superfici aperte che hanno lo stesso bordo $\gamma$, orientate coerentemente con il verso di percorrenza di $\gamma$. Insieme esse formano una superficie chiusa, e la normale uscente coincide con quella di $S_1$ e con l'opposta di quella di $S_2$ (o viceversa). Applicando il teorema:

$$\int_{S_1}\vec{B}\cdot\hat{n}_1\,\mathrm{d}S - \int_{S_2}\vec{B}\cdot\hat{n}_2\,\mathrm{d}S = 0 \quad\Rightarrow\quad \Phi_{S_1} = \Phi_{S_2}.$$

Ha quindi senso parlare di **flusso concatenato** con una linea chiusa $\gamma$, o con un circuito, senza specificare la superficie: qualunque superficie che "si appoggi" sul circuito dà lo stesso risultato. Questa proprietà è essenziale per la legge dell'induzione e per la definizione del coefficiente di autoinduzione $L=\Phi/I$, che sarebbero ambigue se il flusso dipendesse dalla superficie. In termini matematici, un campo a divergenza nulla (detto **solenoidale**) può essere scritto come rotore di un altro campo, il **potenziale vettore** $\vec{A}$, con $\vec{B}=\nabla\times\vec{A}$, e il flusso attraverso una superficie è pari alla circuitazione di $\vec{A}$ lungo il bordo, che chiaramente dipende solo dal bordo.

Un'altra conseguenza riguarda i **tubi di flusso**. Consideriamo un fascio di linee di campo che attraversa una superficie $S_1$ e, più avanti, una superficie $S_2$; la superficie laterale del tubo è formata da linee di campo, quindi il flusso attraverso di essa è nullo. Il teorema impone allora che il flusso attraverso $S_1$ sia uguale a quello attraverso $S_2$: dove il tubo si restringe, il campo si intensifica. È il motivo per cui le linee si addensano vicino ai poli di un magnete, e per cui nei circuiti magnetici con nuclei di ferro di sezione variabile il campo è più intenso dove la sezione è minore. Il flusso nel campo magnetico si comporta in modo analogo alla portata di un fluido incomprimibile in un condotto.

### 23.4.4 Monopoli magnetici

Il teorema di Gauss magnetico esprime, in definitiva, l'assenza di **monopoli magnetici**. Se esistesse una carica magnetica $q_m$, essa sarebbe sorgente di un campo radiale e il teorema andrebbe modificato in $\oint\vec{B}\cdot\hat{n}\,\mathrm{d}S = \mu_0 q_m$. Non c'è alcun principio fondamentale che vieti l'esistenza dei monopoli; anzi, nel 1931 Dirac dimostrò che, se in natura esistesse anche un solo monopolo, la meccanica quantistica imporrebbe la quantizzazione della carica elettrica, fatto osservato sperimentalmente ma altrimenti non spiegato. Diverse teorie di grande unificazione prevedono l'esistenza di monopoli molto massivi prodotti nell'universo primordiale.

Numerosi esperimenti hanno cercato i monopoli: nei raggi cosmici, nelle rocce lunari, negli acceleratori di particelle (come l'esperimento MoEDAL al CERN). Un metodo particolarmente sensibile sfrutta una bobina superconduttrice: il passaggio di un monopolo attraverso la spira produrrebbe un salto discreto della corrente persistente, ben distinguibile da altri segnali. A oggi nessuna osservazione è stata confermata, e il teorema di Gauss nella forma $\oint\vec{B}\cdot\hat{n}\,\mathrm{d}S=0$ è considerato valido con elevatissima precisione. Va detto che in alcuni materiali (i cosiddetti "spin ice") si osservano eccitazioni collettive che si comportano come monopoli magnetici efficaci; si tratta però di quasi-particelle emergenti nel campo di magnetizzazione del materiale, che non violano la legge di Gauss per il campo $\vec{B}$ fondamentale.

### Esercizio d'esempio

**Problema.** Un campo magnetico uniforme $\vec{B} = (0{,}20\,\hat{x} + 0{,}50\,\hat{z})\,\mathrm{T}$ attraversa una semisfera di raggio $R = 10\,\mathrm{cm}$ con la base circolare nel piano $xy$ e centrata nell'origine, con la calotta nel semispazio $z>0$. Calcolare il flusso attraverso la calotta (normale uscente) e verificare il teorema di Gauss.

**Soluzione.** La superficie chiusa è formata dalla calotta $S_c$ e dal disco di base $S_d$. Per il disco, la normale uscente dalla semisfera è $-\hat{z}$:
$$\Phi_d = \vec{B}\cdot(-\hat{z})\,\pi R^2 = -0{,}50\cdot\pi\cdot(0{,}10)^2 \simeq -1{,}57\times10^{-2}\,\mathrm{Wb}.$$
Per il teorema di Gauss il flusso totale è nullo, quindi
$$\Phi_c = -\Phi_d \simeq +1{,}57\times10^{-2}\,\mathrm{Wb}.$$
Possiamo verificarlo osservando che la componente $B_x$ entra nella calotta dal lato $x<0$ ed esce dal lato $x>0$ in modo simmetrico, dando contributo netto nullo, mentre la componente $B_z$ attraversa la calotta con lo stesso flusso che attraversa il disco, cioè $B_z\pi R^2$. Il risultato conferma che il flusso dipende solo dal bordo (la circonferenza di raggio $R$), e non dalla superficie (calotta o disco) che vi si appoggia.

### Punti chiave

- Il flusso magnetico $\Phi_B=\int_S\vec{B}\cdot\hat{n}\,\mathrm{d}S$ si misura in weber, $1\,\mathrm{Wb}=1\,\mathrm{T\,m^2}$.
- Teorema di Gauss: il flusso di $\vec{B}$ attraverso qualunque superficie chiusa è nullo.
- Il teorema esprime l'assenza di monopoli magnetici e la chiusura delle linee di campo.
- Il flusso attraverso una superficie aperta dipende solo dal suo bordo: si parla di flusso concatenato con un circuito.
- Lungo un tubo di flusso il flusso è costante: dove il tubo si restringe il campo si intensifica.
- Il teorema vale anche per campi variabili nel tempo ed è una delle equazioni di Maxwell.
- I monopoli magnetici sono stati cercati a lungo ma mai osservati.

## 23.5 Teorema di Ampère

Il teorema di Gauss caratterizza il comportamento del flusso di $\vec{B}$; per determinare completamente un campo vettoriale occorre però conoscere anche la sua **circuitazione**, cioè l'integrale di linea lungo un percorso chiuso. Nel caso elettrostatico la circuitazione di $\vec{E}$ è sempre nulla, e ciò permette di introdurre il potenziale. Nel caso magnetico la situazione è radicalmente diversa: le linee di $\vec{B}$ sono chiuse, e percorrendo una di esse nel verso del campo l'integrale $\oint\vec{B}\cdot\mathrm{d}\vec{l}$ è certamente positivo. Il teorema di Ampère quantifica questa circuitazione e la lega alle correnti che la generano.

### 23.5.1 Linea circolare

Partiamo dal caso più semplice: un filo rettilineo indefinito percorso dalla corrente $I$ e una linea chiusa $\gamma$ costituita da una circonferenza di raggio $r$, giacente in un piano perpendicolare al filo e centrata su di esso. Lungo tutta la circonferenza il campo ha modulo costante $B = \mu_0 I/(2\pi r)$ ed è tangente alla linea. Scegliendo il verso di percorrenza concorde con quello delle linee di campo (cioè legato al verso della corrente dalla regola della mano destra), si ha $\vec{B}\cdot\mathrm{d}\vec{l} = B\,\mathrm{d}l$ e quindi

$$\oint_\gamma \vec{B}\cdot\mathrm{d}\vec{l} = B\oint_\gamma\mathrm{d}l = \frac{\mu_0 I}{2\pi r}\,2\pi r = \mu_0 I.$$

Il risultato è notevole: la circuitazione non dipende dal raggio della circonferenza. La dipendenza $1/r$ del campo compensa esattamente la crescita $r$ della lunghezza del percorso. Se la circonferenza viene percorsa nel verso opposto, la circuitazione cambia segno e vale $-\mu_0 I$. Se invece la circonferenza non circonda il filo, ad esempio perché è spostata lateralmente, ci si aspetta un risultato diverso: come vedremo subito, in tal caso la circuitazione è nulla.

Consideriamo ora una linea chiusa piana qualsiasi, giacente in un piano perpendicolare al filo. Scomponiamo lo spostamento elementare $\mathrm{d}\vec{l}$ in una componente radiale e una azimutale. Il campo è puramente azimutale, quindi solo la seconda contribuisce: $\vec{B}\cdot\mathrm{d}\vec{l} = B\,r\,\mathrm{d}\phi$, dove $\mathrm{d}\phi$ è l'angolo sotto cui l'elemento di linea è visto dal filo. Sostituendo l'espressione del campo,

$$\vec{B}\cdot\mathrm{d}\vec{l} = \frac{\mu_0 I}{2\pi r}\,r\,\mathrm{d}\phi = \frac{\mu_0 I}{2\pi}\,\mathrm{d}\phi.$$

La circuitazione si riduce dunque a $\frac{\mu_0 I}{2\pi}\oint\mathrm{d}\phi$, e l'integrale dell'angolo dipende solo dalla topologia: se la linea circonda il filo una volta, l'angolo totale spazzato è $2\pi$ e si ritrova $\mu_0 I$; se la linea non circonda il filo, l'angolo prima aumenta e poi diminuisce tornando al valore iniziale, e l'integrale è zero; se la linea si avvolge $N$ volte attorno al filo, la circuitazione vale $N\mu_0 I$. Il campo magnetico non è dunque conservativo, ma ha una struttura "quasi conservativa": la circuitazione dipende solo da quante volte il percorso si avvolge attorno alle correnti.

### 23.5.2 Linea generica

L'argomento precedente si estende a linee non piane (la componente di $\mathrm{d}\vec{l}$ parallela al filo non contribuisce, essendo perpendicolare al campo) e, per sovrapposizione, a un numero qualsiasi di fili. Un risultato più generale, che si può dimostrare a partire dalla prima legge di Laplace per circuiti di forma arbitraria, costituisce il **teorema di Ampère** (o **legge della circuitazione di Ampère**):

$$\oint_\gamma \vec{B}\cdot\mathrm{d}\vec{l} = \mu_0\,I_{conc},$$

dove $I_{conc}$ è la somma algebrica delle correnti **concatenate** con la linea chiusa $\gamma$, cioè delle correnti che attraversano una qualsiasi superficie $S$ che abbia $\gamma$ come bordo. Ogni corrente si conta con segno positivo se attraversa $S$ nel verso della normale associata al verso di percorrenza di $\gamma$ tramite la regola della mano destra, e con segno negativo altrimenti. In presenza di una distribuzione di corrente con densità $\vec{J}$, si scrive

$$\oint_\gamma \vec{B}\cdot\mathrm{d}\vec{l} = \mu_0\int_S\vec{J}\cdot\hat{n}\,\mathrm{d}S.$$

Va sottolineato che il campo $\vec{B}$ che compare nell'integrale è il campo **totale**, prodotto da tutte le correnti, anche da quelle non concatenate; queste ultime però danno contributo nullo alla circuitazione. Inoltre il teorema, in questa forma, vale solo per **correnti stazionarie**: la condizione che il risultato non dipenda dalla superficie $S$ scelta richiede che il flusso di $\vec{J}$ attraverso una superficie chiusa sia nullo, cioè che non vi sia accumulo di carica. Quando le correnti variano nel tempo (ad esempio durante la carica di un condensatore) questa condizione viene meno, e Maxwell dovette correggere la legge aggiungendo la **corrente di spostamento**, come vedremo nel capitolo 24.

Il teorema di Ampère gioca in magnetostatica lo stesso ruolo del teorema di Gauss in elettrostatica: è sempre vero, ma è utile per il calcolo esplicito del campo solo in situazioni di elevata simmetria, in cui si può scegliere una linea lungo la quale $\vec{B}$ abbia modulo costante e sia tangente, oppure perpendicolare. Vediamo i casi classici.

**Conduttore cilindrico pieno.** Un filo cilindrico di raggio $a$ è percorso dalla corrente $I$ distribuita uniformemente sulla sezione, con densità $J = I/(\pi a^2)$. Per simmetria le linee di campo sono circonferenze coassiali. All'esterno ($r>a$) la linea circolare concatena tutta la corrente e si ritrova $B = \mu_0 I/(2\pi r)$: il filo spesso si comporta come un filo sottile. All'interno ($r<a$) la corrente concatenata è $I r^2/a^2$, quindi

$$B\,2\pi r = \mu_0 I\frac{r^2}{a^2}\quad\Rightarrow\quad B = \frac{\mu_0 I r}{2\pi a^2}.$$

Il campo cresce linearmente dal centro fino alla superficie, dove raggiunge il massimo, e poi decresce come $1/r$. Per un conduttore cilindrico cavo (o per lo schermo di un **cavo coassiale**) il campo nella cavità è nullo, e all'esterno di un cavo coassiale con correnti uguali e opposte nei due conduttori il campo è nullo: è uno dei motivi per cui il cavo coassiale non irradia né risente di disturbi esterni.

**Solenoide ideale.** Un solenoide lungo, con $n$ spire per unità di lunghezza percorse dalla corrente $I$, ha all'esterno un campo trascurabile e all'interno un campo parallelo all'asse. Si sceglie come linea un rettangolo con un lato di lunghezza $h$ all'interno, parallelo all'asse, e il lato opposto all'esterno. I lati perpendicolari all'asse non contribuiscono (campo perpendicolare al percorso all'interno, nullo all'esterno), il lato esterno non contribuisce, e la corrente concatenata è $nhI$. Quindi $Bh = \mu_0 nhI$, ossia

$$B = \mu_0 n I,$$

indipendente dalla posizione all'interno: il campo di un solenoide ideale è **uniforme**. Per questo i solenoidi sono il modo standard per produrre campi magnetici uniformi in laboratorio.

**Toroide.** Un avvolgimento di $N$ spire su un anello toroidale produce linee di campo circolari interne all'anello. Prendendo come linea una circonferenza di raggio $r$ interna al toroide, si ha $B\,2\pi r = \mu_0 N I$, cioè $B = \mu_0 NI/(2\pi r)$. Fuori dal toroide la corrente concatenata è nulla (o doppia e di segno opposto) e il campo è nullo: il toroide confina completamente il campo, proprietà sfruttata in trasformatori e induttori a basso disturbo, e anche, a scala gigantesca, nei reattori a fusione di tipo tokamak.

### Esercizio d'esempio

**Problema.** Un cavo coassiale è formato da un conduttore interno pieno di raggio $a = 1{,}0\,\mathrm{mm}$ e da un conduttore esterno cilindrico sottile di raggio $b = 4{,}0\,\mathrm{mm}$. Nel conduttore interno scorre $I = 3{,}0\,\mathrm{A}$, uniformemente distribuita, e nel conduttore esterno la stessa corrente in verso opposto. Calcolare il campo a $r_1 = 0{,}50\,\mathrm{mm}$, $r_2 = 2{,}0\,\mathrm{mm}$, $r_3 = 6{,}0\,\mathrm{mm}$.

**Soluzione.** Per simmetria cilindrica applichiamo il teorema di Ampère a circonferenze coassiali di raggio $r$: $B\,2\pi r = \mu_0 I_{conc}(r)$.

Per $r_1<a$: $I_{conc} = I r_1^2/a^2$, quindi
$$B_1 = \frac{\mu_0 I r_1}{2\pi a^2} = \frac{2\times10^{-7}\cdot3{,}0\cdot5{,}0\times10^{-4}}{(1{,}0\times10^{-3})^2} = 3{,}0\times10^{-4}\,\mathrm{T}.$$
Per $a<r_2<b$: $I_{conc} = I$, quindi
$$B_2 = \frac{\mu_0 I}{2\pi r_2} = \frac{2\times10^{-7}\cdot3{,}0}{2{,}0\times10^{-3}} = 3{,}0\times10^{-4}\,\mathrm{T}.$$
Per $r_3>b$: $I_{conc} = I - I = 0$, quindi $B_3 = 0$.

Il campo è confinato tra i due conduttori; il valore massimo, sulla superficie del conduttore interno, è $\mu_0 I/(2\pi a) = 6{,}0\times10^{-4}\,\mathrm{T}$.

### Punti chiave

- Teorema di Ampère: $\oint_\gamma\vec{B}\cdot\mathrm{d}\vec{l}=\mu_0 I_{conc}$, con le correnti concatenate contate con il segno dato dalla regola della mano destra.
- La circuitazione di $\vec{B}$ dipende solo dalla topologia del percorso rispetto alle correnti, non dalla sua forma: il campo magnetico non è conservativo.
- Nell'integrale compare il campo totale, ma solo le correnti concatenate contribuiscono.
- Nella forma magnetostatica il teorema vale solo per correnti stazionarie; Maxwell lo generalizza con la corrente di spostamento.
- Il teorema è utile per calcolare $\vec{B}$ in casi molto simmetrici: filo cilindrico, cavo coassiale, solenoide ($B=\mu_0 nI$), toroide ($B=\mu_0 NI/(2\pi r)$).
- In un conduttore cilindrico pieno il campo cresce linearmente all'interno e decresce come $1/r$ all'esterno.

## 23.6 Dipolo magnetico

### 23.6.1 Dipolo magnetico

Abbiamo visto che le linee del campo di una calamita a sbarra ricordano molto, a grande distanza, quelle di un dipolo elettrico; e che una spira percorsa da corrente produce un campo con la stessa struttura. Questa analogia suggerisce di introdurre una grandezza che caratterizzi i piccoli circuiti chiusi, il **momento magnetico** (o **momento di dipolo magnetico**). Per una spira piana di area $S$ percorsa dalla corrente $I$ si definisce

$$\vec{m} = I\,S\,\hat{n},$$

dove $\hat{n}$ è il versore normale alla spira, orientato secondo la regola della mano destra rispetto al verso della corrente. L'unità di misura è $\mathrm{A\,m^2}$ (equivalente a $\mathrm{J/T}$). Per una bobina di $N$ spire il momento si moltiplica per $N$.

Si chiama **dipolo magnetico** un circuito le cui dimensioni sono piccole rispetto alla distanza alla quale si osserva il campo. In tali condizioni il campo prodotto dipende solo da $\vec{m}$ e non dalla forma della spira, e ha la stessa espressione del campo di un dipolo elettrico con la sostituzione $\vec{p}/\varepsilon_0\to\mu_0\vec{m}$:

$$\vec{B}(\vec{r}) = \frac{\mu_0}{4\pi}\,\frac{3(\vec{m}\cdot\hat{r})\hat{r} - \vec{m}}{r^3}.$$

Il campo decresce come $1/r^3$; sull'asse del dipolo vale $\mu_0 m/(2\pi r^3)$ ed è parallelo a $\vec{m}$, nel piano equatoriale vale $\mu_0 m/(4\pi r^3)$ ed è antiparallelo. L'analogia con il dipolo elettrico vale anche per il comportamento in un campo esterno uniforme $\vec{B}$: il dipolo non subisce forza netta, ma è soggetto a un **momento meccanico**

$$\vec{M} = \vec{m}\times\vec{B},$$

che tende ad allinearlo al campo. All'orientazione del dipolo si associa un'**energia potenziale**

$$U = -\vec{m}\cdot\vec{B},$$

minima quando $\vec{m}$ è parallelo a $\vec{B}$ (equilibrio stabile) e massima quando è antiparallelo (equilibrio instabile). È così che si spiega il comportamento dell'ago della bussola, che è proprio un dipolo magnetico. In un campo non uniforme compare anche una forza netta $\vec{F}=\nabla(\vec{m}\cdot\vec{B})$, che spinge il dipolo allineato verso le regioni di campo più intenso: è la ragione per cui una calamita attrae un chiodo di ferro, che si magnetizza allineandosi al campo e viene poi trascinato dove il campo è più forte. La stessa forza è alla base dell'esperimento di Stern e Gerlach.

### 23.6.2 Spira circolare

Calcoliamo con la prima legge di Laplace il campo sull'asse di una spira circolare di raggio $R$ percorsa dalla corrente $I$, in un punto $P$ a distanza $z$ dal centro. Ogni elemento $\mathrm{d}\vec{l}$ dista $r=\sqrt{R^2+z^2}$ da $P$ ed è perpendicolare al vettore $\vec{r}$, quindi $|\mathrm{d}\vec{l}\times\hat{r}| = \mathrm{d}l$. Il campo elementare $\mathrm{d}\vec{B}$ è perpendicolare a $\vec{r}$ e forma con l'asse un angolo il cui coseno è $R/r$. Per simmetria, sommando su tutta la spira le componenti perpendicolari all'asse si annullano a coppie, mentre le componenti assiali si sommano:

$$B_z = \oint\frac{\mu_0 I\,\mathrm{d}l}{4\pi r^2}\frac{R}{r} = \frac{\mu_0 I R}{4\pi r^3}\,2\pi R = \frac{\mu_0 I R^2}{2(R^2+z^2)^{3/2}}.$$

Per $z=0$ si ritrova il campo al centro, $\mu_0 I/(2R)$. Per $z\gg R$ il campo diventa

$$B_z\simeq\frac{\mu_0 I R^2}{2z^3} = \frac{\mu_0}{2\pi}\frac{I\pi R^2}{z^3} = \frac{\mu_0}{2\pi}\frac{m}{z^3},$$

che coincide con il campo sull'asse del dipolo magnetico con $m = I\pi R^2$. Questo verifica, in un caso concreto, che a grande distanza una spira si comporta come un dipolo. La spira circolare è il mattone di molti dispositivi: due spire coassiali di raggio $R$ poste a distanza $R$ costituiscono le **bobine di Helmholtz**, che producono nella regione centrale un campo molto uniforme, perché in quel punto si annulla anche la derivata seconda del campo rispetto a $z$.

### 23.6.3 Spira rettangolare

Studiamo ora il comportamento di una spira rettangolare rigida di lati $a$ e $b$, percorsa dalla corrente $I$, in un campo magnetico uniforme $\vec{B}$. Supponiamo che la spira possa ruotare attorno a un asse passante per il centro e parallelo ai lati di lunghezza $a$, e che $\vec{B}$ sia perpendicolare a tale asse; sia $\theta$ l'angolo tra la normale $\hat{n}$ alla spira e il campo. Per la seconda legge di Laplace:

- sui due lati di lunghezza $b$ (perpendicolari all'asse di rotazione) agiscono forze uguali e opposte, dirette lungo l'asse di rotazione, che si annullano e non producono momento;
- sui due lati di lunghezza $a$, perpendicolari a $\vec{B}$, agiscono forze di modulo $F = IaB$, uguali e opposte, ma con rette d'azione distanti $b\sin\theta$: esse formano una **coppia**.

La forza totale è quindi nulla, come per ogni circuito chiuso in campo uniforme, ma il momento della coppia vale

$$M = F\,b\sin\theta = I\,a\,b\,B\sin\theta = m B\sin\theta,$$

con $m = Iab$. In forma vettoriale si ritrova $\vec{M} = \vec{m}\times\vec{B}$, confermando la validità generale della relazione per qualunque spira piana. Il momento tende a ruotare la spira fino a portare $\vec{m}$ parallelo a $\vec{B}$. Questo principio è alla base del **motore elettrico in corrente continua**: un **commutatore** inverte il verso della corrente ogni mezzo giro, in modo che il momento abbia sempre lo stesso verso e la bobina ruoti continuamente. Lo stesso principio è usato nel **galvanometro a bobina mobile**, in cui il momento magnetico, proporzionale alla corrente, è bilanciato dal momento elastico di una molla: la deflessione dell'indice è proporzionale alla corrente da misurare.

### 23.6.4 Teorema di equivalenza di Ampère

L'identità tra il campo lontano di una spira e quello di un dipolo, e tra il comportamento di una spira e quello di un ago magnetico in un campo esterno, è espressa dal **teorema di equivalenza di Ampère**: una spira piccola percorsa dalla corrente $I$ è equivalente, sia per il campo che produce sia per le azioni che subisce, a un dipolo magnetico di momento $\vec{m}=IS\hat{n}$. Il teorema si estende a circuiti di forma e dimensioni qualunque: un circuito qualsiasi può essere suddiviso, tramite una rete di maglie fittissime, in tante spire elementari percorse dalla stessa corrente; le correnti sui lati interni comuni a due maglie si cancellano, e rimane solo la corrente sul bordo. Ogni spira elementare equivale a un piccolo dipolo, e il circuito intero equivale a una **lamina magnetica**, cioè a una superficie appoggiata sul circuito e uniformemente ricoperta di dipoli magnetici perpendicolari a essa, con momento per unità di superficie pari a $I$.

Il significato fisico del teorema va oltre l'aspetto calcolistico. Ampère ne trasse l'ipotesi che i magneti permanenti contengano **correnti microscopiche** (oggi dette **correnti amperiane**) circolanti attorno a ciascuna molecola, ognuna equivalente a un piccolo dipolo. In un materiale non magnetizzato i dipoli sono orientati a caso; in un magnete sono allineati. All'interno del materiale le correnti di molecole adiacenti si compensano, ma sulla superficie laterale rimane una corrente netta, esattamente come nell'argomento delle maglie: una sbarra uniformemente magnetizzata equivale a un solenoide. Questo spiega l'inseparabilità dei poli (spezzando un solenoide si ottengono due solenoidi) e la chiusura delle linee di campo attraverso il magnete. L'ipotesi di Ampère, formulata quasi un secolo prima della scoperta dell'elettrone, fu pienamente confermata dalla fisica atomica.

### 23.6.5 Magnetone di Bohr

Applichiamo le idee precedenti al modello classico dell'atomo di idrogeno, in cui un elettrone di carica $-e$ e massa $m_e$ percorre un'orbita circolare di raggio $r$ con velocità $v$. Il moto periodico equivale a una corrente $I = e/T = ev/(2\pi r)$, che circola in verso opposto a quello dell'elettrone. Il momento magnetico orbitale ha modulo

$$m = I\pi r^2 = \frac{ev}{2\pi r}\pi r^2 = \frac{evr}{2}.$$

Ricordando che il momento angolare orbitale è $L = m_e v r$, si ottiene una relazione che non dipende dai dettagli dell'orbita:

$$\vec{m} = -\frac{e}{2m_e}\vec{L}.$$

Il rapporto $e/(2m_e)$ si chiama **rapporto giromagnetico** orbitale; il segno meno indica che, per la carica negativa dell'elettrone, momento magnetico e momento angolare sono antiparalleli. Nel modello di Bohr il momento angolare è quantizzato in multipli di $\hbar = h/(2\pi)$; per $L=\hbar$ si ottiene l'unità naturale del momento magnetico atomico, il **magnetone di Bohr**:

$$\mu_B = \frac{e\hbar}{2m_e} \simeq 9{,}27\times10^{-24}\,\mathrm{J/T}.$$

L'elettrone possiede inoltre un momento angolare intrinseco, lo **spin**, di modulo (proiezione) $\hbar/2$, a cui è associato un momento magnetico pari, con ottima approssimazione, a un magnetone di Bohr: il rapporto giromagnetico di spin è circa il doppio di quello orbitale (fattore $g\simeq2$, previsto dall'equazione di Dirac). Il magnetismo della materia ha origine proprio dalla somma dei momenti orbitali e di spin degli elettroni. Nei materiali ferromagnetici, come il ferro, le interazioni quantistiche di scambio allineano spontaneamente gli spin di un gran numero di atomi in regioni dette domini, dando origine ai magneti permanenti. La stima classica illustra bene l'ordine di grandezza: se tutti gli atomi di un cubetto di ferro di $1\,\mathrm{cm^3}$ (circa $8{,}5\times10^{22}$ atomi) contribuissero con circa $2\,\mu_B$ ciascuno, il momento magnetico totale sarebbe circa $1{,}6\,\mathrm{A\,m^2}$, equivalente a quello di una spira di $1\,\mathrm{cm^2}$ percorsa da $16\,000\,\mathrm{A}$.

### Esercizio d'esempio

**Problema.** Una bobina rettangolare di $N = 100$ spire, con lati $a = 4{,}0\,\mathrm{cm}$ e $b = 2{,}5\,\mathrm{cm}$, è percorsa da $I = 0{,}50\,\mathrm{A}$ ed è immersa in un campo uniforme $B = 0{,}20\,\mathrm{T}$. Calcolare il momento magnetico, il momento meccanico massimo e il lavoro necessario per ruotare la bobina dalla posizione di equilibrio stabile a quella di equilibrio instabile. Calcolare infine il campo sull'asse di una spira circolare di raggio $R=5{,}0\,\mathrm{cm}$ con $I=0{,}50\,\mathrm{A}$, a distanza $z = 5{,}0\,\mathrm{cm}$ dal centro.

**Soluzione.** Il momento magnetico è
$$m = NIab = 100\cdot0{,}50\cdot4{,}0\times10^{-2}\cdot2{,}5\times10^{-2} = 5{,}0\times10^{-2}\,\mathrm{A\,m^2}.$$
Il momento meccanico è massimo per $\theta = 90^\circ$:
$$M_{max} = mB = 5{,}0\times10^{-2}\cdot0{,}20 = 1{,}0\times10^{-2}\,\mathrm{N\,m}.$$
Il lavoro esterno per passare da $\theta=0$ a $\theta=\pi$ è pari alla variazione di energia potenziale:
$$W = U(\pi)-U(0) = mB-(-mB) = 2mB = 2{,}0\times10^{-2}\,\mathrm{J}.$$
Per la spira circolare:
$$B_z = \frac{\mu_0 I R^2}{2(R^2+z^2)^{3/2}} = \frac{4\pi\times10^{-7}\cdot0{,}50\cdot(5{,}0\times10^{-2})^2}{2\,(2\cdot(5{,}0\times10^{-2})^2)^{3/2}} \simeq \frac{1{,}57\times10^{-9}}{2\cdot3{,}54\times10^{-4}}\simeq 2{,}2\times10^{-6}\,\mathrm{T}.$$

### Punti chiave

- Il momento magnetico di una spira è $\vec{m}=IS\hat{n}$, con $\hat{n}$ dato dalla regola della mano destra; si misura in $\mathrm{A\,m^2}$.
- A grande distanza ogni piccolo circuito produce un campo di dipolo, che decresce come $1/r^3$.
- In campo uniforme un dipolo subisce il momento $\vec{M}=\vec{m}\times\vec{B}$ e ha energia $U=-\vec{m}\cdot\vec{B}$; in campo non uniforme subisce anche una forza.
- Sull'asse di una spira circolare $B=\mu_0IR^2/[2(R^2+z^2)^{3/2}]$.
- Il momento sulla spira rettangolare è il principio del motore in corrente continua e del galvanometro.
- Teorema di equivalenza di Ampère: ogni circuito equivale a una lamina magnetica; i magneti equivalgono a correnti amperiane.
- Il magnetone di Bohr $\mu_B=e\hbar/(2m_e)\simeq9{,}27\times10^{-24}\,\mathrm{J/T}$ è l'unità naturale dei momenti magnetici atomici.

## 23.7 Formulazione differenziale

Le leggi di Gauss e di Ampère, nella forma integrale vista finora, esprimono proprietà globali del campo: flusso attraverso superfici chiuse e circuitazione lungo linee chiuse. Per molti scopi, sia teorici sia applicativi, è preferibile una formulazione **locale**, che leghi il campo in un punto alle sorgenti in quello stesso punto. Il passaggio si ottiene con i due teoremi fondamentali del calcolo vettoriale. Il **teorema della divergenza** (di Gauss-Ostrogradskij) afferma che il flusso di un campo vettoriale attraverso una superficie chiusa è uguale all'integrale della sua divergenza sul volume racchiuso: $\oint_S\vec{B}\cdot\hat{n}\,\mathrm{d}S=\int_V\nabla\cdot\vec{B}\,\mathrm{d}V$. Il **teorema del rotore** (di Stokes) afferma che la circuitazione lungo una linea chiusa è uguale al flusso del rotore attraverso una qualsiasi superficie che ha la linea come bordo: $\oint_\gamma\vec{B}\cdot\mathrm{d}\vec{l}=\int_S(\nabla\times\vec{B})\cdot\hat{n}\,\mathrm{d}S$.

Applicando il teorema della divergenza alla legge di Gauss magnetica si ottiene $\int_V\nabla\cdot\vec{B}\,\mathrm{d}V=0$ per ogni volume $V$; poiché il volume è arbitrario, l'integrando deve essere nullo ovunque:

$$\nabla\cdot\vec{B} = 0.$$

Analogamente, applicando il teorema di Stokes alla legge di Ampère, si ha $\int_S(\nabla\times\vec{B})\cdot\hat{n}\,\mathrm{d}S = \mu_0\int_S\vec{J}\cdot\hat{n}\,\mathrm{d}S$ per ogni superficie $S$, da cui

$$\nabla\times\vec{B} = \mu_0\vec{J}.$$

Queste due equazioni differenziali costituiscono le **equazioni della magnetostatica nel vuoto**. La prima dice che il campo magnetico non ha sorgenti puntiformi (è un campo **solenoidale**), la seconda che le correnti sono i "vortici" del campo. In coordinate cartesiane, la divergenza è $\partial_x B_x+\partial_y B_y+\partial_z B_z$ e il rotore è il vettore di componenti $(\partial_y B_z-\partial_z B_y,\ \partial_z B_x-\partial_x B_z,\ \partial_x B_y-\partial_y B_x)$.

Una conseguenza immediata della seconda equazione è che, poiché la divergenza di un rotore è identicamente nulla, deve essere $\nabla\cdot\vec{J}=0$: le equazioni della magnetostatica sono compatibili solo con correnti stazionarie, per le quali l'equazione di continuità $\nabla\cdot\vec{J}=-\partial\rho/\partial t$ si riduce a $\nabla\cdot\vec{J}=0$. Ritroviamo così, in forma locale, la limitazione già incontrata nella forma integrale del teorema di Ampère.

### 23.7.1 Condizioni al contorno

Le equazioni differenziali richiedono che il campo sia derivabile. Esistono però situazioni fisiche, idealizzate ma molto utili, in cui il campo è discontinuo attraverso una superficie: è il caso di una **corrente superficiale**, cioè di una corrente che scorre in uno strato di spessore trascurabile, descritta dalla **densità di corrente superficiale** $\vec{K}$ (corrente per unità di lunghezza trasversale, misurata in $\mathrm{A/m}$). Un esempio è l'avvolgimento di un solenoide fitto: le spire possono essere approssimate da un foglio di corrente cilindrico con $K = nI$. In questi casi si ricorre alla forma integrale delle leggi per ottenere le **condizioni al contorno** (o condizioni di raccordo) che legano il campo sui due lati della superficie.

Per la **componente normale** si usa il teorema di Gauss. Si considera una piccola scatoletta cilindrica (il "pillbox") con le basi di area $\Delta S$ parallele alla superficie, una per lato, e altezza infinitesima. Il flusso attraverso la superficie laterale tende a zero con l'altezza, e restano i contributi delle due basi: $(B_{2n}-B_{1n})\Delta S = 0$. Quindi

$$B_{2n} = B_{1n}:$$

la componente normale del campo magnetico è **sempre continua** attraverso qualsiasi superficie, anche in presenza di correnti superficiali. È la traduzione locale della conservazione del flusso.

Per la **componente tangenziale** si usa il teorema di Ampère. Si considera un piccolo rettangolo con due lati di lunghezza $\Delta l$ paralleli alla superficie, uno per lato, e gli altri due di lunghezza infinitesima che la attraversano. Il contributo dei lati corti tende a zero, e la corrente concatenata è quella superficiale che attraversa il rettangolo, $K_\perp\Delta l$, dove $K_\perp$ è la componente di $\vec{K}$ perpendicolare al piano del rettangolo. Si ottiene $(B_{2t}-B_{1t})\Delta l = \mu_0 K_\perp\Delta l$, cioè

$$B_{2t}-B_{1t} = \mu_0 K.$$

In forma vettoriale compatta, con $\hat{n}$ normale diretta dal mezzo 1 al mezzo 2: $\hat{n}\times(\vec{B}_2-\vec{B}_1)=\mu_0\vec{K}$. La componente tangenziale del campo **salta** di $\mu_0K$ attraversando una corrente superficiale, mentre è continua se non ci sono correnti superficiali. Il caso del solenoide illustra bene queste condizioni: all'esterno il campo è nullo, all'interno è $\mu_0 nI$ e parallelo alla superficie, e il salto è proprio $\mu_0K$ con $K=nI$. Un altro esempio è il piano indefinito percorso da una corrente superficiale uniforme $K$: per simmetria il campo è parallelo al piano, perpendicolare a $\vec{K}$, di verso opposto sui due lati e di modulo $\mu_0K/2$ su ciascun lato, con un salto totale $\mu_0K$.

Le condizioni al contorno sono analoghe a quelle elettrostatiche, ma con i ruoli scambiati: nel caso elettrico è la componente tangenziale di $\vec{E}$ a essere sempre continua e la componente normale a saltare di $\sigma/\varepsilon_0$ in presenza di una carica superficiale. Lo scambio riflette il fatto che il campo elettrostatico è irrotazionale con sorgenti, mentre quello magnetostatico è solenoidale con vortici. In presenza di materiali magnetici, le condizioni si riformulano in termini del campo $\vec{H}$ (la cui componente tangenziale è continua in assenza di correnti di conduzione superficiali) e del campo $\vec{B}$ (componente normale continua); da esse discende, ad esempio, la "rifrazione" delle linee di campo all'interfaccia tra aria e ferro, che spiega perché i nuclei ferromagnetici incanalano il flusso.

### 23.7.2 Leggi di Maxwell

Mettendo insieme le equazioni dell'elettrostatica e della magnetostatica nel vuoto, otteniamo un sistema di quattro equazioni che descrivono completamente i campi statici:

$$\nabla\cdot\vec{E} = \frac{\rho}{\varepsilon_0},\qquad \nabla\times\vec{E} = 0,$$
$$\nabla\cdot\vec{B} = 0,\qquad \nabla\times\vec{B} = \mu_0\vec{J}.$$

Le corrispondenti forme integrali sono il teorema di Gauss elettrico, la conservatività del campo elettrostatico, il teorema di Gauss magnetico e il teorema di Ampère. In regime statico i due campi sono completamente **disaccoppiati**: $\vec{E}$ dipende solo dalle cariche, $\vec{B}$ solo dalle correnti. Si tratta delle **equazioni di Maxwell nel caso statico**. Il loro contenuto è completo grazie al **teorema di Helmholtz**: un campo vettoriale che si annulla all'infinito è univocamente determinato dalla sua divergenza e dal suo rotore. Conoscere le sorgenti ($\rho$ e $\vec{J}$) significa dunque conoscere i campi.

La struttura delle equazioni suggerisce l'uso dei potenziali. Poiché $\nabla\times\vec{E}=0$, il campo elettrico si scrive come gradiente di un potenziale scalare, $\vec{E}=-\nabla V$. Poiché $\nabla\cdot\vec{B}=0$, il campo magnetico si scrive come rotore di un **potenziale vettore**, $\vec{B}=\nabla\times\vec{A}$. Il potenziale vettore non è univoco: aggiungendo ad $\vec{A}$ il gradiente di una funzione scalare qualsiasi il rotore non cambia (libertà di **gauge**). Scegliendo $\nabla\cdot\vec{A}=0$ (gauge di Coulomb), la legge di Ampère diventa $\nabla^2\vec{A}=-\mu_0\vec{J}$, che è un'equazione di Poisson per ciascuna componente, del tutto analoga a $\nabla^2V=-\rho/\varepsilon_0$. La sua soluzione,

$$\vec{A}(\vec{r}) = \frac{\mu_0}{4\pi}\int\frac{\vec{J}(\vec{r}\,')}{|\vec{r}-\vec{r}\,'|}\,\mathrm{d}V',$$

calcolandone il rotore, restituisce esattamente la prima legge di Laplace, chiudendo il cerchio tra le formulazioni.

Le equazioni statiche non sono però la fine della storia. Quando i campi variano nel tempo, l'esperienza mostra (legge di Faraday) che un campo magnetico variabile genera un campo elettrico, per cui $\nabla\times\vec{E}=-\partial\vec{B}/\partial t$; e Maxwell comprese che, simmetricamente, un campo elettrico variabile genera un campo magnetico, aggiungendo alla legge di Ampère il termine $\mu_0\varepsilon_0\,\partial\vec{E}/\partial t$, necessario anche per rendere le equazioni compatibili con la conservazione della carica quando $\nabla\cdot\vec{J}\neq0$. Le due equazioni sulle divergenze restano invece invariate anche nel caso dinamico. Questo accoppiamento tra campo elettrico e magnetico darà origine alle onde elettromagnetiche, oggetto del capitolo 24.

### Esercizio d'esempio

**Problema.** In un conduttore cilindrico di raggio $a = 2{,}0\,\mathrm{mm}$ la densità di corrente è uniforme e diretta lungo l'asse $z$, $\vec{J} = J\hat{z}$ con $J = 1{,}0\times10^{6}\,\mathrm{A/m^2}$. Verificare che il campo interno $\vec{B} = \frac{\mu_0 J}{2}(-y\,\hat{x}+x\,\hat{y})$ soddisfa le equazioni differenziali della magnetostatica, e calcolarne il modulo sulla superficie. Infine, un solenoide con $n = 2000\,\mathrm{spire/m}$ e $I = 1{,}5\,\mathrm{A}$ è visto come un foglio di corrente: calcolare $K$ e il salto del campo tangenziale.

**Soluzione.** La divergenza è
$$\nabla\cdot\vec{B} = \frac{\mu_0J}{2}\left(\frac{\partial(-y)}{\partial x}+\frac{\partial x}{\partial y}\right) = 0.$$
La componente $z$ del rotore è
$$(\nabla\times\vec{B})_z = \frac{\partial B_y}{\partial x}-\frac{\partial B_x}{\partial y} = \frac{\mu_0J}{2}(1+1) = \mu_0 J,$$
mentre le componenti $x$ e $y$ sono nulle perché $B_x,B_y$ non dipendono da $z$ e $B_z=0$. Le equazioni sono soddisfatte. Il modulo del campo a distanza $r$ dall'asse è $B=\mu_0 J r/2$; sulla superficie
$$B(a) = \frac{4\pi\times10^{-7}\cdot1{,}0\times10^{6}\cdot2{,}0\times10^{-3}}{2}\simeq 1{,}26\times10^{-3}\,\mathrm{T},$$
in accordo con $\mu_0 I/(2\pi a)$ con $I = J\pi a^2\simeq12{,}6\,\mathrm{A}$.

Per il solenoide, $K = nI = 2000\cdot1{,}5 = 3{,}0\times10^{3}\,\mathrm{A/m}$, e il salto del campo tangenziale è
$$\Delta B_t = \mu_0 K = 4\pi\times10^{-7}\cdot3{,}0\times10^{3}\simeq 3{,}8\times10^{-3}\,\mathrm{T},$$
che coincide con il campo interno $\mu_0 nI$, essendo nullo il campo esterno.

### Punti chiave

- In forma differenziale la magnetostatica nel vuoto è descritta da $\nabla\cdot\vec{B}=0$ e $\nabla\times\vec{B}=\mu_0\vec{J}$.
- Il passaggio dalla forma integrale a quella differenziale si basa sui teoremi della divergenza e di Stokes.
- La legge di Ampère statica richiede $\nabla\cdot\vec{J}=0$, cioè correnti stazionarie.
- La componente normale di $\vec{B}$ è sempre continua; la componente tangenziale salta di $\mu_0K$ attraverso una corrente superficiale.
- Il campo magnetico si può scrivere come $\vec{B}=\nabla\times\vec{A}$; nella gauge di Coulomb $\nabla^2\vec{A}=-\mu_0\vec{J}$.
- In regime statico le equazioni di Maxwell disaccoppiano $\vec{E}$ e $\vec{B}$; nel caso dinamico compaiono i termini $\partial\vec{B}/\partial t$ e $\partial\vec{E}/\partial t$ che li accoppiano.
