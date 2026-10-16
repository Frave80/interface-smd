# Capitolo 22 — Circuiti elettrici continui

Un resistore, da solo, non può mantenere una corrente: le cariche che lo attraversano perdono energia negli urti e, in assenza di una sorgente che la reintegri, il moto si arresterebbe in un tempo brevissimo. Per far circolare una corrente stazionaria occorre un dispositivo capace di spingere le cariche "in salita", dal potenziale più basso a quello più alto, trasformando in energia elettrica un'altra forma di energia: il **generatore**. In questo capitolo studiamo i generatori, ideali e reali, e le loro caratteristiche, e formuliamo le **leggi di Kirchhoff**, che consentono di analizzare qualunque rete elettrica in regime stazionario, anche quando le semplici regole di serie e parallelo non sono sufficienti. Ci limitiamo ai circuiti in **corrente continua**, nei quali tensioni e correnti non dipendono dal tempo; i fenomeni transitori e i circuiti in regime variabile richiedono gli strumenti dell'elettromagnetismo che verranno sviluppati più avanti.

## 22.1 Generatori

Un **circuito elettrico** è un insieme di componenti collegati da conduttori in modo da formare uno o più percorsi chiusi per la corrente. Consideriamo il caso più semplice: un percorso chiuso costituito da un resistore e da conduttori di collegamento. Il campo elettrostatico è conservativo, ossia la sua circuitazione lungo qualunque linea chiusa è nulla:

$$
\oint \vec{E}_{es}\cdot\mathrm{d}\vec{\ell} = 0 .
$$

D'altra parte, per la legge di Ohm locale, in ogni punto del circuito si ha $\vec{E} = \rho\vec{J}$ e, poiché la corrente circola sempre nello stesso verso lungo il percorso, l'integrale $\oint \rho\vec{J}\cdot\mathrm{d}\vec{\ell}$ è strettamente positivo. Le due affermazioni sono incompatibili: un campo puramente elettrostatico non può sostenere una corrente stazionaria in un circuito chiuso. In termini energetici, le cariche perdono energia nei tratti resistivi per effetto Joule e un campo conservativo non può restituirgliela lungo un percorso che torna al punto di partenza. Serve dunque una regione del circuito in cui agisca sulle cariche una forza di natura **non elettrostatica**, capace di compiere lavoro positivo su un ciclo chiuso. Tale regione è il **generatore**.

### 22.1.1 Generatore ideale

All'interno di un generatore agisce sui portatori di carica, oltre al campo elettrostatico $\vec{E}_{es}$, una forza di origine diversa (chimica, meccanica, elettromagnetica, luminosa) che, divisa per la carica, definisce un **campo elettromotore** $\vec{E}_m$, non conservativo e diverso da zero solo all'interno del generatore. Si definisce **forza elettromotrice** (f.e.m.) del generatore il lavoro compiuto da questo campo per unità di carica lungo il circuito chiuso:

$$
\mathcal{E} = \oint \vec{E}_m\cdot\mathrm{d}\vec{\ell} = \int_{-}^{+} \vec{E}_m\cdot\mathrm{d}\vec{\ell} ,
$$

dove l'ultimo integrale è esteso all'interno del generatore, dal **polo negativo** al **polo positivo**. Nonostante il nome, la forza elettromotrice non è una forza ma un lavoro per unità di carica, e si misura quindi in volt.

Il campo elettromotore separa le cariche: spinge le cariche positive verso il polo positivo e quelle negative verso il polo negativo. Questo accumulo di cariche sui poli genera un campo elettrostatico che, all'interno del generatore, si oppone al campo elettromotore. A circuito aperto la separazione prosegue finché i due campi non si bilanciano esattamente, $\vec{E}_{es} = -\vec{E}_m$, e la corrente interna si arresta. In questa condizione la differenza di potenziale fra i poli è

$$
V_+ - V_- = -\int_{-}^{+}\vec{E}_{es}\cdot\mathrm{d}\vec{\ell} = \int_{-}^{+}\vec{E}_m\cdot\mathrm{d}\vec{\ell} = \mathcal{E} .
$$

La forza elettromotrice coincide quindi con la **tensione a vuoto**, cioè con la differenza di potenziale misurata ai capi del generatore quando non eroga corrente. Questo fornisce anche un metodo operativo per misurarla: un voltmetro di resistenza interna molto elevata, collegato ai morsetti, preleva una corrente trascurabile e legge praticamente $\mathcal{E}$.

Un **generatore ideale di tensione** è un dispositivo che mantiene fra i suoi morsetti una differenza di potenziale pari a $\mathcal{E}$ *qualunque sia* la corrente erogata. La sua caratteristica tensione-corrente è una retta orizzontale: $\Delta V = \mathcal{E}$ per ogni $i$. Nei disegni dei circuiti viene rappresentato da due tratti paralleli di lunghezza diversa (il più lungo indica il polo positivo) o da un cerchio con i segni $+$ e $-$.

Collegando un generatore ideale a un resistore $R$, la corrente vale $i = \mathcal{E}/R$ e la potenza erogata dal generatore, cioè il lavoro compiuto dal campo elettromotore nell'unità di tempo, è

$$
P_g = \mathcal{E}\,i ,
$$

che coincide con la potenza $R i^2$ dissipata nel resistore, in accordo con la conservazione dell'energia. Il generatore ideale è un'astrazione: se si cortocircuitassero i suoi morsetti ($R \to 0$), la corrente e la potenza diverrebbero infinite, cosa impossibile per qualunque dispositivo reale. Nonostante ciò, esso è uno strumento di modellizzazione indispensabile.

Accanto al generatore ideale di tensione esiste il **generatore ideale di corrente**, che eroga una corrente $i_0$ fissata qualunque sia la tensione ai suoi capi, cioè qualunque sia il carico collegato. La sua caratteristica è una retta verticale. Anche questo è un'idealizzazione, utile per modellare alcuni dispositivi elettronici, come i transistor in determinate condizioni di funzionamento.

### 22.1.2 Generatore reale

Nessun generatore reale è in grado di mantenere una tensione costante indipendentemente dalla corrente erogata. All'interno di una pila, ad esempio, le cariche devono attraversare l'elettrolita e gli elettrodi, che oppongono una resistenza al loro passaggio e dissipano energia per effetto Joule. Sperimentalmente si osserva che la tensione ai morsetti diminuisce, con buona approssimazione in modo lineare, al crescere della corrente erogata. Questo comportamento si modella rappresentando il **generatore reale** come un generatore ideale di f.e.m. $\mathcal{E}$ in serie con una **resistenza interna** $r$:

$$
\Delta V = \mathcal{E} - r\,i .
$$

La caratteristica è ora una retta con pendenza negativa $-r$, che interseca l'asse delle tensioni nella **tensione a vuoto** $\mathcal{E}$ (per $i = 0$) e l'asse delle correnti nella **corrente di cortocircuito** $i_{cc} = \mathcal{E}/r$ (per $\Delta V = 0$). Un generatore è tanto più vicino all'ideale quanto più piccola è la sua resistenza interna rispetto alla resistenza del carico.

Collegando il generatore reale a un carico di resistenza $R$, la corrente è

$$
i = \frac{\mathcal{E}}{R + r},
$$

e la tensione ai morsetti vale $\Delta V = \mathcal{E}\,R/(R+r)$: il generatore e il carico formano un partitore di tensione. Dal punto di vista energetico, il generatore produce la potenza $\mathcal{E}i$, di cui una parte $r i^2$ viene dissipata internamente e la parte restante $R i^2$ viene trasferita al carico. Il **rendimento** del generatore è

$$
\eta = \frac{R\,i^2}{\mathcal{E}\,i} = \frac{R}{R + r} ,
$$

che tende a 1 quando $R \gg r$.

Un problema classico è quello del **massimo trasferimento di potenza**: quale valore di $R$ rende massima la potenza ceduta al carico? Si ha

$$
P_R = R\,i^2 = \frac{\mathcal{E}^2 R}{(R + r)^2} .
$$

Derivando rispetto a $R$ e uguagliando a zero si ottiene $(R + r)^2 - 2R(R + r) = 0$, cioè $R = r$. In questa condizione, detta di **adattamento** del carico, la potenza massima vale $P_{\max} = \mathcal{E}^2/(4r)$ e il rendimento è solo del $50\,\%$: metà della potenza prodotta viene dissipata nel generatore. La condizione di adattamento è ricercata in elettronica e nelle telecomunicazioni, dove interessa trasferire al carico il segnale più intenso possibile; nella distribuzione di energia elettrica si preferisce invece $R \gg r$, per massimizzare il rendimento.

Esiste anche un modello alternativo e del tutto equivalente del generatore reale: un generatore ideale di corrente $i_{cc} = \mathcal{E}/r$ in parallelo con la resistenza $r$. Le due rappresentazioni, dette rispettivamente di **Thévenin** e di **Norton**, producono la stessa caratteristica ai morsetti e sono quindi indistinguibili dall'esterno. La resistenza interna di una pila non è una costante assoluta: cresce man mano che la pila si scarica e varia con la temperatura, ed è questo il motivo per cui una batteria scarica può mostrare una tensione a vuoto quasi normale ma "crollare" non appena le si chiede corrente.

Se in un circuito il generatore è costretto da un altro generatore più potente a far circolare corrente in verso opposto (dal polo positivo al negativo al suo interno), come accade in una batteria in ricarica, esso assorbe potenza e la tensione ai morsetti diventa $\Delta V = \mathcal{E} + r\,i$, maggiore della f.e.m.

### 22.1.3 Tipi di generatore

I generatori si classificano in base al tipo di energia che convertono in energia elettrica, cioè all'origine del campo elettromotore.

I **generatori elettrochimici** (pile e accumulatori) convertono energia chimica. In una pila due elettrodi di materiali diversi sono immersi in un elettrolita; le reazioni di ossidazione e riduzione che avvengono alle interfacce elettrodo-elettrolita trasferiscono elettroni e producono una separazione di carica. La f.e.m. dipende dalla coppia di materiali impiegati ed è tipicamente di $1$–$4\ \mathrm{V}$ per cella: circa $1{,}5\ \mathrm{V}$ per le pile alcaline, $2{,}0\ \mathrm{V}$ per una cella al piombo, $3{,}6$–$3{,}7\ \mathrm{V}$ per una cella agli ioni di litio. Le pile primarie non sono ricaricabili, mentre gli **accumulatori** (batterie secondarie) permettono di invertire la reazione facendo circolare corrente in verso opposto. Una caratteristica importante di una batteria è la **capacità**, cioè la carica totale che può erogare, espressa di solito in amperora ($1\ \mathrm{Ah} = 3600\ \mathrm{C}$). Collegando più celle in serie si ottengono tensioni maggiori, come nella batteria da $12\ \mathrm{V}$ delle automobili, costituita da sei celle al piombo.

I **generatori elettromagnetici** (dinamo e alternatori) convertono energia meccanica sfruttando l'induzione elettromagnetica: un conduttore che si muove in un campo magnetico, o una spira attraversata da un flusso magnetico variabile, è sede di una f.e.m. indotta. Su questo principio si basano gli alternatori delle centrali termoelettriche, idroelettriche ed eoliche, che producono la quasi totalità dell'energia elettrica distribuita in rete. Questi generatori saranno studiati nel capitolo dedicato all'elettromagnetismo; qui basti osservare che il campo elettromotore è in questo caso la forza di Lorentz per unità di carica.

I **generatori fotovoltaici** convertono l'energia della radiazione elettromagnetica. In una cella solare, costituita da una giunzione fra due strati di semiconduttore diversamente drogati, i fotoni assorbiti creano coppie elettrone-lacuna che il campo elettrico interno alla giunzione separa, producendo una f.e.m. di circa $0{,}5$–$0{,}7\ \mathrm{V}$ per cella. Le celle fotovoltaiche non sono ben descritte dal modello lineare $\mathcal{E} - ri$: la loro caratteristica è fortemente non lineare e si comportano piuttosto come generatori di corrente, con una corrente proporzionale all'irraggiamento.

I **generatori termoelettrici** sfruttano l'**effetto Seebeck**: in un circuito formato da due metalli diversi, le cui giunzioni sono mantenute a temperature differenti, si genera una f.e.m. dell'ordine di decine di microvolt per kelvin. Su questo effetto si basano le **termocoppie**, usate come termometri, e i generatori a radioisotopi che alimentano le sonde spaziali dirette verso i pianeti esterni, dove la luce solare è troppo debole.

Infine, i **generatori piezoelettrici** sfruttano la proprietà di alcuni cristalli, come il quarzo, di polarizzarsi elettricamente quando vengono deformati: è il principio degli accendini piezoelettrici e di molti sensori di pressione e accelerazione. In laboratorio si usano poi gli **alimentatori stabilizzati**, dispositivi elettronici che, a partire dalla rete, forniscono una tensione continua regolabile e approssimano molto bene un generatore ideale entro una corrente massima, oltre la quale intervengono limitando la corrente e comportandosi come generatori di corrente.

### Esercizio d'esempio

Una batteria ha tensione a vuoto $\mathcal{E} = 12{,}0\ \mathrm{V}$. Collegata a un resistore $R = 5{,}0\ \Omega$, la tensione ai suoi morsetti scende a $\Delta V = 11{,}5\ \mathrm{V}$. Determinare la resistenza interna, il rendimento in queste condizioni, la corrente di cortocircuito e la massima potenza trasferibile a un carico.

**Soluzione.** La corrente nel circuito è $i = \Delta V/R = 11{,}5/5{,}0 = 2{,}3\ \mathrm{A}$. Dalla caratteristica del generatore reale:
$$
r = \frac{\mathcal{E} - \Delta V}{i} = \frac{12{,}0 - 11{,}5}{2{,}3}\ \Omega = 0{,}22\ \Omega .
$$
Il rendimento è $\eta = R/(R+r) = 5{,}0/5{,}22 = 0{,}96$, cioè il $96\,\%$. La corrente di cortocircuito è $i_{cc} = \mathcal{E}/r = 12{,}0/0{,}22 = 55\ \mathrm{A}$. La massima potenza al carico si ottiene per $R = r = 0{,}22\ \Omega$ e vale
$$
P_{\max} = \frac{\mathcal{E}^2}{4r} = \frac{(12{,}0\ \mathrm{V})^2}{4\cdot0{,}22\ \Omega} = 1{,}6\times10^{2}\ \mathrm{W},
$$
con un rendimento di appena il $50\,\%$.

### Punti chiave

- Un campo elettrostatico, essendo conservativo, non può sostenere una corrente stazionaria in un circuito chiuso: serve un **campo elettromotore** non conservativo.
- La **forza elettromotrice** $\mathcal{E} = \oint\vec{E}_m\cdot\mathrm{d}\vec{\ell}$ è un lavoro per unità di carica, si misura in volt e coincide con la tensione a vuoto.
- Il **generatore ideale di tensione** mantiene $\Delta V = \mathcal{E}$ per ogni corrente; quello ideale di corrente eroga $i_0$ per ogni tensione.
- Il **generatore reale** si modella come ideale in serie con una resistenza interna: $\Delta V = \mathcal{E} - r i$.
- Il rendimento è $\eta = R/(R+r)$; il **massimo trasferimento di potenza** si ha per $R = r$, con $\eta = 50\,\%$.
- I modelli di Thévenin (tensione + serie) e Norton (corrente + parallelo) sono equivalenti.
- I generatori convertono energia chimica (pile), meccanica (alternatori), luminosa (celle fotovoltaiche), termica (termocoppie) o elastica (piezoelettrici).

## 22.2 Leggi di Kirchhoff

Le regole di composizione in serie e in parallelo permettono di risolvere i circuiti più semplici, ma falliscono non appena la rete contiene più generatori in rami diversi o collegamenti che non sono né in serie né in parallelo, come nel ponte di Wheatstone sbilanciato. Per analizzare una rete di forma qualsiasi servono principi generali. Nel 1845 Gustav Kirchhoff, allora ancora studente, formulò due leggi che, insieme alle relazioni costitutive dei singoli componenti (legge di Ohm per i resistori, caratteristica dei generatori), consentono di determinare tutte le correnti e tutte le tensioni di una rete in regime stazionario. Esse non sono principi nuovi, ma la traduzione in linguaggio circuitale di due leggi fondamentali già note: la **conservazione della carica** e la **conservatività del campo elettrostatico** (equivalentemente, la conservazione dell'energia).

Per enunciarle con precisione è utile introdurre un po' di terminologia. Si chiama **nodo** un punto del circuito in cui convergono tre o più conduttori. Si chiama **ramo** un tratto di circuito compreso fra due nodi consecutivi, contenente uno o più componenti in serie e quindi percorso da un'unica corrente. Si chiama **maglia** un qualunque percorso chiuso formato da rami del circuito, che non passi due volte per lo stesso nodo. Una maglia che non racchiude al suo interno altri rami si dice **maglia elementare** (o anello). I conduttori di collegamento si considerano ideali, cioè privi di resistenza: tutti i punti di un filo ideale sono allo stesso potenziale.

### 22.2.1 Prima legge di Kirchhoff

La **prima legge di Kirchhoff**, o **legge dei nodi**, afferma che in ogni nodo di un circuito in regime stazionario la somma algebrica delle correnti è nulla:

$$
\sum_{k} i_k = 0 ,
$$

dove si attribuisce, per convenzione, segno positivo alle correnti entranti nel nodo e segno negativo a quelle uscenti (o viceversa, purché la scelta sia coerente). In forma equivalente: la somma delle correnti che entrano in un nodo è uguale alla somma delle correnti che ne escono.

La legge dei nodi è una conseguenza diretta della **conservazione della carica** e dell'ipotesi di regime stazionario. Consideriamo una superficie chiusa $\Sigma$ che racchiuda il nodo. L'equazione di continuità, in forma integrale, afferma che il flusso uscente della densità di corrente attraverso $\Sigma$ è uguale alla diminuzione per unità di tempo della carica contenuta all'interno:

$$
\oint_\Sigma \vec{J}\cdot\hat{n}\,\mathrm{d}S = -\frac{\mathrm{d}Q_{int}}{\mathrm{d}t} .
$$

In regime stazionario la carica contenuta nel nodo non varia, quindi il secondo membro è nullo. Il primo membro, d'altra parte, è non nullo solo dove la superficie interseca i conduttori, e ciascuna intersezione contribuisce con la corrente del relativo conduttore, con segno positivo se uscente e negativo se entrante. Si ottiene così proprio $\sum_k i_k = 0$. La legge vale non solo per un nodo puntiforme, ma per qualunque superficie chiusa che tagli il circuito: la somma algebrica delle correnti che attraversano una superficie chiusa è nulla. Questa generalizzazione è utile, ad esempio, per dimostrare che la corrente che entra in una "scatola nera" con due soli terminali è uguale a quella che ne esce.

Va sottolineato l'ambito di validità. In regime variabile, ad esempio durante la carica di un condensatore, la carica può accumularsi su un'armatura e la legge dei nodi, applicata a una superficie che racchiuda una sola armatura, non vale più. Si continua però ad applicarla ai nodi del circuito, che sono puntiformi e non accumulano carica in modo apprezzabile, nell'**approssimazione quasi stazionaria**, valida finché le dimensioni del circuito sono piccole rispetto alla lunghezza d'onda associata alle variazioni dei segnali.

Nell'applicazione pratica, i versi delle correnti nei rami sono in generale sconosciuti a priori. Si sceglie allora arbitrariamente un verso per ciascuna corrente, indicandolo con una freccia sullo schema, e si scrivono le equazioni coerentemente. Se alla fine del calcolo una corrente risulta negativa, significa semplicemente che il suo verso effettivo è opposto a quello ipotizzato; il valore assoluto resta corretto. In un circuito con $N$ nodi, le equazioni dei nodi linearmente indipendenti sono $N - 1$: l'equazione dell'ultimo nodo è sempre combinazione delle altre, perché ogni corrente di ramo entra in un nodo ed esce da un altro e, sommando tutte le equazioni, ogni corrente compare due volte con segni opposti.

### 22.2.2 Seconda legge di Kirchhoff

La **seconda legge di Kirchhoff**, o **legge delle maglie**, afferma che lungo ogni maglia di un circuito la somma algebrica delle forze elettromotrici è uguale alla somma algebrica delle cadute di tensione sulle resistenze:

$$
\sum_{k} \mathcal{E}_k = \sum_{k} R_k\, i_k .
$$

Una formulazione equivalente, spesso più comoda, afferma che la somma algebrica delle **differenze di potenziale** incontrate percorrendo una maglia chiusa è nulla:

$$
\sum_{k} \Delta V_k = 0 .
$$

Il fondamento fisico di questa legge è la **conservatività del campo elettrostatico**: il potenziale elettrico è una funzione di punto, quindi partendo da un punto qualsiasi della maglia e tornandovi dopo averla percorsa interamente, la variazione totale di potenziale deve essere nulla. Possiamo anche ricavarla a partire dalle leggi locali. Lungo la maglia il campo totale che agisce sulle cariche è $\vec{E}_{es} + \vec{E}_m$, e per la legge di Ohm locale generalizzata $\vec{E}_{es} + \vec{E}_m = \rho\vec{J}$. Integrando lungo la linea chiusa e ricordando che la circuitazione di $\vec{E}_{es}$ è nulla, si ottiene

$$
\oint \vec{E}_m\cdot\mathrm{d}\vec{\ell} = \oint \rho\,\vec{J}\cdot\mathrm{d}\vec{\ell} \quad\Longrightarrow\quad \sum_k \mathcal{E}_k = \sum_k R_k\,i_k ,
$$

perché il primo integrale è la somma delle f.e.m. dei generatori presenti nella maglia, mentre il secondo, spezzato sui vari rami, dà per ciascun resistore il prodotto $R_k i_k$. Moltiplicando per la carica, la legge delle maglie esprime anche la **conservazione dell'energia**: il lavoro fatto dai generatori su una carica che percorre l'intera maglia è uguale all'energia dissipata nei resistori.

Per applicare correttamente la legge occorre una precisa **convenzione dei segni**. Si sceglie un verso di percorrenza della maglia (orario o antiorario, arbitrario). Allora:

- una f.e.m. si conta con segno positivo se il verso di percorrenza attraversa il generatore dal polo negativo al polo positivo, negativo altrimenti;
- una caduta $R_k i_k$ si conta con segno positivo se il verso di percorrenza coincide con il verso ipotizzato della corrente $i_k$ in quel resistore, negativo altrimenti.

Nel formalismo delle differenze di potenziale, equivalentemente, attraversando un resistore nel verso della corrente il potenziale diminuisce di $R i$, mentre attraversando un generatore dal polo negativo al positivo aumenta di $\mathcal{E}$. Le resistenze interne dei generatori reali vanno trattate come resistori in serie al generatore ideale.

Combinando le due leggi si ottiene un procedimento sistematico, detto **metodo dei rami**, per risolvere una rete con $N$ nodi e $B$ rami. Le incognite sono le $B$ correnti di ramo. Si scrivono $N-1$ equazioni ai nodi indipendenti e $B - (N - 1)$ equazioni alle maglie indipendenti; una scelta sicura è prendere tutte le maglie elementari di un circuito disegnato senza incroci, che sono esattamente in questo numero. Si ottiene così un sistema lineare di $B$ equazioni in $B$ incognite, che ammette soluzione unica. Per ridurre il numero di incognite si possono usare metodi più efficienti: il **metodo delle correnti di maglia**, in cui si assegna una corrente fittizia a ogni maglia elementare e la legge dei nodi è soddisfatta automaticamente, e il **metodo dei potenziali di nodo**, in cui si prendono come incognite i potenziali dei nodi rispetto a un nodo di riferimento (massa). Dalle leggi di Kirchhoff discendono inoltre importanti teoremi sulle reti lineari, come il **principio di sovrapposizione degli effetti** (la risposta a più generatori è la somma delle risposte a ciascuno agente da solo) e i teoremi di **Thévenin** e **Norton**, secondo cui ogni rete lineare vista da due morsetti è equivalente a un generatore reale.

Infine, una verifica sempre consigliabile al termine di un calcolo è il **bilancio energetico**: la potenza complessivamente erogata dai generatori, $\sum \mathcal{E}_k i_k$ (con il segno opportuno per i generatori che assorbono), deve eguagliare la potenza totale dissipata nei resistori, $\sum R_k i_k^2$.

### Esercizio d'esempio

Una rete è formata da due generatori ideali e tre resistori. Il ramo sinistro, fra i nodi A (in alto) e B (in basso), contiene $\mathcal{E}_1 = 12\ \mathrm{V}$ con il polo positivo verso A, in serie con $R_1 = 2{,}0\ \Omega$. Il ramo centrale, fra A e B, contiene solo $R_3 = 4{,}0\ \Omega$. Il ramo destro, fra A e B, contiene $\mathcal{E}_2 = 6{,}0\ \mathrm{V}$ con il polo positivo verso A, in serie con $R_2 = 3{,}0\ \Omega$. Determinare le correnti nei tre rami e verificare il bilancio energetico.

**Soluzione.** Scegliamo come versi positivi: $i_1$ nel ramo sinistro da B verso A, $i_2$ nel ramo destro da B verso A, $i_3$ nel ramo centrale da A verso B. La legge dei nodi in A dà
$$
i_1 + i_2 = i_3 .
$$
Maglia sinistra (ramo sinistro e ramo centrale, percorsa da B ad A nel ramo sinistro e da A a B in quello centrale):
$$
\mathcal{E}_1 = R_1 i_1 + R_3 i_3 \quad\Rightarrow\quad 12 = 2 i_1 + 4 i_3 .
$$
Maglia destra (ramo destro e ramo centrale, percorsa in modo analogo):
$$
\mathcal{E}_2 = R_2 i_2 + R_3 i_3 \quad\Rightarrow\quad 6 = 3 i_2 + 4 i_3 .
$$
Dalle ultime due: $i_1 = 6 - 2 i_3$ e $i_2 = 2 - \tfrac{4}{3} i_3$. Sostituendo nella legge dei nodi:
$$
6 - 2i_3 + 2 - \tfrac{4}{3}i_3 = i_3 \quad\Rightarrow\quad 8 = \tfrac{13}{3} i_3 \quad\Rightarrow\quad i_3 = \tfrac{24}{13}\ \mathrm{A} = 1{,}85\ \mathrm{A}.
$$
Quindi $i_1 = 6 - 3{,}69 = 2{,}31\ \mathrm{A}$ e $i_2 = 2 - 2{,}46 = -0{,}46\ \mathrm{A}$. Il segno negativo indica che nel ramo destro la corrente scorre in realtà da A verso B: il generatore $\mathcal{E}_2$ è attraversato dal polo positivo al negativo e sta *assorbendo* potenza (come una batteria in ricarica).

Bilancio energetico: potenza erogata da $\mathcal{E}_1$: $12\cdot2{,}31 = 27{,}7\ \mathrm{W}$; potenza erogata da $\mathcal{E}_2$: $6{,}0\cdot(-0{,}46) = -2{,}8\ \mathrm{W}$ (cioè assorbita). Totale netto: $24{,}9\ \mathrm{W}$. Potenze dissipate: $R_1 i_1^2 = 2\cdot5{,}33 = 10{,}7\ \mathrm{W}$, $R_2 i_2^2 = 3\cdot0{,}21 = 0{,}6\ \mathrm{W}$, $R_3 i_3^2 = 4\cdot3{,}41 = 13{,}6\ \mathrm{W}$. Totale $24{,}9\ \mathrm{W}$, in accordo con la potenza netta erogata.

### Punti chiave

- Un **nodo** è un punto in cui convergono almeno tre conduttori, un **ramo** un tratto fra due nodi percorso da un'unica corrente, una **maglia** un percorso chiuso.
- La **legge dei nodi** $\sum i_k = 0$ discende dalla conservazione della carica in regime stazionario e vale per qualunque superficie chiusa.
- La **legge delle maglie** $\sum\mathcal{E}_k = \sum R_k i_k$ discende dalla conservatività del campo elettrostatico ed esprime la conservazione dell'energia.
- I versi delle correnti si scelgono arbitrariamente: un risultato negativo indica solo che il verso reale è opposto.
- Con $N$ nodi e $B$ rami servono $N-1$ equazioni ai nodi e $B-N+1$ equazioni alle maglie indipendenti.
- Metodi più efficienti (correnti di maglia, potenziali di nodo) e teoremi (sovrapposizione, Thévenin, Norton) derivano dalle leggi di Kirchhoff.
- Il bilancio fra potenza erogata dai generatori e potenza dissipata nei resistori è un controllo sempre utile della soluzione.

