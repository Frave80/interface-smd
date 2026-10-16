# Capitolo 4 — Esempi di forze

Nel capitolo precedente abbiamo enunciato i principi della dinamica del punto materiale: la legge d'inerzia, la relazione $\vec{F} = m\vec{a}$ e il principio di azione e reazione. Questi principi, da soli, non bastano però a risolvere alcun problema concreto: occorre sapere *quali* forze agiscono su un corpo e *come* esse dipendono dalla posizione, dalla velocità, dal tempo e dalle caratteristiche dei corpi in interazione. Questo capitolo è dedicato proprio a un catalogo ragionato delle forze che si incontrano più spesso nella meccanica dell'ingegnere: la forza d'inerzia (che inerzia non è, nel senso di una vera interazione, ma che conviene introdurre come strumento di calcolo), il peso, le reazioni vincolari d'appoggio, le forze d'attrito radente e viscoso, la tensione dei fili e la forza elastica. Per ciascuna discuteremo l'origine fisica, la legge empirica o teorica che la descrive, l'ambito di validità e le conseguenze sul moto, fino a ricavare le equazioni dell'oscillatore armonico libero, smorzato e forzato, che rappresentano uno dei modelli più importanti di tutta la fisica e dell'ingegneria.

## 4.1 Forza d'inerzia

### 4.1.1 Dal secondo principio al principio di d'Alembert

Il secondo principio della dinamica, nella forma valida in un **sistema di riferimento inerziale**, afferma che la risultante delle forze agenti su un punto materiale di massa $m$ è uguale al prodotto della massa per l'accelerazione:

$$\vec{F} = m\vec{a}.$$

Questa uguaglianza può essere riscritta in modo apparentemente banale portando tutto al primo membro:

$$\vec{F} - m\vec{a} = \vec{0}.$$

Se definiamo la grandezza

$$\vec{F}_{in} = -m\vec{a},$$

che chiamiamo **forza d'inerzia** (o forza di d'Alembert), la legge del moto assume la forma di una condizione di equilibrio:

$$\vec{F} + \vec{F}_{in} = \vec{0}.$$

Questo è il contenuto del **principio di d'Alembert**: un problema di dinamica può essere trattato formalmente come un problema di statica, purché alle forze "vere" si aggiunga la forza d'inerzia. Il vantaggio pratico è notevole. Chi progetta una struttura, un organo meccanico o un veicolo è spesso abituato a ragionare in termini di equilibrio: somma delle forze nulla, somma dei momenti nulla. Con il principio di d'Alembert lo stesso schema mentale si estende ai corpi accelerati, semplicemente "caricando" il corpo di una forza aggiuntiva opposta all'accelerazione e proporzionale alla massa.

È fondamentale sottolineare che la forza d'inerzia **non è un'interazione** tra il corpo e un altro corpo. Non esiste un "agente" che la eserciti, e di conseguenza essa non ha una reazione corrispondente nel senso del terzo principio. È una grandezza costruita a partire dall'accelerazione del corpo stesso, che ha le dimensioni di una forza ($[\mathrm{kg\,m\,s^{-2}}] = [\mathrm{N}]$) e che si rivela comoda nei calcoli. Per questo motivo molti testi la classificano tra le **forze fittizie** o **forze apparenti**: una distinzione che riprenderemo e approfondiremo nel capitolo sulla meccanica relativa.

### 4.1.2 Interpretazione fisica: il punto di vista dell'osservatore solidale

C'è però un'interpretazione fisica molto concreta della forza d'inerzia. Consideriamo un osservatore che si muove insieme al corpo, cioè solidale con esso. Per questo osservatore il corpo è in quiete, quindi la sua accelerazione relativa è nulla. Se egli volesse comunque applicare la legge di Newton, troverebbe che le forze "vere" (peso, reazioni dei vincoli, tensioni) non si annullano. Per salvare la descrizione deve introdurre una forza aggiuntiva, che è esattamente $-m\vec{a}$, dove $\vec{a}$ è l'accelerazione del suo sistema di riferimento rispetto a un riferimento inerziale.

L'esperienza quotidiana è piena di esempi. Quando un autobus frena bruscamente, i passeggeri in piedi si sentono "spinti" in avanti: nel riferimento dell'autobus (che ha accelerazione diretta all'indietro) compare una forza d'inerzia diretta in avanti. Quando un ascensore parte verso l'alto, ci sentiamo più "pesanti": la forza d'inerzia, diretta verso il basso, si somma al peso. In un'auto che percorre una curva, il guidatore si sente spinto verso l'esterno: è la cosiddetta **forza centrifuga**, che altro non è se non la forza d'inerzia associata all'accelerazione centripeta del veicolo.

Dal punto di vista di un osservatore inerziale (ad esempio una persona ferma sul marciapiede), nessuna di queste forze esiste: il passeggero dell'autobus tende semplicemente a proseguire con la sua velocità per inerzia, mentre l'autobus rallenta sotto di lui; il passeggero dell'ascensore ha bisogno di una reazione del pavimento maggiore del peso per essere accelerato verso l'alto; il guidatore in curva ha bisogno di una forza centripeta (fornita dal sedile e dalla cintura) per essere deviato dalla traiettoria rettilinea. Le due descrizioni sono equivalenti, ma è essenziale non mescolarle: o si lavora nel riferimento inerziale con le sole forze vere e $\vec{F} = m\vec{a}$, oppure si lavora nel riferimento solidale aggiungendo la forza d'inerzia e imponendo l'equilibrio.

### 4.1.3 Uso pratico e limiti

L'uso della forza d'inerzia è particolarmente efficace in tre classi di problemi:

1. **Corpi in traslazione accelerata**: un carico sospeso in un veicolo che accelera, un pendolo appeso al soffitto di un vagone, un oggetto appoggiato sul pianale di un camion che frena. In tutti questi casi si scrive l'equilibrio nel riferimento del veicolo aggiungendo $-m\vec{a}_{veicolo}$.
2. **Moti circolari uniformi**: un corpo vincolato a ruotare con velocità angolare $\omega$ su una circonferenza di raggio $r$ ha accelerazione centripeta di modulo $\omega^2 r$; nel riferimento rotante compare una forza centrifuga di modulo $m\omega^2 r$ diretta radialmente verso l'esterno. Il dimensionamento di un rotore, di un regolatore centrifugo o di una centrifuga da laboratorio si fa abitualmente così.
3. **Misure di accelerazione**: un **accelerometro** è, in sostanza, una massa di prova collegata a una molla. Nel riferimento dello strumento la forza d'inerzia deforma la molla, e la deformazione misurata fornisce l'accelerazione. È il principio di funzionamento dei sensori MEMS presenti negli smartphone e nei sistemi airbag.

Occorre però fare attenzione a un limite: la forza d'inerzia nella forma semplice $-m\vec{a}$ descrive completamente le forze apparenti solo quando il riferimento solidale **trasla** (eventualmente con accelerazione variabile) o, nel caso rotante, quando il corpo è fermo nel riferimento rotante. Se il corpo si muove rispetto a un riferimento che ruota, compaiono ulteriori termini, come la **forza di Coriolis**, che saranno trattati in dettaglio nel capitolo 5. Inoltre la forza d'inerzia non va mai inclusa quando si scrive il secondo principio in un riferimento inerziale: sarebbe un doppio conteggio, uno degli errori più frequenti negli esercizi.

Un'ultima osservazione concettuale riguarda la massa che compare nella forza d'inerzia: si tratta della **massa inerziale**, la stessa che compare in $\vec{F} = m\vec{a}$. Il fatto sperimentale, verificato con precisione altissima (dalle esperienze di Eötvös fino ai test moderni con parti per $10^{15}$), che massa inerziale e massa gravitazionale coincidono rende la forza d'inerzia indistinguibile, localmente, dalla forza peso. Questa osservazione, apparentemente innocua, è il punto di partenza del principio di equivalenza su cui Einstein costruì la relatività generale.

### Esercizio d'esempio

Un pendolo semplice di massa $m = 0{,}50\ \mathrm{kg}$ è appeso al soffitto di un vagone ferroviario che accelera su un binario rettilineo orizzontale con accelerazione costante $a = 2{,}0\ \mathrm{m/s^2}$. Determinare l'angolo $\theta$ che il filo forma con la verticale all'equilibrio (nel riferimento del vagone) e la tensione del filo. Si assuma $g = 9{,}81\ \mathrm{m/s^2}$.

**Soluzione.** Nel riferimento del vagone la massa è ferma. Agiscono il peso $m\vec{g}$ (verticale, verso il basso), la tensione $\vec{T}$ (lungo il filo) e la forza d'inerzia $-m\vec{a}$ (orizzontale, opposta al verso di marcia). L'equilibrio fornisce, proiettando sugli assi orizzontale e verticale:

$$T\sin\theta = ma, \qquad T\cos\theta = mg.$$

Dividendo membro a membro:

$$\tan\theta = \frac{a}{g} = \frac{2{,}0}{9{,}81} = 0{,}204 \quad\Rightarrow\quad \theta \approx 11{,}5^\circ.$$

Il filo è inclinato all'indietro rispetto al verso di marcia. Sommando i quadrati:

$$T = m\sqrt{g^2 + a^2} = 0{,}50 \cdot \sqrt{9{,}81^2 + 2{,}0^2}\ \mathrm{N} = 0{,}50 \cdot 10{,}01\ \mathrm{N} \approx 5{,}0\ \mathrm{N}.$$

Si noti che nel riferimento del vagone la massa "sente" una gravità efficace $\vec{g}_{eff} = \vec{g} - \vec{a}$ di modulo $10{,}01\ \mathrm{m/s^2}$. Lo stesso risultato si ottiene nel riferimento del binario scrivendo $\vec{T} + m\vec{g} = m\vec{a}$, senza alcuna forza d'inerzia.

### Punti chiave

- La forza d'inerzia è definita come $\vec{F}_{in} = -m\vec{a}$ e permette di trattare la dinamica come una statica (principio di d'Alembert).
- Non è un'interazione: non ha un corpo che la esercita né una reazione secondo il terzo principio.
- Ha un significato fisico concreto per l'osservatore solidale con il corpo accelerato (autobus, ascensore, auto in curva).
- Nel riferimento inerziale non va mai aggiunta: sarebbe un doppio conteggio.
- Nel moto circolare la forza d'inerzia è la forza centrifuga, di modulo $m\omega^2 r$.
- Se il corpo si muove rispetto a un riferimento rotante compaiono altri termini (Coriolis), trattati nella meccanica relativa.
- L'uguaglianza tra massa inerziale e gravitazionale rende la forza d'inerzia localmente indistinguibile dal peso.

## 4.2 Peso

### 4.2.1 Dalla gravitazione universale al peso

La forza che chiamiamo comunemente **peso** è la manifestazione, vicino alla superficie terrestre, dell'interazione gravitazionale tra un corpo e la Terra. Newton descrisse questa interazione con la **legge di gravitazione universale**: due masse puntiformi $m_1$ e $m_2$ poste a distanza $r$ si attraggono con una forza diretta lungo la congiungente, di modulo

$$F = G\frac{m_1 m_2}{r^2},$$

dove $G = 6{,}674\times 10^{-11}\ \mathrm{N\,m^2\,kg^{-2}}$ è la **costante di gravitazione universale**. Per un corpo sferico con distribuzione di massa a simmetria sferica (come in buona approssimazione è la Terra), si dimostra che all'esterno la forza è la stessa che si avrebbe se tutta la massa fosse concentrata nel centro (teorema del guscio). Un corpo di massa $m$ posto a distanza $r$ dal centro della Terra, di massa $M_T \approx 5{,}97\times 10^{24}\ \mathrm{kg}$, subisce quindi una forza

$$F = G\frac{M_T m}{r^2}.$$

Se il corpo si trova vicino alla superficie, cioè a quota $h \ll R_T$ con $R_T \approx 6{,}37\times 10^6\ \mathrm{m}$, possiamo porre $r \approx R_T$ e scrivere

$$\vec{P} = m\vec{g}, \qquad g = G\frac{M_T}{R_T^2} \approx 9{,}8\ \mathrm{m/s^2}.$$

Il vettore $\vec{g}$ è l'**accelerazione di gravità**: è diretto verso il basso (verso il centro della Terra, in prima approssimazione) e il suo modulo non dipende dalla massa del corpo. Questa indipendenza è la conseguenza dell'uguaglianza tra massa inerziale e massa gravitazionale e spiega l'osservazione di Galileo per cui, in assenza di aria, tutti i corpi cadono con la stessa accelerazione.

### 4.2.2 Variazioni di $g$ con quota e latitudine

L'approssimazione di $g$ costante è eccellente nella maggior parte dei problemi tecnici, ma è utile conoscerne i limiti. Al variare della quota, sviluppando al primo ordine:

$$g(h) = G\frac{M_T}{(R_T + h)^2} \approx g_0\left(1 - \frac{2h}{R_T}\right).$$

A $h = 10\ \mathrm{km}$ (quota di crociera di un aereo di linea) la riduzione relativa è circa $2h/R_T \approx 3\times 10^{-3}$, cioè lo $0{,}3\%$. Sulla Stazione Spaziale Internazionale, a circa $400\ \mathrm{km}$, $g$ vale ancora circa $8{,}7\ \mathrm{m/s^2}$: gli astronauti non sono in "assenza di gravità", ma in caduta libera insieme alla stazione, e per questo non percepiscono il proprio peso.

C'è poi l'effetto della **rotazione terrestre**. Un osservatore solidale con la superficie si trova in un riferimento rotante con velocità angolare $\omega_T = 7{,}29\times 10^{-5}\ \mathrm{rad/s}$. Ciò che misura con un dinamometro (il **peso apparente**) è la somma vettoriale della forza gravitazionale e della forza centrifuga, di modulo $m\omega_T^2 R_T\cos\lambda$, dove $\lambda$ è la latitudine. All'equatore la forza centrifuga vale circa lo $0{,}34\%$ del peso ed è diretta verso l'alto; ai poli è nulla. Aggiungendo lo schiacciamento della Terra, che rende il raggio polare più piccolo di circa $21\ \mathrm{km}$, si ottiene che $g$ varia da circa $9{,}780\ \mathrm{m/s^2}$ all'equatore a circa $9{,}832\ \mathrm{m/s^2}$ ai poli. Il valore convenzionale adottato in metrologia è $g_n = 9{,}80665\ \mathrm{m/s^2}$. La rotazione modifica anche la *direzione* di $\vec{g}$: la verticale indicata da un filo a piombo non passa esattamente per il centro della Terra, salvo ai poli e all'equatore.

### 4.2.3 Peso, massa e misura

Una distinzione che va padroneggiata fin dall'inizio è quella tra **massa** e **peso**. La massa è una proprietà intrinseca del corpo, misurata in chilogrammi e indipendente dal luogo; il peso è una forza, misurata in newton, che dipende dal campo gravitazionale locale. Un astronauta di $80\ \mathrm{kg}$ ha massa $80\ \mathrm{kg}$ sulla Terra e sulla Luna, ma il suo peso passa da circa $785\ \mathrm{N}$ a circa $130\ \mathrm{N}$, perché $g_{Luna} \approx 1{,}62\ \mathrm{m/s^2}$.

Questa distinzione ha conseguenze pratiche sugli strumenti. Una **bilancia a bracci uguali** confronta due pesi nello stesso campo $g$, quindi in realtà confronta due masse: funzionerebbe identicamente sulla Luna. Un **dinamometro** o una bilancia a molla misura invece una forza (la deformazione della molla è proporzionale alla forza applicata) e la sua lettura, se tarata in chilogrammi sulla Terra, sarebbe errata altrove. Le bilance elettroniche commerciali sono di fatto dinamometri e vanno ricalibrate quando vengono spostate in località con $g$ significativamente diverso, cosa che i costruttori di bilance di precisione prevedono esplicitamente.

Anche la misura di $g$ è un classico problema di fisica sperimentale. Il metodo storico è il **pendolo semplice**: per piccole oscillazioni il periodo vale $T = 2\pi\sqrt{\ell/g}$, quindi misurando la lunghezza $\ell$ e il periodo $T$ si ricava $g = 4\pi^2\ell/T^2$. Con un pendolo di un metro e un cronometro manuale, cronometrando venti oscillazioni per ridurre l'incidenza del tempo di reazione, si ottiene facilmente un'incertezza relativa dell'ordine del per mille. I **gravimetri assoluti** moderni misurano invece la caduta libera di uno specchio in una camera a vuoto mediante interferometria laser, raggiungendo incertezze relative di $10^{-9}$: sono così sensibili da rilevare le variazioni di $g$ dovute alle maree terrestri, ai movimenti delle falde acquifere o alla presenza di cavità nel sottosuolo, e trovano impiego in geofisica e nella prospezione mineraria. Questi strumenti ricordano che anche una grandezza "ovvia" come l'accelerazione di gravità è, a un livello di precisione sufficiente, una grandezza locale e variabile nel tempo.

### 4.2.4 Il moto sotto l'azione del solo peso

Se il peso è l'unica forza agente, il secondo principio fornisce $m\vec{a} = m\vec{g}$, ossia $\vec{a} = \vec{g}$: il moto è uniformemente accelerato. Scelto un asse $z$ verticale verso l'alto e un asse $x$ orizzontale nel piano del moto, con condizioni iniziali $\vec{r}(0) = \vec{0}$ e $\vec{v}(0) = (v_0\cos\alpha,\, v_0\sin\alpha)$, si ottiene

$$x(t) = v_0\cos\alpha\; t, \qquad z(t) = v_0\sin\alpha\; t - \tfrac{1}{2}g t^2.$$

Eliminando il tempo si trova la traiettoria parabolica, e si ricavano la gittata $L = v_0^2\sin(2\alpha)/g$ e la quota massima $H = v_0^2\sin^2\alpha/(2g)$. Questi risultati, già noti dalla cinematica, trovano qui la loro giustificazione dinamica. È importante ricordare che valgono in assenza di resistenza dell'aria: per un proiettile reale, o anche per un pallone, l'attrito viscoso (sezione 4.4) può modificare sensibilmente gittata e forma della traiettoria.

Un'altra conseguenza notevole è che il peso è una **forza conservativa**: il lavoro compiuto dal peso su un corpo che si sposta da una quota $z_A$ a una quota $z_B$ vale $W = -mg(z_B - z_A)$, indipendentemente dal percorso. Si può quindi associare al peso l'energia potenziale $U = mgz$, strumento che sarà sviluppato nei capitoli sul lavoro e sull'energia.

Vale infine la pena di chiarire un aspetto concettuale. È utile pensare a $\vec{g}$ non solo come a un'accelerazione, ma come al **campo gravitazionale** prodotto dalla Terra, cioè alla forza per unità di massa che agisce su un corpo posto in un certo punto dello spazio: le sue unità, $\mathrm{N/kg}$, coincidono con $\mathrm{m/s^2}$. Questa lettura prepara il terreno al concetto di campo che verrà ripreso in elettromagnetismo, dove il campo elettrico è la forza per unità di carica. Nei problemi di questo corso, salvo diversa indicazione, si assume il campo uniforme: stesso modulo e stessa direzione in tutta la regione interessata dal moto. Questa ipotesi è ottima finché le dimensioni della regione sono piccole rispetto al raggio terrestre, e cade invece per i moti orbitali o per i lanci balistici a grandissima gittata, dove la variazione di direzione e di modulo di $\vec{g}$ non può essere trascurata.

### Esercizio d'esempio

Calcolare il peso di un satellite di massa $m = 1200\ \mathrm{kg}$ (a) sulla superficie terrestre e (b) in orbita circolare a quota $h = 600\ \mathrm{km}$. Determinare inoltre (c) la velocità orbitale nel caso (b). Si usino $G = 6{,}674\times10^{-11}\ \mathrm{N\,m^2/kg^2}$, $M_T = 5{,}97\times10^{24}\ \mathrm{kg}$, $R_T = 6{,}37\times10^6\ \mathrm{m}$.

**Soluzione.** (a) Alla superficie:

$$g_0 = \frac{GM_T}{R_T^2} = \frac{6{,}674\times10^{-11}\cdot 5{,}97\times10^{24}}{(6{,}37\times10^6)^2}\ \mathrm{m/s^2} = \frac{3{,}984\times10^{14}}{4{,}058\times10^{13}}\ \mathrm{m/s^2} \approx 9{,}82\ \mathrm{m/s^2},$$

quindi $P_0 = mg_0 \approx 1{,}18\times10^4\ \mathrm{N}$.

(b) A quota $h$, $r = R_T + h = 6{,}97\times10^6\ \mathrm{m}$:

$$g(h) = g_0\left(\frac{R_T}{r}\right)^2 = 9{,}82\cdot\left(\frac{6{,}37}{6{,}97}\right)^2\ \mathrm{m/s^2} \approx 8{,}20\ \mathrm{m/s^2},$$

e $P = m g(h) \approx 9{,}84\times10^3\ \mathrm{N}$: il peso è ancora l'83% di quello al suolo.

(c) In orbita circolare il peso fornisce la forza centripeta: $mg(h) = mv^2/r$, da cui

$$v = \sqrt{g(h)\, r} = \sqrt{8{,}20 \cdot 6{,}97\times10^6}\ \mathrm{m/s} \approx 7{,}56\times10^3\ \mathrm{m/s}.$$

### Punti chiave

- Il peso è la forza gravitazionale esercitata dalla Terra: $\vec{P} = m\vec{g}$ con $g = GM_T/R_T^2 \approx 9{,}8\ \mathrm{m/s^2}$.
- $g$ non dipende dalla massa del corpo grazie all'uguaglianza tra massa inerziale e gravitazionale.
- $g$ diminuisce con la quota (circa $-0{,}3\%$ ogni $10\ \mathrm{km}$) e varia con la latitudine per rotazione e schiacciamento terrestri.
- Il peso apparente misurato in superficie include la forza centrifuga dovuta alla rotazione della Terra.
- Massa (kg) e peso (N) sono grandezze distinte: la bilancia a bracci confronta masse, il dinamometro misura forze.
- Sotto il solo peso il moto è uniformemente accelerato e la traiettoria è parabolica.
- Il peso è conservativo, con energia potenziale $U = mgz$.

## 4.3 Appoggio

### 4.3.1 Vincoli e reazioni vincolari

Nella maggior parte delle situazioni reali i corpi non sono liberi di muoversi in tutte le direzioni dello spazio: un libro poggia su un tavolo, un vagone corre su un binario, una pallina rotola in una guida. Le condizioni geometriche che limitano il moto si chiamano **vincoli**, e le forze che i vincoli esercitano sui corpi per far rispettare tali limitazioni si chiamano **reazioni vincolari**. La caratteristica peculiare delle reazioni vincolari è che non sono note a priori: non esiste una "legge della reazione" analoga alla legge di gravitazione. Il loro valore si determina *a posteriori*, imponendo che il moto (o la quiete) sia compatibile con il vincolo. Per questo motivo le reazioni vincolari sono spesso le incognite dei problemi di dinamica e di statica.

L'**appoggio** è il vincolo più semplice: un corpo poggia su una superficie che gli impedisce di penetrarvi, ma non di staccarsene. Si tratta di un **vincolo unilaterale**: la superficie può spingere il corpo, ma non può tirarlo. La forza che la superficie esercita sul corpo si decompone in una componente perpendicolare alla superficie, la **reazione normale** $\vec{N}$, e in una componente parallela, che è la forza d'attrito e che tratteremo nella sezione successiva. In questa sezione ci occupiamo dell'appoggio **liscio**, cioè privo di attrito, nel quale la reazione è puramente normale.

### 4.3.2 Origine microscopica e caratteristiche della reazione normale

Da dove nasce la reazione normale? A livello microscopico, quando un corpo preme su una superficie, gli atomi delle due superfici si avvicinano leggermente più di quanto farebbero in condizioni di riposo. Le forze elettromagnetiche tra gli elettroni e i nuclei, fortemente repulsive a brevi distanze, generano una spinta che si oppone alla compenetrazione. Macroscopicamente, il piano d'appoggio si deforma di una quantità piccolissima (spesso dell'ordine dei nanometri o dei micrometri) e reagisce come una molla estremamente rigida. Nel modello di **vincolo ideale** si trascura questa deformazione: si assume che la superficie sia perfettamente rigida e che possa fornire qualunque reazione necessaria a impedire la compenetrazione.

Le proprietà della reazione normale per un appoggio liscio sono:

1. **direzione**: perpendicolare alla superficie di contatto nel punto di contatto;
2. **verso**: uscente dalla superficie, cioè diretto verso il corpo appoggiato;
3. **modulo**: non negativo, $N \geq 0$, e determinato dalle equazioni del moto.

La condizione $N \geq 0$ esprime il carattere unilaterale del vincolo. Se, risolvendo le equazioni, si trova $N < 0$, significa che il corpo si **stacca** dalla superficie e il vincolo cessa di agire: da quel momento il corpo si muove liberamente e il problema va reimpostato. Un classico esempio è quello di un corpo che scivola senza attrito dalla sommità di una semisfera: la reazione normale diminuisce man mano che il corpo scende e si annulla a un'altezza pari a $2/3$ del raggio sopra il centro, punto in cui il corpo abbandona la superficie.

Una conseguenza importante del fatto che la reazione di un appoggio liscio è perpendicolare alla superficie è che, se la superficie è ferma, la reazione è sempre perpendicolare alla velocità del corpo, e quindi **non compie lavoro**. Questo semplifica enormemente l'uso del teorema dell'energia cinetica nei problemi con vincoli lisci.

### 4.3.3 La reazione normale non è sempre uguale al peso

Un errore molto comune è identificare la reazione normale con il peso. Le due forze sono uguali in modulo solo in un caso particolare: corpo fermo (o in moto rettilineo uniforme) su un piano orizzontale, senza altre forze verticali. In generale bisogna scrivere l'equazione del moto lungo la direzione normale. Vediamo tre situazioni tipiche.

**Piano inclinato.** Un blocco di massa $m$ è appoggiato su un piano liscio inclinato di un angolo $\alpha$ rispetto all'orizzontale. Scegliendo un asse parallelo al piano e uno perpendicolare, il peso si decompone in $mg\sin\alpha$ lungo il piano e $mg\cos\alpha$ perpendicolarmente. Poiché il blocco non si muove in direzione normale, $N = mg\cos\alpha$, che è minore del peso. Lungo il piano il blocco accelera con $a = g\sin\alpha$.

**Ascensore.** Una persona di massa $m$ sta in piedi su una bilancia in un ascensore che accelera verso l'alto con accelerazione $a$. Nel riferimento inerziale dell'edificio: $N - mg = ma$, quindi $N = m(g + a)$. La bilancia, che misura proprio $N$, segna un valore maggiore del peso. Se l'ascensore accelera verso il basso, $N = m(g - a)$; se è in caduta libera ($a = g$), $N = 0$: è la condizione di **imponderabilità**.

**Dosso o avvallamento.** Un'automobile che percorre a velocità $v$ la sommità di un dosso di raggio di curvatura $R$ ha accelerazione centripeta $v^2/R$ diretta verso il basso. L'equazione radiale dà $mg - N = mv^2/R$, cioè $N = m(g - v^2/R)$. Se $v > \sqrt{gR}$ la reazione si annullerebbe: l'auto si stacca dalla strada. In un avvallamento, invece, $N = m(g + v^2/R)$, e le sospensioni vengono caricate più del peso statico.

### 4.3.4 Appoggi curvi e vincoli bilaterali

Quando la superficie d'appoggio è curva, la reazione normale ha una componente legata alla curvatura della traiettoria. Se il corpo si muove lungo una guida di raggio di curvatura $\rho$, l'equazione lungo la normale principale è

$$N_n + F_n = m\frac{v^2}{\rho},$$

dove $F_n$ è la componente normale delle altre forze. La reazione vincolare fornisce la parte di forza centripeta che le altre forze non sono in grado di fornire. È esattamente ciò che accade nel "giro della morte" delle montagne russe: nel punto più alto la reazione e il peso sono entrambi diretti verso il centro, e la condizione minima perché il carrello resti a contatto è $N \geq 0$, cioè $v^2 \geq g\rho$.

Esistono anche **vincoli bilaterali**, che impediscono il moto in entrambi i versi lungo una direzione: una pallina infilata in un anello di filo rigido, un carrello con ruote che abbracciano la rotaia, un pistone in un cilindro. In questo caso la reazione normale può assumere qualunque segno e il corpo non si stacca mai. Le montagne russe moderne utilizzano proprio ruote superiori e inferiori per trasformare un appoggio unilaterale in un vincolo bilaterale, garantendo la sicurezza anche se la velocità è inferiore al minimo calcolato.

### Esercizio d'esempio

Un'automobile di massa $m = 1000\ \mathrm{kg}$ percorre a velocità costante $v = 15\ \mathrm{m/s}$ un tratto di strada che presenta prima un dosso e poi un avvallamento, entrambi assimilabili ad archi di circonferenza di raggio $R = 40\ \mathrm{m}$. Calcolare la reazione normale della strada nel punto più alto del dosso e nel punto più basso dell'avvallamento, e la velocità massima con cui si può affrontare il dosso senza staccarsi ($g = 9{,}81\ \mathrm{m/s^2}$).

**Soluzione.** L'accelerazione centripeta è $a_c = v^2/R = 225/40\ \mathrm{m/s^2} = 5{,}625\ \mathrm{m/s^2}$.

Sul dosso, il centro di curvatura è sotto l'auto; asse verso il basso positivo: $mg - N_1 = m a_c$, quindi

$$N_1 = m(g - a_c) = 1000\cdot(9{,}81 - 5{,}625)\ \mathrm{N} \approx 4{,}19\times10^3\ \mathrm{N}.$$

Nell'avvallamento il centro è sopra l'auto: $N_2 - mg = m a_c$, quindi

$$N_2 = m(g + a_c) = 1000\cdot(9{,}81 + 5{,}625)\ \mathrm{N} \approx 1{,}54\times10^4\ \mathrm{N}.$$

Il rapporto $N_2/N_1 \approx 3{,}7$ mostra quanto la reazione possa differire dal peso statico ($9{,}81\times10^3\ \mathrm{N}$). La velocità limite sul dosso si ha per $N_1 = 0$:

$$v_{max} = \sqrt{gR} = \sqrt{9{,}81\cdot 40}\ \mathrm{m/s} \approx 19{,}8\ \mathrm{m/s} \approx 71\ \mathrm{km/h}.$$

### Punti chiave

- Le reazioni vincolari non hanno una legge propria: si determinano imponendo il rispetto del vincolo.
- L'appoggio è un vincolo unilaterale: la reazione normale soddisfa $N \geq 0$; se il calcolo dà $N < 0$ il corpo si stacca.
- In un appoggio liscio la reazione è perpendicolare alla superficie e, se la superficie è ferma, non compie lavoro.
- La reazione normale non coincide in generale con il peso: dipende dall'inclinazione, dalle altre forze e dall'accelerazione.
- Su traiettorie curve la reazione contribuisce alla forza centripeta: $N_n + F_n = mv^2/\rho$.
- In un ascensore in caduta libera $N = 0$ (imponderabilità).
- I vincoli bilaterali ammettono reazioni di entrambi i segni e impediscono il distacco.

## 4.4 Forza d'attrito

Quando due corpi sono a contatto, la forza che l'uno esercita sull'altro ha in generale, oltre alla componente normale discussa nella sezione precedente, anche una componente tangente alla superficie di contatto. Questa componente è la **forza d'attrito**. Analogamente, un corpo che si muove all'interno di un fluido (aria, acqua, olio) subisce una forza che si oppone al moto relativo rispetto al fluido. Si tratta di fenomeni di enorme importanza pratica: senza attrito non potremmo camminare, le automobili non potrebbero frenare né curvare, le viti si svitarebbero da sole; d'altra parte l'attrito è responsabile della dissipazione di energia nelle macchine, dell'usura dei componenti e di buona parte dei consumi di un veicolo. Distinguiamo due modelli fondamentali: l'attrito radente tra superfici solide e l'attrito viscoso tra un solido e un fluido.

### 4.4.1 Attrito radente

L'**attrito radente** si manifesta tra due superfici solide a contatto. Le sue leggi empiriche furono formulate da Leonardo da Vinci, riscoperte da Amontons alla fine del Seicento e sistematizzate da Coulomb nel Settecento; per questo si parla spesso di **leggi di Coulomb-Amontons**. È importante sottolineare che si tratta di leggi fenomenologiche, cioè di descrizioni approssimate di un comportamento sperimentale, non di leggi fondamentali come la gravitazione universale. Esse funzionano bene per superfici asciutte, in un ampio intervallo di carichi e velocità, ma non sono esatte.

Occorre distinguere due regimi.

**Attrito statico.** Se le due superfici sono in quiete relativa, la forza d'attrito $\vec{F}_s$ assume il valore necessario per mantenere la quiete, purché esso non superi un valore massimo:

$$|\vec{F}_s| \leq \mu_s N,$$

dove $N$ è il modulo della reazione normale e $\mu_s$ è il **coefficiente di attrito statico**, un numero adimensionale che dipende dalla coppia di materiali e dallo stato delle superfici (rugosità, pulizia, umidità, presenza di lubrificanti). Come la reazione normale, la forza d'attrito statico è una reazione vincolare: non ha un valore prefissato, ma si adegua alle altre forze. Se spingiamo leggermente un armadio pesante, esso non si muove perché l'attrito statico equilibra esattamente la nostra spinta; aumentando la spinta, l'attrito cresce di conseguenza, finché si raggiunge la soglia $\mu_s N$, oltre la quale il moto inizia.

**Attrito dinamico.** Se le superfici strisciano l'una sull'altra, la forza d'attrito ha direzione opposta alla velocità relativa e modulo

$$|\vec{F}_d| = \mu_d N, \qquad \vec{F}_d = -\mu_d N\,\frac{\vec{v}_{rel}}{|\vec{v}_{rel}|},$$

dove $\mu_d$ è il **coefficiente di attrito dinamico** (o cinetico). Sperimentalmente si trova quasi sempre $\mu_d < \mu_s$: una volta "staccato", il corpo scivola più facilmente. Questa differenza spiega il fenomeno dello **stick-slip**, cioè l'alternarsi di fasi di aderenza e di strisciamento, responsabile del cigolio delle porte, del suono di un archetto sulla corda del violino e del "salto" di una gomma su una lavagna.

Le leggi di Coulomb-Amontons contengono tre affermazioni empiriche notevoli: (1) la forza d'attrito è proporzionale al carico normale; (2) è indipendente dall'area apparente di contatto; (3) l'attrito dinamico è, in prima approssimazione, indipendente dalla velocità di strisciamento. La seconda affermazione appare sorprendente, ma ha una spiegazione microscopica. Le superfici reali, anche se lucidate, sono rugose a scala micrometrica, e si toccano solo in corrispondenza delle sommità delle asperità. L'**area reale di contatto** è una piccolissima frazione dell'area apparente ed è proporzionale al carico, perché le asperità si deformano plasticamente fino a sostenere il carico. Poiché la forza d'attrito è legata alla resistenza al taglio delle microgiunzioni che si formano in queste zone, essa risulta proporzionale all'area reale, quindi al carico, e indipendente dall'area apparente.

Valori indicativi dei coefficienti sono: acciaio su acciaio asciutto $\mu_s \approx 0{,}7$, $\mu_d \approx 0{,}6$; gomma su asfalto asciutto $\mu_s \approx 1$, che scende a circa $0{,}5$ su asfalto bagnato; teflon su teflon $\mu \approx 0{,}04$; ghiaccio su ghiaccio $\mu_d \approx 0{,}03$. Questi valori hanno un'incertezza notevole, spesso del 20-30%, e vanno misurati sperimentalmente per l'applicazione specifica.

Un metodo semplice di misura del coefficiente statico è il **piano inclinato**: si inclina progressivamente un piano su cui poggia il campione finché questo inizia a scivolare. All'angolo critico $\alpha_c$ si ha $mg\sin\alpha_c = \mu_s mg\cos\alpha_c$, da cui $\mu_s = \tan\alpha_c$. L'angolo $\alpha_c$ si chiama **angolo d'attrito**. Geometricamente, la reazione totale del piano (somma di normale e attrito) deve rimanere entro un cono di semiapertura $\alpha_c$ attorno alla normale: è il **cono d'attrito**, concetto molto usato in statica e in robotica per stabilire se una presa o un appoggio è stabile.

Un esempio tecnico importante è la frenata di un veicolo. Se le ruote non bloccano, il contatto tra pneumatico e strada è di tipo statico (il punto di contatto della ruota che rotola è istantaneamente fermo rispetto all'asfalto), e la decelerazione massima è $\mu_s g$. Se le ruote bloccano, si passa all'attrito dinamico, con decelerazione $\mu_d g$, minore, e per di più si perde la capacità di sterzare. È esattamente il motivo per cui è stato introdotto il sistema **ABS**, che modula la pressione dei freni per mantenere le ruote al limite dell'aderenza statica.

### 4.4.2 Attrito viscoso

Quando un corpo si muove in un fluido, quest'ultimo esercita su di esso una forza resistente. Per velocità sufficientemente basse e corpi di piccole dimensioni, oppure per fluidi molto viscosi, questa forza è proporzionale alla velocità e opposta a essa:

$$\vec{F}_v = -b\,\vec{v},$$

dove $b$ è un coefficiente positivo, misurato in $\mathrm{kg/s}$ (o $\mathrm{N\,s/m}$), che dipende dalla forma e dalle dimensioni del corpo e dalla **viscosità** $\eta$ del fluido. Per una sfera di raggio $r$ in moto lento, Stokes dimostrò che

$$b = 6\pi\eta r.$$

La viscosità dell'acqua a temperatura ambiente vale circa $1{,}0\times10^{-3}\ \mathrm{Pa\,s}$, quella dell'aria circa $1{,}8\times10^{-5}\ \mathrm{Pa\,s}$, quella della glicerina circa $1{,}4\ \mathrm{Pa\,s}$. Il regime lineare (detto **regime di Stokes** o laminare) è valido quando il **numero di Reynolds** $Re = \rho_f v d/\eta$ (con $\rho_f$ densità del fluido e $d$ dimensione caratteristica del corpo) è molto minore di 1. Per valori di $Re$ elevati, come nel caso di un'automobile o di un paracadutista, la resistenza diventa approssimativamente quadratica nella velocità, $F = \tfrac{1}{2}C_x\rho_f A v^2$, con $C_x$ coefficiente di resistenza aerodinamica e $A$ area frontale. In questo corso ci concentriamo sul modello lineare, che si presta a una soluzione analitica completa.

Consideriamo un corpo di massa $m$ che cade in un fluido sotto l'azione del peso e dell'attrito viscoso (trascuriamo per ora la spinta di Archimede, oppure la includiamo in un peso efficace). Con l'asse $z$ diretto verso il basso:

$$m\frac{dv}{dt} = mg - bv.$$

Questa è un'equazione differenziale lineare del primo ordine. Si osserva subito che esiste una velocità per la quale l'accelerazione si annulla, la **velocità limite**:

$$v_\infty = \frac{mg}{b}.$$

Introducendo la **costante di tempo** $\tau = m/b$, l'equazione diventa $dv/dt = (v_\infty - v)/\tau$. Separando le variabili e integrando con la condizione iniziale $v(0) = 0$:

$$v(t) = v_\infty\left(1 - e^{-t/\tau}\right).$$

La velocità cresce esponenzialmente verso il valore limite: dopo un tempo $\tau$ ha raggiunto il 63% di $v_\infty$, dopo $3\tau$ il 95%, dopo $5\tau$ oltre il 99%. La posizione si ottiene integrando ancora: $z(t) = v_\infty t - v_\infty\tau(1 - e^{-t/\tau})$. Per tempi lunghi il moto diventa rettilineo uniforme, con uno "scarto" costante $v_\infty\tau$ rispetto al moto che si avrebbe partendo già alla velocità limite.

Il caso di un corpo lanciato con velocità $v_0$ in assenza di altre forze (per esempio un'imbarcazione che spegne il motore, nel modello lineare) dà invece $v(t) = v_0 e^{-t/\tau}$: la velocità decade esponenzialmente e lo spazio totale percorso è finito, pari a $v_0\tau$.

L'attrito viscoso è alla base di numerose applicazioni e tecniche di misura. Il **viscosimetro a caduta di sfera** misura $\eta$ dalla velocità limite di una sferetta; l'esperimento di Millikan, che determinò la carica dell'elettrone, si basava sulla velocità limite di goccioline d'olio in aria; gli **ammortizzatori** dei veicoli sono dispositivi in cui un pistone si muove in olio, realizzando proprio una forza proporzionale alla velocità. Rispetto all'attrito radente, l'attrito viscoso ha una caratteristica qualitativa fondamentale: non esiste un attrito "statico" viscoso. Qualunque forza, per quanto piccola, mette in moto un corpo immerso in un fluido, perché a velocità nulla la resistenza è nulla.

### Esercizio d'esempio

Una sferetta d'acciaio di raggio $r = 1{,}0\ \mathrm{mm}$ e densità $\rho_s = 7800\ \mathrm{kg/m^3}$ viene lasciata cadere in glicerina ($\eta = 1{,}4\ \mathrm{Pa\,s}$, $\rho_f = 1260\ \mathrm{kg/m^3}$). Calcolare la velocità limite, la costante di tempo e verificare la validità del regime di Stokes. ($g = 9{,}81\ \mathrm{m/s^2}$.)

**Soluzione.** Il volume è $V = \tfrac{4}{3}\pi r^3 = 4{,}19\times10^{-9}\ \mathrm{m^3}$ e la massa $m = \rho_s V = 3{,}27\times10^{-5}\ \mathrm{kg}$. Includendo la spinta di Archimede, la forza motrice è $(\rho_s - \rho_f)Vg$. Il coefficiente di attrito è

$$b = 6\pi\eta r = 6\pi\cdot1{,}4\cdot1{,}0\times10^{-3}\ \mathrm{kg/s} = 2{,}64\times10^{-2}\ \mathrm{kg/s}.$$

Velocità limite:

$$v_\infty = \frac{(\rho_s - \rho_f)Vg}{b} = \frac{6540\cdot4{,}19\times10^{-9}\cdot9{,}81}{2{,}64\times10^{-2}}\ \mathrm{m/s} \approx 1{,}02\times10^{-2}\ \mathrm{m/s}.$$

Costante di tempo: $\tau = m/b = 3{,}27\times10^{-5}/2{,}64\times10^{-2}\ \mathrm{s} \approx 1{,}2\times10^{-3}\ \mathrm{s}$: la sfera raggiunge la velocità limite quasi istantaneamente. Numero di Reynolds con $d = 2r$:

$$Re = \frac{\rho_f v_\infty d}{\eta} = \frac{1260\cdot1{,}02\times10^{-2}\cdot2{,}0\times10^{-3}}{1{,}4} \approx 1{,}8\times10^{-2} \ll 1,$$

quindi il regime di Stokes è pienamente giustificato.

### Punti chiave

- L'attrito radente statico è una reazione vincolare: $|\vec{F}_s| \leq \mu_s N$, con valore determinato dalle altre forze.
- L'attrito radente dinamico ha modulo $\mu_d N$ e verso opposto alla velocità relativa; di norma $\mu_d < \mu_s$.
- Le leggi di Coulomb-Amontons sono empiriche; l'indipendenza dall'area apparente si spiega con l'area reale di contatto delle asperità.
- L'angolo d'attrito soddisfa $\tan\alpha_c = \mu_s$ e definisce il cono d'attrito.
- L'attrito viscoso lineare $\vec{F} = -b\vec{v}$ vale a basso numero di Reynolds; per una sfera $b = 6\pi\eta r$.
- In caduta in un fluido la velocità tende esponenzialmente a $v_\infty = mg/b$ con costante di tempo $\tau = m/b$.
- Non esiste attrito viscoso statico: qualunque forza mette in moto un corpo in un fluido.

## 4.5 Tensione

### 4.5.1 Filo ideale

Funi, cavi, catene e fili sono tra gli elementi più diffusi in meccanica: sollevano carichi nelle gru, sostengono gli ascensori, trasmettono forze nei sistemi di carrucole, mantengono in posizione i ponti strallati. La forza che un filo esercita sui corpi a cui è collegato si chiama **tensione**. Per poterla trattare in modo semplice si introduce il modello di **filo ideale**, caratterizzato da tre proprietà:

1. **inestensibile**: la lunghezza del filo non cambia, qualunque sia la forza applicata;
2. **di massa trascurabile**: la massa del filo è molto minore di quella dei corpi collegati;
3. **perfettamente flessibile**: il filo non oppone alcuna resistenza alla flessione, quindi può trasmettere forze solo lungo la propria direzione.

Da queste ipotesi discendono le proprietà fondamentali della tensione. La terza ipotesi implica che la forza che il filo esercita su un corpo è sempre **diretta lungo il filo** e **verso il filo** stesso: un filo può solo tirare, mai spingere. È quindi, come l'appoggio, un vincolo unilaterale: la tensione deve soddisfare $T \geq 0$, e se il calcolo fornisce $T < 0$ significa che il filo si è allentato e non agisce più.

### 4.5.2 Perché la tensione è uniforme lungo un filo di massa trascurabile

La seconda ipotesi ha una conseguenza importante. Consideriamo un tratto di filo tra due punti A e B, rettilineo, e supponiamo che il resto del filo eserciti su di esso le forze $\vec{T}_A$ e $\vec{T}_B$ alle estremità. Applicando il secondo principio a questo tratto, di massa $m_f$:

$$\vec{T}_A + \vec{T}_B + m_f\vec{g} = m_f\vec{a}.$$

Se $m_f \to 0$, si ottiene $\vec{T}_A = -\vec{T}_B$: le forze alle due estremità sono uguali in modulo e opposte. In altre parole, **la tensione ha lo stesso modulo in ogni punto di un filo ideale**, anche se il filo è accelerato. Questo risultato, che vale per qualunque tratto, significa che un filo ideale "trasmette" integralmente la forza da un'estremità all'altra.

Se il filo non ha massa trascurabile la tensione varia lungo il filo. Una fune verticale di massa per unità di lunghezza $\lambda$ che sostiene un carico $M$ ha, a distanza $s$ dal carico, tensione $T(s) = (M + \lambda s)g$: è massima all'aggancio superiore, dove deve sostenere anche il peso della fune stessa. Nei cavi delle funivie o degli ascensori per grattacieli questo effetto è dominante e richiede accorgimenti di progetto specifici.

La prima ipotesi, l'inestensibilità, è invece un **vincolo cinematico**: se due corpi sono collegati da un filo teso, le loro velocità e accelerazioni lungo il filo sono legate. Nel caso più semplice di due masse collegate da un filo che passa su una carrucola, se una scende di $\Delta s$ l'altra sale di $\Delta s$, e le loro accelerazioni hanno lo stesso modulo. In sistemi di carrucole più complessi il legame può coinvolgere fattori numerici (per esempio, in un paranco con carrucola mobile l'estremo libero si sposta del doppio rispetto al carico).

### 4.5.3 Carrucole e deviazione della tensione

Una **carrucola ideale** (di massa trascurabile e senza attrito sull'asse) ha l'effetto di cambiare la direzione del filo senza alterare il modulo della tensione. Applicando le ipotesi sopra descritte al tratto di filo avvolto, si trova infatti che la tensione è la stessa sui due rami. La carrucola esercita sul filo una forza pari alla somma vettoriale delle due tensioni, e di conseguenza il supporto della carrucola deve sopportare questa forza. Se i due rami sono paralleli, il supporto è caricato con $2T$.

Il sistema più classico è la **macchina di Atwood**: due masse $m_1 > m_2$ appese ai due capi di un filo ideale che passa su una carrucola ideale. Scegliendo come positivo il verso in cui scende $m_1$, le equazioni del moto delle due masse sono

$$m_1 g - T = m_1 a, \qquad T - m_2 g = m_2 a.$$

Sommando membro a membro si elimina la tensione:

$$a = \frac{m_1 - m_2}{m_1 + m_2}\,g, \qquad T = \frac{2m_1 m_2}{m_1 + m_2}\,g.$$

Si notano due fatti istruttivi. Primo: l'accelerazione può essere resa molto più piccola di $g$ scegliendo masse quasi uguali; per questo Atwood ideò la macchina nel 1784 come strumento per "rallentare" la caduta libera e misurarne le leggi con gli orologi dell'epoca. Secondo: la tensione è compresa tra $m_2 g$ e $m_1 g$; in particolare non è uguale al peso di nessuna delle due masse, perché entrambe sono accelerate. Il filo trattiene la massa più pesante meno del suo peso e solleva quella più leggera più del suo peso.

Il **paranco** sfrutta invece la combinazione di carrucole fisse e mobili per ridurre la forza necessaria a sollevare un carico. Con una carrucola mobile alla quale è appeso il carico $Mg$, e i due rami del filo verticali, l'equilibrio richiede $2T = Mg$, quindi è sufficiente tirare con forza $Mg/2$; in compenso, per sollevare il carico di $h$ bisogna tirare il filo di $2h$, in accordo con la conservazione dell'energia: il lavoro fatto è sempre $Mgh$.

### 4.5.4 Fili reali e limiti del modello

Nei fili reali nessuna delle tre ipotesi è rigorosamente vera. I cavi si allungano elasticamente sotto carico (un cavo d'acciaio si comporta come una molla molto rigida, con costante $k = EA/L$, dove $E$ è il modulo di Young, $A$ la sezione e $L$ la lunghezza); hanno una massa che può non essere trascurabile; e hanno una certa rigidezza flessionale, che diventa importante per cavi spessi avvolti su pulegge di piccolo diametro. Inoltre ogni filo ha un **carico di rottura**: se la tensione supera questo valore il filo si spezza. Nella progettazione si adotta un coefficiente di sicurezza, tipicamente tra 5 e 12 per funi di sollevamento, rispetto al carico massimo previsto.

Un fenomeno tipico dei fili reali avvolti attorno a un cilindro fisso con attrito è descritto dalla **formula di Eulero-Eytelwein** (o del cabestano): la tensione su un ramo può essere molto maggiore di quella sull'altro, secondo $T_1 = T_2 e^{\mu\theta}$, dove $\theta$ è l'angolo di avvolgimento e $\mu$ il coefficiente d'attrito. È il principio con cui un marinaio trattiene una nave avvolgendo alcuni giri di cima intorno a una bitta, ed è anche il motivo per cui, in presenza d'attrito sulla carrucola, la tensione non è più uguale sui due rami.

### Esercizio d'esempio

Un blocco di massa $m_1 = 4{,}0\ \mathrm{kg}$ poggia su un tavolo orizzontale con coefficiente di attrito dinamico $\mu_d = 0{,}25$ ed è collegato, tramite un filo ideale che passa su una carrucola ideale posta sul bordo del tavolo, a un corpo di massa $m_2 = 2{,}0\ \mathrm{kg}$ che pende verticalmente. Il sistema è in moto. Calcolare l'accelerazione e la tensione del filo ($g = 9{,}81\ \mathrm{m/s^2}$).

**Soluzione.** Per il blocco sul tavolo, la reazione normale è $N = m_1 g$ e l'attrito dinamico vale $\mu_d m_1 g$. Nel verso del moto (blocco verso la carrucola, corpo appeso verso il basso):

$$T - \mu_d m_1 g = m_1 a, \qquad m_2 g - T = m_2 a.$$

Sommando:

$$a = \frac{m_2 - \mu_d m_1}{m_1 + m_2}\,g = \frac{2{,}0 - 0{,}25\cdot4{,}0}{6{,}0}\cdot9{,}81\ \mathrm{m/s^2} = \frac{1{,}0}{6{,}0}\cdot9{,}81\ \mathrm{m/s^2} \approx 1{,}64\ \mathrm{m/s^2}.$$

Dalla seconda equazione:

$$T = m_2(g - a) = 2{,}0\cdot(9{,}81 - 1{,}64)\ \mathrm{N} \approx 16{,}4\ \mathrm{N}.$$

Verifica con la prima: $T = m_1 a + \mu_d m_1 g = 6{,}54 + 9{,}81 = 16{,}35\ \mathrm{N}$. Si noti che $T < m_2 g = 19{,}6\ \mathrm{N}$, come atteso per un corpo che accelera verso il basso.

### Punti chiave

- Il filo ideale è inestensibile, di massa trascurabile e perfettamente flessibile.
- La tensione è diretta lungo il filo, può solo tirare ($T \geq 0$): è un vincolo unilaterale.
- In un filo di massa trascurabile la tensione ha lo stesso modulo in ogni punto, anche durante il moto accelerato.
- L'inestensibilità impone un vincolo cinematico tra le velocità e le accelerazioni dei corpi collegati.
- Una carrucola ideale cambia la direzione del filo senza modificare il modulo della tensione.
- Nella macchina di Atwood $a = g(m_1 - m_2)/(m_1 + m_2)$ e la tensione non coincide con nessuno dei due pesi.
- I fili reali hanno elasticità, massa, carico di rottura e, se avvolti con attrito, tensioni diverse sui due rami.

## 4.6 Forza elastica

Molti corpi solidi, se deformati di poco, tendono a ritornare nella configurazione iniziale quando la causa della deformazione viene rimossa. La forza responsabile di questo ritorno si chiama **forza elastica**, e il modello più semplice è quello della **molla ideale**. Per una molla di massa trascurabile, con un estremo fisso e l'altro collegato a un corpo, la forza esercitata sul corpo è descritta dalla **legge di Hooke**:

$$\vec{F} = -k\,(x - \ell_0)\,\hat{u}_x,$$

dove $x$ è la lunghezza attuale della molla, $\ell_0$ la sua **lunghezza a riposo**, $\hat{u}_x$ il versore orientato dall'estremo fisso al corpo e $k > 0$ la **costante elastica**, misurata in $\mathrm{N/m}$. Ponendo l'origine nella posizione di riposo, la legge si scrive semplicemente $F = -kx$: la forza è proporzionale alla deformazione e diretta in verso opposto, cioè **di richiamo**. La legge di Hooke vale solo per deformazioni piccole, entro il **limite di proporzionalità** del materiale; oltre questo limite la relazione diventa non lineare e, superato il limite elastico, la deformazione diventa permanente. La sua importanza va però ben oltre le molle: qualunque sistema meccanico che si trovi vicino a una posizione di equilibrio stabile è soggetto, per piccoli spostamenti, a una forza di richiamo approssimativamente lineare. Per questo l'oscillatore armonico è il modello universale delle piccole oscillazioni: pendoli, strutture edilizie, atomi in un reticolo cristallino, circuiti elettrici.

### 4.6.1 Moto armonico libero

Consideriamo un corpo di massa $m$ collegato a una molla di costante $k$, libero di muoversi su un piano orizzontale liscio. Con l'origine nella posizione di riposo, il secondo principio dà

$$m\ddot{x} = -kx \qquad\Longleftrightarrow\qquad \ddot{x} + \omega_0^2 x = 0, \qquad \omega_0 = \sqrt{\frac{k}{m}}.$$

Questa è l'**equazione dell'oscillatore armonico**. È un'equazione differenziale lineare, omogenea, del secondo ordine a coefficienti costanti. La sua soluzione generale è

$$x(t) = A\cos(\omega_0 t + \varphi),$$

dove l'**ampiezza** $A$ e la **fase iniziale** $\varphi$ sono costanti determinate dalle condizioni iniziali: $A = \sqrt{x_0^2 + (v_0/\omega_0)^2}$ e $\tan\varphi = -v_0/(\omega_0 x_0)$. La grandezza $\omega_0$ è la **pulsazione propria** (in $\mathrm{rad/s}$); il **periodo** è $T_0 = 2\pi/\omega_0 = 2\pi\sqrt{m/k}$ e la **frequenza** $f_0 = 1/T_0$ (in hertz).

Il risultato fisicamente più notevole è l'**isocronismo**: il periodo non dipende dall'ampiezza. Che la molla venga allungata di un millimetro o di un centimetro, il corpo impiega lo stesso tempo a compiere un'oscillazione completa. Questa proprietà, conseguenza diretta della linearità della forza, è ciò che ha reso possibile la costruzione di orologi precisi basati su bilancieri a molla e, più di recente, su oscillatori al quarzo. Il periodo dipende invece da massa e rigidezza: una massa maggiore oscilla più lentamente, una molla più rigida più velocemente.

Velocità e accelerazione si ottengono derivando: $v(t) = -A\omega_0\sin(\omega_0 t + \varphi)$, $a(t) = -A\omega_0^2\cos(\omega_0 t + \varphi) = -\omega_0^2 x(t)$. La velocità è massima (in modulo) al passaggio per l'equilibrio e nulla agli estremi; l'accelerazione è massima agli estremi e nulla all'equilibrio. Dal punto di vista energetico, l'energia meccanica

$$E = \tfrac{1}{2}m v^2 + \tfrac{1}{2}k x^2 = \tfrac{1}{2}kA^2$$

si conserva, trasformandosi continuamente da cinetica a potenziale elastica e viceversa.

Se la molla è verticale e sostiene il corpo contro il peso, la posizione di equilibrio si sposta di $\Delta = mg/k$ verso il basso, ma misurando lo spostamento da questa nuova posizione l'equazione del moto rimane identica: il peso, essendo costante, cambia solo il punto attorno a cui si oscilla, non la pulsazione. Questo fornisce anche un metodo di misura di $k$: dall'allungamento statico $\Delta$ si ricava $\omega_0 = \sqrt{g/\Delta}$.

### 4.6.2 Moto armonico smorzato

Nella realtà ogni oscillazione si attenua nel tempo per effetto delle forze dissipative. Il modello più semplice prevede una forza d'attrito viscoso $-b\dot{x}$, che si aggiunge alla forza elastica:

$$m\ddot{x} + b\dot{x} + kx = 0 \qquad\Longleftrightarrow\qquad \ddot{x} + 2\gamma\dot{x} + \omega_0^2 x = 0, \qquad \gamma = \frac{b}{2m}.$$

Il parametro $\gamma$, misurato in $\mathrm{s^{-1}}$, si chiama **coefficiente di smorzamento**. Cercando soluzioni della forma $e^{\lambda t}$ si ottiene l'equazione caratteristica $\lambda^2 + 2\gamma\lambda + \omega_0^2 = 0$, con radici $\lambda = -\gamma \pm \sqrt{\gamma^2 - \omega_0^2}$. Il comportamento dipende dal segno del discriminante, e si distinguono tre regimi.

**Smorzamento debole** ($\gamma < \omega_0$, sottosmorzato). Le radici sono complesse coniugate e la soluzione è

$$x(t) = A e^{-\gamma t}\cos(\omega_s t + \varphi), \qquad \omega_s = \sqrt{\omega_0^2 - \gamma^2}.$$

Il corpo oscilla con pulsazione $\omega_s$ leggermente minore di quella propria, mentre l'ampiezza decresce esponenzialmente con costante di tempo $1/\gamma$. L'energia, proporzionale al quadrato dell'ampiezza, decade come $e^{-2\gamma t}$. Si definisce il **fattore di qualità** $Q = \omega_0/(2\gamma)$, che indica, a meno di un fattore $2\pi$, quante oscillazioni il sistema compie prima che l'energia si riduca di un fattore $e$. Un diapason ha $Q$ dell'ordine di $10^3$, un cristallo di quarzo per orologi $10^4$-$10^6$, la sospensione di un'automobile valori vicini a 1.

**Smorzamento critico** ($\gamma = \omega_0$). Le radici coincidono e la soluzione è $x(t) = (C_1 + C_2 t)e^{-\gamma t}$. Il sistema ritorna all'equilibrio senza oscillare, nel tempo più breve possibile. È la condizione che si cerca di realizzare negli strumenti di misura ad ago (galvanometri, bilance analitiche) e nei chiudiporta, affinché l'indicatore o la porta raggiungano rapidamente la posizione finale senza oscillazioni.

**Smorzamento forte** ($\gamma > \omega_0$, sovrasmorzato). Le radici sono reali e negative, e la soluzione è una combinazione di due esponenziali decrescenti. Il sistema ritorna all'equilibrio senza oscillare, ma più lentamente che nel caso critico, perché uno dei due esponenziali decresce con costante di tempo lunga. Un ammortizzatore troppo "duro" è in questo regime.

### 4.6.3 Moto armonico forzato

Se all'oscillatore smorzato si applica una forza esterna sinusoidale $F(t) = F_0\cos(\omega t)$, l'equazione del moto diventa

$$\ddot{x} + 2\gamma\dot{x} + \omega_0^2 x = \frac{F_0}{m}\cos(\omega t).$$

È un'equazione lineare non omogenea. La sua soluzione generale è la somma della soluzione generale dell'omogenea associata (il moto smorzato appena studiato, detto **transitorio**) e di una soluzione particolare. Poiché il transitorio si estingue con costante di tempo $1/\gamma$, dopo un tempo sufficientemente lungo rimane solo la soluzione particolare, detta **regime stazionario**:

$$x(t) = A(\omega)\cos(\omega t - \delta),$$

con

$$A(\omega) = \frac{F_0/m}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\gamma^2\omega^2}}, \qquad \tan\delta = \frac{2\gamma\omega}{\omega_0^2 - \omega^2}.$$

Il fatto fondamentale è che, a regime, il sistema oscilla alla **frequenza della forzante**, non alla propria. L'ampiezza e lo sfasamento $\delta$ (ritardo della risposta rispetto alla forza) dipendono però fortemente da $\omega$. A bassa frequenza ($\omega \ll \omega_0$) l'ampiezza tende al valore statico $F_0/k$ e la risposta è in fase con la forza: la molla segue lentamente la forzante. Ad alta frequenza ($\omega \gg \omega_0$) l'ampiezza decresce come $1/\omega^2$ e la risposta è in opposizione di fase: domina l'inerzia della massa. Nell'intorno di $\omega_0$ si ha la **risonanza**: l'ampiezza raggiunge il massimo, per $\omega_r = \sqrt{\omega_0^2 - 2\gamma^2}$, e lo sfasamento passa per $\pi/2$ esattamente a $\omega = \omega_0$. Per smorzamenti deboli il valore massimo dell'ampiezza è circa $Q$ volte il valore statico, e la larghezza della curva di risonanza (a metà potenza) è $\Delta\omega \approx 2\gamma = \omega_0/Q$.

La risonanza è uno dei fenomeni più importanti dell'ingegneria, sia come risorsa sia come pericolo. È sfruttata nei circuiti di sintonia delle radio, negli oscillatori al quarzo, nei sensori risonanti, negli strumenti musicali. È invece un pericolo per le strutture: un ponte, un edificio o un albero motore sollecitati periodicamente a una frequenza vicina alla propria possono raggiungere ampiezze di oscillazione distruttive. Il ponte pedonale Millennium di Londra, inaugurato nel 2000, dovette essere chiuso dopo due giorni per le ampie oscillazioni laterali indotte dal passo dei pedoni, e fu reso sicuro aggiungendo smorzatori viscosi che abbassano il fattore di qualità. Nella progettazione meccanica si verifica sempre che le frequenze delle sollecitazioni (rotazione dei motori, vento, traffico, sismi) siano lontane dalle frequenze proprie della struttura.

### Esercizio d'esempio

Un corpo di massa $m = 0{,}20\ \mathrm{kg}$ è collegato a una molla di costante $k = 80\ \mathrm{N/m}$ e a uno smorzatore con $b = 0{,}40\ \mathrm{kg/s}$. (a) Calcolare la pulsazione propria, il coefficiente di smorzamento, la pulsazione delle oscillazioni smorzate e il fattore di qualità. (b) Il sistema è forzato da $F(t) = F_0\cos(\omega t)$ con $F_0 = 0{,}50\ \mathrm{N}$: calcolare l'ampiezza a regime per $\omega = \omega_0$ e confrontarla con lo spostamento statico.

**Soluzione.** (a)

$$\omega_0 = \sqrt{\frac{k}{m}} = \sqrt{\frac{80}{0{,}20}}\ \mathrm{rad/s} = 20\ \mathrm{rad/s}, \qquad \gamma = \frac{b}{2m} = \frac{0{,}40}{0{,}40}\ \mathrm{s^{-1}} = 1{,}0\ \mathrm{s^{-1}}.$$

Poiché $\gamma < \omega_0$ il moto libero è sottosmorzato con

$$\omega_s = \sqrt{400 - 1}\ \mathrm{rad/s} \approx 19{,}97\ \mathrm{rad/s}, \qquad Q = \frac{\omega_0}{2\gamma} = 10.$$

(b) A $\omega = \omega_0$ il termine $(\omega_0^2 - \omega^2)$ si annulla:

$$A(\omega_0) = \frac{F_0/m}{2\gamma\omega_0} = \frac{0{,}50/0{,}20}{2\cdot1{,}0\cdot20}\ \mathrm{m} = \frac{2{,}5}{40}\ \mathrm{m} = 6{,}25\times10^{-2}\ \mathrm{m}.$$

Lo spostamento statico è $F_0/k = 0{,}50/80\ \mathrm{m} = 6{,}25\times10^{-3}\ \mathrm{m}$. Il rapporto è esattamente $Q = 10$: la risonanza amplifica la risposta di un fattore pari al fattore di qualità.

### Punti chiave

- La forza elastica segue la legge di Hooke $F = -kx$ per piccole deformazioni ed è una forza di richiamo.
- L'oscillatore armonico libero ha pulsazione $\omega_0 = \sqrt{k/m}$, indipendente dall'ampiezza (isocronismo).
- L'energia dell'oscillatore libero si conserva ed è pari a $\tfrac{1}{2}kA^2$.
- Con attrito viscoso si distinguono regime sottosmorzato (oscillazioni decrescenti), critico (ritorno più rapido senza oscillare) e sovrasmorzato.
- Il fattore di qualità $Q = \omega_0/(2\gamma)$ misura quanto poco l'oscillatore dissipa.
- Con forzante sinusoidale, a regime il sistema oscilla alla frequenza della forzante, con ampiezza e fase dipendenti da $\omega$.
- In risonanza l'ampiezza è circa $Q$ volte la deformazione statica: fenomeno sfruttato nei circuiti e temuto nelle strutture.
