# Capitolo 20 — Corrente elettrica

Con questo capitolo lasciamo l'elettrostatica, nella quale le cariche sono ferme e i conduttori in equilibrio, per entrare nello studio delle cariche in movimento. Quando all'interno di un conduttore si mantiene un campo elettrico, ad esempio collegandone gli estremi ai poli di un generatore, le cariche libere non raggiungono mai l'equilibrio e si genera un flusso ordinato di carica: la corrente elettrica. Introdurremo dapprima l'intensità di corrente, grandezza globale che descrive quanta carica attraversa una sezione nell'unità di tempo; passeremo poi alla densità di corrente, grandezza locale e vettoriale che descrive il moto dei portatori punto per punto e lo collega alle loro proprietà microscopiche; concluderemo con il principio di conservazione della carica, espresso dall'equazione di continuità, e con le sue conseguenze per i fenomeni stazionari, che costituiscono il fondamento dello studio dei circuiti elettrici dei capitoli successivi.

## 20.1 Corrente

La corrente elettrica è uno dei fenomeni fisici più familiari e al tempo stesso più importanti della tecnologia moderna: dall'illuminazione ai motori, dalle telecomunicazioni all'elettronica digitale, quasi ogni dispositivo che usiamo si basa sul controllo del moto di cariche elettriche. Storicamente, la possibilità di produrre correnti continue e durature nasce nel 1800 con la pila di Volta; prima di allora erano note solo le scariche impulsive delle bottiglie di Leida e delle macchine elettrostatiche. Lo studio quantitativo della corrente ha portato a scoperte fondamentali, come il legame fra corrente e magnetismo (Ørsted, Ampère), che vedremo nei capitoli di magnetostatica. In questa sezione definiamo con precisione l'intensità di corrente, discutiamo la natura dei portatori di carica nei diversi materiali e alcune proprietà generali della conduzione.

### 20.1.1 Intensità di corrente

Consideriamo una superficie $S$ attraversata da cariche in movimento, ad esempio la sezione trasversale di un filo conduttore, e fissiamo su di essa un verso di attraversamento positivo. Sia $dq$ la carica **netta** che attraversa la superficie nel verso positivo durante l'intervallo di tempo $dt$, cioè la carica positiva che la attraversa nel verso scelto meno quella che la attraversa in verso opposto (e, analogamente, con segno opposto per le cariche negative). Si definisce **intensità di corrente** attraverso $S$ la grandezza

$$i = \frac{dq}{dt}$$

cioè la carica che attraversa la superficie nell'unità di tempo. L'unità di misura nel Sistema Internazionale è l'**ampere** (A), con $1\ \text{A} = 1\ \text{C/s}$. L'ampere è una delle sette unità fondamentali del SI: dal 2019 esso è definito fissando il valore numerico della carica elementare, $e = 1.602176634\times10^{-19}$ C esatti, per cui una corrente di 1 A corrisponde al passaggio di circa $6.24\times10^{18}$ cariche elementari al secondo. Storicamente, invece, l'ampere era definito attraverso la forza magnetica fra due fili paralleli percorsi da corrente, e il coulomb ne era una grandezza derivata ($1\ \text{C} = 1\ \text{A}\cdot\text{s}$).

Se la corrente è costante nel tempo, si parla di **corrente continua** (o stazionaria) e la carica che attraversa la sezione in un tempo $t$ è semplicemente $q = i\,t$. Se la corrente varia nel tempo, la carica totale transitata fra gli istanti $t_1$ e $t_2$ si ottiene integrando:

$$q = \int_{t_1}^{t_2} i(t)\,dt$$

e la corrente media nell'intervallo è $\bar{i} = q/(t_2 - t_1)$. Un caso molto importante di corrente variabile è la **corrente alternata**, sinusoidale nel tempo, utilizzata nella rete di distribuzione dell'energia elettrica (in Europa con frequenza di 50 Hz): il suo valor medio in un periodo è nullo, ma non è nullo il suo effetto termico, il che rende necessario introdurre il cosiddetto valore efficace.

È importante sottolineare che l'intensità di corrente è una grandezza **scalare** (con segno), non un vettore, benché si parli comunemente del "verso" della corrente. Il segno dipende dal verso positivo scelto per la superficie: se la carica netta fluisce nel verso scelto la corrente è positiva, altrimenti negativa. In un filo, la corrente si rappresenta con una freccia lungo il conduttore, ma questa freccia indica soltanto il verso di percorrenza convenzionalmente positivo, non una direzione nello spazio: il filo può curvare arbitrariamente senza che la corrente cambi. La descrizione vettoriale locale sarà fornita dalla densità di corrente, nella prossima sezione.

### 20.1.2 Verso convenzionale e portatori di carica

Per convenzione, il **verso della corrente** è quello in cui si muovono (o si muoverebbero) le cariche positive. Questa convenzione fu stabilita prima che si conoscesse la natura microscopica della conduzione e resta in uso ancora oggi. Nei metalli, tuttavia, i **portatori di carica** sono gli elettroni, carichi negativamente, che si muovono quindi in verso opposto alla corrente convenzionale. Dal punto di vista degli effetti macroscopici (riscaldamento, campo magnetico prodotto, carica trasportata) non c'è differenza fra un flusso di cariche positive in un verso e un flusso di cariche negative in verso opposto: in entrambi i casi la carica netta trasportata nel verso convenzionale è positiva. Soltanto esperimenti specifici, come l'**effetto Hall** che vedremo in magnetostatica, permettono di distinguere il segno dei portatori.

I portatori di carica dipendono dal materiale. Nei **metalli** la conduzione è dovuta agli **elettroni di conduzione**, gli elettroni più esterni degli atomi che nel reticolo cristallino non sono legati a un singolo atomo ma sono condivisi da tutto il solido; la loro densità è dell'ordine di $10^{28}$–$10^{29}$ m$^{-3}$ (circa uno per atomo). Nelle **soluzioni elettrolitiche** (ad esempio acqua e sale) i portatori sono **ioni** positivi e negativi, che si muovono in versi opposti contribuendo entrambi alla corrente nello stesso verso convenzionale; in questo caso il passaggio di corrente è accompagnato da trasporto di materia e da reazioni chimiche agli elettrodi (elettrolisi). Nei **gas ionizzati** e nei plasmi, come nelle lampade a scarica, i portatori sono elettroni e ioni positivi. Nei **semiconduttori** (silicio, germanio, arseniuro di gallio) la conduzione è dovuta agli elettroni di conduzione e alle **lacune**, stati vuoti nella banda di valenza che si comportano come particelle di carica positiva; la loro densità è molto minore che nei metalli e può essere controllata con il drogaggio, il che è alla base di tutta l'elettronica moderna.

Nei materiali **isolanti** i portatori liberi sono praticamente assenti e la corrente è trascurabile, salvo quando il campo supera la rigidità dielettrica. Esistono infine i **superconduttori**, materiali che al di sotto di una temperatura critica conducono senza alcuna dissipazione, nei quali i portatori sono coppie di elettroni correlate (coppie di Cooper): la loro descrizione richiede la meccanica quantistica e va oltre lo scopo di questo corso.

### 20.1.3 Moto disordinato e moto di deriva

Anche in assenza di corrente, gli elettroni di conduzione in un metallo non sono fermi: si muovono in modo caotico con velocità elevatissime, dell'ordine di $10^6$ m/s (la cosiddetta velocità di Fermi, di origine quantistica), urtando continuamente gli ioni del reticolo, le impurezze e i difetti. Poiché le direzioni del moto sono distribuite in modo isotropo, il numero di elettroni che attraversa una sezione in un verso è uguale in media a quello che la attraversa nel verso opposto: la carica netta trasportata è nulla e non c'è corrente.

Quando si applica un campo elettrico, a questo moto disordinato si sovrappone un piccolo moto ordinato nel verso della forza elettrica, detto **moto di deriva**, caratterizzato da una velocità media $\vec{v}_d$ detta **velocità di deriva**. È soltanto la deriva a produrre corrente. Come vedremo nella prossima sezione, la velocità di deriva negli ordinari conduttori metallici è sorprendentemente piccola: dell'ordine di frazioni di millimetro al secondo. Ciò pare in contrasto con l'esperienza quotidiana per cui, premendo un interruttore, la lampada si accende istantaneamente. Il paradosso si risolve osservando che il conduttore è già pieno di elettroni: quando si chiude il circuito, il campo elettrico si propaga lungo i fili con velocità prossima a quella della luce, e mette in moto contemporaneamente gli elettroni in tutto il circuito, come quando si apre un rubinetto collegato a un tubo già pieno d'acqua. Non sono gli elettroni a viaggiare dall'interruttore alla lampada, ma il segnale.

Perché si mantenga una corrente stazionaria in un conduttore occorre che al suo interno si mantenga un campo elettrico, il che è possibile solo se il conduttore non è in equilibrio elettrostatico. Ciò richiede un dispositivo, il **generatore**, capace di mantenere una differenza di potenziale fra due punti spendendo energia di natura non elettrostatica (chimica nelle pile, meccanica nelle dinamo, luminosa nelle celle fotovoltaiche). Senza generatore, una corrente può esistere solo in modo transitorio, ad esempio durante la scarica di un condensatore: le cariche si ridistribuiscono finché il conduttore raggiunge di nuovo l'equilibrio.

### 20.1.4 Effetti e misura della corrente

La corrente elettrica si riconosce e si misura attraverso i suoi effetti. L'**effetto termico** (o effetto Joule) consiste nel riscaldamento dei conduttori percorsi da corrente, dovuto al trasferimento di energia dai portatori al reticolo negli urti: è sfruttato nelle stufe, nei fusibili e nelle lampade a incandescenza. L'**effetto magnetico** consiste nella produzione di un campo magnetico attorno ai conduttori percorsi da corrente, che esercita forze su magneti e su altre correnti; è il principio di funzionamento dei motori elettrici e degli strumenti di misura elettromeccanici (galvanometri). L'**effetto chimico** si manifesta nelle soluzioni elettrolitiche con la deposizione di sostanze agli elettrodi; le leggi di Faraday dell'elettrolisi legano la massa depositata alla carica transitata, e storicamente hanno fornito uno dei primi metodi di misura precisa della carica.

Lo strumento che misura la corrente si chiama **amperometro** e va inserito **in serie** nel ramo di circuito di cui si vuole misurare la corrente, in modo che la stessa corrente lo attraversi; per non alterare il circuito, un amperometro ideale deve avere resistenza interna nulla. Gli amperometri moderni misurano tipicamente la piccola tensione ai capi di un resistore di precisione (shunt) attraversato dalla corrente, oppure il campo magnetico generato dal conduttore (pinze amperometriche, sensori Hall), che consente misure senza interrompere il circuito.

Qualche ordine di grandezza aiuta a orientarsi: le correnti nei circuiti integrati sono dell'ordine dei microampere o dei nanoampere per singolo transistore; un LED assorbe circa 20 mA; una lampada domestica circa 0.1–0.5 A; un forno elettrico circa 10 A; il motorino di avviamento di un'automobile alcune centinaia di ampere; un fulmine trasporta picchi di decine di migliaia di ampere per tempi dell'ordine di decine di microsecondi. Per il corpo umano, correnti di qualche decina di milliampere attraverso il torace possono già essere letali, perché interferiscono con l'attività elettrica del cuore.

### Esercizio d'esempio

Una batteria di un'automobile ha una "capacità" dichiarata di 60 A·h. (a) Quanta carica può erogare? (b) Per quanto tempo può alimentare le luci di posizione, che assorbono complessivamente $i = 1.5$ A? (c) Durante l'avviamento il motorino assorbe una corrente che decresce linearmente da 300 A a 100 A in 2.0 s: quanta carica viene erogata e qual è la corrente media? (d) Quanti elettroni attraversano una sezione del cavo durante l'avviamento?

**Soluzione.** (a) La "capacità" di una batteria è in realtà una carica: $q = 60\ \text{A}\times3600\ \text{s} = 2.16\times10^5$ C.

(b) A corrente costante $t = q/i = 2.16\times10^5\ \text{C}/1.5\ \text{A} = 1.44\times10^5$ s, cioè 40 h.

(c) La corrente è $i(t) = 300\ \text{A} - (100\ \text{A/s})\,t$ per $0\le t\le2.0$ s. La carica è l'area sotto la curva:

$$q = \int_0^{2.0}(300 - 100t)\,dt = 300\times2.0 - 50\times4.0 = 400\ \text{C}$$

La corrente media è $\bar{i} = 400\ \text{C}/2.0\ \text{s} = 200$ A, coincidente con la media aritmetica degli estremi perché l'andamento è lineare.

(d) $N = q/e = 400/1.602\times10^{-19} = 2.5\times10^{21}$ elettroni. L'avviamento consuma lo $0.19\%$ della carica totale della batteria.

### Punti chiave

- L'intensità di corrente è la carica netta che attraversa una superficie nell'unità di tempo, $i = dq/dt$; si misura in ampere (1 A = 1 C/s).
- La corrente è uno scalare con segno, riferito al verso positivo scelto sulla superficie; il verso convenzionale è quello del moto delle cariche positive.
- I portatori di carica sono elettroni nei metalli, ioni negli elettroliti, elettroni e ioni nei gas, elettroni e lacune nei semiconduttori.
- La corrente è dovuta al moto di deriva, una piccola velocità ordinata sovrapposta al rapido moto disordinato dei portatori.
- Per mantenere una corrente stazionaria serve un generatore che mantenga un campo nel conduttore, impedendo il raggiungimento dell'equilibrio elettrostatico.
- La corrente si riconosce dagli effetti termico, magnetico e chimico; l'amperometro va inserito in serie e idealmente ha resistenza nulla.

## 20.2 Densità di corrente

L'intensità di corrente è una grandezza globale: ci dice quanta carica attraversa un'intera superficie per unità di tempo, ma non come il flusso di carica sia distribuito sulla superficie né in quale direzione si muovano le cariche nei diversi punti. In un filo sottile questa informazione è superflua, ma in molti casi è essenziale: si pensi alla corrente in un conduttore massiccio di forma irregolare, alla corrente che si disperde nel terreno da un dispersore di messa a terra, al fascio di elettroni di un microscopio elettronico o alla corrente ionica in una cella elettrolitica. Per descrivere il moto delle cariche punto per punto si introduce una grandezza **locale** e **vettoriale**, la densità di corrente, che collega la descrizione macroscopica alle proprietà microscopiche dei portatori.

### 20.2.1 Definizione di densità di corrente

Consideriamo un materiale nel quale ci sia un solo tipo di portatori, ciascuno di carica $q$, presenti con densità numerica $n$ (numero di portatori per unità di volume), e supponiamo che in un certo punto essi si muovano con velocità di deriva $\vec{v}_d$. Prendiamo un elemento di superficie $dS$ con normale $\hat{n}$, che forma un angolo $\theta$ con la direzione di $\vec{v}_d$. Nel tempo $dt$ attraversano $dS$ tutti e soli i portatori che all'inizio si trovano nel cilindretto obliquo che ha base $dS$ e generatrice $\vec{v}_d\,dt$, il cui volume è $d\tau = v_d\,dt\,dS\cos\theta$. Il numero di tali portatori è $n\,d\tau$ e la carica che essi trasportano è

$$dq = nq\,v_d\cos\theta\,dS\,dt$$

La corrente attraverso l'elemento di superficie è quindi $di = nq\,\vec{v}_d\cdot\hat{n}\,dS$. Si definisce allora il vettore **densità di corrente**

$$\vec{J} = nq\,\vec{v}_d = \rho\,\vec{v}_d$$

dove $\rho = nq$ è la densità volumetrica della carica mobile. Con questa definizione la corrente attraverso un elemento di superficie è il flusso elementare di $\vec{J}$, $di = \vec{J}\cdot d\vec{S}$, e la corrente attraverso una superficie finita è il **flusso** della densità di corrente:

$$i = \int_S\vec{J}\cdot d\vec{S}$$

La densità di corrente si misura in A/m$^2$. Il suo modulo rappresenta la corrente per unità di area attraverso una superficie disposta perpendicolarmente al moto delle cariche; la sua direzione è quella della velocità di deriva per cariche positive, opposta per cariche negative. In entrambi i casi $\vec{J}$ ha il verso della corrente convenzionale: per gli elettroni $q = -e$ e $\vec{v}_d$ è opposta al campo, quindi $\vec{J} = -ne\vec{v}_d$ è concorde al campo. Si osservi la stretta analogia con la meccanica dei fluidi: $\vec{J}$ è l'esatto analogo della densità di flusso di massa $\rho_m\vec{v}$, e la corrente è l'analogo della portata in massa. Le linee di forza di $\vec{J}$, dette **linee di corrente**, sono tangenti in ogni punto alla direzione del flusso di carica.

Nel caso più semplice di un filo di sezione $S$ percorso da corrente uniformemente distribuita e perpendicolare alla sezione, l'integrale si riduce a un prodotto: $i = JS$, cioè $J = i/S$. Nelle normali installazioni domestiche, con conduttori di rame di 1.5 o 2.5 mm$^2$ e correnti di 10–16 A, la densità di corrente è dell'ordine di $10^7$ A/m$^2$ (cioè alcuni A/mm$^2$); le norme tecniche fissano valori massimi di densità di corrente per evitare un riscaldamento eccessivo dei cavi. È importante notare, però, che la distribuzione uniforme è un'approssimazione: in corrente alternata ad alta frequenza la corrente tende a concentrarsi presso la superficie del conduttore (**effetto pelle**), e allora la definizione locale di $\vec{J}$ diventa indispensabile.

### 20.2.2 Velocità di deriva

La relazione $J = nqv_d$ permette di stimare la velocità di deriva dei portatori a partire da grandezze misurabili. Nel rame ogni atomo contribuisce con circa un elettrone di conduzione; con densità di massa $8.96\times10^3$ kg/m$^3$ e massa molare $63.5\times10^{-3}$ kg/mol si ha

$$n = \frac{\rho_mN_A}{M} = \frac{8.96\times10^3\times6.02\times10^{23}}{63.5\times10^{-3}}\ \text{m}^{-3} = 8.5\times10^{28}\ \text{m}^{-3}$$

In un filo di sezione 1 mm$^2$ percorso da 1 A, $J = 10^6$ A/m$^2$ e

$$v_d = \frac{J}{ne} = \frac{10^6}{8.5\times10^{28}\times1.6\times10^{-19}}\ \text{m/s} = 7.4\times10^{-5}\ \text{m/s}$$

meno di un decimo di millimetro al secondo: un elettrone impiegherebbe più di tre ore a percorrere un metro di filo. Questa velocità è circa dieci miliardi di volte inferiore alla velocità media del moto disordinato degli elettroni, il che giustifica il quadro descritto nella sezione precedente: la corrente è una minuscola "perturbazione" ordinata sovrapposta a un moto termico caotico molto più rapido. La grande intensità della corrente nonostante la piccolissima velocità di deriva è dovuta all'enorme densità dei portatori: anche uno spostamento lentissimo di un numero così elevato di cariche trasporta una carica considerevole.

Nei semiconduttori, dove la densità dei portatori è molto minore (nel silicio drogato tipicamente $10^{21}$–$10^{24}$ m$^{-3}$), la velocità di deriva a parità di densità di corrente è molto più alta. In un fascio di particelle nel vuoto, come nei tubi a raggi catodici o negli acceleratori, la situazione è ancora diversa: tutte le particelle si muovono con la stessa velocità, elevata, e la densità numerica è piccola. Anche in questo caso vale $\vec{J} = nq\vec{v}$, ma $\vec{v}$ non è una velocità di deriva bensì la velocità effettiva delle particelle.

### 20.2.3 Più tipi di portatori

Quando in un materiale sono presenti più specie di portatori, con cariche $q_k$, densità $n_k$ e velocità di deriva $\vec{v}_k$, ciascuna contribuisce indipendentemente alla densità di corrente, e il contributo totale è la somma:

$$\vec{J} = \sum_k n_kq_k\vec{v}_k$$

Consideriamo ad esempio una soluzione di cloruro di sodio in acqua, in cui sono presenti ioni Na$^+$ e Cl$^-$ con uguale densità $n$. Sotto l'azione di un campo elettrico gli ioni positivi derivano nel verso del campo e quelli negativi in verso opposto. Il contributo degli ioni positivi è $ne\vec{v}_+$, quello degli ioni negativi è $(-e)n\vec{v}_-$; poiché $\vec{v}_-$ è opposta a $\vec{v}_+$, entrambi i contributi sono diretti come il campo e si **sommano**. Lo stesso vale nei semiconduttori per elettroni e lacune: $\vec{J} = e(p\,\vec{v}_p - n\,\vec{v}_n)$, dove $p$ e $n$ sono le densità di lacune ed elettroni. Un'altra osservazione importante è che la densità di carica totale del materiale può essere nulla (il materiale è neutro) anche se la densità di corrente non lo è: in un metallo la carica degli elettroni di conduzione è compensata da quella degli ioni del reticolo, che però sono fermi e non contribuiscono a $\vec{J}$. La corrente richiede cariche **mobili**, non cariche nette: un filo percorso da corrente è, con ottima approssimazione, elettricamente neutro.

### 20.2.4 Mobilità e forma locale della legge di conduzione

Perché la velocità di deriva è costante, anziché crescere indefinitamente sotto l'azione della forza elettrica costante $q\vec{E}$? Un modello classico semplice ma efficace, dovuto a Drude, risponde così: fra un urto e il successivo ogni portatore viene accelerato dal campo con accelerazione $q\vec{E}/m$; negli urti con il reticolo esso perde memoria della velocità acquisita e riparte con velocità casuale, a media nulla. Se $\tau$ è il **tempo medio fra due urti** (tempo di rilassamento), la velocità media acquisita dal campo è

$$\vec{v}_d = \frac{q\tau}{m}\vec{E} = \mu\vec{E}$$

dove $\mu = q\tau/m$ è la **mobilità** del portatore, misurata in m$^2$/(V·s). Si tratta di una situazione simile a quella di un corpo che cade in un fluido viscoso e raggiunge una velocità limite: gli urti si comportano, in media, come una forza di attrito proporzionale alla velocità, $-m\vec{v}_d/\tau$. Sostituendo nell'espressione della densità di corrente:

$$\vec{J} = nq\vec{v}_d = \frac{nq^2\tau}{m}\vec{E} = \sigma\vec{E}$$

La densità di corrente in un punto è proporzionale al campo elettrico nello stesso punto, con costante di proporzionalità $\sigma = nq^2\tau/m$ detta **conducibilità elettrica** del materiale. Si tratta della **forma locale della legge di Ohm**, che verrà approfondita nel capitolo dedicato ai resistori. Nel rame, con $\sigma = 5.96\times10^7$ S/m, si ricava un tempo di rilassamento $\tau = m\sigma/(ne^2)\approx2.5\times10^{-14}$ s: gli elettroni subiscono circa $4\times10^{13}$ urti al secondo. Il modello di Drude è concettualmente approssimato (una descrizione corretta richiede la meccanica quantistica, nella quale gli urti avvengono con le vibrazioni del reticolo e con le imperfezioni, non con gli ioni stessi), ma riproduce correttamente la proporzionalità fra $\vec{J}$ ed $\vec{E}$ e fornisce stime ragionevoli degli ordini di grandezza.

### Esercizio d'esempio

Un filo di rame ($n = 8.5\times10^{28}$ m$^{-3}$) ha diametro $D_1 = 2.0$ mm ed è percorso da una corrente stazionaria $i = 10$ A. In un tratto il diametro si riduce a $D_2 = 1.0$ mm. Calcolare (a) la densità di corrente e la velocità di deriva nei due tratti; (b) il tempo impiegato in media da un elettrone di conduzione a percorrere 1.0 m del tratto più largo; (c) il campo elettrico nel tratto più largo, sapendo che $\sigma = 5.96\times10^7$ S/m.

**Soluzione.** (a) La sezione del primo tratto è $S_1 = \pi D_1^2/4 = 3.14\times10^{-6}$ m$^2$, e quella del secondo $S_2 = 7.85\times10^{-7}$ m$^2$. In condizioni stazionarie la corrente è la stessa nei due tratti (lo dimostreremo nella prossima sezione), quindi:

$$J_1 = \frac{i}{S_1} = 3.18\times10^6\ \text{A/m}^2, \qquad J_2 = \frac{i}{S_2} = 1.27\times10^7\ \text{A/m}^2$$

Le velocità di deriva sono $v_{d1} = J_1/(ne) = 3.18\times10^6/(8.5\times10^{28}\times1.602\times10^{-19}) = 2.3\times10^{-4}$ m/s e $v_{d2} = 4v_{d1} = 9.3\times10^{-4}$ m/s: dimezzando il diametro, densità di corrente e velocità di deriva quadruplicano.

(b) $t = L/v_{d1} = 1.0/2.3\times10^{-4}$ s $= 4.3\times10^3$ s, circa 72 minuti.

(c) $E_1 = J_1/\sigma = 3.18\times10^6/5.96\times10^7 = 5.3\times10^{-2}$ V/m: per avere 10 A in un filo di rame basta un campo di qualche centesimo di volt al metro.

### Punti chiave

- La densità di corrente $\vec{J} = nq\vec{v}_d$ è un vettore locale che ha il verso della corrente convenzionale; si misura in A/m$^2$.
- La corrente attraverso una superficie è il flusso della densità di corrente: $i = \int_S\vec{J}\cdot d\vec{S}$; per distribuzione uniforme $J = i/S$.
- Nei metalli la velocità di deriva è piccolissima (frazioni di mm/s) a causa dell'enorme densità di portatori ($\sim10^{29}$ m$^{-3}$).
- Con più specie di portatori $\vec{J} = \sum n_kq_k\vec{v}_k$; cariche opposte che derivano in versi opposti danno contributi concordi.
- Un conduttore percorso da corrente è complessivamente neutro: la corrente richiede cariche mobili, non carica netta.
- Nel modello di Drude $\vec{v}_d = \mu\vec{E}$ con mobilità $\mu = q\tau/m$, e $\vec{J} = \sigma\vec{E}$ con $\sigma = nq^2\tau/m$ (legge di Ohm locale).

## 20.3 Conservazione della carica

La conservazione della carica elettrica è uno dei principi più solidi di tutta la fisica: in nessun processo osservato, dalle reazioni chimiche alle collisioni fra particelle ad altissima energia, la carica totale di un sistema isolato è mai cambiata. Le cariche possono essere create o distrutte soltanto a coppie di segno opposto (come nella produzione di una coppia elettrone–positrone da un fotone di alta energia), in modo che la carica netta resti invariata. Nell'elettrostatica questo principio è stato usato in forma "globale", ad esempio per affermare che un conduttore isolato mantiene la propria carica. Ora che le cariche si muovono, esso assume una forma più ricca: la carica è conservata **localmente**, cioè non solo la carica totale dell'universo è costante, ma la carica contenuta in qualsiasi regione di spazio può cambiare soltanto perché delle cariche attraversano il contorno di quella regione. Non può sparire in un punto e ricomparire istantaneamente in un altro lontano. Questa affermazione si traduce nell'equazione di continuità, che lega la densità di corrente alla densità di carica, e che nel caso stazionario fornisce le regole fondamentali dei circuiti.

### 20.3.1 Equazione di continuità

Consideriamo una regione di spazio di volume $\tau$, delimitata da una superficie chiusa $S$, con la normale orientata verso l'esterno. La carica contenuta nella regione è $Q_{int} = \int_\tau\rho\,d\tau$, dove $\rho$ è la densità volumetrica di carica. La corrente uscente dalla superficie chiusa è il flusso della densità di corrente, $i_{usc} = \oint_S\vec{J}\cdot d\vec{S}$. La conservazione della carica impone che la carica che esce dalla superficie nell'unità di tempo sia uguale alla diminuzione, per unità di tempo, della carica contenuta all'interno:

$$\oint_S\vec{J}\cdot d\vec{S} = -\frac{dQ_{int}}{dt} = -\frac{d}{dt}\int_\tau\rho\,d\tau$$

Questa è l'**equazione di continuità in forma integrale**. Il segno meno è essenziale: un flusso positivo (uscente) di corrente corrisponde a una diminuzione della carica interna. Se la regione considerata è fissa nello spazio, si può portare la derivata sotto il segno di integrale, che diventa una derivata parziale rispetto al tempo. Applicando poi al primo membro il **teorema della divergenza**, $\oint_S\vec{J}\cdot d\vec{S} = \int_\tau\nabla\cdot\vec{J}\,d\tau$, si ottiene

$$\int_\tau\left(\nabla\cdot\vec{J} + \frac{\partial\rho}{\partial t}\right)d\tau = 0$$

Poiché il volume $\tau$ è arbitrario, l'integrando deve essere nullo in ogni punto, e si ottiene l'**equazione di continuità in forma locale**:

$$\nabla\cdot\vec{J} + \frac{\partial\rho}{\partial t} = 0$$

Il significato fisico è trasparente. La divergenza di $\vec{J}$ in un punto misura quanta corrente "nasce" da quel punto, cioè quanto flusso di carica esce da un volumetto infinitesimo che lo circonda, per unità di volume. Se in un punto la divergenza è positiva, più carica esce di quanta ne entri, e la densità di carica locale deve diminuire; se è negativa, la carica si accumula. L'equazione è formalmente identica all'equazione di continuità della meccanica dei fluidi, $\nabla\cdot(\rho_m\vec{v}) + \partial\rho_m/\partial t = 0$, che esprime la conservazione della massa: la carica si comporta come un fluido indistruttibile.

Un esempio istruttivo di applicazione è il **condensatore in carica**. Consideriamo una superficie chiusa che racchiude una sola armatura di un condensatore collegato a un generatore: attraverso la superficie passa il filo, che porta la corrente entrante $i$, mentre fra le armature non passa alcuna corrente di conduzione (lo spazio è isolante). L'equazione di continuità afferma che la carica sull'armatura cresce con rapidità $dQ/dt = i$. La corrente, dunque, non "attraversa" il condensatore, ma si arresta sulle armature accumulandovi carica; tuttavia, poiché l'altra armatura perde contemporaneamente la stessa carica, il circuito esterno "vede" passare corrente come se il ramo fosse chiuso. Questa situazione, in cui le linee di $\vec{J}$ hanno un'interruzione, sarà riconsiderata in elettromagnetismo con l'introduzione della corrente di spostamento.

Un secondo esempio mostra perché, in un conduttore, la carica netta si trovi sempre in superficie anche quando ci sono correnti. Combinando l'equazione di continuità con la legge di Ohm locale $\vec{J} = \sigma\vec{E}$ e con la legge di Gauss $\nabla\cdot\vec{E} = \rho/\varepsilon_0$, si ottiene

$$\frac{\partial\rho}{\partial t} = -\sigma\nabla\cdot\vec{E} = -\frac{\sigma}{\varepsilon_0}\rho \quad\Longrightarrow\quad \rho(t) = \rho(0)\,e^{-t/\tau_r}, \qquad \tau_r = \frac{\varepsilon_0}{\sigma}$$

Qualunque eccesso di carica posto all'interno di un conduttore omogeneo decade esponenzialmente con un **tempo di rilassamento** $\tau_r$, migrando verso la superficie. Per il rame $\tau_r\approx1.5\times10^{-19}$ s (un valore così piccolo che il modello va preso solo come indicazione: il tempo effettivo è limitato dal tempo fra gli urti), mentre per un isolante come il vetro, con conducibilità di $10^{-12}$ S/m, si arriva a decine di secondi, e per i migliori isolanti a giorni. Questo risultato giustifica la distinzione fra conduttori e isolanti anche dal punto di vista dinamico.

### 20.3.2 Fenomeni stazionari

Si dicono **stazionari** i fenomeni nei quali tutte le grandezze (densità di carica, densità di corrente, campi) sono costanti nel tempo, pur in presenza di cariche in movimento. In questo caso $\partial\rho/\partial t = 0$ in ogni punto e l'equazione di continuità si riduce a

$$\nabla\cdot\vec{J} = 0, \qquad \oint_S\vec{J}\cdot d\vec{S} = 0$$

Il campo $\vec{J}$ è **solenoidale**: il suo flusso attraverso qualsiasi superficie chiusa è nullo, cioè la corrente entrante in ogni regione è uguale a quella uscente. Da questa semplice affermazione discendono conseguenze fondamentali.

La prima riguarda le **linee di corrente**, che in regime stazionario non possono iniziare né terminare in alcun punto: esse devono essere chiuse oppure estendersi all'infinito. Una corrente stazionaria richiede dunque un **circuito chiuso**. Questo è il motivo per cui un condensatore, in regime stazionario, interrompe la corrente continua: le linee di $\vec{J}$ dovrebbero terminare sulle armature, il che è possibile solo durante il transitorio di carica, quando la carica sulle armature cambia.

La seconda conseguenza riguarda i **tubi di flusso**. Consideriamo un tratto di conduttore filiforme, anche di sezione variabile, e la superficie chiusa formata da due sezioni trasversali $S_1$ e $S_2$ e dalla superficie laterale del conduttore. Attraverso la superficie laterale non passa corrente (all'esterno del conduttore c'è un isolante e $\vec{J}$ è tangente alla superficie), quindi il flusso entrante da $S_1$ è uguale a quello uscente da $S_2$:

$$i = \int_{S_1}\vec{J}\cdot d\vec{S} = \int_{S_2}\vec{J}\cdot d\vec{S}$$

In regime stazionario **la corrente è la stessa in ogni sezione di un conduttore privo di diramazioni**, indipendentemente dalla forma e dalle dimensioni della sezione. Dove la sezione si restringe, la densità di corrente aumenta in proporzione inversa, esattamente come la velocità di un fluido incomprimibile aumenta in una strozzatura. Ne segue anche che in un circuito formato da più elementi collegati in serie (generatore, fili, resistori) la corrente è la stessa in ogni elemento.

La terza conseguenza riguarda i **nodi**, cioè i punti in cui convergono più conduttori. Applicando la condizione di flusso nullo a una piccola superficie che racchiude il nodo, e contando come positive le correnti uscenti e negative quelle entranti (o viceversa), si ottiene

$$\sum_k i_k = 0$$

la somma algebrica delle correnti che concorrono in un nodo è nulla. Questa è la **prima legge di Kirchhoff** (o legge dei nodi), uno dei due strumenti fondamentali per l'analisi dei circuiti; essa è dunque semplicemente la conservazione della carica in condizioni stazionarie. La legge vale anche in regime lentamente variabile (quasi stazionario), purché nei nodi non si accumuli carica in misura apprezzabile, il che è vero quando le capacità parassite dei collegamenti sono trascurabili.

Infine, è importante notare che in regime stazionario la densità di carica è costante nel tempo, e quindi il campo elettrico da essa prodotto è un campo elettrostatico a tutti gli effetti: è **conservativo**, ammette un potenziale e la sua circuitazione lungo qualunque linea chiusa è nulla. Le cariche che producono questo campo non sono soltanto quelle dei generatori: in un circuito percorso da corrente stazionaria piccole quantità di carica si dispongono sulle superfici dei conduttori, in particolare nei punti dove il filo curva o cambia sezione, e "guidano" il campo in modo che segua il percorso del filo. Proprio perché il campo elettrostatico è conservativo, però, esso da solo non può mantenere la circolazione della corrente lungo un circuito chiuso, dove l'energia viene continuamente dissipata: lungo il circuito il lavoro del campo elettrostatico per unità di carica è nullo. È necessario un **generatore**, all'interno del quale agisce un campo di natura non elettrostatica (chimica, meccanica, termica) che sposta le cariche in verso opposto al campo elettrostatico; la circuitazione di questo campo si chiama **forza elettromotrice** e sarà discussa nei capitoli dedicati ai circuiti. Dalla conservatività del campo elettrostatico discende invece la **seconda legge di Kirchhoff**, secondo cui la somma delle differenze di potenziale lungo una maglia chiusa è nulla, una volta incluse le forze elettromotrici dei generatori.

### Esercizio d'esempio

(a) In un nodo di un circuito in regime stazionario convergono tre conduttori: nel primo la corrente $i_1 = 3.0$ A entra nel nodo, nel secondo la corrente $i_2 = 1.2$ A esce dal nodo. Determinare la corrente nel terzo conduttore. (b) Il terzo conduttore termina su un'armatura di un condensatore piano di capacità $C = 50\ \mu$F, inizialmente scarico, e la corrente rimane costante per $\Delta t = 2.0$ ms. Calcolare la carica accumulata, la tensione finale e la rapidità di crescita della tensione. (c) Un fascio di protoni con densità di corrente uniforme $J = 2.0$ A/m$^2$ e sezione $S = 1.0$ cm$^2$ colpisce un bersaglio metallico isolato: calcolare la rapidità di crescita della carica del bersaglio.

**Soluzione.** (a) Contando positive le correnti uscenti: $-i_1 + i_2 + i_3 = 0$, da cui $i_3 = i_1 - i_2 = 1.8$ A, uscente dal nodo.

(b) Il regime nel ramo del condensatore non è stazionario: applicando l'equazione di continuità a una superficie che racchiude l'armatura, $dQ/dt = i_3 = 1.8$ A. In $\Delta t = 2.0$ ms la carica accumulata è $Q = i_3\Delta t = 1.8\times2.0\times10^{-3} = 3.6\times10^{-3}$ C. La tensione finale è $\Delta V = Q/C = 3.6\times10^{-3}/5.0\times10^{-5} = 72$ V, con rapidità di crescita $d(\Delta V)/dt = i_3/C = 3.6\times10^4$ V/s. (In un circuito reale la corrente non resterebbe costante a lungo, perché la tensione crescente del condensatore si oppone a quella del generatore.)

(c) La corrente del fascio è $i = JS = 2.0\times1.0\times10^{-4} = 2.0\times10^{-4}$ A. Per l'equazione di continuità applicata a una superficie che racchiude il bersaglio isolato, $dQ/dt = 2.0\times10^{-4}$ C/s: ogni secondo il bersaglio accumula 0.20 mC, pari a circa $1.2\times10^{15}$ protoni al secondo. Se il bersaglio non fosse isolato ma collegato a terra, la carica defluirebbe attraverso il collegamento, e un amperometro inserito su di esso misurerebbe proprio $2.0\times10^{-4}$ A: è il principio della **coppa di Faraday** usata per misurare l'intensità dei fasci di particelle.

### Punti chiave

- La carica si conserva localmente: la carica in una regione cambia solo per il flusso di corrente attraverso il contorno.
- Equazione di continuità in forma integrale: $\oint_S\vec{J}\cdot d\vec{S} = -dQ_{int}/dt$; in forma locale: $\nabla\cdot\vec{J} + \partial\rho/\partial t = 0$.
- In un conduttore omogeneo un eccesso di carica interno decade con tempo di rilassamento $\tau_r = \varepsilon_0/\sigma$, molto breve nei metalli.
- In regime stazionario $\nabla\cdot\vec{J} = 0$: le linee di corrente sono chiuse e una corrente continua richiede un circuito chiuso.
- In un conduttore senza diramazioni la corrente è la stessa in ogni sezione; la densità di corrente è inversamente proporzionale all'area.
- Nei nodi la somma algebrica delle correnti è nulla (prima legge di Kirchhoff), conseguenza diretta della conservazione della carica.
- In regime stazionario il campo elettrico è conservativo; per mantenere la corrente serve un generatore con forza elettromotrice di origine non elettrostatica.
