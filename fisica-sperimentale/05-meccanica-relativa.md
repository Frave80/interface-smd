# Capitolo 5 — Meccanica relativa

Ogni descrizione del moto presuppone la scelta di un sistema di riferimento: dire che un corpo "è fermo" o "si muove a 10 m/s" non ha significato se non si specifica rispetto a che cosa. Finora abbiamo lavorato con un unico riferimento, tacitamente supposto inerziale. In molte situazioni pratiche, però, è naturale o inevitabile descrivere il moto da un riferimento che a sua volta si muove: il passeggero di un treno, il pilota di un aereo, un sensore montato su un braccio robotico, e soprattutto noi stessi, che osserviamo il mondo da una Terra che ruota su se stessa e intorno al Sole. La **meccanica relativa** studia come cambiano posizione, velocità e accelerazione quando si passa da un riferimento a un altro in moto rispetto al primo (cinematica relativa), come si modificano di conseguenza le leggi della dinamica (dinamica relativa, con l'introduzione delle forze apparenti) e come si scrivono le condizioni di equilibrio in un riferimento non inerziale (statica relativa). In tutto il capitolo restiamo nell'ambito della meccanica classica: il tempo è assoluto, uguale per tutti gli osservatori, e le distanze tra punti non dipendono dal riferimento. Il superamento di queste ipotesi sarà oggetto del capitolo 6.

## 5.1 Cinematica relativa

Consideriamo due sistemi di riferimento. Il primo, che indichiamo con $S$ e chiamiamo **riferimento fisso** (o assoluto), ha origine $O$ e assi cartesiani con versori $\hat{\imath}, \hat{\jmath}, \hat{k}$. Il secondo, $S'$, detto **riferimento mobile** (o relativo), ha origine $O'$ e versori $\hat{\imath}', \hat{\jmath}', \hat{k}'$. Il moto di $S'$ rispetto a $S$ è descritto in modo completo da due informazioni: il moto dell'origine $O'$, cioè il vettore posizione $\vec{r}_{O'}(t)$ con le sue derivate, e l'orientazione degli assi mobili, che nel caso più generale ruotano con una **velocità angolare** $\vec{\omega}(t)$. Il nome "fisso" è puramente convenzionale: indica semplicemente il riferimento rispetto al quale descriviamo il moto dell'altro. Tuttavia, nella dinamica relativa, sarà conveniente che $S$ sia inerziale.

Un punto materiale P viene osservato da entrambi i riferimenti. Chiameremo **grandezze assolute** quelle misurate in $S$ (posizione $\vec{r}$, velocità $\vec{v}$, accelerazione $\vec{a}$) e **grandezze relative** quelle misurate in $S'$ ($\vec{r}'$, $\vec{v}'$, $\vec{a}'$). Lo scopo della cinematica relativa è trovare le relazioni tra le une e le altre. L'ipotesi fondamentale, tipica della meccanica classica, è che il tempo $t$ sia lo stesso nei due riferimenti e che le lunghezze dei vettori spaziali siano invarianti.

### 5.1.1 Posizione

La relazione tra le posizioni è puramente geometrica. Il vettore che va da $O$ a P si ottiene sommando il vettore da $O$ a $O'$ e quello da $O'$ a P:

$$\vec{r} = \vec{r}_{O'} + \vec{r}'.$$

Il vettore $\vec{r}'$ è lo stesso oggetto geometrico visto da entrambi gli osservatori, ma l'osservatore mobile ne conosce le componenti rispetto ai propri assi:

$$\vec{r}' = x'\hat{\imath}' + y'\hat{\jmath}' + z'\hat{k}'.$$

Se gli assi di $S'$ restano paralleli a quelli di $S$ (moto di **traslazione**), i versori mobili sono costanti e coincidenti con quelli fissi; allora le componenti si trasformano semplicemente sommando le coordinate di $O'$: $x = x_{O'} + x'$, e analogamente per $y$ e $z$. Se invece $S'$ ruota, i versori mobili cambiano direzione nel tempo e le componenti di $\vec{r}'$ nei due sistemi sono legate da una matrice di rotazione dipendente dal tempo. Per esempio, per una rotazione attorno all'asse $z$ di un angolo $\theta(t)$:

$$\hat{\imath}' = \cos\theta\,\hat{\imath} + \sin\theta\,\hat{\jmath}, \qquad \hat{\jmath}' = -\sin\theta\,\hat{\imath} + \cos\theta\,\hat{\jmath}.$$

Questa distinzione tra il vettore come ente geometrico e le sue componenti in una base è il cuore della cinematica relativa. Un vettore costante per un osservatore può essere variabile per l'altro, proprio perché le basi ruotano l'una rispetto all'altra.

### 5.1.2 Velocità

Per ottenere la velocità assoluta deriviamo la relazione tra le posizioni rispetto al tempo, nel riferimento $S$:

$$\vec{v} = \frac{d\vec{r}}{dt} = \vec{v}_{O'} + \frac{d\vec{r}'}{dt}.$$

La derivata di $\vec{r}'$ va calcolata con attenzione. Applicando la regola del prodotto alle componenti,

$$\frac{d\vec{r}'}{dt} = \left(\dot{x}'\hat{\imath}' + \dot{y}'\hat{\jmath}' + \dot{z}'\hat{k}'\right) + \left(x'\frac{d\hat{\imath}'}{dt} + y'\frac{d\hat{\jmath}'}{dt} + z'\frac{d\hat{k}'}{dt}\right).$$

Il primo gruppo di termini è ciò che l'osservatore mobile misura come velocità del punto: è la **velocità relativa** $\vec{v}'$. Il secondo gruppo è dovuto alla rotazione degli assi. Le **formule di Poisson** stabiliscono che la derivata di un versore solidale con un riferimento che ruota con velocità angolare $\vec{\omega}$ vale

$$\frac{d\hat{u}'}{dt} = \vec{\omega}\times\hat{u}'.$$

Il significato è intuitivo: un vettore di modulo costante che ruota varia solo in direzione, e la sua derivata è perpendicolare sia al vettore sia all'asse di rotazione. Applicando le formule di Poisson il secondo gruppo diventa $\vec{\omega}\times\vec{r}'$. Si ottiene così il **teorema delle velocità relative**:

$$\vec{v} = \vec{v}' + \vec{v}_{O'} + \vec{\omega}\times\vec{r}'.$$

La somma $\vec{v}_t = \vec{v}_{O'} + \vec{\omega}\times\vec{r}'$ si chiama **velocità di trascinamento**: è la velocità che il punto P avrebbe se fosse rigidamente solidale con il riferimento mobile, cioè se fosse "trascinato" da esso. In forma compatta: velocità assoluta = velocità relativa + velocità di trascinamento, $\vec{v} = \vec{v}' + \vec{v}_t$.

Questa relazione ha una portata più generale del caso del punto materiale. Essa fornisce una regola per derivare qualunque vettore $\vec{A}$ in due riferimenti in rotazione relativa:

$$\left(\frac{d\vec{A}}{dt}\right)_S = \left(\frac{d\vec{A}}{dt}\right)_{S'} + \vec{\omega}\times\vec{A}.$$

Nel caso di semplice traslazione ($\vec{\omega} = \vec{0}$) si ritrova la **composizione galileiana delle velocità**, $\vec{v} = \vec{v}' + \vec{v}_{O'}$, familiare dall'esperienza quotidiana: se cammino a $1{,}5\ \mathrm{m/s}$ nel corridoio di un treno che viaggia a $30\ \mathrm{m/s}$, nel verso del moto, la mia velocità rispetto ai binari è $31{,}5\ \mathrm{m/s}$. Un esempio meno banale è il vento apparente percepito da un ciclista o da una barca a vela: la velocità del vento rispetto alla barca è la differenza vettoriale tra la velocità del vento rispetto all'acqua e quella della barca, e le vele vanno regolate in base a questo vento relativo, non a quello assoluto.

### 5.1.3 Accelerazione

Derivando ancora rispetto al tempo nel riferimento $S$ la relazione tra le velocità, e applicando nuovamente la regola di derivazione nei due riferimenti sia a $\vec{v}'$ sia a $\vec{r}'$, si ottiene il **teorema delle accelerazioni relative** (o **teorema di Coriolis**):

$$\vec{a} = \vec{a}' + \vec{a}_{O'} + \dot{\vec{\omega}}\times\vec{r}' + \vec{\omega}\times(\vec{\omega}\times\vec{r}') + 2\,\vec{\omega}\times\vec{v}'.$$

Conviene esaminare un termine alla volta.

- $\vec{a}'$ è l'**accelerazione relativa**, misurata dall'osservatore mobile.
- $\vec{a}_{O'}$ è l'accelerazione dell'origine del riferimento mobile.
- $\dot{\vec{\omega}}\times\vec{r}'$ è il termine dovuto alla variazione della velocità angolare (accelerazione angolare del riferimento); ha carattere tangenziale.
- $\vec{\omega}\times(\vec{\omega}\times\vec{r}')$ è l'**accelerazione centripeta**: diretta verso l'asse di rotazione, ha modulo $\omega^2 d$, dove $d$ è la distanza del punto dall'asse.
- $2\,\vec{\omega}\times\vec{v}'$ è l'**accelerazione di Coriolis** (o complementare), presente solo se il punto si muove rispetto al riferimento rotante.

I primi tre termini dopo $\vec{a}'$ formano l'**accelerazione di trascinamento** $\vec{a}_t$, cioè l'accelerazione che il punto avrebbe se fosse solidale con $S'$. La relazione finale si scrive quindi

$$\vec{a} = \vec{a}' + \vec{a}_t + \vec{a}_c, \qquad \vec{a}_c = 2\,\vec{\omega}\times\vec{v}'.$$

È importante notare che, a differenza della velocità, l'accelerazione assoluta *non* è semplicemente la somma di quella relativa e di quella di trascinamento: c'è un termine in più, quello di Coriolis. L'origine del fattore 2 è istruttiva: metà del termine nasce dalla rotazione del vettore velocità relativa (che, pur costante per l'osservatore mobile, ruota agli occhi di quello fisso), l'altra metà dal fatto che, spostandosi, il punto passa a zone del riferimento mobile con diversa velocità di trascinamento.

Un esempio illuminante è quello di una formica che cammina con velocità costante $v'$ lungo un raggio di un disco che ruota con velocità angolare costante $\omega$. Per la formica il moto è rettilineo uniforme, quindi $\vec{a}' = \vec{0}$. Per un osservatore fisso, però, la formica ha un'accelerazione centripeta $\omega^2 r$ diretta verso il centro e un'accelerazione di Coriolis di modulo $2\omega v'$ in direzione tangenziale. Quest'ultima corrisponde al fatto che, allontanandosi dal centro, la formica deve aumentare la propria velocità tangenziale assoluta, da $\omega r$ a $\omega(r + dr)$.

Nel caso di **traslazione** pura ($\vec{\omega} = \vec{0}$), la relazione si riduce a $\vec{a} = \vec{a}' + \vec{a}_{O'}$; se poi $S'$ trasla con velocità costante, $\vec{a}_{O'} = \vec{0}$ e $\vec{a} = \vec{a}'$: **l'accelerazione è la stessa nei due riferimenti**. Questa osservazione, banale nella forma, è il fondamento del principio di relatività galileiana che discuteremo nella sezione 5.2.

### Esercizio d'esempio

Una piattaforma circolare ruota in senso antiorario (vista dall'alto) con velocità angolare costante $\omega = 0{,}50\ \mathrm{rad/s}$ attorno a un asse verticale. Una persona cammina radialmente verso l'esterno con velocità relativa costante $v' = 1{,}2\ \mathrm{m/s}$. Calcolare, nell'istante in cui si trova a distanza $r' = 3{,}0\ \mathrm{m}$ dal centro, (a) la velocità assoluta e (b) l'accelerazione assoluta.

**Soluzione.** Usiamo assi solidali con la piattaforma: $\hat{u}_r$ radiale verso l'esterno, $\hat{u}_\theta$ tangenziale nel verso della rotazione, $\vec{\omega} = \omega\hat{k}$. L'origine è sull'asse, quindi $\vec{v}_{O'} = \vec{0}$, $\vec{a}_{O'} = \vec{0}$; inoltre $\dot{\vec{\omega}} = \vec{0}$.

(a) Velocità relativa: $\vec{v}' = 1{,}2\,\hat{u}_r\ \mathrm{m/s}$. Velocità di trascinamento: $\vec{\omega}\times\vec{r}' = \omega r'\,\hat{u}_\theta = 1{,}5\,\hat{u}_\theta\ \mathrm{m/s}$. Quindi

$$\vec{v} = (1{,}2\,\hat{u}_r + 1{,}5\,\hat{u}_\theta)\ \mathrm{m/s}, \qquad |\vec{v}| = \sqrt{1{,}44 + 2{,}25}\ \mathrm{m/s} \approx 1{,}92\ \mathrm{m/s}.$$

(b) $\vec{a}' = \vec{0}$. Accelerazione centripeta: $-\omega^2 r'\,\hat{u}_r = -0{,}25\cdot3{,}0\,\hat{u}_r = -0{,}75\,\hat{u}_r\ \mathrm{m/s^2}$. Accelerazione di Coriolis: $2\vec{\omega}\times\vec{v}' = 2\omega v'\,\hat{u}_\theta = 2\cdot0{,}50\cdot1{,}2\,\hat{u}_\theta = 1{,}2\,\hat{u}_\theta\ \mathrm{m/s^2}$. Quindi

$$\vec{a} = (-0{,}75\,\hat{u}_r + 1{,}2\,\hat{u}_\theta)\ \mathrm{m/s^2}, \qquad |\vec{a}| \approx 1{,}42\ \mathrm{m/s^2}.$$

Questa accelerazione deve essere fornita dall'attrito tra le scarpe e la piattaforma.

### Punti chiave

- Il moto di un riferimento mobile è descritto dal moto della sua origine e dalla sua velocità angolare $\vec{\omega}$.
- Posizioni: $\vec{r} = \vec{r}_{O'} + \vec{r}'$; in meccanica classica tempo e distanze sono gli stessi per tutti gli osservatori.
- Le formule di Poisson $d\hat{u}'/dt = \vec{\omega}\times\hat{u}'$ permettono di derivare i versori di un riferimento rotante.
- Velocità: $\vec{v} = \vec{v}' + \vec{v}_t$, con velocità di trascinamento $\vec{v}_t = \vec{v}_{O'} + \vec{\omega}\times\vec{r}'$.
- Accelerazione: $\vec{a} = \vec{a}' + \vec{a}_t + 2\vec{\omega}\times\vec{v}'$; il termine di Coriolis compare solo se il punto si muove nel riferimento rotante.
- L'accelerazione di trascinamento include il termine di $O'$, quello tangenziale $\dot{\vec{\omega}}\times\vec{r}'$ e quello centripeto.
- In traslazione uniforme le accelerazioni nei due riferimenti coincidono.

## 5.2 Dinamica relativa

### 5.2.1 Forze apparenti

Supponiamo che il riferimento $S$ sia inerziale. In esso vale il secondo principio della dinamica: $\vec{F} = m\vec{a}$, dove $\vec{F}$ è la risultante delle **forze reali**, cioè delle forze dovute a interazioni con altri corpi (peso, reazioni vincolari, tensioni, forze elastiche, attriti, forze elettromagnetiche). Sostituendo nell'equazione l'espressione dell'accelerazione assoluta ricavata nella sezione precedente si ha

$$\vec{F} = m\left(\vec{a}' + \vec{a}_t + \vec{a}_c\right).$$

Isolando a primo membro il termine $m\vec{a}'$, che è ciò che l'osservatore mobile misurerebbe come "massa per accelerazione", si ottiene

$$m\vec{a}' = \vec{F} - m\vec{a}_t - m\vec{a}_c.$$

L'osservatore in $S'$ può dunque continuare a utilizzare una legge formalmente identica a quella di Newton, a condizione di aggiungere alle forze reali due termini:

$$\vec{F}_t = -m\vec{a}_t, \qquad \vec{F}_c = -m\vec{a}_c = -2m\,\vec{\omega}\times\vec{v}'.$$

Questi termini si chiamano **forze apparenti** (o fittizie, o inerziali): rispettivamente **forza di trascinamento** e **forza di Coriolis**. La forza di trascinamento, a sua volta, si scompone in tre contributi:

$$\vec{F}_t = -m\vec{a}_{O'} - m\,\dot{\vec{\omega}}\times\vec{r}' - m\,\vec{\omega}\times(\vec{\omega}\times\vec{r}').$$

Il primo è la forza d'inerzia dovuta all'accelerazione dell'origine, già incontrata nella sezione 4.1; il secondo, detto talvolta **forza di Eulero**, compare solo se la velocità angolare del riferimento varia nel tempo; il terzo è la **forza centrifuga**, diretta radialmente in verso uscente dall'asse di rotazione, di modulo $m\omega^2 d$.

Le forze apparenti hanno caratteristiche che le distinguono nettamente dalle forze reali. Primo, non derivano da un'interazione con un altro corpo, quindi non ammettono una reazione nel senso del terzo principio. Secondo, sono tutte **proporzionali alla massa** del corpo su cui agiscono, esattamente come il peso. Terzo, dipendono dal riferimento: scompaiono se si torna a descrivere il moto in un riferimento inerziale. Per un osservatore mobile esse sono comunque perfettamente "reali" nel senso operativo: un dinamometro a molla in un riferimento accelerato ne misura gli effetti, e una persona su una giostra ne avverte chiaramente la spinta.

La forza di Coriolis merita qualche commento. Essendo perpendicolare alla velocità relativa, non compie lavoro nel riferimento mobile: modifica la direzione del moto, non il modulo della velocità relativa. Il suo effetto è deviare i corpi in movimento verso destra (nel caso di rotazione antioraria vista dall'alto, come la Terra vista dal polo nord) o verso sinistra (rotazione oraria). Sulla Terra, con $\omega_T = 7{,}29\times10^{-5}\ \mathrm{rad/s}$, la forza di Coriolis è piccola per i moti di uso quotidiano, ma diventa dominante su grandi scale spaziali e temporali: determina la circolazione antioraria dei cicloni nell'emisfero nord e oraria nell'emisfero sud, la deviazione delle correnti oceaniche, la deriva dei proiettili d'artiglieria a lunga gittata. Il **pendolo di Foucault** (1851) rese visibile la rotazione terrestre proprio attraverso l'effetto di Coriolis: il piano di oscillazione di un lungo pendolo ruota lentamente, con un periodo di $24\ \mathrm{h}/\sin\lambda$ alla latitudine $\lambda$, circa 32 ore a Milano. Contrariamente a una diffusa leggenda, invece, la forza di Coriolis è del tutto trascurabile nel determinare il verso del vortice nello scarico di un lavandino, dominato dalle condizioni iniziali dell'acqua e dalla forma del recipiente.

### 5.2.2 Sistemi inerziali

Un **sistema di riferimento inerziale** è un riferimento in cui vale il primo principio della dinamica: un corpo non soggetto a forze reali permane nel suo stato di quiete o di moto rettilineo uniforme. In un riferimento inerziale le forze apparenti sono nulle e il secondo principio vale nella forma $\vec{F} = m\vec{a}$.

Dalle formule precedenti segue subito una proprietà fondamentale: se $S$ è inerziale, un riferimento $S'$ è anch'esso inerziale **se e solo se** trasla rispetto a $S$ con velocità costante, cioè se $\vec{\omega} = \vec{0}$ e $\vec{a}_{O'} = \vec{0}$. In questo caso infatti $\vec{a}_t = \vec{0}$, $\vec{a}_c = \vec{0}$ e quindi $\vec{a}' = \vec{a}$: le due accelerazioni coincidono e le leggi del moto sono identiche. Ne segue che esiste un'intera famiglia di riferimenti inerziali, tutti in moto rettilineo uniforme gli uni rispetto agli altri.

Le relazioni tra le coordinate di due riferimenti inerziali con assi paralleli, con $S'$ in moto con velocità $\vec{V}$ costante e origini coincidenti a $t = 0$, sono le **trasformazioni di Galileo**:

$$\vec{r}' = \vec{r} - \vec{V}t, \qquad t' = t.$$

Da esse discende la composizione delle velocità $\vec{v}' = \vec{v} - \vec{V}$ e l'invarianza delle accelerazioni $\vec{a}' = \vec{a}$. Poiché anche le forze reali (che dipendono da distanze relative e velocità relative tra corpi) e le masse sono invarianti, l'equazione $\vec{F} = m\vec{a}$ ha la stessa forma in tutti i riferimenti inerziali. Questo è il **principio di relatività galileiana**: le leggi della meccanica sono le stesse in tutti i riferimenti inerziali, e nessun esperimento meccanico eseguito all'interno di un riferimento permette di stabilire se esso è in quiete o in moto rettilineo uniforme. Galileo lo illustrò con la celebre immagine della "gran nave": chiusi sottocoperta, i passeggeri osservano farfalle, pesci e gocce d'acqua comportarsi esattamente allo stesso modo sia a nave ferma sia a nave in moto uniforme.

Resta il problema di trovare, in pratica, un riferimento inerziale. A rigore, nessun riferimento legato a un corpo materiale lo è esattamente, perché tutti i corpi sono soggetti a qualche accelerazione. Il riferimento **terrestre** (o del laboratorio) è non inerziale a causa della rotazione della Terra su se stessa (accelerazione centripeta all'equatore $\approx 3{,}4\times10^{-2}\ \mathrm{m/s^2}$) e della rivoluzione intorno al Sole ($\approx 6\times10^{-3}\ \mathrm{m/s^2}$). Il riferimento **geocentrico**, con origine nel centro della Terra e assi diretti verso stelle fisse, elimina la rotazione ma non la rivoluzione. Il riferimento **eliocentrico** (o di Copernico), con origine nel centro di massa del sistema solare e assi verso stelle lontane, ha un'accelerazione residua dovuta al moto attorno al centro della Galassia, dell'ordine di $10^{-10}\ \mathrm{m/s^2}$: è inerziale con ottima approssimazione per qualunque problema di meccanica del sistema solare. La scelta del riferimento "abbastanza inerziale" dipende quindi dalla precisione richiesta e dalla durata e dall'estensione del fenomeno studiato.

### 5.2.3 Sistemi non inerziali

Un riferimento che accelera o ruota rispetto a un riferimento inerziale è **non inerziale**. Nei riferimenti non inerziali il primo principio non vale: un corpo libero da forze reali può accelerare. Per descrivere correttamente la dinamica in tali riferimenti si scrive

$$m\vec{a}' = \vec{F} + \vec{F}_t + \vec{F}_c.$$

Vediamo i casi più significativi.

**Riferimento in traslazione accelerata.** Se $\vec{\omega} = \vec{0}$, l'unica forza apparente è $-m\vec{a}_{O'}$, uniforme nello spazio. Essa si comporta come un "campo gravitazionale" aggiuntivo, e infatti si può definire una gravità efficace $\vec{g}_{eff} = \vec{g} - \vec{a}_{O'}$. In un ascensore in caduta libera $\vec{a}_{O'} = \vec{g}$ e $\vec{g}_{eff} = \vec{0}$: gli oggetti fluttuano, come nella stazione spaziale. È proprio questa equivalenza tra effetti di un'accelerazione e di un campo gravitazionale che Einstein elevò a principio fisico.

**Riferimento in rotazione uniforme.** Se $O'$ è fermo e $\vec{\omega}$ è costante, le forze apparenti sono la forza centrifuga e la forza di Coriolis. Un corpo fermo nel riferimento rotante subisce solo la forza centrifuga; un corpo in moto anche quella di Coriolis. Un esempio istruttivo: su una piattaforma rotante, una palla lanciata in linea retta (nel riferimento inerziale) appare all'osservatore solidale come deviata lungo una traiettoria curva, come se una forza laterale la spingesse. La descrizione nel riferimento inerziale è più semplice (moto rettilineo uniforme), ma quella nel riferimento rotante è quella che sperimenta chi sta sulla piattaforma.

**Il riferimento terrestre.** Per un corpo in quiete sulla superficie terrestre la forza centrifuga si combina con la forza gravitazionale per dare il peso apparente, come già discusso nella sezione 4.2. Per un corpo in moto, si aggiunge la forza di Coriolis. Un esempio quantitativo: un corpo lasciato cadere da un'altezza $h$ all'equatore non cade esattamente lungo la verticale, ma viene deviato verso est di una quantità $\delta = \tfrac{1}{3}\omega_T g\,t^3\cos\lambda$, con $t = \sqrt{2h/g}$. Per $h = 100\ \mathrm{m}$ si ottengono circa $2\ \mathrm{cm}$: una deviazione piccola ma misurabile, effettivamente osservata in esperimenti condotti in pozzi minerari nell'Ottocento.

In conclusione, la scelta tra descrizione inerziale e non inerziale è una questione di convenienza. La fisica non cambia: cambia la contabilità delle forze. Le regole d'oro sono due: nel riferimento inerziale si usano solo forze reali; nel riferimento non inerziale si aggiungono tutte e sole le forze apparenti pertinenti, senza dimenticarne nessuna e senza introdurne di spurie.

### Esercizio d'esempio

Un'automobile di massa $m = 1200\ \mathrm{kg}$ procede verso nord a velocità $v' = 30\ \mathrm{m/s}$ su una strada rettilinea a Milano (latitudine $\lambda = 45{,}5^\circ$). Calcolare modulo, direzione e verso della forza di Coriolis dovuta alla rotazione terrestre e confrontarla con il peso ($\omega_T = 7{,}29\times10^{-5}\ \mathrm{rad/s}$, $g = 9{,}81\ \mathrm{m/s^2}$).

**Soluzione.** Usiamo assi locali: $\hat{x}$ verso est, $\hat{y}$ verso nord, $\hat{z}$ verso l'alto. Il vettore $\vec{\omega}_T$, parallelo all'asse terrestre, ha componenti $\vec{\omega}_T = \omega_T(0,\ \cos\lambda,\ \sin\lambda)$. La velocità è $\vec{v}' = (0,\ v',\ 0)$. Il prodotto vettoriale vale

$$\vec{\omega}_T\times\vec{v}' = \omega_T v'\,(\cos\lambda\cdot0 - \sin\lambda\cdot1,\ 0,\ 0) = -\omega_T v'\sin\lambda\ \hat{x}.$$

Quindi

$$\vec{F}_c = -2m\,\vec{\omega}_T\times\vec{v}' = 2m\omega_T v'\sin\lambda\ \hat{x}.$$

Numericamente:

$$F_c = 2\cdot1200\cdot7{,}29\times10^{-5}\cdot30\cdot\sin45{,}5^\circ\ \mathrm{N} = 5{,}25\cdot0{,}713\ \mathrm{N} \approx 3{,}7\ \mathrm{N},$$

diretta verso est, cioè verso destra rispetto al verso di marcia (come previsto nell'emisfero nord). Il rapporto con il peso, $mg = 1{,}18\times10^4\ \mathrm{N}$, è circa $3\times10^{-4}$: un effetto del tutto trascurabile per la guida, ma che sommato su migliaia di chilometri e su masse d'aria enormi governa la meteorologia.

### Punti chiave

- In un riferimento non inerziale vale $m\vec{a}' = \vec{F} + \vec{F}_t + \vec{F}_c$, con forze apparenti $\vec{F}_t = -m\vec{a}_t$ e $\vec{F}_c = -2m\vec{\omega}\times\vec{v}'$.
- La forza di trascinamento comprende la forza d'inerzia di traslazione, la forza di Eulero e la forza centrifuga $-m\vec{\omega}\times(\vec{\omega}\times\vec{r}')$.
- Le forze apparenti sono proporzionali alla massa, non hanno reazione e dipendono dal riferimento.
- La forza di Coriolis è perpendicolare alla velocità relativa e non compie lavoro; sulla Terra devia i moti verso destra nell'emisfero nord.
- I riferimenti inerziali sono tutti in moto rettilineo uniforme gli uni rispetto agli altri e sono collegati dalle trasformazioni di Galileo.
- Principio di relatività galileiana: le leggi della meccanica hanno la stessa forma in tutti i riferimenti inerziali.
- Il riferimento terrestre è approssimativamente inerziale; quello eliocentrico lo è con ottima approssimazione.

## 5.3 Statica relativa

### 5.3.1 Equilibrio in un riferimento non inerziale

La **statica relativa** studia le condizioni sotto le quali un corpo resta in quiete rispetto a un riferimento non inerziale. Si tratta di un problema di grande interesse pratico: un carico fermo sul pianale di un camion che frena, un passeggero seduto su una giostra, l'acqua in un secchio che ruota, un componente montato su un rotore, un regolatore centrifugo, un pendolo appeso nel vagone di un treno in curva. In tutti questi casi l'osservatore solidale con il riferimento mobile vede il corpo fermo, e vuole sapere quali forze reali (tensioni, reazioni, attriti) sono necessarie a mantenerlo in quella condizione.

Imponendo nella legge della dinamica relativa che il corpo sia in quiete rispetto a $S'$, cioè $\vec{v}' = \vec{0}$ e $\vec{a}' = \vec{0}$, si ottiene la **condizione di equilibrio relativo**:

$$\vec{F} + \vec{F}_t = \vec{0}.$$

La forza di Coriolis non compare, perché è proporzionale alla velocità relativa, che è nulla. Rimane la forza di trascinamento, che per un corpo in quiete relativa si riduce a

$$\vec{F}_t = -m\vec{a}_{O'} - m\,\dot{\vec{\omega}}\times\vec{r}' - m\,\vec{\omega}\times(\vec{\omega}\times\vec{r}').$$

Il problema di statica relativa ha quindi la stessa struttura di un problema di statica ordinaria, con la sola differenza che, alle forze reali, si aggiungono le forze di trascinamento, calcolate nella posizione di equilibrio del corpo. Questo è in sostanza il principio di d'Alembert applicato in forma sistematica. È importante tenere presente che l'equilibrio relativo non è un equilibrio nel senso assoluto: nel riferimento inerziale il corpo è accelerato, e la condizione $\vec{F} + \vec{F}_t = \vec{0}$ equivale semplicemente a $\vec{F} = m\vec{a}_t$, cioè alla richiesta che le forze reali forniscano esattamente l'accelerazione di trascinamento.

### 5.3.2 Equilibrio in un riferimento traslante

Nel caso di traslazione con accelerazione $\vec{a}_{O'}$, la condizione di equilibrio diventa

$$\vec{F} - m\vec{a}_{O'} = \vec{0}.$$

Se tra le forze reali c'è il peso, conviene raggrupparlo con la forza d'inerzia definendo il **campo gravitazionale efficace** $\vec{g}_{eff} = \vec{g} - \vec{a}_{O'}$. Il problema diventa allora identico a un problema di statica in un campo gravitazionale uniforme di intensità e direzione diverse da quelle del campo reale. Tutte le conclusioni della statica ordinaria valgono con $\vec{g}$ sostituito da $\vec{g}_{eff}$.

Gli esempi sono innumerevoli. Un filo a piombo nel vagone di un treno che accelera si dispone lungo $\vec{g}_{eff}$, inclinato all'indietro, come visto nell'esercizio della sezione 4.1: è il principio di un semplice **accelerometro a pendolo**. La superficie libera di un liquido in un serbatoio accelerato orizzontalmente si dispone perpendicolarmente a $\vec{g}_{eff}$, e quindi si inclina rispetto all'orizzontale di un angolo $\theta$ con $\tan\theta = a/g$: è il motivo per cui le autocisterne sono dotate di paratie interne, che limitano lo spostamento del liquido in frenata. Una cassa sul pianale di un camion che frena con decelerazione $a$ resta ferma rispetto al camion solo se l'attrito statico è sufficiente a fornire la forza $ma$: la condizione è $\mu_s mg \geq ma$, cioè $a \leq \mu_s g$. Oltre questo valore la cassa scivola in avanti, ed è per questo che i carichi vanno sempre fissati con cinghie.

### 5.3.3 Equilibrio in un riferimento rotante

Se il riferimento ruota con velocità angolare costante attorno a un asse fisso, la forza di trascinamento si riduce alla **forza centrifuga**, $\vec{F}_{cf} = m\omega^2 d\,\hat{u}_d$, diretta lungo la perpendicolare all'asse e uscente da esso, con $d$ distanza del corpo dall'asse. La condizione di equilibrio relativo è

$$\vec{F} + m\omega^2 d\,\hat{u}_d = \vec{0}.$$

**Il regolatore centrifugo (o pendolo conico).** Una massa $m$ è appesa a un filo di lunghezza $\ell$ il cui estremo superiore è fissato su un asse verticale che ruota con velocità angolare $\omega$. Nel riferimento rotante la massa è in quiete, a un angolo $\theta$ dalla verticale, sotto l'azione del peso, della tensione e della forza centrifuga, con $d = \ell\sin\theta$. Le equazioni di equilibrio sono

$$T\cos\theta = mg, \qquad T\sin\theta = m\omega^2\ell\sin\theta.$$

Se $\sin\theta \neq 0$, dalla seconda si ricava $T = m\omega^2\ell$, e dalla prima

$$\cos\theta = \frac{g}{\omega^2\ell}.$$

Questa soluzione esiste solo se $\omega^2 > g/\ell$: al di sotto di questa velocità angolare critica l'unica posizione di equilibrio è quella verticale ($\theta = 0$). Al di sopra, la massa si solleva, e tanto più quanto maggiore è $\omega$. Il **regolatore di Watt**, inventato nel 1788 per le macchine a vapore, sfruttava esattamente questo comportamento: due sfere rotanti, sollevandosi all'aumentare della velocità, azionavano tramite leveraggi una valvola che riduceva l'afflusso di vapore, stabilizzando la velocità del motore. È uno dei primi esempi storici di controllo automatico in retroazione.

**Il liquido in rotazione.** Un recipiente cilindrico contenente un liquido ruota con velocità angolare costante $\omega$ attorno al proprio asse verticale. A regime il liquido è in quiete rispetto al recipiente. Ogni elemento di liquido sente il peso e la forza centrifuga, e la superficie libera si dispone perpendicolarmente alla risultante, cioè al campo efficace $\vec{g}_{eff} = -g\hat{k} + \omega^2 r\,\hat{u}_r$. La pendenza della superficie a distanza $r$ dall'asse è dunque $dz/dr = \omega^2 r/g$, e integrando si ottiene

$$z(r) = z_0 + \frac{\omega^2 r^2}{2g}:$$

la superficie libera è un **paraboloide di rotazione**. Questo effetto è sfruttato nei **telescopi a specchio liquido**, in cui uno strato di mercurio posto in rotazione assume naturalmente la forma parabolica ideale per focalizzare la luce, e nella produzione di specchi parabolici per colata centrifuga.

**Curve sopraelevate.** Un veicolo che percorre una curva di raggio $R$ a velocità costante $v$ è in quiete rispetto a un riferimento che ruota con $\omega = v/R$. Se la strada è inclinata di un angolo $\alpha$ verso l'interno, si può chiedere quale velocità permette di percorrere la curva senza alcun bisogno di attrito laterale. Nel riferimento rotante la reazione normale deve equilibrare peso e forza centrifuga; si ottiene $\tan\alpha = v^2/(gR)$. Questa **velocità di progetto** è quella per cui le piste ciclistiche, le autostrade e le linee ferroviarie ad alta velocità vengono sopraelevate: per un treno che percorre a $300\ \mathrm{km/h}$ curve con raggio di diversi chilometri, la sopraelevazione della rotaia esterna compensa buona parte della forza centrifuga, migliorando sicurezza e comfort.

### 5.3.4 Stabilità dell'equilibrio relativo

Come nella statica ordinaria, le posizioni di equilibrio relativo possono essere **stabili** o **instabili**. Nel caso del pendolo conico, per $\omega^2 < g/\ell$ la posizione verticale è stabile; per $\omega^2 > g/\ell$ essa diventa instabile, e la posizione stabile è quella inclinata. Il passaggio da un tipo di equilibrio all'altro al variare di un parametro si chiama **biforcazione**, ed è un fenomeno comune in meccanica dei rotori. Per analizzare la stabilità nei riferimenti rotanti si può associare alla forza centrifuga un'energia potenziale efficace $U_{cf} = -\tfrac{1}{2}m\omega^2 d^2$ e studiare i minimi dell'energia potenziale totale. Occorre però prudenza: la forza di Coriolis, pur non entrando nella condizione di equilibrio, interviene nelle piccole oscillazioni attorno a essa, e può in certi casi stabilizzare equilibri che l'analisi della sola energia potenziale classificherebbe come instabili. Un esempio celebre è la stabilità dei punti lagrangiani L4 e L5 nel problema dei tre corpi, dove si trovano gli asteroidi troiani di Giove.

### Esercizio d'esempio

Un regolatore centrifugo è costituito da una sfera di massa $m = 0{,}30\ \mathrm{kg}$ appesa a un'asta rigida di massa trascurabile e lunghezza $\ell = 0{,}25\ \mathrm{m}$, incernierata in alto a un albero verticale. L'albero ruota a $n = 90\ \mathrm{giri/min}$. Determinare l'angolo di equilibrio relativo e la forza nell'asta ($g = 9{,}81\ \mathrm{m/s^2}$).

**Soluzione.** La velocità angolare è

$$\omega = \frac{2\pi n}{60} = \frac{2\pi\cdot90}{60}\ \mathrm{rad/s} = 9{,}42\ \mathrm{rad/s}.$$

Verifichiamo che si superi la soglia: $g/\ell = 39{,}2\ \mathrm{s^{-2}}$ mentre $\omega^2 = 88{,}8\ \mathrm{s^{-2}}$, quindi esiste l'equilibrio inclinato. Dalla condizione di equilibrio relativo:

$$\cos\theta = \frac{g}{\omega^2\ell} = \frac{9{,}81}{88{,}8\cdot0{,}25} = 0{,}442 \quad\Rightarrow\quad \theta \approx 63{,}8^\circ.$$

La forza nell'asta (trazione) vale

$$T = m\omega^2\ell = 0{,}30\cdot88{,}8\cdot0{,}25\ \mathrm{N} \approx 6{,}66\ \mathrm{N},$$

circa 2,3 volte il peso della sfera ($2{,}94\ \mathrm{N}$). La distanza dall'asse è $d = \ell\sin\theta = 0{,}224\ \mathrm{m}$ e la forza centrifuga $m\omega^2 d \approx 5{,}97\ \mathrm{N}$.

### Punti chiave

- La statica relativa studia la quiete di un corpo rispetto a un riferimento non inerziale.
- La condizione di equilibrio relativo è $\vec{F} + \vec{F}_t = \vec{0}$; la forza di Coriolis non interviene perché $\vec{v}' = \vec{0}$.
- In un riferimento traslante conviene introdurre il campo efficace $\vec{g}_{eff} = \vec{g} - \vec{a}_{O'}$.
- In un riferimento rotante uniforme l'unica forza apparente in quiete relativa è la forza centrifuga $m\omega^2 d$.
- Il pendolo conico ha equilibrio inclinato solo per $\omega^2 > g/\ell$, con $\cos\theta = g/(\omega^2\ell)$.
- Un liquido in rotazione assume una superficie a paraboloide $z = z_0 + \omega^2 r^2/(2g)$.
- L'equilibrio relativo equivale, nel riferimento inerziale, a $\vec{F} = m\vec{a}_t$.
