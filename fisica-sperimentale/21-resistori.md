# Capitolo 21 — Resistori

Nel capitolo precedente abbiamo introdotto la corrente elettrica come flusso ordinato di cariche e ne abbiamo descritto le grandezze fondamentali: intensità di corrente, densità di corrente ed equazione di continuità. Resta però aperta una domanda centrale: che cosa determina *quanta* corrente circola in un materiale quando gli si applica una differenza di potenziale? La risposta conduce al concetto di **resistenza elettrica** e al componente circuitale che la realizza, il **resistore**. In questo capitolo formuliamo le leggi di Ohm nella forma macroscopica e locale, ne diamo un'interpretazione microscopica tramite il modello classico di Drude, studiamo la dissipazione di energia per effetto Joule, impariamo a combinare resistori in serie e in parallelo e concludiamo con il fenomeno sorprendente della superconduttività, in cui la resistenza si annulla del tutto. Si tratta di argomenti che costituiscono la base dell'elettrotecnica e dell'elettronica e che lo studente di Ingegneria ritroverà in ogni corso successivo.

## 21.1 Resistenza elettrica

Quando un conduttore viene inserito tra due punti mantenuti a potenziale diverso, al suo interno si stabilisce un campo elettrico che mette in moto i portatori di carica liberi. In condizioni elettrostatiche, come visto nel capitolo sui materiali conduttori, il campo all'interno di un conduttore è nullo; ma se un agente esterno (un generatore) mantiene costante la differenza di potenziale, l'equilibrio elettrostatico non viene mai raggiunto e nel conduttore scorre una corrente stazionaria. L'esperienza mostra che, per un'ampia classe di materiali e in un vasto intervallo di condizioni, la corrente è proporzionale alla tensione applicata. Questo risultato, scoperto sperimentalmente da Georg Simon Ohm negli anni Venti dell'Ottocento, è il punto di partenza della teoria dei circuiti.

### 21.1.1 Prima legge di Ohm

Consideriamo un tratto di conduttore ai cui estremi A e B è applicata una **differenza di potenziale** (o **tensione**) $\Delta V = V_A - V_B$, e indichiamo con $i$ l'intensità di corrente che lo attraversa da A verso B. La **prima legge di Ohm** afferma che, per i cosiddetti **conduttori ohmici**, il rapporto fra tensione e corrente è una costante caratteristica del conduttore, indipendente dal valore della tensione stessa:

$$
\Delta V = R\, i .
$$

La costante $R$ prende il nome di **resistenza elettrica** del conduttore; nel Sistema Internazionale si misura in **ohm** ($\Omega$), con $1\ \Omega = 1\ \mathrm{V/A}$. L'inverso della resistenza è la **conduttanza** $G = 1/R$, che si misura in **siemens** ($\mathrm{S} = \Omega^{-1}$). Un componente progettato per avere una resistenza ben definita si chiama **resistore**; nei circuiti viene rappresentato con una linea a zig-zag o con un rettangolo.

È importante comprendere bene il contenuto fisico di questa legge. La relazione $\Delta V = R i$ potrebbe sembrare una semplice definizione di $R$; ma ciò che la rende una legge fisica è l'affermazione che $R$ *non dipende* da $\Delta V$ né da $i$. In un grafico corrente-tensione, la cosiddetta **caratteristica tensione-corrente**, un conduttore ohmico è rappresentato da una retta passante per l'origine, la cui pendenza è $1/R$. Molti dispositivi non obbediscono a questa legge: un diodo a semiconduttore, ad esempio, conduce quasi solo in un verso e la sua corrente cresce esponenzialmente con la tensione; una lampadina a incandescenza ha una caratteristica che si incurva perché la temperatura del filamento, e con essa la resistenza, aumenta al crescere della potenza dissipata. Per questi dispositivi si può comunque definire una **resistenza statica** $R = \Delta V / i$ o una **resistenza differenziale** $r = \mathrm{d}(\Delta V)/\mathrm{d}i$, ma tali grandezze dipendono dal punto di lavoro.

Un'altra osservazione riguarda la convenzione dei segni. Se la corrente scorre nel verso dei potenziali decrescenti, cioè dal punto a potenziale maggiore verso quello a potenziale minore, il prodotto $R i$ coincide con la **caduta di tensione** ai capi del resistore. Questa convenzione, detta **degli utilizzatori**, sarà fondamentale nello scrivere le leggi di Kirchhoff nel capitolo successivo: attraversando un resistore nel verso della corrente il potenziale diminuisce di $R i$.

Infine, la resistenza di un conduttore metallico dipende dalla temperatura. Per i metalli, in un intervallo non troppo ampio attorno alla temperatura ambiente, vale con buona approssimazione la legge lineare

$$
R(T) = R_0\,[1 + \alpha\,(T - T_0)],
$$

dove $\alpha$ è il **coefficiente termico di resistività**, positivo e dell'ordine di $4\times 10^{-3}\ \mathrm{K^{-1}}$ per il rame. Questa dipendenza è sfruttata nei termometri a resistenza di platino (Pt100), largamente impiegati nell'industria.

### 21.1.2 Seconda legge di Ohm

La prima legge descrive il comportamento di un conduttore nel suo insieme, ma non spiega da che cosa dipenda il valore di $R$. Esperimenti condotti su fili dello stesso materiale ma di dimensioni diverse mostrano che la resistenza cresce proporzionalmente alla lunghezza $\ell$ del filo e decresce in modo inversamente proporzionale alla sua sezione $S$. La **seconda legge di Ohm** lo esprime nella forma

$$
R = \rho\,\frac{\ell}{S},
$$

dove $\rho$ è la **resistività** del materiale, misurata in $\Omega\cdot\mathrm{m}$. La resistività è una proprietà *intensiva*, che dipende solo dalla natura del materiale e dal suo stato (temperatura, pressione, purezza, struttura cristallina), mentre la resistenza è una proprietà del singolo oggetto, che dipende anche dalla sua geometria. L'inverso della resistività è la **conducibilità elettrica** $\sigma = 1/\rho$, misurata in $\mathrm{S/m}$.

La dipendenza da $\ell$ e da $S$ ha un'interpretazione intuitiva. Un filo lungo $2\ell$ si può pensare come due fili lunghi $\ell$ collegati uno dopo l'altro: la stessa corrente deve attraversarli entrambi e le cadute di tensione si sommano, sicché la resistenza raddoppia. Un filo di sezione $2S$ equivale invece a due fili di sezione $S$ affiancati: la corrente si divide fra due percorsi paralleli e la resistenza si dimezza. Anticipiamo così, in forma qualitativa, le regole di composizione in serie e in parallelo che studieremo nella sezione 21.4.

La resistività varia di moltissimi ordini di grandezza da un materiale all'altro, più di qualunque altra proprietà fisica comune. I buoni conduttori metallici, come argento ($1{,}6\times10^{-8}\ \Omega\,\mathrm{m}$), rame ($1{,}7\times10^{-8}\ \Omega\,\mathrm{m}$) e alluminio ($2{,}8\times10^{-8}\ \Omega\,\mathrm{m}$), hanno resistività dell'ordine di $10^{-8}\ \Omega\,\mathrm{m}$. Le leghe resistive come la costantana o il nichel-cromo arrivano a circa $10^{-6}\ \Omega\,\mathrm{m}$ e hanno coefficienti termici molto piccoli, il che le rende adatte per resistori di precisione o elementi riscaldanti. I semiconduttori, come silicio e germanio, presentano resistività intermedie e fortemente dipendenti dal drogaggio e dalla temperatura; a differenza dei metalli, la loro resistività *diminuisce* al crescere di $T$, perché aumenta il numero di portatori liberi. Gli isolanti, come vetro, quarzo o polimeri, raggiungono valori da $10^{10}$ a oltre $10^{16}\ \Omega\,\mathrm{m}$. Nel complesso l'intervallo copre più di venti ordini di grandezza.

La seconda legge di Ohm, nella forma scritta, vale per un conduttore omogeneo, di sezione costante, percorso da una corrente distribuita uniformemente sulla sezione. Se la sezione varia lungo il conduttore, o se il materiale non è omogeneo, occorre suddividere il conduttore in fette infinitesime di spessore $\mathrm{d}\ell$ e sommarne i contributi in serie:

$$
R = \int_{A}^{B} \frac{\rho(\ell)}{S(\ell)}\,\mathrm{d}\ell .
$$

Questa espressione permette ad esempio di calcolare la resistenza di un tronco di cono o di un guscio cilindrico percorso da corrente radiale, situazioni tipiche dei cavi coassiali con isolante debolmente conduttore.

### 21.1.3 Legge di Ohm infinitesima

Le due leggi di Ohm sono relazioni *globali*, riferite all'intero conduttore. In elettromagnetismo è però spesso più utile una formulazione *locale*, che leghi le grandezze punto per punto. Consideriamo un piccolo cilindretto di materiale di lunghezza $\mathrm{d}\ell$ e sezione $\mathrm{d}S$, orientato lungo la direzione del campo elettrico. La differenza di potenziale ai suoi capi è $\mathrm{d}V = E\,\mathrm{d}\ell$, la corrente che lo attraversa è $\mathrm{d}i = J\,\mathrm{d}S$ e la sua resistenza è, per la seconda legge, $\mathrm{d}R = \rho\,\mathrm{d}\ell/\mathrm{d}S$. Applicando la prima legge al cilindretto si ottiene

$$
E\,\mathrm{d}\ell = \rho\,\frac{\mathrm{d}\ell}{\mathrm{d}S}\,J\,\mathrm{d}S \quad\Longrightarrow\quad E = \rho\,J .
$$

Poiché in un materiale isotropo la densità di corrente e il campo elettrico hanno la stessa direzione e lo stesso verso, la relazione si scrive in forma vettoriale come

$$
\vec{J} = \sigma\,\vec{E}, \qquad \vec{E} = \rho\,\vec{J}.
$$

Questa è la **legge di Ohm in forma locale** (o infinitesima). Essa è più generale delle precedenti perché non fa riferimento alla forma del conduttore e vale in ogni punto di un materiale ohmico, anche quando le linee di corrente non sono parallele. Nei materiali anisotropi, come alcuni cristalli o materiali compositi stratificati, la conducibilità diventa un tensore e $\vec{J}$ può non essere parallelo a $\vec{E}$; in questo corso ci limitiamo al caso isotropo.

È istruttivo verificare che, integrando la legge locale, si riottengono le leggi globali. Per un filo rettilineo omogeneo di sezione $S$, la densità di corrente è uniforme, $J = i/S$, e il campo è uniforme, $E = \Delta V/\ell$. Sostituendo in $E = \rho J$ si ottiene $\Delta V/\ell = \rho\, i/S$, ovvero $\Delta V = (\rho\ell/S)\,i$, che riassume entrambe le leggi di Ohm.

La forma locale chiarisce anche un aspetto concettuale importante: in un conduttore percorso da corrente stazionaria il campo elettrico *non* è nullo, a differenza del caso elettrostatico. Per un filo di rame di sezione $1\ \mathrm{mm^2}$ percorso da $1\ \mathrm{A}$ il campo vale circa $1{,}7\times10^{-2}\ \mathrm{V/m}$: piccolo, ma sufficiente a sostenere la corrente. Inoltre, combinando la legge locale con l'equazione di continuità in regime stazionario, $\nabla\cdot\vec{J} = 0$, si deduce che in un conduttore omogeneo $\nabla\cdot\vec{E} = 0$, quindi la densità di carica volumetrica è nulla all'interno: le eventuali cariche che modellano il campo si dispongono sulla superficie del conduttore e sulle interfacce fra materiali diversi.

### Esercizio d'esempio

Un filo di rame ($\rho = 1{,}7\times10^{-8}\ \Omega\,\mathrm{m}$) lungo $\ell = 25\ \mathrm{m}$ e di diametro $d = 1{,}0\ \mathrm{mm}$ è collegato a una differenza di potenziale $\Delta V = 0{,}50\ \mathrm{V}$. Calcolare la resistenza, la corrente, la densità di corrente e il campo elettrico nel filo.

**Soluzione.** La sezione è
$$
S = \frac{\pi d^2}{4} = \frac{\pi (1{,}0\times10^{-3}\ \mathrm{m})^2}{4} = 7{,}85\times10^{-7}\ \mathrm{m^2}.
$$
Per la seconda legge di Ohm:
$$
R = \rho\frac{\ell}{S} = 1{,}7\times10^{-8}\ \Omega\,\mathrm{m}\cdot\frac{25\ \mathrm{m}}{7{,}85\times10^{-7}\ \mathrm{m^2}} = 0{,}54\ \Omega .
$$
Per la prima legge:
$$
i = \frac{\Delta V}{R} = \frac{0{,}50\ \mathrm{V}}{0{,}54\ \Omega} = 0{,}92\ \mathrm{A}.
$$
La densità di corrente è $J = i/S = 0{,}92/7{,}85\times10^{-7} = 1{,}2\times10^{6}\ \mathrm{A/m^2}$ e il campo vale $E = \Delta V/\ell = 0{,}50/25 = 2{,}0\times10^{-2}\ \mathrm{V/m}$. Come verifica, $\rho J = 1{,}7\times10^{-8}\cdot1{,}2\times10^{6} \approx 2{,}0\times10^{-2}\ \mathrm{V/m}$, in accordo con la legge di Ohm locale.

### Punti chiave

- La **prima legge di Ohm** $\Delta V = R i$ afferma che, nei conduttori ohmici, la resistenza è indipendente dalla tensione applicata.
- La resistenza si misura in ohm ($1\ \Omega = 1\ \mathrm{V/A}$); la conduttanza $G = 1/R$ in siemens.
- La **seconda legge di Ohm** $R = \rho\,\ell/S$ separa il contributo del materiale (resistività $\rho$) da quello della geometria.
- La resistività varia di oltre venti ordini di grandezza fra metalli, semiconduttori e isolanti; nei metalli cresce linearmente con la temperatura.
- La **legge di Ohm locale** $\vec{J} = \sigma\vec{E}$ vale punto per punto in un materiale ohmico isotropo ed è la forma più generale.
- In un conduttore percorso da corrente stazionaria il campo elettrico interno è diverso da zero, ma la densità di carica volumetrica è nulla se il materiale è omogeneo.
- Molti dispositivi (diodi, lampade) non sono ohmici: per essi si usa la resistenza differenziale dipendente dal punto di lavoro.

## 21.2 Modello di Drude

Le leggi di Ohm sono leggi empiriche: descrivono con precisione il comportamento dei conduttori ma non spiegano *perché* la corrente sia proporzionale al campo, né da che cosa dipenda la resistività. Nel 1900, pochi anni dopo la scoperta dell'elettrone da parte di J. J. Thomson, Paul Drude propose un modello microscopico della conduzione nei metalli basato sulla teoria cinetica dei gas. Pur essendo un modello classico, che ignora la natura quantistica degli elettroni, esso riproduce correttamente la legge di Ohm e fornisce stime ragionevoli degli ordini di grandezza in gioco. Per questo è tuttora il primo passo per capire la conduzione elettrica.

### 21.2.1 Modello di Drude

Il modello di Drude parte dall'idea che in un metallo gli elettroni più esterni degli atomi (gli elettroni di valenza) non siano legati ai singoli atomi, ma siano liberi di muoversi in tutto il volume del cristallo. Gli ioni positivi, che restano nelle posizioni del reticolo cristallino, formano una struttura praticamente fissa, mentre gli elettroni liberi costituiscono un **gas di elettroni** che riempie gli spazi fra gli ioni. Le ipotesi fondamentali del modello sono le seguenti.

1. **Elettroni liberi e indipendenti**: fra un urto e l'altro ogni elettrone si muove come una particella libera, soggetta soltanto agli eventuali campi esterni applicati; si trascurano le interazioni elettrone-elettrone e quelle elettrone-ione al di fuori degli urti.
2. **Urti istantanei**: gli elettroni subiscono collisioni istantanee che ne modificano bruscamente la velocità. Nella versione originale si pensava a urti contro gli ioni del reticolo; oggi sappiamo che gli urti rilevanti avvengono con le vibrazioni del reticolo (fononi), con impurezze e con difetti.
3. **Tempo di rilassamento**: la probabilità che un elettrone subisca un urto nell'intervallo $\mathrm{d}t$ è $\mathrm{d}t/\tau$, dove $\tau$ è il **tempo medio fra due urti** (o **tempo di rilassamento**), indipendente dalla posizione e dalla velocità dell'elettrone.
4. **Perdita di memoria**: dopo ogni urto l'elettrone riemerge con una velocità di direzione casuale, il cui modulo è legato alla temperatura locale; in altre parole l'urto cancella ogni informazione sulla velocità precedente, compreso l'eventuale contributo accumulato per effetto del campo.

La densità degli elettroni liberi $n$ si stima facilmente: se ogni atomo cede $Z$ elettroni di valenza, si ha $n = Z\,\rho_m N_A / M$, con $\rho_m$ densità di massa, $N_A$ numero di Avogadro e $M$ massa molare. Per il rame, con $Z = 1$, $\rho_m = 8{,}96\times10^{3}\ \mathrm{kg/m^3}$ e $M = 63{,}5\times10^{-3}\ \mathrm{kg/mol}$, si trova $n \approx 8{,}5\times10^{28}\ \mathrm{m^{-3}}$: un numero enorme, circa mille volte la densità delle molecole di un gas in condizioni normali.

Il modello descrive dunque gli elettroni come le molecole di un gas, in continuo moto disordinato, sul quale si sovrappone un moto ordinato di trascinamento quando si applica un campo elettrico. Le due componenti del moto hanno velocità caratteristiche molto diverse, che analizziamo separatamente nelle prossime sottosezioni.

Vale la pena anticipare i limiti del modello. Drude trattava gli elettroni come particelle classiche con distribuzione di Maxwell-Boltzmann; ciò porta a previsioni sbagliate per il calore specifico elettronico (che risulta troppo grande) e per la dipendenza della resistività dalla temperatura. Questi problemi furono risolti da Sommerfeld, applicando agli elettroni la statistica quantistica di Fermi-Dirac, e successivamente dalla teoria a bande dei solidi, che spiega anche perché alcuni materiali siano isolanti e altri semiconduttori. Ciononostante, l'espressione della conducibilità ottenuta da Drude resta formalmente valida, a patto di reinterpretare $\tau$ e la velocità degli elettroni.

### 21.2.2 Velocità termica

In assenza di campo esterno, gli elettroni liberi si muovono in modo completamente caotico, come le molecole di un gas in equilibrio termico. Secondo la teoria cinetica classica, l'energia cinetica media associata al moto di traslazione è legata alla temperatura assoluta dal teorema di equipartizione:

$$
\frac{1}{2} m_e \langle v^2 \rangle = \frac{3}{2} k_B T ,
$$

da cui si ricava la **velocità termica** (velocità quadratica media)

$$
v_t = \sqrt{\langle v^2\rangle} = \sqrt{\frac{3 k_B T}{m_e}} .
$$

A temperatura ambiente, $T = 300\ \mathrm{K}$, con $k_B = 1{,}38\times10^{-23}\ \mathrm{J/K}$ e $m_e = 9{,}11\times10^{-31}\ \mathrm{kg}$, si ottiene $v_t \approx 1{,}2\times10^{5}\ \mathrm{m/s}$. Si tratta di una velocità molto elevata, ma il moto termico è *isotropo*: in ogni istante vi sono tanti elettroni che si muovono in un verso quanti nel verso opposto, e la velocità media vettoriale è nulla:

$$
\langle \vec{v} \rangle = \vec{0} .
$$

Di conseguenza, il moto termico non produce alcuna corrente netta: attraverso qualunque superficie interna al conduttore, il numero di elettroni che passano in un verso è in media uguale a quello che passano nel verso opposto.

Dalla velocità termica e dal tempo medio fra gli urti si definisce il **libero cammino medio** $\lambda = v_t\,\tau$, cioè la distanza media percorsa da un elettrone fra due urti successivi. Nel modello di Drude originale si pensava che $\lambda$ fosse dell'ordine della distanza interatomica, qualche decimo di nanometro, coerentemente con l'idea di urti contro gli ioni. In realtà, come mostra la teoria quantistica, gli elettroni si muovono con velocità molto maggiori, dell'ordine della **velocità di Fermi** $v_F \approx 1{,}6\times10^{6}\ \mathrm{m/s}$ nel rame, indipendentemente dalla temperatura, e il libero cammino medio a temperatura ambiente è di alcune decine di nanometri: un elettrone attraversa indisturbato centinaia di celle reticolari, perché un reticolo cristallino perfettamente periodico non diffonde le onde elettroniche. Sono le imperfezioni del reticolo, comprese le vibrazioni termiche, a causare gli urti.

Questo punto ha una conseguenza importante. Nel modello classico la resistività dovrebbe crescere come $\sqrt{T}$, perché aumenta $v_t$ e quindi diminuisce $\tau$ a parità di $\lambda$; sperimentalmente invece nei metalli puri la resistività cresce approssimativamente in modo lineare con $T$. La spiegazione corretta è che la velocità degli elettroni rilevanti è quella di Fermi, praticamente indipendente da $T$, mentre il numero di fononi, e dunque la frequenza degli urti, cresce proporzionalmente alla temperatura. A bassissime temperature le vibrazioni si smorzano e la resistività tende a un valore costante, la **resistività residua**, determinata dalle impurezze e dai difetti del campione.

### 21.2.3 Velocità di deriva

Applichiamo ora al conduttore un campo elettrico uniforme $\vec{E}$. Su ciascun elettrone, di carica $-e$, agisce la forza $\vec{F} = -e\vec{E}$, che fra un urto e l'altro gli imprime un'accelerazione costante

$$
\vec{a} = -\frac{e\vec{E}}{m_e} .
$$

Se un elettrone emerge da un urto con velocità $\vec{v}_0$ (casuale) e viaggia per un tempo $t$ prima dell'urto successivo, la sua velocità sarà $\vec{v} = \vec{v}_0 - e\vec{E}t/m_e$. Facendo la media su tutti gli elettroni, il termine $\vec{v}_0$ si annulla per la perdita di memoria, mentre il tempo trascorso dall'ultimo urto vale in media $\tau$. Si ottiene così una velocità media non nulla, detta **velocità di deriva**:

$$
\vec{v}_d = -\frac{e\tau}{m_e}\,\vec{E} .
$$

Il coefficiente di proporzionalità fra velocità di deriva e campo, in modulo, si chiama **mobilità** dei portatori:

$$
\mu = \frac{e\tau}{m_e}, \qquad v_d = \mu E ,
$$

e si misura in $\mathrm{m^2/(V\,s)}$. La velocità di deriva è diretta in verso opposto al campo, perché gli elettroni hanno carica negativa.

Un modo equivalente di ottenere lo stesso risultato consiste nello scrivere un'equazione del moto per la velocità media in cui gli urti sono rappresentati da una forza di tipo viscoso:

$$
m_e\frac{\mathrm{d}\vec{v}_d}{\mathrm{d}t} = -e\vec{E} - \frac{m_e}{\tau}\vec{v}_d .
$$

In regime stazionario la derivata si annulla e si ritrova $\vec{v}_d = -e\tau\vec{E}/m_e$. Questa formulazione mostra che, dopo l'accensione del campo, la velocità di deriva raggiunge il valore di regime in un tempo dell'ordine di $\tau$, che nei metalli è di circa $10^{-14}\ \mathrm{s}$: per tutti gli scopi pratici, la risposta del conduttore è istantanea.

Ricordando che la densità di corrente è $\vec{J} = n q \vec{v}_d$, con $q = -e$, si ottiene

$$
\vec{J} = (-e)\,n\left(-\frac{e\tau}{m_e}\vec{E}\right) = \frac{n e^2 \tau}{m_e}\,\vec{E} .
$$

Abbiamo ritrovato la legge di Ohm locale $\vec{J} = \sigma\vec{E}$, con la conducibilità espressa in termini di grandezze microscopiche:

$$
\sigma = \frac{n e^2 \tau}{m_e} = n e \mu, \qquad \rho = \frac{m_e}{n e^2 \tau} .
$$

Questo è il risultato centrale del modello: la proporzionalità fra corrente e campo nasce dall'equilibrio fra l'accelerazione dovuta al campo e la perdita di velocità ordinata negli urti. Senza urti gli elettroni accelererebbero indefinitamente e la corrente crescerebbe nel tempo; sono proprio le collisioni a produrre una velocità media costante e quindi una resistenza finita.

Dalla resistività misurata si può ricavare il tempo di rilassamento. Per il rame, $\tau = m_e/(n e^2 \rho) \approx 2{,}5\times10^{-14}\ \mathrm{s}$. Con densità di corrente tipiche dei cavi domestici, la velocità di deriva risulta sorprendentemente piccola, dell'ordine di frazioni di millimetro al secondo, come mostra l'esercizio seguente. Ciò non contraddice il fatto che una lampada si accenda istantaneamente quando si chiude l'interruttore: ciò che si propaga rapidamente lungo il filo, a una velocità prossima a quella della luce, è il *segnale* elettromagnetico che mette in moto contemporaneamente tutti gli elettroni del circuito, non i singoli elettroni.

### Esercizio d'esempio

Un filo di rame di sezione $S = 2{,}5\ \mathrm{mm^2}$ è percorso da una corrente $i = 10\ \mathrm{A}$. Sapendo che $n = 8{,}5\times10^{28}\ \mathrm{m^{-3}}$ e $\rho = 1{,}7\times10^{-8}\ \Omega\,\mathrm{m}$, calcolare la velocità di deriva, il tempo di rilassamento e la mobilità, e confrontare $v_d$ con la velocità termica a $300\ \mathrm{K}$.

**Soluzione.** La densità di corrente vale
$$
J = \frac{i}{S} = \frac{10\ \mathrm{A}}{2{,}5\times10^{-6}\ \mathrm{m^2}} = 4{,}0\times10^{6}\ \mathrm{A/m^2}.
$$
La velocità di deriva è
$$
v_d = \frac{J}{n e} = \frac{4{,}0\times10^{6}}{8{,}5\times10^{28}\cdot1{,}6\times10^{-19}}\ \mathrm{m/s} = 2{,}9\times10^{-4}\ \mathrm{m/s},
$$
circa $0{,}3\ \mathrm{mm/s}$. Il tempo di rilassamento:
$$
\tau = \frac{m_e}{n e^2 \rho} = \frac{9{,}11\times10^{-31}}{8{,}5\times10^{28}\cdot(1{,}6\times10^{-19})^2\cdot1{,}7\times10^{-8}}\ \mathrm{s} = 2{,}5\times10^{-14}\ \mathrm{s}.
$$
La mobilità: $\mu = e\tau/m_e = 1{,}6\times10^{-19}\cdot2{,}5\times10^{-14}/9{,}11\times10^{-31} = 4{,}4\times10^{-3}\ \mathrm{m^2/(V\,s)}$. La velocità termica è $v_t = \sqrt{3k_BT/m_e} = 1{,}2\times10^{5}\ \mathrm{m/s}$, quindi $v_d/v_t \approx 2\times10^{-9}$: il moto ordinato è una piccolissima perturbazione sovrapposta all'agitazione termica.

### Punti chiave

- Il **modello di Drude** tratta gli elettroni di conduzione come un gas classico di particelle libere che subiscono urti istantanei con tempo medio $\tau$.
- La **velocità termica** $v_t = \sqrt{3k_BT/m_e}$ è elevata ($\sim10^5\ \mathrm{m/s}$) ma isotropa: non genera corrente netta.
- In presenza di campo gli elettroni acquistano una **velocità di deriva** $\vec{v}_d = -e\tau\vec{E}/m_e$, piccolissima ($\sim10^{-4}\ \mathrm{m/s}$).
- La **mobilità** $\mu = e\tau/m_e$ lega velocità di deriva e campo.
- Il modello riproduce la legge di Ohm con $\sigma = n e^2\tau/m_e$: la resistenza nasce dagli urti.
- La propagazione quasi istantanea del segnale elettrico non va confusa con il lento moto di deriva degli elettroni.
- Il modello classico sbaglia la dipendenza dalla temperatura e il calore specifico elettronico; la correzione richiede la statistica di Fermi-Dirac.

## 21.3 Legge di Joule

Chiunque abbia toccato un caricabatterie dopo qualche ora di utilizzo, o abbia osservato il filamento incandescente di una vecchia lampadina, sa che un conduttore percorso da corrente si riscalda. Questo fenomeno, studiato sistematicamente da James Prescott Joule intorno al 1840, è detto **effetto Joule** ed è la manifestazione macroscopica della dissipazione di energia che accompagna il passaggio di corrente in un materiale resistivo. In questa sezione ricaviamo l'espressione della potenza dissipata, ne diamo la forma locale e l'interpretazione microscopica, e discutiamo le sue numerose conseguenze tecnologiche, sia desiderate (stufe, fusibili, saldatori) sia indesiderate (perdite nelle linee di trasmissione, surriscaldamento dei circuiti elettronici).

### 21.3.1 Lavoro e potenza della forza elettrica

Consideriamo un tratto di conduttore fra i punti A e B, a potenziali $V_A > V_B$, attraversato da una corrente stazionaria $i$ nel verso da A a B. In un intervallo di tempo $\mathrm{d}t$ attraversa il conduttore una carica $\mathrm{d}q = i\,\mathrm{d}t$. Dal punto di vista energetico è come se questa carica entrasse in A e uscisse in B: il campo elettrico compie su di essa un lavoro pari alla diminuzione della sua energia potenziale elettrica,

$$
\mathrm{d}W = \mathrm{d}q\,(V_A - V_B) = i\,\Delta V\,\mathrm{d}t .
$$

La **potenza** trasferita dal campo ai portatori di carica è quindi

$$
P = \frac{\mathrm{d}W}{\mathrm{d}t} = \Delta V\, i .
$$

Questa relazione è del tutto generale: vale per qualunque componente (resistore, motore, batteria in carica, diodo) attraversato da una corrente $i$ e ai cui capi c'è una tensione $\Delta V$. Essa esprime la potenza *assorbita* dal componente secondo la convenzione degli utilizzatori; se il prodotto risulta negativo, il componente sta in realtà *erogando* potenza al resto del circuito, come accade per un generatore.

Ci si potrebbe chiedere dove vada a finire l'energia ceduta dal campo. Nel caso di un motore elettrico, essa si trasforma in gran parte in lavoro meccanico; in una batteria che si ricarica, in energia chimica. In un resistore, invece, gli elettroni non accumulano energia cinetica, perché la loro velocità di deriva è costante; l'intera energia viene trasferita al reticolo cristallino sotto forma di agitazione termica, cioè di energia interna. Il resistore si scalda finché la potenza ceduta all'ambiente per conduzione, convezione e irraggiamento non eguaglia la potenza elettrica assorbita, raggiungendo una temperatura di regime.

### 21.3.2 Potenza dissipata in un resistore

Per un resistore ohmico possiamo combinare $P = \Delta V\,i$ con la prima legge di Ohm $\Delta V = R i$, ottenendo tre forme equivalenti della **legge di Joule**:

$$
P = R\,i^2 = \frac{(\Delta V)^2}{R} = \Delta V\,i .
$$

La potenza si misura in watt ($1\ \mathrm{W} = 1\ \mathrm{V\cdot A} = 1\ \mathrm{J/s}$). L'energia dissipata in un intervallo di tempo $t$, a corrente costante, è $Q = R i^2 t$; nel caso di corrente variabile occorre integrare, $Q = \int R\, i^2(t)\,\mathrm{d}t$. In ambito tecnico ed economico l'energia elettrica si misura spesso in **chilowattora**: $1\ \mathrm{kWh} = 3{,}6\times10^{6}\ \mathrm{J}$.

La scelta fra le diverse espressioni non è indifferente quando si confrontano più resistori. Se due resistori sono percorsi dalla *stessa corrente* (come in un collegamento in serie), conviene usare $P = R i^2$: dissipa di più quello con resistenza maggiore. Se invece sono sottoposti alla *stessa tensione* (collegamento in parallelo), conviene $P = (\Delta V)^2/R$: dissipa di più quello con resistenza minore. Questa apparente contraddizione si risolve ricordando quale grandezza è fissata. Ad esempio, in un impianto domestico tutti gli elettrodomestici sono collegati in parallelo alla tensione di rete di $230\ \mathrm{V}$ e quelli di maggiore potenza, come un forno o uno scaldabagno da $2\ \mathrm{kW}$, hanno la resistenza più bassa, circa $26\ \Omega$.

Ogni resistore commerciale è caratterizzato, oltre che dal valore nominale di resistenza e dalla tolleranza, da una **potenza massima** che può dissipare senza danneggiarsi (tipicamente $1/4\ \mathrm{W}$ o $1/2\ \mathrm{W}$ per i piccoli resistori a strato, fino a decine o centinaia di watt per resistori di potenza dotati di dissipatore). Superare questo limite porta a temperature eccessive, variazioni permanenti della resistenza o alla rottura del componente.

### 21.3.3 Forma locale e interpretazione microscopica

Come per la legge di Ohm, anche la legge di Joule ammette una forma locale. Consideriamo di nuovo un cilindretto di volume $\mathrm{d}\tau = \mathrm{d}S\,\mathrm{d}\ell$ con asse parallelo a $\vec{J}$. La potenza che vi si dissipa è $\mathrm{d}P = \mathrm{d}V\,\mathrm{d}i = (E\,\mathrm{d}\ell)(J\,\mathrm{d}S) = \vec{J}\cdot\vec{E}\,\mathrm{d}\tau$. Si definisce allora la **densità di potenza** dissipata

$$
p = \frac{\mathrm{d}P}{\mathrm{d}\tau} = \vec{J}\cdot\vec{E} = \sigma E^2 = \rho J^2 ,
$$

misurata in $\mathrm{W/m^3}$. Integrando su tutto il volume del conduttore si ritrova la potenza totale. Questa forma è utile quando la corrente non è distribuita uniformemente, per esempio in un conduttore di sezione variabile: la dissipazione è massima dove la densità di corrente è più alta, cioè nelle strozzature. È esattamente questo il principio del **fusibile**: un tratto di conduttore sottile, o di materiale a basso punto di fusione, in cui la densità di potenza è elevata e che fonde interrompendo il circuito quando la corrente supera il valore di sicurezza.

Il modello di Drude fornisce un'interpretazione chiara della dissipazione. Fra un urto e l'altro ogni elettrone viene accelerato dal campo e acquista, in media, un'energia cinetica aggiuntiva legata al moto di deriva; nell'urto successivo questa energia viene ceduta al reticolo, che si scalda. La potenza trasferita a ciascun elettrone è $\vec{F}\cdot\vec{v}_d = (-e\vec{E})\cdot\vec{v}_d$; moltiplicando per la densità $n$ degli elettroni si ottiene

$$
p = n(-e)\vec{v}_d\cdot\vec{E} = \vec{J}\cdot\vec{E} ,
$$

in accordo con l'espressione macroscopica. Il campo fornisce lavoro con continuità, gli urti lo convertono in calore: il resistore funziona come un convertitore irreversibile di energia elettrica in energia interna. Da un punto di vista termodinamico, l'effetto Joule è un processo irreversibile che produce entropia.

### 21.3.4 Applicazioni e trasmissione dell'energia

L'effetto Joule è sfruttato intenzionalmente in moltissimi dispositivi: stufe e forni elettrici, bollitori, ferri da stiro, asciugacapelli, saldatori, lunotti termici delle automobili e, storicamente, lampade a incandescenza, in cui un filamento di tungsteno raggiunge circa $2700\ \mathrm{K}$ e irradia luce visibile, ma con un'efficienza luminosa di pochi percento. Gli elementi riscaldanti sono realizzati con leghe come il nichel-cromo, che hanno resistività elevata, resistono all'ossidazione ad alta temperatura e presentano un coefficiente termico ridotto.

In altri contesti l'effetto Joule è invece una perdita da minimizzare. L'esempio più importante è il **trasporto dell'energia elettrica** su lunghe distanze. Supponiamo di dover trasmettere una potenza $P_u$ a un utilizzatore attraverso una linea di resistenza complessiva $R_L$. La corrente necessaria è $i = P_u/V$, dove $V$ è la tensione di trasmissione, e la potenza persa nella linea è

$$
P_{\text{persa}} = R_L\,i^2 = R_L\,\frac{P_u^2}{V^2} .
$$

A parità di potenza trasmessa, le perdite diminuiscono con il quadrato della tensione. Per questo le linee di trasmissione operano a tensioni molto elevate (in Italia fino a $380\ \mathrm{kV}$), che vengono poi abbassate con trasformatori prima di raggiungere le utenze. Lo stesso ragionamento spiega perché le sezioni dei cavi debbano essere dimensionate in base alla corrente: un cavo troppo sottile ha resistenza elevata, si scalda e può danneggiare l'isolamento, con rischio di incendio. Le normative impiantistiche prescrivono infatti sezioni minime ($1{,}5\ \mathrm{mm^2}$ per le prese luce, $2{,}5\ \mathrm{mm^2}$ per le prese di forza nelle abitazioni) proprio per limitare il riscaldamento.

Infine, nell'elettronica moderna la dissipazione per effetto Joule nei transistor è uno dei principali limiti alla miniaturizzazione e all'aumento della frequenza di funzionamento dei processori, che richiedono sistemi di raffreddamento dedicati.

### Esercizio d'esempio

Una centrale deve fornire una potenza $P_u = 50\ \mathrm{MW}$ a una città distante $100\ \mathrm{km}$, tramite una linea a due conduttori di alluminio ($\rho = 2{,}8\times10^{-8}\ \Omega\,\mathrm{m}$) di sezione $S = 400\ \mathrm{mm^2}$ ciascuno. Calcolare la frazione di potenza persa se la trasmissione avviene a $V_1 = 20\ \mathrm{kV}$ e a $V_2 = 380\ \mathrm{kV}$ (trattare il problema come in corrente continua).

**Soluzione.** La lunghezza complessiva dei conduttori (andata e ritorno) è $\ell = 2\times100\ \mathrm{km} = 2{,}0\times10^{5}\ \mathrm{m}$. La resistenza di linea è
$$
R_L = \rho\frac{\ell}{S} = 2{,}8\times10^{-8}\cdot\frac{2{,}0\times10^{5}}{4{,}0\times10^{-4}}\ \Omega = 14\ \Omega .
$$
A $20\ \mathrm{kV}$ la corrente è $i_1 = P_u/V_1 = 5{,}0\times10^{7}/2{,}0\times10^{4} = 2{,}5\times10^{3}\ \mathrm{A}$ e la potenza persa è $R_L i_1^2 = 14\cdot(2{,}5\times10^{3})^2 = 8{,}75\times10^{7}\ \mathrm{W}$: maggiore della potenza utile; del resto la caduta di tensione sulla linea, $R_L i_1 = 35\ \mathrm{kV}$, supererebbe la stessa tensione di trasmissione, il che rende questa soluzione del tutto impraticabile. A $380\ \mathrm{kV}$ la corrente è $i_2 = 5{,}0\times10^{7}/3{,}8\times10^{5} = 132\ \mathrm{A}$ e la potenza persa è $14\cdot132^2 = 2{,}4\times10^{5}\ \mathrm{W}$, pari a circa lo $0{,}5\,\%$ della potenza trasmessa. Il rapporto fra le perdite nei due casi è $(V_2/V_1)^2 = 361$.

### Punti chiave

- La potenza assorbita da un qualunque componente è $P = \Delta V\,i$ (convenzione degli utilizzatori).
- Per un resistore la **legge di Joule** dà $P = R i^2 = (\Delta V)^2/R$; l'energia elettrica viene convertita integralmente in energia interna.
- A parità di corrente dissipa di più la resistenza maggiore; a parità di tensione la resistenza minore.
- In forma locale la densità di potenza è $p = \vec{J}\cdot\vec{E} = \rho J^2$; è massima dove la corrente si concentra (principio del fusibile).
- Microscopicamente, il campo accelera gli elettroni e gli urti trasferiscono l'energia al reticolo: l'effetto Joule è un processo irreversibile.
- Le perdite di trasmissione scalano come $1/V^2$: per questo l'energia si trasporta ad alta tensione.
- Ogni resistore reale ha una potenza massima ammissibile, oltre la quale si danneggia.

## 21.4 Serie e parallelo

I circuiti reali contengono quasi sempre più resistori collegati fra loro. Prima di affrontare i metodi generali di analisi dei circuiti, basati sulle leggi di Kirchhoff del prossimo capitolo, è utile imparare a riconoscere due configurazioni elementari, il collegamento in **serie** e quello in **parallelo**, e a sostituire un gruppo di resistori con un unico **resistore equivalente**. Due reti si dicono equivalenti rispetto a una coppia di morsetti se, applicando la stessa tensione ai morsetti, assorbono la stessa corrente; dall'esterno, cioè, non è possibile distinguerle con misure di tensione e corrente su quei morsetti. La riduzione serie-parallelo permette di risolvere rapidamente molti circuiti con un solo generatore e costituisce uno strumento indispensabile per l'analisi di partitori, strumenti di misura e reti di carico.

### 21.4.1 Resistori in serie

Due o più resistori si dicono collegati **in serie** quando sono disposti uno dopo l'altro lungo un unico ramo, senza diramazioni intermedie, in modo che siano necessariamente attraversati dalla **stessa corrente**. Questa proprietà discende dalla conservazione della carica: in regime stazionario non può esservi accumulo di carica nei nodi intermedi, perciò la corrente che entra in un resistore deve uscire tale e quale ed entrare nel successivo.

Siano $R_1, R_2, \ldots, R_N$ i resistori in serie, percorsi dalla corrente $i$. La caduta di tensione ai capi di ciascuno è $\Delta V_k = R_k i$ e, poiché il potenziale è una funzione di punto, la tensione complessiva fra gli estremi della serie è la somma delle singole cadute:

$$
\Delta V = \sum_{k=1}^{N} \Delta V_k = \left(\sum_{k=1}^{N} R_k\right) i .
$$

Confrontando con $\Delta V = R_{eq}\,i$ si ottiene la **resistenza equivalente della serie**:

$$
R_{eq} = R_1 + R_2 + \cdots + R_N = \sum_{k=1}^{N} R_k .
$$

La resistenza equivalente di una serie è sempre *maggiore* della più grande delle resistenze componenti. Il risultato è coerente con la seconda legge di Ohm: mettere in serie conduttori dello stesso materiale e della stessa sezione equivale ad allungare il conduttore, e la resistenza cresce proporzionalmente alla lunghezza totale.

Una conseguenza importante è il **partitore di tensione**. La tensione ai capi del $k$-esimo resistore è una frazione della tensione totale proporzionale alla sua resistenza:

$$
\Delta V_k = \frac{R_k}{R_{eq}}\,\Delta V .
$$

Con due resistori, $\Delta V_2 = \Delta V\, R_2/(R_1+R_2)$. Il partitore è uno dei circuiti più usati in elettronica: permette di ottenere una tensione ridotta e regolabile a partire da una sorgente fissa, come avviene nei potenziometri usati per il controllo del volume o nei sensori resistivi (termistori, fotoresistenze) letti tramite un convertitore analogico-digitale. Occorre però ricordare che la formula del partitore vale solo se il carico collegato all'uscita assorbe una corrente trascurabile, cioè se la sua resistenza è molto maggiore di $R_2$; altrimenti il carico si trova in parallelo con $R_2$ e modifica il rapporto di partizione.

Anche la potenza si ripartisce in proporzione alle resistenze: essendo $i$ comune, $P_k = R_k i^2$ e la potenza totale è $P = R_{eq} i^2 = \sum P_k$. Un'applicazione tipica, e un difetto noto, del collegamento in serie è quella delle vecchie luci natalizie: se una lampadina si brucia, il circuito si apre e si spengono tutte.

### 21.4.2 Resistori in parallelo

Due o più resistori si dicono collegati **in parallelo** quando ciascuno ha un estremo collegato a uno stesso nodo A e l'altro estremo a uno stesso nodo B. In questo caso tutti i resistori sono sottoposti alla **stessa differenza di potenziale** $\Delta V = V_A - V_B$, mentre la corrente totale che entra in A si suddivide fra i vari rami.

La corrente nel $k$-esimo ramo è $i_k = \Delta V/R_k$. Per la conservazione della carica la corrente totale è la somma delle correnti nei rami:

$$
i = \sum_{k=1}^{N} i_k = \left(\sum_{k=1}^{N}\frac{1}{R_k}\right)\Delta V .
$$

Confrontando con $i = \Delta V/R_{eq}$ si ottiene la **resistenza equivalente del parallelo**:

$$
\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \cdots + \frac{1}{R_N} = \sum_{k=1}^{N}\frac{1}{R_k} .
$$

In termini di conduttanze la regola è più semplice: le conduttanze in parallelo si sommano, $G_{eq} = \sum G_k$. La resistenza equivalente di un parallelo è sempre *minore* della più piccola delle resistenze componenti: aggiungere un ramo in parallelo offre alla corrente un percorso in più e quindi riduce la resistenza complessiva. Anche questo è coerente con la seconda legge di Ohm, poiché affiancare conduttori equivale ad aumentare la sezione.

Per due soli resistori conviene ricordare la forma compatta

$$
R_{eq} = \frac{R_1 R_2}{R_1 + R_2},
$$

detta talvolta "prodotto su somma". Due casi particolari sono istruttivi: $N$ resistori uguali di valore $R$ in parallelo hanno $R_{eq} = R/N$; se uno dei due resistori è molto più piccolo dell'altro, $R_1 \ll R_2$, si ha $R_{eq} \approx R_1$, cioè la corrente passa quasi tutta nel ramo a resistenza minore. Il caso limite $R_1 = 0$ è il **cortocircuito**: un filo ideale in parallelo a un resistore lo esclude completamente.

Il duale del partitore di tensione è il **partitore di corrente**. Con due resistori in parallelo percorsi dalla corrente totale $i$, la corrente in ciascun ramo è

$$
i_1 = \frac{R_2}{R_1 + R_2}\,i, \qquad i_2 = \frac{R_1}{R_1 + R_2}\,i ,
$$

cioè la corrente si ripartisce in proporzione *inversa* alle resistenze. Questo principio è alla base dello **shunt** usato per estendere la portata di un amperometro: una piccola resistenza posta in parallelo allo strumento devia la maggior parte della corrente, lasciandone passare nello strumento solo una frazione nota.

Il collegamento in parallelo è quello degli impianti elettrici domestici: tutti gli apparecchi sono sottoposti alla stessa tensione di rete e funzionano indipendentemente, sicché lo spegnimento di uno non influenza gli altri. Al tempo stesso, ogni utilizzatore aggiunto aumenta la corrente totale prelevata dalla linea, ed è per questo che il contatore interrompe la fornitura quando si accendono troppi apparecchi di potenza elevata.

Le nozioni di serie e parallelo chiariscono anche come vadano inseriti gli strumenti di misura. Un **amperometro**, che deve essere attraversato dalla corrente da misurare, si collega in serie al ramo di interesse; per non alterare la corrente stessa deve avere una resistenza interna molto piccola rispetto a quella del ramo, poiché la sua resistenza si somma a quella del circuito. Un **voltmetro**, che deve misurare la differenza di potenziale fra due punti, si collega in parallelo al componente; per non sottrarre corrente al circuito deve avere una resistenza interna molto grande, poiché il parallelo con una resistenza piccola abbasserebbe la resistenza equivalente e modificherebbe la tensione da misurare. Un errore tipico in laboratorio consiste nel collegare per sbaglio un amperometro in parallelo a un generatore: la sua bassissima resistenza realizza di fatto un cortocircuito, con correnti elevate che possono danneggiare lo strumento o far intervenire il suo fusibile di protezione.

Infine, non tutte le reti si possono ridurre con sole operazioni serie-parallelo. Un esempio classico è il **ponte di Wheatstone** sbilanciato, in cui il resistore centrale collega due nodi che non sono in serie né in parallelo con gli altri rami. Per queste reti occorrono metodi generali, come le leggi di Kirchhoff, oppure trasformazioni particolari (triangolo-stella). Quando il ponte è bilanciato, cioè $R_1/R_2 = R_3/R_4$, i due nodi centrali sono allo stesso potenziale, nel resistore centrale non passa corrente e la rete torna riducibile: è il principio con cui si misurano resistenze incognite con grande precisione.

### Esercizio d'esempio

Un generatore ideale di tensione $\Delta V = 12\ \mathrm{V}$ alimenta la rete seguente: un resistore $R_1 = 4{,}0\ \Omega$ in serie con il parallelo di $R_2 = 6{,}0\ \Omega$ e $R_3 = 12\ \Omega$. Calcolare la resistenza equivalente, la corrente erogata, la corrente in ciascun ramo e la potenza dissipata in ogni resistore.

**Soluzione.** Il parallelo di $R_2$ e $R_3$ vale
$$
R_{23} = \frac{R_2R_3}{R_2+R_3} = \frac{6{,}0\cdot12}{18}\ \Omega = 4{,}0\ \Omega .
$$
La resistenza equivalente totale è $R_{eq} = R_1 + R_{23} = 8{,}0\ \Omega$ e la corrente erogata è $i = \Delta V/R_{eq} = 12/8{,}0 = 1{,}5\ \mathrm{A}$. La tensione ai capi del parallelo è $\Delta V_{23} = R_{23}\,i = 6{,}0\ \mathrm{V}$ (partitore: metà della tensione, essendo $R_1 = R_{23}$). Le correnti nei rami sono $i_2 = 6{,}0/6{,}0 = 1{,}0\ \mathrm{A}$ e $i_3 = 6{,}0/12 = 0{,}50\ \mathrm{A}$, la cui somma restituisce $1{,}5\ \mathrm{A}$. Le potenze sono $P_1 = R_1 i^2 = 4{,}0\cdot2{,}25 = 9{,}0\ \mathrm{W}$, $P_2 = 6{,}0^2/6{,}0 = 6{,}0\ \mathrm{W}$, $P_3 = 6{,}0^2/12 = 3{,}0\ \mathrm{W}$. Il totale, $18\ \mathrm{W}$, coincide con la potenza erogata $\Delta V\,i = 12\cdot1{,}5 = 18\ \mathrm{W}$.

### Punti chiave

- Resistori in **serie** sono percorsi dalla stessa corrente; le tensioni si sommano e $R_{eq} = \sum R_k$.
- Resistori in **parallelo** sono sottoposti alla stessa tensione; le correnti si sommano e $1/R_{eq} = \sum 1/R_k$.
- La serie ha resistenza maggiore della massima componente; il parallelo minore della minima.
- Il **partitore di tensione** ripartisce la tensione in proporzione alle resistenze; il **partitore di corrente** in proporzione inversa.
- Un cortocircuito in parallelo a un resistore lo esclude; un circuito aperto in serie interrompe la corrente.
- Non tutte le reti sono riducibili con serie e parallelo (es. ponte di Wheatstone sbilanciato): servono le leggi di Kirchhoff.
- La conservazione dell'energia si verifica controllando che la somma delle potenze dissipate eguagli quella erogata dal generatore.

## 21.5 Superconduttori

Nella sezione 21.2 abbiamo visto che, nei metalli ordinari, la resistività diminuisce al calare della temperatura, perché si riducono le vibrazioni reticolari, ma tende a un valore residuo finito dovuto a impurezze e difetti. Nel 1911 Heike Kamerlingh Onnes, a Leida, poco dopo essere riuscito a liquefare l'elio, misurò la resistenza di un campione di mercurio raffreddato e osservò un fenomeno del tutto inatteso: al di sotto di circa $4{,}2\ \mathrm{K}$ la resistenza crollava bruscamente a un valore non misurabile, entro la sensibilità degli strumenti. Questo stato della materia, in cui la resistenza elettrica in corrente continua è esattamente nulla, prende il nome di **superconduttività**, e la temperatura alla quale avviene la transizione si chiama **temperatura critica** $T_c$.

Che la resistenza sia davvero nulla, e non solo molto piccola, è stato verificato con esperimenti di **corrente persistente**: si induce una corrente in un anello superconduttore e se ne misura il campo magnetico nel tempo. In esperimenti protratti per anni non si è osservata alcuna diminuzione apprezzabile; dalle sensibilità raggiunte si ricava un limite superiore alla resistività inferiore a $10^{-24}\ \Omega\,\mathrm{m}$, cioè almeno quindici ordini di grandezza sotto quella del rame a temperatura ambiente. In un circuito chiuso superconduttore la corrente può dunque circolare indefinitamente senza alcun generatore e senza dissipazione per effetto Joule.

La resistenza nulla, tuttavia, non basta a caratterizzare un superconduttore. Nel 1933 Walther Meissner e Robert Ochsenfeld scoprirono che un superconduttore, raffreddato sotto $T_c$ in presenza di un campo magnetico debole, **espelle** il campo dal proprio interno: le linee di campo vengono deviate attorno al campione e all'interno si ha $\vec{B} = \vec{0}$. Questo fenomeno, detto **effetto Meissner**, distingue il superconduttore da un ipotetico "conduttore perfetto", che avrebbe resistenza nulla ma si limiterebbe a *congelare* il flusso magnetico presente al momento della transizione, senza espellerlo. L'espulsione del campo è ottenuta tramite correnti superficiali, che circolano in uno strato sottile di spessore dell'ordine di $10$–$100\ \mathrm{nm}$ (la **lunghezza di penetrazione di London**) e generano un campo che annulla quello esterno all'interno del materiale. Il superconduttore si comporta quindi come un **diamagnete perfetto**. La spettacolare levitazione di un magnete sopra un campione superconduttore raffreddato in azoto liquido è una manifestazione diretta di questo effetto.

Lo stato superconduttore esiste solo entro certi limiti. Oltre alla temperatura critica, esiste un **campo magnetico critico** $B_c$ al di sopra del quale la superconduttività viene distrutta, e una **densità di corrente critica** $J_c$, legata al fatto che la corrente trasportata genera a sua volta un campo magnetico. Per molti materiali il campo critico dipende dalla temperatura secondo la legge empirica

$$
B_c(T) \simeq B_c(0)\left[1 - \left(\frac{T}{T_c}\right)^2\right],
$$

che si annulla a $T = T_c$ ed è massima a temperatura zero. Nel piano $(T, B)$ questa curva separa la regione superconduttrice, sotto la curva, da quella normale.

La spiegazione microscopica della superconduttività convenzionale fu data solo nel 1957 da Bardeen, Cooper e Schrieffer (**teoria BCS**). In essa gli elettroni, attraverso l'interazione con le vibrazioni del reticolo, formano coppie legate, le **coppie di Cooper**, che si comportano collettivamente come un unico stato quantistico coerente. Per diffondere una coppia occorre fornire un'energia finita, detta **gap** superconduttore; a bassa temperatura le vibrazioni non dispongono di questa energia, e il condensato scorre senza urti, cioè senza resistenza. Si tratta di un fenomeno intrinsecamente quantistico, che nessun modello classico come quello di Drude può descrivere.

### 21.5.1 Classificazione

I superconduttori si classificano secondo due criteri principali: il comportamento in presenza di campo magnetico (tipo I e tipo II) e il valore della temperatura critica (superconduttori a bassa e ad alta temperatura critica).

**Superconduttori di tipo I.** Sono per lo più metalli puri, come mercurio ($T_c = 4{,}15\ \mathrm{K}$), piombo ($7{,}2\ \mathrm{K}$), stagno ($3{,}7\ \mathrm{K}$) e alluminio ($1{,}2\ \mathrm{K}$). In essi l'effetto Meissner è completo fino al campo critico $B_c$: per $B < B_c$ il campo è totalmente espulso, per $B > B_c$ il materiale torna bruscamente allo stato normale e il campo penetra interamente. La transizione è netta e il campo critico è basso, tipicamente dell'ordine di $10^{-2}$–$10^{-1}\ \mathrm{T}$ (per il piombo $B_c(0) \approx 0{,}08\ \mathrm{T}$). Questi valori così ridotti rendono i superconduttori di tipo I inadatti alla realizzazione di magneti: già la corrente che dovrebbe generare il campo distruggerebbe lo stato superconduttore.

**Superconduttori di tipo II.** Comprendono leghe e composti, come niobio-titanio (NbTi, $T_c \approx 9\ \mathrm{K}$) e niobio-stagno (Nb$_3$Sn, $T_c \approx 18\ \mathrm{K}$), oltre al niobio puro e a tutti i superconduttori ad alta temperatura critica. Essi presentano due campi critici. Per $B < B_{c1}$ si comportano come quelli di tipo I, con espulsione completa del campo. Per $B_{c1} < B < B_{c2}$ entrano in uno **stato misto** (o stato di vortice): il campo penetra parzialmente nel materiale sotto forma di sottili tubi di flusso, detti **vortici di Abrikosov**, ciascuno dei quali trasporta un quanto di flusso magnetico $\Phi_0 = h/(2e) \approx 2{,}07\times10^{-15}\ \mathrm{Wb}$, circondati da regioni che restano superconduttrici. Solo per $B > B_{c2}$ la superconduttività scompare del tutto. Il campo $B_{c2}$ può essere molto elevato: circa $10\ \mathrm{T}$ per NbTi e oltre $20\ \mathrm{T}$ per Nb$_3$Sn a $4\ \mathrm{K}$. Per trasportare grandi correnti nello stato misto senza dissipazione occorre impedire che i vortici si muovano sotto l'azione della forza esercitata dalla corrente: a questo scopo si introducono deliberatamente difetti nel materiale che "ancorano" i vortici (**pinning**). È grazie ai superconduttori di tipo II che si costruiscono i magneti per la risonanza magnetica negli ospedali e quelli che curvano i fasci di particelle negli acceleratori come LHC al CERN, dove cavi di NbTi raffreddati a $1{,}9\ \mathrm{K}$ producono campi di oltre $8\ \mathrm{T}$.

**Bassa e alta temperatura critica.** Per i primi settant'anni dalla scoperta, le temperature critiche note rimasero al di sotto di circa $23\ \mathrm{K}$, il che richiedeva il costoso raffreddamento con elio liquido ($4{,}2\ \mathrm{K}$). Nel 1986 Bednorz e Müller scoprirono la superconduttività in ossidi ceramici di rame (cuprati) e in breve tempo si trovarono composti come YBa$_2$Cu$_3$O$_7$ (YBCO), con $T_c \approx 92\ \mathrm{K}$, superiore alla temperatura di ebollizione dell'azoto liquido ($77\ \mathrm{K}$). Questi **superconduttori ad alta temperatura critica** (HTS) possono essere raffreddati con azoto liquido, molto più economico e semplice da maneggiare. Il record a pressione ambiente appartiene a cuprati a base di mercurio, con $T_c$ di circa $135\ \mathrm{K}$. Altri materiali di interesse sono il diboruro di magnesio (MgB$_2$, $T_c = 39\ \mathrm{K}$), scoperto nel 2001, e i superconduttori a base di ferro. Il meccanismo microscopico della superconduttività nei cuprati non è ancora completamente compreso e non sembra riconducibile alla sola teoria BCS: si parla per questo anche di **superconduttori non convenzionali**. Composti ricchi di idrogeno hanno mostrato temperature critiche vicine a quella ambiente, ma solo a pressioni enormi, dell'ordine di centinaia di gigapascal, che ne escludono per ora applicazioni pratiche.

Fra le applicazioni tecnologiche, oltre ai magneti, si ricordano i cavi superconduttori per la distribuzione di energia senza perdite Joule, i limitatori di corrente di guasto per le reti elettriche, i treni a levitazione magnetica e i **SQUID** (Superconducting Quantum Interference Devices), magnetometri sensibilissimi in grado di misurare campi dell'ordine di $10^{-15}\ \mathrm{T}$, usati anche per rilevare i deboli campi magnetici prodotti dall'attività cerebrale.

### Esercizio d'esempio

Un campione di piombo ha $T_c = 7{,}2\ \mathrm{K}$ e $B_c(0) = 0{,}080\ \mathrm{T}$. (a) Calcolare il campo critico a $T = 4{,}2\ \mathrm{K}$. (b) Un filo di piombo di raggio $r = 0{,}50\ \mathrm{mm}$ a $4{,}2\ \mathrm{K}$ trasporta corrente; sapendo che il campo magnetico sulla superficie di un filo rettilineo percorso dalla corrente $i$ vale $B = \mu_0 i/(2\pi r)$, stimare la corrente massima prima che il filo perda la superconduttività (criterio di Silsbee).

**Soluzione.** (a) Dalla legge empirica:
$$
B_c(4{,}2\ \mathrm{K}) = 0{,}080\ \mathrm{T}\left[1 - \left(\frac{4{,}2}{7{,}2}\right)^2\right] = 0{,}080\cdot(1 - 0{,}340)\ \mathrm{T} = 0{,}053\ \mathrm{T}.
$$
(b) Imponendo che il campo superficiale eguagli $B_c$:
$$
i_{\max} = \frac{2\pi r B_c}{\mu_0} = \frac{2\pi\cdot5{,}0\times10^{-4}\ \mathrm{m}\cdot0{,}053\ \mathrm{T}}{4\pi\times10^{-7}\ \mathrm{T\,m/A}} = 1{,}3\times10^{2}\ \mathrm{A}.
$$
Un filo di rame dello stesso diametro, con $R/\ell = \rho/(\pi r^2) = 2{,}2\times10^{-2}\ \Omega/\mathrm{m}$, dissiperebbe con questa corrente circa $370\ \mathrm{W}$ per metro a temperatura ambiente; nel piombo superconduttore la dissipazione è nulla.

### Punti chiave

- Al di sotto della **temperatura critica** $T_c$ un superconduttore ha resistenza in continua esattamente nulla; le correnti persistenti circolano senza attenuazione.
- L'**effetto Meissner** (espulsione del campo magnetico) distingue il superconduttore da un conduttore perfetto: esso è un diamagnete perfetto.
- La superconduttività è distrutta oltre un campo critico $B_c(T)$ e una densità di corrente critica $J_c$.
- I superconduttori di **tipo I** (metalli puri) hanno un unico campo critico basso e transizione netta.
- I superconduttori di **tipo II** (leghe, composti, ceramiche) presentano uno stato misto con vortici di flusso quantizzato fra $B_{c1}$ e $B_{c2}$, e sopportano campi elevati.
- I superconduttori **ad alta $T_c$** (cuprati, $T_c > 77\ \mathrm{K}$) si raffreddano con azoto liquido; il loro meccanismo non è del tutto spiegato dalla teoria BCS.
- Le applicazioni principali sono magneti per risonanza magnetica e acceleratori, SQUID e cavi di potenza senza perdite.

