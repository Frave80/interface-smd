# Capitolo 3 — Dinamica del punto

La **dinamica** studia il moto dei corpi in relazione alle cause che lo determinano. Se la cinematica si limita a descrivere come varia la posizione nel tempo, la dinamica spiega perché un corpo accelera, introducendo i concetti di **forza** e di **massa** e collegandoli tramite i tre principi formulati da Isaac Newton nei *Philosophiae Naturalis Principia Mathematica* (1687). Questi principi, verificati da secoli di esperimenti, costituiscono il fondamento della meccanica classica e restano validi in tutte le situazioni ingegneristiche ordinarie, cioè per velocità molto inferiori a quella della luce e per corpi di dimensioni molto maggiori di quelle atomiche. In questo capitolo si presentano i tre principi, si discutono il ruolo dei sistemi di riferimento inerziali, la natura delle forze e delle reazioni vincolari, si introducono le grandezze angolari (momento della forza, momento d'inerzia, momento angolare) e infine si studiano le condizioni di equilibrio di un punto materiale.

## 3.1 Primo principio della dinamica

Il **primo principio della dinamica**, noto anche come **principio d'inerzia**, afferma:

> Un corpo non soggetto a forze, o soggetto a forze con risultante nulla, persevera nel suo stato di quiete o di moto rettilineo uniforme.

In forma compatta: se $\sum\vec F = \vec 0$ allora $\vec v = $ costante, ovvero $\vec a = \vec 0$. L'enunciato ha una portata concettuale enorme perché rovescia l'intuizione comune, codificata nella fisica aristotelica, secondo cui lo stato "naturale" dei corpi sarebbe la quiete e occorrerebbe una causa per mantenere un moto. L'esperienza quotidiana sembra dare ragione ad Aristotele: un carrello spinto e poi lasciato si ferma, una palla che rotola rallenta. Galileo comprese però che questi rallentamenti sono dovuti all'attrito e alla resistenza dell'aria, cioè a forze, e che riducendo progressivamente tali disturbi il moto prosegue sempre più a lungo. Con il celebre ragionamento dei piani inclinati contrapposti, egli osservò che una pallina scesa lungo un piano risale su un secondo piano fino quasi alla stessa quota, indipendentemente dall'inclinazione del secondo piano; se quest'ultimo diventa orizzontale, la pallina, non potendo mai raggiungere la quota iniziale, dovrebbe continuare a muoversi indefinitamente.

Il principio d'inerzia stabilisce dunque che ciò che richiede una causa non è il moto ma la **variazione** dello stato di moto, cioè l'accelerazione. La proprietà dei corpi di opporsi alle variazioni della propria velocità si chiama **inerzia**. Si noti anche che quiete e moto rettilineo uniforme sono messi sullo stesso piano: non c'è alcuna differenza dinamica tra un corpo fermo e uno che si muove con velocità costante. Questa equivalenza, come si vedrà, è strettamente legata alla relatività del moto.

### 3.1.1 Sistema di riferimento inerziale

Il primo principio non può essere vero in qualunque sistema di riferimento. Si consideri un passeggero in un autobus che frena bruscamente: rispetto all'autobus il passeggero, che pure non è spinto da nessuno in avanti, accelera verso la parte anteriore del veicolo. Oppure si pensi a una pallina appoggiata sul pavimento liscio di una giostra in rotazione: vista dalla giostra, essa si allontana dal centro senza che alcuna forza identificabile agisca su di essa. In questi sistemi di riferimento, che sono essi stessi accelerati, un corpo libero da forze non si muove di moto rettilineo uniforme.

Il primo principio assume quindi il ruolo di **definizione** di una classe privilegiata di sistemi di riferimento: si chiama **sistema di riferimento inerziale** un sistema rispetto al quale un corpo isolato (sufficientemente lontano da tutti gli altri corpi, in modo che le interazioni siano trascurabili) si muove di moto rettilineo uniforme o resta in quiete. Il contenuto fisico del principio sta nell'affermare che **tali sistemi esistono**. Una volta individuato un sistema inerziale, qualunque altro sistema che si muova rispetto a esso di moto traslatorio rettilineo uniforme è anch'esso inerziale: infatti, se $\vec v' = \vec v - \vec V$ con $\vec V$ costante, le accelerazioni nei due sistemi coincidono, $\vec a' = \vec a$. Non esiste invece un sistema inerziale "privilegiato" o "assoluto": tutti i sistemi inerziali sono fisicamente equivalenti. È il **principio di relatività galileiana**, illustrato da Galileo con l'esempio del "gran navilio": chiusi nella stiva di una nave che si muove con velocità costante su un mare calmo, non è possibile, con alcun esperimento meccanico, stabilire se la nave sia in moto o ferma.

Un sistema che ruota o accelera rispetto a un sistema inerziale si dice **non inerziale**. In un sistema non inerziale le leggi della dinamica nella forma newtoniana non valgono direttamente; per poterle usare occorre introdurre delle **forze apparenti** (o fittizie, o inerziali), come la forza centrifuga e la forza di Coriolis, che non sono dovute a interazioni con altri corpi ma alla scelta del riferimento. Il loro studio sarà affrontato nella meccanica relativa.

Dal punto di vista pratico, quali sistemi sono inerziali? A rigore nessun sistema reale lo è esattamente; si tratta di una buona approssimazione entro una certa precisione. Il **sistema del laboratorio**, solidale con la superficie terrestre, non è inerziale perché la Terra ruota attorno al proprio asse (accelerazione centripeta all'equatore $\omega_T^2R_T \simeq 3{,}4\times10^{-2}\ \mathrm{m/s^2}$, con $\omega_T \simeq 7{,}29\times10^{-5}\ \mathrm{rad/s}$) e orbita attorno al Sole (accelerazione $\simeq 6\times10^{-3}\ \mathrm{m/s^2}$). Queste accelerazioni sono piccole rispetto a $g$ (dell'ordine dello $0{,}3\%$ e dello $0{,}06\%$ rispettivamente), e per la maggior parte dei problemi tecnici di breve durata e piccola estensione il laboratorio può essere considerato inerziale. Gli effetti della rotazione terrestre diventano invece osservabili su tempi lunghi o grandi distanze: la rotazione del piano di oscillazione del **pendolo di Foucault**, la deviazione verso est dei gravi in caduta da grandi altezze, la circolazione dei cicloni, la deriva delle traiettorie balistiche a lunga gittata. Un'approssimazione migliore è il **sistema geocentrico**, con origine nel centro della Terra e assi diretti verso stelle fisse, adatto allo studio dei satelliti artificiali; ancora migliore il **sistema eliocentrico** (o delle stelle fisse), con origine nel centro di massa del Sistema Solare, usato per le missioni interplanetarie.

È istruttivo anche un esperimento concettuale: dentro un ascensore in caduta libera un oggetto lasciato andare resta sospeso rispetto alla cabina, come se non agissero forze. Questa osservazione, che Einstein pose alla base della relatività generale (principio di equivalenza), mostra che la distinzione tra forze "vere" e accelerazione del riferimento richiede cura. Nell'ambito della meccanica newtoniana si adotta la convenzione che in un sistema inerziale ogni accelerazione di un corpo deve poter essere ricondotta a un'interazione con altri corpi identificabili; in un sistema non inerziale, invece, compaiono accelerazioni prive di una causa materiale.

Il primo principio, infine, non è un semplice caso particolare del secondo (per $\vec F = 0$ si ha $\vec a = 0$): esso è logicamente precedente, perché individua i sistemi di riferimento in cui il secondo principio è valido. Senza aver prima fissato un sistema inerziale, la relazione tra forza e accelerazione non avrebbe un significato univoco, dato che l'accelerazione dipende dal riferimento scelto. Da questo punto di vista il principio d'inerzia è la "porta d'ingresso" della dinamica, e la verifica sperimentale della sua validità (ad esempio con un disco a cuscino d'aria che scivola su un piano orizzontale quasi senza attrito, mantenendo velocità costante per diversi metri) è uno degli esperimenti fondamentali di un laboratorio didattico.

### Esercizio d'esempio

**Testo.** Un disco a cuscino d'aria di massa $m = 0{,}200\ \mathrm{kg}$ viene lanciato su un tavolo orizzontale con velocità $v_0 = 0{,}800\ \mathrm{m/s}$. Le posizioni registrate ogni $0{,}500\ \mathrm{s}$ sono $0{,}000$; $0{,}399$; $0{,}797$; $1{,}194$; $1{,}590\ \mathrm{m}$. (a) Verificare se il moto è compatibile con il principio d'inerzia. (b) Stimare l'eventuale forza residua di attrito. (c) Valutare se la rotazione terrestre possa influire sul risultato, stimando l'ordine di grandezza $m\,\omega_T v_0$ della forza di Coriolis (l'effetto centrifugo è già incluso nella definizione della verticale locale e non agisce lungo il tavolo).

**Soluzione.** (a) Le velocità medie negli intervalli successivi sono

$$v_1 = \frac{0{,}399}{0{,}500} = 0{,}798\ \mathrm{m/s},\quad v_2 = 0{,}796\ \mathrm{m/s},\quad v_3 = 0{,}794\ \mathrm{m/s},\quad v_4 = 0{,}792\ \mathrm{m/s}.$$

La velocità è quasi costante: il moto è con ottima approssimazione rettilineo uniforme, in accordo con il primo principio.

(b) Si osserva tuttavia una piccola diminuzione regolare di $0{,}002\ \mathrm{m/s}$ ogni $0{,}500\ \mathrm{s}$, cioè un'accelerazione $a \simeq -4\times10^{-3}\ \mathrm{m/s^2}$. Ne segue una forza residua (attrito con l'aria, leggera pendenza del tavolo)

$$|F| = m|a| \simeq 0{,}200\ \mathrm{kg}\cdot4\times10^{-3}\ \mathrm{m/s^2} = 8\times10^{-4}\ \mathrm{N}.$$

(c) L'ordine di grandezza della forza di Coriolis vale

$$m\,\omega_T v_0 \simeq 0{,}200\cdot7{,}29\times10^{-5}\cdot0{,}800\ \mathrm{N} \simeq 1{,}2\times10^{-5}\ \mathrm{N},$$

circa settanta volte più piccola della forza residua misurata e per di più perpendicolare alla velocità. Nell'esperimento il laboratorio può dunque essere considerato inerziale: gli scostamenti dal moto uniforme sono dovuti a forze reali e non alla non inerzialità del riferimento.

### Punti chiave

- Il principio d'inerzia afferma che, in assenza di forze (o con risultante nulla), un corpo mantiene velocità costante.
- Ciò che richiede una causa è la variazione dello stato di moto, cioè l'accelerazione; l'inerzia è la tendenza a conservare la velocità.
- Il primo principio definisce i sistemi di riferimento inerziali e ne afferma l'esistenza.
- Ogni sistema in moto traslatorio uniforme rispetto a un inerziale è inerziale: vale il principio di relatività galileiana.
- Nei sistemi non inerziali compaiono forze apparenti (centrifuga, Coriolis) non dovute a interazioni.
- Il laboratorio terrestre è inerziale con buona approssimazione per esperimenti brevi e locali; effetti come il pendolo di Foucault rivelano la rotazione terrestre.
- Il primo principio è logicamente precedente al secondo, perché fissa i riferimenti in cui questo vale.

## 3.2 Secondo principio della dinamica

Il **secondo principio della dinamica**, o **legge fondamentale della dinamica**, stabilisce la relazione quantitativa tra la causa del moto accelerato, la forza, e il suo effetto, l'accelerazione. In un sistema di riferimento inerziale esso si scrive

$$\vec F = m\,\vec a ,$$

dove $\vec F$ è la **risultante** di tutte le forze agenti sul punto materiale, $m$ la sua massa (inerziale) e $\vec a$ l'accelerazione. L'equazione è vettoriale ed equivale a tre equazioni scalari, una per ogni componente: $F_x = m\ddot x$, $F_y = m\ddot y$, $F_z = m\ddot z$. Essa afferma che l'accelerazione ha sempre la stessa direzione e lo stesso verso della forza risultante (non della velocità) e un modulo direttamente proporzionale alla forza e inversamente proporzionale alla massa. Il secondo principio è valido in tutti i sistemi inerziali e, combinato con le leggi di forza specifiche, permette di prevedere il moto dei corpi.

### 3.2.1 Forza

Una **forza** è la grandezza fisica che descrive l'interazione tra corpi e che è responsabile delle variazioni del loro stato di moto (effetto **dinamico**) o delle loro deformazioni (effetto **statico**). Le forze sono grandezze **vettoriali**: per descriverle occorre specificare modulo, direzione, verso e punto di applicazione. L'evidenza sperimentale che le forze si compongono secondo la regola del parallelogramma, cioè si sommano come vettori, è un fatto fisico, non una conseguenza matematica, e costituisce il cosiddetto **principio di sovrapposizione**: l'effetto di più forze agenti simultaneamente su un punto è uguale all'effetto della loro somma vettoriale, e ciascuna forza agisce indipendentemente dalle altre.

Dal punto di vista operativo, l'intensità di una forza si può misurare staticamente con un **dinamometro**, cioè una molla tarata il cui allungamento è proporzionale alla forza applicata (legge di Hooke), oppure dinamicamente misurando l'accelerazione che essa imprime a una massa nota. L'unità di misura SI è il **newton**: $1\ \mathrm{N}$ è la forza che imprime a un corpo di massa $1\ \mathrm{kg}$ un'accelerazione di $1\ \mathrm{m/s^2}$, quindi $1\ \mathrm{N} = 1\ \mathrm{kg\,m/s^2}$. Per avere un'idea, il peso di una mela di circa $100\ \mathrm{g}$ è di circa $1\ \mathrm{N}$.

Le forze che si incontrano in meccanica si distinguono in **forze a distanza**, come la forza gravitazionale e quella elettrica o magnetica, che agiscono senza contatto attraverso un campo, e **forze di contatto**, come le reazioni vincolari, l'attrito, la tensione di un filo, la spinta di un fluido, che si manifestano quando due corpi si toccano. A livello microscopico anche le forze di contatto sono di origine elettromagnetica, derivando dalle interazioni tra gli elettroni e i nuclei degli atomi delle superfici affacciate. Le **interazioni fondamentali** note sono quattro: gravitazionale, elettromagnetica, nucleare forte e nucleare debole; solo le prime due hanno un raggio d'azione macroscopico e sono quindi rilevanti per la meccanica ordinaria.

### 3.2.2 Massa

La **massa inerziale** è la grandezza scalare che misura l'inerzia di un corpo, cioè la sua resistenza a variare la velocità sotto l'azione di una forza: a parità di forza, un corpo con massa doppia subisce un'accelerazione dimezzata. Operativamente, il rapporto tra le masse di due corpi si può determinare applicando a entrambi la stessa forza (ad esempio con la stessa molla compressa della stessa quantità) e misurando le accelerazioni: $m_1/m_2 = a_2/a_1$. Fissata una massa campione (il chilogrammo), si può così misurare qualunque altra massa. La massa è una grandezza **additiva** (la massa di un sistema è la somma delle masse delle parti), **positiva** e, in meccanica classica, **invariante**: non dipende dalla velocità né dal sistema di riferimento.

Va distinta dalla massa inerziale la **massa gravitazionale**, la proprietà dei corpi di attrarsi reciprocamente per effetto della gravità e di essere attratti dalla Terra. Il **peso** di un corpo è la forza gravitazionale che la Terra esercita su di esso, $\vec P = m\vec g$. Il fatto sperimentale che tutti i corpi cadano con la stessa accelerazione (Galileo) implica che massa inerziale e massa gravitazionale siano proporzionali, e con un'opportuna scelta delle unità uguali. Questa uguaglianza è stata verificata con precisione straordinaria, fino a una parte su $10^{15}$ in esperimenti moderni, ed è uno dei pilastri della relatività generale. Peso e massa vanno comunque distinti concettualmente: la massa è una proprietà intrinseca del corpo e si misura in chilogrammi, il peso è una forza che dipende dal luogo e si misura in newton. Un astronauta sulla Luna ha la stessa massa che sulla Terra, ma pesa circa un sesto.

### 3.2.3 Struttura della materia

Il modello del punto materiale ignora la struttura interna dei corpi, ma è utile richiamare che cosa sappiamo della **struttura della materia** per comprendere sia l'origine delle forze sia i limiti di validità della meccanica classica. La materia ordinaria è costituita da **atomi**, di dimensioni dell'ordine di $10^{-10}\ \mathrm{m}$, formati da un **nucleo** molto piccolo ($\sim10^{-15}\ \mathrm{m}$) e denso, contenente protoni (carica $+e$) e neutroni (neutri), circondato da elettroni (carica $-e$). Le masse caratteristiche sono $m_p \simeq m_n \simeq 1{,}67\times10^{-27}\ \mathrm{kg}$ e $m_e \simeq 9{,}11\times10^{-31}\ \mathrm{kg}$: quasi tutta la massa di un atomo è concentrata nel nucleo, mentre il suo volume è determinato dalla nube elettronica. Gli atomi si legano in **molecole** e, nei solidi, si organizzano spesso in reticoli cristallini ordinati.

Questa struttura spiega perché un corpo macroscopico, contenente un numero di atomi dell'ordine del numero di Avogadro ($N_A \simeq 6{,}022\times10^{23}\ \mathrm{mol^{-1}}$), possa essere trattato come un continuo: le grandezze macroscopiche (massa, densità, forza di contatto) sono medie su un numero enorme di costituenti. Spiega anche l'origine delle forze di contatto: quando due corpi si avvicinano, le nubi elettroniche superficiali si respingono, generando le reazioni vincolari; la deformazione dei legami interatomici produce le forze elastiche. Infine, chiarisce l'ambito di validità della meccanica newtoniana: per descrivere il comportamento dei singoli elettroni e atomi occorre la meccanica quantistica, e per particelle con velocità prossime a quella della luce la relatività.

### 3.2.4 Problema fondamentale della dinamica

Il **problema fondamentale della dinamica** consiste nel determinare il moto di un punto materiale note le forze che agiscono su di esso e le condizioni iniziali. Poiché le forze dipendono in generale dalla posizione, dalla velocità e dal tempo, il secondo principio diventa un'**equazione differenziale** del secondo ordine nell'incognita $\vec r(t)$:

$$m\,\frac{d^2\vec r}{dt^2} = \vec F\!\left(\vec r, \frac{d\vec r}{dt}, t\right).$$

La teoria delle equazioni differenziali garantisce che, sotto ipotesi di regolarità ampiamente soddisfatte dalle forze fisiche, la soluzione esiste ed è unica una volta assegnate la posizione iniziale $\vec r_0$ e la velocità iniziale $\vec v_0$. Questa è l'essenza del **determinismo** della meccanica classica: lo stato presente (posizione e velocità) determina univocamente l'evoluzione futura. Esistono casi in cui, pur valendo il determinismo in linea di principio, piccolissime incertezze sulle condizioni iniziali crescono esponenzialmente nel tempo, rendendo impossibile la previsione a lungo termine (sistemi **caotici**, come l'atmosfera).

Alcuni casi notevoli possono essere risolti analiticamente. Se la forza è **costante** (ad esempio il peso), l'accelerazione è costante e si ritrovano il moto uniformemente accelerato e il moto parabolico. Se la forza è **elastica**, $F = -kx$, si ottiene $\ddot x + (k/m)x = 0$, cioè un moto armonico con pulsazione $\omega = \sqrt{k/m}$. Se la forza dipende dalla velocità, come una resistenza viscosa $F = -bv$, il moto rallenta esponenzialmente con costante di tempo $\tau = m/b$. Il procedimento operativo si articola in passi ben precisi: scegliere un sistema di riferimento inerziale; isolare il corpo e disegnare il **diagramma di corpo libero**, con tutte le forze agenti su di esso; scrivere il secondo principio proiettato sugli assi; risolvere le equazioni con le condizioni iniziali; verificare dimensioni e ordini di grandezza del risultato. Esiste anche il **problema inverso**: noto il moto, ricavare la forza, $\vec F = m\ddot{\vec r}$. Fu proprio risolvendo il problema inverso per le orbite planetarie descritte dalle leggi di Keplero che Newton scoprì la legge di gravitazione universale.

### 3.2.5 Quantità di moto

Si definisce **quantità di moto** (o momento lineare) di un punto materiale il vettore

$$\vec p = m\,\vec v ,$$

misurato in $\mathrm{kg\,m/s}$. Con questa grandezza il secondo principio assume la forma più generale, originariamente data da Newton:

$$\vec F = \frac{d\vec p}{dt}.$$

Se la massa è costante questa forma coincide con $\vec F = m\vec a$; essa rimane però valida anche in situazioni in cui la massa del sistema varia (come in un razzo che espelle gas, purché si tratti correttamente il sistema), ed è la forma che si generalizza alla relatività. Il contenuto fisico è chiaro: la forza misura la rapidità con cui varia la quantità di moto.

Integrando nel tempo si ottiene il **teorema dell'impulso**:

$$\vec J = \int_{t_1}^{t_2}\vec F\,dt = \vec p_2 - \vec p_1 = \Delta\vec p ,$$

dove $\vec J$ è l'**impulso** della forza, misurato in $\mathrm{N\,s}$ (equivalente a $\mathrm{kg\,m/s}$). Questo teorema è particolarmente utile quando le forze agiscono per tempi molto brevi e con intensità molto elevata e difficilmente misurabile istante per istante, come negli **urti**: si può ricavare la forza media $\vec F_m = \Delta\vec p/\Delta t$ dalla variazione di quantità di moto e dalla durata dell'interazione. Il principio di funzionamento di airbag, caschi e paraurti deformabili si basa proprio sull'aumento del tempo di urto, che a parità di variazione di quantità di moto riduce la forza media.

Infine, se la risultante delle forze è nulla, la quantità di moto si conserva: $\vec F = 0 \Rightarrow \vec p = $ costante. Per un singolo punto ciò riformula il principio d'inerzia; per un sistema di punti, come si vedrà, porterà alla **conservazione della quantità di moto** dei sistemi isolati, una delle leggi più generali della fisica.

### Esercizio d'esempio

**Testo.** Una pallina da tennis di massa $m = 57{,}0\ \mathrm{g}$ arriva perpendicolarmente su una racchetta con velocità di modulo $v_1 = 25{,}0\ \mathrm{m/s}$ e viene rinviata nella stessa direzione ma in verso opposto con velocità $v_2 = 35{,}0\ \mathrm{m/s}$. Il contatto dura $\Delta t = 4{,}50\ \mathrm{ms}$. Calcolare l'impulso ricevuto dalla pallina, la forza media esercitata dalla racchetta e l'accelerazione media della pallina; confrontare la forza con il peso della pallina.

**Soluzione.** Si sceglie l'asse $x$ nel verso della velocità finale. Allora $v_{1x} = -25{,}0\ \mathrm{m/s}$ e $v_{2x} = +35{,}0\ \mathrm{m/s}$. La variazione di quantità di moto è

$$\Delta p_x = m(v_{2x} - v_{1x}) = 0{,}0570\ \mathrm{kg}\cdot(35{,}0 + 25{,}0)\ \mathrm{m/s} = 3{,}42\ \mathrm{kg\,m/s}.$$

Per il teorema dell'impulso $J_x = 3{,}42\ \mathrm{N\,s}$. La forza media è

$$F_m = \frac{J_x}{\Delta t} = \frac{3{,}42\ \mathrm{N\,s}}{4{,}50\times10^{-3}\ \mathrm{s}} = 760\ \mathrm{N},$$

e l'accelerazione media $a_m = F_m/m = 760/0{,}0570\ \mathrm{m/s^2} \simeq 1{,}33\times10^{4}\ \mathrm{m/s^2}$, oltre mille volte $g$. Il peso della pallina vale $mg = 0{,}0570\cdot9{,}81\ \mathrm{N} \simeq 0{,}559\ \mathrm{N}$: il rapporto $F_m/(mg) \simeq 1{,}4\times10^{3}$ giustifica pienamente la consueta approssimazione di trascurare il peso durante un urto.

### Punti chiave

- In un riferimento inerziale vale $\vec F = m\vec a$, con $\vec F$ risultante di tutte le forze; l'accelerazione è parallela alla forza.
- Le forze sono vettori che si sommano per sovrapposizione; si misurano con dinamometri e l'unità SI è il newton.
- La massa inerziale misura l'inerzia; è sperimentalmente uguale alla massa gravitazionale, per cui tutti i corpi cadono con la stessa $g$.
- Massa (kg) e peso (N) sono concettualmente distinti: il peso dipende dal luogo, la massa no.
- La struttura atomica della materia spiega l'origine elettromagnetica delle forze di contatto e i limiti della meccanica classica.
- Il problema fondamentale della dinamica è un'equazione differenziale del secondo ordine: note forze e condizioni iniziali, il moto è determinato.
- La forma generale del secondo principio è $\vec F = d\vec p/dt$; l'impulso di una forza uguaglia la variazione di quantità di moto.

## 3.3 Terzo principio della dinamica

Il **terzo principio della dinamica**, o **principio di azione e reazione**, afferma:

> Quando un corpo A esercita una forza su un corpo B, il corpo B esercita simultaneamente sul corpo A una forza uguale in modulo, avente la stessa retta d'azione e verso opposto.

In simboli, indicando con $\vec F_{AB}$ la forza esercitata da A su B e con $\vec F_{BA}$ quella esercitata da B su A,

$$\vec F_{BA} = -\vec F_{AB}.$$

Il principio esprime il fatto che le forze nascono sempre da **interazioni** tra coppie di corpi: non esiste una forza "isolata", ma ogni forza ha la sua controparte agente sull'altro corpo coinvolto. Le due forze della coppia si dicono **azione** e **reazione**, ma la distinzione è puramente convenzionale: nessuna delle due precede l'altra o ne è la causa. Il principio vale per tutte le forze di contatto e per le forze a distanza della gravitazione e dell'elettrostatica; si dice che esso vale in **forma forte** quando, oltre a essere opposte, le due forze giacciono sulla retta che congiunge i due punti (forze **centrali**). Esistono situazioni, come l'interazione magnetica tra cariche in moto, in cui il principio nella forma newtoniana non è verificato istante per istante; in quei casi la conservazione della quantità di moto è recuperata attribuendo quantità di moto al campo elettromagnetico. Per tutti i problemi di meccanica di questo corso il terzo principio vale senza restrizioni.

### 3.3.1 Reazioni vincolari

Un **vincolo** è un qualsiasi dispositivo che limita le possibilità di movimento di un corpo: un piano d'appoggio, una guida, un filo, un perno, una cerniera. I vincoli agiscono sul corpo mediante forze dette **reazioni vincolari**, che hanno la caratteristica di non essere note a priori: il loro valore si adatta, entro certi limiti, a quanto necessario per impedire i movimenti che il vincolo non consente. Esse si determinano quindi come incognite del problema dinamico, imponendo che il moto rispetti il vincolo. Questo le distingue dalle **forze attive** (peso, forza elastica, forza elettrica), la cui espressione è data da una legge nota indipendentemente dal moto.

Il caso più semplice è un corpo appoggiato su un piano orizzontale. Il piano impedisce al corpo di penetrarvi esercitando una forza perpendicolare alla superficie, detta **reazione normale** $\vec N$. Se il corpo è in quiete, il secondo principio lungo la verticale impone $N - mg = 0$, cioè $N = mg$. Se però il corpo è spinto verso il basso da una forza aggiuntiva, o si trova in un ascensore che accelera verso l'alto con accelerazione $a$, la reazione cambia: $N = m(g + a)$. La bilancia pesapersone misura appunto la reazione normale, e non il peso, il che spiega la sensazione di "pesare di più" quando l'ascensore parte verso l'alto. Quando $N$ calcolata risulta negativa, significa che il vincolo dovrebbe "tirare" il corpo, cosa che un semplice appoggio non può fare: il corpo si stacca. Il vincolo di appoggio è infatti **unilatero**, cioè può esercitare forze solo in un verso; una guida in cui il corpo scorre intrappolato è invece **bilatera**.

Se il vincolo è **liscio** (ideale), la reazione è perpendicolare alla superficie o alla guida e quindi non compie lavoro durante uno scorrimento. Se il vincolo è **scabro**, oltre alla componente normale compare una componente tangenziale, la **forza di attrito**, che si oppone allo scorrimento relativo. L'attrito radente statico può assumere qualunque valore fino a un massimo $f_s \le \mu_s N$, dove $\mu_s$ è il coefficiente di attrito statico; durante lo scorrimento vale $f_d = \mu_d N$, con $\mu_d$ coefficiente di attrito dinamico, solitamente un po' minore di $\mu_s$. Le leggi dell'attrito sono leggi empiriche approssimate, studiate in dettaglio nel capitolo dedicato agli esempi di forze.

Un altro vincolo molto comune è il **filo** ideale, cioè inestensibile, di massa trascurabile e perfettamente flessibile. Il filo esercita sul corpo a cui è attaccato una forza diretta lungo il filo stesso e sempre di trazione, detta **tensione** $\vec T$; un filo non può spingere (vincolo unilatero). Se il filo è privo di massa e scorre su carrucole ideali (prive di massa e di attrito), la tensione ha lo stesso modulo in tutti i suoi punti: questa proprietà discende dal secondo principio applicato a un tratto di filo di massa nulla, per il quale la risultante delle forze deve essere nulla qualunque sia l'accelerazione. L'inestensibilità impone inoltre un legame cinematico tra i moti dei corpi collegati, ad esempio uguali moduli di accelerazione per due masse appese ai capi di una carrucola fissa.

### 3.3.2 Azione e reazione

Il punto concettuale più importante, e più spesso frainteso, del terzo principio è che **azione e reazione agiscono su corpi diversi**. Di conseguenza esse non si fanno mai equilibrio tra loro: per stabilire se un corpo è in equilibrio o accelera bisogna considerare solo le forze che agiscono **su di esso**. Si consideri un libro appoggiato su un tavolo. Sul libro agiscono il peso $\vec P$ (forza della Terra sul libro) e la reazione normale $\vec N$ (forza del tavolo sul libro). In equilibrio $\vec N = -\vec P$, ma queste due forze **non** costituiscono una coppia azione-reazione: agiscono sullo stesso corpo e sono uguali e opposte solo perché il libro è in equilibrio (se il tavolo fosse in un ascensore accelerato, non lo sarebbero). Le vere coppie azione-reazione sono: il peso del libro, forza della Terra sul libro, e la forza con cui il libro attrae la Terra, applicata al centro della Terra; la forza del tavolo sul libro e la forza con cui il libro preme sul tavolo.

Un classico "paradosso" aiuta a chiarire: se il cavallo tira il carro con una forza e il carro tira il cavallo con forza uguale e opposta, come fa il sistema a muoversi? La risposta è che il moto del carro dipende solo dalle forze applicate al carro (la trazione del cavallo e l'attrito del terreno sulle ruote), mentre il moto del cavallo dipende dalle forze applicate al cavallo (la reazione del carro e la forza di attrito che il terreno esercita sugli zoccoli, diretta in avanti perché il cavallo spinge il terreno all'indietro). Il sistema accelera se la forza in avanti che il terreno esercita sul cavallo supera l'attrito che si oppone al rotolamento del carro.

Il terzo principio è alla base di numerosi fenomeni e applicazioni. La **propulsione** di qualsiasi mezzo si basa su di esso: un'auto avanza perché le ruote motrici spingono l'asfalto all'indietro e l'asfalto, per reazione, spinge l'auto in avanti attraverso l'attrito statico; un nuotatore spinge l'acqua indietro; un razzo espelle i gas di scarico ad alta velocità e ne riceve una spinta uguale e contraria, il che gli consente di accelerare anche nel vuoto. Il **rinculo** di un'arma da fuoco è la reazione alla forza che spinge il proiettile. Un'importante conseguenza del terzo principio, unito al secondo, è che in un sistema di corpi le forze interne si cancellano a coppie nella somma: per due corpi isolati che interagiscono, $\frac{d\vec p_A}{dt} = \vec F_{BA}$ e $\frac{d\vec p_B}{dt} = \vec F_{AB}$, quindi

$$\frac{d}{dt}(\vec p_A + \vec p_B) = \vec F_{BA} + \vec F_{AB} = \vec 0 .$$

La quantità di moto totale di un sistema isolato si conserva: il terzo principio è equivalente, per sistemi di due corpi, alla conservazione della quantità di moto. Questa connessione si può anche rovesciare per dare una definizione operativa del rapporto tra masse: in un'interazione isolata tra due corpi le accelerazioni sono opposte e inversamente proporzionali alle masse, $m_A/m_B = |\vec a_B|/|\vec a_A|$. Il terzo principio va quindi inteso non solo come regola pratica per i diagrammi di corpo libero, ma come espressione di una proprietà profonda delle interazioni fisiche.

### Esercizio d'esempio

**Testo.** Due blocchi di massa $m_1 = 4{,}00\ \mathrm{kg}$ e $m_2 = 6{,}00\ \mathrm{kg}$ sono a contatto su un piano orizzontale liscio. Una forza orizzontale $F = 30{,}0\ \mathrm{N}$ spinge il blocco 1, che a sua volta spinge il blocco 2. Calcolare: (a) l'accelerazione del sistema; (b) la forza di contatto tra i blocchi; (c) le reazioni normali del piano su ciascun blocco. Verificare il terzo principio.

**Soluzione.** (a) I blocchi restano a contatto e hanno la stessa accelerazione $a$. Considerando il sistema dei due blocchi, le forze di contatto interne si cancellano per il terzo principio, e lungo l'orizzontale resta solo $F$:

$$a = \frac{F}{m_1 + m_2} = \frac{30{,}0\ \mathrm{N}}{10{,}0\ \mathrm{kg}} = 3{,}00\ \mathrm{m/s^2}.$$

(b) Sul blocco 2 agisce orizzontalmente soltanto la forza di contatto $F_{12}$ esercitata dal blocco 1:

$$F_{12} = m_2 a = 6{,}00\ \mathrm{kg}\cdot3{,}00\ \mathrm{m/s^2} = 18{,}0\ \mathrm{N}.$$

Verifica sul blocco 1: su di esso agiscono $F$ in avanti e la reazione $F_{21} = -F_{12}$ all'indietro, quindi $F - F_{21} = m_1 a$, ossia $30{,}0 - 18{,}0 = 12{,}0\ \mathrm{N} = 4{,}00\cdot3{,}00\ \mathrm{N}$. Le due forze di contatto sono uguali e opposte e agiscono su corpi diversi, come previsto.

(c) Lungo la verticale non c'è accelerazione, quindi $N_1 = m_1 g = 39{,}2\ \mathrm{N}$ e $N_2 = m_2 g = 58{,}9\ \mathrm{N}$. Si noti che la forza di contatto è minore di $F$: se la spinta fosse applicata al blocco più leggero dall'altra parte, la forza di contatto varrebbe $m_1 a = 12{,}0\ \mathrm{N}$.

### Punti chiave

- Ogni forza nasce da un'interazione: se A agisce su B con $\vec F_{AB}$, B agisce su A con $\vec F_{BA} = -\vec F_{AB}$.
- Azione e reazione agiscono su corpi diversi e quindi non si equilibrano mai tra loro.
- Le reazioni vincolari non sono note a priori: si determinano imponendo il rispetto del vincolo.
- Un vincolo liscio esercita solo una reazione normale; un vincolo scabro anche una componente di attrito.
- Un filo ideale trasmette una tensione uniforme e impone legami cinematici tra i corpi collegati.
- Peso e reazione normale di un corpo appoggiato non sono una coppia azione-reazione.
- Per un sistema isolato il terzo principio implica la conservazione della quantità di moto totale.

## 3.4 Grandezze angolari

Molti moti hanno un carattere rotatorio: un punto che percorre una circonferenza, un pianeta che orbita attorno al Sole, un pendolo che oscilla attorno al punto di sospensione. Per descriverli in modo efficace è utile introdurre grandezze che tengano conto non solo dell'intensità di forze e velocità, ma anche della loro **posizione** rispetto a un punto di riferimento, detto **polo**. Le grandezze angolari fondamentali sono il **momento della forza**, il **momento d'inerzia** e il **momento angolare**. Per il punto materiale esse costituiscono una riformulazione delle leggi di Newton; il loro pieno valore emergerà nello studio dei sistemi di punti e dei corpi rigidi, dove il comportamento rotatorio non è riducibile a quello di un singolo punto. Lo strumento matematico essenziale è il **prodotto vettoriale**: dati due vettori $\vec A$ e $\vec B$, il vettore $\vec A\times\vec B$ ha modulo $AB\sin\theta$ (con $\theta$ angolo tra i due), direzione perpendicolare al piano individuato da $\vec A$ e $\vec B$ e verso dato dalla regola della mano destra. Il prodotto vettoriale è anticommutativo, $\vec A\times\vec B = -\vec B\times\vec A$, e si annulla per vettori paralleli.

### 3.4.1 Momento della forza

Il **momento della forza** $\vec F$, applicata nel punto $P$, rispetto al polo $O$ è il vettore

$$\vec M_O = \vec r\times\vec F, \qquad \vec r = \overrightarrow{OP}.$$

Il suo modulo vale $M_O = rF\sin\theta = F\,b$, dove $b = r\sin\theta$ è il **braccio** della forza, cioè la distanza del polo dalla retta d'azione della forza. L'unità SI è il $\mathrm{N\,m}$ (da non confondere con il joule, sebbene dimensionalmente equivalente: il momento è un vettore e non un'energia). La direzione del momento è perpendicolare al piano contenente $\vec r$ e $\vec F$ e individua l'asse attorno al quale la forza tende a far ruotare il corpo; il verso, secondo la regola della mano destra, indica il senso di rotazione (antiorario se il momento punta verso l'osservatore).

Il momento della forza quantifica la **capacità di una forza di produrre rotazione** attorno a un polo. L'esperienza quotidiana ne fornisce molti esempi: è più facile aprire una porta spingendo lontano dai cardini che vicino, perché a parità di forza il braccio è maggiore; una chiave inglese lunga permette di svitare bulloni serrati con forza minore. Se la retta d'azione della forza passa per il polo il braccio è nullo e il momento è nullo: una forza diretta verso i cardini non fa ruotare la porta. Il momento dipende dalla scelta del polo: cambiando polo da $O$ a $O'$ si ha $\vec M_{O'} = \vec M_O + \overrightarrow{O'O}\times\vec F$. Per più forze applicate allo stesso punto, il momento della risultante è uguale alla somma dei momenti (teorema di Varignon), conseguenza della proprietà distributiva del prodotto vettoriale.

Spesso interessa il **momento assiale**, cioè la componente del momento lungo un asse fisso passante per il polo, ad esempio l'asse dei cardini di una porta o l'asse di un albero motore. Essa si ottiene proiettando $\vec M_O$ sul versore dell'asse, $M_z = \vec M_O\cdot\hat k$, e non dipende dalla scelta del polo lungo l'asse. In un problema piano con asse $z$ perpendicolare al piano del moto, il momento ha solo componente $z$ e si può trattare come uno scalare dotato di segno: $M_z = xF_y - yF_x$.

### 3.4.2 Momento d'inerzia

Il **momento d'inerzia** di un punto materiale di massa $m$ rispetto a un asse è la grandezza scalare

$$I = m\,d^2,$$

dove $d$ è la distanza del punto dall'asse. L'unità SI è il $\mathrm{kg\,m^2}$. Il momento d'inerzia gioca nei moti di rotazione lo stesso ruolo che la massa gioca nei moti di traslazione: misura l'**inerzia rotazionale**, cioè la resistenza del corpo a variare la propria velocità angolare. A differenza della massa, però, il momento d'inerzia non è una proprietà intrinseca del corpo ma dipende dall'asse scelto, e in particolare cresce con il quadrato della distanza.

Per comprenderne l'origine si consideri un punto materiale vincolato a ruotare su una circonferenza di raggio $d$ attorno a un asse fisso, ad esempio tramite un'asta rigida di massa trascurabile. Se sul punto agisce una forza con componente tangenziale $F_t$, il secondo principio lungo la tangente dà $F_t = m a_t = m d\,\alpha$, dove $\alpha$ è l'accelerazione angolare. Moltiplicando per il braccio $d$ si ottiene il momento assiale

$$M = F_t\,d = m d^2\,\alpha = I\,\alpha.$$

Questa relazione è l'analogo rotazionale di $F = ma$: un momento applicato produce un'accelerazione angolare inversamente proporzionale al momento d'inerzia. A parità di momento, un corpo con la massa distribuita lontano dall'asse accelera più lentamente. Per un sistema di più punti materiali il momento d'inerzia è additivo, $I = \sum_i m_i d_i^2$, e per un corpo continuo diventa un integrale, $I = \int d^2\,dm$: questi sviluppi saranno affrontati nello studio dei sistemi e del corpo rigido, dove si introdurranno anche teoremi utili come quello di Huygens-Steiner. Già a livello di punto materiale, però, il concetto spiega perché i volani si costruiscono concentrando la massa sulla periferia, o perché un pattinatore che allarga le braccia rallenta la propria rotazione.

Con il momento d'inerzia si esprime anche l'**energia cinetica di rotazione**: per un punto che ruota con velocità angolare $\omega$ attorno all'asse, $v = \omega d$ e $K = \tfrac12 mv^2 = \tfrac12 I\omega^2$, in perfetta analogia con $\tfrac12 mv^2$.

### 3.4.3 Momento angolare

Il **momento angolare** (o momento della quantità di moto) di un punto materiale rispetto al polo $O$ è il vettore

$$\vec L_O = \vec r\times\vec p = \vec r\times m\vec v,$$

misurato in $\mathrm{kg\,m^2/s}$ (equivalente a $\mathrm{J\,s}$). Il suo modulo vale $L_O = r\,m\,v\sin\theta$, e la sua direzione è perpendicolare al piano individuato da posizione e velocità. Per un punto in moto circolare di raggio $R$ attorno a $O$, la velocità è perpendicolare al raggio e $L_O = mRv = mR^2\omega = I\omega$: il momento angolare è perpendicolare al piano dell'orbita e ha modulo pari al prodotto del momento d'inerzia per la velocità angolare, analogo rotazionale di $p = mv$. Anche un punto in moto rettilineo uniforme possiede momento angolare rispetto a un polo che non stia sulla sua traiettoria: $L_O = mvb$, con $b$ distanza del polo dalla retta del moto, ed esso è costante.

La relazione dinamica fondamentale si ottiene derivando $\vec L_O$ rispetto al tempo, con polo $O$ fisso in un riferimento inerziale:

$$\frac{d\vec L_O}{dt} = \frac{d\vec r}{dt}\times m\vec v + \vec r\times m\frac{d\vec v}{dt} = \vec v\times m\vec v + \vec r\times\vec F = \vec M_O,$$

poiché il prodotto vettoriale di un vettore per se stesso è nullo. Si ottiene il **teorema del momento angolare**:

$$\vec M_O = \frac{d\vec L_O}{dt},$$

analogo rotazionale di $\vec F = d\vec p/dt$. Se il polo è in moto con velocità $\vec v_O$ compare un termine aggiuntivo, $-\vec v_O\times m\vec v$, che si annulla se il polo è fisso o se la sua velocità è parallela a quella del punto.

Una conseguenza di grande importanza è la **conservazione del momento angolare**: se il momento delle forze rispetto a $O$ è nullo, $\vec L_O$ è costante. Ciò accade in particolare per le **forze centrali**, cioè forze sempre dirette verso (o da) un centro fisso $O$: in questo caso $\vec r$ e $\vec F$ sono paralleli e $\vec M_O = 0$. Poiché $\vec L_O$ è costante in direzione, il moto avviene in un piano fisso perpendicolare a $\vec L_O$; poiché è costante in modulo, la **velocità areolare** $dA/dt = L_O/(2m)$ è costante, cioè il raggio vettore spazza aree uguali in tempi uguali. È esattamente la seconda legge di Keplero sul moto dei pianeti, che risulta così una conseguenza del carattere centrale della forza gravitazionale. Un altro esempio è una pallina che ruota su un tavolo liscio legata a un filo che passa per un foro centrale: tirando il filo dal basso il raggio diminuisce, la forza resta centrale e la velocità angolare aumenta in modo che $mr^2\omega$ resti costante.

### Esercizio d'esempio

**Testo.** Una pallina di massa $m = 0{,}150\ \mathrm{kg}$ ruota su un tavolo orizzontale liscio, legata a un filo che passa per un foro al centro del tavolo. Inizialmente percorre una circonferenza di raggio $r_1 = 0{,}600\ \mathrm{m}$ con velocità $v_1 = 1{,}20\ \mathrm{m/s}$. Tirando lentamente il filo dal basso, il raggio si riduce a $r_2 = 0{,}300\ \mathrm{m}$. Calcolare: (a) il momento angolare e il momento d'inerzia iniziali rispetto al foro; (b) la velocità e la velocità angolare finali; (c) la tensione del filo nelle due configurazioni.

**Soluzione.** (a) Il momento angolare rispetto al foro vale

$$L = m r_1 v_1 = 0{,}150\cdot0{,}600\cdot1{,}20\ \mathrm{kg\,m^2/s} = 0{,}108\ \mathrm{kg\,m^2/s},$$

e il momento d'inerzia $I_1 = m r_1^2 = 0{,}150\cdot0{,}360\ \mathrm{kg\,m^2} = 5{,}40\times10^{-2}\ \mathrm{kg\,m^2}$, con $\omega_1 = v_1/r_1 = 2{,}00\ \mathrm{rad/s}$.

(b) La tensione è sempre diretta verso il foro: la forza è centrale e il momento rispetto al foro è nullo, mentre peso e reazione normale si bilanciano. Il momento angolare si conserva:

$$v_2 = \frac{r_1}{r_2}v_1 = 2\cdot1{,}20\ \mathrm{m/s} = 2{,}40\ \mathrm{m/s}, \qquad \omega_2 = \frac{v_2}{r_2} = 8{,}00\ \mathrm{rad/s}.$$

Dimezzando il raggio il momento d'inerzia diventa un quarto e la velocità angolare quadruplica.

(c) La tensione fornisce la forza centripeta, $T = mv^2/r$:

$$T_1 = \frac{0{,}150\cdot1{,}20^2}{0{,}600}\ \mathrm{N} = 0{,}360\ \mathrm{N}, \qquad T_2 = \frac{0{,}150\cdot2{,}40^2}{0{,}300}\ \mathrm{N} = 2{,}88\ \mathrm{N}.$$

La tensione aumenta di un fattore $8 = (r_1/r_2)^3$: chi tira il filo compie lavoro, che si ritrova come aumento dell'energia cinetica della pallina.

### Punti chiave

- Il momento della forza $\vec M_O = \vec r\times\vec F$ ha modulo $F\,b$ (forza per braccio) e misura la tendenza a far ruotare.
- Il momento dipende dal polo; il momento assiale, proiezione su un asse, non dipende dal polo scelto sull'asse.
- Il momento d'inerzia $I = md^2$ misura l'inerzia rotazionale e dipende dall'asse; per una rotazione attorno a un asse fisso $M = I\alpha$.
- Il momento angolare $\vec L_O = \vec r\times m\vec v$ vale $I\omega$ nel moto circolare.
- Con polo fisso in un riferimento inerziale vale $\vec M_O = d\vec L_O/dt$.
- Per forze centrali il momento angolare si conserva: moto piano e velocità areolare costante (seconda legge di Keplero).
- Le grandezze angolari sono gli analoghi rotazionali di forza, massa e quantità di moto.

## 3.5 Statica del punto

La **statica** è la parte della meccanica che studia le condizioni di **equilibrio** dei corpi, cioè le situazioni in cui un corpo, inizialmente in quiete, rimane in quiete. Per un punto materiale la statica si deduce direttamente dal secondo principio, imponendo accelerazione nulla, ma ha una sua autonomia sia concettuale sia pratica: nell'ingegneria civile e meccanica la verifica dell'equilibrio di strutture, macchine e componenti è un'attività quotidiana. In questa sezione si formulano le condizioni di equilibrio del punto materiale, si discute la stabilità dell'equilibrio e si presentano le principali forze che entrano nei problemi di statica, con il metodo sistematico per risolverli.

### 3.5.1 Equilibrio

Un punto materiale è in **equilibrio** in un riferimento inerziale se, posto in quiete in una certa posizione, vi rimane indefinitamente. Dal secondo principio, $\vec a = \vec 0$ in ogni istante, e quindi la condizione necessaria e sufficiente (insieme alla velocità iniziale nulla) è che la risultante di tutte le forze agenti sul punto sia nulla:

$$\sum_i \vec F_i = \vec 0 \quad\Longleftrightarrow\quad \sum_i F_{ix} = 0,\ \ \sum_i F_{iy} = 0,\ \ \sum_i F_{iz} = 0.$$

Le tre equazioni scalari consentono di determinare al più tre incognite (nel piano, due), che tipicamente sono reazioni vincolari, tensioni di fili o la posizione di equilibrio stessa. Si osservi che la condizione $\sum\vec F = 0$ è anche soddisfatta da un punto in moto rettilineo uniforme: si parla allora di **equilibrio dinamico**, distinto dall'**equilibrio statico** in cui il punto è fermo. Per il punto materiale la condizione sulle forze è sufficiente; per i corpi estesi, come si vedrà, occorrerà imporre anche che sia nullo il momento risultante, per evitare rotazioni.

Una configurazione di equilibrio può essere di tre tipi, a seconda di come il sistema risponde a una piccola perturbazione. L'equilibrio è **stabile** se, spostato di poco il punto dalla posizione di equilibrio, le forze tendono a riportarvelo: una pallina sul fondo di una scodella. È **instabile** se le forze tendono ad allontanarlo ulteriormente: una pallina in cima a una cupola. È **indifferente** se nelle posizioni vicine il punto è ancora in equilibrio: una pallina su un piano orizzontale. Nel caso unidimensionale, con forza $F(x)$ e posizione di equilibrio $x_e$ tale che $F(x_e) = 0$, l'equilibrio è stabile se $dF/dx < 0$ in $x_e$ (forza di richiamo), instabile se $dF/dx > 0$. Nell'intorno di un equilibrio stabile la forza è approssimativamente lineare, $F \simeq -k(x - x_e)$ con $k = -dF/dx > 0$, e il moto conseguente a una piccola perturbazione è un **moto armonico** con pulsazione $\omega = \sqrt{k/m}$. Questo spiega l'universalità delle piccole oscillazioni in natura. Quando si introdurrà l'energia potenziale, la stabilità sarà riformulata in modo elegante: le posizioni di equilibrio stabile corrispondono ai minimi dell'energia potenziale, quelle instabili ai massimi.

### 3.5.2 Forze

Per risolvere un problema di statica occorre identificare con cura tutte le forze che agiscono sul punto. Le più frequenti sono le seguenti.

Il **peso** $\vec P = m\vec g$, verticale e diretto verso il basso, sempre presente per i corpi nelle vicinanze della superficie terrestre. La **reazione normale** $\vec N$ di una superficie d'appoggio, perpendicolare alla superficie e diretta verso l'esterno; per un vincolo unilatero deve risultare $N \ge 0$. La **forza di attrito statico** $\vec f_s$, tangente alla superficie e opposta alla tendenza allo scivolamento, con modulo che si adatta alle necessità dell'equilibrio fino al valore massimo $\mu_s N$: la condizione di equilibrio su un piano scabro è quindi una **disuguaglianza**, $|f_s| \le \mu_s N$. La **tensione** $\vec T$ di un filo, diretta lungo il filo e sempre di trazione ($T \ge 0$). La **forza elastica** di una molla ideale, $\vec F_e = -k\,\Delta\vec x$, proporzionale alla deformazione e diretta in modo da riportare la molla alla lunghezza di riposo; la costante elastica $k$ si misura in $\mathrm{N/m}$. Infine eventuali **forze esterne** applicate, note in modulo e direzione.

Il metodo di soluzione è sistematico. Si individua il punto di cui studiare l'equilibrio (ad esempio un corpo appeso o il nodo in cui convergono più funi). Si traccia il **diagramma di corpo libero**: si disegna il punto isolato e tutte le forze agenti su di esso, e solo quelle, senza includere le forze che il punto esercita su altri corpi. Si sceglie un sistema di assi conveniente, spesso uno parallelo e uno perpendicolare al piano d'appoggio, in modo che il maggior numero possibile di forze abbia una sola componente. Si scrivono le equazioni di equilibrio per componenti e si risolvono. Si verifica infine la consistenza fisica dei risultati: tensioni e reazioni normali non negative, attrito entro il limite massimo, dimensioni corrette.

Un esempio fondamentale è il **piano inclinato**. Un corpo di massa $m$ poggia su un piano inclinato di un angolo $\theta$ sull'orizzontale. Con l'asse $x$ lungo il piano verso il basso e l'asse $y$ perpendicolare, il peso ha componenti $P_x = mg\sin\theta$ e $P_y = -mg\cos\theta$. L'equilibrio impone $N = mg\cos\theta$ e $f_s = mg\sin\theta$, diretta verso l'alto lungo il piano. La condizione $f_s \le \mu_s N$ diventa $\tan\theta \le \mu_s$: il corpo resta fermo finché l'inclinazione non supera l'**angolo di attrito** $\theta_s = \arctan\mu_s$, indipendente dalla massa. Questa proprietà fornisce un metodo semplice per misurare il coefficiente di attrito statico: si aumenta lentamente l'inclinazione e si registra l'angolo a cui il corpo comincia a scivolare. Se il piano è liscio, invece, l'equilibrio richiede una forza aggiuntiva, ad esempio la tensione di un filo parallelo al piano, $T = mg\sin\theta$: il piano inclinato è una **macchina semplice** che permette di sollevare un carico applicando una forza minore del peso, a prezzo di uno spostamento maggiore.

Un altro esempio classico è un corpo appeso a due funi che formano angoli diversi con la verticale: il problema si riduce all'equilibrio del nodo, sul quale agiscono le due tensioni e la tensione della fune verticale, uguale al peso del corpo. Più le funi sono vicine all'orizzontale, più grandi diventano le tensioni necessarie a sostenere il peso: una fune tesa perfettamente orizzontale non potrebbe mai sostenere un carico appeso al centro, perché la tensione dovrebbe essere infinita. È per questo che i cavi delle linee elettriche presentano sempre una certa freccia.

### Esercizio d'esempio

**Testo.** Un semaforo di massa $m = 15{,}0\ \mathrm{kg}$ è appeso a un nodo da cui partono due cavi fissati a due pali; il cavo sinistro forma un angolo $\alpha = 30{,}0^\circ$ con l'orizzontale, quello destro un angolo $\beta = 50{,}0^\circ$. Calcolare le tensioni dei due cavi. Ciascun cavo può sopportare al massimo $250\ \mathrm{N}$: il sistema è sicuro?

**Soluzione.** Si studia l'equilibrio del nodo, con asse $x$ orizzontale verso destra e asse $y$ verticale verso l'alto. Le forze sul nodo sono il peso trasmesso dal cavo verticale, $P = mg = 15{,}0\cdot9{,}81\ \mathrm{N} = 147\ \mathrm{N}$ verso il basso, la tensione $T_1$ diretta verso sinistra e verso l'alto, la tensione $T_2$ verso destra e verso l'alto. Le equazioni di equilibrio sono

$$\begin{cases} -T_1\cos\alpha + T_2\cos\beta = 0\\ T_1\sin\alpha + T_2\sin\beta - mg = 0\end{cases}$$

Dalla prima $T_1 = T_2\cos\beta/\cos\alpha$. Sostituendo nella seconda:

$$T_2\left(\frac{\cos\beta\sin\alpha}{\cos\alpha} + \sin\beta\right) = mg \;\Rightarrow\; T_2 = \frac{mg\cos\alpha}{\sin(\alpha+\beta)} = \frac{147\cdot0{,}866}{\sin80{,}0^\circ}\ \mathrm{N} = \frac{127{,}4}{0{,}985}\ \mathrm{N}\simeq 129\ \mathrm{N}.$$

Analogamente $T_1 = mg\cos\beta/\sin(\alpha+\beta) = 147\cdot0{,}643/0{,}985\ \mathrm{N} \simeq 96{,}0\ \mathrm{N}$. Il cavo più ripido è il più sollecitato. Entrambe le tensioni sono inferiori al limite di $250\ \mathrm{N}$, con un coefficiente di sicurezza di circa $1{,}9$ sul cavo destro: il sistema è sicuro. Si noti che la somma delle tensioni, $225\ \mathrm{N}$, supera il peso: le componenti orizzontali, pur cancellandosi, "costano" tensione aggiuntiva.

### Punti chiave

- Un punto materiale è in equilibrio se e solo se la risultante delle forze è nulla e la velocità iniziale è nulla.
- Le equazioni di equilibrio si scrivono per componenti: tre nello spazio, due nel piano.
- L'equilibrio è stabile, instabile o indifferente a seconda della risposta a piccole perturbazioni; attorno a un equilibrio stabile il moto è armonico.
- Il diagramma di corpo libero include solo le forze agenti sul punto considerato.
- L'attrito statico si adatta all'equilibrio fino al massimo $\mu_sN$; su un piano inclinato il corpo resta fermo se $\tan\theta \le \mu_s$.
- Tensioni e reazioni normali devono risultare non negative; in caso contrario il vincolo cede o il corpo si stacca.
- Funi poco inclinate rispetto all'orizzontale richiedono tensioni molto grandi per sostenere un carico.
