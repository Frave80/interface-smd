# Capitolo 18 — Condensatori

Il condensatore è il primo vero "componente" elettrico che si incontra studiando l'elettrostatica: un dispositivo costituito da due conduttori isolati fra loro, capace di immagazzinare carica elettrica e, con essa, energia associata al campo elettrico. Dopo aver studiato nel capitolo precedente il comportamento dei conduttori in equilibrio elettrostatico, siamo ora in grado di analizzare sistemi formati da due conduttori affacciati e di introdurre una grandezza che ne riassume in un solo numero il comportamento elettrico: la capacità. In questo capitolo definiremo la capacità e la calcoleremo per le geometrie fondamentali (piana, cilindrica, sferica), ricaveremo l'energia immagazzinata e la densità di energia del campo elettrostatico, studieremo i collegamenti in serie e in parallelo e concluderemo con il concetto più generale di mutua capacità, che descrive l'interazione elettrostatica fra più conduttori e ha importanti ricadute pratiche, ad esempio negli accoppiamenti parassiti dei circuiti elettronici.

## 18.1 Capacità

Un **condensatore** è un sistema di due conduttori, detti **armature**, separati da un mezzo isolante (il vuoto, l'aria o un materiale dielettrico) e disposti in modo tale che, quando su di essi si trovano cariche uguali e opposte $+Q$ e $-Q$, praticamente tutte le linee di forza del campo elettrico che partono dall'armatura positiva terminino sull'armatura negativa. Questa condizione si chiama **induzione completa**: essa garantisce che il campo elettrico sia confinato, in buona approssimazione, nella regione compresa fra le armature e che il sistema sia elettricamente "chiuso", cioè poco sensibile alla presenza di altri corpi carichi nell'ambiente circostante.

Poiché ciascuna armatura è un conduttore in equilibrio, essa è una superficie equipotenziale; fra le due armature esiste quindi una ben definita **differenza di potenziale** $\Delta V = V_+ - V_-$. L'osservazione sperimentale fondamentale, che discende direttamente dalla linearità delle equazioni dell'elettrostatica (principio di sovrapposizione), è che la carica $Q$ e la differenza di potenziale $\Delta V$ sono direttamente proporzionali: se raddoppiamo la carica sulle armature, la distribuzione superficiale di carica raddoppia punto per punto mantenendo la stessa forma, il campo raddoppia ovunque e con esso raddoppia l'integrale di linea che fornisce la differenza di potenziale. Si definisce allora la **capacità** del condensatore come la costante di proporzionalità:

$$C = \frac{Q}{\Delta V}$$

La capacità si misura in **farad** (simbolo F), con $1\ \text{F} = 1\ \text{C}/\text{V}$. Si tratta di un'unità enorme rispetto ai valori tipici dei dispositivi reali: i condensatori impiegati nei circuiti elettronici hanno capacità che vanno dai picofarad ($10^{-12}$ F) ai millifarad, mentre solo i cosiddetti supercondensatori, che sfruttano strati elettrochimici di spessore nanometrico, raggiungono valori di migliaia di farad. È utile notare fin da subito che la capacità dipende **esclusivamente dalla geometria** delle armature (forma, dimensioni, distanza reciproca) e dalle proprietà del mezzo interposto, ma non dalla carica né dalla tensione applicata: è una proprietà del dispositivo, esattamente come la massa è una proprietà di un corpo e non della forza che gli viene applicata.

Il concetto di capacità si può estendere anche a un **conduttore isolato**: in questo caso si immagina che la seconda armatura sia una sfera di raggio infinito posta a potenziale nullo (l'"infinito"), e si definisce $C = Q/V$, dove $V$ è il potenziale del conduttore rispetto all'infinito. Per una sfera conduttrice di raggio $R$ nel vuoto, il potenziale vale $V = Q/(4\pi\varepsilon_0 R)$ e quindi $C = 4\pi\varepsilon_0 R$. Questo risultato mostra subito quanto sia grande il farad: una sfera con capacità di 1 F dovrebbe avere un raggio di circa $9\times 10^9$ m, oltre mille volte il raggio terrestre. La Terra stessa, considerata come sfera conduttrice, ha una capacità di soli 0.7 mF circa.

Il procedimento generale per calcolare la capacità di un condensatore è sempre lo stesso e conviene fissarlo come metodo: (1) si suppone che sulle armature ci siano le cariche $+Q$ e $-Q$; (2) si determina il campo elettrico $\vec{E}$ nella regione fra le armature, tipicamente sfruttando la simmetria e il teorema di Gauss; (3) si calcola la differenza di potenziale integrando il campo lungo un percorso qualsiasi che vada dall'armatura positiva a quella negativa, $\Delta V = \int_+^- \vec{E}\cdot d\vec{l}$; (4) si fa il rapporto $Q/\Delta V$, nel quale la carica $Q$ si semplifica necessariamente, lasciando un'espressione puramente geometrica. Applichiamo ora questo metodo alle tre geometrie classiche.

### 18.1.1 Condensatore piano

Il **condensatore piano** è formato da due lastre conduttrici piane e parallele, ciascuna di area $S$, poste a distanza $d$ l'una dall'altra. Supponiamo che le dimensioni lineari delle armature siano molto maggiori della distanza, $\sqrt{S} \gg d$: in questa ipotesi si possono trascurare gli **effetti di bordo**, ovvero la deformazione delle linee di campo vicino ai margini delle lastre, e trattare ciascuna armatura come un piano indefinito.

Quando le armature portano le cariche $\pm Q$, la carica si distribuisce sulle facce interne affacciate con densità superficiale uniforme $\sigma = Q/S$. Il campo generato da un piano indefinito uniformemente carico ha modulo $\sigma/(2\varepsilon_0)$ ed è diretto perpendicolarmente al piano. Sovrapponendo i contributi delle due armature si trova che all'esterno i due campi, uguali e opposti, si annullano, mentre all'interno si sommano. Lo stesso risultato si ottiene in modo ancora più diretto con il teorema di Coulomb per i conduttori: appena fuori dalla superficie di un conduttore il campo vale $\sigma/\varepsilon_0$. Il campo fra le armature è quindi uniforme e vale

$$E = \frac{\sigma}{\varepsilon_0} = \frac{Q}{\varepsilon_0 S}$$

La differenza di potenziale si ottiene integrando un campo costante lungo un segmento perpendicolare alle armature, $\Delta V = E d = Q d/(\varepsilon_0 S)$, e quindi la capacità è

$$C = \frac{\varepsilon_0 S}{d}$$

Questa formula, forse la più usata di tutto il capitolo, contiene tutta la fisica essenziale: la capacità cresce proporzionalmente all'area delle armature, perché a parità di tensione una superficie maggiore ospita più carica, e cresce al diminuire della distanza, perché a parità di carica un campo uniforme produce una differenza di potenziale proporzionale alla distanza percorsa. Per avere capacità elevate occorrono quindi armature grandi e molto vicine; i condensatori commerciali realizzano questo obiettivo arrotolando lunghi nastri metallici separati da sottilissimi film isolanti, o sfruttando strati di ossido di spessore micrometrico come nei condensatori elettrolitici. La costante $\varepsilon_0 = 8.854\times 10^{-12}\ \text{F/m}$ assume qui un significato operativo immediato: è la capacità per unità di area e per unità di inverso della distanza, e le sue unità F/m derivano proprio da questa formula.

Nella realtà gli effetti di bordo producono un leggero aumento della capacità rispetto al valore ideale, perché le linee di campo che "sporgono" dai margini aggiungono un contributo di carica alle facce esterne vicino ai bordi. Questo effetto è tanto più piccolo quanto più è soddisfatta la condizione $d \ll \sqrt{S}$, e nei casi pratici di interesse è trascurabile. Un modo classico per ridurlo, usato nei condensatori campione di laboratorio, è circondare l'armatura di misura con un **anello di guardia** mantenuto allo stesso potenziale.

### 18.1.2 Condensatore cilindrico

Il **condensatore cilindrico** è costituito da due superfici cilindriche conduttrici coassiali: un'armatura interna di raggio $R_1$ e un'armatura esterna di raggio $R_2 > R_1$, entrambe di lunghezza $L$. Anche qui assumiamo $L \gg R_2$ per poter trascurare gli effetti alle estremità e considerare il sistema dotato di simmetria cilindrica. L'esempio tecnologico più importante è il **cavo coassiale**, impiegato per trasmettere segnali televisivi e di strumentazione: la sua capacità per unità di lunghezza è un parametro di progetto fondamentale.

Poniamo la carica $+Q$ sull'armatura interna e $-Q$ su quella esterna. Per simmetria il campo nella regione $R_1 < r < R_2$ è radiale e il suo modulo dipende solo dalla distanza $r$ dall'asse. Applichiamo il teorema di Gauss a una superficie cilindrica coassiale di raggio $r$ e lunghezza $L$: il flusso attraverso le basi è nullo perché il campo è parallelo a esse, mentre il flusso laterale vale $E\cdot 2\pi r L$. La carica racchiusa è $Q$, e quindi

$$E(r) = \frac{Q}{2\pi\varepsilon_0 L r} = \frac{\lambda}{2\pi\varepsilon_0 r}$$

dove $\lambda = Q/L$ è la carica per unità di lunghezza. Il campo, a differenza del caso piano, non è uniforme: decresce come $1/r$ allontanandosi dall'asse ed è massimo in prossimità del conduttore interno. Questo dettaglio ha conseguenze pratiche, perché la **rigidità dielettrica** dell'isolante, cioè il campo massimo che esso sopporta prima di scaricarsi, va confrontata proprio con il campo sulla superficie interna.

La differenza di potenziale si ottiene integrando lungo un raggio:

$$\Delta V = \int_{R_1}^{R_2} \frac{Q}{2\pi\varepsilon_0 L r}\,dr = \frac{Q}{2\pi\varepsilon_0 L}\ln\frac{R_2}{R_1}$$

e quindi la capacità è

$$C = \frac{2\pi\varepsilon_0 L}{\ln(R_2/R_1)}$$

La capacità è proporzionale alla lunghezza, il che rende naturale parlare di capacità per unità di lunghezza $C/L = 2\pi\varepsilon_0/\ln(R_2/R_1)$. La dipendenza dal rapporto dei raggi è soltanto logaritmica: per variare sensibilmente la capacità occorre cambiare di molto la geometria. È istruttivo verificare il **limite piano**: se lo spessore $d = R_2 - R_1$ è molto piccolo rispetto a $R_1$, si ha $\ln(R_2/R_1) = \ln(1 + d/R_1) \simeq d/R_1$, da cui $C \simeq 2\pi\varepsilon_0 R_1 L/d = \varepsilon_0 S/d$, con $S = 2\pi R_1 L$ area dell'armatura. Ritroviamo esattamente il condensatore piano: quando la distanza fra le armature è piccola rispetto al loro raggio di curvatura, la curvatura diventa irrilevante e localmente le armature appaiono piane.

### 18.1.3 Condensatore sferico

Il **condensatore sferico** è formato da due gusci sferici conduttori concentrici, di raggi $R_1 < R_2$. Grazie alla simmetria sferica non ci sono effetti di bordo, e il calcolo è esatto. Con $+Q$ sulla sfera interna e $-Q$ su quella esterna, il teorema di Gauss applicato a una sfera di raggio $r$ compreso fra le armature fornisce un campo radiale identico a quello di una carica puntiforme posta nel centro:

$$E(r) = \frac{Q}{4\pi\varepsilon_0 r^2}, \qquad R_1 < r < R_2$$

All'esterno ($r > R_2$) la carica racchiusa è nulla e il campo si annulla: l'induzione è completa e il sistema è perfettamente schermato. La differenza di potenziale vale

$$\Delta V = \frac{Q}{4\pi\varepsilon_0}\left(\frac{1}{R_1} - \frac{1}{R_2}\right) = \frac{Q}{4\pi\varepsilon_0}\frac{R_2 - R_1}{R_1 R_2}$$

da cui

$$C = 4\pi\varepsilon_0\frac{R_1 R_2}{R_2 - R_1}$$

Due limiti sono particolarmente significativi. Se $R_2 \to \infty$, l'armatura esterna si allontana all'infinito e si ottiene $C \to 4\pi\varepsilon_0 R_1$, cioè la capacità della sfera isolata discussa sopra: il conduttore isolato è dunque un condensatore la cui seconda armatura è "all'infinito". Se invece $R_2 - R_1 = d \ll R_1$, si ha $R_1 R_2 \simeq R_1^2$ e $C \simeq 4\pi\varepsilon_0 R_1^2/d = \varepsilon_0 S/d$, con $S = 4\pi R_1^2$: ancora una volta ritroviamo il condensatore piano. Questa convergenza dei tre risultati nel limite di armature vicine non è casuale: esprime il fatto che in ogni condensatore con armature molto ravvicinate il campo è localmente uniforme e la capacità è determinata dal rapporto fra area e distanza.

Il confronto fra le tre geometrie mette in luce un aspetto generale: la capacità è sempre il prodotto di $\varepsilon_0$ per una **lunghezza caratteristica** della geometria ($S/d$ nel caso piano, $2\pi L/\ln(R_2/R_1)$ nel caso cilindrico, $4\pi R_1R_2/(R_2-R_1)$ nel caso sferico). Questa osservazione dimensionale è utile per controllare la correttezza dei calcoli: qualsiasi espressione della capacità nel vuoto deve avere la forma $\varepsilon_0 \times$ [metri].

### Esercizio d'esempio

Un cavo coassiale ha conduttore interno di raggio $R_1 = 0.50$ mm e schermo esterno di raggio $R_2 = 2.0$ mm; lo spazio intermedio è in aria (assimilabile al vuoto). Il cavo è lungo $L = 10$ m ed è sottoposto a una differenza di potenziale $\Delta V = 200$ V. Calcolare: (a) la capacità per unità di lunghezza e la capacità totale; (b) la carica sulle armature; (c) il campo elettrico massimo fra le armature.

**Soluzione.** (a) Il rapporto fra i raggi è $R_2/R_1 = 4.0$, e $\ln 4 = 1.386$. La capacità per unità di lunghezza vale

$$\frac{C}{L} = \frac{2\pi\varepsilon_0}{\ln(R_2/R_1)} = \frac{2\pi \cdot 8.854\times10^{-12}\ \text{F/m}}{1.386} = 4.01\times10^{-11}\ \text{F/m} \simeq 40\ \text{pF/m}$$

La capacità totale è $C = 40.1\ \text{pF/m} \times 10\ \text{m} = 4.01\times10^{-10}\ \text{F} \simeq 0.40$ nF.

(b) La carica vale $Q = C\,\Delta V = 4.01\times10^{-10}\ \text{F}\times 200\ \text{V} = 8.0\times10^{-8}$ C, cioè 80 nC; la densità lineare è $\lambda = Q/L = 8.0\times10^{-9}$ C/m.

(c) Il campo è massimo sulla superficie del conduttore interno, $r = R_1$:

$$E_{max} = \frac{\lambda}{2\pi\varepsilon_0 R_1} = \frac{\Delta V}{R_1 \ln(R_2/R_1)} = \frac{200\ \text{V}}{5.0\times10^{-4}\ \text{m}\times 1.386} = 2.9\times10^{5}\ \text{V/m}$$

Il valore è circa un decimo della rigidità dielettrica dell'aria secca ($\approx 3\times10^6$ V/m): il cavo lavora in sicurezza. Si osservi che l'espressione $E_{max} = \Delta V/[R_1\ln(R_2/R_1)]$ mostra come, a parità di tensione, il campo massimo dipenda in modo cruciale dal raggio del conduttore interno.

### Punti chiave

- La capacità $C = Q/\Delta V$ è una proprietà geometrica del sistema di conduttori e del mezzo interposto; non dipende da $Q$ né da $\Delta V$ grazie alla linearità dell'elettrostatica.
- Il metodo di calcolo è sempre: ipotizzare $\pm Q$, trovare $\vec{E}$ con Gauss, integrare per ottenere $\Delta V$, fare il rapporto.
- Condensatore piano: $C = \varepsilon_0 S/d$, valido trascurando gli effetti di bordo ($d \ll \sqrt{S}$); il campo interno è uniforme.
- Condensatore cilindrico: $C = 2\pi\varepsilon_0 L/\ln(R_2/R_1)$; il campo decresce come $1/r$ ed è massimo sull'armatura interna.
- Condensatore sferico: $C = 4\pi\varepsilon_0 R_1R_2/(R_2-R_1)$; per $R_2\to\infty$ si ottiene la sfera isolata $C = 4\pi\varepsilon_0 R$.
- Nel limite di armature molto vicine tutte le geometrie si riducono al condensatore piano.
- Il farad è un'unità molto grande: le capacità tipiche sono dell'ordine dei pF–µF.

## 18.2 Energia elettrostatica

Caricare un condensatore richiede lavoro. Quando si trasferisce carica da un'armatura all'altra, la carica già presente si oppone all'arrivo di nuova carica dello stesso segno, e occorre un agente esterno (tipicamente un generatore) che compia lavoro contro le forze elettriche. Questo lavoro non va perduto: resta immagazzinato nel sistema sotto forma di **energia potenziale elettrostatica** e può essere restituito in seguito, ad esempio quando il condensatore si scarica attraverso un circuito. È proprio questa capacità di accumulare energia e di rilasciarla rapidamente che rende i condensatori indispensabili in moltissime applicazioni: il flash delle fotocamere, i defibrillatori cardiaci, i circuiti di filtraggio degli alimentatori, i sistemi di recupero dell'energia in frenata dei veicoli elettrici. In questa sezione calcoleremo l'energia accumulata in un condensatore, mostreremo che essa può essere interpretata come energia distribuita nel campo elettrico e la useremo per ricavare la forza fra le armature.

### 18.2.1 Lavoro di carica ed energia del condensatore

Consideriamo un condensatore di capacità $C$ inizialmente scarico e immaginiamo di caricarlo trasportando, una dopo l'altra, piccole quantità di carica $dq$ dall'armatura negativa a quella positiva. In un istante intermedio del processo le armature portano le cariche $\pm q$ e fra esse c'è la differenza di potenziale $v = q/C$. Per spostare la carica $dq$ attraverso questa differenza di potenziale, in condizioni quasi statiche (cioè senza variazioni di energia cinetica), l'agente esterno deve compiere il lavoro

$$dW = v\,dq = \frac{q}{C}\,dq$$

Si noti che il lavoro elementare cresce man mano che la carica aumenta: le prime cariche si spostano "gratis", perché il condensatore è scarico, mentre le ultime devono vincere una differenza di potenziale prossima a quella finale. Integrando da $q = 0$ a $q = Q$:

$$U_e = W = \int_0^Q \frac{q}{C}\,dq = \frac{Q^2}{2C}$$

Usando la relazione $Q = C\,\Delta V$, l'energia si può scrivere in tre forme equivalenti:

$$U_e = \frac{Q^2}{2C} = \frac{1}{2}Q\,\Delta V = \frac{1}{2}C\,\Delta V^2$$

Il fattore $1/2$ ha un significato preciso e merita attenzione: l'energia immagazzinata non è $Q\,\Delta V$, come si avrebbe spostando tutta la carica attraverso la differenza di potenziale finale, ma la metà, perché la differenza di potenziale cresce linearmente durante la carica e il suo valor medio è $\Delta V/2$. In un diagramma $v$–$q$ l'energia è l'area del triangolo sotto la retta $v = q/C$.

La scelta della forma più conveniente dipende dalle condizioni del problema. Se il condensatore è **isolato**, cioè scollegato dal generatore, la carica resta costante e conviene usare $Q^2/(2C)$. Se invece il condensatore è **collegato a un generatore** che mantiene costante la tensione, conviene usare $\frac{1}{2}C\Delta V^2$. Questa distinzione diventa cruciale quando si modifica la geometria del condensatore (ad esempio allontanando le armature) e si vuole capire come varia l'energia, come vedremo fra poco.

È importante anche riflettere sul bilancio energetico complessivo quando un condensatore viene caricato da un generatore ideale di forza elettromotrice $\mathcal{E}$. Il generatore sposta la carica totale $Q = C\mathcal{E}$ attraverso una differenza di potenziale costante $\mathcal{E}$, erogando l'energia $Q\mathcal{E} = C\mathcal{E}^2$. Di questa, solo la metà, $\frac{1}{2}C\mathcal{E}^2$, si ritrova immagazzinata nel condensatore. L'altra metà viene dissipata per effetto Joule nelle resistenze del circuito (o irraggiata, se la resistenza è trascurabile), indipendentemente dal valore della resistenza: è un risultato sorprendente che verrà ripreso nello studio dei circuiti RC.

### 18.2.2 Densità di energia del campo elettrico

Dove si trova l'energia immagazzinata? Una risposta possibile è che essa sia associata alle cariche e alla loro configurazione; una risposta alternativa, più profonda e destinata a rivelarsi la più feconda, è che l'energia sia **localizzata nel campo elettrico**, distribuita nello spazio in cui il campo è diverso da zero. Il condensatore piano permette di rendere quantitativa questa idea in modo semplicissimo. Il campo fra le armature è uniforme e vale $E = \Delta V/d$, ed è nullo all'esterno. Scriviamo l'energia in funzione del campo:

$$U_e = \frac{1}{2}C\,\Delta V^2 = \frac{1}{2}\frac{\varepsilon_0 S}{d}(E d)^2 = \frac{1}{2}\varepsilon_0 E^2\,(S d)$$

Il prodotto $S d$ è proprio il volume $\tau$ della regione occupata dal campo. Si definisce quindi la **densità di energia elettrostatica**

$$u_e = \frac{U_e}{\tau} = \frac{1}{2}\varepsilon_0 E^2$$

misurata in J/m$^3$. Benché ricavata per il caso particolare di un campo uniforme, questa espressione ha validità generale: in qualunque configurazione di campo elettrostatico nel vuoto l'energia totale si ottiene integrando la densità su tutto lo spazio,

$$U_e = \int_{\tau} \frac{1}{2}\varepsilon_0 E^2\,d\tau$$

Possiamo verificarlo sul condensatore sferico. Il campo fra le armature vale $E = Q/(4\pi\varepsilon_0 r^2)$; prendendo come elemento di volume un guscio sferico $d\tau = 4\pi r^2 dr$ si ha

$$U_e = \int_{R_1}^{R_2}\frac{1}{2}\varepsilon_0\frac{Q^2}{16\pi^2\varepsilon_0^2 r^4}\,4\pi r^2\,dr = \frac{Q^2}{8\pi\varepsilon_0}\left(\frac{1}{R_1}-\frac{1}{R_2}\right)$$

che coincide esattamente con $Q^2/(2C)$ usando la capacità del condensatore sferico. La coincidenza dei due calcoli non è una curiosità: dimostra che i due punti di vista (energia delle cariche ed energia del campo) sono equivalenti in elettrostatica. Tuttavia, quando si studieranno le onde elettromagnetiche, si vedrà che il campo può trasportare energia anche in assenza di cariche, e allora la localizzazione dell'energia nel campo diventerà l'unica interpretazione sostenibile.

Un ordine di grandezza è utile: in aria il campo non può superare circa $3\times10^6$ V/m senza provocare una scarica, per cui la densità di energia massima vale $u_e \approx \frac{1}{2}\cdot 8.85\times10^{-12}\cdot (3\times10^6)^2 \approx 40$ J/m$^3$. È un valore modesto se confrontato, ad esempio, con la densità di energia chimica di una batteria (dell'ordine di $10^9$ J/m$^3$): per questo i condensatori sono ottimi per erogare energia rapidamente, ma non per immagazzinarne grandi quantità. L'uso di dielettrici con elevata costante dielettrica e alta rigidità migliora enormemente queste prestazioni, come si vedrà nel capitolo successivo.

### 18.2.3 Forza fra le armature

L'espressione dell'energia consente di calcolare la forza con cui le armature si attraggono, tramite il **metodo dei lavori virtuali**. Consideriamo un condensatore piano isolato, con carica $Q$ costante, e immaginiamo di allontanare l'armatura mobile di un tratto infinitesimo $dx$. Poiché il sistema è isolato, il lavoro compiuto dalla forza elettrica è uguale alla diminuzione di energia potenziale: $F_x\,dx = -dU_e$. Con $U_e = Q^2/(2C) = Q^2 x/(2\varepsilon_0 S)$, dove $x$ è la distanza fra le armature:

$$F_x = -\left(\frac{\partial U_e}{\partial x}\right)_Q = -\frac{Q^2}{2\varepsilon_0 S}$$

Il segno negativo indica che la forza tende a ridurre $x$: le armature si attraggono, come è ovvio dato che portano cariche opposte. Il modulo si può riscrivere come $F = \frac{1}{2}\varepsilon_0 E^2 S$, cioè la forza per unità di area (la **pressione elettrostatica**) è uguale alla densità di energia $u_e$. Si noti che il risultato non è $\sigma E$, come ingenuamente ci si aspetterebbe, ma $\sigma E/2$: la carica di un'armatura risente soltanto del campo prodotto dall'altra armatura, che è la metà del campo totale.

Se invece il condensatore è mantenuto a **tensione costante** da un generatore, il bilancio deve includere il lavoro del generatore: allontanando le armature la capacità diminuisce, la carica diminuisce e il generatore riassorbe carica. Si dimostra che in questo caso $F_x = +(\partial U_e/\partial x)_{\Delta V}$, e il risultato numerico della forza è, come deve essere, lo stesso, dato che la forza in un certo istante dipende solo dalla configurazione delle cariche e non da ciò che accade dopo. Su questo principio funzionano l'**elettrometro assoluto** a bilancia, che misura una tensione pesando la forza fra le armature, e molti microattuatori elettrostatici dei dispositivi MEMS.

### Esercizio d'esempio

Un condensatore piano nel vuoto ha armature di area $S = 0.020$ m$^2$ poste a distanza $d = 1.0$ mm ed è collegato a un generatore che fornisce $\Delta V = 500$ V. Calcolare: (a) l'energia immagazzinata e la densità di energia; (b) la forza fra le armature. (c) Il condensatore viene poi staccato dal generatore e le armature vengono allontanate fino a $d' = 3.0$ mm: calcolare la nuova energia e il lavoro compiuto dall'operatore.

**Soluzione.** (a) La capacità è $C = \varepsilon_0 S/d = 8.854\times10^{-12}\times 0.020/1.0\times10^{-3} = 1.77\times10^{-10}$ F. L'energia vale

$$U_e = \tfrac{1}{2}C\Delta V^2 = \tfrac{1}{2}\times 1.77\times10^{-10}\ \text{F}\times(500\ \text{V})^2 = 2.21\times10^{-5}\ \text{J}$$

Il campo è $E = \Delta V/d = 5.0\times10^5$ V/m e la densità di energia $u_e = \frac{1}{2}\varepsilon_0E^2 = 1.11$ J/m$^3$. Controllo: $u_e\cdot S d = 1.11\times 2.0\times10^{-5} = 2.21\times10^{-5}$ J, in accordo.

(b) $F = \frac{1}{2}\varepsilon_0E^2 S = u_e S = 1.11\ \text{J/m}^3\times0.020\ \text{m}^2 = 2.2\times10^{-2}$ N, attrattiva.

(c) Staccato il generatore, la carica resta $Q = C\Delta V = 8.85\times10^{-8}$ C. La nuova capacità è $C' = C/3 = 5.90\times10^{-11}$ F e la nuova energia $U_e' = Q^2/(2C') = 3U_e = 6.64\times10^{-5}$ J. Il lavoro compiuto dall'operatore, che deve vincere la forza attrattiva (costante, perché a carica costante il campo non cambia), è $W = U_e' - U_e = 4.43\times10^{-5}$ J, che coincide con $F\,(d'-d) = 2.2\times10^{-2}\ \text{N}\times2.0\times10^{-3}\ \text{m}$. La tensione sale a $\Delta V' = Q/C' = 1500$ V.

### Punti chiave

- L'energia di un condensatore carico è $U_e = Q^2/(2C) = \frac{1}{2}Q\Delta V = \frac{1}{2}C\Delta V^2$; il fattore $1/2$ deriva dalla crescita lineare della tensione durante la carica.
- A carica costante (condensatore isolato) conviene $Q^2/2C$; a tensione costante (collegato al generatore) conviene $\frac{1}{2}C\Delta V^2$.
- Caricando un condensatore con un generatore ideale, metà dell'energia erogata viene dissipata, indipendentemente dalla resistenza del circuito.
- L'energia è localizzata nel campo con densità $u_e = \frac{1}{2}\varepsilon_0E^2$; l'energia totale è l'integrale di $u_e$ sul volume.
- La forza fra le armature di un condensatore piano vale $F = \frac{1}{2}\varepsilon_0E^2S$: la pressione elettrostatica coincide con la densità di energia.
- Il metodo dei lavori virtuali permette di ricavare le forze dalla derivata dell'energia rispetto a uno spostamento, con attenzione al vincolo ($Q$ o $\Delta V$ costante).

## 18.3 Serie e parallelo

Nei circuiti reali i condensatori raramente compaiono da soli: più spesso sono collegati fra loro per ottenere un valore di capacità non disponibile commercialmente, per suddividere una tensione elevata su più componenti o per aumentare la quantità di carica immagazzinabile. Due configurazioni elementari, il collegamento in **serie** e il collegamento in **parallelo**, permettono di analizzare la maggior parte delle reti di condensatori; nei casi più complessi esse vanno combinate passo dopo passo. In entrambi i casi l'obiettivo è trovare la **capacità equivalente** $C_{eq}$, cioè la capacità di un unico condensatore che, sottoposto alla stessa differenza di potenziale totale, accumulerebbe la stessa carica totale fornita dal generatore. Il concetto di equivalenza è centrale: il generatore "vede" la rete solo attraverso i due morsetti a cui è collegato, e non può distinguere la rete dal suo equivalente.

Prima di procedere conviene precisare due principi fisici che stanno alla base dell'analisi. Il primo è la **conservazione della carica**: in un tratto di conduttore isolato dal resto del circuito (ad esempio il filo che collega due armature di condensatori diversi, senza alcun altro collegamento) la carica totale resta quella iniziale, tipicamente zero. Il secondo è il carattere **conservativo** del campo elettrostatico: la differenza di potenziale fra due punti non dipende dal percorso, e quindi in una maglia chiusa la somma delle differenze di potenziale è nulla. Inoltre, i fili di collegamento sono conduttori in equilibrio e quindi ciascun filo, insieme alle armature che collega, costituisce un'unica regione equipotenziale.

### 18.3.1 Condensatori in serie

Due o più condensatori si dicono collegati in **serie** quando sono disposti uno dopo l'altro lungo un unico percorso, in modo che l'armatura negativa del primo sia collegata all'armatura positiva del secondo, e così via, e il generatore sia collegato fra l'armatura positiva del primo e quella negativa dell'ultimo. Il punto essenziale è che i nodi intermedi non hanno altri collegamenti.

Analizziamo cosa accade quando si applica la differenza di potenziale $\Delta V$. Il generatore porta la carica $+Q$ sull'armatura sinistra del primo condensatore e $-Q$ sull'armatura destra dell'ultimo. Per induzione completa, sull'armatura destra del primo condensatore compare la carica $-Q$. Ma questa armatura è collegata, tramite un filo isolato dal resto, all'armatura sinistra del secondo condensatore, e l'insieme era inizialmente neutro: per la conservazione della carica sull'armatura sinistra del secondo condensatore deve comparire $+Q$. Ripetendo il ragionamento lungo la catena si conclude che **tutti i condensatori in serie portano la stessa carica** $Q$, qualunque sia la loro capacità.

Le differenze di potenziale ai capi dei singoli condensatori sono invece diverse, $\Delta V_k = Q/C_k$, e la loro somma deve uguagliare la tensione totale:

$$\Delta V = \sum_k \Delta V_k = Q\sum_k\frac{1}{C_k}$$

Confrontando con la definizione $\Delta V = Q/C_{eq}$ si trova

$$\frac{1}{C_{eq}} = \sum_k\frac{1}{C_k}$$

Nel caso di due condensatori: $C_{eq} = C_1C_2/(C_1+C_2)$. La capacità equivalente della serie è **sempre minore** della più piccola delle capacità collegate. Un'interpretazione intuitiva si ottiene pensando a due condensatori piani identici in serie: è come se si avesse un unico condensatore con la stessa area e distanza doppia fra le armature (le armature intermedie, collegate fra loro, sono come una lastra conduttrice sottile interposta, che non altera il campo), e quindi capacità dimezzata.

Una conseguenza pratica importante riguarda la **ripartizione della tensione**: poiché $\Delta V_k = Q/C_k$, la tensione si distribuisce in proporzione inversa alle capacità, e il condensatore con capacità minore sopporta la tensione maggiore. Per due condensatori, $\Delta V_1 = \Delta V\,C_2/(C_1+C_2)$: è il **partitore capacitivo**, usato ad esempio nelle sonde per alte tensioni. Il collegamento in serie si usa quando la tensione da applicare supera quella massima sopportabile da un singolo condensatore; bisogna però fare attenzione che nessuno dei componenti superi la propria tensione di lavoro, il che richiede di verificare i singoli $\Delta V_k$.

Anche l'energia si ripartisce secondo la stessa logica: $U_k = Q^2/(2C_k)$, quindi nella serie è il condensatore più piccolo a immagazzinare la maggior parte dell'energia. L'energia totale è la somma delle energie dei singoli condensatori e coincide con $Q^2/(2C_{eq})$, come deve essere.

### 18.3.2 Condensatori in parallelo

Due o più condensatori si dicono collegati in **parallelo** quando tutte le loro armature "positive" sono collegate a uno stesso nodo e tutte le armature "negative" a un altro nodo; il generatore è collegato fra questi due nodi. Poiché ciascun nodo, con le armature e i fili che lo compongono, è un unico conduttore equipotenziale, **tutti i condensatori in parallelo sono sottoposti alla stessa differenza di potenziale** $\Delta V$.

Le cariche sui singoli condensatori sono invece diverse, $Q_k = C_k\,\Delta V$, e la carica totale fornita dal generatore è la loro somma:

$$Q = \sum_k Q_k = \Delta V\sum_k C_k$$

Dalla definizione $Q = C_{eq}\,\Delta V$ si ottiene

$$C_{eq} = \sum_k C_k$$

La capacità equivalente del parallelo è la **somma** delle capacità ed è quindi sempre maggiore della più grande di esse. L'interpretazione geometrica è immediata: due condensatori piani affiancati, con la stessa distanza fra le armature, equivalgono a un unico condensatore con area pari alla somma delle aree. La carica si ripartisce in proporzione diretta alle capacità, e così l'energia, $U_k = \frac{1}{2}C_k\Delta V^2$.

Il collegamento in parallelo si usa per aumentare la capacità complessiva e quindi la carica e l'energia immagazzinabili a una data tensione: i banchi di condensatori dei laboratori di alta potenza, così come i "pacchi" di supercondensatori nei veicoli, sono formati da numerosi elementi in parallelo (spesso combinati con stringhe in serie per raggiungere la tensione desiderata).

### 18.3.3 Reti miste e ridistribuzione della carica

Le reti più complesse si analizzano riconoscendo progressivamente sottogruppi in serie o in parallelo e sostituendoli con il loro equivalente, fino a ridurre la rete a un unico condensatore. Bisogna però fare attenzione: due condensatori sono in serie solo se il nodo comune non ha altre connessioni, e sono in parallelo solo se condividono entrambi i nodi. Alcune reti (ad esempio a ponte) non sono riducibili con queste sole regole e richiedono di scrivere esplicitamente le equazioni di conservazione della carica sui nodi isolati e di somma nulla delle tensioni sulle maglie.

Un caso istruttivo è la **ridistribuzione della carica** fra due condensatori: un condensatore $C_1$ caricato alla tensione $V_0$ viene staccato dal generatore e collegato in parallelo a un condensatore scarico $C_2$. La carica totale $Q_0 = C_1V_0$ si conserva e si ripartisce fino a che entrambi raggiungono la stessa tensione finale $V_f = C_1V_0/(C_1+C_2)$. L'energia finale, $\frac{1}{2}(C_1+C_2)V_f^2 = \frac{1}{2}C_1V_0^2\cdot C_1/(C_1+C_2)$, è minore di quella iniziale: la differenza viene dissipata per effetto Joule nei fili durante il transitorio o irraggiata come onda elettromagnetica. Anche qui, come nella carica da generatore, la perdita non dipende dalla resistenza dei collegamenti.

### Esercizio d'esempio

Tre condensatori $C_1 = 2.0\ \mu$F, $C_2 = 3.0\ \mu$F e $C_3 = 6.0\ \mu$F sono collegati come segue: $C_2$ e $C_3$ in serie fra loro, e questo ramo in parallelo con $C_1$. Ai capi della rete si applica $\Delta V = 12$ V. Calcolare la capacità equivalente, la carica e la tensione di ciascun condensatore e l'energia totale.

**Soluzione.** La serie $C_2$–$C_3$ ha capacità $C_{23} = C_2C_3/(C_2+C_3) = (3.0\times6.0)/(9.0)\ \mu\text{F} = 2.0\ \mu$F. Il parallelo con $C_1$ dà

$$C_{eq} = C_1 + C_{23} = 2.0 + 2.0 = 4.0\ \mu\text{F}$$

Il condensatore $C_1$ ha la tensione piena: $\Delta V_1 = 12$ V, $Q_1 = C_1\Delta V_1 = 24\ \mu$C. Anche il ramo serie è sottoposto a 12 V e porta la carica $Q_{23} = C_{23}\cdot 12\ \text{V} = 24\ \mu$C, uguale su $C_2$ e $C_3$. Le tensioni sono $\Delta V_2 = Q_{23}/C_2 = 8.0$ V e $\Delta V_3 = Q_{23}/C_3 = 4.0$ V; la loro somma è 12 V, come previsto, e la tensione maggiore spetta al condensatore più piccolo. La carica totale fornita dal generatore è $Q = Q_1 + Q_{23} = 48\ \mu$C $= C_{eq}\Delta V$. L'energia totale è $U = \frac{1}{2}C_{eq}\Delta V^2 = \frac{1}{2}\times4.0\times10^{-6}\times144 = 2.88\times10^{-4}$ J; controllo: $U_1 = 144\ \mu$J, $U_2 = \frac{1}{2}\cdot3\cdot64 = 96\ \mu$J, $U_3 = \frac{1}{2}\cdot6\cdot16 = 48\ \mu$J, somma 288 $\mu$J.

### Punti chiave

- In serie tutti i condensatori hanno la stessa carica (conservazione della carica sui nodi isolati); le tensioni si sommano: $1/C_{eq} = \sum 1/C_k$.
- In parallelo tutti i condensatori hanno la stessa tensione (nodi equipotenziali); le cariche si sommano: $C_{eq} = \sum C_k$.
- In serie la capacità equivalente è minore della più piccola; in parallelo è maggiore della più grande.
- In serie la tensione si ripartisce in modo inversamente proporzionale alle capacità (partitore capacitivo).
- Le reti miste si riducono passo dopo passo; le reti non riducibili si risolvono con conservazione della carica e somma nulla delle tensioni nelle maglie.
- Nella ridistribuzione di carica fra condensatori l'energia elettrostatica diminuisce: la differenza è dissipata nel transitorio.

## 18.4 Mutua capacità

Fino a questo punto abbiamo considerato condensatori ideali, nei quali l'induzione fra le armature è completa e il sistema può essere descritto da un unico numero, la capacità. Nella realtà, però, ogni conduttore interagisce elettrostaticamente con tutti gli altri conduttori presenti: le piste di un circuito stampato, i fili di un cavo multipolare, le armature di un condensatore e la carcassa metallica dello strumento che lo contiene, perfino il corpo dell'operatore che si avvicina a un circuito sensibile. Per descrivere queste situazioni occorre un formalismo più generale, quello dei **coefficienti di potenziale** e dei **coefficienti di capacità**, dal quale emerge il concetto di **mutua capacità** fra due conduttori. Il condensatore ideale apparirà allora come un caso particolare, e capiremo con precisione in che senso un conduttore cavo funziona da schermo elettrostatico.

### 18.4.1 Coefficienti di potenziale e di capacità

Consideriamo un sistema di $N$ conduttori, numerati da 1 a $N$, isolati fra loro e immersi nel vuoto; il riferimento di potenziale nullo è posto all'infinito (oppure, equivalentemente, su un conduttore di riferimento molto esteso chiamato "massa" o "terra"). Ciascun conduttore $j$ porti la carica $Q_j$ e si trovi al potenziale $V_i$. Il problema elettrostatico consiste nel determinare i potenziali noti le cariche, o viceversa.

La chiave è ancora una volta la **linearità** delle equazioni dell'elettrostatica. Supponiamo che soltanto il conduttore $j$ sia carico, con carica unitaria, e che tutti gli altri siano scarichi: in questa configurazione il conduttore $i$ assume un certo potenziale, che indichiamo con $p_{ij}$. Per il principio di sovrapposizione, la configurazione generale con cariche $Q_1,\dots,Q_N$ è la somma delle configurazioni elementari, e quindi

$$V_i = \sum_{j=1}^{N} p_{ij}\,Q_j$$

I numeri $p_{ij}$ si chiamano **coefficienti di potenziale**, si misurano in F$^{-1}$ e dipendono soltanto dalla geometria del sistema (forma, dimensioni e posizione relativa dei conduttori). Il sistema lineare si può invertire, ottenendo le cariche in funzione dei potenziali:

$$Q_i = \sum_{j=1}^{N} c_{ij}\,V_j$$

dove la matrice dei **coefficienti di capacità** $c_{ij}$ è l'inversa della matrice dei $p_{ij}$. Il coefficiente $c_{ij}$ ha un significato operativo molto chiaro: è la carica che compare sul conduttore $i$ quando il conduttore $j$ è portato al potenziale di 1 V e tutti gli altri conduttori (compreso $i$, se $i\neq j$) sono collegati a terra, cioè mantenuti a potenziale nullo. I coefficienti diagonali $c_{ii}$ sono talvolta chiamati coefficienti di capacità propriamente detti, mentre quelli fuori diagonale, $c_{ij}$ con $i\neq j$, sono detti **coefficienti di induzione**.

Questi coefficienti godono di alcune proprietà generali, che si possono dedurre da semplici considerazioni fisiche. In primo luogo $c_{ii} > 0$: se il conduttore $i$ è portato a potenziale positivo e tutti gli altri sono a terra, la carica su $i$ è necessariamente positiva, perché le linee di campo partono da $i$ verso conduttori a potenziale più basso. In secondo luogo $c_{ij} \le 0$ per $i \neq j$: il conduttore $j$, portato a potenziale positivo, induce su ogni altro conduttore a terra una carica negativa (o nulla, se il conduttore è schermato). In terzo luogo, la somma $\sum_j c_{ij} \ge 0$: poiché ogni linea di campo che parte dal conduttore $i$ può terminare o su un altro conduttore o all'infinito, la carica indotta complessivamente sugli altri conduttori non può superare in modulo la carica inducente.

### 18.4.2 Reciprocità e definizione di mutua capacità

La proprietà più notevole e meno intuitiva dei coefficienti è la **simmetria**: $p_{ij} = p_{ji}$ e quindi $c_{ij} = c_{ji}$. Questo è il **teorema di reciprocità** (dovuto a Green): il potenziale che una carica unitaria posta sul conduttore $j$ produce sul conduttore $i$ è uguale al potenziale che la stessa carica posta su $i$ produce su $j$, anche se i due conduttori hanno forme e dimensioni completamente diverse.

La dimostrazione più elegante sfrutta l'energia. L'energia elettrostatica di un sistema di conduttori vale $U_e = \frac{1}{2}\sum_i Q_iV_i = \frac{1}{2}\sum_{i,j}p_{ij}Q_iQ_j$, e non può dipendere dall'ordine con cui le cariche vengono portate sui conduttori, dato che il campo è conservativo. Si carichi dapprima il conduttore $i$ fino a $Q_i$, con lavoro $\frac{1}{2}p_{ii}Q_i^2$, e poi il conduttore $j$ fino a $Q_j$: durante questa seconda fase, ogni carica $dq$ aggiunta a $j$ deve vincere il potenziale $p_{ji}Q_i + p_{jj}q$, e il lavoro totale contiene il termine misto $p_{ji}Q_iQ_j$. Invertendo l'ordine si ottiene il termine misto $p_{ij}Q_iQ_j$. Poiché lo stato finale è lo stesso, i due lavori devono coincidere e quindi $p_{ij} = p_{ji}$.

Si definisce allora la **mutua capacità** fra i conduttori $i$ e $j$ come

$$C_{ij} = -c_{ij} \ge 0, \qquad i\neq j$$

e la **capacità verso massa** (o verso terra) del conduttore $i$ come $C_{i0} = \sum_j c_{ij}$. Con queste definizioni la relazione fra cariche e potenziali si riscrive in una forma molto espressiva:

$$Q_i = C_{i0}\,V_i + \sum_{j\neq i} C_{ij}\,(V_i - V_j)$$

La carica di ogni conduttore è la somma di un termine dovuto alla sua capacità verso massa, proporzionale al suo potenziale, e di termini dovuti alle mutue capacità, proporzionali alle differenze di potenziale rispetto agli altri conduttori. Questa scrittura corrisponde a un **circuito equivalente**: ogni coppia di conduttori è collegata da un condensatore di capacità $C_{ij}$ e ogni conduttore è collegato a massa da un condensatore di capacità $C_{i0}$. Un sistema di conduttori arbitrari diventa così una rete di condensatori ordinari, analizzabile con le regole di serie e parallelo della sezione precedente. È questo il modello che gli ingegneri elettronici usano per descrivere le **capacità parassite**.

### 18.4.3 Il condensatore come caso particolare e la schermatura elettrostatica

Applichiamo il formalismo a due conduttori. Le relazioni sono $Q_1 = c_{11}V_1 + c_{12}V_2$ e $Q_2 = c_{12}V_1 + c_{22}V_2$. Se fra i due conduttori c'è **induzione completa**, per qualunque valore dei potenziali deve valere $Q_1 = -Q_2$, il che impone $c_{11} = -c_{12} = c_{22} \equiv C$; le capacità verso massa sono nulle e si ritrova $Q_1 = C(V_1 - V_2)$: il condensatore ideale è un sistema di due conduttori con sola mutua capacità. Quando invece l'induzione non è completa, le capacità verso massa sono diverse da zero; se i due conduttori portano cariche $\pm Q$, la differenza di potenziale vale $V_1 - V_2 = (p_{11} + p_{22} - 2p_{12})Q$, e la capacità "efficace" del sistema è $C = 1/(p_{11}+p_{22}-2p_{12})$, che dipende in generale anche dalla presenza degli altri corpi.

Il caso dei due gusci sferici concentrici è illuminante. Sia 1 una sfera di raggio $R_1$ e 2 un guscio sottile di raggio $R_2$ che la racchiude. Con cariche $Q_1$ e $Q_2$, la superficie interna del guscio porta $-Q_1$ e quella esterna $Q_1+Q_2$; i potenziali sono

$$V_2 = \frac{Q_1+Q_2}{4\pi\varepsilon_0R_2}, \qquad V_1 = \frac{Q_1}{4\pi\varepsilon_0R_1} + \frac{Q_2}{4\pi\varepsilon_0R_2}$$

da cui si leggono $p_{11} = 1/(4\pi\varepsilon_0R_1)$, $p_{12} = p_{21} = p_{22} = 1/(4\pi\varepsilon_0R_2)$: la reciprocità è verificata. Invertendo si trova $c_{11} = -c_{12} = C_s$, con $C_s = 4\pi\varepsilon_0R_1R_2/(R_2-R_1)$ la capacità del condensatore sferico, e $c_{22} = C_s + 4\pi\varepsilon_0R_2$. Quindi la mutua capacità è $C_{12} = C_s$, la capacità verso massa della sfera interna è $C_{10} = 0$ e quella del guscio esterno è $C_{20} = 4\pi\varepsilon_0R_2$. Il risultato $C_{10} = 0$ esprime in termini quantitativi lo **schermo elettrostatico**: un conduttore completamente racchiuso in una cavità di un altro conduttore non ha alcuna interazione capacitiva con l'esterno, e la sua carica dipende soltanto dalla differenza di potenziale rispetto al guscio che lo circonda. Qualunque cosa accada fuori dal guscio, compresa la variazione del potenziale del guscio stesso, la situazione interna non cambia se non per una costante additiva. È il principio della **gabbia di Faraday** e dei cavi schermati: collegando lo schermo a massa se ne fissa anche il potenziale, e il conduttore interno risulta perfettamente isolato dai disturbi elettrostatici esterni.

### 18.4.4 Capacità parassite e accoppiamenti

Le mutue capacità non volute fra conduttori vicini sono dette **capacità parassite** e sono una delle principali fonti di disturbo nei circuiti elettronici. Due piste parallele di un circuito stampato, lunghe pochi centimetri e distanti qualche decimo di millimetro, hanno mutua capacità dell'ordine del picofarad: sembra poco, ma ai segnali rapidi (frequenze di centinaia di megahertz) questa capacità offre un percorso di accoppiamento efficace, e un segnale su una pista induce un disturbo sull'altra (fenomeno detto **diafonia** o *crosstalk*). La progettazione dei circuiti ad alta velocità consiste in buona parte nel controllare queste capacità: distanziando le piste, interponendo piste collegate a massa che "assorbono" le linee di campo (riducendo la mutua capacità a vantaggio delle capacità verso massa), usando cavi schermati e piani di massa.

Il concetto di mutua capacità ha però anche applicazioni positive di grande rilevanza. I **sensori capacitivi** degli schermi tattili dei telefoni misurano proprio la variazione della mutua capacità fra elettrodi incrociati quando un dito, che è un conduttore collegato a massa attraverso il corpo, si avvicina e devia verso di sé parte delle linee di campo. Analogamente funzionano i sensori di prossimità, i misuratori di livello dei liquidi e i trasduttori di spostamento capacitivi impiegati in metrologia, capaci di risolvere variazioni di posizione dell'ordine del nanometro.

Infine il formalismo dei coefficienti consente di scrivere in forma compatta l'energia di un sistema di conduttori:

$$U_e = \frac{1}{2}\sum_i Q_iV_i = \frac{1}{2}\sum_{i,j}c_{ij}V_iV_j = \frac{1}{2}\sum_i C_{i0}V_i^2 + \frac{1}{2}\sum_{i<j}C_{ij}(V_i-V_j)^2$$

L'ultima scrittura mostra che l'energia del sistema è esattamente quella della rete di condensatori equivalente: ogni capacità verso massa e ogni mutua capacità contribuisce con il termine $\frac{1}{2}C\,\Delta V^2$ calcolato con la tensione ai propri capi. Poiché l'energia elettrostatica deve essere positiva per qualunque scelta dei potenziali non tutti nulli, la matrice $c_{ij}$ è definita positiva, il che implica in particolare $c_{ii} > 0$ e $c_{ii}c_{jj} > c_{ij}^2$.

### Esercizio d'esempio

Una sfera conduttrice di raggio $R_1 = 5.0$ cm è posta al centro di un guscio sferico conduttore sottile di raggio $R_2 = 10$ cm. (a) Determinare la mutua capacità e le capacità verso massa. (b) Calcolare le cariche sui due conduttori quando $V_1 = 1000$ V e $V_2 = 0$, e quando $V_1 = V_2 = 1000$ V. (c) Calcolare l'energia nel primo caso.

**Soluzione.** (a) La mutua capacità coincide con la capacità del condensatore sferico:

$$C_{12} = 4\pi\varepsilon_0\frac{R_1R_2}{R_2-R_1} = 1.113\times10^{-10}\ \text{F/m}\times\frac{0.050\times0.10}{0.050}\ \text{m} = 1.11\times10^{-11}\ \text{F}$$

(abbiamo usato $4\pi\varepsilon_0 = 1.113\times10^{-10}$ F/m). La sfera interna è schermata: $C_{10} = 0$. Il guscio ha capacità verso massa $C_{20} = 4\pi\varepsilon_0R_2 = 1.11\times10^{-11}$ F (numericamente uguale a $C_{12}$ per la scelta particolare dei raggi).

(b) Primo caso: $Q_1 = C_{10}V_1 + C_{12}(V_1 - V_2) = 1.11\times10^{-11}\times1000 = 11.1$ nC; $Q_2 = C_{20}V_2 + C_{12}(V_2 - V_1) = -11.1$ nC. È il funzionamento come condensatore, con cariche uguali e opposte. Secondo caso: $Q_1 = 0 + C_{12}\cdot0 = 0$, mentre $Q_2 = C_{20}\cdot1000\ \text{V} = 11.1$ nC: la sfera interna, allo stesso potenziale del guscio, resta scarica, e la carica si dispone tutta sulla superficie esterna del guscio.

(c) Nel primo caso $U_e = \frac{1}{2}C_{12}(V_1-V_2)^2 = \frac{1}{2}\times1.11\times10^{-11}\times10^6 = 5.6\times10^{-6}$ J.

### Punti chiave

- In un sistema di $N$ conduttori potenziali e cariche sono legati linearmente: $V_i = \sum_j p_{ij}Q_j$ e $Q_i = \sum_j c_{ij}V_j$, con coefficienti puramente geometrici.
- I coefficienti sono simmetrici ($p_{ij} = p_{ji}$, teorema di reciprocità), conseguenza della conservatività del campo e dell'unicità dell'energia.
- $c_{ii} > 0$, $c_{ij}\le 0$ per $i\ne j$; la mutua capacità è $C_{ij} = -c_{ij}$ e la capacità verso massa è $C_{i0} = \sum_j c_{ij}$.
- Ogni sistema di conduttori equivale a una rete di condensatori: mutue capacità fra le coppie e capacità verso massa.
- Il condensatore ideale (induzione completa) ha solo mutua capacità; un conduttore racchiuso in un guscio ha capacità verso l'esterno nulla (schermo elettrostatico).
- Le capacità parassite causano accoppiamenti indesiderati (diafonia), ma la variazione di mutua capacità è sfruttata nei sensori capacitivi e negli schermi tattili.
