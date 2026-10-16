# Capitolo 7 — Relazioni integrali

Le leggi della dinamica del punto materiale, nella forma $\vec{F} = m\vec{a}$ oppure $\vec{F} = \mathrm{d}\vec{p}/\mathrm{d}t$, sono **relazioni differenziali**: legano la forza agente in un certo istante alla variazione istantanea dello stato di moto. Per conoscere il moto occorre integrarle, operazione che in molti casi pratici è difficile o addirittura impossibile in forma chiusa, perché la forza può dipendere in modo complicato dalla posizione, dalla velocità e dal tempo. In questo capitolo si integrano le equazioni della dinamica *una volta*, rispetto al tempo oppure rispetto allo spazio, ottenendo delle **relazioni integrali**: il teorema dell'impulso, il teorema dell'impulso angolare, il teorema dell'energia cinetica (o delle forze vive). Queste relazioni non contengono più informazioni delle leggi di Newton, ma le riorganizzano in modo da mettere in evidenza grandezze — impulso, lavoro, energia — che spesso permettono di risolvere un problema confrontando soltanto lo stato iniziale e quello finale, senza dover seguire istante per istante l'evoluzione del sistema. Da qui nascono i **teoremi di conservazione**, che costituiscono uno degli strumenti più potenti e generali dell'intera fisica.

## 7.1 Impulso

L'idea di fondo di questa sezione è semplice: se la seconda legge della dinamica dice che la forza è la derivata temporale della quantità di moto, allora integrando la forza nel tempo si ottiene la variazione della quantità di moto. Analogamente, poiché il momento della forza è la derivata temporale del momento angolare, integrando il momento nel tempo si ottiene la variazione del momento angolare. Le due grandezze integrali che compaiono in questi teoremi si chiamano rispettivamente **impulso** e **impulso angolare**. Il loro interesse pratico è enorme quando le forze agiscono per intervalli di tempo molto brevi e con andamento temporale complicato o sconosciuto, come accade negli urti, nei colpi, nei rimbalzi, nelle esplosioni: in questi casi non serve conoscere la forza istante per istante, ma basta conoscerne l'effetto complessivo.

### 7.1.1 Impulso

Si consideri un punto materiale di massa $m$ soggetto a una forza risultante $\vec{F}(t)$. La seconda legge della dinamica, nella sua forma più generale valida anche quando la massa non è costante, si scrive

$$
\vec{F} = \frac{\mathrm{d}\vec{p}}{\mathrm{d}t}, \qquad \vec{p} = m\vec{v}.
$$

Moltiplicando entrambi i membri per $\mathrm{d}t$ e integrando tra un istante iniziale $t_i$ e un istante finale $t_f$ si ottiene

$$
\vec{J} \equiv \int_{t_i}^{t_f} \vec{F}(t)\,\mathrm{d}t = \vec{p}_f - \vec{p}_i = \Delta\vec{p}.
$$

La grandezza vettoriale $\vec{J}$ si chiama **impulso** della forza nell'intervallo considerato e la relazione appena scritta è il **teorema dell'impulso**: l'impulso della forza risultante agente su un punto materiale è uguale alla variazione della sua quantità di moto. L'impulso ha le dimensioni di una forza per un tempo, quindi si misura in $\mathrm{N\,s}$, unità che coincide con il $\mathrm{kg\,m/s}$ della quantità di moto, come deve essere per coerenza dimensionale.

È importante sottolineare alcuni aspetti. Il primo è che l'impulso è una grandezza **vettoriale**: l'integrale va inteso componente per componente, e il teorema vale separatamente per ciascuna delle tre componenti cartesiane. Se, ad esempio, una forza agisce solo in direzione verticale, la componente orizzontale della quantità di moto resta invariata, qualunque sia l'andamento della forza. Il secondo aspetto è che il teorema riguarda la forza **risultante**: se sul punto agiscono più forze, l'impulso totale è la somma vettoriale degli impulsi delle singole forze, e solo la somma è legata alla variazione di $\vec{p}$. Il terzo è che il teorema non richiede alcuna ipotesi sulla natura della forza: può essere conservativa o dissipativa, costante o variabile, dipendente dalla posizione o dalla velocità.

Nel caso particolare di forza costante l'impulso si riduce al prodotto $\vec{J} = \vec{F}\,\Delta t$. Quando la forza varia nel tempo è utile introdurre la **forza media** nell'intervallo $\Delta t = t_f - t_i$, definita come quella forza costante che produrrebbe lo stesso impulso:

$$
\langle\vec{F}\rangle = \frac{1}{\Delta t}\int_{t_i}^{t_f}\vec{F}(t)\,\mathrm{d}t = \frac{\Delta\vec{p}}{\Delta t}.
$$

Graficamente, per una forza unidimensionale, l'impulso è l'area sottesa dalla curva $F(t)$ nel piano forza-tempo, e la forza media è l'altezza del rettangolo di base $\Delta t$ con la stessa area. Questa interpretazione chiarisce subito un fatto ben noto dall'esperienza quotidiana: a parità di variazione di quantità di moto, una durata d'interazione più lunga comporta una forza media più piccola. È il principio su cui si basano gli airbag, i caschi, i materassi per il salto in alto, le zone di deformazione programmata delle automobili, ma anche il gesto istintivo di piegare le ginocchia quando si atterra da un salto: allungare il tempo di arresto riduce la forza scambiata e quindi il danno.

Le **forze impulsive** sono forze molto intense che agiscono per tempi molto brevi, al limite infinitesimi, producendo però un impulso finito. Esempi tipici sono la forza di una mazza sulla palla, la reazione del suolo durante un rimbalzo, la forza tra due biglie che collidono. Durante il brevissimo intervallo d'urto la posizione del corpo praticamente non cambia, mentre la velocità può variare in modo significativo. Inoltre, in questo intervallo le forze ordinarie non impulsive, come il peso, danno un contributo trascurabile all'impulso totale, perché il loro valore resta finito mentre $\Delta t \to 0$. È questa l'**approssimazione impulsiva**, che si userà sistematicamente nello studio degli urti.

Dal teorema dell'impulso discende immediatamente la **conservazione della quantità di moto** per un punto isolato: se la forza risultante è nulla, l'impulso è nullo e quindi $\vec{p}$ resta costante. Si tratta naturalmente di una riformulazione del primo principio della dinamica, ma vedremo che per i sistemi di punti diventa un risultato di grande portata.

### 7.1.2 Impulso angolare

Il ragionamento si estende in modo diretto al moto rotatorio. Fissato un **polo** $O$, il **momento angolare** del punto materiale rispetto a $O$ è $\vec{L}_O = \vec{r}\times\vec{p}$, dove $\vec{r}$ è il vettore posizione del punto rispetto al polo, mentre il **momento della forza** è $\vec{M}_O = \vec{r}\times\vec{F}$. Come visto nel capitolo sulla dinamica del punto, se il polo è fermo in un sistema inerziale (o, più in generale, se la sua velocità è parallela a quella del punto) vale il **teorema del momento angolare**:

$$
\vec{M}_O = \frac{\mathrm{d}\vec{L}_O}{\mathrm{d}t}.
$$

Integrando nel tempo si ottiene

$$
\vec{H}_O \equiv \int_{t_i}^{t_f}\vec{M}_O(t)\,\mathrm{d}t = \vec{L}_{O,f} - \vec{L}_{O,i} = \Delta\vec{L}_O.
$$

La grandezza $\vec{H}_O$ si chiama **impulso angolare** (o momento dell'impulso) rispetto al polo $O$ e la relazione è il **teorema dell'impulso angolare**. Si misura in $\mathrm{N\,m\,s}$, equivalente a $\mathrm{kg\,m^2/s}$, che è l'unità del momento angolare.

Anche in questo caso valgono alcune precisazioni. L'impulso angolare dipende dalla scelta del polo, così come il momento angolare; una scelta oculata del polo può semplificare enormemente un problema, ad esempio scegliendolo nel punto di applicazione di una forza incognita, il cui momento risulterà nullo. Il teorema richiede che il polo sia fisso, oppure che si tenga conto del termine aggiuntivo $-\vec{v}_O\times\vec{p}$ che compare quando il polo si muove. Infine, per una forza impulsiva applicata in un punto che non si sposta apprezzabilmente durante l'urto, l'impulso angolare è semplicemente il momento dell'impulso: $\vec{H}_O = \vec{r}\times\vec{J}$, dove $\vec{r}$ è la posizione del punto di applicazione.

La conseguenza più importante è la **conservazione del momento angolare**: se il momento risultante delle forze rispetto a un polo fisso è nullo, il momento angolare rispetto a quel polo resta costante. Ciò si verifica non solo quando la forza è nulla, ma anche quando la forza è sempre diretta verso il polo, cioè è una **forza centrale** con centro nel polo stesso. È il caso della gravitazione planetaria, della forza elettrica di un nucleo su un elettrone, della tensione di un filo che trattiene un corpo in rotazione e passa per un foro. In tutti questi casi $\vec{L}_O$ è costante in modulo, direzione e verso: il moto avviene in un piano fisso perpendicolare a $\vec{L}_O$, e la **velocità areolare** $\mathrm{d}A/\mathrm{d}t = L_O/(2m)$ resta costante, risultato che ritroveremo come seconda legge di Kepler.

Un esempio classico è quello di una pallina che ruota su un tavolo liscio legata a un filo che passa per un foro centrale: tirando il filo dal basso il raggio dell'orbita diminuisce, e poiché la tensione è centrale il momento angolare $L = m r v_\perp$ si conserva, quindi la velocità tangenziale aumenta in proporzione inversa al raggio. Lo stesso principio spiega l'accelerazione di un pattinatore che chiude le braccia durante una piroetta, anche se per una trattazione rigorosa servono i concetti di sistema di punti e corpo rigido.

Il confronto tra i due teoremi mostra una struttura parallela: la forza sta alla quantità di moto come il momento della forza sta al momento angolare, e l'impulso sta alla variazione di quantità di moto come l'impulso angolare sta alla variazione di momento angolare. Questa simmetria formale tra moto traslatorio e rotatorio si ritroverà più volte nel corso, in particolare nella dinamica dei sistemi e del corpo rigido.

### Esercizio d'esempio

Una palla da tennis di massa $m = 0{,}058\ \mathrm{kg}$ arriva orizzontalmente sulla racchetta con velocità di modulo $v_i = 30\ \mathrm{m/s}$ e viene rinviata nella direzione opposta con velocità $v_f = 40\ \mathrm{m/s}$. Il contatto dura $\Delta t = 4{,}0\ \mathrm{ms}$. Calcolare l'impulso fornito dalla racchetta e la forza media. Calcolare inoltre l'impulso angolare rispetto a un polo $O$ posto a $d = 0{,}50\ \mathrm{m}$ sotto la traiettoria della palla.

**Soluzione.** Si sceglie l'asse $x$ nel verso della velocità finale. Allora $v_{i,x} = -30\ \mathrm{m/s}$ e $v_{f,x} = +40\ \mathrm{m/s}$. La variazione di quantità di moto è

$$
\Delta p_x = m(v_{f,x} - v_{i,x}) = 0{,}058\cdot(40 + 30)\ \mathrm{kg\,m/s} = 4{,}06\ \mathrm{N\,s}.
$$

Per il teorema dell'impulso, $J_x = 4{,}06\ \mathrm{N\,s}$ (il peso è trascurabile nell'approssimazione impulsiva: $mg\,\Delta t \approx 2{,}3\times10^{-3}\ \mathrm{N\,s}$). La forza media vale

$$
\langle F_x\rangle = \frac{J_x}{\Delta t} = \frac{4{,}06}{4{,}0\times10^{-3}}\ \mathrm{N} \approx 1{,}0\times10^{3}\ \mathrm{N},
$$

circa 1800 volte il peso della palla. Per l'impulso angolare, il punto d'impatto si trova a $\vec{r} = (x, d, 0)$ rispetto a $O$ con $d = 0{,}50\ \mathrm{m}$ lungo $y$; poiché $\vec{J}$ è lungo $x$, si ha $\vec{H}_O = \vec{r}\times\vec{J} = -d\,J_x\,\hat{z}$, di modulo

$$
H_O = d\,J_x = 0{,}50\cdot 4{,}06\ \mathrm{N\,m\,s} \approx 2{,}0\ \mathrm{kg\,m^2/s},
$$

pari alla variazione del momento angolare della palla rispetto a $O$.

### Punti chiave

- L'**impulso** $\vec{J} = \int\vec{F}\,\mathrm{d}t$ di una forza è un vettore misurato in $\mathrm{N\,s}$; il teorema dell'impulso afferma $\vec{J} = \Delta\vec{p}$.
- La **forza media** è $\langle\vec{F}\rangle = \Delta\vec{p}/\Delta t$: a parità di $\Delta\vec{p}$, allungare il tempo d'interazione riduce la forza.
- Nell'**approssimazione impulsiva** le forze non impulsive (peso, attriti ordinari) danno contributo trascurabile durante l'urto.
- L'**impulso angolare** $\vec{H}_O = \int\vec{M}_O\,\mathrm{d}t$ è uguale alla variazione di momento angolare $\Delta\vec{L}_O$ rispetto a un polo fisso.
- Se la forza risultante è nulla si conserva $\vec{p}$; se il momento risultante è nullo si conserva $\vec{L}_O$.
- Per le **forze centrali** il momento angolare rispetto al centro si conserva: moto piano e velocità areolare costante.

## 7.2 Lavoro e potenza

Il teorema dell'impulso nasce dall'integrazione della legge della dinamica rispetto al tempo. Una seconda, e altrettanto fondamentale, possibilità è integrare rispetto allo spazio, cioè lungo la traiettoria percorsa dal punto. La grandezza che emerge da questa operazione è il **lavoro**, una grandezza scalare che misura in che misura una forza contribuisce a modificare lo stato di moto del punto spostandolo. Il lavoro per unità di tempo è la **potenza**, grandezza di primaria importanza in ingegneria perché caratterizza le macchine e i motori non per quanto lavoro possono compiere in assoluto, ma per quanto rapidamente possono farlo. Lavoro e potenza costituiscono il ponte tra la dinamica e il concetto di energia, che sarà sviluppato nella sezione successiva.

### 7.2.1 Lavoro

Si consideri un punto materiale che, sotto l'azione di una forza $\vec{F}$, compie uno spostamento infinitesimo $\mathrm{d}\vec{r}$. Si definisce **lavoro elementare** della forza il prodotto scalare

$$
\mathrm{d}W = \vec{F}\cdot\mathrm{d}\vec{r} = F\,\mathrm{d}r\cos\theta = F_x\,\mathrm{d}x + F_y\,\mathrm{d}y + F_z\,\mathrm{d}z,
$$

dove $\theta$ è l'angolo tra la forza e lo spostamento. Il **lavoro** compiuto lungo una traiettoria finita $\gamma$ che porta il punto dalla posizione $A$ alla posizione $B$ è l'integrale di linea

$$
W_{A\to B} = \int_{\gamma}\vec{F}\cdot\mathrm{d}\vec{r}.
$$

Il lavoro è uno **scalare** e si misura in **joule**: $1\ \mathrm{J} = 1\ \mathrm{N\,m} = 1\ \mathrm{kg\,m^2/s^2}$. Si noti che il joule ha le stesse dimensioni del momento di una forza, ma le due grandezze sono concettualmente diverse (una è scalare, l'altra vettoriale) e per il momento si preferisce scrivere $\mathrm{N\,m}$.

Dalla definizione discendono subito alcune proprietà. Il lavoro è **positivo** (lavoro *motore*) quando la forza ha una componente concorde allo spostamento, cioè per $\theta < 90^\circ$; è **negativo** (lavoro *resistente*) quando la componente è opposta, per $\theta > 90^\circ$; è **nullo** quando la forza è perpendicolare allo spostamento. Quest'ultimo caso è molto frequente: la reazione vincolare di un piano liscio, la tensione di un filo inestensibile in un pendolo, la forza centripeta in un moto circolare uniforme, la forza di Lorentz magnetica su una carica in moto non compiono mai lavoro. Ciò non significa che queste forze siano inutili, perché possono cambiare la *direzione* della velocità, ma non ne cambiano il *modulo*.

Solo la componente della forza tangente alla traiettoria compie lavoro. Scrivendo $\mathrm{d}\vec{r} = \hat{u}_T\,\mathrm{d}s$, dove $s$ è l'ascissa curvilinea e $\hat{u}_T$ il versore tangente, si ha $\mathrm{d}W = F_T\,\mathrm{d}s$. Se più forze agiscono contemporaneamente sul punto, il lavoro della risultante è la somma dei lavori delle singole forze, per la linearità del prodotto scalare e dell'integrale.

Nel caso generale, il lavoro **dipende dal percorso** seguito tra $A$ e $B$ e non soltanto dagli estremi. Ad esempio, trascinando un mobile su un pavimento scabro da un punto all'altro, la forza d'attrito compie un lavoro resistente proporzionale alla lunghezza del percorso: un percorso tortuoso dissipa più di uno rettilineo. Vi sono però forze particolari, dette **conservative**, il cui lavoro dipende solo dalle posizioni iniziale e finale; ad esse si dedicherà la sezione sull'energia potenziale.

Alcuni esempi di calcolo sono istruttivi. Per una **forza costante**, come il peso $\vec{P} = -mg\,\hat{z}$ in prossimità della superficie terrestre, il lavoro è $W = \vec{F}\cdot\Delta\vec{r}$, e per il peso in particolare $W = -mg(z_B - z_A)$: dipende solo dalla variazione di quota. Per una **forza elastica** unidimensionale $F_x = -kx$, il lavoro tra $x_A$ e $x_B$ è

$$
W = \int_{x_A}^{x_B}(-kx)\,\mathrm{d}x = -\tfrac{1}{2}k\left(x_B^2 - x_A^2\right).
$$

Per una forza d'**attrito dinamico** di modulo costante $\mu_d N$, sempre opposta alla velocità, il lavoro su un percorso di lunghezza $\ell$ è $W = -\mu_d N\ell$, sempre negativo.

Il risultato centrale che collega lavoro e moto è il **teorema dell'energia cinetica**, che sarà discusso nella sezione 7.3. Qui ne anticipiamo il senso: il lavoro della forza risultante lungo un tratto di traiettoria è uguale alla variazione della quantità $\tfrac{1}{2}mv^2$. Questo è il motivo per cui il lavoro è il concetto chiave per introdurre l'energia.

Un'osservazione importante riguarda la **dipendenza dal sistema di riferimento**. Poiché lo spostamento dipende dall'osservatore, anche il lavoro di una forza dipende dal riferimento: una forza può compiere lavoro nullo in un sistema e non nullo in un altro. Un passeggero seduto in un treno che accelera è fermo rispetto al treno, ma si sposta rispetto ai binari: il lavoro della forza che il sedile esercita su di lui è nullo nel primo riferimento e positivo nel secondo. Ciò non contraddice nulla, purché si usi coerentemente un unico sistema di riferimento inerziale per applicare i teoremi.

### 7.2.2 Potenza

Spesso non interessa soltanto *quanto* lavoro venga compiuto, ma anche *in quanto tempo*. Si definisce **potenza** istantanea il lavoro compiuto per unità di tempo:

$$
P = \frac{\mathrm{d}W}{\mathrm{d}t} = \vec{F}\cdot\frac{\mathrm{d}\vec{r}}{\mathrm{d}t} = \vec{F}\cdot\vec{v}.
$$

La potenza si misura in **watt**: $1\ \mathrm{W} = 1\ \mathrm{J/s}$. Nella pratica tecnica sono ancora diffuse unità non SI come il cavallo vapore ($1\ \mathrm{CV} \approx 735{,}5\ \mathrm{W}$) e, per l'energia, il chilowattora, $1\ \mathrm{kWh} = 3{,}6\times10^{6}\ \mathrm{J}$, che è un'unità di *energia*, non di potenza, nonostante il nome possa trarre in inganno.

La formula $P = \vec{F}\cdot\vec{v}$ è molto utile. Ad esempio, per un'automobile che procede a velocità costante su strada piana, la forza motrice trasmessa dalle ruote equilibra la somma delle resistenze (attrito di rotolamento e resistenza aerodinamica). Se la resistenza aerodinamica è proporzionale a $v^2$, la potenza necessaria per vincerla cresce come $v^3$: raddoppiare la velocità richiede una potenza otto volte maggiore. Questo spiega perché i consumi crescano così rapidamente alle alte velocità autostradali. Al contrario, a potenza erogata fissata, la forza motrice disponibile è inversamente proporzionale alla velocità, $F = P/v$: è il motivo per cui si usano le marce basse quando serve molta forza, ad esempio in salita o allo spunto.

Si definisce inoltre la **potenza media** in un intervallo $\Delta t$:

$$
\langle P\rangle = \frac{W}{\Delta t} = \frac{1}{\Delta t}\int_{t_i}^{t_f}P(t)\,\mathrm{d}t,
$$

e, viceversa, il lavoro compiuto in un intervallo è l'integrale temporale della potenza, $W = \int P\,\mathrm{d}t$, cioè l'area sotto la curva $P(t)$.

Il concetto di potenza è anche alla base della definizione di **rendimento** di una macchina: se una macchina assorbe una potenza $P_{in}$ e ne restituisce in forma utile una potenza $P_{out}$, il rendimento è $\eta = P_{out}/P_{in}$, sempre minore di uno a causa delle inevitabili dissipazioni (attriti, effetto Joule, perdite termiche). Un motore elettrico ha tipicamente rendimenti dell'ordine dell'85-95%, un motore a combustione interna del 25-40%.

Combinando potenza e teorema dell'energia cinetica si ottiene la forma differenziale $P = \mathrm{d}K/\mathrm{d}t$: la potenza della forza risultante è il tasso di variazione dell'energia cinetica. Anche la potenza, come il lavoro, dipende dal sistema di riferimento, poiché vi compare la velocità.

Per i moti rotatori esiste un'espressione analoga. Se un corpo ruota attorno a un asse fisso con velocità angolare $\omega$ sotto l'azione di un momento assiale $M$, la potenza vale $P = M\omega$. È la relazione che lega coppia motrice e regime di rotazione in un motore: a parità di potenza, un motore che gira lentamente sviluppa una coppia elevata, uno che gira velocemente una coppia ridotta.

### Esercizio d'esempio

Un'automobile di massa $m = 1200\ \mathrm{kg}$ sale a velocità costante $v = 72\ \mathrm{km/h}$ lungo una strada rettilinea con pendenza $\alpha = 5{,}0^\circ$. Le resistenze complessive (aerodinamica e di rotolamento) valgono $F_r = 500\ \mathrm{N}$. Calcolare la potenza erogata alle ruote e il lavoro compiuto dal motore in un percorso di $\ell = 2{,}0\ \mathrm{km}$. Calcolare anche il lavoro del peso sullo stesso tratto.

**Soluzione.** La velocità in unità SI è $v = 72/3{,}6 = 20\ \mathrm{m/s}$. Essendo il moto uniforme, la forza motrice $F_m$ equilibra la componente del peso lungo il piano e le resistenze:

$$
F_m = mg\sin\alpha + F_r = 1200\cdot9{,}81\cdot\sin5^\circ + 500\ \mathrm{N} \approx 1026 + 500 = 1526\ \mathrm{N}.
$$

La potenza è parallela alla velocità, quindi

$$
P = F_m v = 1526\cdot 20\ \mathrm{W} \approx 3{,}05\times10^{4}\ \mathrm{W} \approx 30\ \mathrm{kW}.
$$

Il lavoro del motore sul tratto è $W_m = F_m\ell = 1526\cdot2000\ \mathrm{J} \approx 3{,}05\times10^{6}\ \mathrm{J}$ (pari a circa $0{,}85\ \mathrm{kWh}$), oppure equivalentemente $W_m = P\,\Delta t$ con $\Delta t = \ell/v = 100\ \mathrm{s}$. Il dislivello è $h = \ell\sin\alpha \approx 174\ \mathrm{m}$, perciò il lavoro del peso è

$$
W_P = -mgh \approx -1200\cdot9{,}81\cdot174\ \mathrm{J} \approx -2{,}05\times10^{6}\ \mathrm{J}.
$$

Il lavoro delle resistenze è $W_r = -F_r\ell = -1{,}0\times10^{6}\ \mathrm{J}$. La somma dei tre lavori è nulla, coerentemente con il fatto che l'energia cinetica non cambia.

### Punti chiave

- Il **lavoro** di una forza è l'integrale di linea $W = \int_\gamma\vec{F}\cdot\mathrm{d}\vec{r}$; è uno scalare e si misura in joule.
- Compie lavoro solo la componente tangenziale della forza: le forze perpendicolari alla velocità (reazioni di vincoli lisci, forza centripeta) hanno lavoro nullo.
- In generale il lavoro dipende dal percorso; per le **forze conservative** dipende solo dagli estremi.
- Esempi notevoli: peso $W = -mg\Delta z$, forza elastica $W = -\tfrac12 k(x_B^2 - x_A^2)$, attrito dinamico $W = -\mu_d N\ell$.
- La **potenza** è $P = \mathrm{d}W/\mathrm{d}t = \vec{F}\cdot\vec{v}$, si misura in watt; per rotazioni $P = M\omega$.
- Il kilowattora è un'unità di energia: $1\ \mathrm{kWh} = 3{,}6\ \mathrm{MJ}$.
- Lavoro e potenza dipendono dal sistema di riferimento, perché vi compaiono spostamento e velocità.

## 7.3 Energia

Il concetto di **energia** è forse il più unificante dell'intera fisica. In meccanica esso nasce in modo naturale dal lavoro: il lavoro compiuto dalla forza risultante su un punto materiale si traduce in una variazione di una grandezza legata alla velocità, l'**energia cinetica**; il lavoro di certe forze particolari, quelle conservative, si può esprimere come variazione di una funzione della sola posizione, l'**energia potenziale**. La somma delle due, l'**energia meccanica**, gode di una proprietà notevolissima: in assenza di forze dissipative resta costante durante il moto. Questa sezione costruisce passo dopo passo questi concetti, discutendo anche come l'energia potenziale permetta di analizzare le posizioni di equilibrio di un punto, cioè la sua statica, in modo elegante e generale.

### 7.3.1 Energia cinetica

Si parta dalla seconda legge della dinamica per un punto di massa costante, $\vec{F} = m\,\mathrm{d}\vec{v}/\mathrm{d}t$, e si calcoli il lavoro elementare della forza risultante:

$$
\mathrm{d}W = \vec{F}\cdot\mathrm{d}\vec{r} = m\frac{\mathrm{d}\vec{v}}{\mathrm{d}t}\cdot\vec{v}\,\mathrm{d}t = m\,\vec{v}\cdot\mathrm{d}\vec{v} = \mathrm{d}\!\left(\tfrac{1}{2}mv^2\right).
$$

Si è usata l'identità $\vec{v}\cdot\mathrm{d}\vec{v} = \tfrac{1}{2}\mathrm{d}(\vec{v}\cdot\vec{v})$. Definendo l'**energia cinetica**

$$
K = \tfrac{1}{2}mv^2 = \frac{p^2}{2m},
$$

e integrando lungo la traiettoria da $A$ a $B$, si ottiene il **teorema dell'energia cinetica** (o teorema delle forze vive):

$$
W_{A\to B} = K_B - K_A = \Delta K.
$$

In parole: il lavoro compiuto dalla forza risultante su un punto materiale è uguale alla variazione della sua energia cinetica. Il teorema vale per qualsiasi forza, conservativa o meno, purché si consideri il lavoro di *tutte* le forze agenti, e vale in qualunque sistema di riferimento inerziale (nei riferimenti non inerziali va aggiunto il lavoro delle forze apparenti).

L'energia cinetica è una grandezza scalare, sempre **non negativa**, nulla solo se il punto è fermo; si misura in joule. Dipende dal sistema di riferimento, poiché dipende dalla velocità. Essa rappresenta, in un senso preciso, la capacità di un corpo in moto di compiere lavoro: per arrestare un corpo che ha energia cinetica $K$, le forze esterne devono compiere su di esso un lavoro $-K$, e il corpo, per reazione, compie sull'ambiente un lavoro positivo. È il motivo per cui l'energia d'impatto di un veicolo cresce col quadrato della velocità e lo spazio di frenata, a parità di forza frenante, è proporzionale a $v^2$: passando da $50\ \mathrm{km/h}$ a $70\ \mathrm{km/h}$ lo spazio di frenata quasi raddoppia.

È utile confrontare il teorema dell'energia cinetica con quello dell'impulso. Il primo è scalare, e quindi fornisce una sola equazione, ma coinvolge lo spazio percorso; il secondo è vettoriale e coinvolge il tempo. Quando in un problema compaiono distanze e velocità ma non tempi, il primo è di solito lo strumento più rapido; quando compaiono tempi e velocità ma non distanze, conviene il secondo.

Si osservi infine che la formula $K = \tfrac12 mv^2$ è un'approssimazione non relativistica. Come visto nel capitolo sulla meccanica relativistica, l'espressione esatta è $K = (\gamma - 1)mc^2$, che si riduce a quella classica per $v \ll c$.

### 7.3.2 Energia potenziale

Una forza si dice **conservativa** se il lavoro che compie su un punto che si sposta da $A$ a $B$ dipende soltanto dalle posizioni $A$ e $B$ e non dal particolare percorso seguito. Proprietà equivalenti sono: il lavoro lungo qualunque percorso chiuso è nullo,

$$
\oint\vec{F}\cdot\mathrm{d}\vec{r} = 0,
$$

e, se il dominio è semplicemente connesso, il rotore della forza è nullo, $\nabla\times\vec{F} = 0$. Condizione necessaria perché una forza sia conservativa è che dipenda solo dalla posizione: forze che dipendono dalla velocità, come l'attrito o la resistenza viscosa, non possono esserlo.

Per una forza conservativa si può definire una funzione scalare della posizione, l'**energia potenziale** $U(\vec{r})$, tale che

$$
W_{A\to B} = -\left[U(B) - U(A)\right] = -\Delta U.
$$

Il segno meno ha un significato fisico preciso: quando la forza compie lavoro positivo, l'energia potenziale diminuisce. L'energia potenziale è definita a meno di una **costante additiva** arbitraria, poiché solo le sue differenze hanno significato fisico; si sceglie un punto di riferimento in cui porre $U = 0$, e il valore in un generico punto $P$ è $U(P) = -\int_{\text{rif}}^{P}\vec{F}\cdot\mathrm{d}\vec{r}$.

La relazione inversa permette di ricavare la forza dall'energia potenziale: in forma differenziale $\mathrm{d}U = -\vec{F}\cdot\mathrm{d}\vec{r}$, da cui

$$
\vec{F} = -\nabla U = -\left(\frac{\partial U}{\partial x}\hat{x} + \frac{\partial U}{\partial y}\hat{y} + \frac{\partial U}{\partial z}\hat{z}\right).
$$

La forza è quindi diretta nel verso in cui l'energia potenziale decresce più rapidamente, ed è perpendicolare alle superfici **equipotenziali** $U = \text{cost}$.

Le energie potenziali più importanti in meccanica sono tre. Per la **forza peso** in prossimità della superficie terrestre, $\vec{F} = -mg\,\hat{z}$, si ha $U = mgz$, con lo zero a quota $z = 0$ scelta arbitrariamente. Per la **forza elastica** di una molla ideale di costante $k$, $F_x = -kx$, si ha $U = \tfrac12 kx^2$, con lo zero naturale nella posizione di riposo. Per la **forza gravitazionale** tra due masse puntiformi, $F = -GMm/r^2$ radiale, si ha $U = -GMm/r$, con lo zero all'infinito; ne riparleremo diffusamente nel capitolo sulla gravitazione. Più in generale, ogni **forza centrale** il cui modulo dipende solo dalla distanza dal centro, $\vec{F} = f(r)\hat{r}$, è conservativa, con $U(r) = -\int f(r)\,\mathrm{d}r$.

Le forze non conservative si dividono in **dissipative**, come l'attrito, il cui lavoro è sempre negativo e trasforma energia meccanica in energia interna (riscaldamento), e in forze che possono compiere lavoro positivo senza derivare da un potenziale, come quelle esercitate da un motore o dai muscoli.

### 7.3.3 Statica del punto

La conoscenza dell'energia potenziale permette di studiare in modo molto efficace l'**equilibrio** di un punto materiale soggetto a forze conservative. Una posizione è di equilibrio se la forza risultante vi è nulla; poiché $\vec{F} = -\nabla U$, le posizioni di equilibrio sono i **punti stazionari** dell'energia potenziale, quelli in cui il gradiente si annulla. Nel caso unidimensionale la condizione è $\mathrm{d}U/\mathrm{d}x = 0$.

La natura dell'equilibrio si ricava dal comportamento di $U$ attorno al punto stazionario $x_0$. Se $U$ ha un **minimo** ($U''(x_0) > 0$), uno spostamento piccolo genera una forza che riporta il punto verso $x_0$: l'equilibrio è **stabile**. Se $U$ ha un **massimo** ($U''(x_0) < 0$), la forza conseguente allontana ulteriormente il punto: l'equilibrio è **instabile**. Se $U$ è costante in un intorno di $x_0$, il punto resta in equilibrio in qualunque posizione vicina: l'equilibrio è **indifferente**. L'immagine intuitiva è quella di una pallina su un profilo collinare: in fondo a una valle è stabile, sulla cima di un dosso è instabile, su un tratto piano è indifferente.

Attorno a un minimo stabile si può sviluppare l'energia potenziale in serie di Taylor:

$$
U(x) \approx U(x_0) + \tfrac12 U''(x_0)(x - x_0)^2,
$$

ottenendo una forza di richiamo $F \approx -U''(x_0)(x - x_0)$, di tipo elastico con costante efficace $k_{\text{eff}} = U''(x_0)$. Ne segue che **ogni piccola oscillazione attorno a un minimo dell'energia potenziale è approssimativamente armonica**, con pulsazione $\omega = \sqrt{U''(x_0)/m}$. Questo risultato spiega perché l'oscillatore armonico sia così ubiquo in fisica: dalle vibrazioni degli atomi in un solido alle oscillazioni di un pendolo per piccoli angoli, fino alle vibrazioni delle strutture in ingegneria.

Il grafico di $U(x)$ consente inoltre di prevedere qualitativamente il moto senza integrare le equazioni. Fissata l'energia meccanica $E$, il moto è possibile solo nelle regioni in cui $U(x) \le E$, poiché l'energia cinetica $K = E - U$ non può essere negativa. I punti in cui $U(x) = E$ sono **punti di inversione**: lì la velocità si annulla e il moto cambia verso. Se la regione permessa è limitata da due punti di inversione, il moto è oscillatorio e periodico (moto **legato**); se si estende all'infinito, il punto può allontanarsi indefinitamente (moto **non legato**). L'altezza delle barriere di potenziale determina se il punto può superarle o resta intrappolato in una buca.

### 7.3.4 Energia meccanica

Si consideri ora un punto su cui agiscono forze conservative, di energia potenziale complessiva $U$, e forze non conservative. Il teorema dell'energia cinetica dice $W_{\text{tot}} = \Delta K$; separando i contributi, $W_{\text{tot}} = W_c + W_{nc} = -\Delta U + W_{nc}$. Ne segue

$$
\Delta K + \Delta U = W_{nc}.
$$

Definendo l'**energia meccanica**

$$
E = K + U,
$$

si ottiene $\Delta E = W_{nc}$: la variazione dell'energia meccanica è uguale al lavoro delle sole forze non conservative. Se queste sono assenti, o se il loro lavoro è nullo (come per le reazioni di vincoli lisci e fissi), l'energia meccanica si **conserva**:

$$
E = \tfrac12 mv^2 + U(\vec{r}) = \text{costante}.
$$

È questo il **principio di conservazione dell'energia meccanica**, che verrà discusso in dettaglio nella prossima sezione. Se invece agiscono forze dissipative, $W_{nc} < 0$ e l'energia meccanica diminuisce: la quota persa non scompare, ma si trasforma in energia interna dei corpi, osservabile come riscaldamento, come chiarirà la termodinamica.

L'energia meccanica fornisce un **integrale primo del moto**: una relazione tra posizione e velocità che sostituisce un'integrazione dell'equazione del moto. Nel caso unidimensionale, ad esempio, dalla conservazione dell'energia si ricava $v(x) = \pm\sqrt{2[E - U(x)]/m}$, e il tempo per andare da $x_1$ a $x_2$ si ottiene con una sola quadratura, $t = \int \mathrm{d}x/v(x)$.

### Esercizio d'esempio

Un blocco di massa $m = 2{,}0\ \mathrm{kg}$ viene lasciato da fermo in cima a un piano inclinato di altezza $h = 1{,}5\ \mathrm{m}$ e inclinazione $\alpha = 30^\circ$. Il coefficiente di attrito dinamico è $\mu_d = 0{,}20$. Arrivato in fondo, il blocco percorre un tratto orizzontale liscio e comprime una molla di costante $k = 800\ \mathrm{N/m}$. Calcolare la velocità alla base del piano e la massima compressione della molla.

**Soluzione.** Lungo il piano la lunghezza percorsa è $\ell = h/\sin\alpha = 3{,}0\ \mathrm{m}$ e la normale vale $N = mg\cos\alpha$. Il lavoro dell'attrito è

$$
W_{nc} = -\mu_d mg\cos\alpha\,\ell = -0{,}20\cdot2{,}0\cdot9{,}81\cdot0{,}866\cdot3{,}0\ \mathrm{J} \approx -10{,}2\ \mathrm{J}.
$$

L'energia meccanica iniziale (zero di $U$ alla base) è $E_i = mgh = 2{,}0\cdot9{,}81\cdot1{,}5 \approx 29{,}4\ \mathrm{J}$. Alla base

$$
\tfrac12 mv^2 = E_i + W_{nc} \approx 19{,}2\ \mathrm{J} \;\Rightarrow\; v = \sqrt{\frac{2\cdot19{,}2}{2{,}0}}\ \mathrm{m/s} \approx 4{,}4\ \mathrm{m/s}.
$$

Sul tratto liscio l'energia meccanica si conserva; alla massima compressione $x_{\max}$ la velocità è nulla:

$$
\tfrac12 k x_{\max}^2 = 19{,}2\ \mathrm{J} \;\Rightarrow\; x_{\max} = \sqrt{\frac{2\cdot19{,}2}{800}}\ \mathrm{m} \approx 0{,}22\ \mathrm{m}.
$$

### Punti chiave

- **Teorema dell'energia cinetica**: il lavoro della forza risultante è $W = \Delta K$, con $K = \tfrac12 mv^2 = p^2/2m$; vale per qualsiasi forza.
- Una forza è **conservativa** se il suo lavoro non dipende dal percorso (equivalentemente $\oint\vec{F}\cdot\mathrm{d}\vec{r} = 0$); allora $W = -\Delta U$ e $\vec{F} = -\nabla U$.
- Energie potenziali notevoli: peso $mgz$, molla $\tfrac12 kx^2$, gravitazione $-GMm/r$; $U$ è definita a meno di una costante.
- Le posizioni di **equilibrio** sono i punti stazionari di $U$: minimo stabile, massimo instabile, tratto piatto indifferente.
- Attorno a un minimo, le piccole oscillazioni sono armoniche con $\omega = \sqrt{U''(x_0)/m}$.
- L'**energia meccanica** $E = K + U$ varia solo per il lavoro delle forze non conservative: $\Delta E = W_{nc}$.
- Nelle regioni con $U > E$ il moto è proibito; i punti con $U = E$ sono punti di inversione.

## 7.4 Teoremi di conservazione

Le relazioni integrali ricavate nelle sezioni precedenti conducono, sotto opportune condizioni, a tre **leggi di conservazione** per il punto materiale: della quantità di moto, del momento angolare e dell'energia meccanica. Una grandezza si dice **conservata** se rimane costante nel tempo durante l'evoluzione del sistema, qualunque sia la complessità del moto. Le leggi di conservazione sono strumenti di straordinaria efficacia perché permettono di mettere in relazione direttamente lo stato iniziale e quello finale, saltando tutti i passaggi intermedi. Hanno inoltre un significato profondo: come si dimostra nella meccanica analitica (teorema di Noether), ciascuna di esse è legata a una **simmetria** delle leggi fisiche. In questa sezione si raccolgono le tre leggi, se ne precisano con cura le condizioni di validità e si discute come scegliere quella più adatta a un dato problema.

Il primo teorema riguarda la **conservazione della quantità di moto**. Dal teorema dell'impulso, $\Delta\vec{p} = \int\vec{F}\,\mathrm{d}t$, segue che se la forza risultante agente sul punto è identicamente nulla in un intervallo di tempo, la quantità di moto resta costante in quell'intervallo:

$$
\vec{F} = 0 \;\Longrightarrow\; \vec{p} = m\vec{v} = \text{costante}.
$$

Per un singolo punto materiale questo enunciato coincide con il principio d'inerzia e può sembrare banale. Tuttavia ha un'importante versione parziale: se è nulla soltanto una componente della forza, ad esempio $F_x = 0$, allora si conserva la sola componente corrispondente $p_x$, anche se le altre variano. È il caso di un proiettile in volo in assenza di attrito dell'aria: il peso è verticale, quindi la componente orizzontale della velocità resta costante, mentre quella verticale varia uniformemente. Inoltre, come si vedrà nel capitolo sulla meccanica dei sistemi, la conservazione della quantità di moto diventa realmente potente per un sistema di più corpi isolato, dove le forze interne si annullano a coppie per il terzo principio. La simmetria associata a questa legge è l'**omogeneità dello spazio**: le leggi della fisica sono le stesse in ogni punto, e traslare l'intero esperimento non ne cambia l'esito.

Il secondo teorema riguarda la **conservazione del momento angolare**. Dal teorema dell'impulso angolare, se il momento risultante delle forze rispetto a un polo fisso $O$ è nullo, il momento angolare rispetto a quel polo si conserva:

$$
\vec{M}_O = 0 \;\Longrightarrow\; \vec{L}_O = \vec{r}\times m\vec{v} = \text{costante}.
$$

Il momento può annullarsi anche in presenza di forze non nulle, purché esse siano sempre dirette verso il polo (o da esso), cioè siano **centrali**. Questo rende il teorema prezioso nello studio dei moti planetari, dell'atomo di idrogeno classico, delle orbite dei satelliti. Anche qui esiste una versione parziale: se è nulla la componente del momento lungo un asse fisso, si conserva la componente del momento angolare lungo quell'asse. Ad esempio, per un pendolo conico o per un corpo che si muove su una superficie di rotazione liscia con asse verticale, il peso e la reazione vincolare hanno momento con componente verticale nulla rispetto a un punto dell'asse, per cui si conserva $L_z$. La simmetria associata è l'**isotropia dello spazio**: le leggi della fisica non dipendono dall'orientazione nello spazio.

Il terzo teorema riguarda la **conservazione dell'energia meccanica**. Dal teorema dell'energia cinetica e dalla definizione di energia potenziale segue che, se agiscono solo forze conservative oppure le forze non conservative non compiono lavoro, l'energia meccanica si conserva:

$$
W_{nc} = 0 \;\Longrightarrow\; E = K + U = \text{costante}.
$$

Le forze che non compiono lavoro comprendono le reazioni dei vincoli lisci e fissi (perpendicolari allo spostamento), le tensioni di fili inestensibili vincolati a punti fissi e, per il caso del rotolamento puro, la forza d'attrito statico applicata nel punto di contatto istantaneamente fermo. Non va confusa la conservazione dell'energia *meccanica*, che vale solo sotto queste condizioni, con il principio generale di conservazione dell'*energia*, che vale sempre: in presenza di attriti l'energia meccanica diminuisce, ma l'energia totale, che include l'energia interna dei corpi, resta costante. La formulazione completa di questo principio è il primo principio della termodinamica. La simmetria associata alla conservazione dell'energia è l'**omogeneità del tempo**: le leggi della fisica non cambiano da un istante all'altro, per cui ripetere un esperimento domani dà lo stesso risultato di oggi.

Un punto delicato riguarda il **sistema di riferimento**. I teoremi di conservazione si applicano in un riferimento inerziale. In un riferimento non inerziale occorre includere le forze apparenti, che in generale non sono nulle e possono rompere la conservazione: ad esempio in un riferimento rotante la forza centrifuga è conservativa e possiede un'energia potenziale $-\tfrac12 m\omega^2 r_\perp^2$, mentre la forza di Coriolis, perpendicolare alla velocità relativa, non compie lavoro. Inoltre il valore delle grandezze conservate dipende dall'osservatore: la quantità di moto e l'energia cinetica cambiano cambiando riferimento, ma la loro costanza nel tempo è preservata in ogni riferimento inerziale.

Nella pratica della risoluzione dei problemi, i teoremi di conservazione si applicano secondo una strategia ben precisa. Per prima cosa si identifica con cura il sistema e le forze che agiscono su di esso. Poi si verifica per ciascuna legge se ne sono soddisfatte le ipotesi: la forza risultante (o una sua componente) è nulla? Il momento risultante rispetto a un opportuno polo (o lungo un asse) è nullo? Le forze non conservative compiono lavoro? A questo punto si scrivono le equazioni di conservazione applicabili tra lo stato iniziale e quello finale; spesso il numero di equazioni così ottenute è sufficiente a determinare le incognite. Quando l'energia non si conserva, si usa la forma generalizzata $\Delta E = W_{nc}$, calcolando esplicitamente il lavoro dissipato.

Un esempio istruttivo è il **pendolo semplice** di lunghezza $\ell$. Sul punto agiscono il peso (conservativo) e la tensione del filo (perpendicolare alla velocità, lavoro nullo): l'energia meccanica si conserva. Rispetto al punto di sospensione, invece, il peso ha momento non nullo, quindi il momento angolare non si conserva; né si conserva la quantità di moto, perché la risultante non è nulla. La sola conservazione dell'energia basta però a trovare la velocità in funzione dell'angolo, $v^2 = 2g\ell(\cos\theta - \cos\theta_0)$, senza integrare l'equazione del moto non lineare. Un caso opposto è quello della pallina sul tavolo liscio trattenuta da un filo che passa per un foro: tirando il filo, la tensione compie lavoro (il punto di applicazione si sposta radialmente) e l'energia cinetica aumenta, ma il momento angolare rispetto al foro si conserva, perché la tensione è centrale. Questi due esempi mostrano come la scelta della legge di conservazione giusta dipenda da un'analisi attenta delle forze.

Infine, le leggi di conservazione forniscono anche un potente strumento di **verifica**. Se in una soluzione numerica o analitica di un problema conservativo l'energia calcolata cambia nel tempo, c'è un errore; se in un esperimento si osserva una perdita di energia meccanica, si deduce la presenza di forze dissipative e se ne può stimare l'entità. In ambito ingegneristico, ad esempio, il bilancio energetico di una macchina permette di calcolare le perdite e il rendimento senza conoscere il dettaglio dei singoli meccanismi dissipativi.

È utile riassumere in una tabella ideale le corrispondenze. La quantità di moto si conserva se la forza risultante è nulla, ed è legata all'omogeneità dello spazio; il momento angolare si conserva se il momento risultante è nullo, ed è legato all'isotropia dello spazio; l'energia meccanica si conserva se le forze non conservative non compiono lavoro, ed è legata all'omogeneità del tempo. Le tre leggi sono indipendenti: in un problema possono valere tutte, alcune o nessuna, e riconoscere quali valgano è la prima e più importante abilità da sviluppare.

### Esercizio d'esempio

Una pallina di massa $m = 0{,}10\ \mathrm{kg}$ ruota su un tavolo orizzontale liscio, legata a un filo che passa per un foro centrale $O$. Inizialmente il raggio è $r_1 = 0{,}50\ \mathrm{m}$ e la velocità $v_1 = 2{,}0\ \mathrm{m/s}$. Tirando lentamente il filo dal basso il raggio viene ridotto a $r_2 = 0{,}20\ \mathrm{m}$. Calcolare la nuova velocità, la variazione di energia cinetica e il lavoro compiuto dalla persona che tira il filo.

**Soluzione.** La tensione è centrale rispetto a $O$, il peso e la normale si bilanciano e hanno momento risultante nullo: si conserva $L_O$. Poiché la velocità è sempre (quasi) tangenziale,

$$
m r_1 v_1 = m r_2 v_2 \;\Rightarrow\; v_2 = v_1\frac{r_1}{r_2} = 2{,}0\cdot\frac{0{,}50}{0{,}20}\ \mathrm{m/s} = 5{,}0\ \mathrm{m/s}.
$$

L'energia meccanica *non* si conserva, perché la tensione ha una componente lungo lo spostamento radiale. La variazione di energia cinetica è

$$
\Delta K = \tfrac12 m\left(v_2^2 - v_1^2\right) = \tfrac12\cdot0{,}10\cdot(25 - 4{,}0)\ \mathrm{J} = 1{,}05\ \mathrm{J}.
$$

Per il teorema dell'energia cinetica il lavoro della tensione, e quindi quello della persona che tira il filo (filo ideale), è $W = 1{,}05\ \mathrm{J}$. Si verifica anche direttamente: $T = mv^2/r = L^2/(m r^3)$ con $L = 0{,}10\ \mathrm{kg\,m^2/s}$, e $W = \int_{r_2}^{r_1}T\,\mathrm{d}r = \frac{L^2}{2m}\left(\frac{1}{r_2^2} - \frac{1}{r_1^2}\right) = 0{,}05\cdot(25 - 4)\ \mathrm{J} = 1{,}05\ \mathrm{J}$.

### Punti chiave

- Una grandezza **conservata** resta costante durante il moto; le leggi di conservazione legano direttamente stato iniziale e finale.
- **Quantità di moto**: si conserva se $\vec{F}_{\text{ris}} = 0$; se è nulla una sola componente, si conserva la componente corrispondente.
- **Momento angolare**: si conserva rispetto a un polo fisso se $\vec{M}_O = 0$, in particolare per forze centrali.
- **Energia meccanica**: si conserva se $W_{nc} = 0$; in generale $\Delta E = W_{nc}$.
- Simmetrie associate: omogeneità dello spazio ($\vec{p}$), isotropia dello spazio ($\vec{L}$), omogeneità del tempo ($E$).
- Le tre leggi sono indipendenti: va verificato caso per caso quali valgono, in un riferimento inerziale.
- La perdita di energia meccanica per attrito non viola la conservazione dell'energia totale, che include l'energia interna.
