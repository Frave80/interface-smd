# Capitolo 11 — Meccanica dei fluidi

La meccanica dei fluidi estende i principi della dinamica newtoniana a sistemi materiali continui che, a differenza dei solidi, non possiedono una forma propria e si adattano al recipiente che li contiene. Liquidi e gas, pur molto diversi per densità e comprimibilità, condividono una proprietà fondamentale: in condizioni di equilibrio non sono in grado di sostenere sforzi di taglio. Da questa semplice osservazione discendono l'isotropia della pressione, la legge di Stevin, i principi di Pascal e di Archimede. Il capitolo procede dalle proprietà meccaniche ed elastiche dei fluidi alla statica, passa per i fenomeni di superficie (tensione superficiale e capillarità), introduce gli strumenti per descrivere il moto (descrizioni lagrangiana ed euleriana) e arriva alla dinamica dei fluidi ideali (continuità, Bernoulli, Torricelli), dei fluidi viscosi (regimi laminare e turbolento, resistenza, portanza, effetto Magnus) e infine dei fluidi comprimibili, con la propagazione del suono e l'equazione generale dell'energia. Gli strumenti sviluppati sono quelli che un ingegnere usa quotidianamente per dimensionare tubazioni, serbatoi, pompe, profili alari e impianti idraulici.

## 11.1 Proprietà meccaniche

Prima di scrivere qualunque equazione del moto di un fluido occorre chiarire con quali grandezze lo si descrive. Un fluido è costituito da un numero enorme di molecole in continua agitazione: in un millimetro cubo d'acqua ve ne sono circa $3\times10^{19}$. Seguire ciascuna di esse è impossibile e del resto inutile; ciò che interessa all'ingegnere sono le proprietà medie su volumi piccoli rispetto alle dimensioni del sistema ma grandi rispetto alle distanze intermolecolari. È l'**ipotesi del continuo**: si suppone che la materia riempia lo spazio con continuità e che a ogni punto si possano associare grandezze locali come densità, pressione e velocità, funzioni regolari della posizione e del tempo. L'ipotesi vale finché le lunghezze caratteristiche del problema sono molto maggiori del cammino libero medio delle molecole; cade, per esempio, nei gas estremamente rarefatti dell'alta atmosfera o nei microcanali di dimensioni nanometriche. In questa sezione si introducono le tre proprietà meccaniche fondamentali: la densità, che descrive come è distribuita la massa; la pressione, che descrive gli sforzi normali; il comportamento rispetto al taglio, che distingue un fluido da un solido.

### 11.1.1 Densità

La **densità** (o massa volumica) in un punto è definita come il limite del rapporto tra la massa $\Delta m$ contenuta in un piccolo volume $\Delta V$ attorno al punto e il volume stesso:

$$
\rho = \lim_{\Delta V \to \delta V} \frac{\Delta m}{\Delta V} = \frac{dm}{dV}.
$$

Il limite non va inteso in senso matematico stretto: il volume $\delta V$ deve restare abbastanza grande da contenere molte molecole, altrimenti il rapporto fluttuerebbe in modo casuale a seconda che una molecola si trovi o meno al suo interno. Questo è il senso operativo dell'ipotesi del continuo. L'unità SI è il $\mathrm{kg/m^3}$. Valori tipici sono $\rho \approx 1000\ \mathrm{kg/m^3}$ per l'acqua a 4 °C, $\rho \approx 13\,600\ \mathrm{kg/m^3}$ per il mercurio, $\rho \approx 1{,}2\ \mathrm{kg/m^3}$ per l'aria a temperatura ambiente e pressione atmosferica. La differenza di circa tre ordini di grandezza tra liquidi e gas riflette la diversa distanza media tra le molecole: nei liquidi le molecole sono praticamente a contatto, nei gas sono separate da distanze circa dieci volte maggiori del loro diametro.

Nota la densità, la massa di un volume finito si ottiene integrando: $m = \int_V \rho\, dV$. Se la densità è uniforme il fluido si dice **omogeneo** e $m = \rho V$. Spesso si usa anche la **densità relativa**, rapporto adimensionale tra la densità di una sostanza e quella dell'acqua, e il **peso specifico** $\gamma = \rho g$, misurato in $\mathrm{N/m^3}$, comodo nei problemi idrostatici. La densità dipende in generale dalla temperatura e dalla pressione: nei liquidi la dipendenza è debole (l'acqua varia la propria densità di qualche per mille tra 0 °C e 30 °C), mentre nei gas è forte e, per un gas ideale, $\rho = pM/(RT)$, dove $M$ è la massa molare. Proprio questa differenza giustifica la distinzione tra **fluidi incomprimibili**, per i quali si può assumere $\rho$ costante, e **fluidi comprimibili**. Va osservato che anche un gas può essere trattato come incomprimibile se le variazioni di pressione in gioco sono piccole rispetto alla pressione stessa, come accade nei flussi d'aria a velocità molto inferiori a quella del suono.

### 11.1.2 Pressione

Consideriamo un piccolo elemento di superficie $dS$, orientato con versore normale $\hat n$, immerso nel fluido o appoggiato su una parete. Il fluido da una parte esercita sull'elemento una forza $d\vec F$. Si chiama **sforzo** (o tensione) la forza per unità di superficie $d\vec F/dS$; esso si decompone in una componente normale alla superficie e in una componente tangenziale. In un fluido in quiete, come vedremo nella sottosezione successiva, la componente tangenziale è nulla, e la forza è puramente normale e diretta verso la superficie, cioè compressiva. Si definisce allora la **pressione** come il modulo della forza normale per unità di superficie:

$$
p = \frac{dF_n}{dS}, \qquad d\vec F = -p\,\hat n\, dS,
$$

dove $\hat n$ è il versore uscente dalla porzione di fluido considerata. L'unità SI è il pascal, $1\ \mathrm{Pa} = 1\ \mathrm{N/m^2}$, unità molto piccola: la pressione atmosferica al livello del mare vale circa $1{,}013\times10^5\ \mathrm{Pa}$. Nella pratica tecnica si usano anche il bar ($10^5\ \mathrm{Pa}$), l'atmosfera ($101\,325\ \mathrm{Pa}$) e il millimetro di mercurio o torr ($\approx 133{,}3\ \mathrm{Pa}$).

Una proprietà essenziale è l'**isotropia della pressione**: in un fluido in quiete la pressione in un punto non dipende dall'orientazione della superficie su cui la si misura. Lo si dimostra considerando un piccolo prisma triangolare di fluido, con due facce ortogonali tra loro (di aree $dS_x$ e $dS_y$) e una faccia inclinata di area $dS$, tale che $dS_x = dS\sin\theta$ e $dS_y = dS\cos\theta$. Scrivendo l'equilibrio delle forze lungo $x$ e $y$, le forze di superficie sono proporzionali alle aree, cioè al quadrato della dimensione lineare $\ell$ del prisma, mentre il peso è proporzionale al volume, cioè a $\ell^3$. Facendo tendere a zero le dimensioni, il peso diventa trascurabile e l'equilibrio impone $p_x\,dS\sin\theta = p\,dS\sin\theta$ e $p_y\,dS\cos\theta = p\,dS\cos\theta$, da cui $p_x = p_y = p$ qualunque sia $\theta$. La pressione è dunque una grandezza **scalare**, funzione del punto $p(\vec r)$, anche se genera forze vettoriali sulle superfici.

Microscopicamente, la pressione di un gas nasce dagli urti delle molecole contro le pareti: ogni urto trasferisce quantità di moto, e la media temporale della quantità di moto trasferita per unità di tempo e di superficie è proprio la pressione. Nei liquidi contribuiscono anche le forze repulsive a corto raggio tra molecole. Occorre infine distinguere la **pressione assoluta**, misurata rispetto al vuoto, dalla **pressione relativa** (o manometrica), misurata rispetto alla pressione atmosferica: un manometro per pneumatici che indica 2 bar segnala una pressione assoluta di circa 3 bar.

### 11.1.3 Taglio

Lo **sforzo di taglio** è la componente tangenziale della forza per unità di superficie, $\tau = dF_t/dS$. Esso è ciò che distingue in modo netto un fluido da un solido. Un solido sottoposto a uno sforzo di taglio si deforma di una quantità finita e poi raggiunge un nuovo equilibrio elastico: la deformazione è proporzionale allo sforzo (legge di Hooke per il taglio). Un fluido, invece, sotto l'azione di uno sforzo di taglio anche piccolissimo si deforma indefinitamente, cioè **scorre**. Questa può essere presa come la definizione stessa di fluido: un mezzo continuo che non può restare in equilibrio in presenza di sforzi tangenziali. Ne segue immediatamente che in un fluido in quiete gli sforzi di taglio sono nulli, il che giustifica la definizione di pressione data sopra.

Nei fluidi in moto, invece, gli sforzi tangenziali esistono e sono legati non alla deformazione ma alla **velocità di deformazione**. L'esperimento tipico è quello di Couette semplificato: un sottile strato di fluido di spessore $h$ è compreso tra due lastre piane parallele; la lastra inferiore è ferma, quella superiore è trascinata con velocità $v_0$ da una forza $F$. Si osserva che, per molti fluidi, la forza necessaria è proporzionale all'area $S$ della lastra e alla velocità, e inversamente proporzionale allo spessore:

$$
\tau = \frac{F}{S} = \eta \frac{v_0}{h} \quad\longrightarrow\quad \tau = \eta\frac{dv}{dy}.
$$

La costante $\eta$ è la **viscosità dinamica**, misurata in $\mathrm{Pa\cdot s}$; i fluidi che obbediscono a questa relazione lineare si dicono **newtoniani** (acqua, aria, oli minerali). L'acqua a 20 °C ha $\eta \approx 1{,}0\times10^{-3}\ \mathrm{Pa\cdot s}$, l'aria $\eta \approx 1{,}8\times10^{-5}\ \mathrm{Pa\cdot s}$, la glicerina circa $1{,}4\ \mathrm{Pa\cdot s}$. Esistono poi fluidi **non newtoniani**, come il sangue, le vernici, il ketchup o le sospensioni di amido, nei quali la relazione tra sforzo e gradiente di velocità non è lineare o dipende dalla storia del moto. Si definisce anche la **viscosità cinematica** $\nu = \eta/\rho$, in $\mathrm{m^2/s}$, che compare naturalmente nelle equazioni del moto e nel numero di Reynolds.

Una conseguenza importante della viscosità è la **condizione di aderenza** (o di non scorrimento): a contatto con una parete solida il fluido assume la stessa velocità della parete. Questa condizione, verificata sperimentalmente in quasi tutti i casi pratici, implica che vicino alle pareti si formino zone con forti gradienti di velocità, gli **strati limite**, nei quali gli effetti viscosi sono dominanti anche per fluidi poco viscosi come l'aria. Un fluido ideale, privo di viscosità ($\eta = 0$), è un'astrazione utile quando gli effetti viscosi sono confinati in regioni sottili e il resto del moto è governato essenzialmente da inerzia e pressione.

### Esercizio d'esempio

Un sottile strato d'olio di viscosità $\eta = 0{,}25\ \mathrm{Pa\cdot s}$ e spessore $h = 0{,}50\ \mathrm{mm}$ separa una lastra quadrata di lato $L = 0{,}20\ \mathrm{m}$ da un piano fisso. Determinare la forza necessaria per trascinare la lastra a velocità costante $v_0 = 0{,}40\ \mathrm{m/s}$ e la potenza dissipata. Calcolare inoltre la massa d'olio contenuta nello strato, sapendo che $\rho = 880\ \mathrm{kg/m^3}$.

**Soluzione.** Assumendo un profilo lineare di velocità, il gradiente è $dv/dy = v_0/h = 0{,}40/(0{,}50\times10^{-3}) = 800\ \mathrm{s^{-1}}$. Lo sforzo di taglio vale $\tau = \eta\, v_0/h = 0{,}25\times800 = 200\ \mathrm{Pa}$. L'area della lastra è $S = L^2 = 0{,}040\ \mathrm{m^2}$, quindi

$$
F = \tau S = 200\times0{,}040 = 8{,}0\ \mathrm{N}.
$$

La potenza dissipata per attrito viscoso, uguale alla potenza fornita dalla forza a velocità costante, è $P = F v_0 = 8{,}0\times0{,}40 = 3{,}2\ \mathrm{W}$; essa si trasforma in calore nell'olio. Il volume dello strato è $V = S h = 0{,}040\times0{,}50\times10^{-3} = 2{,}0\times10^{-5}\ \mathrm{m^3}$, quindi la massa è $m = \rho V = 880\times2{,}0\times10^{-5} \approx 1{,}8\times10^{-2}\ \mathrm{kg}$, cioè circa 18 g.

### Punti chiave

- L'ipotesi del continuo permette di definire grandezze locali (densità, pressione, velocità) mediate su volumi piccoli ma contenenti molte molecole.
- La densità $\rho = dm/dV$ si misura in $\mathrm{kg/m^3}$; nei liquidi è quasi costante, nei gas dipende fortemente da $p$ e $T$.
- La pressione è la forza normale per unità di superficie, si misura in pascal ed è una grandezza scalare isotropa in un fluido in quiete.
- Pressione assoluta e relativa differiscono per la pressione atmosferica di riferimento.
- Un fluido non può sostenere sforzi di taglio in equilibrio: sotto taglio scorre indefinitamente.
- Nei fluidi newtoniani lo sforzo di taglio è proporzionale al gradiente di velocità, $\tau = \eta\, dv/dy$; $\eta$ è la viscosità dinamica, $\nu = \eta/\rho$ quella cinematica.
- A contatto con una parete il fluido viscoso ne assume la velocità (condizione di aderenza).

## 11.2 Proprietà elastiche

Le proprietà elastiche descrivono come un mezzo continuo risponde agli sforzi deformandosi. Nel capitolo sulla meccanica dei solidi si sono introdotti i moduli elastici di Young, di taglio e di compressibilità, legati da relazioni che dipendono dalla struttura del materiale. Per i fluidi il quadro si semplifica in modo drastico: poiché un fluido non può opporre resistenza statica al taglio, l'unica deformazione a cui reagisce elasticamente è la variazione di volume. La risposta al taglio è invece dissipativa, di natura viscosa, e ha una struttura matematica diversa da quella elastica. In questa sezione si confrontano i due comportamenti, mettendo in evidenza come la comprimibilità determini la velocità del suono e come la viscosità rappresenti l'analogo dinamico del modulo di taglio.

### 11.2.1 Compressione idrostatica

Si parla di **compressione idrostatica** quando un corpo è sottoposto a una pressione uniforme su tutta la sua superficie, come accade a un oggetto immerso in un fluido. In questa situazione il corpo non cambia forma ma solo volume. Se la pressione aumenta di $\Delta p$, il volume subisce una variazione relativa $\Delta V/V$ negativa; per piccole variazioni la relazione è lineare e si scrive

$$
\Delta p = -K \frac{\Delta V}{V}, \qquad K = -V\frac{dp}{dV},
$$

dove $K$ è il **modulo di compressibilità** (o modulo di bulk), misurato in pascal. Il segno meno garantisce che $K$ sia positivo, poiché a un aumento di pressione corrisponde una diminuzione di volume. Il suo inverso, $\beta = 1/K$, è la **compressibilità**. Poiché la massa si conserva, $\rho V = \text{cost}$, si ha $d\rho/\rho = -dV/V$ e il modulo può essere espresso anche in termini di densità: $K = \rho\, dp/d\rho$. Questa forma è particolarmente utile perché, come si vedrà nella sezione sui fluidi comprimibili, la velocità del suono in un mezzo è $c = \sqrt{K/\rho} = \sqrt{dp/d\rho}$.

I valori di $K$ differiscono enormemente tra liquidi e gas. Per l'acqua $K \approx 2{,}2\times10^9\ \mathrm{Pa}$: per ridurre di un solo punto percentuale il volume dell'acqua occorre un aumento di pressione di circa 220 bar, pari alla pressione che si trova a oltre 2 km di profondità nell'oceano. Per il mercurio $K\approx 2{,}8\times10^{10}\ \mathrm{Pa}$. È questo il motivo per cui nella stragrande maggioranza dei problemi i liquidi si trattano come incomprimibili. Per un gas, invece, il modulo di compressibilità è dello stesso ordine della pressione stessa. Per un gas ideale in trasformazione isoterma $pV = \text{cost}$, quindi $dp/dV = -p/V$ e $K_T = p$: a pressione atmosferica $K_T \approx 10^5\ \mathrm{Pa}$, oltre ventimila volte meno dell'acqua. Se la compressione è rapida e non c'è tempo per scambiare calore, la trasformazione è adiabatica, $pV^\gamma = \text{cost}$, e si ottiene $K_S = \gamma p$, con $\gamma = c_p/c_v \approx 1{,}4$ per l'aria. La distinzione tra modulo isotermo e adiabatico fu storicamente cruciale: Newton calcolò la velocità del suono usando $K_T$ e ottenne un valore errato di circa il 15%, corretto poi da Laplace con $K_S$.

Anche i solidi hanno un modulo di compressibilità, legato al modulo di Young $E$ e al coefficiente di Poisson $\nu_P$ dalla relazione $K = E/[3(1-2\nu_P)]$. Per l'acciaio $K \approx 1{,}6\times10^{11}\ \mathrm{Pa}$. È interessante notare che il modulo di compressibilità di liquidi e solidi è dello stesso ordine di grandezza: dal punto di vista della risposta volumetrica, un liquido somiglia molto più a un solido che a un gas, poiché in entrambi le molecole sono a stretto contatto e la compressione richiede di vincere le forze repulsive a corto raggio. La comprimibilità dei liquidi, pur piccola, non è sempre trascurabile: essa è responsabile del **colpo d'ariete**, la sovrapressione che si genera quando si chiude bruscamente una valvola in una condotta in cui scorre acqua, e che si propaga lungo il tubo alla velocità del suono nell'acqua (circa $1\,400$-$1\,500\ \mathrm{m/s}$, ridotta dall'elasticità delle pareti).

### 11.2.2 Taglio

Nei solidi la risposta al taglio è caratterizzata dal **modulo di taglio** $G$: uno sforzo tangenziale $\tau$ produce una deformazione angolare $\gamma_s$ secondo la legge $\tau = G\gamma_s$. La deformazione è finita e, rimosso lo sforzo, il solido ritorna alla configurazione iniziale. Per un fluido il modulo di taglio statico è nullo: qualunque sforzo tangenziale, anche minimo, provoca una deformazione che cresce nel tempo senza limite. Ciò che resta proporzionale allo sforzo non è la deformazione ma la sua rapidità di variazione:

$$
\tau = G\,\gamma_s \ \ (\text{solido elastico}), \qquad \tau = \eta\,\frac{d\gamma_s}{dt} \ \ (\text{fluido newtoniano}).
$$

Per verificare che la seconda forma coincide con la legge di Newton della viscosità vista nella sezione precedente, si consideri lo strato di fluido tra due lastre: un elemento di altezza $dy$, la cui faccia superiore si muove rispetto a quella inferiore con velocità relativa $dv$, ruota nel tempo $dt$ di un angolo $d\gamma_s = dv\,dt/dy$. Quindi $d\gamma_s/dt = dv/dy$ e si ritrova $\tau = \eta\,dv/dy$. Questa analogia formale mostra che la viscosità $\eta$ svolge, per i fluidi, il ruolo che il modulo di taglio $G$ svolge per i solidi, ma con una differenza fisica profonda: il lavoro compiuto dalle forze elastiche si immagazzina come energia potenziale ed è recuperabile, mentre il lavoro compiuto contro le forze viscose si dissipa irreversibilmente in calore.

Tra il comportamento puramente elastico e quello puramente viscoso esiste un'ampia gamma di materiali intermedi, detti **viscoelastici**. Il modello di Maxwell, per esempio, combina in serie una molla di modulo $G$ e uno smorzatore di viscosità $\eta$: per sollecitazioni rapide il materiale risponde come un solido elastico, per sollecitazioni lente come un fluido. Il rapporto $\tau_M = \eta/G$ è il **tempo di rilassamento** che separa i due regimi. Esempi quotidiani sono la plastilina "intelligente", che rimbalza se lanciata ma cola se lasciata ferma, e il vetro o la pece, che su tempi geologici o di decenni manifestano un lento scorrimento. Anche i comuni liquidi, a frequenze altissime (dell'ordine dei terahertz), mostrano una piccola rigidità di taglio, perché le molecole non hanno il tempo di riorganizzarsi.

La viscosità dipende fortemente dalla temperatura, e in modo opposto nei liquidi e nei gas. Nei liquidi diminuisce rapidamente al crescere della temperatura, perché l'agitazione termica aiuta le molecole a superare i legami con le vicine e a scorrere: l'olio motore a freddo è molto più denso che a caldo. Nei gas, invece, la viscosità cresce con la temperatura: il trasferimento di quantità di moto tra strati di fluido avviene tramite le molecole che migrano da uno strato all'altro, e questo trasporto è più efficace quando le molecole sono più veloci. La teoria cinetica prevede per un gas ideale $\eta \propto \sqrt{T}$ e, sorprendentemente, indipendente dalla pressione, risultato verificato da Maxwell stesso. Questa diversa origine microscopica sottolinea che la viscosità non è una proprietà "elastica" in senso stretto, ma un fenomeno di **trasporto** di quantità di moto, analogo alla conduzione del calore (trasporto di energia) e alla diffusione (trasporto di massa).

Riassumendo, dei tre moduli elastici che caratterizzano un solido isotropo, per un fluido sopravvive soltanto il modulo di compressibilità $K$; il modulo di taglio e il modulo di Young sono nulli in condizioni statiche. La risposta al taglio è sostituita dalla viscosità, che governa la dinamica ma non la statica. Questo spiega perché la statica dei fluidi, oggetto della prossima sezione, si costruisce interamente sulla sola grandezza pressione.

### Esercizio d'esempio

Un batiscafo scende a una profondità alla quale la pressione dell'acqua è aumentata di $\Delta p = 4{,}0\times10^7\ \mathrm{Pa}$ (circa 4 km) rispetto alla superficie. (a) Di quale frazione diminuisce il volume di un campione d'acqua, se $K = 2{,}2\times10^9\ \mathrm{Pa}$? (b) Di quanto aumenta la densità, partendo da $\rho_0 = 1025\ \mathrm{kg/m^3}$? (c) Confrontare con la variazione di volume di una bolla d'aria compressa isotermicamente da $p_0 = 1{,}0\times10^5\ \mathrm{Pa}$ alla stessa sovrapressione.

**Soluzione.** (a) Dalla definizione del modulo di compressibilità,

$$
\frac{\Delta V}{V} = -\frac{\Delta p}{K} = -\frac{4{,}0\times10^7}{2{,}2\times10^9} \approx -1{,}8\times10^{-2},
$$

cioè una riduzione di volume dell'1,8%. (b) Poiché $\Delta\rho/\rho \approx -\Delta V/V$, si ha $\Delta\rho \approx 1025\times1{,}8\times10^{-2} \approx 19\ \mathrm{kg/m^3}$, e la densità sale a circa $1044\ \mathrm{kg/m^3}$. (c) Per la bolla d'aria, isoterma: $p_0V_0 = pV$ con $p = p_0 + \Delta p = 4{,}01\times10^7\ \mathrm{Pa}$. Quindi $V/V_0 = p_0/p \approx 2{,}5\times10^{-3}$: il volume si riduce a un quattrocentesimo del valore iniziale. Il confronto mostra in modo quantitativo perché l'acqua possa considerarsi incomprimibile mentre l'aria no.

### Punti chiave

- Sotto compressione idrostatica un corpo cambia volume ma non forma; la risposta è descritta dal modulo di compressibilità $K = -V\,dp/dV = \rho\,dp/d\rho$.
- Per l'acqua $K \approx 2{,}2\times10^9\ \mathrm{Pa}$: i liquidi sono praticamente incomprimibili.
- Per un gas ideale $K_T = p$ (isoterma) e $K_S = \gamma p$ (adiabatica): i gas sono molto comprimibili.
- La velocità del suono dipende dal modulo di compressibilità: $c = \sqrt{K/\rho}$.
- Un fluido ha modulo di taglio statico nullo; la risposta al taglio è viscosa, $\tau = \eta\, d\gamma_s/dt$.
- La viscosità è l'analogo dinamico del modulo di taglio, ma dissipa energia invece di immagazzinarla.
- La viscosità dei liquidi diminuisce con la temperatura, quella dei gas aumenta: si tratta di un fenomeno di trasporto di quantità di moto.

## 11.3 Statica dei fluidi

La statica dei fluidi studia le condizioni di equilibrio di un fluido in quiete, rispetto a un sistema di riferimento inerziale o, più in generale, rispetto a un riferimento in cui il fluido appare fermo. Poiché un fluido in equilibrio non sostiene sforzi di taglio, le uniche forze di contatto sono quelle di pressione, e il problema si riduce a determinare come la pressione varia da punto a punto sotto l'azione delle forze di volume, tipicamente la gravità. Da un'unica equazione differenziale discendono risultati di enorme importanza pratica: la legge di Stevin, che regola la pressione nei serbatoi, nelle dighe e negli oceani; il principio di Pascal, alla base dei sistemi idraulici; il principio di Archimede, che spiega il galleggiamento delle navi e dei palloni aerostatici; la misura della pressione atmosferica e la sua diminuzione con la quota.

### 11.3.1 Equazione della statica dei fluidi

Si consideri un elemento di fluido a forma di parallelepipedo, con spigoli $dx$, $dy$, $dz$ paralleli agli assi, centrato nel punto $(x,y,z)$. Su di esso agiscono due tipi di forze. Le **forze di volume** (o di massa) sono proporzionali al volume e si esprimono come $\vec f\,dV$, dove $\vec f$ è la forza per unità di volume; nel caso della gravità $\vec f = \rho\vec g$. Le **forze di superficie** sono dovute alla pressione esercitata dal fluido circostante sulle sei facce. Lungo $x$, sulla faccia di sinistra agisce la forza $p(x)\,dy\,dz$ diretta verso $+x$, sulla faccia di destra la forza $p(x+dx)\,dy\,dz$ diretta verso $-x$. La forza netta lungo $x$ è quindi

$$
dF_x = \left[p(x) - p(x+dx)\right]dy\,dz = -\frac{\partial p}{\partial x}\,dx\,dy\,dz.
$$

Ripetendo il ragionamento per le altre direzioni si ottiene la forza di pressione netta per unità di volume, $-\nabla p$. È un risultato importante: una pressione uniforme, per quanto grande, non produce alcuna forza netta su un elemento di fluido; conta solo la sua variazione spaziale. L'equilibrio richiede che la somma delle forze sia nulla:

$$
-\nabla p + \vec f = 0 \qquad\Longrightarrow\qquad \nabla p = \rho\,\vec g.
$$

Questa è l'**equazione fondamentale della statica dei fluidi**. Essa afferma che il gradiente di pressione è parallelo alla forza di volume: le superfici isobare sono perpendicolari a $\vec f$. Nel campo gravitazionale terrestre, con asse $z$ verticale verso l'alto, $\vec g = -g\hat z$ e si ottiene $\partial p/\partial x = \partial p/\partial y = 0$ e $dp/dz = -\rho g$. La pressione dipende solo dalla quota e diminuisce salendo; le superfici isobare sono piani orizzontali. Ne segue che la superficie libera di un liquido in quiete, che è isobara alla pressione atmosferica, è orizzontale.

L'equazione si generalizza facilmente ai riferimenti non inerziali, aggiungendo le forze apparenti. In un recipiente che accelera orizzontalmente con accelerazione $\vec a$, la forza per unità di volume efficace è $\rho(\vec g - \vec a)$ e la superficie libera si inclina di un angolo $\theta$ con $\tan\theta = a/g$. In un recipiente cilindrico che ruota con velocità angolare $\omega$ attorno al proprio asse, la forza centrifuga $\rho\omega^2 r$ fa assumere alla superficie libera la forma di un paraboloide di rotazione, $z(r) = z_0 + \omega^2 r^2/(2g)$. Si noti infine che la condizione di equilibrio richiede che $\vec f/\rho$ sia conservativa: se $\vec f = -\rho\nabla U$, allora $p$ e $U$ sono costanti sulle stesse superfici.

### 11.3.2 Legge di Stevin

Per un liquido incomprimibile e omogeneo ($\rho$ costante) in un campo gravitazionale uniforme, l'equazione $dp/dz = -\rho g$ si integra immediatamente. Indicando con $h$ la profondità sotto la superficie libera, dove la pressione vale $p_0$, si ottiene la **legge di Stevin**:

$$
p(h) = p_0 + \rho g h.
$$

La pressione cresce linearmente con la profondità: nell'acqua aumenta di circa un'atmosfera ogni 10 m. Una forma equivalente, valida per due punti qualsiasi del fluido, è $p_1 + \rho g z_1 = p_2 + \rho g z_2$: la somma della pressione e del termine $\rho g z$, detto **pressione piezometrica**, è costante nel fluido in quiete.

La legge di Stevin ha conseguenze notevoli. La prima è il **paradosso idrostatico**: la pressione sul fondo di un recipiente dipende soltanto dall'altezza del liquido e non dalla forma del recipiente né dalla quantità di liquido contenuta. Tre recipienti con la stessa area di base, uno cilindrico, uno svasato verso l'alto e uno rastremato, riempiti fino alla stessa altezza, esercitano sul fondo la stessa forza, pur contenendo pesi di liquido diversi; la differenza è assorbita dalle componenti verticali delle forze sulle pareti laterali inclinate. La seconda conseguenza è il principio dei **vasi comunicanti**: in recipienti collegati alla base e contenenti lo stesso liquido, le superfici libere si dispongono alla stessa quota, perché sono tutte alla pressione atmosferica. Se i liquidi sono due, immiscibili e di densità diverse (come in un tubo a U con acqua e olio), le altezze misurate dalla superficie di separazione sono inversamente proporzionali alle densità: $\rho_1 h_1 = \rho_2 h_2$.

Sulla legge di Stevin si basano i **manometri a liquido**: un tubo a U contenente un liquido di densità nota, con un ramo collegato al recipiente e l'altro aperto, misura la pressione relativa come $\Delta p = \rho g\,\Delta h$. Una terza applicazione è il calcolo della **spinta su una parete**: su una diga rettangolare di larghezza $b$ e altezza $H$ la pressione relativa cresce linearmente da zero in superficie a $\rho g H$ al fondo, e la forza risultante vale $F = \int_0^H \rho g h\, b\,dh = \rho g b H^2/2$. Il punto di applicazione, detto **centro di spinta**, si trova a profondità $2H/3$, più in basso del baricentro della parete proprio perché la pressione aumenta con la profondità.

### 11.3.3 Principio di Pascal

Il **principio di Pascal** afferma che una variazione di pressione applicata in un punto di un fluido incomprimibile in equilibrio si trasmette inalterata a ogni altro punto del fluido e alle pareti del recipiente. È una conseguenza diretta della legge di Stevin: se la pressione sulla superficie libera passa da $p_0$ a $p_0 + \Delta p$, la pressione a ogni profondità diventa $p_0 + \Delta p + \rho g h$, cioè aumenta della stessa quantità $\Delta p$ ovunque. Per un fluido comprimibile la trasmissione non è istantanea: la perturbazione si propaga come un'onda alla velocità del suono, e solo al raggiungimento del nuovo equilibrio la variazione è uniforme.

L'applicazione più nota è il **torchio idraulico** (o leva idraulica). Due cilindri di sezioni $S_1 \ll S_2$, collegati e riempiti d'olio, sono chiusi da pistoni. Una forza $F_1$ sul pistone piccolo genera una sovrapressione $\Delta p = F_1/S_1$ che si trasmette al pistone grande, su cui produce la forza

$$
F_2 = \Delta p\, S_2 = F_1\frac{S_2}{S_1}.
$$

La forza è moltiplicata per il rapporto delle aree. Non si tratta però di energia gratuita: poiché l'olio è incomprimibile, il volume spostato è lo stesso, $S_1 d_1 = S_2 d_2$, e il pistone grande si sposta di una distanza ridotta dello stesso fattore. Il lavoro $F_1 d_1 = F_2 d_2$ si conserva, esattamente come in una leva meccanica. Su questo principio funzionano i sollevatori delle officine, i freni idraulici degli autoveicoli, le presse industriali, gli attuatori delle macchine movimento terra e i comandi di volo degli aerei.

### 11.3.4 Principio di Archimede

Un corpo immerso, totalmente o parzialmente, in un fluido in quiete riceve una forza verticale diretta verso l'alto, detta **spinta di Archimede**, pari al peso del fluido spostato:

$$
\vec F_A = -\rho_f V_{imm}\,\vec g,
$$

dove $\rho_f$ è la densità del fluido e $V_{imm}$ il volume immerso. La dimostrazione più elegante è quella per sostituzione: si immagini di rimuovere il corpo e di riempire la cavità con fluido identico a quello circostante. Questo fluido è in equilibrio, quindi la risultante delle forze di pressione che il fluido esterno esercita sulla sua superficie deve bilanciare esattamente il suo peso. Ma le forze di pressione dipendono solo dalla forma della superficie e non da ciò che essa contiene; rimettendo il corpo al suo posto, esse restano le stesse. La spinta è applicata nel **centro di spinta**, baricentro del volume di fluido spostato, che in generale non coincide con il baricentro del corpo.

Il confronto tra peso e spinta determina il comportamento del corpo. Se la densità media del corpo $\rho_c$ è maggiore di quella del fluido, il corpo affonda; se è minore, galleggia, emergendo finché il volume immerso soddisfa $\rho_f V_{imm} = \rho_c V$, cioè $V_{imm}/V = \rho_c/\rho_f$. Per un iceberg ($\rho_c \approx 917\ \mathrm{kg/m^3}$) in acqua di mare ($\rho_f \approx 1025\ \mathrm{kg/m^3}$) circa l'89% del volume è sommerso. Una nave d'acciaio galleggia perché la sua densità media, comprendente l'aria interna allo scafo, è minore di quella dell'acqua. La **stabilità** del galleggiamento dipende dalla posizione relativa del baricentro e del **metacentro**, punto di intersezione tra la retta d'azione della spinta in posizione inclinata e l'asse di simmetria: se il metacentro è al di sopra del baricentro, una piccola inclinazione genera un momento raddrizzante.

Il principio vale anche nei gas: un pallone aerostatico sale perché l'aria calda o l'elio al suo interno sono meno densi dell'aria circostante. Nelle misure di precisione con la bilancia occorre correggere per la spinta dell'aria, che per un oggetto di densità $1000\ \mathrm{kg/m^3}$ vale circa lo 0,12% del peso. Archimede stesso, secondo la tradizione, usò il principio per verificare la purezza dell'oro di una corona confrontandone la perdita apparente di peso in acqua con quella di un lingotto d'oro.

### 11.3.5 Pressione atmosferica

L'atmosfera terrestre è un fluido in equilibrio nel campo gravitazionale, e il suo peso genera al suolo una pressione, la **pressione atmosferica**. La sua prima misura si deve a Torricelli (1643): un tubo di vetro lungo circa un metro, chiuso a un'estremità e riempito di mercurio, viene capovolto in una bacinella di mercurio. La colonna scende fino a un'altezza di circa 760 mm, lasciando sopra di sé uno spazio quasi vuoto (contenente solo vapore di mercurio a pressione trascurabile). Applicando la legge di Stevin tra la superficie libera della bacinella, dove agisce $p_{atm}$, e la sommità della colonna, dove la pressione è praticamente nulla, si ottiene

$$
p_{atm} = \rho_{Hg}\,g\,h = 13\,595\times9{,}807\times0{,}760 \approx 1{,}013\times10^5\ \mathrm{Pa}.
$$

Questo valore definisce l'**atmosfera standard**. Con l'acqua, che è 13,6 volte meno densa, la colonna sarebbe alta circa 10,3 m: è questo il motivo per cui una pompa aspirante non può sollevare l'acqua oltre circa 10 m, fatto noto ai fontanieri fiorentini e che stimolò le ricerche di Torricelli. L'esperimento di Pascal sul Puy de Dôme (1648), in cui il barometro portato in quota mostrò una colonna più bassa, confermò che la pressione è dovuta al peso dell'aria sovrastante.

Una pressione di $10^5\ \mathrm{Pa}$ corrisponde a una forza di circa $10^5\ \mathrm{N}$ (il peso di dieci tonnellate) su ogni metro quadrato. Non ce ne accorgiamo perché la pressione agisce uniformemente da tutti i lati e i fluidi del nostro corpo sono alla stessa pressione. L'esperimento degli **emisferi di Magdeburgo** (Otto von Guericke, 1654), nel quale due semisfere metalliche svuotate d'aria non poterono essere separate da due tiri di cavalli, ne rese spettacolarmente evidente l'entità.

### 11.3.6 Equazione barometrica

La legge di Stevin non si applica all'atmosfera su grandi dislivelli, perché la densità dell'aria non è costante ma diminuisce con la pressione. Trattando l'aria come un gas ideale di massa molare $M \approx 0{,}029\ \mathrm{kg/mol}$, si ha $\rho = pM/(RT)$, e l'equazione della statica diventa

$$
\frac{dp}{dz} = -\frac{Mg}{RT}\,p.
$$

Nell'ipotesi semplificativa di **atmosfera isoterma** ($T$ costante), la soluzione è un esponenziale decrescente:

$$
p(z) = p_0\, e^{-z/H}, \qquad H = \frac{RT}{Mg},
$$

nota come **equazione barometrica** (o legge di Laplace). La grandezza $H$ è l'**altezza di scala**: per $T = 288\ \mathrm{K}$ si ottiene $H \approx 8{,}4\ \mathrm{km}$, cioè la pressione si riduce di un fattore $e$ ogni 8,4 km circa. A 5,5 km di quota la pressione è circa metà di quella al livello del mare; in cima all'Everest è circa un terzo. Lo stesso andamento esponenziale vale per la densità. Dal punto di vista microscopico, l'equazione barometrica è un caso particolare della **distribuzione di Boltzmann**: la probabilità di trovare una molecola a quota $z$ è proporzionale a $e^{-mgz/(k_BT)}$, con $m$ massa molecolare e $k_B$ costante di Boltzmann.

In realtà la temperatura nella troposfera decresce con la quota di circa $6{,}5\ \mathrm{K/km}$ (gradiente termico verticale). Assumendo $T(z) = T_0 - \Gamma z$ si ottiene una legge di potenza, $p = p_0(1 - \Gamma z/T_0)^{Mg/(R\Gamma)}$, che costituisce il modello di **atmosfera standard internazionale** usato in aeronautica per tarare gli altimetri, strumenti che non sono altro che barometri graduati in metri. Per piccoli dislivelli, sviluppando l'esponenziale al primo ordine, si ritrova la legge di Stevin con $\rho$ costante: $p \approx p_0(1 - z/H) = p_0 - \rho_0 g z$.

### Esercizio d'esempio

Un cubo di legno di lato $a = 0{,}20\ \mathrm{m}$ e densità $\rho_c = 600\ \mathrm{kg/m^3}$ galleggia in acqua dolce ($\rho_f = 1000\ \mathrm{kg/m^3}$). (a) Determinare la profondità di immersione. (b) Calcolare la massa minima da appoggiare sopra il cubo per farlo sommergere completamente. (c) Calcolare la pressione assoluta sulla faccia inferiore del cubo nel caso (a), con $p_0 = 1{,}013\times10^5\ \mathrm{Pa}$.

**Soluzione.** (a) All'equilibrio il peso è uguale alla spinta: $\rho_c a^3 g = \rho_f a^2 y g$, quindi

$$
y = a\frac{\rho_c}{\rho_f} = 0{,}20\times0{,}60 = 0{,}12\ \mathrm{m}.
$$

(b) Per la completa immersione la spinta massima è $\rho_f a^3 g$; deve bilanciare il peso del cubo più quello della massa aggiunta: $(\rho_c a^3 + m)g = \rho_f a^3 g$, da cui $m = (\rho_f - \rho_c)a^3 = 400\times8{,}0\times10^{-3} = 3{,}2\ \mathrm{kg}$. (c) Per la legge di Stevin, $p = p_0 + \rho_f g y = 1{,}013\times10^5 + 1000\times9{,}81\times0{,}12 = 1{,}013\times10^5 + 1{,}18\times10^3 \approx 1{,}025\times10^5\ \mathrm{Pa}$. Si può verificare che la forza netta di pressione sulla faccia inferiore, $(p - p_0)a^2 = 1{,}18\times10^3\times0{,}040 \approx 47\ \mathrm{N}$, coincide con il peso del cubo, $600\times8{,}0\times10^{-3}\times9{,}81 \approx 47\ \mathrm{N}$.

### Punti chiave

- L'equazione della statica dei fluidi è $\nabla p = \vec f$, con $\vec f = \rho\vec g$ nel campo gravitazionale: le isobare sono perpendicolari alla forza di volume.
- La legge di Stevin $p = p_0 + \rho g h$ vale per liquidi incomprimibili; la pressione dipende solo dalla profondità (paradosso idrostatico, vasi comunicanti).
- Il principio di Pascal: una variazione di pressione si trasmette inalterata in tutto il fluido; il torchio idraulico moltiplica la forza conservando il lavoro.
- Il principio di Archimede: la spinta è pari al peso del fluido spostato ed è applicata nel baricentro del volume immerso.
- La pressione atmosferica, misurata da Torricelli, vale circa $1{,}013\times10^5\ \mathrm{Pa}$, equivalente a 760 mm di mercurio o 10,3 m d'acqua.
- Nell'atmosfera isoterma la pressione decresce esponenzialmente con la quota, $p = p_0 e^{-z/H}$, con altezza di scala $H = RT/(Mg) \approx 8\ \mathrm{km}$.
- In un riferimento non inerziale occorre aggiungere le forze apparenti: superficie inclinata in accelerazione, paraboloide in rotazione.

## 11.4 Fenomeni di superficie

Finora il fluido è stato trattato come un mezzo continuo i cui punti interni sono tutti equivalenti. Alle superfici di separazione, però, accade qualcosa di nuovo: le molecole che si trovano sul confine tra un liquido e un gas, o tra due liquidi immiscibili, o tra un liquido e un solido, hanno un intorno diverso da quelle interne, e questa asimmetria dà origine a un insieme di fenomeni detti **fenomeni di superficie** o **capillari**. Essi spiegano perché le gocce sono sferiche, perché alcuni insetti camminano sull'acqua, perché la linfa risale nei vasi delle piante e perché i detergenti funzionano. I loro effetti sono trascurabili alle grandi scale, dove domina la gravità, ma diventano predominanti alle scale millimetriche e submillimetriche, rilevanti nella microfluidica, nella stampa a getto d'inchiostro, nella lubrificazione e nell'idrologia dei suoli.

### 11.4.1 Tensione superficiale

Si osserva sperimentalmente che la superficie libera di un liquido si comporta come una membrana elastica tesa, che tende a ridurre la propria area. Un ago d'acciaio appoggiato con cura galleggia sull'acqua pur essendo otto volte più denso; una lamina di sapone tesa su un telaio metallico con un lato mobile tende a contrarsi, trascinando il lato mobile. Per quantificare il fenomeno si consideri proprio questo esperimento: un telaio rettangolare con un lato mobile di lunghezza $\ell$ sostiene una lamina liquida. Per mantenere il lato fermo occorre applicare una forza $F$ proporzionale a $\ell$. Poiché la lamina ha due facce, si definisce la **tensione superficiale** come

$$
\sigma = \frac{F}{2\ell},
$$

cioè la forza per unità di lunghezza che agisce tangenzialmente alla superficie, perpendicolarmente a ogni linea tracciata su di essa. L'unità SI è il $\mathrm{N/m}$. Spostando il lato mobile di $dx$ a temperatura costante, la forza compie il lavoro $dW = F\,dx = \sigma\,2\ell\,dx = \sigma\,dA$, dove $dA$ è l'aumento di area totale. Dunque $\sigma$ si interpreta equivalentemente come il **lavoro necessario per aumentare di un'unità l'area della superficie**, misurabile in $\mathrm{J/m^2}$; più precisamente, in condizioni isoterme, $\sigma$ è l'energia libera per unità di area.

Valori tipici a 20 °C: acqua $\sigma \approx 0{,}073\ \mathrm{N/m}$, etanolo $0{,}022\ \mathrm{N/m}$, mercurio $0{,}49\ \mathrm{N/m}$, acqua saponata circa $0{,}025\ \mathrm{N/m}$. La tensione superficiale diminuisce al crescere della temperatura e si annulla al punto critico, dove scompare la distinzione tra liquido e vapore. Le sostanze **tensioattive** (saponi, detergenti), concentrandosi alla superficie, riducono drasticamente $\sigma$ e permettono all'acqua di bagnare meglio i tessuti e di inglobare le particelle di grasso.

Il fatto che una superficie liquida tenda a minimizzare la propria area, compatibilmente con i vincoli, spiega la forma sferica delle piccole gocce e delle bolle: la sfera è la figura che, a parità di volume, ha la superficie minima. Le gocce grandi invece si schiacciano per effetto della gravità; il confine tra i due regimi è fissato dalla **lunghezza capillare** $\ell_c = \sqrt{\sigma/(\rho g)}$, che per l'acqua vale circa 2,7 mm. Su scale minori di $\ell_c$ domina la tensione superficiale, su scale maggiori la gravità.

### 11.4.2 Legge di Laplace

Quando una superficie liquida è curva, la tensione superficiale produce una differenza di pressione tra i due lati, detta **pressione capillare** o **sovrapressione di Laplace**. Si consideri una goccia sferica di raggio $R$. Tagliandola idealmente lungo un piano diametrale, su ciascuna metà agiscono due forze opposte: la tensione superficiale lungo la circonferenza di taglio, $2\pi R\sigma$, che tende a riunire le due metà, e la differenza di pressione tra interno ed esterno agente sulla sezione $\pi R^2$, che tende a separarle. L'equilibrio impone $\Delta p\,\pi R^2 = 2\pi R\sigma$, quindi

$$
\Delta p = p_{int} - p_{est} = \frac{2\sigma}{R}.
$$

Lo stesso risultato si ottiene con il principio dei lavori virtuali: aumentando il raggio di $dR$, il lavoro della pressione $\Delta p\,4\pi R^2 dR$ deve uguagliare l'aumento di energia superficiale $\sigma\,8\pi R\,dR$. Per una **bolla di sapone**, che possiede due superfici (interna ed esterna), la sovrapressione raddoppia: $\Delta p = 4\sigma/R$. Per una superficie di forma generica, con raggi di curvatura principali $R_1$ e $R_2$, vale la **legge di Laplace** (o di Young-Laplace) nella forma generale

$$
\Delta p = \sigma\left(\frac{1}{R_1} + \frac{1}{R_2}\right),
$$

dove la pressione è maggiore dal lato concavo. Per una superficie cilindrica uno dei raggi è infinito e $\Delta p = \sigma/R$; per un piano $\Delta p = 0$.

La legge di Laplace ha conseguenze sorprendenti. La sovrapressione è inversamente proporzionale al raggio: più piccola è la bolla, maggiore la pressione interna. Se due bolle di sapone di diverso raggio vengono messe in comunicazione con un tubicino, la più piccola si svuota nella più grande, contrariamente all'intuizione che vorrebbe un riequilibrio verso dimensioni uguali. Nei polmoni, gli alveoli di diverse dimensioni sarebbero soggetti a questa instabilità se non fosse per il **surfattante polmonare**, che riduce la tensione superficiale in misura crescente al diminuire del raggio. La legge spiega anche perché è difficile far nascere bolle di vapore in un liquido perfettamente puro (le bolle iniziali, piccolissime, richiederebbero pressioni enormi) e perché l'ebollizione avviene preferenzialmente su impurità e asperità delle pareti.

### 11.4.3 Tensione interfacciale

Il concetto di tensione superficiale si estende a qualunque interfaccia tra due fasi. Si parla di **tensione interfacciale** $\sigma_{12}$ tra le fasi 1 e 2: ad esempio tra acqua e olio ($\sigma \approx 0{,}03$-$0{,}05\ \mathrm{N/m}$), tra liquido e solido, tra solido e gas. La tensione superficiale propriamente detta è la tensione interfacciale liquido-vapore (o liquido-aria). Quando tre fasi si incontrano lungo una linea, detta **linea di contatto** o **linea triplice**, come accade al bordo di una goccia appoggiata su un piano solido, le tre tensioni interfacciali agiscono su ogni elemento della linea, e l'equilibrio delle loro componenti parallele al piano solido fornisce l'**equazione di Young**:

$$
\sigma_{SG} = \sigma_{SL} + \sigma_{LG}\cos\theta,
$$

dove $\theta$ è l'**angolo di contatto**, misurato all'interno del liquido tra la superficie solida e la tangente alla superficie liquida. L'angolo di contatto caratterizza la **bagnabilità**: se $\theta < 90°$ il liquido **bagna** il solido e tende a spandersi (acqua su vetro pulito, $\theta \approx 0°$); se $\theta > 90°$ il liquido non bagna e forma gocce rotondeggianti (mercurio su vetro, $\theta \approx 140°$; acqua su teflon, $\theta \approx 110°$). Il caso limite $\theta = 0$ corrisponde alla **bagnabilità perfetta**, possibile quando $\sigma_{SG} \geq \sigma_{SL} + \sigma_{LG}$; si definisce allora il **coefficiente di spandimento** $S = \sigma_{SG} - \sigma_{SL} - \sigma_{LG}$, il cui segno decide se il liquido forma un film continuo.

Le superfici **superidrofobiche**, come la foglia di loto, combinano una chimica idrofoba con una rugosità micrometrica che intrappola aria: l'angolo di contatto apparente supera 150°, e le gocce rotolano via trascinando lo sporco (effetto autopulente). Le applicazioni tecnologiche della bagnabilità sono innumerevoli: verniciatura, saldatura, flottazione dei minerali, rivestimenti antiappannamento, tessuti impermeabili ma traspiranti.

### 11.4.4 Capillarità

Quando un tubo di piccolo diametro, detto **capillare**, viene immerso verticalmente in un liquido, il livello del liquido nel tubo si porta a una quota diversa da quella esterna: sale se il liquido bagna le pareti, scende se non le bagna. Questo fenomeno è la **capillarità** o **azione capillare**. La superficie libera nel tubo, detta **menisco**, è concava verso l'alto nel primo caso e convessa nel secondo.

L'altezza di risalita si ricava con un bilancio di forze sulla colonna sollevata. Lungo la linea di contatto, di lunghezza $2\pi r$, la tensione superficiale agisce con componente verticale $\sigma\cos\theta$ per unità di lunghezza; questa forza deve sostenere il peso della colonna, $\rho g\pi r^2 h$. Si ottiene la **legge di Jurin**:

$$
h = \frac{2\sigma\cos\theta}{\rho g r}.
$$

Lo stesso risultato si ricava dalla legge di Laplace: il menisco è approssimativamente una calotta sferica di raggio $R = r/\cos\theta$; sotto di esso la pressione è inferiore a quella atmosferica di $2\sigma/R$, e questo difetto di pressione deve essere compensato da una colonna idrostatica $\rho g h$. Per l'acqua in un capillare di vetro con $r = 0{,}1\ \mathrm{mm}$ e $\theta\approx0$ si trova $h \approx 15\ \mathrm{cm}$; per $r = 1\ \mu\mathrm{m}$ si arriverebbe a 15 m. Per il mercurio ($\cos\theta < 0$) $h$ è negativo e si osserva una **depressione capillare**: è il motivo per cui la lettura dei barometri a mercurio va corretta per il diametro del tubo.

La capillarità è fondamentale in natura e nella tecnica. Contribuisce alla risalita dell'acqua nei terreni e nei muri (umidità di risalita), all'imbibizione di carta, spugne e tessuti, all'azione degli stoppini delle candele e delle lampade a olio, al funzionamento delle penne stilografiche e dei tubi di calore (heat pipe) usati per il raffreddamento dei processori. Nella risalita della linfa negli alberi, invece, la capillarità da sola non basta: il ruolo principale è svolto dalla tensione negativa generata dall'evaporazione nelle foglie, ma i fenomeni di superficie restano essenziali nel garantire la coesione delle colonne d'acqua.

### 11.4.5 Modello atomico

L'origine microscopica della tensione superficiale risiede nelle **forze di coesione** tra le molecole del liquido, attrattive a media distanza (forze di van der Waals, legami a idrogeno nell'acqua). Una molecola all'interno del liquido è circondata in modo simmetrico da molecole vicine: le forze attrattive si compensano in media e la risultante è nulla. Una molecola in superficie, invece, ha vicini solo da un lato: la risultante delle attrazioni è diretta verso l'interno del liquido. Per portare una molecola dall'interno alla superficie occorre quindi compiere lavoro contro queste forze, e la superficie possiede un'**energia in eccesso** rispetto al volume. Il sistema tende a minimizzare l'energia riducendo il numero di molecole superficiali, cioè l'area.

Questo modello permette una stima d'ordine di grandezza. Se $\varepsilon$ è l'energia di legame tra due molecole vicine e ogni molecola interna ha $z$ primi vicini, in un impacchettamento compatto una molecola superficiale ne perde circa un quarto; poiché ciascun legame rotto è condiviso tra le due superfici che si creano tagliando idealmente il liquido, la sua energia in eccesso è dell'ordine di $z\varepsilon/8$. Detta $a$ la distanza intermolecolare, in superficie ci sono circa $1/a^2$ molecole per unità di area, quindi

$$
\sigma \sim \frac{z\varepsilon}{8a^2} \sim \frac{\Delta H_{vap}}{4 N_A a^2},
$$

dove si è usato il fatto che l'entalpia molare di vaporizzazione $\Delta H_{vap}$ corrisponde a rompere tutti i $z/2$ legami per molecola. Per l'acqua, con $\Delta H_{vap}\approx 4{,}1\times10^4\ \mathrm{J/mol}$ e $a\approx 3\times10^{-10}\ \mathrm{m}$, si ottiene circa $0{,}2\ \mathrm{N/m}$: un valore un po' più grande del dato sperimentale (il modello trascura l'agitazione termica e il riarrangiamento delle molecole superficiali), ma con il corretto ordine di grandezza, risultato notevole per una stima così rozza. Questo legame tra tensione superficiale e calore latente spiega perché i liquidi con forti interazioni (acqua, metalli fusi) abbiano $\sigma$ elevata, e perché $\sigma$ si annulli al punto critico, dove il calore latente diventa nullo.

Allo stesso modo, la bagnabilità si interpreta come competizione tra **forze di coesione** (tra molecole del liquido) e **forze di adesione** (tra molecole del liquido e del solido). Se l'adesione prevale, il liquido tende a estendersi sul solido e bagna; se prevale la coesione, il liquido si raccoglie in gocce. Il vetro, ricco di gruppi ossidrili polari, attrae fortemente le molecole d'acqua, mentre gli atomi di mercurio sono legati tra loro dal legame metallico, molto più intenso dell'interazione con il vetro.

### Esercizio d'esempio

Un capillare di vetro di raggio interno $r = 0{,}25\ \mathrm{mm}$ è immerso verticalmente in acqua a 20 °C ($\sigma = 0{,}073\ \mathrm{N/m}$, $\rho = 1000\ \mathrm{kg/m^3}$, $\theta \approx 0°$). (a) Calcolare l'altezza di risalita. (b) Calcolare la differenza di pressione attraverso il menisco. (c) Calcolare la sovrapressione all'interno di una bolla di sapone di raggio $R = 2{,}0\ \mathrm{cm}$, con $\sigma_s = 0{,}025\ \mathrm{N/m}$.

**Soluzione.** (a) Dalla legge di Jurin,

$$
h = \frac{2\sigma\cos\theta}{\rho g r} = \frac{2\times0{,}073\times1}{1000\times9{,}81\times2{,}5\times10^{-4}} \approx 5{,}95\times10^{-2}\ \mathrm{m} \approx 6{,}0\ \mathrm{cm}.
$$

(b) Il menisco è una semisfera di raggio $r$; la pressione sotto di esso è inferiore a quella atmosferica di $\Delta p = 2\sigma/r = 2\times0{,}073/2{,}5\times10^{-4} = 584\ \mathrm{Pa}$. Verifica: $\rho g h = 1000\times9{,}81\times0{,}0595 \approx 584\ \mathrm{Pa}$. (c) La bolla ha due superfici: $\Delta p = 4\sigma_s/R = 4\times0{,}025/0{,}020 = 5{,}0\ \mathrm{Pa}$, una sovrapressione minuscola rispetto a quella atmosferica.

### Punti chiave

- La tensione superficiale $\sigma$ è la forza per unità di lunghezza tangente alla superficie, oppure il lavoro per unità di area necessario ad ampliarla; per l'acqua $\sigma \approx 0{,}073\ \mathrm{N/m}$.
- La legge di Laplace lega la curvatura alla sovrapressione: $\Delta p = \sigma(1/R_1 + 1/R_2)$; per una goccia $2\sigma/R$, per una bolla $4\sigma/R$.
- All'incontro di tre fasi l'equazione di Young $\sigma_{SG} = \sigma_{SL} + \sigma_{LG}\cos\theta$ definisce l'angolo di contatto e la bagnabilità.
- La legge di Jurin $h = 2\sigma\cos\theta/(\rho g r)$ descrive la risalita (o depressione) capillare.
- La lunghezza capillare $\ell_c = \sqrt{\sigma/(\rho g)}$ separa il regime dominato dalla tensione superficiale da quello dominato dalla gravità.
- Microscopicamente, la tensione superficiale nasce dall'asimmetria delle forze di coesione sulle molecole superficiali ed è correlata al calore latente di vaporizzazione.
- La bagnabilità è il risultato della competizione tra forze di adesione e di coesione.

## 11.5 Cinematica dei fluidi

La cinematica dei fluidi si occupa di descrivere il moto di un fluido senza indagarne le cause, così come la cinematica del punto descrive traiettorie, velocità e accelerazioni prima di introdurre le forze. La differenza essenziale rispetto alla meccanica del punto materiale o del corpo rigido è che un fluido è un sistema continuo con infiniti gradi di libertà, le cui parti si muovono in modo diverso l'una dall'altra e si deformano continuamente. Servono quindi strumenti nuovi. Esistono due punti di vista complementari: si possono seguire le singole particelle di fluido lungo il loro moto (descrizione **lagrangiana**), oppure si può osservare ciò che accade in ciascun punto fisso dello spazio (descrizione **euleriana**). La seconda è di gran lunga la più usata in fluidodinamica, ma la prima è indispensabile per applicare le leggi di Newton, che si riferiscono a porzioni di materia identificate. Il ponte tra le due è la **derivata materiale**. Una volta stabilito il linguaggio, si introduce la nozione di moto stazionario, che semplifica notevolmente la trattazione e sarà alla base delle leggi della dinamica dei fluidi ideali.

### 11.5.1 Descrizione lagrangiana

Nella **descrizione lagrangiana** si seguono le singole **particelle di fluido**, intese come porzioni di fluido piccole rispetto alle scale del moto ma ancora contenenti un gran numero di molecole, in accordo con l'ipotesi del continuo. Ciascuna particella viene identificata da un'etichetta, tipicamente la sua posizione $\vec r_0$ in un istante di riferimento $t_0$. Il moto del fluido è allora descritto dalla funzione

$$
\vec r = \vec r(\vec r_0, t),
$$

che fornisce, per ogni particella, la sua posizione all'istante $t$. Fissato $\vec r_0$, questa funzione descrive la **traiettoria** (o linea di percorso) della particella; la sua velocità e la sua accelerazione si ottengono derivando rispetto al tempo a etichetta fissata:

$$
\vec v(\vec r_0,t) = \frac{\partial \vec r}{\partial t}\bigg|_{\vec r_0}, \qquad \vec a(\vec r_0,t) = \frac{\partial^2 \vec r}{\partial t^2}\bigg|_{\vec r_0}.
$$

La descrizione lagrangiana è la diretta estensione della cinematica del punto materiale a un insieme infinito di punti, ed è quindi concettualmente la più naturale. È anche quella in cui le leggi fondamentali si scrivono con maggiore semplicità: la seconda legge di Newton si applica a una particella di fluido, cioè a una massa fissata, e la conservazione della massa si esprime affermando che la massa di ogni particella non cambia nel tempo. Tuttavia, nella pratica, essa è scomoda: richiede di tenere traccia della storia di ogni particella, mentre spesso interessa conoscere la velocità e la pressione in punti fissi, come all'ingresso di una turbina, sulla superficie di un'ala o in una sezione di tubazione. Inoltre, le particelle che in un certo istante sono vicine possono, in un moto complesso come quello turbolento, allontanarsi rapidamente, rendendo la descrizione estremamente intricata.

La descrizione lagrangiana trova comunque applicazione diretta in diversi ambiti. Sperimentalmente, la si realizza seguendo traccianti, come piccoli palloncini sonda lanciati nell'atmosfera, boe galleggianti alla deriva negli oceani o particelle fluorescenti in un esperimento di laboratorio (tecnica di **particle tracking velocimetry**). Nelle simulazioni numeriche, i metodi detti "a particelle" (come la smoothed particle hydrodynamics) seguono un gran numero di particelle fluide e sono particolarmente adatti a problemi con superfici libere molto deformate, come le onde che si infrangono o gli schizzi.

### 11.5.2 Descrizione euleriana

Nella **descrizione euleriana**, introdotta da Eulero nel XVIII secolo, si rinuncia a seguire le particelle e si osserva invece il fluido da punti fissi dello spazio. Le grandezze che descrivono il moto sono **campi**, funzioni della posizione $\vec r$ e del tempo $t$:

$$
\vec v = \vec v(\vec r, t), \qquad p = p(\vec r,t), \qquad \rho = \rho(\vec r,t).
$$

Il campo $\vec v(\vec r,t)$ fornisce la velocità della particella che, all'istante $t$, si trova a passare per il punto $\vec r$. È come se si disponesse di una rete di anemometri fissi in ogni punto dello spazio: istante per istante, ciascuno registra la velocità del fluido che lo investe, senza preoccuparsi di quale particella sia.

Lo strumento geometrico fondamentale della descrizione euleriana è la **linea di corrente**: una curva che, in un dato istante, è tangente in ogni suo punto al vettore velocità. In coordinate cartesiane le linee di corrente soddisfano $dx/v_x = dy/v_y = dz/v_z$. Due linee di corrente non possono intersecarsi (salvo in punti di ristagno dove $\vec v = 0$), perché in un punto la velocità ha una sola direzione. L'insieme delle linee di corrente passanti per una curva chiusa forma un **tubo di flusso**, attraverso la cui superficie laterale non passa fluido: il tubo di flusso si comporta come una condotta ideale, concetto che verrà sfruttato nel ricavare le leggi di continuità e di Bernoulli. Oltre alle linee di corrente e alle traiettorie, si definiscono le **linee di emissione**, luogo delle particelle che sono passate in tempi successivi per uno stesso punto: sono quelle che si visualizzano iniettando con continuità un colorante o del fumo da un ugello fisso.

Il punto delicato è il calcolo dell'accelerazione. Questa non coincide con la derivata parziale $\partial\vec v/\partial t$, che misura la variazione della velocità in un punto fisso; l'accelerazione di una particella deve tener conto anche del fatto che, muovendosi, la particella si sposta in regioni dove la velocità è diversa. Nell'intervallo $dt$ la particella passa da $\vec r$ a $\vec r + \vec v\,dt$, e la variazione della sua velocità è

$$
d\vec v = \frac{\partial \vec v}{\partial t}dt + \frac{\partial \vec v}{\partial x}v_x dt + \frac{\partial \vec v}{\partial y}v_y dt + \frac{\partial \vec v}{\partial z}v_z dt.
$$

Dividendo per $dt$ si ottiene la **derivata materiale** (o sostanziale, o lagrangiana):

$$
\vec a = \frac{D\vec v}{Dt} = \frac{\partial\vec v}{\partial t} + (\vec v\cdot\nabla)\vec v.
$$

Il primo termine è l'**accelerazione locale**, dovuta alla variazione temporale del campo in un punto; il secondo è l'**accelerazione convettiva**, dovuta allo spostamento della particella in un campo non uniforme. Lo stesso operatore $D/Dt = \partial/\partial t + \vec v\cdot\nabla$ si applica a qualunque grandezza: per esempio $D\rho/Dt$ è la variazione di densità percepita da un osservatore che si muove con il fluido. Si noti che l'accelerazione convettiva è non lineare nella velocità: è proprio questo termine il responsabile della grande complessità della fluidodinamica e, in ultima analisi, della turbolenza.

Un esempio chiarisce la differenza. In un ugello convergente alimentato a portata costante, il campo di velocità non cambia nel tempo, quindi $\partial\vec v/\partial t = 0$ in ogni punto; tuttavia ogni particella accelera passando dalla sezione larga a quella stretta, perché $(\vec v\cdot\nabla)\vec v\neq0$. Viceversa, in un tubo rettilineo di sezione costante in cui la portata viene aumentata, tutte le particelle accelerano insieme, e l'accelerazione è puramente locale.

Un'altra grandezza cinematica importante è la **vorticità** $\vec\omega = \nabla\times\vec v$, che misura la rotazione locale delle particelle fluide: in un moto rigido di rotazione con velocità angolare $\vec\Omega$ si ha $\vec\omega = 2\vec\Omega$. Un moto con $\vec\omega = 0$ ovunque si dice **irrotazionale**; in tal caso il campo di velocità si può esprimere come gradiente di un potenziale, $\vec v = \nabla\phi$. Il vortice libero che si forma nello scarico di un lavandino, in cui la velocità tangenziale decresce come $1/r$, è un esempio sorprendente di moto irrotazionale (tranne che sull'asse), pur essendo le traiettorie circolari: le particelle circolano senza ruotare su sé stesse.

### 11.5.3 Moto stazionario

Un moto si dice **stazionario** (o permanente) se, in ogni punto fisso dello spazio, le grandezze che lo descrivono non dipendono dal tempo:

$$
\frac{\partial \vec v}{\partial t} = 0, \qquad \frac{\partial p}{\partial t} = 0, \qquad \frac{\partial \rho}{\partial t} = 0.
$$

Stazionario non significa che il fluido sia fermo, né che le particelle non accelerino: significa soltanto che l'immagine istantanea del campo di moto è sempre la stessa. L'acqua che scorre in un fiume con portata costante, l'aria attorno a un'ala in volo a velocità costante (vista dal riferimento solidale con l'ala), l'olio in un circuito idraulico a regime sono esempi di moti stazionari, almeno in senso medio.

Nel moto stazionario si verifica una semplificazione notevole: **linee di corrente, traiettorie e linee di emissione coincidono**. Infatti, se il campo di velocità non cambia nel tempo, una particella che parte da un punto segue la linea di corrente che passa per esso, e tutte le particelle che passano successivamente per quello stesso punto seguono la stessa curva. Le linee di corrente diventano quindi visibili sperimentalmente con fumo o coloranti, come si fa nelle gallerie del vento e nelle vasche idrodinamiche. In un moto non stazionario, invece, le tre famiglie di linee sono in generale diverse e la loro interpretazione richiede cautela.

La stazionarietà dipende dal sistema di riferimento. Una barca che avanza a velocità costante in un lago genera, nel riferimento della riva, un campo di moto non stazionario (la scia si sposta); nel riferimento della barca, lo stesso campo appare stazionario. Per questo motivo, nello studio di corpi in moto uniforme in un fluido, si preferisce sempre mettersi nel riferimento del corpo, considerando il fluido che lo investe con velocità uniforme all'infinito: è il principio delle gallerie del vento, dove il modello è fermo e l'aria è messa in movimento.

Molti moti reali non sono stazionari in senso stretto ma lo sono **in media**: nel moto turbolento la velocità in un punto fluttua continuamente, ma la sua media su un intervallo di tempo sufficientemente lungo è costante. In questi casi si scompone la velocità in valore medio e fluttuazione, e si applicano le leggi del moto stazionario ai valori medi, con opportune correzioni. Analogamente, si parla di **moto quasi stazionario** quando le condizioni cambiano lentamente rispetto al tempo che il fluido impiega ad attraversare il sistema, come nello svuotamento di un serbatoio attraverso un piccolo foro: in ogni istante si può applicare il teorema di Bernoulli come se il moto fosse stazionario.

È utile infine classificare i moti secondo la geometria. Un moto si dice **unidimensionale** quando le grandezze dipendono da una sola coordinata spaziale, come in un'approssimazione di tubo di flusso o di condotta in cui si considerano valori medi sulla sezione; **bidimensionale** (o piano) quando dipendono da due coordinate, come nel flusso attorno a un'ala di apertura infinita; **tridimensionale** nel caso generale. Molti problemi di ingegneria idraulica si trattano nell'approssimazione unidimensionale stazionaria, che porta direttamente alle leggi della prossima sezione.

### Esercizio d'esempio

Il campo di velocità di un fluido nel piano è $\vec v = (k x,\ -k y)$, con $k = 2{,}0\ \mathrm{s^{-1}}$ (flusso attorno a un punto di ristagno). (a) Verificare che il moto è stazionario. (b) Determinare le linee di corrente. (c) Calcolare l'accelerazione di una particella che si trova nel punto $(x,y) = (0{,}50\ \mathrm{m},\ 1{,}0\ \mathrm{m})$. (d) Calcolare la vorticità.

**Soluzione.** (a) Le componenti non dipendono dal tempo, quindi $\partial\vec v/\partial t = 0$: il moto è stazionario. (b) Le linee di corrente soddisfano $dx/(kx) = dy/(-ky)$, cioè $dx/x = -dy/y$; integrando, $\ln x = -\ln y + \text{cost}$, da cui $xy = C$: sono iperboli equilatere con asintoti gli assi. Poiché il moto è stazionario, esse coincidono con le traiettorie. (c) L'accelerazione è puramente convettiva:

$$
a_x = v_x\frac{\partial v_x}{\partial x} + v_y\frac{\partial v_x}{\partial y} = (kx)(k) + 0 = k^2 x, \qquad a_y = v_x\frac{\partial v_y}{\partial x} + v_y\frac{\partial v_y}{\partial y} = 0 + (-ky)(-k) = k^2 y.
$$

Nel punto dato: $a_x = 4{,}0\times0{,}50 = 2{,}0\ \mathrm{m/s^2}$, $a_y = 4{,}0\times1{,}0 = 4{,}0\ \mathrm{m/s^2}$, con modulo $|\vec a| = \sqrt{2{,}0^2 + 4{,}0^2} \approx 4{,}5\ \mathrm{m/s^2}$. La particella accelera pur essendo il campo stazionario. (d) La vorticità ha solo componente $z$: $\omega_z = \partial v_y/\partial x - \partial v_x/\partial y = 0 - 0 = 0$. Il moto è irrotazionale, con potenziale $\phi = k(x^2 - y^2)/2$.

### Punti chiave

- La descrizione lagrangiana segue le singole particelle fluide: $\vec r = \vec r(\vec r_0,t)$; è naturale per scrivere le leggi di Newton ma scomoda in pratica.
- La descrizione euleriana usa campi definiti nei punti fissi dello spazio: $\vec v(\vec r,t)$, $p(\vec r,t)$, $\rho(\vec r,t)$.
- La derivata materiale $D/Dt = \partial/\partial t + \vec v\cdot\nabla$ collega i due punti di vista; l'accelerazione ha una parte locale e una convettiva.
- Le linee di corrente sono tangenti alla velocità in ogni istante; i tubi di flusso si comportano come condotte ideali.
- Un moto è stazionario se le grandezze non dipendono dal tempo in ogni punto fisso; in tal caso linee di corrente, traiettorie e linee di emissione coincidono.
- La stazionarietà dipende dal riferimento: conviene studiare un corpo in moto uniforme nel riferimento solidale con esso.
- La vorticità $\nabla\times\vec v$ misura la rotazione locale; se è nulla il moto è irrotazionale e ammette un potenziale di velocità.

## 11.6 Dinamica dei fluidi ideali

Un **fluido ideale** (o perfetto) è un modello in cui si trascurano la viscosità e la comprimibilità: il fluido è privo di attriti interni, quindi non dissipa energia meccanica, e ha densità costante. È un'idealizzazione, ma estremamente efficace: in molte situazioni pratiche, come il moto dell'acqua in condotte brevi e larghe, l'efflusso da serbatoi, il flusso d'aria lontano dalle pareti a velocità moderate, gli effetti viscosi sono confinati in strati sottili e il comportamento globale è ben descritto dal modello ideale. In questa sezione si ricavano le due leggi fondamentali: la conservazione della massa, che nella forma integrale per un tubo di flusso prende il nome di legge di Leonardo, e la conservazione dell'energia meccanica lungo una linea di corrente, che costituisce il principio di Bernoulli. Dalla loro combinazione discendono il teorema di Torricelli e i principali strumenti di misura della velocità e della portata dei fluidi.

### 11.6.1 Equazione di continuità

L'**equazione di continuità** è l'espressione matematica della conservazione della massa per un fluido in moto. Si consideri un volume di controllo $V$ fisso nello spazio, delimitato da una superficie chiusa $S$ con normale uscente $\hat n$. La massa contenuta in $V$ è $\int_V\rho\,dV$; essa può variare soltanto perché del fluido entra o esce attraverso $S$. La massa che attraversa un elemento di superficie $dS$ nell'unità di tempo è $\rho\vec v\cdot\hat n\,dS$, positiva se uscente. Il bilancio di massa si scrive quindi

$$
\frac{d}{dt}\int_V \rho\,dV = -\oint_S \rho\,\vec v\cdot\hat n\,dS.
$$

Il vettore $\vec J = \rho\vec v$ è la **densità di corrente di massa** (o flusso di massa per unità di area), misurata in $\mathrm{kg/(m^2\,s)}$. Applicando il teorema della divergenza e osservando che il volume è arbitrario, si ottiene la forma locale:

$$
\frac{\partial\rho}{\partial t} + \nabla\cdot(\rho\vec v) = 0.
$$

Questa equazione ha la stessa struttura delle leggi di conservazione della carica elettrica e dell'energia: la variazione locale di una grandezza è bilanciata dalla divergenza della sua corrente. Utilizzando la derivata materiale, si può riscriverla come $D\rho/Dt + \rho\,\nabla\cdot\vec v = 0$, che mette in evidenza il significato fisico della divergenza della velocità: essa rappresenta la rapidità relativa di dilatazione di una particella fluida.

Per un fluido **incomprimibile** $\rho$ è costante sia nel tempo sia nello spazio, e l'equazione si riduce a

$$
\nabla\cdot\vec v = 0.
$$

Il campo di velocità è **solenoidale**: il flusso della velocità attraverso qualunque superficie chiusa è nullo, cioè tanto fluido entra in una regione quanto ne esce. Questa condizione, puramente cinematica, è un vincolo molto forte sul campo di moto. Si può verificare, per esempio, che il campo $\vec v = (kx, -ky)$ dell'esercizio della sezione precedente soddisfa $\partial v_x/\partial x + \partial v_y/\partial y = k - k = 0$, e rappresenta quindi un possibile moto di un fluido incomprimibile.

### 11.6.2 Legge di Leonardo

Si applichi ora l'equazione di continuità a un tratto di tubo di flusso (o di condotta) in moto stazionario, compreso tra due sezioni trasversali $S_1$ e $S_2$. Poiché il moto è stazionario, la massa contenuta nel tratto non varia; poiché nessun fluido attraversa la superficie laterale del tubo, la massa che entra da $S_1$ nell'unità di tempo deve uguagliare quella che esce da $S_2$. Introducendo la **portata in massa** $Q_m = \int_S\rho\,\vec v\cdot\hat n\,dS$, misurata in $\mathrm{kg/s}$, e considerando velocità medie sulle sezioni, si ha

$$
\rho_1 v_1 S_1 = \rho_2 v_2 S_2.
$$

Per un fluido incomprimibile la densità si semplifica e si ottiene la **legge di Leonardo** (o legge di conservazione della portata):

$$
Q = v_1 S_1 = v_2 S_2 = \text{costante},
$$

dove $Q$ è la **portata volumetrica**, misurata in $\mathrm{m^3/s}$. Il nome ricorda Leonardo da Vinci, che nei suoi studi sul moto delle acque osservò che in un fiume la velocità è maggiore dove l'alveo è più stretto e minore dove si allarga. La legge esprime che la velocità media è inversamente proporzionale all'area della sezione. Da essa si deduce che, in un fluido incomprimibile in moto stazionario, le linee di corrente si addensano dove la velocità è maggiore: la densità delle linee di corrente è una misura visiva dell'intensità del flusso.

Le applicazioni sono immediate. Restringendo con un dito la sezione di uscita di un tubo da giardino si ottiene un getto più veloce, che arriva più lontano. Gli ugelli degli idranti, delle turbine Pelton e degli spruzzatori sfruttano lo stesso principio. Il getto d'acqua che esce da un rubinetto si assottiglia scendendo, perché accelerando per effetto della gravità deve ridurre la propria sezione per mantenere costante la portata. Nel sistema circolatorio, la velocità del sangue diminuisce dall'aorta (circa $0{,}3\ \mathrm{m/s}$) ai capillari (meno di $1\ \mathrm{mm/s}$) perché, pur essendo ciascun capillare minuscolo, la loro sezione complessiva è circa mille volte quella dell'aorta. Se una condotta si ramifica, la legge si generalizza imponendo che la somma delle portate entranti in un nodo sia uguale alla somma delle uscenti, in perfetta analogia con la legge di Kirchhoff per le correnti nei circuiti elettrici.

### 11.6.3 Principio di Bernoulli

Il **principio di Bernoulli** (Daniel Bernoulli, *Hydrodynamica*, 1738) è la conservazione dell'energia meccanica per un fluido ideale. Si consideri un tratto di tubo di flusso in moto stazionario, tra la sezione 1 (area $S_1$, quota $z_1$, pressione $p_1$, velocità $v_1$) e la sezione 2. In un intervallo $dt$ la porzione di fluido compresa tra le due sezioni avanza: la sezione 1 si sposta di $v_1 dt$, la sezione 2 di $v_2 dt$. Per la continuità il volume spostato è lo stesso, $dV = S_1 v_1 dt = S_2 v_2 dt$, e corrisponde alla massa $dm = \rho\,dV$. Il risultato netto è come se la massa $dm$ fosse stata trasferita dalla sezione 1 alla sezione 2, poiché la parte intermedia, in regime stazionario, è invariata.

Il lavoro delle forze di pressione esterne è $dW_p = p_1 S_1 v_1 dt - p_2 S_2 v_2 dt = (p_1 - p_2)dV$. Esso, in assenza di attriti, deve uguagliare la variazione di energia cinetica e potenziale gravitazionale della massa trasferita:

$$
(p_1 - p_2)\,dV = \tfrac12 dm\,(v_2^2 - v_1^2) + dm\,g\,(z_2 - z_1).
$$

Dividendo per $dV$ e riordinando, si ottiene il **teorema di Bernoulli**:

$$
p + \tfrac12\rho v^2 + \rho g z = \text{costante lungo una linea di corrente}.
$$

I tre termini hanno le dimensioni di una pressione, cioè di un'energia per unità di volume. Il termine $p$ è la **pressione statica**, $\frac12\rho v^2$ la **pressione dinamica**, $\rho g z$ la **pressione idrostatica** (o di gravità); la loro somma si chiama **pressione totale**. Dividendo per $\rho g$ si ottiene la forma in **altezze** o **carichi** usata dagli idraulici: $z + p/(\rho g) + v^2/(2g) = H$, dove $H$ è il **carico totale**, somma di altezza geometrica, piezometrica e cinetica. Se la velocità è nulla, il teorema si riduce alla legge di Stevin, che ne è un caso particolare.

Le ipotesi di validità vanno tenute ben presenti: fluido incomprimibile, non viscoso, moto stazionario, forze di volume conservative; il teorema vale lungo una stessa linea di corrente. Se il moto è anche irrotazionale, la costante è la stessa per tutto il campo di moto. In un fluido reale le perdite viscose fanno diminuire il carico totale lungo il moto, e si aggiunge un termine di **perdita di carico**.

Il principio di Bernoulli spiega numerosi fenomeni e funziona da base per strumenti di misura. Dove la velocità aumenta, la pressione diminuisce. Il **tubo di Venturi** è una condotta con una strozzatura: misurando la differenza di pressione tra la sezione larga e quella stretta con un manometro differenziale, e combinando Bernoulli con la continuità, si ricava la portata: $Q = S_1S_2\sqrt{2\Delta p/[\rho(S_1^2 - S_2^2)]}$. Il **tubo di Pitot** misura la velocità di un fluido confrontando la pressione totale in un punto di ristagno (dove $v = 0$) con la pressione statica: $v = \sqrt{2(p_{tot} - p)/\rho}$; è lo strumento che fornisce la velocità rispetto all'aria sugli aerei. Allo stesso principio si devono l'aspirazione nei carburatori e negli spruzzatori (effetto Venturi), la tendenza di due navi affiancate ad avvicinarsi, il sollevamento dei tetti durante le tempeste, la tenda della doccia che si gonfia verso l'interno.

### 11.6.4 Principio di Torricelli

Si consideri un serbatoio aperto, contenente un liquido fino a un'altezza $h$ sopra un piccolo foro praticato sulla parete laterale o sul fondo. Si vuole determinare la velocità di efflusso. Si applica il teorema di Bernoulli lungo una linea di corrente che va dalla superficie libera (punto 1) al getto appena uscito dal foro (punto 2). In entrambi i punti la pressione è quella atmosferica, $p_1 = p_2 = p_0$. Se la sezione del serbatoio è molto più grande di quella del foro, per la continuità la velocità di discesa della superficie libera è trascurabile, $v_1 \approx 0$. Ponendo $z_1 - z_2 = h$, si ottiene il **teorema di Torricelli**:

$$
v = \sqrt{2gh}.
$$

Il liquido esce con la stessa velocità che avrebbe un corpo in caduta libera dalla quota della superficie libera. Il risultato, ricavato da Torricelli nel 1643 sulla base di considerazioni sperimentali ben prima di Bernoulli, ha un'interpretazione energetica semplice: l'energia potenziale persa dal liquido che scende nel serbatoio si trasforma in energia cinetica del getto, senza perdite. Se il serbatoio è chiuso e pressurizzato con una sovrapressione $\Delta p$ sulla superficie, la velocità diventa $v = \sqrt{2gh + 2\Delta p/\rho}$.

Nella realtà la portata effettiva è inferiore a quella teorica $S_{foro}\sqrt{2gh}$ per due motivi. Il primo è l'attrito viscoso, che riduce la velocità di qualche percento (coefficiente di velocità $c_v \approx 0{,}97$-$0{,}99$). Il secondo, più rilevante, è la **vena contratta**: le linee di corrente convergono verso il foro anche dopo averlo superato, e il getto raggiunge la sezione minima a una piccola distanza dall'uscita, con area pari a circa il 60-65% di quella del foro per un foro a spigolo vivo. Il prodotto dei due coefficienti è il **coefficiente di efflusso** $c_d \approx 0{,}6$, e la portata reale è $Q = c_d S\sqrt{2gh}$.

Dal teorema di Torricelli si ricava anche il **tempo di svuotamento** di un serbatoio, nell'ipotesi di moto quasi stazionario. Se il serbatoio ha sezione costante $A$ e il foro sezione $a$, la continuità impone $-A\,dh/dt = a\sqrt{2gh}$. Separando le variabili e integrando da $h_0$ a $0$:

$$
t_s = \frac{A}{a}\sqrt{\frac{2h_0}{g}}.
$$

Il livello scende inizialmente in fretta e poi sempre più lentamente, perché la velocità di efflusso diminuisce con la radice dell'altezza. Questa proprietà era sfruttata nelle **clessidre ad acqua** (clepsidre), la cui forma veniva sagomata in modo che il livello scendesse uniformemente nel tempo. Infine, se il foro è laterale a quota $y$ dal suolo, il getto descrive una parabola e raggiunge il terreno a distanza $x = 2\sqrt{h\,y}$ dalla parete; la gittata massima si ottiene con il foro a metà dell'altezza totale del liquido.

### Esercizio d'esempio

Un tubo orizzontale trasporta acqua ($\rho = 1000\ \mathrm{kg/m^3}$) con portata $Q = 6{,}0\times10^{-3}\ \mathrm{m^3/s}$. La sezione passa da un diametro $D_1 = 8{,}0\ \mathrm{cm}$ a un diametro $D_2 = 4{,}0\ \mathrm{cm}$ (tubo di Venturi). La pressione nella sezione larga è $p_1 = 1{,}50\times10^5\ \mathrm{Pa}$. Calcolare (a) le velocità nelle due sezioni, (b) la pressione nella strozzatura, (c) il dislivello che si leggerebbe in un manometro differenziale a mercurio ($\rho_{Hg} = 13\,600\ \mathrm{kg/m^3}$).

**Soluzione.** (a) Le aree valgono $S_1 = \pi D_1^2/4 = 5{,}03\times10^{-3}\ \mathrm{m^2}$ e $S_2 = 1{,}26\times10^{-3}\ \mathrm{m^2}$. Per la legge di Leonardo,

$$
v_1 = \frac{Q}{S_1} = \frac{6{,}0\times10^{-3}}{5{,}03\times10^{-3}} \approx 1{,}19\ \mathrm{m/s}, \qquad v_2 = \frac{Q}{S_2} \approx 4{,}77\ \mathrm{m/s}.
$$

(b) Per il teorema di Bernoulli, con $z_1 = z_2$:

$$
p_2 = p_1 - \tfrac12\rho(v_2^2 - v_1^2) = 1{,}50\times10^5 - 500\times(22{,}8 - 1{,}42) \approx 1{,}50\times10^5 - 1{,}07\times10^4 \approx 1{,}39\times10^5\ \mathrm{Pa}.
$$

(c) Nel manometro differenziale, sopra il mercurio c'è acqua, quindi $\Delta p = (\rho_{Hg} - \rho)g\Delta h$, da cui $\Delta h = 1{,}07\times10^4/(12\,600\times9{,}81) \approx 8{,}6\times10^{-2}\ \mathrm{m}$, cioè circa 8,6 cm.

### Punti chiave

- Un fluido ideale è incomprimibile e non viscoso: non dissipa energia meccanica.
- L'equazione di continuità $\partial\rho/\partial t + \nabla\cdot(\rho\vec v) = 0$ esprime la conservazione della massa; per fluidi incomprimibili $\nabla\cdot\vec v = 0$.
- La legge di Leonardo $Q = vS = \text{cost}$ afferma che in una condotta la velocità media è inversamente proporzionale alla sezione.
- Il teorema di Bernoulli $p + \frac12\rho v^2 + \rho g z = \text{cost}$ vale lungo una linea di corrente per moto stazionario di un fluido ideale; dove la velocità aumenta la pressione diminuisce.
- Tubo di Venturi e tubo di Pitot sfruttano Bernoulli per misurare portata e velocità.
- Il teorema di Torricelli $v = \sqrt{2gh}$ fornisce la velocità di efflusso da un serbatoio; la portata reale è ridotta dal coefficiente di efflusso $c_d\approx0{,}6$.
- Il tempo di svuotamento di un serbatoio cilindrico è $t_s = (A/a)\sqrt{2h_0/g}$.

## 11.7 Dinamica dei fluidi viscosi

Il modello di fluido ideale, pur potente, fallisce in modo clamoroso in alcune previsioni. La più famosa è il **paradosso di d'Alembert** (1752): un corpo di qualunque forma che si muove a velocità costante in un fluido ideale illimitato non subisce alcuna resistenza al moto. L'esperienza quotidiana di chi pedala controvento lo smentisce. Analogamente, il modello ideale non sa spiegare perché per mantenere l'acqua in moto in una lunga condotta orizzontale serva una differenza di pressione tra gli estremi. La chiave è la viscosità: anche se piccola, essa impone la condizione di aderenza alle pareti, genera strati limite, dissipa energia e, in certe condizioni, rende il moto instabile e turbolento. In questa sezione si studiano i due regimi di moto, laminare e turbolento, il criterio che li distingue (numero di Reynolds), le forze di resistenza su un corpo immerso, e le forze trasversali al moto, cioè la portanza aerodinamica e l'effetto Magnus.

### 11.7.1 Moto laminare

Si dice **laminare** un moto in cui il fluido si muove per strati (lamine) che scorrono ordinatamente l'uno sull'altro, senza mescolarsi su scala macroscopica. Le linee di corrente sono regolari e il moto, se le condizioni al contorno sono stazionarie, è stazionario. Il moto laminare si osserva a basse velocità, in condotte di piccolo diametro e con fluidi molto viscosi: il miele che cola da un cucchiaio, l'olio in un cuscinetto, il sangue nei capillari.

Il caso più importante è il **moto di Poiseuille** in un tubo cilindrico rettilineo di raggio $R$ e lunghezza $L$, ai cui estremi è applicata una differenza di pressione $\Delta p$. Si consideri un cilindro coassiale di fluido di raggio $r$. In moto stazionario e uniforme lungo l'asse, la forza netta di pressione sulle basi, $\Delta p\,\pi r^2$, deve bilanciare la forza viscosa sulla superficie laterale, $\tau\,2\pi r L$, con $\tau = -\eta\,dv/dr$. Quindi

$$
\frac{dv}{dr} = -\frac{\Delta p}{2\eta L}r \quad\Longrightarrow\quad v(r) = \frac{\Delta p}{4\eta L}\left(R^2 - r^2\right),
$$

dove la costante di integrazione è stata fissata con la condizione di aderenza $v(R) = 0$. Il profilo di velocità è **parabolico**, con velocità massima sull'asse, $v_{max} = \Delta p R^2/(4\eta L)$, e velocità media pari a metà della massima. Integrando sulla sezione si ottiene la portata, data dalla **legge di Hagen-Poiseuille**:

$$
Q = \int_0^R v(r)\,2\pi r\,dr = \frac{\pi R^4}{8\eta L}\,\Delta p.
$$

La portata è proporzionale alla differenza di pressione, in analogia con la legge di Ohm: si definisce la **resistenza idraulica** $R_{id} = 8\eta L/(\pi R^4)$, tale che $\Delta p = R_{id}Q$. La dipendenza dalla quarta potenza del raggio è drammatica: dimezzando il raggio di un vaso sanguigno, a parità di differenza di pressione, la portata si riduce di sedici volte. È per questo che anche modeste ostruzioni arteriose hanno conseguenze cliniche serie e che l'organismo regola il flusso sanguigno variando di poco il diametro delle arteriole. La legge di Poiseuille fornisce anche il principio dei **viscosimetri capillari**, nei quali si misura il tempo di efflusso di un volume noto di liquido attraverso un capillare calibrato.

La potenza dissipata per attrito viscoso è $P = \Delta p\,Q$; essa rappresenta il lavoro che la pompa deve fornire per mantenere il moto e si trasforma interamente in calore. Nel linguaggio di Bernoulli, si ha una **perdita di carico** distribuita lungo la condotta, proporzionale alla velocità nel regime laminare.

### 11.7.2 Moto turbolento

Aumentando la velocità, il moto laminare diventa instabile e si trasforma in **moto turbolento**: il fluido si muove in modo irregolare, con vortici di tutte le dimensioni che nascono, interagiscono e si dissolvono; la velocità in ogni punto fluttua in modo apparentemente casuale attorno a un valor medio. La turbolenza produce un intenso mescolamento trasversale di quantità di moto, calore e sostanze disciolte, molto più efficace della diffusione molecolare. Il fumo di una sigaretta, che sale prima in un filo regolare e poi si sfrangia in volute caotiche, mostra la transizione a occhio nudo.

Osborne Reynolds (1883) studiò sistematicamente la transizione iniettando un filetto di colorante nell'acqua che scorreva in un tubo di vetro. Scoprì che il passaggio dipende non dalle singole grandezze ma da una loro combinazione adimensionale, il **numero di Reynolds**:

$$
Re = \frac{\rho v D}{\eta} = \frac{vD}{\nu},
$$

dove $v$ è la velocità media, $D$ una lunghezza caratteristica (il diametro del tubo) e $\nu$ la viscosità cinematica. Il numero di Reynolds rappresenta il rapporto tra le forze d'inerzia, dell'ordine di $\rho v^2/D$ per unità di volume, e le forze viscose, dell'ordine di $\eta v/D^2$. Per tubi cilindrici il moto è laminare per $Re \lesssim 2000$, turbolento per $Re \gtrsim 4000$, e nell'intervallo intermedio si ha un regime di transizione in cui laminare e turbolento si alternano. Il valore critico dipende dalla cura con cui si evitano disturbi all'ingresso: in condizioni di laboratorio molto controllate si è mantenuto il moto laminare fino a $Re \sim 10^5$.

Il numero di Reynolds è anche il cardine della **similitudine dinamica**: due moti geometricamente simili con lo stesso $Re$ sono dinamicamente simili, cioè hanno campi di velocità adimensionali identici. Ciò consente di provare in galleria del vento modelli in scala di aerei, automobili e edifici, purché si riproduca il numero di Reynolds (o ci si avvicini sufficientemente).

In regime turbolento il profilo di velocità medio in un tubo è molto più piatto di quello parabolico, con forti gradienti concentrati vicino alla parete in un sottile **sottostrato viscoso**. La perdita di carico non è più proporzionale alla velocità ma circa al suo quadrato, e si esprime con la **formula di Darcy-Weisbach**:

$$
\Delta p = f\,\frac{L}{D}\,\frac{\rho v^2}{2},
$$

dove $f$ è il **fattore d'attrito**, che dipende da $Re$ e dalla rugosità relativa della parete; i suoi valori si leggono sul **diagramma di Moody**. In regime laminare $f = 64/Re$, e la formula si riduce a quella di Poiseuille. Quasi tutti i moti di interesse ingegneristico (acqua negli acquedotti, aria attorno ai veicoli, gas nei condotti) sono turbolenti: un tubo da 5 cm in cui l'acqua scorre a $1\ \mathrm{m/s}$ ha $Re \approx 5\times10^4$.

### 11.7.3 Attrito viscoso

Un corpo che si muove in un fluido, o equivalentemente un fluido che investe un corpo fermo, subisce una forza di **resistenza** (in inglese *drag*) diretta come la velocità relativa del fluido. La resistenza ha due origini: l'**attrito di superficie**, dovuto agli sforzi tangenziali viscosi sulla superficie del corpo, e la **resistenza di forma** (o di pressione), dovuta alla differenza tra la pressione sulla parte anteriore e quella sulla parte posteriore, dove il flusso si stacca dal corpo formando una scia vorticosa a bassa pressione.

A bassi numeri di Reynolds ($Re \lesssim 1$, calcolato con il diametro del corpo), dominano gli effetti viscosi e la resistenza è proporzionale alla velocità. Per una sfera di raggio $r$ vale la **legge di Stokes**:

$$
\vec F = -6\pi\eta r\,\vec v.
$$

È la forza di attrito viscoso lineare già incontrata nella dinamica del punto. Una sfera di massa volumica $\rho_s$ che cade in un fluido di densità $\rho_f$ raggiunge una **velocità limite** quando peso, spinta di Archimede e resistenza si bilanciano: $\frac43\pi r^3(\rho_s - \rho_f)g = 6\pi\eta r v_\infty$, cioè

$$
v_\infty = \frac{2 r^2(\rho_s - \rho_f)g}{9\eta}.
$$

Su questa relazione si basa il **viscosimetro a caduta di sfera**; essa governa inoltre la sedimentazione di particelle fini, la caduta delle goccioline delle nebbie e fu usata da Millikan nell'esperimento della goccia d'olio per la misura della carica elementare.

Ad alti numeri di Reynolds ($10^3 \lesssim Re \lesssim 10^5$) prevale la resistenza di forma, e la forza è proporzionale al quadrato della velocità. Si scrive

$$
F = \tfrac12 C_D\,\rho\,A\,v^2,
$$

dove $A$ è l'area frontale e $C_D$ il **coefficiente di resistenza**, adimensionale, che dipende dalla forma del corpo e da $Re$. Per una sfera $C_D \approx 0{,}47$, per un disco piatto perpendicolare al flusso $C_D\approx1{,}2$, per un'automobile moderna $C_D\approx0{,}25$-$0{,}35$, per un profilo affusolato a goccia $C_D\approx0{,}04$. La **carenatura** dei veicoli mira a ritardare il distacco della corrente e a ridurre la scia. Poiché la potenza necessaria a vincere la resistenza è $P = Fv \propto v^3$, raddoppiare la velocità di un'automobile richiede otto volte la potenza: questo spiega il forte aumento dei consumi in autostrada. Attorno a $Re\approx3\times10^5$ la sfera mostra la **crisi della resistenza**: lo strato limite diventa turbolento, aderisce più a lungo alla superficie, la scia si restringe e $C_D$ crolla a circa $0{,}1$. Le fossette delle palline da golf servono proprio ad anticipare questa transizione e a ridurre la resistenza.

### 11.7.4 Portanza

La **portanza** (in inglese *lift*) è la componente della forza aerodinamica perpendicolare alla velocità relativa del fluido. È la forza che sostiene gli aerei, che fa girare le turbine eoliche e le eliche, che spinge le barche a vela di bolina. Analogamente alla resistenza si scrive

$$
L = \tfrac12 C_L\,\rho\,S\,v^2,
$$

dove $S$ è la superficie alare (in pianta) e $C_L$ il **coefficiente di portanza**, che dipende dalla forma del profilo e dall'**angolo d'attacco** $\alpha$, cioè l'angolo tra la corda del profilo e la direzione della corrente. Per piccoli angoli $C_L$ cresce linearmente con $\alpha$ (per un profilo sottile, $C_L \approx 2\pi\alpha$ con $\alpha$ in radianti); oltre un angolo critico di circa 15° la corrente si stacca dal dorso dell'ala e la portanza crolla bruscamente: è lo **stallo**.

Dal punto di vista fisico, la portanza si può spiegare in modi equivalenti. Secondo il **principio di Bernoulli**, la forma del profilo e l'angolo d'attacco fanno sì che l'aria scorra più velocemente sul dorso che sul ventre; di conseguenza la pressione sul dorso è minore e ne risulta una forza netta verso l'alto. Va evitata la spiegazione scorretta, ma diffusa, secondo cui le particelle che si separano al bordo d'attacco dovrebbero "ricongiungersi" al bordo d'uscita: in realtà l'aria sul dorso arriva prima. Secondo la **terza legge di Newton**, l'ala devia verso il basso una grande massa d'aria (*downwash*): per farlo deve esercitare una forza sull'aria verso il basso, e l'aria reagisce con una forza uguale e opposta verso l'alto. Le due descrizioni non sono in contraddizione: la distribuzione di pressione è proprio il meccanismo con cui l'ala trasferisce quantità di moto all'aria.

Il formalismo più completo è quello della **circolazione**. Si definisce la circolazione $\Gamma = \oint\vec v\cdot d\vec\ell$ lungo una curva chiusa che circonda il profilo. Il **teorema di Kutta-Žukovskij** afferma che, per un profilo di apertura unitaria in un fluido ideale, la portanza per unità di apertura è

$$
L' = \rho\,v\,\Gamma.
$$

La circolazione attorno all'ala si instaura grazie alla viscosità, che impone al flusso di lasciare in modo regolare il bordo d'uscita aguzzo (condizione di Kutta). Per un aereo in volo livellato la portanza uguaglia il peso; poiché $L\propto v^2$, al decollo, quando la velocità è bassa, si aumenta $C_L$ estendendo ipersostentatori (flap e slat) e aumentando l'angolo d'attacco.

### 11.7.5 Effetto Magnus

L'**effetto Magnus**, studiato da Heinrich Gustav Magnus nel 1852, è la forza trasversale che agisce su un corpo rotante, tipicamente una sfera o un cilindro, che si muove in un fluido. Un cilindro che ruota con velocità angolare $\omega$ trascina per viscosità il fluido a contatto con la sua superficie. Nel riferimento del cilindro, sul lato in cui la superficie si muove nello stesso verso della corrente la velocità del fluido risulta aumentata, sul lato opposto diminuita. Per il principio di Bernoulli, la pressione è minore dal lato a velocità maggiore, e ne risulta una forza perpendicolare sia alla velocità sia all'asse di rotazione:

$$
\vec F_M \propto \vec\omega\times\vec v.
$$

Il fenomeno è un esempio concreto del teorema di Kutta-Žukovskij: la rotazione del corpo produce una circolazione $\Gamma$ attorno a esso, e quindi una portanza per unità di lunghezza $L' = \rho v\Gamma$. Per un cilindro di raggio $R$ che trascina il fluido con velocità periferica $\omega R$, la circolazione è dell'ordine di $\Gamma \approx 2\pi R^2\omega$, e la forza per unità di lunghezza vale circa $2\pi\rho R^2\omega v$.

L'effetto Magnus è ben noto in ambito sportivo: è responsabile delle traiettorie a "effetto" dei palloni da calcio nei tiri di punizione, dei colpi tagliati e liftati nel tennis e nel ping-pong, delle palle curve nel baseball, del volo prolungato delle palline da golf colpite con rotazione all'indietro (*backspin*), che ricevono una portanza verso l'alto. In ingegneria esso è stato sfruttato nei **rotori Flettner**, grandi cilindri verticali rotanti installati su navi per fornire una spinta propulsiva grazie al vento: dopo i prototipi degli anni Venti del Novecento, la tecnologia è tornata d'attualità per ridurre i consumi del trasporto marittimo. Negli effetti balistici, la rotazione dei proiettili produce piccole deviazioni laterali che vanno corrette nel tiro a lunga distanza.

### Esercizio d'esempio

Dell'olio ($\eta = 0{,}10\ \mathrm{Pa\cdot s}$, $\rho = 900\ \mathrm{kg/m^3}$) scorre in un tubo orizzontale di raggio $R = 5{,}0\ \mathrm{mm}$ e lunghezza $L = 2{,}0\ \mathrm{m}$, con portata $Q = 2{,}0\times10^{-5}\ \mathrm{m^3/s}$. (a) Verificare che il moto è laminare. (b) Calcolare la differenza di pressione necessaria. (c) Calcolare la potenza dissipata. (d) Calcolare la velocità limite di una sfera d'acciaio ($\rho_s = 7800\ \mathrm{kg/m^3}$) di raggio $r = 1{,}0\ \mathrm{mm}$ che cade nello stesso olio.

**Soluzione.** (a) La velocità media è $\bar v = Q/(\pi R^2) = 2{,}0\times10^{-5}/(7{,}85\times10^{-5}) \approx 0{,}255\ \mathrm{m/s}$. Il numero di Reynolds vale $Re = \rho\bar v D/\eta = 900\times0{,}255\times0{,}010/0{,}10 \approx 23$, ben al di sotto di 2000: il moto è laminare. (b) Dalla legge di Hagen-Poiseuille,

$$
\Delta p = \frac{8\eta L Q}{\pi R^4} = \frac{8\times0{,}10\times2{,}0\times2{,}0\times10^{-5}}{\pi\times(5{,}0\times10^{-3})^4} = \frac{3{,}2\times10^{-5}}{1{,}96\times10^{-9}} \approx 1{,}6\times10^4\ \mathrm{Pa}.
$$

(c) $P = \Delta p\,Q \approx 1{,}63\times10^4\times2{,}0\times10^{-5} \approx 0{,}33\ \mathrm{W}$. (d) Dalla legge di Stokes,

$$
v_\infty = \frac{2r^2(\rho_s - \rho_f)g}{9\eta} = \frac{2\times(1{,}0\times10^{-3})^2\times6900\times9{,}81}{9\times0{,}10} \approx 0{,}15\ \mathrm{m/s}.
$$

Verifica a posteriori: $Re = \rho_f v_\infty (2r)/\eta = 900\times0{,}15\times2{,}0\times10^{-3}/0{,}10 \approx 2{,}7$, dell'ordine dell'unità: la legge di Stokes è ancora accettabile come stima, con un errore di qualche decina di percento.

### Punti chiave

- La viscosità risolve il paradosso di d'Alembert: introduce aderenza alle pareti, strati limite e dissipazione.
- Nel moto laminare in un tubo il profilo è parabolico e la portata segue la legge di Hagen-Poiseuille $Q = \pi R^4\Delta p/(8\eta L)$.
- Il numero di Reynolds $Re = \rho v D/\eta$ confronta forze d'inerzia e viscose; nei tubi il moto è laminare per $Re \lesssim 2000$ e turbolento per $Re \gtrsim 4000$.
- In regime turbolento le perdite di carico crescono circa con $v^2$ (formula di Darcy-Weisbach).
- A bassi $Re$ la resistenza su una sfera è lineare (Stokes, $6\pi\eta r v$); ad alti $Re$ è quadratica, $F = \frac12 C_D\rho A v^2$.
- La portanza $L = \frac12 C_L\rho S v^2$ è perpendicolare alla velocità ed è legata alla circolazione dal teorema di Kutta-Žukovskij $L' = \rho v\Gamma$.
- L'effetto Magnus produce una forza trasversale su corpi rotanti, proporzionale a $\vec\omega\times\vec v$.

