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

