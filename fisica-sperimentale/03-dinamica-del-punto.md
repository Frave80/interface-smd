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

**Testo.** Un disco a cuscino d'aria di massa $m = 0{,}200\ \mathrm{kg}$ viene lanciato su un tavolo orizzontale con velocità $v_0 = 0{,}800\ \mathrm{m/s}$. Le posizioni registrate ogni $0{,}500\ \mathrm{s}$ sono $0{,}000$; $0{,}399$; $0{,}797$; $1{,}194$; $1{,}590\ \mathrm{m}$. (a) Verificare se il moto è compatibile con il principio d'inerzia. (b) Stimare l'eventuale forza residua di attrito. (c) Valutare quanto la rotazione terrestre (con accelerazione centripeta massima $a_c \simeq 3{,}4\times10^{-2}\ \mathrm{m/s^2}$, in gran parte compensata dalla definizione stessa di verticale locale) possa influire sul risultato, confrontando con una forza dell'ordine di $m\,\omega_T v_0$, tipica dell'effetto di Coriolis.

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
