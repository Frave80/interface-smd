# Capitolo 16 — Elettrostatica

L'elettrostatica studia le interazioni fra cariche elettriche ferme, o comunque in moto così lento che gli effetti magnetici e di propagazione possano essere trascurati. È il primo capitolo dell'elettromagnetismo e, allo stesso tempo, quello in cui si costruiscono tutti gli strumenti concettuali che verranno riutilizzati in seguito: il concetto di **campo** come proprietà dello spazio, il **flusso** di un campo vettoriale attraverso una superficie, il **potenziale** come funzione scalare da cui ricavare il campo, la descrizione locale tramite operatori differenziali. Partiremo dai fenomeni osservabili in laboratorio (bacchette strofinate, elettroscopi, attrazione di pezzetti di carta), arriveremo alla legge di Coulomb, la tradurremo nel linguaggio dei campi, ne ricaveremo il teorema di Gauss e la conservatività, studieremo il dipolo come primo esempio di distribuzione neutra ma non banale, e chiuderemo con la formulazione differenziale delle equazioni dell'elettrostatica, cioè le prime due equazioni di Maxwell nel caso statico.

## 16.1 Elettrizzazione

L'osservazione sperimentale da cui nasce l'elettrostatica è antichissima: un pezzo d'ambra (in greco *élektron*) strofinato con un panno di lana attira piccoli frammenti di paglia o di carta. Per secoli il fenomeno è rimasto una curiosità; solo fra Seicento e Settecento è stato studiato sistematicamente, fino a riconoscere che i corpi possono trovarsi in uno stato particolare, detto **stato di elettrizzazione**, nel quale esercitano forze a distanza su altri corpi. Oggi sappiamo che questo stato corrisponde a un eccesso o a un difetto di elettroni rispetto alla condizione di neutralità, ma è istruttivo ripercorrere i diversi modi con cui un corpo può essere elettrizzato, perché ciascuno di essi mette in luce un aspetto diverso della natura della carica elettrica e del comportamento dei materiali.

Prima di procedere, conviene introdurre una distinzione fondamentale fra due classi di materiali. Si dicono **conduttori** i materiali nei quali alcune cariche (tipicamente gli elettroni più esterni degli atomi, nei metalli) sono libere di muoversi su distanze macroscopiche all'interno del corpo; si dicono **isolanti** o **dielettrici** i materiali nei quali le cariche restano legate ai rispettivi atomi o molecole e possono al più spostarsi di frazioni di diametro atomico. Metalli, soluzioni elettrolitiche, il corpo umano e la Terra sono buoni conduttori; vetro, plastiche, ambra, aria secca, ceramiche sono buoni isolanti. Esistono poi i **semiconduttori**, con proprietà intermedie e fortemente dipendenti da temperatura e drogaggio, che qui non tratteremo. La distinzione è cruciale: in un isolante la carica depositata resta localizzata dove è stata messa, mentre in un conduttore si ridistribuisce immediatamente su tutto il corpo.

### 16.1.1 Strofinio

L'**elettrizzazione per strofinio** è il fenomeno storicamente più antico. Si prende una bacchetta di vetro e la si strofina con un panno di seta; si prende poi una bacchetta di plastica (o d'ambra, o di ebanite) e la si strofina con un panno di lana. Sospendendo le bacchette a fili isolanti e avvicinandole fra loro si osserva che due bacchette di vetro strofinate si respingono, due bacchette di plastica strofinate si respingono, mentre una bacchetta di vetro e una di plastica si attraggono. Da queste osservazioni si conclude che esistono **due tipi di elettrizzazione** e che corpi elettrizzati nello stesso modo si respingono mentre corpi elettrizzati in modo diverso si attraggono. Per convenzione, risalente a Benjamin Franklin, si chiama **positiva** l'elettrizzazione assunta dal vetro strofinato con la seta e **negativa** quella assunta dalla plastica (o dall'ambra) strofinata con la lana.

Un'osservazione ulteriore è che anche il panno usato per strofinare si elettrizza, e con segno opposto a quello della bacchetta: la seta che ha strofinato il vetro attira il vetro stesso. Questo suggerisce che lo strofinio non crei elettricità dal nulla, ma la **trasferisca** da un corpo all'altro. Microscopicamente, nel contatto intimo fra due superfici di materiali diversi una parte degli elettroni passa dal materiale che li trattiene più debolmente a quello che li trattiene più fortemente; lo strofinio serve semplicemente a moltiplicare i punti di contatto. I materiali si possono ordinare in una **serie triboelettrica** in base alla loro tendenza a cedere o acquistare elettroni: un materiale strofinato con uno che lo segue nella serie si carica positivamente, con uno che lo precede si carica negativamente.

Per un isolante la carica prodotta per strofinio resta confinata nella zona strofinata. Se si prova a strofinare una bacchetta metallica tenendola in mano, invece, non si osserva alcuna elettrizzazione: la carica si trasferisce immediatamente al corpo dello sperimentatore e da questo alla Terra. Se però il metallo è montato su un manico isolante, anche esso si elettrizza per strofinio, e la carica si distribuisce su tutta la sua superficie. Questo esperimento mostra che la differenza fra conduttori e isolanti non sta nella capacità di elettrizzarsi, ma nella mobilità delle cariche.

### 16.1.2 Contatto

Un secondo modo di elettrizzare un corpo è il **contatto** con un corpo già carico. Se si tocca con una bacchetta di vetro elettrizzata una sferetta metallica montata su un sostegno isolante, la sferetta acquista un'elettrizzazione dello stesso segno della bacchetta, e da quel momento viene respinta da essa. Il fenomeno è ben visibile con l'**elettroscopio a foglie**: un'asta metallica verticale, isolata dal contenitore, termina in basso con due sottili foglie d'oro o d'alluminio. Toccando il pomello superiore con un corpo carico, parte della carica passa all'asta e si distribuisce fra le foglie, che, cariche dello stesso segno, si respingono e divaricano. L'apertura delle foglie fornisce una misura qualitativa (e, con una taratura, quantitativa) della carica trasferita.

Il trasferimento per contatto è massimo quando entrambi i corpi sono conduttori. Se si mettono a contatto due sfere metalliche identiche, una carica e l'altra neutra, dopo la separazione ciascuna di esse porta esattamente metà della carica iniziale. Questo procedimento, usato da Coulomb nei suoi esperimenti con la bilancia di torsione, consente di dividere una carica in parti note (metà, quarto, ottavo…) senza conoscerne il valore assoluto, ed è stato essenziale per stabilire la dipendenza della forza dal prodotto delle cariche. Se i due conduttori non sono identici la ripartizione non è più a metà, ma è dettata dalla condizione che i due corpi, una volta in contatto, formino un unico conduttore in equilibrio, con lo stesso potenziale: ritroveremo questo concetto nel capitolo sui conduttori.

L'esperimento dell'elettroscopio permette anche di verificare un principio fondamentale: la **conservazione della carica**. Se si carica un elettroscopio e poi lo si tocca con un secondo elettroscopio identico e scarico, le foglie del primo si chiudono parzialmente e quelle del secondo si aprono dello stesso angolo; la carica totale dei due strumenti resta quella iniziale. Più in generale, in un sistema isolato la somma algebrica delle cariche è costante nel tempo: la carica può essere spostata, non creata né distrutta. Anche nei processi di fisica delle particelle in cui vengono create o annichilate particelle cariche, come la produzione di coppie elettrone-positrone, la carica totale resta invariata.

### 16.1.3 Induzione elettrostatica

Un fenomeno più sottile è l'**induzione elettrostatica**, che permette di elettrizzare un conduttore senza toccarlo. Si avvicina una bacchetta carica positivamente a un conduttore isolato e inizialmente neutro, senza contatto. Le cariche libere del conduttore (gli elettroni) vengono attratte verso la bacchetta e si accumulano sulla parte di superficie a essa più vicina, lasciando sulla parte opposta un difetto di elettroni, cioè una carica positiva. Il conduttore resta complessivamente neutro, ma presenta una separazione di cariche: si parla di **cariche indotte**. Se si allontana la bacchetta, le cariche si ridistribuiscono e il conduttore torna nella condizione iniziale.

Il procedimento diventa un vero metodo di elettrizzazione se, mentre la bacchetta è vicina, si collega il conduttore a terra (per esempio toccandolo con un dito). Gli elettroni attratti dalla bacchetta positiva arrivano anche dalla Terra, che si comporta come un serbatoio praticamente infinito di cariche; interrompendo poi il collegamento a terra e solo dopo allontanando la bacchetta, il conduttore resta carico negativamente, cioè con segno **opposto** a quello del corpo induttore. Si noti l'ordine delle operazioni: se si allontanasse la bacchetta prima di interrompere il collegamento a terra, la carica in eccesso tornerebbe alla Terra.

L'induzione spiega anche un comportamento dell'elettroscopio che a prima vista sembra paradossale: avvicinando al pomello, senza toccarlo, una bacchetta carica, le foglie si aprono. La bacchetta attira verso il pomello le cariche di segno opposto e respinge verso le foglie quelle dello stesso segno, che quindi si divaricano. Allontanando la bacchetta le foglie si richiudono. Se invece l'elettroscopio è già carico, l'avvicinamento di un corpo carico dello stesso segno aumenta la divaricazione, mentre quello di un corpo carico di segno opposto la riduce: si ottiene così un modo semplice per determinare il segno di una carica incognita.

### 16.1.4 Polarizzazione

Resta da spiegare l'osservazione originaria: perché una bacchetta carica attira pezzetti di carta, che sono isolanti e neutri? In un isolante le cariche non sono libere di migrare attraverso il corpo, quindi non si può avere induzione nel senso visto sopra. Tuttavia, in presenza di un corpo carico, ogni atomo o molecola del dielettrico subisce una piccola deformazione: la nube elettronica viene spostata leggermente rispetto al nucleo, oppure, se la molecola possiede già una separazione permanente di carica (come l'acqua), essa tende a orientarsi. Il risultato è che ogni elemento di volume del materiale si comporta come un **dipolo elettrico** microscopico, cioè come una coppia di cariche uguali e opposte molto vicine. Questo fenomeno si chiama **polarizzazione** del dielettrico.

L'effetto netto della polarizzazione è che sulla superficie del pezzetto di carta rivolta verso la bacchetta compare una carica di segno opposto a quella della bacchetta, mentre sulla superficie opposta ne compare una di segno uguale. Si tratta di **cariche di polarizzazione**, legate al materiale e non estraibili (non si può isolarle tagliando il pezzetto a metà, a differenza di quanto accade per le cariche indotte su un conduttore). Poiché la forza elettrica diminuisce rapidamente con la distanza, l'attrazione sulle cariche più vicine prevale sulla repulsione su quelle più lontane, e la carta viene attratta. Lo stesso meccanismo agisce, con intensità maggiore, sui conduttori neutri: per questo un qualsiasi corpo neutro è sempre attratto da un corpo carico, indipendentemente dal segno di quest'ultimo.

La polarizzazione è anche responsabile di un fenomeno quotidiano: un palloncino strofinato sui capelli aderisce a una parete. La parete, isolante, si polarizza localmente e l'attrazione fra la carica del palloncino e la carica di polarizzazione indotta è sufficiente a vincere il peso del palloncino. Allo stesso modo, un sottile filo d'acqua che scende da un rubinetto viene deviato da una bacchetta carica, perché le molecole d'acqua, polari, si orientano nel campo. Lo studio quantitativo della polarizzazione verrà affrontato nel capitolo dedicato ai dielettrici; qui ci limitiamo a sottolineare che la stessa idea di dipolo indotto sarà ripresa nella sezione 16.6.

### Esercizio d'esempio

Tre sfere metalliche identiche, A, B e C, sono montate su sostegni isolanti. Inizialmente A porta una carica $q_A = 8{,}0\ \mu\text{C}$, B porta $q_B = -2{,}0\ \mu\text{C}$ e C è neutra. Si mette A a contatto con B, poi si separano; quindi si mette B a contatto con C e si separano; infine si mettono A e C a contatto e si separano. Determinare le cariche finali e verificare la conservazione della carica.

**Soluzione.** Quando due conduttori identici sono messi a contatto, per simmetria la carica totale si divide in parti uguali.

1. Contatto A–B: carica totale $q_A + q_B = 8{,}0 - 2{,}0 = 6{,}0\ \mu\text{C}$; dopo la separazione $q_A = q_B = 3{,}0\ \mu\text{C}$.
2. Contatto B–C: carica totale $3{,}0 + 0 = 3{,}0\ \mu\text{C}$; quindi $q_B = q_C = 1{,}5\ \mu\text{C}$.
3. Contatto A–C: carica totale $3{,}0 + 1{,}5 = 4{,}5\ \mu\text{C}$; quindi $q_A = q_C = 2{,}25\ \mu\text{C}$.

Cariche finali: $q_A = 2{,}25\ \mu\text{C}$, $q_B = 1{,}5\ \mu\text{C}$, $q_C = 2{,}25\ \mu\text{C}$. Somma: $2{,}25 + 1{,}5 + 2{,}25 = 6{,}0\ \mu\text{C}$, uguale alla carica totale iniziale $8{,}0 - 2{,}0 + 0 = 6{,}0\ \mu\text{C}$. Il numero di elettroni mancanti complessivamente è $N = Q/e = 6{,}0\times10^{-6}/1{,}602\times10^{-19} \approx 3{,}7\times10^{13}$.

### Punti chiave

- Esistono due tipi di elettrizzazione, convenzionalmente positiva e negativa; cariche dello stesso segno si respingono, di segno opposto si attraggono.
- Nei **conduttori** alcune cariche sono libere di muoversi su scala macroscopica; negli **isolanti** restano legate agli atomi.
- Lo strofinio trasferisce elettroni fra due materiali diversi: i due corpi si caricano con segni opposti.
- Il contatto fra conduttori ripartisce la carica; per conduttori identici la ripartizione è in parti uguali.
- L'**induzione elettrostatica** separa le cariche in un conduttore senza contatto; con un collegamento a terra si ottiene una carica netta di segno opposto all'induttore.
- La **polarizzazione** di un dielettrico crea dipoli microscopici e cariche superficiali legate, che spiegano l'attrazione di corpi neutri.
- La carica elettrica di un sistema isolato si **conserva**.

## 16.2 Forza elettrica

Dopo aver descritto qualitativamente i fenomeni di elettrizzazione, occorre passare a una descrizione quantitativa. Le domande da porsi sono: che cos'è esattamente la grandezza "carica elettrica" e come si misura? Qual è la sua natura microscopica? Con quale legge due corpi carichi interagiscono? Come si può sondare l'effetto delle cariche nello spazio circostante? Le quattro sottosezioni che seguono rispondono a queste domande e portano alla formulazione della legge di Coulomb, che è la legge fondamentale dell'elettrostatica, analoga per importanza alla legge di gravitazione universale in meccanica.

### 16.2.1 Carica elettrica

La **carica elettrica** è una grandezza fisica scalare, dotata di segno, che caratterizza la capacità di un corpo di partecipare all'interazione elettromagnetica. Le osservazioni sperimentali ne fissano alcune proprietà fondamentali. Innanzitutto la carica è **additiva**: la carica di un sistema è la somma algebrica delle cariche delle sue parti, tenendo conto dei segni. In secondo luogo la carica si **conserva** in un sistema isolato, come già discusso. In terzo luogo la carica è **quantizzata**: ogni carica osservata in natura è un multiplo intero della **carica elementare**

$$e = 1{,}602\,176\,634\times10^{-19}\ \text{C},$$

come dimostrato dall'esperimento di Millikan sulle goccioline d'olio (1909). L'elettrone porta carica $-e$, il protone $+e$. I quark possiedono cariche frazionarie ($\pm e/3$, $\pm 2e/3$), ma non sono mai osservati isolati, per cui la quantizzazione in unità di $e$ vale per tutte le particelle libere. Infine la carica è **invariante relativistica**: il suo valore non dipende dallo stato di moto dell'osservatore.

Nel Sistema Internazionale l'unità di carica è il **coulomb** (C). Dal 2019 il valore di $e$ è fissato esattamente e il coulomb è definito di conseguenza; operativamente, un coulomb è la carica trasportata in un secondo da una corrente di un ampere, $1\ \text{C} = 1\ \text{A}\cdot\text{s}$. Si tratta di una quantità enorme su scala elettrostatica: le cariche ottenute per strofinio sono tipicamente dell'ordine dei nanocoulomb o dei microcoulomb. Un coulomb corrisponde a circa $6{,}24\times10^{18}$ cariche elementari.

Poiché $e$ è così piccola, nella maggior parte delle situazioni macroscopiche la granularità della carica è irrilevante e conviene descrivere la carica come una grandezza distribuita con continuità. Si introducono allora le **densità di carica**: volumica $\rho = \mathrm{d}q/\mathrm{d}V$ (in C/m³), superficiale $\sigma = \mathrm{d}q/\mathrm{d}S$ (in C/m²) e lineare $\lambda = \mathrm{d}q/\mathrm{d}l$ (in C/m). La carica totale di una distribuzione si ottiene integrando la densità appropriata sul dominio occupato, per esempio $Q = \int_V \rho\,\mathrm{d}V$. Questa descrizione è legittima quando l'elemento di volume $\mathrm{d}V$ è piccolo rispetto alle scale macroscopiche di interesse ma contiene comunque un numero enorme di cariche elementari.

### 16.2.2 Struttura della materia

La comprensione microscopica dell'elettrizzazione si fonda sulla struttura atomica della materia. Ogni atomo è costituito da un **nucleo**, formato da protoni (carica $+e$, massa $m_p \approx 1{,}673\times10^{-27}$ kg) e neutroni (carica nulla, massa simile), circondato da una nube di **elettroni** (carica $-e$, massa $m_e \approx 9{,}109\times10^{-31}$ kg). Le dimensioni tipiche dell'atomo sono dell'ordine di $10^{-10}$ m, quelle del nucleo di $10^{-15}$ m. In un atomo neutro il numero di elettroni è uguale al numero atomico $Z$, cioè al numero di protoni. Il fatto che la carica dell'elettrone e quella del protone siano uguali in modulo con una precisione straordinaria (verificata a meno di una parte su $10^{21}$) è ciò che rende la materia ordinaria neutra con altissima accuratezza.

Poiché i nuclei sono pesanti e fortemente legati, nei processi di elettrizzazione ordinari sono soltanto gli elettroni, e in particolare quelli più esterni, a essere trasferiti. Un corpo è carico negativamente se possiede più elettroni dei protoni, positivamente se ne possiede meno. Nei **metalli** gli elettroni di valenza non appartengono a un singolo atomo ma sono delocalizzati in tutto il reticolo cristallino, formando un "gas" di elettroni liberi: è per questo che i metalli sono buoni conduttori. Negli **isolanti** tutti gli elettroni sono legati ai rispettivi atomi o ai legami chimici e possono solo spostarsi di poco sotto l'azione di forze esterne. Nelle **soluzioni elettrolitiche** i portatori di carica mobili sono ioni positivi e negativi.

L'interazione elettrica è responsabile della coesione degli atomi, della formazione dei legami chimici, della struttura dei solidi, dell'attrito e delle forze di contatto in genere: tutte le forze "macroscopiche" della meccanica, eccetto la gravità, sono in ultima analisi di origine elettromagnetica. La ragione per cui nella vita quotidiana non ci accorgiamo delle enormi forze elettriche in gioco è proprio la quasi perfetta neutralità della materia: le attrazioni e le repulsioni si compensano a distanze grandi rispetto a quelle atomiche.

### 16.2.3 Forza di Coulomb

Nel 1785 Charles-Augustin de Coulomb misurò con una **bilancia di torsione** la forza fra due piccole sfere cariche, stabilendo la legge che porta il suo nome. Per due **cariche puntiformi** $q_1$ e $q_2$ ferme nel vuoto, poste a distanza $r$, la forza che $q_1$ esercita su $q_2$ è

$$\vec{F}_{12} = \frac{1}{4\pi\varepsilon_0}\,\frac{q_1 q_2}{r^2}\,\hat{u}_{12},$$

dove $\hat{u}_{12}$ è il versore diretto da $q_1$ verso $q_2$. La forza è **centrale** (diretta lungo la congiungente), proporzionale al prodotto delle cariche, inversamente proporzionale al quadrato della distanza. Se $q_1 q_2 > 0$ la forza su $q_2$ è diretta lontano da $q_1$ (repulsione), se $q_1 q_2 < 0$ è diretta verso $q_1$ (attrazione). Per il terzo principio della dinamica $\vec{F}_{21} = -\vec{F}_{12}$, come si verifica immediatamente dalla formula scambiando gli indici.

La costante $\varepsilon_0$ è la **costante dielettrica del vuoto** (o permittività del vuoto), $\varepsilon_0 \approx 8{,}854\times10^{-12}\ \text{C}^2/(\text{N}\,\text{m}^2)$, e si pone spesso $k = 1/(4\pi\varepsilon_0) \approx 8{,}988\times10^{9}\ \text{N}\,\text{m}^2/\text{C}^2$. Il fattore $4\pi$ è introdotto nella costante (sistema "razionalizzato") perché semplifica le leggi che coinvolgono il flusso, come il teorema di Gauss.

La struttura della legge di Coulomb è identica a quella della legge di gravitazione di Newton, ma le differenze sono sostanziali. La forza gravitazionale è sempre attrattiva, mentre quella elettrica può essere attrattiva o repulsiva. Inoltre l'interazione elettrica è enormemente più intensa: fra un elettrone e un protone il rapporto fra forza elettrica e forza gravitazionale vale

$$\frac{F_e}{F_g} = \frac{e^2}{4\pi\varepsilon_0\,G\,m_e m_p} \approx 2{,}3\times10^{39},$$

indipendente dalla distanza. È proprio la compensazione fra cariche positive e negative a rendere la gravità dominante su scala astronomica.

La legge di Coulomb vale rigorosamente per cariche **puntiformi** (cioè di dimensioni trascurabili rispetto alla distanza) e **ferme** (o lentamente variabili). L'esponente 2 è stato verificato con precisione straordinaria: eventuali deviazioni del tipo $r^{-(2+\delta)}$ hanno $|\delta| < 10^{-16}$. Fondamentale è anche il **principio di sovrapposizione**: la forza esercitata su una carica da un insieme di cariche è la somma vettoriale delle forze che ciascuna eserciterebbe da sola,

$$\vec{F}_0 = \sum_i \frac{1}{4\pi\varepsilon_0}\,\frac{q_i q_0}{r_{i0}^2}\,\hat{u}_{i0}.$$

Si tratta di un fatto sperimentale, non di una conseguenza logica, ed equivale a dire che le equazioni dell'elettrostatica sono lineari. Per distribuzioni continue la somma diventa un integrale, sostituendo $q_i$ con $\rho\,\mathrm{d}V$, $\sigma\,\mathrm{d}S$ o $\lambda\,\mathrm{d}l$.

### 16.2.4 Carica esploratrice

Per studiare l'effetto di una distribuzione di cariche nello spazio circostante si ricorre a una **carica esploratrice** (o carica di prova) $q_0$: una carica puntiforme, convenzionalmente positiva, che si pone nel punto di interesse misurando la forza che subisce. Per non alterare la distribuzione che si vuole sondare, la carica esploratrice deve essere **piccola**: se fosse grande, per induzione o polarizzazione modificherebbe la posizione delle cariche delle sorgenti (in particolare su conduttori vicini), e la misura non descriverebbe più la situazione originaria. Formalmente si considera il limite $q_0\to0$.

Il punto chiave è che, per il principio di sovrapposizione e per la forma della legge di Coulomb, la forza su $q_0$ è proporzionale a $q_0$ stessa: raddoppiando la carica esploratrice la forza raddoppia, invertendone il segno la forza si inverte. Il rapporto $\vec{F}/q_0$ è quindi indipendente dalla carica di prova e dipende soltanto dalla distribuzione delle sorgenti e dal punto dello spazio considerato. Questa osservazione apre la strada alla definizione del campo elettrico, discussa nella sezione successiva: invece di parlare di una forza fra due cariche, si attribuisce allo spazio attorno alle sorgenti una proprietà vettoriale definita punto per punto, che "attende" una carica per esercitare su di essa una forza.

L'uso della carica esploratrice ha anche un significato concettuale profondo. Nella legge di Coulomb l'interazione appare come istantanea e a distanza; nella descrizione mediante campo, invece, ciascuna carica interagisce localmente con il campo presente nel punto in cui si trova. Nel caso statico le due descrizioni sono equivalenti, ma quando le cariche si muovono si scopre che le perturbazioni del campo si propagano alla velocità della luce: il campo diventa allora un'entità fisica dotata di energia e quantità di moto propria, e non solo un artificio matematico.

### Esercizio d'esempio

Tre cariche puntiformi sono poste nel vuoto ai vertici di un triangolo equilatero di lato $a = 0{,}10$ m: $q_1 = q_2 = +2{,}0\ \mu\text{C}$ e $q_3 = -2{,}0\ \mu\text{C}$. Calcolare la forza totale agente su $q_3$.

**Soluzione.** Il modulo di ciascuna forza su $q_3$ è

$$F = \frac{1}{4\pi\varepsilon_0}\frac{|q|^2}{a^2} = 8{,}99\times10^{9}\cdot\frac{(2{,}0\times10^{-6})^2}{(0{,}10)^2} = 8{,}99\times10^{9}\cdot 4{,}0\times10^{-10} \approx 3{,}6\ \text{N}.$$

Entrambe le forze sono attrattive (cariche di segno opposto), dirette da $q_3$ verso $q_1$ e verso $q_2$. Poniamo $q_1$ e $q_2$ sull'asse $x$ in $(\mp a/2,0)$ e $q_3$ in $(0, a\sqrt3/2)$. Le componenti orizzontali delle due forze si cancellano per simmetria; le componenti verticali, entrambe dirette verso il basso, valgono ciascuna $F\cos30^\circ$. La forza risultante è

$$\vec{F}_3 = -2F\cos30^\circ\,\hat{y} = -2\cdot3{,}6\cdot0{,}866\,\hat{y} \approx -6{,}2\ \text{N}\ \hat{y},$$

diretta da $q_3$ verso il punto medio del lato opposto.

### Punti chiave

- La carica elettrica è additiva, conservata, quantizzata in multipli di $e = 1{,}602\times10^{-19}$ C e relativisticamente invariante.
- Nella materia ordinaria solo gli elettroni esterni si trasferiscono; nei metalli formano un gas di elettroni liberi.
- La legge di Coulomb: $\vec{F} = \frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r^2}\hat{u}$, valida per cariche puntiformi e ferme.
- $\varepsilon_0 \approx 8{,}854\times10^{-12}$ C²/(N m²), $k \approx 8{,}99\times10^9$ N m²/C².
- Vale il principio di sovrapposizione: le forze dovute a più cariche si sommano vettorialmente.
- La forza elettrica supera quella gravitazionale di circa 39 ordini di grandezza fra elettrone e protone.
- La carica esploratrice deve essere piccola per non perturbare le sorgenti; $\vec{F}/q_0$ non dipende da $q_0$.

## 16.3 Campo elettrico

Il passaggio dalla forza al campo rappresenta uno dei salti concettuali più importanti della fisica classica. Invece di descrivere l'interazione come un'azione diretta fra due cariche lontane, si afferma che ogni distribuzione di carica modifica le proprietà dello spazio circostante, creando un **campo elettrico**; una seconda carica, posta in un punto, risente di una forza determinata dal valore locale del campo. In questa sezione definiamo il campo, impariamo a rappresentarlo graficamente mediante le linee di campo e i tubi di flusso, e studiamo il moto di particelle cariche in un campo assegnato.

### 16.3.1 Campo elettrico

Il **campo elettrico** in un punto $P$ è definito come la forza per unità di carica che agirebbe su una carica esploratrice posta in $P$:

$$\vec{E}(P) = \lim_{q_0\to0}\frac{\vec{F}(P)}{q_0}.$$

Si tratta di un **campo vettoriale**, cioè di una funzione che associa a ogni punto dello spazio un vettore. Nel SI si misura in newton su coulomb (N/C) o, equivalentemente, come vedremo, in volt su metro (V/m). Noto il campo, la forza su una qualunque carica puntiforme $q$ posta in $P$ è semplicemente $\vec{F} = q\vec{E}(P)$: se $q>0$ la forza ha lo stesso verso del campo, se $q<0$ verso opposto.

Dalla legge di Coulomb segue immediatamente il campo generato da una carica puntiforme $q$ posta nell'origine:

$$\vec{E}(\vec{r}) = \frac{1}{4\pi\varepsilon_0}\,\frac{q}{r^2}\,\hat{r}.$$

Il campo è radiale, uscente se $q>0$ ed entrante se $q<0$, con modulo che decresce come $1/r^2$. Per il principio di sovrapposizione, il campo generato da un insieme di cariche puntiformi $q_i$ poste in $\vec{r}_i$ è

$$\vec{E}(\vec{r}) = \frac{1}{4\pi\varepsilon_0}\sum_i q_i\,\frac{\vec{r}-\vec{r}_i}{|\vec{r}-\vec{r}_i|^3},$$

e per una distribuzione continua di densità $\rho(\vec{r}\,')$

$$\vec{E}(\vec{r}) = \frac{1}{4\pi\varepsilon_0}\int_V \rho(\vec{r}\,')\,\frac{\vec{r}-\vec{r}\,'}{|\vec{r}-\vec{r}\,'|^3}\,\mathrm{d}V'.$$

Questa formula è del tutto generale, ma il calcolo diretto dell'integrale è spesso laborioso; nelle sezioni seguenti vedremo strumenti (teorema di Gauss, potenziale) che lo semplificano molto nei casi dotati di simmetria.

Due risultati classici, ottenibili per integrazione diretta, sono di grande utilità. Per un **filo rettilineo indefinito** con densità lineare uniforme $\lambda$, il campo a distanza $r$ dal filo è radiale rispetto all'asse e vale $E = \lambda/(2\pi\varepsilon_0 r)$: decresce solo come $1/r$, perché la sorgente è estesa in una dimensione. Per un **piano indefinito** con densità superficiale uniforme $\sigma$, il campo è perpendicolare al piano e di modulo $E = \sigma/(2\varepsilon_0)$, indipendente dalla distanza. Questi casi sono idealizzazioni: un filo o un piano reali sono finiti, ma le formule sono ottime approssimazioni a distanze piccole rispetto alle dimensioni della sorgente e lontano dai bordi.

Il campo elettrico ha significato fisico autonomo, non è soltanto un modo comodo di riscrivere la legge di Coulomb. In elettrostatica la sua introduzione è un cambio di linguaggio, ma essa prepara la descrizione dei fenomeni dinamici, nei quali il campo trasporta energia e informazione a velocità finita. Anche in statica, del resto, il campo permette di separare il problema in due parti: il calcolo del campo prodotto dalle sorgenti e lo studio dell'effetto del campo su una carica di prova.

### 16.3.2 Linee di flusso

Per visualizzare un campo vettoriale Faraday introdusse le **linee di campo** (o linee di forza, o linee di flusso): curve orientate tangenti in ogni punto al vettore campo e con lo stesso verso. Il disegno delle linee di campo fornisce un'immagine immediata della direzione del campo nello spazio; per convenzione, la **densità** delle linee (numero di linee che attraversano una superficie unitaria perpendicolare a esse) è proporzionale al modulo del campo, per cui dove le linee si addensano il campo è intenso e dove si diradano è debole.

Le linee del campo elettrostatico godono di alcune proprietà generali. Esse **nascono** dalle cariche positive e **terminano** sulle cariche negative (oppure si estendono all'infinito); il numero di linee che escono da una carica positiva o entrano in una negativa è proporzionale al valore della carica. Due linee di campo **non si intersecano mai** in un punto in cui il campo è definito e non nullo, perché in ogni punto il campo ha una sola direzione. Nel caso elettrostatico, inoltre, le linee di campo **non si chiudono su se stesse**: questa proprietà, che deriva dalla conservatività del campo (sezione 16.5), distingue nettamente il campo elettrostatico dal campo magnetico.

Per una carica puntiforme positiva isolata le linee sono semirette uscenti dalla carica, distribuite uniformemente in tutte le direzioni; la loro densità su una sfera di raggio $r$ è proporzionale a $1/(4\pi r^2)$, in accordo con l'andamento $1/r^2$ del campo. Per due cariche uguali e positive le linee si respingono reciprocamente e nella zona intermedia esiste un punto di campo nullo. Per due cariche uguali e opposte (dipolo) le linee partono dalla positiva e si richiudono sulla negativa, piegandosi lungo archi. Per due piani paralleli con cariche opposte le linee sono parallele ed equidistanti nella regione interna: il campo è **uniforme**.

Occorre ricordare che le linee di campo sono uno strumento di rappresentazione, non oggetti fisici. In particolare, una carica che parte da ferma in un campo non segue necessariamente una linea di campo: la sua accelerazione è tangente alla linea, ma la velocità, una volta acquisita, ne cambia la traiettoria. Le traiettorie coincidono con le linee solo se queste sono rettilinee o se la particella è soggetta a forti attriti che ne annullano l'inerzia.

### 16.3.3 Tubo di flusso

Consideriamo una piccola curva chiusa $\gamma$ nello spazio e tracciamo le linee di campo passanti per tutti i suoi punti: esse formano una superficie tubolare detta **tubo di flusso**. Per costruzione, il campo è tangente alla superficie laterale del tubo, quindi nessuna linea di campo la attraversa: le linee entrano dalla sezione iniziale e escono dalla sezione finale, come l'acqua in un condotto.

Questa immagine diventa quantitativa introducendo il **flusso** del campo attraverso una sezione del tubo, che definiremo con precisione nella sezione 16.4. Per ora basta osservare che, in una regione priva di cariche, il numero di linee di campo che attraversano una sezione del tubo è lo stesso per ogni sezione, perché le linee non possono né nascere né morire. Ne segue che il prodotto fra modulo del campo e area della sezione trasversale si conserva lungo il tubo:

$$E_1 S_1 = E_2 S_2.$$

Dove il tubo si restringe il campo si intensifica, dove si allarga si indebolisce. Per una carica puntiforme i tubi di flusso sono coni con vertice nella carica; la sezione a distanza $r$ è proporzionale a $r^2$, e ritroviamo l'andamento $E\propto1/r^2$. La conservazione del flusso lungo un tubo è, in forma locale, il contenuto del teorema di Gauss in assenza di cariche, e mostra come l'andamento $1/r^2$ della legge di Coulomb sia strettamente legato alla geometria tridimensionale dello spazio.

L'analogia idrodinamica è utile e precisa: il campo elettrico in una regione vuota di cariche si comporta come il campo di velocità di un fluido incomprimibile in moto stazionario, e le cariche positive e negative giocano il ruolo di sorgenti e pozzi. Questa analogia verrà formalizzata nella formulazione differenziale (sezione 16.7) con l'operatore divergenza.

### 16.3.4 Moto di cariche

Il caso più importante dal punto di vista applicativo è quello di una particella di carica $q$ e massa $m$ in un **campo uniforme** $\vec{E}$, come quello presente fra le armature di un condensatore piano. Trascurando la gravità (lecito per elettroni e ioni, dove il rapporto $q/m$ è enorme) la seconda legge della dinamica dà

$$\vec{a} = \frac{q}{m}\vec{E},$$

accelerazione costante. Il moto è quindi analogo al moto di un proiettile nel campo gravitazionale: rettilineo uniformemente accelerato se la velocità iniziale è parallela al campo, parabolico altrimenti. Per un elettrone ($q/m \approx -1{,}76\times10^{11}$ C/kg) in un campo di $10^4$ V/m l'accelerazione è dell'ordine di $10^{15}$ m/s², circa $10^{14}$ volte quella di gravità.

Consideriamo un elettrone che entra con velocità $v_0$ orizzontale fra due piastre parallele lunghe $L$, fra le quali è presente un campo verticale $E$. Lungo l'orizzontale il moto è uniforme, quindi l'elettrone resta fra le piastre per un tempo $t = L/v_0$. Lungo la verticale subisce un'accelerazione $a = eE/m_e$ e all'uscita è stato deviato di

$$y = \frac{1}{2}\frac{eE}{m_e}\frac{L^2}{v_0^2},$$

con un angolo di deflessione dato da $\tan\theta = eEL/(m_e v_0^2)$. Su questo principio funzionavano i tubi a raggi catodici degli oscilloscopi analogici, le stampanti a getto d'inchiostro a deflessione elettrostatica e numerosi spettrometri per particelle cariche. J.J. Thomson utilizzò proprio un dispositivo di questo tipo, combinato con un campo magnetico, per misurare nel 1897 il rapporto $e/m$ dell'elettrone.

Un altro esempio è l'accelerazione di una particella da ferma lungo un campo uniforme per una distanza $d$: la velocità finale si ricava dal teorema dell'energia cinetica, $\frac12 mv^2 = qEd$. Vedremo nella sezione 16.5 che $Ed$ è la differenza di potenziale $\Delta V$ fra i punti estremi, per cui $\frac12mv^2 = q\,\Delta V$; per questo si usa come unità di energia in fisica atomica l'**elettronvolt**, $1\ \text{eV} = 1{,}602\times10^{-19}$ J, energia acquistata da una carica elementare che attraversa una differenza di potenziale di 1 V. Quando la velocità si avvicina a quella della luce la dinamica newtoniana non è più valida e occorre usare la relatività ristretta; per elettroni ciò accade già per differenze di potenziale di qualche decina di kilovolt.

### Esercizio d'esempio

Un elettrone entra con velocità $v_0 = 2{,}0\times10^{7}$ m/s, parallela alle armature, nella regione fra due piastre lunghe $L = 4{,}0$ cm, fra le quali c'è un campo uniforme $E = 1{,}2\times10^{4}$ N/C diretto verso l'alto. Calcolare la deflessione verticale all'uscita e l'angolo di deviazione.

**Soluzione.** La forza sull'elettrone è $\vec{F} = -e\vec{E}$, diretta verso il basso. L'accelerazione ha modulo

$$a = \frac{eE}{m_e} = \frac{1{,}60\times10^{-19}\cdot1{,}2\times10^{4}}{9{,}11\times10^{-31}} \approx 2{,}11\times10^{15}\ \text{m/s}^2.$$

Tempo di transito: $t = L/v_0 = 0{,}040/2{,}0\times10^{7} = 2{,}0\times10^{-9}$ s. Deflessione:

$$y = \tfrac12 a t^2 = \tfrac12\cdot2{,}11\times10^{15}\cdot(2{,}0\times10^{-9})^2 \approx 4{,}2\times10^{-3}\ \text{m} = 4{,}2\ \text{mm}.$$

Velocità verticale all'uscita: $v_y = at \approx 4{,}2\times10^{6}$ m/s. Angolo: $\tan\theta = v_y/v_0 \approx 0{,}21$, cioè $\theta \approx 12^\circ$, verso il basso. La forza peso ($m_eg \approx 9\times10^{-30}$ N) è trascurabile rispetto a quella elettrica ($eE \approx 1{,}9\times10^{-15}$ N).

### Punti chiave

- Il campo elettrico è la forza per unità di carica di prova: $\vec{E} = \vec{F}/q_0$, in N/C = V/m.
- Carica puntiforme: $\vec{E} = \frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\hat{r}$; vale la sovrapposizione anche per i campi.
- Filo indefinito: $E = \lambda/(2\pi\varepsilon_0 r)$; piano indefinito: $E = \sigma/(2\varepsilon_0)$.
- Le linee di campo partono dalle cariche positive, terminano sulle negative, non si incrociano e in elettrostatica non sono chiuse.
- Lungo un tubo di flusso privo di cariche il prodotto $ES$ si conserva.
- In campo uniforme una carica ha accelerazione costante $q\vec{E}/m$: moto rettilineo o parabolico.
- L'elettronvolt ($1{,}602\times10^{-19}$ J) è l'energia acquistata da una carica $e$ attraverso 1 V.

## 16.4 Teorema di Gauss

Il teorema di Gauss è la prima delle leggi fondamentali dell'elettrostatica scritte in forma "globale". Esso collega il flusso del campo elettrico attraverso una superficie chiusa alla carica contenuta al suo interno, e discende direttamente dall'andamento $1/r^2$ della legge di Coulomb e dal principio di sovrapposizione. Oltre al suo valore teorico (è una delle equazioni di Maxwell), il teorema costituisce uno strumento potentissimo per calcolare il campo generato da distribuzioni di carica dotate di simmetria, evitando integrazioni vettoriali laboriose.

### 16.4.1 Flusso

Data una superficie orientata $S$ e un campo vettoriale $\vec{E}$, si definisce **flusso** di $\vec{E}$ attraverso $S$ la grandezza scalare

$$\Phi_S(\vec{E}) = \int_S \vec{E}\cdot\hat{n}\,\mathrm{d}S = \int_S E\cos\theta\,\mathrm{d}S,$$

dove $\hat{n}$ è il versore normale all'elemento di superficie $\mathrm{d}S$ e $\theta$ l'angolo fra $\vec{E}$ e $\hat{n}$. Il flusso si misura in N m²/C (o V m). Per una superficie piana di area $S$ immersa in un campo uniforme che forma un angolo $\theta$ con la normale, il flusso vale semplicemente $ES\cos\theta$: è massimo se il campo è perpendicolare alla superficie, nullo se è tangente a essa.

Il segno del flusso dipende dalla scelta dell'orientazione di $\hat{n}$. Per una **superficie chiusa**, che delimita un volume, la convenzione è di scegliere la normale **uscente**: il flusso è allora positivo quando il campo "esce" dalla superficie e negativo quando "entra". In termini di linee di campo, il flusso attraverso una superficie è proporzionale al numero netto di linee che la attraversano, contando positivamente quelle uscenti e negativamente quelle entranti. Questa interpretazione, pur intuitiva, va presa come immagine qualitativa: il flusso è una grandezza continua e ben definita indipendentemente da come si disegnano le linee.

Il concetto di flusso è mutuato dall'idrodinamica: se $\vec{v}$ è il campo di velocità di un fluido, il flusso di $\vec{v}$ attraverso una superficie è la portata volumetrica, cioè il volume di fluido che attraversa la superficie nell'unità di tempo. Nel caso elettrico non c'è nulla che "scorra", ma la matematica è identica, e l'analogia aiuta a comprendere perché il flusso uscente da una superficie chiusa sia legato alle "sorgenti" contenute al suo interno.

### 16.4.2 Superficie sferica

Consideriamo una carica puntiforme $q$ al centro di una sfera di raggio $R$. Per simmetria il campo sulla sfera è radiale, quindi parallelo alla normale uscente, e ha modulo costante $E = q/(4\pi\varepsilon_0R^2)$. Il flusso si calcola immediatamente:

$$\Phi = \oint_S E\,\mathrm{d}S = E\cdot4\pi R^2 = \frac{q}{4\pi\varepsilon_0R^2}\cdot4\pi R^2 = \frac{q}{\varepsilon_0}.$$

Il risultato è notevole: il flusso **non dipende dal raggio** della sfera. L'area cresce come $R^2$ esattamente quanto il campo diminuisce come $1/R^2$. È qui che si vede il ruolo cruciale dell'esponente 2 nella legge di Coulomb e del fattore $4\pi$ in essa: con un esponente diverso il flusso dipenderebbe da $R$ e non varrebbe alcuna legge semplice. Si può anzi dire che il teorema di Gauss è una riformulazione della legge di Coulomb, equivalente a essa nel caso statico.

Lo stesso risultato si interpreta con le linee di campo: tutte le linee che escono dalla carica attraversano qualsiasi sfera centrata su di essa, e il loro numero, proporzionale a $q$, non dipende dal raggio. Per una carica negativa il flusso vale $q/\varepsilon_0 < 0$, perché le linee entrano.

### 16.4.3 Superficie generica

Il risultato si estende a una qualunque superficie chiusa $S$ che racchiuda la carica. Lo strumento matematico è l'**angolo solido**: l'elemento di superficie $\mathrm{d}S$, visto dalla carica, sottende un angolo solido $\mathrm{d}\Omega = \hat{r}\cdot\hat{n}\,\mathrm{d}S/r^2$. Il flusso elementare vale allora

$$\mathrm{d}\Phi = \frac{q}{4\pi\varepsilon_0}\frac{\hat{r}\cdot\hat{n}}{r^2}\mathrm{d}S = \frac{q}{4\pi\varepsilon_0}\,\mathrm{d}\Omega,$$

e integrando su una superficie chiusa che contiene la carica si ottiene l'angolo solido totale $4\pi$, quindi ancora $\Phi = q/\varepsilon_0$. Se invece la carica è **esterna** alla superficie, ogni cono di vertice $q$ che interseca $S$ la attraversa un numero pari di volte, entrando e uscendo: i contributi corrispondenti hanno lo stesso angolo solido ma segno opposto e si cancellano, per cui il flusso è nullo.

Per il principio di sovrapposizione, data una distribuzione arbitraria di cariche, il flusso del campo totale è la somma dei flussi dovuti alle singole cariche: contribuiscono solo quelle interne. Si arriva così al **teorema di Gauss**:

$$\oint_S \vec{E}\cdot\hat{n}\,\mathrm{d}S = \frac{Q_{\text{int}}}{\varepsilon_0},$$

dove $Q_{\text{int}}$ è la carica totale (con segno) racchiusa dalla superficie. Si sottolinea che il campo $\vec{E}$ che compare a primo membro è il campo **totale**, generato da tutte le cariche, anche quelle esterne; sono le cariche esterne a non contribuire al **flusso** totale, non al campo.

Il teorema vale sempre, ma è utile per calcolare il campo solo quando la simmetria permette di scegliere una **superficie gaussiana** su cui il campo sia costante in modulo e parallelo o perpendicolare alla normale. I tre casi classici sono:

- **simmetria sferica**: per una sfera uniformemente carica di raggio $R$ e carica $Q$, all'esterno $E = Q/(4\pi\varepsilon_0r^2)$ (come se la carica fosse concentrata al centro), all'interno $E = Qr/(4\pi\varepsilon_0R^3)$, che cresce linearmente da zero;
- **simmetria cilindrica**: per un filo indefinito, una superficie cilindrica coassiale di raggio $r$ e altezza $h$ dà $E\cdot2\pi rh = \lambda h/\varepsilon_0$, cioè $E = \lambda/(2\pi\varepsilon_0r)$;
- **simmetria piana**: per un piano indefinito, un cilindretto a cavallo del piano con basi di area $A$ dà $2EA = \sigma A/\varepsilon_0$, cioè $E = \sigma/(2\varepsilon_0)$.

Questi risultati, che con l'integrazione diretta richiederebbero calcoli non banali, si ottengono così in poche righe. Il teorema di Gauss ha anche conseguenze qualitative importanti: per esempio, implica che non possa esistere una configurazione di equilibrio stabile per una carica soggetta solo a forze elettrostatiche (**teorema di Earnshaw**), perché in un punto di equilibrio stabile il campo dovrebbe puntare verso il punto da tutte le direzioni, dando un flusso non nullo attraverso una piccola sfera priva di cariche.

Conviene infine sottolineare alcuni aspetti di metodo nell'uso del teorema. La superficie gaussiana è una superficie **matematica**, scelta liberamente da chi risolve il problema, e non deve coincidere con alcuna superficie fisica; la sua scelta deve rispecchiare la simmetria della distribuzione di carica, perché solo così si può portare il modulo del campo fuori dall'integrale. Prima di applicare il teorema occorre sempre giustificare, con argomenti di simmetria, la direzione del campo e il fatto che il suo modulo dipenda da una sola coordinata: per esempio, per una distribuzione a simmetria sferica, qualsiasi componente tangenziale del campo violerebbe l'invarianza per rotazioni, quindi il campo deve essere radiale. Senza queste premesse il teorema resta vero, ma fornisce soltanto il valore di un integrale e non il campo punto per punto. Si noti inoltre che il teorema di Gauss, da solo, non basta a determinare un campo elettrostatico: un campo arbitrario a divergenza assegnata non è unico, e serve anche l'informazione sulla conservatività (sezione 16.5) per chiudere il problema.

È infine interessante osservare che lo stesso teorema vale per il campo gravitazionale, con la sostituzione $1/(4\pi\varepsilon_0)\to -G$ e carica $\to$ massa: il flusso del campo gravitazionale attraverso una superficie chiusa vale $-4\pi G M_{\text{int}}$. È proprio da questa forma che si ricava il celebre risultato, dimostrato da Newton con fatica, secondo cui un pianeta a simmetria sferica attrae i corpi esterni come se tutta la massa fosse concentrata nel centro, e un guscio sferico omogeneo non esercita alcuna forza sui corpi al suo interno. L'analogo elettrico, il campo nullo all'interno di un guscio sferico uniformemente carico, è stato usato storicamente proprio per verificare con grande precisione l'esponente della legge di Coulomb: misurando l'eventuale campo all'interno di una sfera conduttrice carica, Cavendish prima e poi Maxwell e molti altri hanno posto limiti sempre più stringenti a possibili deviazioni dalla legge dell'inverso del quadrato.

### Esercizio d'esempio

Una sfera isolante di raggio $R = 5{,}0$ cm porta una carica $Q = 3{,}0\ \text{nC}$ distribuita uniformemente nel volume. Calcolare il campo a $r_1 = 2{,}0$ cm e a $r_2 = 10$ cm dal centro.

**Soluzione.** La densità di carica è $\rho = Q/(\frac43\pi R^3)$. Per $r_1 < R$, una sfera gaussiana di raggio $r_1$ racchiude $Q_{\text{int}} = Q\,(r_1/R)^3$. Dal teorema di Gauss $E\cdot4\pi r_1^2 = Q r_1^3/(\varepsilon_0R^3)$, quindi

$$E(r_1) = \frac{Q\,r_1}{4\pi\varepsilon_0R^3} = 8{,}99\times10^{9}\cdot\frac{3{,}0\times10^{-9}\cdot0{,}020}{(0{,}050)^3} = 8{,}99\times10^{9}\cdot\frac{6{,}0\times10^{-11}}{1{,}25\times10^{-4}} \approx 4{,}3\times10^{3}\ \text{N/C}.$$

Per $r_2 > R$ tutta la carica è interna:

$$E(r_2) = \frac{Q}{4\pi\varepsilon_0r_2^2} = 8{,}99\times10^{9}\cdot\frac{3{,}0\times10^{-9}}{(0{,}10)^2} \approx 2{,}7\times10^{3}\ \text{N/C}.$$

Il campo è radiale e uscente in entrambi i punti. Il valore massimo si ha sulla superficie: $E(R) \approx 1{,}08\times10^4$ N/C.

### Punti chiave

- Il flusso di $\vec{E}$ attraverso $S$ è $\Phi = \int_S\vec{E}\cdot\hat{n}\,\mathrm{d}S$; per superfici chiuse si usa la normale uscente.
- Per una carica puntiforme il flusso attraverso qualunque superficie chiusa che la contiene vale $q/\varepsilon_0$, indipendentemente da forma e dimensioni.
- Le cariche esterne danno flusso totale nullo, ma contribuiscono al campo sulla superficie.
- Teorema di Gauss: $\oint_S\vec{E}\cdot\hat{n}\,\mathrm{d}S = Q_{\text{int}}/\varepsilon_0$; è equivalente alla legge di Coulomb in statica.
- È uno strumento di calcolo efficace solo con simmetria sferica, cilindrica o piana.
- Una distribuzione a simmetria sferica genera all'esterno lo stesso campo di una carica puntiforme posta al centro.
- Conseguenza: non esistono punti di equilibrio stabile per cariche soggette solo a forze elettrostatiche (Earnshaw).

## 16.5 Campo conservativo

In meccanica abbiamo visto che le forze il cui lavoro non dipende dal percorso, ma solo dai punti iniziale e finale, si dicono **conservative** e ammettono un'energia potenziale. La forza di Coulomb, essendo una forza centrale che dipende solo dalla distanza, appartiene a questa categoria, esattamente come la forza gravitazionale. Questa proprietà ha conseguenze di enorme portata: consente di introdurre il potenziale elettrostatico, una funzione scalare che contiene tutta l'informazione sul campo vettoriale, e di formulare bilanci energetici per cariche in moto e per intere distribuzioni di carica.

### 16.5.1 Energia potenziale elettrostatica

Calcoliamo il lavoro compiuto dalla forza elettrica quando una carica $q_0$ si sposta da un punto $A$ a un punto $B$ nel campo di una carica puntiforme $q$ fissa nell'origine. Lungo un tratto infinitesimo $\mathrm{d}\vec{l}$ il lavoro è

$$\mathrm{d}W = \vec{F}\cdot\mathrm{d}\vec{l} = \frac{qq_0}{4\pi\varepsilon_0r^2}\,\hat{r}\cdot\mathrm{d}\vec{l} = \frac{qq_0}{4\pi\varepsilon_0r^2}\,\mathrm{d}r,$$

perché $\hat{r}\cdot\mathrm{d}\vec{l}$ è proprio la variazione $\mathrm{d}r$ della distanza dall'origine. Integrando:

$$W_{AB} = \frac{qq_0}{4\pi\varepsilon_0}\left(\frac{1}{r_A}-\frac{1}{r_B}\right).$$

Il lavoro dipende solo dalle distanze iniziale e finale, non dal percorso: la forza è conservativa. Equivalentemente, il lavoro lungo un qualunque percorso chiuso è nullo. Per il principio di sovrapposizione la proprietà vale per il campo di una qualunque distribuzione statica di cariche, che è somma di campi coulombiani.

Si può allora definire l'**energia potenziale elettrostatica** $U$ tale che $W_{AB} = U(A)-U(B) = -\Delta U$. Per due cariche puntiformi, scegliendo nulla l'energia quando sono infinitamente lontane,

$$U(r) = \frac{1}{4\pi\varepsilon_0}\frac{qq_0}{r}.$$

L'energia è positiva per cariche dello stesso segno (sistema repulsivo: occorre fornire lavoro per avvicinarle, e il sistema lo restituisce allontanandosi) e negativa per cariche di segno opposto (sistema legato: occorre lavoro esterno per separarle). Per esempio, nell'atomo di idrogeno l'energia potenziale fra elettrone e protone alla distanza di Bohr $a_0 = 5{,}29\times10^{-11}$ m vale circa $-27{,}2$ eV, e l'energia di legame complessiva, includendo l'energia cinetica, è $-13{,}6$ eV.

Se la carica si muove soggetta alla sola forza elettrica, si conserva l'energia meccanica: $K + U = \text{costante}$. Questo principio consente di risolvere rapidamente molti problemi, come la distanza minima di avvicinamento di una particella $\alpha$ a un nucleo nell'esperimento di Rutherford, oppure la velocità acquistata da uno ione accelerato da un campo elettrico, senza dover conoscere i dettagli della traiettoria.

Il confronto con l'energia potenziale gravitazionale è illuminante. Anche per la gravitazione si ha $U = -GMm/r$, con la stessa dipendenza da $1/r$; la differenza è che il prodotto delle "cariche" gravitazionali è sempre positivo e il segno meno davanti rende l'interazione sempre attrattiva, mentre nel caso elettrico il segno di $U$ è deciso dal prodotto $qq_0$. In entrambi i casi la scelta di porre lo zero dell'energia all'infinito è una convenzione, comoda perché corrisponde alla situazione di cariche non interagenti; qualunque altra scelta lascerebbe invariate le differenze di energia, che sono le uniche grandezze misurabili. Si noti infine che l'energia potenziale è una proprietà del **sistema** delle due cariche, non della sola carica $q_0$: parlare di "energia di $q_0$ nel campo di $q$" è lecito solo quando $q$ è considerata fissa, come un vincolo esterno.

### 16.5.2 Potenziale elettrostatico

Come il campo è la forza per unità di carica, si definisce il **potenziale elettrostatico** come l'energia potenziale per unità di carica di prova:

$$V(P) = \frac{U(P)}{q_0}.$$

Il potenziale si misura in **volt** (V), con $1\ \text{V} = 1\ \text{J/C}$. È una funzione scalare dello spazio, definita a meno di una costante additiva: hanno significato fisico solo le **differenze di potenziale**, legate al campo dalla relazione

$$V(A)-V(B) = \int_A^B\vec{E}\cdot\mathrm{d}\vec{l}.$$

La differenza di potenziale fra due punti è il lavoro compiuto dal campo per portare una carica unitaria positiva dal primo al secondo. Il campo punta nel verso dei potenziali decrescenti: le cariche positive, lasciate libere, si spostano verso potenziali più bassi, quelle negative verso potenziali più alti. Il potenziale di una carica puntiforme, con riferimento all'infinito, è

$$V(r) = \frac{1}{4\pi\varepsilon_0}\frac{q}{r},$$

e per una distribuzione qualsiasi, sovrapponendo i contributi,

$$V(\vec{r}) = \frac{1}{4\pi\varepsilon_0}\int_V\frac{\rho(\vec{r}\,')}{|\vec{r}-\vec{r}\,'|}\,\mathrm{d}V'.$$

Il vantaggio è evidente: si integra una funzione scalare invece di un vettore. Il riferimento all'infinito è possibile solo per distribuzioni di carica limitate; per distribuzioni idealmente infinite (filo, piano) il potenziale all'infinito diverge e occorre scegliere un altro punto di riferimento.

Invertendo la relazione integrale si ricava il campo dal potenziale. In forma infinitesima $\mathrm{d}V = -\vec{E}\cdot\mathrm{d}\vec{l}$, quindi

$$\vec{E} = -\nabla V = -\left(\frac{\partial V}{\partial x}\hat{x}+\frac{\partial V}{\partial y}\hat{y}+\frac{\partial V}{\partial z}\hat{z}\right).$$

Il campo è l'opposto del **gradiente** del potenziale. Questa relazione giustifica l'unità V/m per il campo elettrico. Le **superfici equipotenziali**, luoghi dei punti con lo stesso potenziale, sono in ogni punto perpendicolari alle linee di campo, perché uno spostamento lungo una superficie equipotenziale non comporta variazione di $V$ e quindi $\vec{E}\cdot\mathrm{d}\vec{l} = 0$. Per una carica puntiforme le equipotenziali sono sfere concentriche; per un campo uniforme sono piani perpendicolari al campo, e la differenza di potenziale fra due piani a distanza $d$ vale $\Delta V = Ed$.

Un'immagine utile è quella topografica: il potenziale è come l'altitudine su una mappa, le equipotenziali sono le curve di livello, il campo è diretto lungo la linea di massima pendenza in discesa e il suo modulo è tanto più grande quanto più le curve di livello sono fitte.

Il potenziale è anche la grandezza effettivamente misurata negli strumenti elettrici. Un voltmetro misura sempre una differenza di potenziale fra i suoi due terminali, mai un potenziale "assoluto"; nei circuiti e negli impianti si sceglie come riferimento il potenziale della Terra, cui si attribuisce per convenzione valore nullo (**massa** o **terra**). La Terra, essendo un conduttore di dimensioni enormi, può cedere o assorbire cariche senza che il suo potenziale cambi apprezzabilmente, e per questo costituisce un riferimento stabile. Ordini di grandezza utili: una pila stilo fornisce 1,5 V, la rete domestica 230 V efficaci, le linee di trasmissione ad alta tensione centinaia di kilovolt, la differenza di potenziale fra una nube temporalesca e il suolo può raggiungere le centinaia di milioni di volt. Va infine ricordato che differenze di potenziale elevate non implicano di per sé pericolo: la scarica elettrostatica che si avverte toccando una maniglia dopo aver camminato su una moquette può corrispondere a diverse migliaia di volt, ma la carica e l'energia in gioco sono minuscole.

### 16.5.3 Energia elettrostatica

Oltre all'energia potenziale di una carica in un campo esterno, è importante conoscere l'**energia elettrostatica** di un'intera distribuzione di carica, cioè il lavoro che un agente esterno deve compiere per costruirla portando le cariche una a una dall'infinito, dove inizialmente sono infinitamente lontane fra loro e in quiete. Per due cariche il lavoro è $U_{12} = q_1q_2/(4\pi\varepsilon_0 r_{12})$. Aggiungendo una terza carica occorre vincere sia la forza di $q_1$ sia quella di $q_2$, e così via. Per $N$ cariche puntiformi si ottiene

$$U = \frac{1}{4\pi\varepsilon_0}\sum_{i<j}\frac{q_iq_j}{r_{ij}} = \frac{1}{2}\sum_{i=1}^N q_iV_i,$$

dove $V_i$ è il potenziale nel punto in cui si trova $q_i$ dovuto a tutte le **altre** cariche. Il fattore $1/2$ evita di contare due volte ogni coppia. Il risultato non dipende dall'ordine con cui le cariche vengono portate in posizione, coerentemente con la conservatività.

Per una distribuzione continua la somma diventa un integrale:

$$U = \frac{1}{2}\int_V\rho\,V\,\mathrm{d}V.$$

In questo caso il potenziale $V$ è quello dovuto all'intera distribuzione, perché il contributo di un elemento di carica infinitesimo al potenziale nel suo stesso punto è trascurabile. Questa formula include l'**energia propria** delle cariche, cioè il lavoro necessario per assemblare ciascun elemento di carica; per una carica puntiforme ideale tale energia diverge, segno che il modello puntiforme non è adatto a descrivere la struttura interna delle particelle.

Un esempio classico è la sfera uniformemente carica di raggio $R$ e carica $Q$: costruendola strato dopo strato si ottiene

$$U = \frac{3}{5}\frac{Q^2}{4\pi\varepsilon_0R}.$$

Questa formula fu usata per stimare il "raggio classico dell'elettrone", uguagliando l'energia elettrostatica alla sua energia di riposo $m_ec^2$, e trova applicazione nella fisica nucleare per stimare il contributo della repulsione coulombiana fra protoni all'energia di legame dei nuclei. Nella sezione 16.7 vedremo che la stessa energia si può riscrivere come integrale del quadrato del campo esteso a tutto lo spazio, attribuendo così l'energia al campo stesso.

### Esercizio d'esempio

Un protone parte da fermo dalla piastra positiva di un condensatore piano, fra le cui armature c'è una differenza di potenziale $\Delta V = 500$ V. Calcolare l'energia cinetica e la velocità con cui raggiunge la piastra negativa. Successivamente, il protone viene sparato frontalmente contro un nucleo d'oro ($Z = 79$), supposto fisso: con l'energia cinetica trovata, qual è la minima distanza di avvicinamento?

**Soluzione.** Per la conservazione dell'energia $K = e\,\Delta V = 500$ eV $= 500\cdot1{,}602\times10^{-19} = 8{,}01\times10^{-17}$ J. La velocità:

$$v = \sqrt{\frac{2K}{m_p}} = \sqrt{\frac{2\cdot8{,}01\times10^{-17}}{1{,}673\times10^{-27}}} \approx 3{,}1\times10^{5}\ \text{m/s}.$$

Nell'urto frontale col nucleo, alla minima distanza il protone è istantaneamente fermo e tutta l'energia cinetica è diventata potenziale:

$$K = \frac{1}{4\pi\varepsilon_0}\frac{Ze\cdot e}{r_{\min}}\ \Rightarrow\ r_{\min} = \frac{Ze^2}{4\pi\varepsilon_0K} = \frac{8{,}99\times10^9\cdot79\cdot(1{,}602\times10^{-19})^2}{8{,}01\times10^{-17}} \approx 2{,}3\times10^{-10}\ \text{m}.$$

A questa distanza, paragonabile alle dimensioni atomiche, in realtà la schermatura degli elettroni atomici non sarebbe trascurabile: il calcolo mostra che servono energie dell'ordine dei MeV per sondare le dimensioni nucleari.

### Punti chiave

- La forza di Coulomb è conservativa: il lavoro dipende solo dagli estremi e la circuitazione di $\vec{E}$ è nulla.
- Energia potenziale di due cariche: $U = \frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r}$, nulla all'infinito.
- Il potenziale è energia per unità di carica, in volt: $V = \frac{1}{4\pi\varepsilon_0}\frac{q}{r}$ per la carica puntiforme.
- $V(A)-V(B) = \int_A^B\vec{E}\cdot\mathrm{d}\vec{l}$ e $\vec{E} = -\nabla V$.
- Le superfici equipotenziali sono perpendicolari alle linee di campo; il campo punta verso i potenziali decrescenti.
- L'energia di un sistema di cariche è $U = \frac12\sum q_iV_i$ o $\frac12\int\rho V\,\mathrm{d}V$.
- Sfera uniformemente carica: $U = \frac35\frac{Q^2}{4\pi\varepsilon_0R}$.

## 16.6 Dipolo elettrico

Il **dipolo elettrico** è il sistema formato da due cariche puntiformi uguali in modulo e di segno opposto, $+q$ e $-q$, poste a una distanza fissa $d$. Nonostante la carica totale sia nulla, il dipolo genera un campo elettrico e risente di forze e momenti in presenza di un campo esterno. Il dipolo è un modello di straordinaria importanza: descrive molecole polari come l'acqua, gli atomi polarizzati da un campo esterno, le antenne elementari, e costituisce il primo termine non banale nella descrizione a grande distanza di qualunque distribuzione di carica neutra. La grandezza che lo caratterizza è il **momento di dipolo elettrico**

$$\vec{p} = q\,\vec{d},$$

dove $\vec{d}$ è il vettore che va dalla carica negativa alla positiva. Si misura in C m; per le molecole si usa spesso il debye ($1\ \text{D} \approx 3{,}336\times10^{-30}$ C m). La molecola d'acqua ha $p \approx 1{,}85$ D $\approx 6{,}2\times10^{-30}$ C m.

### 16.6.1 Interazioni create

Calcoliamo il potenziale generato dal dipolo in un punto $P$ a distanza $r$ dal suo centro, con $r\gg d$ (approssimazione di **dipolo puntiforme**). Detto $\theta$ l'angolo fra $\vec{p}$ e la direzione di $P$, le distanze di $P$ dalle due cariche sono circa $r_\pm \approx r\mp\frac{d}{2}\cos\theta$. Sommando i potenziali:

$$V = \frac{q}{4\pi\varepsilon_0}\left(\frac{1}{r_+}-\frac{1}{r_-}\right) \approx \frac{q}{4\pi\varepsilon_0}\frac{d\cos\theta}{r^2} = \frac{1}{4\pi\varepsilon_0}\frac{\vec{p}\cdot\hat{r}}{r^2}.$$

Il potenziale del dipolo decresce come $1/r^2$, più rapidamente di quello di una carica singola: a grande distanza le due cariche tendono a compensarsi. Il potenziale è nullo sul piano perpendicolare a $\vec{p}$ passante per il centro (piano equatoriale), positivo dal lato della carica positiva e negativo dall'altro.

Il campo si ottiene dal gradiente in coordinate polari: $E_r = -\partial V/\partial r$ e $E_\theta = -\frac{1}{r}\partial V/\partial\theta$, da cui

$$E_r = \frac{1}{4\pi\varepsilon_0}\frac{2p\cos\theta}{r^3},\qquad E_\theta = \frac{1}{4\pi\varepsilon_0}\frac{p\sin\theta}{r^3},$$

o, in forma vettoriale indipendente dalle coordinate,

$$\vec{E} = \frac{1}{4\pi\varepsilon_0}\frac{3(\vec{p}\cdot\hat{r})\hat{r}-\vec{p}}{r^3}.$$

Il campo decresce come $1/r^3$. Sull'asse del dipolo ($\theta=0$) vale $2p/(4\pi\varepsilon_0r^3)$ ed è parallelo a $\vec{p}$; sul piano equatoriale ($\theta = \pi/2$) vale $p/(4\pi\varepsilon_0r^3)$ ed è antiparallelo a $\vec{p}$. Le linee di campo escono dalla carica positiva e rientrano nella negativa, formando caratteristici "lobi" simmetrici. È importante sottolineare che queste formule valgono solo lontano dal dipolo; nelle vicinanze delle cariche occorre usare l'espressione esatta come somma di due campi coulombiani.

### 16.6.2 Interazioni subite

Poniamo ora un dipolo rigido in un **campo esterno uniforme** $\vec{E}$. Le forze sulle due cariche sono $+q\vec{E}$ e $-q\vec{E}$, uguali e opposte: la **forza risultante è nulla** e il centro di massa del dipolo non accelera. Le due forze però non sono applicate nello stesso punto e formano una coppia, il cui momento vale

$$\vec{M} = \vec{p}\times\vec{E},$$

con modulo $pE\sin\theta$. Il momento tende ad allineare il dipolo al campo. L'energia potenziale del dipolo nel campo è

$$U = -\vec{p}\cdot\vec{E} = -pE\cos\theta,$$

minima ($-pE$) quando $\vec{p}$ è parallelo a $\vec{E}$ (equilibrio stabile) e massima ($+pE$) quando è antiparallelo (equilibrio instabile). Il lavoro necessario per ruotare il dipolo dalla posizione stabile a quella instabile è $2pE$. Un dipolo spostato di poco dall'equilibrio stabile compie oscillazioni attorno alla direzione del campo, come un pendolo; con un certo attrito (per esempio per urti in un fluido) finisce per allinearsi. È questo il meccanismo microscopico della **polarizzazione per orientamento** nei dielettrici polari, contrastata dall'agitazione termica.

Se il campo esterno **non è uniforme**, oltre al momento il dipolo subisce anche una forza netta, perché le due cariche si trovano in punti con campi diversi. Per un dipolo puntiforme si ottiene

$$\vec{F} = (\vec{p}\cdot\nabla)\vec{E} = \nabla(\vec{p}\cdot\vec{E})\ \ (\text{per }\vec{p}\text{ costante}),$$

cioè la forza è l'opposto del gradiente dell'energia potenziale. Un dipolo allineato al campo viene attratto verso le regioni in cui il campo è più intenso. È proprio quello che succede ai pezzetti di carta attratti da una bacchetta carica: si polarizzano allineando il dipolo indotto al campo e vengono quindi attirati verso la bacchetta, dove il campo è più forte. Lo stesso principio è alla base della **dielettroforesi**, tecnica usata per manipolare cellule e microparticelle in campi non uniformi.

È utile distinguere due tipi di dipoli molecolari. Le **molecole polari**, come l'acqua, l'ammoniaca o l'acido cloridrico, possiedono un momento di dipolo **permanente**, dovuto alla struttura asimmetrica della distribuzione degli elettroni di legame; in assenza di campo i loro dipoli sono orientati a caso per l'agitazione termica e il momento medio è nullo, mentre un campo esterno tende a orientarli producendo un momento medio parallelo al campo. Le **molecole apolari**, come l'ossigeno, l'azoto o gli atomi dei gas nobili, non hanno momento permanente, ma in un campo esterno acquistano un momento di dipolo **indotto** proporzionale al campo, $\vec{p} = \alpha\vec{E}$, dove $\alpha$ è la **polarizzabilità** della molecola. In entrambi i casi l'effetto macroscopico è la polarizzazione del materiale, ma la dipendenza dalla temperatura è diversa: la polarizzazione per orientamento diminuisce al crescere della temperatura, quella per deformazione ne è praticamente indipendente. Lo stesso concetto di dipolo indotto spiega le forze di van der Waals fra molecole neutre, responsabili della coesione dei liquidi e dei solidi molecolari.

### 16.6.3 Sviluppo in multipoli

Il dipolo è il secondo termine di una serie più generale. Consideriamo una distribuzione di carica arbitraria confinata in una regione di dimensioni $a$ attorno all'origine e calcoliamone il potenziale in un punto lontano, con $r\gg a$. Sviluppando $1/|\vec{r}-\vec{r}\,'|$ in serie di potenze di $r'/r$ si ottiene lo **sviluppo in multipoli**:

$$V(\vec{r}) = \frac{1}{4\pi\varepsilon_0}\left[\frac{Q}{r}+\frac{\vec{p}\cdot\hat{r}}{r^2}+\frac{1}{2}\sum_{ij}Q_{ij}\frac{\hat{r}_i\hat{r}_j}{r^3}+\dots\right].$$

Il primo termine, di **monopolo**, dipende solo dalla carica totale $Q = \int\rho\,\mathrm{d}V$ e decresce come $1/r$. Il secondo, di **dipolo**, dipende dal momento di dipolo della distribuzione $\vec{p} = \int\rho\,\vec{r}\,'\,\mathrm{d}V'$ e decresce come $1/r^2$. Il terzo, di **quadrupolo**, è descritto da un tensore simmetrico $Q_{ij}$ e decresce come $1/r^3$, e così via con ottupolo e termini superiori.

Lo sviluppo ha un valore pratico enorme: a grande distanza basta conoscere i primi termini non nulli. Il rapporto fra due termini successivi è dell'ordine di $a/r$, quindi a una distanza dieci volte maggiore delle dimensioni della sorgente ogni termine è circa dieci volte più piccolo del precedente, e l'approssimazione di troncare la serie al primo termine non nullo è eccellente. Per una distribuzione con carica netta, il termine di monopolo domina e la distribuzione appare come una carica puntiforme; per una distribuzione neutra domina il termine di dipolo, se non nullo; per distribuzioni con carica e dipolo nulli (come la molecola di CO$_2$, lineare e simmetrica) il primo termine non nullo è il quadrupolo. Si noti che il momento di dipolo dipende in generale dalla scelta dell'origine, ma diventa indipendente da essa quando la carica totale è nulla; analogamente il primo momento non nullo è sempre indipendente dall'origine. Lo sviluppo in multipoli si applica anche alla gravità (forma della Terra e dei pianeti), al magnetismo e alla radiazione delle antenne.

### Esercizio d'esempio

Una molecola d'acqua ($p = 6{,}2\times10^{-30}$ C m) si trova in un campo uniforme $E = 2{,}0\times10^{5}$ N/C. (a) Calcolare il momento massimo agente sulla molecola. (b) Calcolare il lavoro necessario per ruotarla da $\theta = 0$ a $\theta = 90^\circ$. (c) Confrontare l'energia di orientamento con l'energia termica $k_BT$ a 300 K. (d) Calcolare il campo generato dalla molecola a $r = 1{,}0$ nm lungo il suo asse.

**Soluzione.** (a) $M_{\max} = pE = 6{,}2\times10^{-30}\cdot2{,}0\times10^{5} = 1{,}24\times10^{-24}$ N m.

(b) $W = U(90^\circ)-U(0) = 0-(-pE) = pE = 1{,}24\times10^{-24}$ J.

(c) $k_BT = 1{,}38\times10^{-23}\cdot300 = 4{,}14\times10^{-21}$ J. Il rapporto $pE/k_BT \approx 3\times10^{-4}$: l'agitazione termica prevale nettamente e l'allineamento medio è debole, come accade nei dielettrici polari reali.

(d) Sull'asse:

$$E = \frac{1}{4\pi\varepsilon_0}\frac{2p}{r^3} = 8{,}99\times10^9\cdot\frac{2\cdot6{,}2\times10^{-30}}{(1{,}0\times10^{-9})^3} \approx 1{,}1\times10^{8}\ \text{N/C}.$$

### Punti chiave

- Il momento di dipolo è $\vec{p} = q\vec{d}$, diretto dalla carica negativa alla positiva, in C m.
- Potenziale del dipolo: $V = \frac{1}{4\pi\varepsilon_0}\frac{\vec{p}\cdot\hat{r}}{r^2}$; campo $\propto1/r^3$.
- In campo uniforme: forza nulla, momento $\vec{M} = \vec{p}\times\vec{E}$, energia $U = -\vec{p}\cdot\vec{E}$.
- L'equilibrio è stabile con $\vec{p}$ parallelo a $\vec{E}$, instabile se antiparallelo.
- In campo non uniforme il dipolo allineato è attratto verso le zone di campo più intenso.
- Lo sviluppo in multipoli descrive a grande distanza ogni distribuzione: monopolo $1/r$, dipolo $1/r^2$, quadrupolo $1/r^3$.
- Il primo momento non nullo di una distribuzione non dipende dalla scelta dell'origine.

## 16.7 Formulazione differenziale

Le leggi dell'elettrostatica viste finora sono scritte in forma **integrale**: il teorema di Gauss lega il flusso attraverso una superficie chiusa alla carica contenuta, la conservatività afferma che la circuitazione del campo lungo una linea chiusa è nulla. Queste formulazioni riguardano regioni estese dello spazio. È possibile, ed estremamente utile, riscriverle in forma **locale**, cioè come relazioni fra il campo e le sue derivate in ogni punto dello spazio. Questa formulazione differenziale è quella in cui si scrivono di solito le equazioni di Maxwell; permette di trattare in modo sistematico i problemi elettrostatici come problemi di equazioni alle derivate parziali con condizioni al contorno, ed è il punto di partenza per i metodi numerici usati in ingegneria (differenze finite, elementi finiti). Gli strumenti matematici necessari sono gli operatori **divergenza** e **rotore** e i due teoremi integrali di Gauss–Green (o della divergenza) e di Stokes.

### 16.7.1 Condizioni al contorno

Prima di affrontare le equazioni locali, è istruttivo vedere che cosa accade al campo quando si attraversa una superficie su cui è distribuita una carica con densità superficiale $\sigma$. In un punto di una tale superficie il campo non è in generale continuo: si comporta in modo diverso nella componente perpendicolare e in quella parallela alla superficie.

Per la **componente normale** si applica il teorema di Gauss a un cilindretto infinitesimo ("scatoletta di Gauss") a cavallo della superficie, con basi di area $\Delta S$ parallele a essa e altezza trascurabile. Il flusso attraverso la superficie laterale tende a zero con l'altezza, e restano i contributi delle due basi:

$$(\vec{E}_2-\vec{E}_1)\cdot\hat{n}\,\Delta S = \frac{\sigma\,\Delta S}{\varepsilon_0}\ \Rightarrow\ E_{2n}-E_{1n} = \frac{\sigma}{\varepsilon_0},$$

dove $\hat{n}$ è la normale orientata dal mezzo 1 al mezzo 2. La componente normale subisce dunque un **salto** pari a $\sigma/\varepsilon_0$. Si verifica subito che per un piano indefinito, con $E = \sigma/(2\varepsilon_0)$ da entrambi i lati e versi opposti, il salto è proprio $\sigma/\varepsilon_0$.

Per la **componente tangenziale** si usa la conservatività: si calcola la circuitazione del campo lungo un rettangolino infinitesimo con due lati paralleli alla superficie, di lunghezza $\Delta l$, uno per parte, e lati perpendicolari di lunghezza trascurabile. La circuitazione nulla implica

$$(\vec{E}_2-\vec{E}_1)\cdot\hat{t}\,\Delta l = 0\ \Rightarrow\ E_{2t} = E_{1t}.$$

La componente tangenziale è **continua** attraverso qualsiasi superficie. Di conseguenza anche il potenziale è continuo attraverso uno strato di carica superficiale (una discontinuità del potenziale richiederebbe un campo infinito), mentre la sua derivata normale presenta un salto. Queste condizioni al contorno sono fondamentali nello studio dei conduttori (capitolo 17) e dei dielettrici, e rappresentano il caso limite delle equazioni differenziali in presenza di distribuzioni superficiali, dove le derivate ordinarie perdono significato.

### 16.7.2 Leggi di Maxwell

Il **teorema della divergenza** afferma che, per un campo vettoriale regolare, il flusso uscente da una superficie chiusa è uguale all'integrale della divergenza sul volume racchiuso:

$$\oint_S\vec{E}\cdot\hat{n}\,\mathrm{d}S = \int_V\nabla\cdot\vec{E}\,\mathrm{d}V,\qquad \nabla\cdot\vec{E} = \frac{\partial E_x}{\partial x}+\frac{\partial E_y}{\partial y}+\frac{\partial E_z}{\partial z}.$$

La divergenza di un campo in un punto rappresenta il flusso uscente per unità di volume da un volumetto infinitesimo attorno a quel punto: misura quanto il punto si comporta da "sorgente" del campo. Scrivendo la carica interna come $Q_{\text{int}} = \int_V\rho\,\mathrm{d}V$, il teorema di Gauss diventa $\int_V(\nabla\cdot\vec{E}-\rho/\varepsilon_0)\,\mathrm{d}V = 0$ per qualunque volume $V$; ciò è possibile solo se l'integrando è nullo ovunque:

$$\nabla\cdot\vec{E} = \frac{\rho}{\varepsilon_0}.$$

È la **prima equazione di Maxwell** (legge di Gauss in forma locale): le sorgenti del campo elettrico sono le cariche, e in ogni punto privo di carica la divergenza del campo è nulla. Il campo elettrico "nasce" dove c'è carica positiva e "muore" dove c'è carica negativa.

Analogamente, il **teorema di Stokes** afferma che la circuitazione di un campo lungo una linea chiusa è uguale al flusso del rotore attraverso una qualsiasi superficie che ha la linea come bordo:

$$\oint_\gamma\vec{E}\cdot\mathrm{d}\vec{l} = \int_S(\nabla\times\vec{E})\cdot\hat{n}\,\mathrm{d}S.$$

Il rotore misura la tendenza del campo a "girare" attorno a un punto. Poiché il campo elettrostatico ha circuitazione nulla lungo qualsiasi linea chiusa, il flusso del rotore è nullo attraverso qualsiasi superficie, e quindi

$$\nabla\times\vec{E} = 0.$$

È la **seconda equazione di Maxwell nel caso statico**: il campo elettrostatico è **irrotazionale**. In elettrodinamica questa equazione verrà modificata dalla legge di Faraday, $\nabla\times\vec{E} = -\partial\vec{B}/\partial t$, ma in condizioni statiche il rotore è nullo. Un campo irrotazionale in una regione semplicemente connessa è sempre il gradiente di una funzione scalare, e infatti $\vec{E} = -\nabla V$ soddisfa identicamente $\nabla\times\vec{E} = 0$, perché il rotore di un gradiente è sempre nullo.

Combinando le due equazioni si ottiene un'unica equazione per il potenziale. Sostituendo $\vec{E} = -\nabla V$ nella legge di Gauss:

$$\nabla^2V = \frac{\partial^2V}{\partial x^2}+\frac{\partial^2V}{\partial y^2}+\frac{\partial^2V}{\partial z^2} = -\frac{\rho}{\varepsilon_0}.$$

È l'**equazione di Poisson**; nelle regioni prive di carica diventa l'**equazione di Laplace** $\nabla^2V = 0$. L'operatore $\nabla^2$ è il laplaciano. Il problema generale dell'elettrostatica si riduce così a risolvere l'equazione di Poisson con opportune condizioni al contorno (valori del potenziale sui conduttori, o della sua derivata normale). Un risultato matematico fondamentale, il **teorema di unicità**, garantisce che, assegnate la densità di carica nel volume e le condizioni sul bordo, la soluzione è unica: qualunque metodo che produca una soluzione (anche indovinata, come nel metodo delle cariche immagine) fornisce la soluzione corretta. Le funzioni che soddisfano l'equazione di Laplace, dette armoniche, hanno la proprietà che il valore in un punto è la media dei valori su una sfera centrata in esso: non hanno massimi né minimi interni, il che è un'altra forma del teorema di Earnshaw.

### 16.7.3 Energia elettrostatica

Nella sezione 16.5 abbiamo scritto l'energia di una distribuzione come $U = \frac12\int\rho V\,\mathrm{d}V$. Con la formulazione differenziale possiamo esprimerla in funzione del solo campo. Sostituendo $\rho = \varepsilon_0\nabla\cdot\vec{E}$ e usando l'identità vettoriale $\nabla\cdot(V\vec{E}) = V\nabla\cdot\vec{E}+\vec{E}\cdot\nabla V$:

$$U = \frac{\varepsilon_0}{2}\int V\,\nabla\cdot\vec{E}\,\mathrm{d}V = \frac{\varepsilon_0}{2}\left[\oint_S V\vec{E}\cdot\hat{n}\,\mathrm{d}S-\int\vec{E}\cdot\nabla V\,\mathrm{d}V\right].$$

Se si estende l'integrazione a tutto lo spazio, per una distribuzione limitata l'integrale di superficie su una sfera di raggio $R\to\infty$ tende a zero, perché $V\sim1/R$, $E\sim1/R^2$ e l'area cresce solo come $R^2$. Ricordando che $-\nabla V = \vec{E}$ resta

$$U = \frac{\varepsilon_0}{2}\int_{\text{tutto lo spazio}}E^2\,\mathrm{d}V.$$

Questo risultato suggerisce di interpretare l'energia come **localizzata nel campo**, con una **densità di energia**

$$u = \frac{\varepsilon_0}{2}E^2,$$

misurata in J/m³. In elettrostatica le due interpretazioni (energia associata alle cariche oppure al campo) sono matematicamente equivalenti, perché danno lo stesso valore totale. In elettrodinamica, però, si osservano onde elettromagnetiche che si propagano lontano da qualsiasi carica e trasportano energia: l'interpretazione in termini di densità di energia del campo diventa allora l'unica fisicamente sostenibile.

La formula con $E^2$ è sempre positiva, mentre $\frac12\sum q_iV_i$ può essere negativa: la differenza sta nel fatto che la formula di campo include l'energia propria delle singole cariche, che è positiva (e infinita per cariche puntiformi). Per distribuzioni continue e regolari le due espressioni coincidono. A titolo d'esempio, si può verificare che per una sfera uniformemente carica l'integrale di $\frac{\varepsilon_0}{2}E^2$ sull'interno e sull'esterno, con i campi trovati nella sezione 16.4, restituisce esattamente $\frac35Q^2/(4\pi\varepsilon_0R)$: il contributo esterno vale $\frac12Q^2/(4\pi\varepsilon_0R)$ e quello interno $\frac{1}{10}Q^2/(4\pi\varepsilon_0R)$.

L'espressione dell'energia in termini di campo ha anche un utile risvolto pratico: la rigidità dielettrica dell'aria, circa $3\times10^6$ V/m, pone un limite alla densità di energia immagazzinabile in un campo elettrico in aria, pari a $u_{\max} = \frac12\varepsilon_0E^2 \approx 40$ J/m³, valore modesto se confrontato con le densità di energia chimiche, e questo spiega perché per immagazzinare energia elettrostatica in modo efficiente si usino dielettrici solidi ad alta rigidità.

### Esercizio d'esempio

In una regione di spazio il potenziale elettrostatico è $V(x,y,z) = V_0\,(x^2-y^2)/a^2 + \alpha z^2$, con $V_0 = 100$ V, $a = 0{,}10$ m. (a) Determinare $\alpha$ affinché la regione sia priva di carica. (b) Con $\alpha = 0$, calcolare la densità di carica. (c) Nel caso (a), calcolare il campo e la densità di energia nel punto $P = (0{,}05;\ 0;\ 0)$ m.

**Soluzione.** (a) Laplaciano: $\nabla^2V = 2V_0/a^2-2V_0/a^2+2\alpha = 2\alpha$. Per avere $\rho = 0$ serve $\nabla^2V = 0$, quindi $\alpha = 0$.

(b) Con $\alpha = 0$ si ha già $\nabla^2V = 0$, quindi $\rho = -\varepsilon_0\nabla^2V = 0$: il potenziale descrive una regione vuota di carica (è il potenziale di un quadrupolo elettrico, usato nelle trappole ioniche). Se invece, per esempio, $\alpha = 1000$ V/m², si avrebbe $\rho = -\varepsilon_0\cdot2000 \approx -1{,}8\times10^{-8}$ C/m³.

(c) $\vec{E} = -\nabla V = -\frac{2V_0}{a^2}(x\,\hat{x}-y\,\hat{y})$. In $P$: $E_x = -\frac{2\cdot100}{0{,}01}\cdot0{,}05 = -1000$ V/m, $E_y = E_z = 0$. Densità di energia:

$$u = \tfrac12\varepsilon_0E^2 = \tfrac12\cdot8{,}85\times10^{-12}\cdot10^6 \approx 4{,}4\times10^{-6}\ \text{J/m}^3.$$

Si verifica anche $\nabla\times\vec{E} = 0$, come deve essere per un campo derivante da un potenziale.

### Punti chiave

- Componente normale del campo: salto $E_{2n}-E_{1n} = \sigma/\varepsilon_0$; componente tangenziale continua.
- Prima equazione di Maxwell: $\nabla\cdot\vec{E} = \rho/\varepsilon_0$ (Gauss in forma locale).
- Seconda equazione in statica: $\nabla\times\vec{E} = 0$; il campo è irrotazionale e quindi $\vec{E} = -\nabla V$.
- Equazione di Poisson $\nabla^2V = -\rho/\varepsilon_0$; nel vuoto equazione di Laplace $\nabla^2V = 0$.
- Il teorema di unicità garantisce una sola soluzione date sorgenti e condizioni al contorno.
- L'energia elettrostatica si scrive $U = \frac{\varepsilon_0}{2}\int E^2\,\mathrm{d}V$, con densità $u = \frac12\varepsilon_0E^2$.
- L'energia può essere pensata come localizzata nel campo, interpretazione indispensabile in elettrodinamica.
