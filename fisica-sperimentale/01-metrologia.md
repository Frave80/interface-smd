# Capitolo 1 — Metrologia

La **metrologia** è la scienza della misura: si occupa di definire le grandezze fisiche, di stabilire le unità con cui esprimerle, di costruire e confrontare i campioni e di valutare l'affidabilità dei risultati sperimentali. Prima di studiare qualsiasi legge della meccanica, della termodinamica o dell'elettromagnetismo è indispensabile capire che cosa significhi "misurare", quale linguaggio usare per comunicare un risultato numerico e come quantificare l'incertezza che inevitabilmente lo accompagna. Questo capitolo introduce il metodo sperimentale, il concetto di grandezza fisica e di unità di misura, il Sistema Internazionale, l'analisi dimensionale, le notazioni per scrivere numeri molto grandi o molto piccoli e, infine, la teoria elementare degli errori e delle cifre significative. Sono strumenti che accompagneranno lo studente di Ingegneria per tutto il corso e, più in generale, per tutta la vita professionale: un progetto ingegneristico è sempre, in ultima analisi, una catena di misure, stime e calcoli il cui valore dipende dalla correttezza con cui sono trattate le incertezze.

## 1.1 Metodo sperimentale

Il **metodo sperimentale**, detto anche metodo scientifico o galileiano, è il procedimento con cui la fisica costruisce la propria conoscenza della natura. Non si tratta di una ricetta rigida, ma di un insieme di atteggiamenti e regole che rendono una conoscenza controllabile, condivisibile e migliorabile. Il suo cuore è il confronto sistematico fra le previsioni di un modello e i risultati di misure eseguite in condizioni controllate e riproducibili. In questa sezione si discute prima che cosa si intenda in generale per scienza e poi quale posto occupi la fisica all'interno delle scienze naturali.

### 1.1.1 Scienza

Con il termine **scienza** si indica un corpo di conoscenze ottenuto mediante un metodo che garantisca l'oggettività dei risultati, cioè la loro indipendenza dall'osservatore, e la possibilità di sottoporli a verifica. La parola "oggettivo" va intesa in senso operativo: un risultato è oggettivo se un qualunque altro sperimentatore, ripetendo la stessa procedura con strumenti equivalenti, ottiene un risultato compatibile entro le incertezze dichiarate. Questa richiesta di **riproducibilità** distingue la conoscenza scientifica dall'opinione, dalla tradizione o dall'autorità.

Storicamente il metodo sperimentale moderno viene associato a Galileo Galilei, che all'inizio del Seicento propose di sostituire alle argomentazioni puramente logiche della filosofia naturale aristotelica le "sensate esperienze" e le "necessarie dimostrazioni". Le prime sono le osservazioni e gli esperimenti, eseguiti in modo da isolare il fenomeno di interesse dalle cause di disturbo; le seconde sono le deduzioni matematiche che, a partire da ipotesi, permettono di ricavare conseguenze quantitative da sottoporre a controllo. Il metodo si può schematizzare in alcune fasi, che nella pratica si intrecciano continuamente.

La prima fase è l'**osservazione** di un fenomeno e la scelta delle grandezze rilevanti per descriverlo. Già questa fase non è neutra: decidere che la caduta di un corpo dipende dall'altezza e dal tempo ma non dal colore del corpo è una scelta guidata dall'esperienza e da ipotesi implicite. La seconda fase è la formulazione di un'**ipotesi**, cioè di una relazione tra grandezze che si suppone valga; spesso l'ipotesi prende la forma di una legge matematica. La terza fase è l'**esperimento**: si progetta una situazione in cui le grandezze sono misurabili e le cause di disturbo sono controllate, si eseguono le misure e si stimano le incertezze. La quarta fase è la **verifica**: si confrontano le previsioni dell'ipotesi con i dati. Se il confronto è positivo l'ipotesi viene corroborata e può essere elevata al rango di **legge**; se è negativo l'ipotesi va modificata o abbandonata.

Un punto concettuale fondamentale, messo in luce dal filosofo Karl Popper, è che nessun numero finito di esperimenti può dimostrare definitivamente una legge generale, mentre un solo esperimento ben condotto e in disaccordo con essa è sufficiente a falsificarla. Si dice quindi che le teorie scientifiche sono **falsificabili**: un'affermazione che non può, neppure in linea di principio, essere smentita da un'osservazione non appartiene al dominio della scienza. Ciò non rende la scienza fragile o arbitraria: le leggi della meccanica newtoniana sono state confermate da innumerevoli esperimenti, e quando si è scoperto che falliscono (a velocità prossime a quella della luce o su scale atomiche) si è compreso che esse restano validissime all'interno di un preciso **ambito di validità**. Una buona teoria successiva, come la relatività ristretta, deve riprodurre la precedente nel limite in cui quest'ultima funziona.

Un altro elemento caratteristico è il ruolo del **modello**. La realtà fisica è sempre troppo complessa per essere descritta in tutti i dettagli; lo scienziato costruisce allora una rappresentazione semplificata che conserva gli aspetti essenziali. Il "punto materiale" della meccanica, il "gas perfetto" della termodinamica, il "filo inestensibile" e la "superficie liscia" sono esempi di modelli. Un modello non è vero o falso in assoluto: è adeguato o inadeguato a descrivere un certo fenomeno con una certa precisione. Il criterio di adeguatezza è ancora una volta sperimentale: il modello è buono se le sue previsioni concordano con le misure entro le incertezze richieste dall'applicazione.

### 1.1.2 Fisica

La **fisica** è la scienza naturale che studia i costituenti fondamentali della materia e le loro interazioni, cercando di descrivere i fenomeni mediante un numero ridotto di principi generali espressi in linguaggio matematico. Il termine deriva dal greco *physis*, "natura". Rispetto ad altre scienze, come la chimica o la biologia, la fisica si caratterizza per il livello di generalità a cui opera e per l'uso sistematico della matematica come linguaggio. Le leggi fisiche sono relazioni quantitative tra **grandezze fisiche**, cioè proprietà di un sistema che possono essere misurate.

Tradizionalmente la fisica si suddivide in **fisica classica** e **fisica moderna**. La fisica classica, sviluppata fino alla fine dell'Ottocento, comprende la meccanica (lo studio del moto e delle sue cause), la termodinamica (lo studio degli scambi di energia sotto forma di calore e lavoro), l'elettromagnetismo (lo studio dei fenomeni elettrici, magnetici e della luce) e l'ottica. La fisica moderna, nata nel Novecento, comprende la relatività, che modifica i concetti di spazio e tempo per velocità elevate, e la meccanica quantistica, necessaria per descrivere atomi, molecole e particelle subatomiche. Per gli scopi di un corso di Ingegneria del primo anno la fisica classica è largamente sufficiente: le velocità in gioco sono molto inferiori a quella della luce ($c \simeq 3\times10^{8}\ \mathrm{m/s}$) e le dimensioni dei sistemi sono molto maggiori di quelle atomiche ($\sim10^{-10}\ \mathrm{m}$).

È utile distinguere tra **fisica sperimentale** e **fisica teorica**, pur ricordando che si tratta di due facce dello stesso metodo. La fisica sperimentale progetta ed esegue misure, sviluppa strumenti e tecniche, valuta le incertezze; la fisica teorica costruisce modelli matematici, ne deduce le conseguenze e propone nuove previsioni da verificare. Nessuna delle due può fare a meno dell'altra: una teoria senza conferme sperimentali è una speculazione, mentre una raccolta di dati senza un quadro interpretativo non costituisce conoscenza. L'approccio di questo corso è appunto "sperimentale" nel senso che ogni concetto viene introdotto a partire dai fenomeni osservabili e ogni legge è accompagnata dalla discussione del suo ambito di validità.

Il legame tra fisica e ingegneria è diretto. L'ingegnere applica le leggi fisiche per progettare dispositivi, strutture e processi: il calcolo delle sollecitazioni di una trave usa la statica, il dimensionamento di uno scambiatore di calore usa la termodinamica, la progettazione di un motore elettrico usa l'elettromagnetismo. In ciascun caso l'ingegnere deve saper scegliere il modello più semplice adeguato al problema, stimare l'ordine di grandezza dei risultati, verificare la coerenza dimensionale delle formule e valutare l'effetto delle incertezze sui parametri di progetto. Sono esattamente le competenze che la metrologia e il metodo sperimentale intendono sviluppare.

Infine, va sottolineato che nella fisica la **misura** occupa un ruolo centrale e quasi definitorio. Una grandezza fisica è definita operativamente, cioè tramite la procedura con cui la si misura: la lunghezza è ciò che si misura con un metro campione, il tempo è ciò che si misura con un orologio. Questa **definizione operativa**, proposta in forma esplicita da Percy Bridgman nel Novecento ma implicita già in Galileo, garantisce che ogni concetto fisico sia ancorato a qualcosa di osservabile. Ne consegue che parlare di una grandezza senza specificare come la si misura, e con quale incertezza, è privo di significato fisico. Anche le costanti fondamentali, come la velocità della luce o la costante di Planck, sono oggi utilizzate come base per definire le unità di misura, a testimonianza dello stretto intreccio tra leggi della natura e pratica metrologica.

### Esercizio d'esempio

**Testo.** Per verificare l'ipotesi che il periodo $T$ delle piccole oscillazioni di un pendolo semplice sia indipendente dalla massa appesa, uno studente misura il tempo di 20 oscillazioni complete con due masse diverse, $m_1 = 0{,}100\ \mathrm{kg}$ e $m_2 = 0{,}300\ \mathrm{kg}$, a parità di lunghezza $L = 1{,}000\ \mathrm{m}$. Ottiene $t_1 = (40{,}2 \pm 0{,}2)\ \mathrm{s}$ e $t_2 = (40{,}0 \pm 0{,}2)\ \mathrm{s}$. L'ipotesi è corroborata? Il risultato è compatibile con la previsione teorica $T = 2\pi\sqrt{L/g}$ con $g = 9{,}81\ \mathrm{m/s^2}$?

**Soluzione.** Dividere per il numero di oscillazioni riduce l'incertezza relativa sul singolo periodo. Si ottiene

$$T_1 = \frac{t_1}{20} = (2{,}010 \pm 0{,}010)\ \mathrm{s}, \qquad T_2 = \frac{t_2}{20} = (2{,}000 \pm 0{,}010)\ \mathrm{s}.$$

La differenza è $T_1 - T_2 = 0{,}010\ \mathrm{s}$, mentre l'incertezza sulla differenza, sommando le incertezze massime, è $0{,}020\ \mathrm{s}$. Poiché la differenza è minore dell'incertezza, le due misure sono **compatibili**: i dati non permettono di distinguere un effetto della massa, e l'ipotesi è corroborata (non dimostrata). La previsione teorica vale

$$T_{\mathrm{teo}} = 2\pi\sqrt{\frac{1{,}000\ \mathrm{m}}{9{,}81\ \mathrm{m/s^2}}} \simeq 2{,}006\ \mathrm{s},$$

che cade all'interno di entrambi gli intervalli di misura. Il modello del pendolo semplice è quindi adeguato a descrivere l'esperimento con la precisione raggiunta.

### Punti chiave

- Il metodo sperimentale combina osservazione, ipotesi, esperimento e verifica, in un ciclo che si ripete.
- Un risultato scientifico deve essere riproducibile da altri sperimentatori con strumenti equivalenti.
- Le teorie sono falsificabili: gli esperimenti possono corroborarle o smentirle, mai dimostrarle in modo definitivo.
- Ogni legge fisica ha un ambito di validità; teorie più generali devono ricondursi alle precedenti nel limite opportuno.
- I modelli (punto materiale, gas perfetto, ecc.) sono semplificazioni adeguate entro una certa precisione.
- Le grandezze fisiche sono definite operativamente, tramite la procedura con cui si misurano.
- Per l'ingegneria la fisica classica è sufficiente quando $v \ll c$ e le dimensioni sono molto maggiori di quelle atomiche.

## 1.2 Grandezze fisiche

Una **grandezza fisica** è una proprietà di un fenomeno, di un corpo o di una sostanza che può essere espressa quantitativamente mediante un numero e un riferimento. Lunghezza, massa, tempo, temperatura, velocità, forza, energia, carica elettrica sono esempi di grandezze fisiche; bellezza, gusto o simpatia non lo sono, perché non esiste una procedura condivisa per misurarle. **Misurare** una grandezza significa confrontarla con un'altra grandezza della stessa specie, scelta come riferimento e detta **unità di misura**, e determinare quante volte l'unità è contenuta nella grandezza. Il risultato della misura è quindi sempre la coppia "valore numerico più unità", accompagnata da un'incertezza. In questa sezione si analizzano le unità, la distinzione tra grandezze fondamentali e derivate, i sistemi di unità, le conversioni e lo strumento potentissimo dell'analisi dimensionale.

### 1.2.1 Unità di misura

Se $G$ è una grandezza e $[G]_u$ l'unità scelta, la misura fornisce il numero puro $\{G\}$ tale che

$$G = \{G\}\,[G]_u .$$

Ad esempio, scrivere $L = 3{,}2\ \mathrm{m}$ significa che la lunghezza $L$ è pari a $3{,}2$ volte la lunghezza del metro. Il valore numerico dipende dalla scelta dell'unità, mentre la grandezza in sé no: la stessa lunghezza vale $320\ \mathrm{cm}$ o $0{,}0032\ \mathrm{km}$. Per questa ragione un numero privo di unità, quando riferito a una grandezza dimensionale, non ha alcun significato fisico e costituisce un errore grave in un elaborato tecnico.

Un'unità di misura deve soddisfare alcuni requisiti: deve essere **invariabile** nel tempo e nello spazio, **riproducibile** in laboratori diversi, **accessibile** con precisione adeguata e, preferibilmente, legata a fenomeni naturali universali piuttosto che a oggetti particolari. Storicamente le unità erano basate su oggetti campione: il metro era la distanza tra due tacche su una barra di platino-iridio conservata a Sèvres, il chilogrammo era la massa di un cilindro della stessa lega. Questi campioni, però, possono deteriorarsi o variare in modo impercettibile. Per tale motivo, con la revisione del 2019, tutte le unità del Sistema Internazionale sono definite fissando il valore numerico esatto di sette **costanti fondamentali**: la frequenza della transizione iperfina del cesio-133 $\Delta\nu_{\mathrm{Cs}}$, la velocità della luce nel vuoto $c$, la costante di Planck $h$, la carica elementare $e$, la costante di Boltzmann $k_B$, la costante di Avogadro $N_A$ e l'efficacia luminosa $K_{cd}$.

Così, il **secondo** è definito fissando $\Delta\nu_{\mathrm{Cs}} = 9\,192\,631\,770\ \mathrm{Hz}$; il **metro** è la distanza percorsa dalla luce nel vuoto in $1/299\,792\,458$ di secondo, essendo $c = 299\,792\,458\ \mathrm{m/s}$ esatto; il **chilogrammo** è definito fissando $h = 6{,}626\,070\,15\times10^{-34}\ \mathrm{J\,s}$. Il vantaggio è che chiunque disponga della tecnologia adeguata può realizzare le unità senza dover confrontare i propri strumenti con un oggetto unico.

### 1.2.2 Grandezze fondamentali e derivate

Non è necessario definire indipendentemente un'unità per ogni grandezza: molte grandezze sono legate tra loro da definizioni o leggi fisiche. Si sceglie allora un piccolo insieme di **grandezze fondamentali**, le cui unità vengono definite autonomamente, e si esprimono tutte le altre, dette **grandezze derivate**, tramite relazioni con le fondamentali. Nel Sistema Internazionale le grandezze fondamentali sono sette:

| Grandezza | Simbolo dimensionale | Unità SI | Simbolo |
|---|---|---|---|
| lunghezza | $\mathsf{L}$ | metro | m |
| massa | $\mathsf{M}$ | chilogrammo | kg |
| tempo | $\mathsf{T}$ | secondo | s |
| corrente elettrica | $\mathsf{I}$ | ampere | A |
| temperatura termodinamica | $\Theta$ | kelvin | K |
| quantità di sostanza | $\mathsf{N}$ | mole | mol |
| intensità luminosa | $\mathsf{J}$ | candela | cd |

Le grandezze derivate si ottengono come prodotti di potenze di quelle fondamentali. La velocità è il rapporto tra uno spostamento e un intervallo di tempo, quindi la sua unità è $\mathrm{m/s}$; l'accelerazione si misura in $\mathrm{m/s^2}$; la forza, per il secondo principio della dinamica, è massa per accelerazione e si misura in $\mathrm{kg\,m/s^2}$, unità a cui si dà il nome di **newton** (N). Altre unità derivate con nome proprio sono il **joule** ($\mathrm{J} = \mathrm{N\,m}$) per l'energia, il **watt** ($\mathrm{W} = \mathrm{J/s}$) per la potenza, il **pascal** ($\mathrm{Pa} = \mathrm{N/m^2}$) per la pressione, il **coulomb** ($\mathrm{C} = \mathrm{A\,s}$) per la carica, il **volt** ($\mathrm{V} = \mathrm{W/A}$) per la differenza di potenziale. La scelta di quali grandezze considerare fondamentali è in parte convenzionale: si sarebbe potuto scegliere la forza come fondamentale e derivare la massa, come avveniva nel sistema tecnico.

### 1.2.3 Grandezze adimensionali

Una grandezza si dice **adimensionale** quando le sue dimensioni si riducono a $1$, cioè quando tutti gli esponenti delle grandezze fondamentali sono nulli. Tipicamente le grandezze adimensionali nascono come rapporti tra grandezze omogenee: l'indice di rifrazione $n = c/v$, la deformazione relativa $\varepsilon = \Delta L/L$, il coefficiente di attrito $\mu$, il rendimento $\eta$ di una macchina. Il loro valore numerico non dipende dal sistema di unità adottato, e per questo hanno un ruolo privilegiato nella descrizione dei fenomeni: due sistemi fisici che hanno gli stessi valori dei parametri adimensionali rilevanti si comportano in modo simile, principio alla base della costruzione di modelli in scala (si pensi al numero di Reynolds nella fluidodinamica).

Un caso particolare è l'**angolo piano**. Definito come rapporto tra la lunghezza dell'arco $s$ e il raggio $r$, $\theta = s/r$, è adimensionale; tuttavia, per chiarezza, gli si attribuisce l'unità **radiante** (rad). Analogamente l'**angolo solido** $\Omega = A/r^2$ si misura in **steradianti** (sr). È importante ricordare che in tutte le formule della fisica in cui un angolo compare come argomento di funzioni trigonometriche sviluppate in serie, o in relazioni come $s = r\theta$ e $v = \omega r$, l'angolo deve essere espresso in radianti. Gli argomenti delle funzioni esponenziali, logaritmiche e trigonometriche devono sempre essere adimensionali: espressioni come $e^{t}$ con $t$ in secondi sono prive di senso, mentre $e^{-t/\tau}$ con $\tau$ tempo caratteristico è corretta.

### 1.2.4 Sistemi di unità di misura

Un **sistema di unità di misura** è un insieme coerente di unità fondamentali e derivate. Si dice **coerente** quando le unità derivate si ottengono da quelle fondamentali tramite le relazioni fisiche senza fattori numerici diversi da $1$: nel SI, $1\ \mathrm{N} = 1\ \mathrm{kg}\cdot1\ \mathrm{m/s^2}$. Il **Sistema Internazionale** (SI), adottato nel 1960 dalla Conferenza Generale dei Pesi e delle Misure e obbligatorio per legge in Italia e nell'Unione Europea per gli usi ufficiali, è quello che si utilizzerà in tutto il corso.

Altri sistemi storicamente rilevanti sono il **sistema CGS** (centimetro, grammo, secondo), ancora diffuso in alcuni ambiti della fisica teorica e dell'elettromagnetismo, in cui la forza si misura in dine ($1\ \mathrm{dyn} = 10^{-5}\ \mathrm{N}$) e l'energia in erg ($1\ \mathrm{erg} = 10^{-7}\ \mathrm{J}$); il **sistema tecnico** o pratico, in cui la forza è fondamentale e si misura in chilogrammo-forza ($1\ \mathrm{kgf} = 9{,}806\,65\ \mathrm{N}$, il peso di un chilogrammo in condizioni di gravità standard); il **sistema anglosassone** (imperiale e consuetudinario statunitense), con pollici, piedi, libbre, ancora in uso in molte normative e cataloghi tecnici. Esistono inoltre unità "tollerate" accanto al SI, come il litro, la tonnellata, l'ora, il bar, l'elettronvolt, che vanno sempre convertite con attenzione prima di inserirle nelle formule.

### 1.2.5 Conversioni di unità

Convertire un valore da un'unità a un'altra significa moltiplicarlo per un **fattore di conversione** uguale a $1$, cioè per un rapporto tra due espressioni equivalenti della stessa grandezza. Ad esempio, per esprimere $v = 90\ \mathrm{km/h}$ in $\mathrm{m/s}$:

$$v = 90\ \frac{\mathrm{km}}{\mathrm{h}}\cdot\frac{1000\ \mathrm{m}}{1\ \mathrm{km}}\cdot\frac{1\ \mathrm{h}}{3600\ \mathrm{s}} = 25\ \mathrm{m/s}.$$

Il metodo consiste nel trattare le unità come simboli algebrici che si semplificano tra numeratore e denominatore. Particolare attenzione richiedono le unità elevate a potenza: poiché $1\ \mathrm{cm} = 10^{-2}\ \mathrm{m}$, si ha $1\ \mathrm{cm^2} = 10^{-4}\ \mathrm{m^2}$ e $1\ \mathrm{cm^3} = 10^{-6}\ \mathrm{m^3}$; un errore frequente è convertire le aree o i volumi con il fattore lineare. Ad esempio una densità di $1\ \mathrm{g/cm^3}$ corrisponde a $10^{-3}\ \mathrm{kg}/10^{-6}\ \mathrm{m^3} = 10^{3}\ \mathrm{kg/m^3}$. Un'eccezione rilevante alle conversioni puramente moltiplicative è la temperatura: tra gradi Celsius e kelvin esiste una traslazione, $T[\mathrm{K}] = t[^\circ\mathrm{C}] + 273{,}15$, mentre le **differenze** di temperatura hanno lo stesso valore nelle due scale.

### 1.2.6 Operazioni tra grandezze con unità

Le grandezze fisiche obbediscono a regole algebriche precise. Si possono **sommare** o **sottrarre** soltanto grandezze **omogenee**, cioè con le stesse dimensioni, ed espresse nella stessa unità: $2\ \mathrm{m} + 30\ \mathrm{cm}$ va prima convertito in $2\ \mathrm{m} + 0{,}30\ \mathrm{m} = 2{,}30\ \mathrm{m}$, mentre $2\ \mathrm{m} + 3\ \mathrm{s}$ è privo di senso. Allo stesso modo si possono confrontare (uguaglianza, disuguaglianza) solo grandezze omogenee. Al contrario, si possono **moltiplicare** e **dividere** grandezze qualsiasi: il risultato ha come valore numerico il prodotto (o quoziente) dei valori e come unità il prodotto (o quoziente) delle unità. Ad esempio $F = 3\ \mathrm{N}$ applicata lungo uno spostamento $d = 2\ \mathrm{m}$ compie un lavoro $W = 6\ \mathrm{N\,m} = 6\ \mathrm{J}$. Le potenze e le radici agiscono analogamente sulle unità: $\sqrt{9\ \mathrm{m^2}} = 3\ \mathrm{m}$.

Una buona pratica consiste nel portare sempre le unità nei calcoli, almeno nei passaggi finali: oltre a ottenere direttamente l'unità del risultato, si ha un controllo immediato della correttezza delle formule. Se il calcolo di una velocità fornisce un risultato in $\mathrm{m^2/s}$, c'è certamente un errore.

### 1.2.7 Analisi dimensionale

L'**analisi dimensionale** studia le relazioni tra grandezze fisiche sulla base delle loro dimensioni. Si indica con $[G]$ la **dimensione** della grandezza $G$, espressa come prodotto di potenze delle dimensioni fondamentali:

$$[G] = \mathsf{L}^{a}\,\mathsf{M}^{b}\,\mathsf{T}^{c}\,\mathsf{I}^{d}\,\Theta^{e}\,\mathsf{N}^{f}\,\mathsf{J}^{g}.$$

Ad esempio $[v] = \mathsf{L\,T^{-1}}$, $[F] = \mathsf{M\,L\,T^{-2}}$, $[E] = \mathsf{M\,L^2\,T^{-2}}$. Il principio fondamentale è il **principio di omogeneità dimensionale**: ogni equazione fisicamente corretta deve avere le stesse dimensioni in entrambi i membri e in ciascun addendo. Questo principio ha due usi principali.

Il primo è la **verifica** delle formule: se nella soluzione di un problema si ottiene $x = \tfrac12 a t$, l'analisi mostra subito che $[a t] = \mathsf{L\,T^{-1}} \neq \mathsf{L}$, quindi la formula è sbagliata (quella corretta è $x = \tfrac12 a t^2$). Va sottolineato che l'omogeneità è condizione necessaria ma non sufficiente: una formula dimensionalmente corretta può comunque essere errata per un fattore numerico adimensionale.

Il secondo uso è la **deduzione** della forma di una legge. Supponiamo che il periodo $T$ di un pendolo semplice dipenda dalla lunghezza $L$, dalla massa $m$ e dall'accelerazione di gravità $g$, nella forma $T = k\,L^{\alpha} m^{\beta} g^{\gamma}$ con $k$ adimensionale. Imponendo l'omogeneità:

$$\mathsf{T} = \mathsf{L}^{\alpha}\,\mathsf{M}^{\beta}\,(\mathsf{L\,T^{-2}})^{\gamma} \;\Rightarrow\; \begin{cases}\alpha + \gamma = 0\\ \beta = 0\\ -2\gamma = 1\end{cases} \;\Rightarrow\; \gamma = -\tfrac12,\ \alpha = \tfrac12,\ \beta = 0,$$

da cui $T = k\sqrt{L/g}$. Senza risolvere alcuna equazione del moto si è scoperto che il periodo non dipende dalla massa e scala con la radice della lunghezza; solo la costante $k = 2\pi$ richiede la teoria completa o un esperimento. Questa tecnica, formalizzata dal **teorema di Buckingham** (o teorema $\Pi$), è uno strumento potente per stimare ordini di grandezza e per progettare esperimenti, ma presuppone di conoscere a priori tutte le grandezze da cui il fenomeno dipende.

### Esercizio d'esempio

**Testo.** La forza di resistenza aerodinamica su un corpo che si muove in un fluido ad alta velocità dipende dalla densità del fluido $\rho$, dalla velocità $v$ e dall'area frontale $A$. (a) Determinare con l'analisi dimensionale la forma della legge $F = k\,\rho^{\alpha} v^{\beta} A^{\gamma}$. (b) Calcolare la forza su un'automobile con $A = 2{,}2\ \mathrm{m^2}$, $v = 108\ \mathrm{km/h}$, in aria con $\rho = 1{,}2\ \mathrm{kg/m^3}$, assumendo $k = 0{,}15$.

**Soluzione.** (a) Le dimensioni sono $[F] = \mathsf{M\,L\,T^{-2}}$, $[\rho] = \mathsf{M\,L^{-3}}$, $[v] = \mathsf{L\,T^{-1}}$, $[A] = \mathsf{L^2}$. Imponendo l'omogeneità:

$$\mathsf{M\,L\,T^{-2}} = \mathsf{M}^{\alpha}\mathsf{L}^{-3\alpha}\,\mathsf{L}^{\beta}\mathsf{T}^{-\beta}\,\mathsf{L}^{2\gamma}.$$

Per la massa $\alpha = 1$; per il tempo $\beta = 2$; per la lunghezza $1 = -3 + 2 + 2\gamma$, cioè $\gamma = 1$. Quindi $F = k\,\rho\,v^2 A$.

(b) Si converte la velocità: $v = 108/3{,}6\ \mathrm{m/s} = 30\ \mathrm{m/s}$. Allora

$$F = 0{,}15\cdot 1{,}2\ \mathrm{kg/m^3}\cdot(30\ \mathrm{m/s})^2\cdot 2{,}2\ \mathrm{m^2} = 0{,}15\cdot1{,}2\cdot900\cdot2{,}2\ \mathrm{kg\,m/s^2}\simeq 3{,}6\times10^{2}\ \mathrm{N}.$$

Le unità si combinano correttamente in newton, confermando la coerenza del risultato.

### Punti chiave

- Una misura è il rapporto tra la grandezza e l'unità: il risultato è sempre "numero + unità + incertezza".
- Dal 2019 le sette unità fondamentali del SI sono definite fissando i valori esatti di sette costanti fondamentali.
- Le grandezze derivate si esprimono come prodotti di potenze delle fondamentali; molte unità derivate hanno nome proprio (N, J, W, Pa, ...).
- Le grandezze adimensionali non dipendono dal sistema di unità; gli argomenti di funzioni trascendenti devono essere adimensionali e gli angoli vanno in radianti.
- Le conversioni si eseguono moltiplicando per fattori uguali a 1; attenzione alle potenze delle unità e alle scale di temperatura.
- Si sommano e confrontano solo grandezze omogenee; prodotti e quozienti combinano anche le unità.
- L'analisi dimensionale verifica le formule e ne deduce la struttura, a meno di costanti adimensionali.

## 1.3 Notazione

La fisica si occupa di fenomeni che coprono un intervallo di scale enorme. Il raggio di un protone è dell'ordine di $10^{-15}\ \mathrm{m}$, quello dell'universo osservabile dell'ordine di $10^{26}\ \mathrm{m}$; la massa di un elettrone vale circa $9{,}11\times10^{-31}\ \mathrm{kg}$, quella del Sole circa $2\times10^{30}\ \mathrm{kg}$. Scrivere questi numeri in forma decimale ordinaria, con decine di zeri, sarebbe scomodo, poco leggibile e soprattutto fonte di errori di trascrizione. Inoltre la scrittura ordinaria non permette di distinguere quali cifre siano state effettivamente misurate e quali siano semplici "segnaposto" per indicare la posizione della virgola. Per risolvere entrambi i problemi si usano le potenze di dieci, organizzate in due convenzioni strettamente imparentate: la **notazione scientifica** e la **notazione ingegneristica**. Questa sezione ne illustra le regole, i vantaggi e l'uso combinato con i prefissi del Sistema Internazionale.

### 1.3.1 Notazione scientifica

In **notazione scientifica** (detta anche notazione esponenziale normalizzata) un numero reale $x \neq 0$ viene scritto nella forma

$$x = \pm\, a \times 10^{n}, \qquad 1 \le a < 10,\quad n \in \mathbb{Z}.$$

Il numero $a$ si chiama **mantissa** (o coefficiente) e contiene tutte le cifre significative del valore; l'intero $n$ si chiama **esponente** o **ordine di grandezza**. La condizione $1 \le a < 10$ rende la rappresentazione unica: esiste un solo modo di scrivere un dato numero in notazione scientifica. Ad esempio la velocità della luce si scrive $c = 2{,}997\,924\,58\times10^{8}\ \mathrm{m/s}$, la carica elementare $e = 1{,}602\,176\,634\times10^{-19}\ \mathrm{C}$, la distanza media Terra–Sole $1{,}496\times10^{11}\ \mathrm{m}$.

Per convertire un numero in notazione scientifica si sposta la virgola fino a ottenere una sola cifra non nulla alla sua sinistra, contando gli spostamenti: se la virgola si sposta verso sinistra l'esponente è positivo e pari al numero di posizioni, se si sposta verso destra l'esponente è negativo. Così $45\,300 = 4{,}53\times10^{4}$ (quattro posizioni a sinistra) e $0{,}000\,72 = 7{,}2\times10^{-4}$ (quattro posizioni a destra). Il procedimento inverso consente di tornare alla forma decimale.

Il primo grande vantaggio di questa notazione è la **compattezza**. Il secondo, altrettanto importante, è la **chiarezza sulle cifre significative**. Se si scrive che una distanza vale $1500\ \mathrm{m}$, non è chiaro se gli zeri finali siano stati misurati (precisione al metro) oppure servano solo a fissare l'ordine di grandezza (precisione alle centinaia di metri). In notazione scientifica l'ambiguità scompare: $1{,}5\times10^{3}\ \mathrm{m}$ dichiara due cifre significative, $1{,}500\times10^{3}\ \mathrm{m}$ ne dichiara quattro. Tutte le cifre della mantissa sono, per convenzione, significative.

Il terzo vantaggio riguarda la **facilità di calcolo**. Le proprietà delle potenze permettono di eseguire mentalmente prodotti e quozienti: si moltiplicano (o dividono) le mantisse e si sommano (o sottraggono) gli esponenti,

$$(a\times10^{n})(b\times10^{m}) = (ab)\times10^{n+m}, \qquad \frac{a\times10^{n}}{b\times10^{m}} = \frac{a}{b}\times10^{n-m}.$$

Se il prodotto delle mantisse esce dall'intervallo $[1,10)$, si rinormalizza: $(4\times10^{3})(5\times10^{2}) = 20\times10^{5} = 2\times10^{6}$. Per le potenze si eleva la mantissa e si moltiplica l'esponente: $(3\times10^{4})^2 = 9\times10^{8}$. Per le radici quadrate conviene prima rendere pari l'esponente: $\sqrt{1{,}6\times10^{-5}} = \sqrt{16\times10^{-6}} = 4\times10^{-3}$. Le somme e le differenze richiedono invece di portare i due numeri allo stesso esponente: $3{,}2\times10^{5} + 4{,}0\times10^{3} = 3{,}2\times10^{5} + 0{,}040\times10^{5} = 3{,}24\times10^{5}$. Questo esempio mostra anche che, quando due addendi differiscono di molti ordini di grandezza, il più piccolo diventa trascurabile rispetto alla precisione del più grande.

Strettamente legato alla notazione scientifica è il concetto di **ordine di grandezza**, cioè la potenza di dieci più vicina al valore della grandezza. Convenzionalmente si arrotonda la mantissa: se $a < \sqrt{10} \simeq 3{,}16$ l'ordine di grandezza è $10^{n}$, altrimenti è $10^{n+1}$ (molti testi usano più semplicemente la soglia 5). L'altezza di una persona, $1{,}75\ \mathrm{m}$, ha ordine di grandezza $10^{0}\ \mathrm{m}$; la massa di un'automobile, $1{,}3\times10^{3}\ \mathrm{kg}$, ha ordine $10^{3}\ \mathrm{kg}$. Le **stime di ordini di grandezza** (talvolta chiamate "problemi di Fermi") sono uno strumento quotidiano del fisico e dell'ingegnere: permettono di valutare in pochi secondi se un risultato è plausibile, se un effetto è trascurabile rispetto a un altro, se un progetto è realistico. Ad esempio, prima di eseguire un calcolo dettagliato dell'energia cinetica di un treno ($m\sim10^{5}\ \mathrm{kg}$, $v\sim10^{2}/3{,}6\ \mathrm{m/s}\sim 3\times10^{1}\ \mathrm{m/s}$) si può stimare $E\sim\tfrac12\cdot10^{5}\cdot10^{3}\ \mathrm{J}\sim 5\times10^{7}\ \mathrm{J}$, un valore di riferimento con cui confrontare il calcolo preciso.

Si osservi infine che nei calcolatori e nei linguaggi di programmazione la notazione scientifica viene scritta con la lettera E: `6.022E23` significa $6{,}022\times10^{23}$. Nei testi e negli elaborati tecnici questa forma va evitata a favore della scrittura con la potenza di dieci esplicita.

### 1.3.2 Notazione ingegneristica

La **notazione ingegneristica** è una variante della notazione scientifica in cui l'esponente della potenza di dieci è vincolato a essere un **multiplo di tre**:

$$x = \pm\, a \times 10^{3k}, \qquad 1 \le a < 1000,\quad k \in \mathbb{Z}.$$

Di conseguenza la mantissa può avere una, due o tre cifre prima della virgola. Ad esempio $45\,300\ \mathrm{m}$ si scrive $45{,}3\times10^{3}\ \mathrm{m}$, $0{,}000\,72\ \mathrm{A}$ diventa $720\times10^{-6}\ \mathrm{A}$, una capacità di $4{,}7\times10^{-8}\ \mathrm{F}$ diventa $47\times10^{-9}\ \mathrm{F}$.

La ragione di questa scelta è la corrispondenza diretta con i **prefissi del Sistema Internazionale**, che sono definiti (salvo eccezioni) proprio per potenze di mille. Ogni potenza $10^{3k}$ può essere sostituita dal prefisso corrispondente, ottenendo una scrittura immediata e leggibile: $45{,}3\times10^{3}\ \mathrm{m} = 45{,}3\ \mathrm{km}$, $720\times10^{-6}\ \mathrm{A} = 720\ \mathrm{\mu A}$, $47\times10^{-9}\ \mathrm{F} = 47\ \mathrm{nF}$. I prefissi principali sono riportati nella tabella.

| Fattore | Prefisso | Simbolo | Fattore | Prefisso | Simbolo |
|---|---|---|---|---|---|
| $10^{3}$ | kilo | k | $10^{-3}$ | milli | m |
| $10^{6}$ | mega | M | $10^{-6}$ | micro | µ |
| $10^{9}$ | giga | G | $10^{-9}$ | nano | n |
| $10^{12}$ | tera | T | $10^{-12}$ | pico | p |
| $10^{15}$ | peta | P | $10^{-15}$ | femto | f |
| $10^{18}$ | exa | E | $10^{-18}$ | atto | a |

Esistono anche i prefissi non multipli di tre, come etto ($10^{2}$, h), deca ($10^{1}$, da), deci ($10^{-1}$, d) e centi ($10^{-2}$, c), di uso comune nella vita quotidiana (centimetro, decilitro, ettogrammo) ma meno impiegati nella pratica ingegneristica. Recentemente il SI ha aggiunto anche prefissi per scale estreme (ronna, quetta, ronto, quecto), utili ad esempio nella quantificazione dei dati informatici o delle masse planetarie.

Alcune regole d'uso dei prefissi meritano attenzione. Il prefisso si scrive attaccato al simbolo dell'unità, senza spazio né punto, e insieme formano un nuovo simbolo che può essere elevato a potenza: $\mathrm{km^2}$ significa $(\mathrm{km})^2 = 10^{6}\ \mathrm{m^2}$, non $\mathrm{k}(\mathrm{m^2}) = 10^{3}\ \mathrm{m^2}$. Non si usano prefissi composti: si scrive $\mathrm{ns}$ e non $\mathrm{m\mu s}$. Le maiuscole e minuscole sono significative: $\mathrm{mW}$ (milliwatt) e $\mathrm{MW}$ (megawatt) differiscono di nove ordini di grandezza. Un'eccezione storica riguarda il chilogrammo: pur essendo l'unità fondamentale di massa, contiene già il prefisso "kilo", e i multipli e sottomultipli si formano a partire dal grammo (si scrive $\mathrm{mg}$ e non $\mathrm{\mu kg}$).

La notazione ingegneristica è particolarmente diffusa in elettronica e in elettrotecnica, dove i valori di resistenze, capacità, induttanze, correnti e frequenze coprono molti ordini di grandezza e vengono letti e comunicati quotidianamente: un resistore da $4{,}7\ \mathrm{k\Omega}$, un condensatore da $100\ \mathrm{nF}$, una frequenza di clock di $3{,}2\ \mathrm{GHz}$. Anche gli strumenti di misura digitali (multimetri, oscilloscopi) e molte calcolatrici scientifiche dispongono di una modalità "ENG" che visualizza i risultati in questa forma.

Il prezzo da pagare per la maggiore leggibilità è una certa perdita di informazione sulle cifre significative. Scrivere $1500\ \mathrm{m} = 1{,}5\ \mathrm{km}$ è una buona soluzione se le cifre significative sono due, ma se un valore come $120\ \mathrm{kHz}$ ha due sole cifre significative la notazione ingegneristica non lo rende evidente, perché lo zero finale potrebbe essere misurato o no. In questi casi si può scrivere $0{,}12\ \mathrm{MHz}$ oppure ricorrere alla notazione scientifica $1{,}2\times10^{5}\ \mathrm{Hz}$, oppure ancora, cosa sempre raccomandabile, accompagnare il valore con la sua incertezza: $(120\pm5)\ \mathrm{kHz}$ non lascia dubbi. In sintesi, la notazione scientifica è preferibile nei calcoli e quando si vuole evidenziare la precisione, quella ingegneristica nella comunicazione tecnica di valori di componenti e nella lettura di strumenti; un professionista deve saper passare rapidamente dall'una all'altra.

Un'ultima osservazione pratica riguarda il **separatore decimale**. Nella convenzione italiana ed europea, e nelle raccomandazioni del SI, la virgola è ammessa come separatore decimale, mentre nei paesi anglosassoni si usa il punto. Per evitare confusione, le cifre di numeri lunghi si raggruppano a tre a tre con uno spazio sottile, mai con punti o virgole: si scrive $299\,792\,458$ e non $299.792.458$. Tra il valore numerico e il simbolo dell'unità si lascia sempre uno spazio ($25\ \mathrm{m/s}$, non $25\mathrm{m/s}$), con la sola eccezione dei simboli di grado, primo e secondo angolare.

### Esercizio d'esempio

**Testo.** Un filo di rame ha sezione circolare di diametro $d = 0{,}50\ \mathrm{mm}$ ed è lungo $L = 25\ \mathrm{m}$. La resistività del rame vale $\rho = 1{,}7\times10^{-8}\ \mathrm{\Omega\,m}$. Calcolare la resistenza $R = \rho L / A$, esprimendo i passaggi in notazione scientifica e il risultato finale in notazione ingegneristica.

**Soluzione.** Si converte il diametro in metri: $d = 0{,}50\times10^{-3}\ \mathrm{m} = 5{,}0\times10^{-4}\ \mathrm{m}$. L'area della sezione è

$$A = \frac{\pi d^2}{4} = \frac{\pi\,(5{,}0\times10^{-4}\ \mathrm{m})^2}{4} = \frac{\pi\cdot25\times10^{-8}}{4}\ \mathrm{m^2} \simeq 1{,}96\times10^{-7}\ \mathrm{m^2}.$$

La lunghezza è $L = 2{,}5\times10^{1}\ \mathrm{m}$. Quindi

$$R = \frac{(1{,}7\times10^{-8}\ \mathrm{\Omega\,m})(2{,}5\times10^{1}\ \mathrm{m})}{1{,}96\times10^{-7}\ \mathrm{m^2}} = \frac{4{,}25\times10^{-7}}{1{,}96\times10^{-7}}\ \mathrm{\Omega} \simeq 2{,}2\ \mathrm{\Omega}.$$

Il risultato ha due cifre significative, come i dati meno precisi. In notazione ingegneristica, poiché l'esponente è $0$, il valore resta $2{,}2\ \mathrm{\Omega}$; se lo si volesse esprimere in milliohm si scriverebbe $2{,}2\times10^{3}\ \mathrm{m\Omega}$, forma corretta ma meno naturale. Una stima preliminare dell'ordine di grandezza ($10^{-8}\cdot10^{1}/10^{-7} = 10^{0}\ \mathrm{\Omega}$) conferma la plausibilità del risultato.

### Punti chiave

- La notazione scientifica scrive un numero come $a\times10^{n}$ con $1\le a<10$: rappresentazione unica e compatta.
- Tutte le cifre della mantissa sono significative: la notazione scientifica elimina l'ambiguità degli zeri finali.
- Nei prodotti si moltiplicano le mantisse e si sommano gli esponenti; nelle somme si porta tutto allo stesso esponente.
- L'ordine di grandezza è la potenza di dieci più vicina al valore; le stime di Fermi servono a controllare la plausibilità dei risultati.
- La notazione ingegneristica usa esponenti multipli di tre ($1\le a<1000$) e si abbina ai prefissi SI (k, M, G, m, µ, n, ...).
- I prefissi si attaccano al simbolo e l'eventuale potenza si applica all'insieme: $1\ \mathrm{km^2} = 10^{6}\ \mathrm{m^2}$.
- Per comunicare la precisione senza ambiguità è sempre preferibile indicare esplicitamente l'incertezza.

## 1.4 Errori e cifre significative

Nessuna misura è perfetta. Ripetendo più volte la misura della stessa grandezza con lo stesso strumento si ottengono in generale valori leggermente diversi; usando strumenti diversi si possono ottenere valori sistematicamente spostati. Il **valore vero** di una grandezza è un concetto ideale, inaccessibile per principio: ciò che si può fare è fornire una **miglior stima** del valore e un intervallo, detto **incertezza** (o, con terminologia tradizionale, **errore**), entro il quale si ritiene ragionevolmente che il valore vero si trovi. Il risultato di una misura si scrive quindi nella forma

$$G = (\bar{G} \pm \delta G)\ [\text{unità}],$$

dove $\bar{G}$ è la miglior stima e $\delta G$ l'**incertezza assoluta**. Il rapporto $\delta G/|\bar G|$ è l'**incertezza relativa**, adimensionale, spesso espressa in percentuale; essa misura la **precisione** della misura e permette di confrontare la qualità di misure di grandezze diverse. È opportuno chiarire che la parola "errore" in questo contesto non indica uno sbaglio dello sperimentatore, ma l'inevitabile scarto tra valore misurato e valore vero. Gli errori grossolani (lettura sbagliata di una scala, trascrizione errata, strumento guasto) non rientrano nella teoria degli errori e vanno eliminati ripetendo la misura. Le incertezze propriamente dette si classificano in due grandi categorie, sistematiche e statistiche, con proprietà e rimedi molto diversi.

### 1.4.1 Errore sistematico

Un **errore sistematico** è un errore che agisce sempre nello stesso verso e con la stessa entità, o comunque secondo una legge determinata, in tutte le ripetizioni di una misura eseguita nelle stesse condizioni. Le sue cause tipiche sono: uno strumento **mal tarato** (una bilancia che segna $5\ \mathrm{g}$ anche a piatto vuoto, un cronometro che ritarda), un **difetto di metodo** (trascurare l'attrito o la resistenza dell'aria quando non sono trascurabili, misurare una tensione con un voltmetro di resistenza interna troppo bassa che perturba il circuito), un **errore di parallasse** sistematico dovuto alla posizione dell'occhio, condizioni ambientali diverse da quelle di taratura (temperatura che dilata un metro metallico).

La caratteristica decisiva degli errori sistematici è che **non si riducono ripetendo la misura**: la media di mille letture di una bilancia starata è sbagliata quanto la singola lettura. Essi influenzano l'**accuratezza** (o esattezza) della misura, cioè la vicinanza della miglior stima al valore vero, e non la sua precisione. Per individuarli occorre cambiare qualcosa: confrontare lo strumento con un campione di riferimento (operazione di **taratura**), misurare la stessa grandezza con metodi indipendenti, variare le condizioni sperimentali e osservare se il risultato cambia. Una volta individuato, un errore sistematico può essere corretto (ad esempio sottraendo la lettura a vuoto, detta **offset** o errore di zero) oppure, se non è eliminabile, stimato e incluso nell'incertezza complessiva.

Un caso particolare di incertezza di tipo sistematico è quella legata alla **sensibilità** dello strumento, cioè alla più piccola variazione della grandezza che lo strumento è in grado di apprezzare (la risoluzione: $1\ \mathrm{mm}$ per un righello, $0{,}01\ \mathrm{mm}$ per un micrometro, $0{,}01\ \mathrm{s}$ per un cronometro digitale). Se ripetendo la misura si ottiene sempre lo stesso valore, l'unica incertezza stimabile è legata alla risoluzione: convenzionalmente si assume come incertezza massima metà della divisione più piccola, oppure la divisione intera, a seconda delle convenzioni adottate e della possibilità di interpolare.

### 1.4.2 Errore statistico

Un **errore statistico** (o **casuale**, o accidentale) è dovuto a una moltitudine di piccole cause incontrollabili che agiscono in modo variabile da una misura all'altra: fluttuazioni di temperatura, vibrazioni, rumore elettrico, il tempo di reazione dell'operatore che preme il pulsante del cronometro ora un po' prima ora un po' dopo. Gli errori statistici spostano il risultato con uguale probabilità in eccesso e in difetto e si manifestano come **dispersione** dei valori ottenuti ripetendo la misura. Essi determinano la **precisione** della misura.

A differenza di quelli sistematici, gli errori statistici possono essere trattati con gli strumenti della statistica e **si riducono aumentando il numero di misure**. Date $N$ misure $x_1, x_2, \dots, x_N$ della stessa grandezza, la miglior stima del valore vero è la **media aritmetica**

$$\bar{x} = \frac{1}{N}\sum_{i=1}^{N} x_i .$$

La dispersione delle singole misure attorno alla media è descritta dalla **deviazione standard campionaria**

$$\sigma_x = \sqrt{\frac{1}{N-1}\sum_{i=1}^{N}(x_i - \bar{x})^2},$$

dove il denominatore $N-1$ (invece di $N$) tiene conto del fatto che la media è stata calcolata dagli stessi dati, perdendo un grado di libertà. La deviazione standard rappresenta l'incertezza tipica della **singola** misura e non diminuisce con $N$: tende a un valore caratteristico del procedimento. L'incertezza sulla **media** è invece la **deviazione standard della media**

$$\sigma_{\bar x} = \frac{\sigma_x}{\sqrt{N}},$$

che decresce come $1/\sqrt{N}$: quadruplicando il numero di misure si dimezza l'incertezza. Questo andamento mostra però anche i limiti del procedimento: per guadagnare un fattore dieci in precisione servono cento volte più misure, ed è inutile spingere l'incertezza statistica molto al di sotto di quella sistematica o della risoluzione dello strumento.

Quando le cause di errore casuale sono numerose, indipendenti e di piccola entità, la distribuzione dei risultati tende a una **distribuzione gaussiana** (o normale), come garantito dal teorema del limite centrale. Per una gaussiana circa il 68% delle misure cade entro $\pm\sigma$ dalla media, il 95% entro $\pm2\sigma$ e il 99,7% entro $\pm3\sigma$. Ciò fornisce un'interpretazione probabilistica dell'incertezza: dichiarare $\bar x \pm \sigma_{\bar x}$ significa affermare che il valore vero cade nell'intervallo con probabilità di circa il 68%. Due misure della stessa grandezza si dicono **compatibili** se la loro differenza è minore di una piccola multipla (tipicamente due o tre volte) dell'incertezza combinata.

### 1.4.3 Propagazione degli errori

Molto spesso la grandezza di interesse non viene misurata direttamente, ma calcolata a partire da altre grandezze misurate: si parla di **misura indiretta**. Ad esempio la densità di un cilindro si ottiene da massa, diametro e altezza. Occorre allora stabilire come le incertezze sulle grandezze misurate si **propagano** sul risultato. Sia $q = f(x, y, \dots)$ con incertezze $\delta x, \delta y, \dots$ piccole. Sviluppando $f$ al primo ordine si ottiene la stima dell'**incertezza massima**

$$\delta q = \left|\frac{\partial f}{\partial x}\right|\delta x + \left|\frac{\partial f}{\partial y}\right|\delta y + \dots$$

Questa formula è conservativa: assume che tutti gli errori si combinino nel modo più sfavorevole. Se invece le incertezze sono **statistiche e indipendenti**, è improbabile che si sommino tutte con lo stesso segno, e la stima corretta è la **somma in quadratura**

$$\delta q = \sqrt{\left(\frac{\partial f}{\partial x}\delta x\right)^2 + \left(\frac{\partial f}{\partial y}\delta y\right)^2 + \dots}$$

Da queste formule generali discendono alcune regole pratiche. Per **somme e differenze**, $q = x \pm y$, si sommano le **incertezze assolute** (in quadratura nel caso statistico): $\delta q = \delta x + \delta y$. Ciò rende critica la differenza tra due grandezze quasi uguali: l'incertezza assoluta resta quella dei dati, ma l'incertezza relativa può diventare enorme. Per **prodotti e quozienti**, $q = xy$ o $q = x/y$, si sommano le **incertezze relative**: $\delta q/|q| = \delta x/|x| + \delta y/|y|$. Per una **potenza**, $q = x^n$, l'incertezza relativa si moltiplica per l'esponente: $\delta q/|q| = |n|\,\delta x/|x|$. Per il prodotto per una **costante esatta**, $q = kx$, si ha $\delta q = |k|\delta x$.

Queste regole hanno conseguenze pratiche immediate per la progettazione di un esperimento: conviene concentrare gli sforzi sulla grandezza che contribuisce maggiormente all'incertezza finale, in particolare su quelle che compaiono con esponente elevato. Nel calcolo del volume di una sfera, $V = \tfrac{4}{3}\pi r^3$, un'incertezza relativa dell'1% sul raggio si traduce in un'incertezza del 3% sul volume.

### 1.4.4 Cifre significative

Le **cifre significative** di un numero che rappresenta una misura sono le cifre note con certezza più la prima cifra incerta. Esse esprimono, in modo implicito, la precisione del valore. Le regole per contarle sono: tutte le cifre diverse da zero sono significative; gli zeri compresi tra cifre non nulle sono significativi ($3{,}05$ ha tre cifre significative); gli zeri iniziali non sono significativi, perché indicano solo la posizione della virgola ($0{,}0047$ ha due cifre significative); gli zeri finali dopo la virgola sono significativi ($2{,}50$ ha tre cifre significative, e scriverlo come $2{,}5$ significherebbe dichiarare una precisione minore); gli zeri finali di un numero intero sono ambigui, e l'ambiguità si risolve con la notazione scientifica.

Quando si dispone esplicitamente dell'incertezza, il numero di cifre significative del risultato è dettato da essa. La regola generale è: **l'incertezza si arrotonda a una cifra significativa** (o due, se la prima è 1 o 2), e **la miglior stima si arrotonda alla stessa posizione decimale dell'incertezza**. Ad esempio, un calcolo che fornisce $g = 9{,}8237\ \mathrm{m/s^2}$ con $\delta g = 0{,}0472\ \mathrm{m/s^2}$ va scritto $g = (9{,}82 \pm 0{,}05)\ \mathrm{m/s^2}$. Scrivere $(9{,}8237 \pm 0{,}0472)\ \mathrm{m/s^2}$ è scorretto, perché le ultime cifre non hanno significato fisico; scrivere $(9{,}8 \pm 0{,}05)\ \mathrm{m/s^2}$ è altrettanto scorretto perché la stima è troncata prima della posizione dell'incertezza.

In assenza di incertezze esplicite si usano regole approssimate. Nei **prodotti e quozienti** il risultato deve avere tante cifre significative quante ne ha il fattore che ne ha meno: $3{,}2\times 1{,}456 = 4{,}6592 \to 4{,}7$. Nelle **somme e differenze** il risultato si arrotonda alla posizione decimale del termine meno preciso: $12{,}1 + 0{,}352 = 12{,}452 \to 12{,}5$. I numeri **esatti** (come il $2$ in $2\pi r$, o il numero di oggetti contati) e le costanti definite esattamente non limitano il numero di cifre significative. Durante i calcoli intermedi conviene mantenere una o due cifre in più del necessario e arrotondare solo il risultato finale, per evitare l'accumulo di errori di arrotondamento.

### 1.4.5 Arrotondamenti

L'**arrotondamento** è l'operazione con cui si riduce il numero di cifre di un valore. La regola standard è la seguente: si individua l'ultima cifra da conservare e si osserva la cifra successiva; se essa è minore di 5, l'ultima cifra conservata resta invariata (arrotondamento per **difetto**); se è maggiore di 5, o uguale a 5 seguita da cifre non tutte nulle, l'ultima cifra conservata si aumenta di uno (arrotondamento per **eccesso**). Così $2{,}743 \to 2{,}74$ e $2{,}747 \to 2{,}75$ arrotondando a tre cifre significative.

Il caso in cui la cifra eliminata è esattamente 5 (seguita solo da zeri) richiede una convenzione. La regola scolastica arrotonda sempre per eccesso, ma ciò introduce una piccola distorsione sistematica verso l'alto quando si arrotondano molti valori. Per questo nelle norme tecniche e nei calcolatori si adotta spesso la regola dell'**arrotondamento al pari** (detto anche arrotondamento del banchiere): si arrotonda in modo che l'ultima cifra conservata sia pari. Così $2{,}745 \to 2{,}74$ e $2{,}755 \to 2{,}76$. In media metà dei casi si arrotonda per eccesso e metà per difetto, eliminando la distorsione.

Va evitato il cosiddetto **doppio arrotondamento**: arrotondare $2{,}7449$ prima a $2{,}745$ e poi a $2{,}75$ dà un risultato sbagliato, poiché l'arrotondamento diretto a tre cifre fornisce $2{,}74$. L'arrotondamento va sempre eseguito in un solo passo partendo dal valore completo. Infine, va distinto l'arrotondamento dal **troncamento**, che consiste nel semplice scarto delle cifre in eccesso: il troncamento produce un errore sempre dello stesso segno ed è da evitare nella presentazione dei risultati, anche se è usato in alcuni contesti informatici.

### Esercizio d'esempio

**Testo.** Per determinare l'accelerazione di gravità si misura il periodo di un pendolo di lunghezza $L = (0{,}800 \pm 0{,}002)\ \mathrm{m}$. Cinque misure del tempo di 10 oscillazioni forniscono $17{,}91$, $17{,}95$, $17{,}88$, $17{,}97$, $17{,}94\ \mathrm{s}$. Calcolare $g = 4\pi^2 L/T^2$ con la sua incertezza.

**Soluzione.** La media dei tempi è $\bar t = (17{,}91+17{,}95+17{,}88+17{,}97+17{,}94)/5\ \mathrm{s} = 17{,}93\ \mathrm{s}$. Gli scarti sono $-0{,}02$, $+0{,}02$, $-0{,}05$, $+0{,}04$, $+0{,}01\ \mathrm{s}$; la somma dei quadrati vale $0{,}0050\ \mathrm{s^2}$. La deviazione standard è

$$\sigma_t = \sqrt{\frac{0{,}0050}{4}}\ \mathrm{s} \simeq 0{,}035\ \mathrm{s}, \qquad \sigma_{\bar t} = \frac{0{,}035}{\sqrt5}\ \mathrm{s} \simeq 0{,}016\ \mathrm{s}.$$

Il periodo è $T = \bar t/10 = (1{,}7930 \pm 0{,}0016)\ \mathrm{s}$ (cifre in più conservate nel calcolo intermedio). Si calcola

$$g = \frac{4\pi^2\cdot0{,}800\ \mathrm{m}}{(1{,}793\ \mathrm{s})^2} = \frac{31{,}58}{3{,}215}\ \mathrm{m/s^2} \simeq 9{,}824\ \mathrm{m/s^2}.$$

Le incertezze relative sono $\delta L/L = 0{,}002/0{,}800 = 0{,}25\%$ e $\delta T/T = 0{,}0016/1{,}793 \simeq 0{,}09\%$. Poiché $T$ compare al quadrato, il suo contributo raddoppia: $0{,}18\%$. Sommando in quadratura (contributi indipendenti):

$$\frac{\delta g}{g} = \sqrt{(0{,}25\%)^2 + (0{,}18\%)^2} \simeq 0{,}31\%, \qquad \delta g \simeq 0{,}030\ \mathrm{m/s^2}.$$

Arrotondando l'incertezza a una cifra e la stima alla stessa posizione: $g = (9{,}82 \pm 0{,}03)\ \mathrm{m/s^2}$, compatibile con il valore di riferimento $9{,}81\ \mathrm{m/s^2}$. Il contributo dominante è quello della lunghezza: per migliorare la misura conviene usare un metro più preciso piuttosto che ripetere i tempi.

### Punti chiave

- Il risultato di una misura si scrive come miglior stima ± incertezza, con unità; l'incertezza relativa misura la precisione.
- Gli errori sistematici agiscono sempre nello stesso verso, compromettono l'accuratezza e non si riducono ripetendo la misura: si scoprono con tarature e metodi indipendenti.
- Gli errori statistici producono dispersione; la media è la miglior stima e la sua incertezza decresce come $\sigma/\sqrt N$.
- Nelle misure indirette le incertezze si propagano: si sommano le assolute per somme/differenze, le relative per prodotti/quozienti, con fattore $|n|$ per le potenze.
- Per incertezze statistiche indipendenti si usa la somma in quadratura, meno pessimistica della somma lineare.
- L'incertezza si arrotonda a una (o due) cifre significative e la stima alla stessa posizione decimale.
- Si arrotonda in un solo passo dal valore completo; il caso del 5 esatto si tratta di preferenza con l'arrotondamento al pari.
