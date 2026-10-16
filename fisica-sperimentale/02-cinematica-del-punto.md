# Capitolo 2 — Cinematica del punto

La **cinematica** è la parte della meccanica che descrive il moto dei corpi senza occuparsi delle cause che lo producono: risponde alla domanda "come si muove un corpo?" e non alla domanda "perché si muove così?", che sarà invece oggetto della dinamica. In questo capitolo il corpo in moto è schematizzato come **punto materiale**, cioè un oggetto di cui si trascurano dimensioni, forma e orientazione, conservando soltanto la posizione. Il modello è adeguato quando le dimensioni del corpo sono piccole rispetto alle distanze percorse, oppure quando interessa solo il moto di un punto rappresentativo (come il centro di massa). Si procede in due passi: prima si studia il moto lungo una traiettoria nota con grandezze scalari (cinematica scalare), introducendo i moti fondamentali come la caduta dei gravi e il moto armonico; poi si generalizza alla descrizione vettoriale nello spazio tridimensionale, che permette di trattare qualsiasi traiettoria e di introdurre le componenti tangenziale e normale dell'accelerazione.

## 2.1 Cinematica scalare

Nella **cinematica scalare** si considera un punto che si muove lungo una traiettoria nota, che per semplicità può essere una retta (moto **rettilineo**) oppure una curva qualsiasi percorsa e misurata tramite la sua ascissa curvilinea. In questo caso la posizione è individuata da un solo numero reale, funzione del tempo, e velocità e accelerazione sono anch'esse grandezze scalari, dotate di segno. Questa descrizione, pur limitata, contiene già tutti gli strumenti concettuali (derivate e integrali rispetto al tempo, condizioni iniziali, interpretazione grafica dei diagrammi orari) che verranno poi estesi al caso vettoriale.

### 2.1.1 Sistema di riferimento

Per descrivere il moto occorre prima di tutto stabilire **rispetto a che cosa** si misura la posizione. Il moto è infatti un concetto relativo: un passeggero seduto in un treno è fermo rispetto al vagone ma in moto rispetto ai binari. Un **sistema di riferimento** è costituito da un corpo rigido (o un insieme di punti a distanze reciproche fisse) rispetto al quale si misurano le posizioni, da un **sistema di coordinate** solidale con esso e da un **orologio** per misurare il tempo. Nella meccanica classica si assume che il tempo sia assoluto, cioè scorra allo stesso modo per tutti gli osservatori, e che le lunghezze non dipendano dallo stato di moto; queste ipotesi cadono solo a velocità prossime a quella della luce.

Nel caso del moto lungo una retta il sistema di coordinate si riduce a un **asse orientato**: si sceglie un punto $O$ come **origine**, un verso positivo e un'unità di lunghezza. Ogni punto della retta è allora individuato da un numero reale $x$, positivo o negativo a seconda che il punto si trovi dalla parte positiva o negativa rispetto a $O$. Se la traiettoria è curva ma nota (una rotaia, una pista circolare), si usa l'**ascissa curvilinea** $s$, cioè la lunghezza dell'arco misurata lungo la traiettoria a partire da un'origine, con un verso di percorrenza fissato. Anche l'origine dei tempi $t = 0$ è una scelta arbitraria, che conviene far coincidere con un istante significativo, ad esempio l'inizio del moto.

La scelta del sistema di riferimento è libera, e un'opportuna scelta può semplificare enormemente la descrizione. Per studiare un sasso lanciato verso l'alto è naturale orientare l'asse verticalmente verso l'alto con origine nel punto di lancio; per un'auto che frena conviene un asse orizzontale nel verso del moto con origine nel punto di inizio della frenata. È però essenziale mantenere la stessa scelta in tutto lo svolgimento di un problema e assegnare coerentemente i segni a tutte le grandezze.

### 2.1.2 Posizione

La **posizione** del punto è descritta dalla funzione $x(t)$, detta **legge oraria** o equazione del moto, che associa a ogni istante $t$ la coordinata del punto. Nel SI la posizione si misura in metri. Il grafico di $x$ in funzione di $t$ si chiama **diagramma orario** e non va confuso con la traiettoria: anche per un moto rettilineo il diagramma orario può essere una curva qualsiasi. Fisicamente la legge oraria deve essere una funzione continua (il punto non può "saltare" da una posizione a un'altra) e, salvo idealizzazioni come gli urti, derivabile almeno due volte.

Tra due istanti $t_1$ e $t_2$ si definisce lo **spostamento** $\Delta x = x(t_2) - x(t_1)$, grandezza dotata di segno che dipende solo dalle posizioni iniziale e finale. Lo spostamento va distinto dalla **distanza percorsa**, cioè la lunghezza effettiva del tragitto, che è sempre non negativa e che coincide con $|\Delta x|$ solo se il punto non inverte il verso del moto nell'intervallo. Un corridore che percorre un giro completo di pista ha spostamento nullo ma distanza percorsa di $400\ \mathrm{m}$.

### 2.1.3 Velocità

La **velocità media** nell'intervallo $[t_1, t_2]$ è il rapporto tra lo spostamento e la durata dell'intervallo:

$$v_m = \frac{\Delta x}{\Delta t} = \frac{x(t_2) - x(t_1)}{t_2 - t_1}.$$

Graficamente è la pendenza della retta secante al diagramma orario tra i due punti. La velocità media fornisce un'informazione globale ma perde i dettagli: un'auto che percorre $100\ \mathrm{km}$ in un'ora ha velocità media $100\ \mathrm{km/h}$, sia che abbia viaggiato a velocità costante, sia che si sia fermata a metà strada recuperando poi il tempo perso. Per descrivere lo stato di moto in un singolo istante si fa tendere a zero l'intervallo e si definisce la **velocità istantanea**

$$v(t) = \lim_{\Delta t\to0}\frac{x(t+\Delta t)-x(t)}{\Delta t} = \frac{dx}{dt} = \dot{x}.$$

La velocità istantanea è la derivata della legge oraria e, graficamente, la pendenza della retta tangente al diagramma orario. Il suo segno indica il verso del moto: positiva se il punto si muove nel verso dell'asse, negativa nel verso opposto. Il suo modulo $|v|$, chiamato talvolta **celerità**, è ciò che indica il tachimetro di un veicolo. L'unità SI è il $\mathrm{m/s}$; nell'uso comune si incontra il $\mathrm{km/h}$, con $1\ \mathrm{m/s} = 3{,}6\ \mathrm{km/h}$.

Il problema inverso, ricavare la posizione nota la velocità, si risolve per integrazione:

$$x(t) = x_0 + \int_{t_0}^{t} v(t')\,dt',$$

dove $x_0 = x(t_0)$ è la **condizione iniziale**. Graficamente lo spostamento è l'area con segno sottesa al grafico della velocità in funzione del tempo. Il caso più semplice è il **moto rettilineo uniforme**, con $v$ costante: $x(t) = x_0 + v\,(t - t_0)$, il cui diagramma orario è una retta.

### 2.1.4 Accelerazione

Analogamente si definisce l'**accelerazione media** $a_m = \Delta v/\Delta t$ e l'**accelerazione istantanea**, derivata della velocità e quindi derivata seconda della posizione:

$$a(t) = \frac{dv}{dt} = \frac{d^2x}{dt^2} = \ddot{x}.$$

L'unità SI è il $\mathrm{m/s^2}$. Il segno dell'accelerazione non va confuso con il concetto di "accelerare" o "rallentare" del linguaggio comune: il punto aumenta il modulo della velocità quando $v$ e $a$ hanno lo stesso segno, lo diminuisce quando hanno segno opposto. Un'auto che procede nel verso negativo dell'asse e frena ha accelerazione positiva.

Dall'accelerazione si risale alla velocità per integrazione, $v(t) = v_0 + \int_{t_0}^{t} a(t')\,dt'$. Se l'accelerazione è costante si ha il **moto uniformemente accelerato**:

$$v(t) = v_0 + a\,t, \qquad x(t) = x_0 + v_0\,t + \tfrac12 a\,t^2,$$

avendo posto $t_0 = 0$. Eliminando il tempo tra le due relazioni si ricava una formula molto utile che lega direttamente velocità e posizione:

$$v^2 = v_0^2 + 2a\,(x - x_0).$$

Un'ulteriore relazione utile si ottiene dalla regola della catena, $a = \frac{dv}{dt} = \frac{dv}{dx}\frac{dx}{dt} = v\frac{dv}{dx}$, che permette di trattare i casi in cui l'accelerazione è nota in funzione della posizione anziché del tempo. In generale la conoscenza della funzione $a(t)$ e delle due condizioni iniziali $x_0$ e $v_0$ determina completamente il moto: è questa la struttura che ritroveremo nel problema fondamentale della dinamica.

### 2.1.5 Moto del grave

Il **moto del grave** è il moto di un corpo soggetto soltanto all'attrazione gravitazionale terrestre, trascurando la resistenza dell'aria. Galileo scoprì sperimentalmente, con i suoi esperimenti sui piani inclinati, che in queste condizioni tutti i corpi cadono con la stessa accelerazione costante, indipendente dalla massa e dalla composizione, diretta verso il basso, detta **accelerazione di gravità** $g$. Il suo valore varia leggermente con la latitudine e la quota; il valore standard è $g = 9{,}806\,65\ \mathrm{m/s^2}$, e nei problemi si usa di solito $g \simeq 9{,}81\ \mathrm{m/s^2}$. L'ipotesi di $g$ costante è valida se le variazioni di quota sono piccole rispetto al raggio terrestre ($R_T \simeq 6{,}37\times10^{6}\ \mathrm{m}$).

Orientando l'asse $z$ verticalmente verso l'alto, l'accelerazione vale $a = -g$ e il moto è uniformemente accelerato:

$$v(t) = v_0 - g\,t, \qquad z(t) = z_0 + v_0\,t - \tfrac12 g\,t^2.$$

Per un corpo lanciato verso l'alto con velocità $v_0 > 0$ dalla quota $z_0 = 0$, la velocità si annulla all'istante $t_{\max} = v_0/g$, in corrispondenza della **quota massima**

$$h_{\max} = \frac{v_0^2}{2g},$$

che si ricava anche direttamente da $v^2 = v_0^2 - 2g z$ ponendo $v = 0$. Il moto è simmetrico: il corpo impiega lo stesso tempo a salire e a scendere e ripassa per la quota di lancio con velocità $-v_0$. Per un corpo lasciato cadere da fermo da un'altezza $h$, il tempo di caduta e la velocità all'arrivo al suolo sono

$$t_c = \sqrt{\frac{2h}{g}}, \qquad |v_f| = \sqrt{2gh}.$$

Nella realtà la resistenza dell'aria modifica sensibilmente questi risultati per corpi leggeri o con grande superficie (un foglio di carta, una piuma) e per velocità elevate; l'esperimento della piuma e del martello lasciati cadere sulla Luna durante la missione Apollo 15 ha mostrato in modo spettacolare che in assenza di atmosfera essi cadono insieme. La dipendenza della resistenza dalla velocità e la conseguente **velocità limite** verranno studiate nella dinamica.

### 2.1.6 Moto armonico

Il **moto armonico** è il moto di un punto la cui legge oraria è una funzione sinusoidale del tempo:

$$x(t) = A\cos(\omega t + \varphi).$$

La costante $A > 0$ è l'**ampiezza**, cioè il massimo spostamento dalla posizione di equilibrio $x = 0$; $\omega$ è la **pulsazione** (o frequenza angolare), misurata in $\mathrm{rad/s}$; l'argomento $\omega t + \varphi$ è la **fase** e $\varphi$ la **fase iniziale**. Il moto è periodico con **periodo** $T = 2\pi/\omega$ e **frequenza** $f = 1/T = \omega/2\pi$, misurata in hertz ($1\ \mathrm{Hz} = 1\ \mathrm{s^{-1}}$). Derivando si ottengono velocità e accelerazione:

$$v(t) = -A\omega\sin(\omega t+\varphi), \qquad a(t) = -A\omega^2\cos(\omega t+\varphi) = -\omega^2 x(t).$$

La relazione $a = -\omega^2 x$ è la proprietà caratteristica del moto armonico: l'accelerazione è proporzionale allo spostamento e di verso opposto, cioè tende sempre a riportare il punto verso l'equilibrio. Essa può essere scritta come **equazione differenziale del moto armonico**

$$\ddot{x} + \omega^2 x = 0,$$

la cui soluzione generale è proprio la legge sinusoidale, con $A$ e $\varphi$ determinate dalle condizioni iniziali: $A = \sqrt{x_0^2 + (v_0/\omega)^2}$ e $\tan\varphi = -v_0/(\omega x_0)$. La velocità è massima in modulo, $v_{\max} = A\omega$, quando il punto passa per l'equilibrio, ed è nulla negli estremi $x = \pm A$; l'accelerazione, al contrario, è nulla al centro e massima, $a_{\max} = A\omega^2$, agli estremi. Velocità e posizione sono sfasate di un quarto di periodo, accelerazione e posizione sono in opposizione di fase.

Il moto armonico ha un'importanza enorme in fisica e in ingegneria: descrive una massa attaccata a una molla, le piccole oscillazioni di un pendolo, le vibrazioni di strutture e macchine, la corrente in un circuito oscillante, e più in generale il comportamento di qualunque sistema perturbato di poco da una posizione di equilibrio stabile. Esiste inoltre un'interpretazione geometrica utile: il moto armonico è la **proiezione** su un diametro di un moto circolare uniforme di raggio $A$ e velocità angolare $\omega$. Questa corrispondenza spiega perché la pulsazione si misuri in radianti al secondo e sarà ripresa nella cinematica vettoriale.

### Esercizio d'esempio

**Testo.** Una pallina viene lanciata verticalmente verso l'alto con velocità $v_0 = 14{,}0\ \mathrm{m/s}$ dal bordo di un terrazzo alto $h = 20{,}0\ \mathrm{m}$ rispetto al suolo; ricadendo, sfiora il terrazzo e prosegue fino a terra. Trascurando la resistenza dell'aria, calcolare: (a) la quota massima rispetto al suolo; (b) il tempo totale di volo; (c) la velocità con cui tocca il suolo. Usare $g = 9{,}81\ \mathrm{m/s^2}$.

**Soluzione.** Si sceglie l'asse $z$ verticale verso l'alto con origine al suolo; allora $z_0 = 20{,}0\ \mathrm{m}$, $v_0 = +14{,}0\ \mathrm{m/s}$, $a = -g$.

(a) Nel punto più alto $v = 0$, quindi

$$z_{\max} = z_0 + \frac{v_0^2}{2g} = 20{,}0\ \mathrm{m} + \frac{(14{,}0\ \mathrm{m/s})^2}{2\cdot9{,}81\ \mathrm{m/s^2}} = 20{,}0\ \mathrm{m} + 9{,}99\ \mathrm{m} \simeq 30{,}0\ \mathrm{m}.$$

(b) Il suolo corrisponde a $z = 0$: $0 = 20{,}0 + 14{,}0\,t - 4{,}905\,t^2$. Risolvendo l'equazione di secondo grado,

$$t = \frac{14{,}0 + \sqrt{14{,}0^2 + 4\cdot4{,}905\cdot20{,}0}}{2\cdot4{,}905}\ \mathrm{s} = \frac{14{,}0 + \sqrt{196 + 392{,}4}}{9{,}81}\ \mathrm{s} = \frac{14{,}0 + 24{,}26}{9{,}81}\ \mathrm{s} \simeq 3{,}90\ \mathrm{s}.$$

La radice negativa ($t<0$) non ha significato fisico per il problema posto.

(c) Dalla relazione $v^2 = v_0^2 - 2g(z - z_0)$ con $z = 0$:

$$v = -\sqrt{196 + 2\cdot9{,}81\cdot20{,}0}\ \mathrm{m/s} = -24{,}3\ \mathrm{m/s},$$

dove il segno meno indica che la velocità è diretta verso il basso. Come controllo, $v = v_0 - g t = 14{,}0 - 9{,}81\cdot3{,}90 \simeq -24{,}3\ \mathrm{m/s}$.

### Punti chiave

- Il moto è relativo: un sistema di riferimento comprende un corpo di riferimento, un sistema di coordinate e un orologio.
- La legge oraria $x(t)$ descrive la posizione; lo spostamento differisce in generale dalla distanza percorsa.
- La velocità istantanea è $v = dx/dt$ e l'accelerazione $a = dv/dt = d^2x/dt^2$; i loro segni dipendono dall'orientazione dell'asse.
- Integrando si risale da $a$ a $v$ e $x$: servono due condizioni iniziali ($x_0$, $v_0$).
- Nel moto uniformemente accelerato valgono $x = x_0 + v_0t + \tfrac12at^2$ e $v^2 = v_0^2 + 2a\Delta x$.
- Nel vuoto e vicino alla superficie terrestre tutti i corpi cadono con la stessa accelerazione $g \simeq 9{,}81\ \mathrm{m/s^2}$.
- Il moto armonico, $x = A\cos(\omega t+\varphi)$, è caratterizzato da $\ddot x = -\omega^2 x$ e ha periodo $T = 2\pi/\omega$.

## 2.2 Cinematica vettoriale

La descrizione scalare è sufficiente quando la traiettoria è nota in anticipo, ma nella maggior parte delle situazioni reali il moto si svolge nel piano o nello spazio e la traiettoria è essa stessa un'incognita: si pensi a un proiettile, a un satellite, a una particella carica in un campo magnetico. Occorre allora descrivere la posizione con un **vettore**, cioè un ente dotato di modulo, direzione e verso, e definire velocità e accelerazione come derivate di grandezze vettoriali. Questo passaggio porta con sé concetti nuovi e importanti: la velocità è sempre tangente alla traiettoria, mentre l'accelerazione ha in generale una componente lungo la traiettoria, legata alla variazione del modulo della velocità, e una componente perpendicolare, legata alla variazione della direzione. In questa sezione si richiamano gli strumenti essenziali del calcolo vettoriale e si applicano allo studio del moto, con particolare attenzione al moto circolare e al moto dei proiettili.

### 2.2.1 Posizione

Fissato un sistema di riferimento con origine $O$ e tre assi cartesiani ortogonali $x$, $y$, $z$, a cui sono associati i **versori** $\hat{\imath}$, $\hat{\jmath}$, $\hat{k}$ (vettori di modulo unitario diretti come gli assi), la posizione del punto $P$ è individuata dal **vettore posizione** $\vec{r}$, che congiunge l'origine con il punto:

$$\vec{r}(t) = \overrightarrow{OP} = x(t)\,\hat{\imath} + y(t)\,\hat{\jmath} + z(t)\,\hat{k}.$$

Le tre funzioni scalari $x(t)$, $y(t)$, $z(t)$ sono le **componenti cartesiane** del vettore posizione e costituiscono, nel loro insieme, la legge oraria vettoriale. Il modulo $r = |\vec r| = \sqrt{x^2+y^2+z^2}$ è la distanza del punto dall'origine. Il luogo dei punti occupati dal punto mobile al variare del tempo è la **traiettoria**, che si ottiene eliminando il parametro $t$ tra le equazioni delle componenti. Ad esempio, se $x(t) = R\cos\omega t$ e $y(t) = R\sin\omega t$, eliminando $t$ si ottiene $x^2 + y^2 = R^2$: la traiettoria è una circonferenza.

Lo **spostamento** tra due istanti è il vettore $\Delta\vec r = \vec r(t_2) - \vec r(t_1)$, che congiunge la posizione iniziale con quella finale. Esso non dipende dalla scelta dell'origine (mentre $\vec r$ sì) ed è in generale diverso, in modulo, dalla lunghezza dell'arco di traiettoria percorso; i due coincidono solo nel limite di spostamenti infinitesimi, dove $|d\vec r| = ds$, con $s$ ascissa curvilinea.

Oltre alle coordinate cartesiane, per problemi con particolari simmetrie conviene usare altri sistemi di coordinate. Nel piano, le **coordinate polari** $(r, \theta)$ sono legate a quelle cartesiane da $x = r\cos\theta$, $y = r\sin\theta$; si introducono i versori radiale $\hat u_r$, diretto come $\vec r$, e trasverso $\hat u_\theta$, perpendicolare a esso nel verso di $\theta$ crescente, cosicché $\vec r = r\,\hat u_r$. A differenza dei versori cartesiani, questi versori cambiano direzione al variare della posizione del punto, e quindi anche nel tempo: le loro derivate valgono $\dot{\hat u}_r = \dot\theta\,\hat u_\theta$ e $\dot{\hat u}_\theta = -\dot\theta\,\hat u_r$. Ciò ha conseguenze importanti nel calcolo di velocità e accelerazione.

### 2.2.2 Velocità

La **velocità media** in un intervallo è il vettore $\vec v_m = \Delta\vec r/\Delta t$, parallelo allo spostamento. La **velocità istantanea** è la derivata del vettore posizione:

$$\vec{v}(t) = \lim_{\Delta t\to0}\frac{\Delta\vec r}{\Delta t} = \frac{d\vec r}{dt} = \dot x\,\hat\imath + \dot y\,\hat\jmath + \dot z\,\hat k.$$

Poiché i versori cartesiani sono costanti, derivare un vettore significa semplicemente derivare le sue componenti. Ogni componente della velocità si comporta come nel caso scalare, e questo è il motivo per cui la cinematica scalare si estende senza difficoltà al caso vettoriale in coordinate cartesiane.

Una proprietà fondamentale è che **la velocità è sempre tangente alla traiettoria**. Infatti, al tendere a zero di $\Delta t$, la corda $\Delta\vec r$ tende a disporsi lungo la tangente. Introducendo l'ascissa curvilinea $s(t)$ e il **versore tangente** $\hat u_t$, si può scrivere

$$\vec v = \frac{d\vec r}{ds}\frac{ds}{dt} = \dot s\,\hat u_t ,$$

dove $\dot s$ è la velocità scalare della sezione precedente e $|\vec v| = |\dot s|$. La velocità vettoriale contiene quindi due informazioni: quanto rapidamente il punto si muove lungo la traiettoria (il modulo) e in quale direzione si sta muovendo (il versore tangente).

In coordinate polari, derivando $\vec r = r\,\hat u_r$ e ricordando che il versore radiale varia nel tempo,

$$\vec v = \dot r\,\hat u_r + r\dot\theta\,\hat u_\theta.$$

Il primo termine è la **velocità radiale**, che descrive l'allontanamento o l'avvicinamento all'origine; il secondo è la **velocità trasversa**, dovuta alla rotazione del vettore posizione. La quantità $\omega = \dot\theta$ è la **velocità angolare**, misurata in $\mathrm{rad/s}$. Nel **moto circolare** di raggio $R$ costante si ha $\dot r = 0$ e quindi $\vec v = R\omega\,\hat u_\theta$: la velocità è tangente alla circonferenza e il suo modulo è $v = \omega R$. Se $\omega$ è costante il moto è **circolare uniforme**, con periodo $T = 2\pi/\omega$. Si noti che anche in questo caso il vettore velocità cambia continuamente direzione pur mantenendo modulo costante.

Nota la velocità, la posizione si ricava per integrazione vettoriale, cioè integrando separatamente ogni componente:

$$\vec r(t) = \vec r_0 + \int_{t_0}^{t}\vec v(t')\,dt'.$$

### 2.2.3 Accelerazione

L'**accelerazione** è la derivata della velocità rispetto al tempo, ovvero la derivata seconda della posizione:

$$\vec a(t) = \frac{d\vec v}{dt} = \frac{d^2\vec r}{dt^2} = \ddot x\,\hat\imath + \ddot y\,\hat\jmath + \ddot z\,\hat k.$$

Un punto essenziale è che un corpo è accelerato non solo quando cambia il modulo della velocità ma anche quando ne cambia la direzione. Lo si vede derivando l'espressione $\vec v = v\,\hat u_t$ (con $v = \dot s$):

$$\vec a = \frac{dv}{dt}\,\hat u_t + v\,\frac{d\hat u_t}{dt}.$$

Si dimostra che la derivata del versore tangente è perpendicolare a esso (perché il suo modulo è costante) ed è diretta verso il centro di curvatura della traiettoria; precisamente $d\hat u_t/dt = (v/\rho)\,\hat u_n$, dove $\rho$ è il **raggio di curvatura** locale e $\hat u_n$ il **versore normale**, diretto verso la concavità. Si ottiene così la decomposizione intrinseca

$$\vec a = \underbrace{\frac{dv}{dt}\,\hat u_t}_{\vec a_t} + \underbrace{\frac{v^2}{\rho}\,\hat u_n}_{\vec a_n}.$$

L'**accelerazione tangenziale** $a_t = dv/dt$ descrive la variazione del modulo della velocità; l'**accelerazione normale** o **centripeta** $a_n = v^2/\rho$ descrive la variazione della direzione ed è sempre diretta verso l'interno della curva. In un moto rettilineo ($\rho\to\infty$) l'accelerazione normale è nulla; in un moto uniforme ($v$ costante) l'accelerazione tangenziale è nulla. Il modulo complessivo è $a = \sqrt{a_t^2 + a_n^2}$. Questa decomposizione ha grande rilevanza ingegneristica: nel progetto di una curva stradale o ferroviaria si limita l'accelerazione centripeta $v^2/\rho$ per garantire sicurezza e comfort.

Per il **moto circolare** in coordinate polari, derivando $\vec v = R\omega\,\hat u_\theta$ si ottiene

$$\vec a = R\dot\omega\,\hat u_\theta - R\omega^2\,\hat u_r ,$$

dove $\alpha = \dot\omega$ è l'**accelerazione angolare** ($\mathrm{rad/s^2}$). Il termine tangenziale vale $R\alpha$, quello centripeto $R\omega^2 = v^2/R$ ed è diretto verso il centro. Nel moto circolare uniforme resta solo l'accelerazione centripeta. Proiettando il moto circolare uniforme su un asse, ad esempio $x = R\cos\omega t$, si ritrova esattamente il moto armonico: la componente $x$ dell'accelerazione centripeta vale $-\omega^2 x$.

Un'applicazione classica è il **moto del proiettile**, ovvero il moto di un grave lanciato con velocità iniziale obliqua. Con l'asse $y$ verticale verso l'alto, l'accelerazione è costante, $\vec a = -g\,\hat\jmath$, e le componenti si integrano indipendentemente. Se il lancio avviene dall'origine con velocità $v_0$ inclinata di un angolo $\theta$ sull'orizzontale:

$$x(t) = v_0\cos\theta\,t, \qquad y(t) = v_0\sin\theta\,t - \tfrac12 g t^2.$$

Il moto orizzontale è uniforme, quello verticale uniformemente accelerato: è il **principio di indipendenza dei moti** enunciato da Galileo. Eliminando il tempo si ricava la traiettoria parabolica

$$y = x\tan\theta - \frac{g}{2v_0^2\cos^2\theta}\,x^2,$$

e ponendo $y = 0$ la **gittata** $G = v_0^2\sin(2\theta)/g$, massima per $\theta = 45^\circ$ in assenza di resistenza dell'aria. Nel punto più alto della traiettoria la velocità è orizzontale e l'accelerazione $\vec g$ è tutta normale: il raggio di curvatura vale quindi $\rho = (v_0\cos\theta)^2/g$.

Più in generale, conoscendo l'accelerazione in funzione del tempo e le condizioni iniziali vettoriali $\vec r_0$ e $\vec v_0$ (sei condizioni scalari nello spazio), il moto è completamente determinato per doppia integrazione. Questa osservazione prepara il terreno alla dinamica, dove l'accelerazione sarà determinata dalle forze agenti sul punto.

### Esercizio d'esempio

**Testo.** Un'auto percorre una curva circolare di raggio $R = 80{,}0\ \mathrm{m}$. In un certo istante la sua velocità è $v = 15{,}0\ \mathrm{m/s}$ e sta accelerando uniformemente lungo la traiettoria, passando a $20{,}0\ \mathrm{m/s}$ in $4{,}00\ \mathrm{s}$. Calcolare, all'istante iniziale: (a) l'accelerazione tangenziale; (b) l'accelerazione centripeta; (c) il modulo dell'accelerazione totale e l'angolo che essa forma con la velocità; (d) la velocità angolare e l'accelerazione angolare.

**Soluzione.** (a) L'accelerazione tangenziale è costante:

$$a_t = \frac{\Delta v}{\Delta t} = \frac{20{,}0 - 15{,}0}{4{,}00}\ \mathrm{m/s^2} = 1{,}25\ \mathrm{m/s^2}.$$

(b) L'accelerazione centripeta all'istante iniziale vale

$$a_n = \frac{v^2}{R} = \frac{(15{,}0\ \mathrm{m/s})^2}{80{,}0\ \mathrm{m}} = 2{,}81\ \mathrm{m/s^2}.$$

(c) Le due componenti sono perpendicolari, quindi

$$a = \sqrt{a_t^2 + a_n^2} = \sqrt{1{,}25^2 + 2{,}81^2}\ \mathrm{m/s^2} \simeq 3{,}08\ \mathrm{m/s^2}.$$

L'angolo tra $\vec a$ e $\vec v$ (che è diretta come $\hat u_t$) soddisfa $\tan\beta = a_n/a_t = 2{,}25$, da cui $\beta \simeq 66^\circ$: l'accelerazione punta "in avanti e verso l'interno" della curva.

(d) Velocità e accelerazione angolare sono

$$\omega = \frac{v}{R} = \frac{15{,}0}{80{,}0}\ \mathrm{rad/s} = 0{,}188\ \mathrm{rad/s}, \qquad \alpha = \frac{a_t}{R} = \frac{1{,}25}{80{,}0}\ \mathrm{rad/s^2} = 1{,}56\times10^{-2}\ \mathrm{rad/s^2}.$$

Si osservi che, mentre $a_t$ resta costante, $a_n$ cresce con il quadrato della velocità: dopo $4\ \mathrm{s}$ varrà $5{,}00\ \mathrm{m/s^2}$.

### Punti chiave

- Nello spazio la posizione è il vettore $\vec r(t)$; la traiettoria si ottiene eliminando il tempo tra le componenti.
- La velocità $\vec v = d\vec r/dt$ è sempre tangente alla traiettoria e vale $\vec v = \dot s\,\hat u_t$.
- In coordinate polari $\vec v = \dot r\,\hat u_r + r\dot\theta\,\hat u_\theta$, perché i versori polari ruotano con il punto.
- L'accelerazione si decompone in tangenziale $dv/dt$ (variazione del modulo) e normale $v^2/\rho$ (variazione della direzione).
- Nel moto circolare uniforme l'accelerazione è centripeta, di modulo $\omega^2R = v^2/R$; la sua proiezione su un diametro è un moto armonico.
- Nel moto del proiettile le componenti orizzontale (uniforme) e verticale (uniformemente accelerata) sono indipendenti; la traiettoria è una parabola.
- Note $\vec a(t)$, $\vec r_0$ e $\vec v_0$, il moto è completamente determinato per integrazione.
