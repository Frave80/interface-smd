# Capitolo 6 — Meccanica relativistica

La meccanica relativa del capitolo precedente poggia su due ipotesi così naturali da sembrare ovvie: il tempo scorre allo stesso modo per tutti gli osservatori, e la lunghezza di un oggetto è la stessa per chiunque la misuri. Da esse discendono le trasformazioni di Galileo e la regola di composizione delle velocità per semplice somma vettoriale. Alla fine dell'Ottocento, però, l'elettromagnetismo di Maxwell e una serie di esperimenti di grande precisione sulla propagazione della luce misero in crisi questo quadro: la velocità della luce nel vuoto risultava la stessa per tutti gli osservatori inerziali, in palese contraddizione con la composizione galileiana delle velocità. Nel 1905 Albert Einstein risolse la contraddizione rinunciando al carattere assoluto del tempo. Ne nacque la **teoria della relatività speciale** (o ristretta), che modifica profondamente i concetti di simultaneità, durata e lunghezza, e che si riduce alla meccanica classica quando le velocità in gioco sono piccole rispetto a quella della luce. In questo capitolo ricaviamo, a partire dai postulati, le conseguenze cinematiche della relatività speciale (relatività della simultaneità, dilatazione dei tempi, contrazione delle lunghezze), le trasformazioni di Lorentz e la nuova legge di composizione delle velocità; concludiamo con una panoramica dei diversi livelli del principio di relatività, da quello galileiano a quello generale. Per un ingegnere questi concetti non sono una curiosità accademica: il sistema di posizionamento satellitare GPS, per esempio, non funzionerebbe senza le correzioni relativistiche.

## 6.1 Relatività speciale

Il punto di partenza della relatività speciale sono due **postulati** enunciati da Einstein:

1. **Principio di relatività**: le leggi della fisica (non solo della meccanica, ma anche dell'elettromagnetismo e dell'ottica) hanno la stessa forma in tutti i sistemi di riferimento inerziali. Nessun esperimento eseguito all'interno di un riferimento permette di stabilire se esso è in quiete o in moto rettilineo uniforme.
2. **Costanza della velocità della luce**: la velocità della luce nel vuoto ha lo stesso valore $c$ in tutti i riferimenti inerziali, indipendentemente dal moto della sorgente e dell'osservatore.

Il valore di $c$ è oggi fissato per definizione: $c = 299\,792\,458\ \mathrm{m/s}$, ed è proprio su questo valore esatto che si basa, dal 1983, la definizione del metro nel Sistema Internazionale. Il secondo postulato è sorprendente: se un'astronave che viaggia a $0{,}5c$ accende un faro in avanti, sia gli astronauti sia un osservatore a terra misurano per la luce la velocità $c$, e non $1{,}5c$ come prevedrebbe la composizione galileiana. La conferma sperimentale più celebre è l'esperimento di **Michelson e Morley** (1887), che con un interferometro cercò invano una differenza nella velocità della luce lungo direzioni diverse rispetto al moto orbitale della Terra; esperimenti successivi con sorgenti in moto veloce (per esempio fotoni emessi da pioni che viaggiano a $0{,}99975c$, al CERN nel 1964) hanno confermato che la velocità della luce non dipende da quella della sorgente.

Accettare entrambi i postulati richiede di rivedere le nozioni di tempo e di spazio. Per farlo in modo operativo, cioè in termini di procedure di misura, immaginiamo che ogni riferimento inerziale sia dotato di un reticolo di regoli rigidi e di orologi identici posti in ogni punto, a riposo nel riferimento. Un **evento** è qualcosa che accade in un punto dello spazio in un istante: è individuato da quattro numeri $(x, y, z, t)$ letti sui regoli e sull'orologio che si trovano in quel punto.

### 6.1.1 Misure indipendenti

Prima di scoprire quali grandezze cambiano tra un riferimento e l'altro, conviene individuare quelle che non cambiano, cioè le **misure indipendenti** dall'osservatore. Sono il fondamento su cui costruire il resto.

La prima è la **coincidenza di eventi**. Se due eventi avvengono nello stesso punto e nello stesso istante (due particelle che si urtano, una lancetta che si trova di fronte a una tacca, un fotone che colpisce un rivelatore), tutti gli osservatori concordano su questo fatto. Una coincidenza spazio-temporale lascia tracce fisiche (un urto, un segno, un'esplosione) che non possono dipendere dal punto di vista.

La seconda sono le **lunghezze trasversali**, cioè perpendicolari alla direzione del moto relativo. Consideriamo due riferimenti $S$ e $S'$, con $S'$ in moto con velocità $V$ lungo l'asse $x$ comune. Supponiamo che in ciascun riferimento ci sia un'asta di lunghezza propria $1\ \mathrm{m}$ disposta lungo $y$, con un pennello alle estremità. Quando le aste si incrociano, ciascuna lascia un segno sull'altra. Se, per esempio, l'asta in moto risultasse più corta per l'osservatore $S$, per il principio di relatività anche l'asta di $S$ dovrebbe risultare più corta per $S'$: ma allora i segni lasciati sarebbero contraddittori (l'asta di $S$ sporcherebbe quella di $S'$ dentro i suoi estremi, e viceversa). Poiché i segni sono fatti oggettivi, l'unica possibilità coerente con la simmetria tra i due riferimenti è che le lunghezze trasversali siano uguali: $y' = y$, $z' = z$.

La terza grandezza indipendente è proprio la **velocità della luce**, per il secondo postulato. Infine, sono indipendenti dal riferimento le **grandezze proprie**: il **tempo proprio** di un orologio è quello misurato da un orologio che si muove insieme al fenomeno, e la **lunghezza propria** di un oggetto è quella misurata nel riferimento in cui l'oggetto è a riposo. Tutti gli osservatori concordano sul valore di queste grandezze, perché esse si riferiscono a un riferimento ben preciso. Ciò che invece dipende dall'osservatore, come vedremo, sono le durate e le lunghezze longitudinali misurate in riferimenti in cui il fenomeno o l'oggetto è in moto.

### 6.1.2 Simultaneità

In meccanica classica due eventi simultanei per un osservatore lo sono per tutti. In relatività questo non è più vero. Per capirlo, bisogna anzitutto definire che cosa significa che due orologi posti in punti diversi sono **sincronizzati**. Einstein propose una procedura operativa basata sulla luce: si invia un lampo da un punto A a un punto B, dove viene riflesso e torna in A. Se il lampo parte da A all'istante $t_1$ (letto sull'orologio di A) e ritorna all'istante $t_2$, l'orologio di B è sincronizzato con quello di A se, nel momento della riflessione, segna $(t_1 + t_2)/2$. Questa procedura presuppone che la luce impieghi lo stesso tempo all'andata e al ritorno, il che è garantito dall'isotropia e dalla costanza di $c$ nel riferimento in cui A e B sono fermi. Un modo equivalente: un lampo emesso nel punto medio di A e B raggiunge contemporaneamente A e B.

Consideriamo ora il celebre esperimento ideale del **treno di Einstein**. Un vagone si muove con velocità $V$ rispetto al marciapiede. Al centro del vagone una lampada emette un lampo. Nel riferimento del vagone ($S'$), la luce percorre la stessa distanza verso la parete anteriore e verso quella posteriore, con la stessa velocità $c$: i due arrivi sono **simultanei**. Nel riferimento del marciapiede ($S$), la luce viaggia ancora con velocità $c$ in entrambe le direzioni (secondo postulato), ma nel frattempo la parete posteriore si avvicina al punto di emissione e quella anteriore se ne allontana. Di conseguenza la luce raggiunge prima la parete posteriore e poi quella anteriore: per l'osservatore a terra **i due eventi non sono simultanei**.

Non c'è contraddizione: semplicemente la simultaneità di eventi che avvengono in punti diversi dello spazio non è un concetto assoluto, ma relativo al riferimento. Questa è forse la conseguenza più profonda della relatività speciale, ed è all'origine di tutte le altre. Quantitativamente, come si ricava dalle trasformazioni di Lorentz (sezione 6.2), due eventi simultanei in $S'$ e separati da una distanza $\Delta x'$ lungo la direzione del moto risultano, in $S$, separati da un intervallo di tempo

$$\Delta t = \gamma\,\frac{V\,\Delta x'}{c^2}.$$

Con $V$ dell'ordine di quelle quotidiane, il fattore $V/c^2$ è minuscolo: per un treno a $100\ \mathrm{m/s}$ e una distanza di $100\ \mathrm{m}$, $\Delta t \approx 10^{-13}\ \mathrm{s}$. Questo spiega perché la relatività della simultaneità sfugge completamente all'esperienza comune.

È importante sottolineare che la relatività della simultaneità non mette in discussione la **causalità**. Se un evento A può essere la causa di un evento B (cioè un segnale con velocità non superiore a $c$ può collegarli), allora tutti gli osservatori concordano che A precede B. L'ordine temporale può invertirsi solo tra eventi che nessun segnale fisico può collegare.

### 6.1.3 Intervallo di tempo

Per confrontare le durate misurate in due riferimenti, si utilizza un dispositivo ideale particolarmente semplice: l'**orologio a luce**. È costituito da due specchi paralleli, posti a distanza $L$ l'uno dall'altro, tra i quali rimbalza un impulso luminoso. Un "tic" corrisponde a un viaggio di andata e ritorno. Nel riferimento $S'$ in cui l'orologio è fermo, il tempo di un tic è

$$\Delta t_0 = \frac{2L}{c}.$$

Questo è il **tempo proprio**: è misurato da un singolo orologio, fermo rispetto ai due eventi (partenza e ritorno dell'impulso), che avvengono nello stesso punto.

Supponiamo ora che l'orologio si muova con velocità $V$ rispetto al riferimento $S$, in direzione perpendicolare alla congiungente degli specchi. Per l'osservatore in $S$ l'impulso percorre una traiettoria obliqua, a zig-zag: durante il viaggio di andata, che dura $\Delta t/2$, lo specchio si sposta orizzontalmente di $V\Delta t/2$. La distanza $L$ tra gli specchi è trasversale al moto e quindi è la stessa in $S$ (misura indipendente). La luce, per il secondo postulato, viaggia a velocità $c$ anche in $S$. Applicando il teorema di Pitagora al percorso di andata:

$$\left(\frac{c\,\Delta t}{2}\right)^2 = L^2 + \left(\frac{V\,\Delta t}{2}\right)^2.$$

Risolvendo rispetto a $\Delta t$ e usando $L = c\,\Delta t_0/2$:

$$\Delta t = \frac{\Delta t_0}{\sqrt{1 - V^2/c^2}} = \gamma\,\Delta t_0, \qquad \gamma = \frac{1}{\sqrt{1 - \beta^2}}, \quad \beta = \frac{V}{c}.$$

Il **fattore di Lorentz** $\gamma$ è sempre maggiore o uguale a 1. Il risultato è la **dilatazione dei tempi**: un orologio in moto appare scandire il tempo più lentamente di quanto facciano gli orologi del riferimento rispetto a cui si muove. Il ragionamento non riguarda solo l'orologio a luce: per il principio di relatività, tutti i processi fisici (oscillazioni atomiche, decadimenti radioattivi, battito cardiaco) devono rallentare nello stesso modo, altrimenti si potrebbe usare la discrepanza tra due tipi di orologi per rivelare il moto assoluto.

La conferma sperimentale più nota riguarda i **muoni** prodotti dai raggi cosmici nell'alta atmosfera, a circa $10$-$15\ \mathrm{km}$ di quota. Il muone è una particella instabile con vita media propria $\tau_0 = 2{,}2\ \mu\mathrm{s}$. Anche viaggiando quasi alla velocità della luce, in $2{,}2\ \mu\mathrm{s}$ percorrerebbe solo $660\ \mathrm{m}$: quasi nessun muone dovrebbe raggiungere il suolo. Invece se ne osservano moltissimi, perché nel riferimento terrestre la loro vita media è dilatata del fattore $\gamma$, che può valere 10-50. Esperimenti con muoni accelerati in anelli di accumulazione (CERN, 1977) hanno verificato la formula con precisione del per mille. Anche gli orologi atomici trasportati su aerei (esperimento di Hafele e Keating, 1971) e quelli a bordo dei satelliti GPS mostrano il ritardo previsto.

È essenziale notare la simmetria: ciascun osservatore vede rallentare gli orologi dell'altro. Non c'è contraddizione, perché il confronto richiede orologi diversi in punti diversi, e la sincronizzazione di questi orologi dipende dal riferimento, come visto a proposito della simultaneità.

### 6.1.4 Lunghezza longitudinale

Consideriamo ora un'asta disposta lungo la direzione del moto relativo. Nel riferimento $S'$ in cui l'asta è ferma, la sua lunghezza è $L_0$, **lunghezza propria**. Per misurarne la lunghezza in $S$, rispetto al quale l'asta si muove con velocità $V$, occorre segnare **simultaneamente** (in $S$) le posizioni dei due estremi. Un modo semplice per determinare il risultato sfrutta i muoni dell'esempio precedente. Nel riferimento della Terra il muone percorre lo spessore $L_0$ dell'atmosfera in un tempo $\Delta t = L_0/V$, e in questo tempo il suo orologio interno avanza di $\Delta t_0 = \Delta t/\gamma$. Nel riferimento del muone, invece, il muone è fermo e l'atmosfera gli scorre incontro con velocità $V$; il tempo che impiega a passare è il tempo proprio del muone, $\Delta t_0$. Quindi, per il muone, lo spessore dell'atmosfera è

$$L = V\,\Delta t_0 = \frac{V\,\Delta t}{\gamma} = \frac{L_0}{\gamma} = L_0\sqrt{1 - \frac{V^2}{c^2}}.$$

Questa è la **contrazione delle lunghezze** (o contrazione di Lorentz-FitzGerald): un oggetto in moto appare accorciato nella direzione del moto di un fattore $1/\gamma$. Le dimensioni trasversali restano invariate. Il muone, che nel suo riferimento vive solo $2{,}2\ \mu\mathrm{s}$, riesce a raggiungere il suolo perché vede l'atmosfera contratta: due descrizioni diverse dello stesso fatto oggettivo (il muone arriva a terra), coerenti tra loro.

Due osservazioni concettuali sono importanti. Primo, la contrazione non è una compressione fisica dell'oggetto dovuta a forze: è una conseguenza della diversa definizione di simultaneità nei due riferimenti, poiché misurare una lunghezza significa rilevare simultaneamente le posizioni degli estremi. Secondo, la contrazione è reciproca: un'asta ferma in $S$ appare contratta all'osservatore $S'$. Si potrebbe pensare a paradossi (il "paradosso del garage": un'asta lunga entra in un garage corto se si muove abbastanza veloce, per l'osservatore del garage, ma non per quello dell'asta), che si risolvono tutti osservando che "l'asta è interamente dentro il garage" è un'affermazione sulla simultaneità di due eventi distanti, e come tale dipende dal riferimento.

Per velocità ordinarie gli effetti sono infinitesimi: un'automobile lunga $4\ \mathrm{m}$ a $30\ \mathrm{m/s}$ si contrae di circa $L_0\beta^2/2 \approx 2\times10^{-14}\ \mathrm{m}$, meno del diametro di un nucleo atomico.

### Esercizio d'esempio

Un muone viene prodotto a quota $h = 12\ \mathrm{km}$ e si muove verticalmente verso il suolo con velocità $V = 0{,}998\,c$. La sua vita media propria è $\tau_0 = 2{,}2\ \mu\mathrm{s}$. Calcolare (a) il fattore di Lorentz, (b) la vita media nel riferimento terrestre e la distanza media percorsa, (c) lo spessore dell'atmosfera nel riferimento del muone. ($c = 3{,}00\times10^8\ \mathrm{m/s}$.)

**Soluzione.** (a)

$$\gamma = \frac{1}{\sqrt{1 - 0{,}998^2}} = \frac{1}{\sqrt{1 - 0{,}996004}} = \frac{1}{\sqrt{0{,}003996}} = \frac{1}{0{,}0632} \approx 15{,}8.$$

(b) Vita media nel riferimento terrestre:

$$\tau = \gamma\tau_0 = 15{,}8\cdot2{,}2\ \mu\mathrm{s} \approx 34{,}8\ \mu\mathrm{s}.$$

Distanza media percorsa: $d = V\tau = 0{,}998\cdot3{,}00\times10^8\cdot34{,}8\times10^{-6}\ \mathrm{m} \approx 1{,}04\times10^4\ \mathrm{m} = 10{,}4\ \mathrm{km}$. Senza dilatazione dei tempi si avrebbe solo $V\tau_0 \approx 659\ \mathrm{m}$.

(c) Nel riferimento del muone:

$$L = \frac{h}{\gamma} = \frac{12\times10^3}{15{,}8}\ \mathrm{m} \approx 759\ \mathrm{m}.$$

Il tempo per attraversarlo è $L/V \approx 2{,}5\ \mu\mathrm{s}$, confrontabile con $\tau_0$: una frazione significativa dei muoni ($e^{-2{,}5/2{,}2} \approx 32\%$) raggiunge il suolo, in accordo con le osservazioni. Lo stesso valore si ottiene nel riferimento terrestre: $e^{-12/10{,}4} \approx 32\%$.

### Punti chiave

- Postulati di Einstein: le leggi fisiche sono le stesse in tutti i riferimenti inerziali; la velocità della luce nel vuoto è $c$ per tutti.
- Coincidenze di eventi, lunghezze trasversali, velocità della luce e grandezze proprie sono indipendenti dall'osservatore.
- La simultaneità di eventi distanti è relativa: eventi simultanei in $S'$ non lo sono in $S$ se separati lungo la direzione del moto.
- Dilatazione dei tempi: $\Delta t = \gamma\Delta t_0$, con $\gamma = 1/\sqrt{1 - V^2/c^2} \geq 1$ e $\Delta t_0$ tempo proprio.
- Contrazione delle lunghezze: $L = L_0/\gamma$ nella sola direzione del moto, con $L_0$ lunghezza propria.
- Gli effetti sono reciproci e non contraddittori, perché coinvolgono la sincronizzazione di orologi distanti.
- La causalità è preservata: l'ordine di eventi collegabili da segnali non cambia.
- Verifiche sperimentali: muoni cosmici, orologi atomici su aerei e satelliti, particelle negli acceleratori.

## 6.2 Cinematica relativistica

### 6.2.1 Cinematica inerziale

La **cinematica inerziale** relativistica si occupa di come si trasformano le coordinate di un evento, le velocità e, più in generale, le grandezze cinematiche passando da un riferimento inerziale a un altro. In meccanica classica questo ruolo è svolto dalle trasformazioni di Galileo; in relatività speciale esse devono essere sostituite da trasformazioni compatibili con l'invarianza della velocità della luce: le **trasformazioni di Lorentz**.

**Le trasformazioni di Lorentz.** Consideriamo la **configurazione standard**: due riferimenti inerziali $S$ e $S'$ con assi paralleli, $S'$ in moto con velocità $V$ lungo l'asse $x$ di $S$, e origini coincidenti all'istante $t = t' = 0$. Si cercano trasformazioni lineari (la linearità discende dall'omogeneità dello spazio e del tempo: nessun punto e nessun istante sono privilegiati). Le coordinate trasversali, come abbiamo visto, non cambiano. Per le coordinate $x$ e $t$, imponendo che un lampo di luce emesso dall'origine all'istante zero si propaghi come una sfera di raggio $ct$ in $S$ e $ct'$ in $S'$, e che per $V \ll c$ si ritrovino le trasformazioni di Galileo, si ottiene:

$$x' = \gamma\,(x - Vt), \qquad y' = y, \qquad z' = z, \qquad t' = \gamma\left(t - \frac{V}{c^2}\,x\right).$$

Le trasformazioni inverse si ottengono scambiando le coordinate con e senza apice e cambiando segno a $V$, come imposto dal principio di relatività:

$$x = \gamma\,(x' + Vt'), \qquad t = \gamma\left(t' + \frac{V}{c^2}\,x'\right).$$

La novità essenziale rispetto a Galileo è la seconda equazione: il tempo $t'$ dipende non solo da $t$ ma anche dalla posizione $x$. È questo termine, $-\gamma Vx/c^2$, che codifica la relatività della simultaneità: eventi con lo stesso $t$ ma diverso $x$ hanno, in $S'$, tempi $t'$ diversi. Nel **limite classico** $V \ll c$, si ha $\gamma \to 1$ e $Vx/c^2 \to 0$, e si ritrovano esattamente $x' = x - Vt$ e $t' = t$. La meccanica newtoniana appare così come caso limite della relatività, valido con ottima approssimazione per tutte le velocità tecnologiche ordinarie: anche per un satellite in orbita bassa, a circa $7{,}7\ \mathrm{km/s}$, si ha $\gamma - 1 \approx 3\times10^{-10}$.

Dalle trasformazioni di Lorentz si ritrovano immediatamente i risultati della sezione 6.1. Per la **dilatazione dei tempi**: un orologio fermo in $S'$ nel punto $x'$ fissato registra due eventi separati da $\Delta t'$ e $\Delta x' = 0$; dalla trasformazione inversa $\Delta t = \gamma\,\Delta t'$. Per la **contrazione delle lunghezze**: un'asta ferma in $S'$ ha estremi con $\Delta x' = L_0$; misurandone gli estremi simultaneamente in $S$ ($\Delta t = 0$), dalla prima equazione $L_0 = \gamma\,\Delta x$, cioè $\Delta x = L_0/\gamma$. Per la **simultaneità**: due eventi con $\Delta t' = 0$ e $\Delta x' \neq 0$ hanno $\Delta t = \gamma V\Delta x'/c^2 \neq 0$.

**L'intervallo invariante.** Le trasformazioni di Galileo lasciano invariati separatamente l'intervallo di tempo e la distanza spaziale tra due eventi simultanei. Quelle di Lorentz non conservano né l'uno né l'altra, ma lasciano invariata una loro combinazione, l'**intervallo spazio-temporale**:

$$\Delta s^2 = c^2\Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2.$$

Si verifica per sostituzione diretta che $\Delta s'^2 = \Delta s^2$. Questa invarianza è l'analogo, nello **spazio-tempo di Minkowski**, dell'invarianza della distanza euclidea per rotazioni nello spazio ordinario: le trasformazioni di Lorentz si possono interpretare come "rotazioni" (iperboliche) nello spazio-tempo quadridimensionale. Il segno dell'intervallo classifica le coppie di eventi: se $\Delta s^2 > 0$ l'intervallo è **di tipo tempo** e gli eventi possono essere legati causalmente (esiste un riferimento in cui avvengono nello stesso punto, e lì $\Delta s/c$ è il tempo proprio); se $\Delta s^2 < 0$ è **di tipo spazio** e nessun segnale può collegarli (esiste un riferimento in cui sono simultanei); se $\Delta s^2 = 0$ è **di tipo luce**, e gli eventi sono collegabili solo da un raggio luminoso. Poiché $\Delta s^2$ è invariante, questa classificazione è la stessa per tutti gli osservatori, e ciò garantisce che la causalità sia rispettata.

**Composizione delle velocità.** Supponiamo che un punto si muova con velocità $u'_x$ lungo $x'$ nel riferimento $S'$. Quale velocità misura l'osservatore in $S$? Differenziando le trasformazioni inverse, $dx = \gamma(dx' + V\,dt')$ e $dt = \gamma(dt' + V\,dx'/c^2)$; dividendo:

$$u_x = \frac{dx}{dt} = \frac{u'_x + V}{1 + \dfrac{u'_x V}{c^2}}.$$

Questa è la **legge relativistica di composizione delle velocità** (per moti paralleli alla velocità relativa). Per velocità piccole il denominatore tende a 1 e si ritrova la somma galileiana $u_x = u'_x + V$. Per velocità grandi, la somma è sempre minore di $c$: componendo due velocità inferiori a $c$ non si supera mai $c$. Per esempio, se $u'_x = 0{,}8c$ e $V = 0{,}8c$, si ottiene $u_x = 1{,}6c/1{,}64 \approx 0{,}976c$, e non $1{,}6c$. Se poi $u'_x = c$ (un raggio di luce), si ottiene $u_x = (c + V)/(1 + V/c) = c$, qualunque sia $V$: la formula incorpora il secondo postulato. Per le componenti trasversali, anche se le lunghezze trasversali sono invarianti, la velocità cambia perché cambia il tempo:

$$u_y = \frac{u'_y}{\gamma\left(1 + \dfrac{u'_x V}{c^2}\right)}.$$

**La velocità della luce come limite.** Il fattore $\gamma$ diventa immaginario per $V > c$, e le trasformazioni di Lorentz perdono significato: nessun riferimento inerziale può muoversi con velocità pari o superiore a $c$ rispetto a un altro. Analogamente, nessun segnale che trasporti informazione o energia può propagarsi più veloce della luce, perché altrimenti esisterebbero riferimenti in cui l'effetto precede la causa. Questo limite si riflette nella dinamica relativistica: per accelerare un corpo dotato di massa fino a $c$ occorrerebbe un'energia infinita, come mostrano l'impulso relativistico $\vec{p} = \gamma m\vec{v}$ e l'energia $E = \gamma mc^2$. Gli acceleratori di particelle ne danno ogni giorno conferma: i protoni del Large Hadron Collider, con energia di $6{,}8\ \mathrm{TeV}$, hanno $\gamma \approx 7000$ ma velocità inferiore a $c$ di circa $3\ \mathrm{m/s}$.

**Effetto Doppler relativistico.** Una conseguenza importante della cinematica relativistica riguarda la frequenza della luce emessa da una sorgente in moto. Se una sorgente che emette con frequenza propria $f_0$ si allontana dall'osservatore con velocità $V$ lungo la linea di vista, la frequenza ricevuta è

$$f = f_0\sqrt{\frac{1 - \beta}{1 + \beta}},$$

e diventa $f_0\sqrt{(1 + \beta)/(1 - \beta)}$ per una sorgente in avvicinamento. Rispetto al caso acustico, qui conta solo la velocità relativa tra sorgente e osservatore, perché non esiste un mezzo privilegiato. Questo effetto, combinato con la dilatazione dei tempi, permette di misurare le velocità delle galassie (spostamento verso il rosso) ed è sfruttato nei radar di velocità e nella spettroscopia.

### Esercizio d'esempio

Nel riferimento $S$ del laboratorio, due eventi avvengono nelle coordinate $(x_1 = 0,\ t_1 = 0)$ e $(x_2 = 900\ \mathrm{m},\ t_2 = 2{,}0\ \mu\mathrm{s})$. Un riferimento $S'$ si muove con velocità $V = 0{,}60\,c$ lungo $x$. (a) Calcolare $\Delta x'$ e $\Delta t'$. (b) Verificare l'invarianza dell'intervallo e stabilirne il tipo. (c) Una particella si muove in $S'$ con $u'_x = 0{,}70\,c$: calcolarne la velocità in $S$. ($c = 3{,}00\times10^8\ \mathrm{m/s}$.)

**Soluzione.** (a) $\gamma = 1/\sqrt{1 - 0{,}36} = 1/0{,}80 = 1{,}25$; $V = 1{,}80\times10^8\ \mathrm{m/s}$.

$$\Delta x' = \gamma(\Delta x - V\Delta t) = 1{,}25\,(900 - 1{,}80\times10^8\cdot2{,}0\times10^{-6})\ \mathrm{m} = 1{,}25\,(900 - 360)\ \mathrm{m} = 675\ \mathrm{m},$$

$$\Delta t' = \gamma\left(\Delta t - \frac{V\Delta x}{c^2}\right) = 1{,}25\left(2{,}0\times10^{-6} - \frac{1{,}80\times10^8\cdot900}{9{,}00\times10^{16}}\right)\ \mathrm{s} = 1{,}25\,(2{,}0 - 1{,}8)\times10^{-6}\ \mathrm{s} = 0{,}25\ \mu\mathrm{s}.$$

(b) In $S$: $c\Delta t = 600\ \mathrm{m}$, $\Delta s^2 = 600^2 - 900^2 = -4{,}5\times10^5\ \mathrm{m^2}$. In $S'$: $c\Delta t' = 75\ \mathrm{m}$, $\Delta s'^2 = 75^2 - 675^2 = 5625 - 455625 = -4{,}5\times10^5\ \mathrm{m^2}$. L'intervallo è invariante e negativo, quindi di tipo spazio: nessun segnale può collegare i due eventi, e infatti esiste un riferimento (con $V = c^2\Delta t/\Delta x = 0{,}667\,c$) in cui sono simultanei.

(c)

$$u_x = \frac{0{,}70c + 0{,}60c}{1 + 0{,}70\cdot0{,}60} = \frac{1{,}30c}{1{,}42} \approx 0{,}915\,c.$$

### Punti chiave

- Le trasformazioni di Lorentz sostituiscono quelle di Galileo: $x' = \gamma(x - Vt)$, $t' = \gamma(t - Vx/c^2)$, con coordinate trasversali invariate.
- Il termine $Vx/c^2$ nella trasformazione del tempo esprime la relatività della simultaneità.
- Per $V \ll c$ si ritrovano le trasformazioni di Galileo: la meccanica classica è un caso limite.
- L'intervallo $\Delta s^2 = c^2\Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$ è invariante e classifica le coppie di eventi in tipo tempo, spazio, luce.
- Composizione delle velocità: $u_x = (u'_x + V)/(1 + u'_x V/c^2)$; il risultato non supera mai $c$.
- Nessun riferimento, corpo massivo o segnale può raggiungere o superare la velocità della luce.
- L'effetto Doppler relativistico dipende solo dalla velocità relativa tra sorgente e osservatore.

## 6.3 Principi di relatività

Il termine "relatività" indica, in fisica, un'affermazione sul fatto che le leggi della natura siano le stesse per osservatori diversi. A seconda di quali osservatori si considerano equivalenti e di quali leggi si richiede che siano invarianti, si ottengono enunciati di portata crescente. Possiamo distinguere tre livelli: il principio di relatività **semplice** (o galileiano), valido per la meccanica e per riferimenti inerziali con trasformazioni di Galileo; il principio di relatività **speciale** (o ristretto), esteso da Einstein a tutte le leggi fisiche, ancora per riferimenti inerziali ma con trasformazioni di Lorentz; il principio di relatività **generale**, che estende l'equivalenza a riferimenti in moto qualsiasi e fornisce una nuova teoria della gravitazione. Ripercorrerli in sequenza permette di comprendere la logica che ha guidato lo sviluppo della fisica moderna e di collocare correttamente i risultati dei capitoli precedenti.

### 6.3.1 Principi semplici

Il primo principio di relatività della storia della fisica fu enunciato da Galileo Galilei nel *Dialogo sopra i due massimi sistemi del mondo* (1632), con l'esempio della nave già ricordato nel capitolo 5. Nella formulazione moderna esso afferma che **le leggi della meccanica sono le stesse in tutti i sistemi di riferimento inerziali**. Le relazioni tra le coordinate di due riferimenti inerziali sono le trasformazioni di Galileo,

$$\vec{r}\,' = \vec{r} - \vec{V}t, \qquad t' = t,$$

e il loro contenuto fisico si riassume in due presupposti: il **tempo assoluto**, uguale per tutti gli osservatori, e lo **spazio assoluto** nel senso che le distanze tra punti misurate simultaneamente sono le stesse per tutti. Da qui discendono la composizione additiva delle velocità e l'invarianza delle accelerazioni.

L'equazione di Newton, $\vec{F} = m\vec{a}$, è **invariante** (o, più precisamente, **covariante**) rispetto alle trasformazioni di Galileo: le masse sono le stesse, le accelerazioni sono le stesse, e le forze fondamentali della meccanica classica (gravitazione, forze elastiche, reazioni di contatto) dipendono da distanze e velocità relative, anch'esse invarianti. Di conseguenza nessun esperimento puramente meccanico permette di distinguere un riferimento inerziale da un altro: non esiste uno stato di "quiete assoluta" rilevabile.

Il principio di relatività galileiana ha una struttura che conviene sottolineare, perché si ritrova identica nei livelli successivi. Esso afferma l'esistenza di una **classe privilegiata di osservatori** (gli inerziali), di un **gruppo di trasformazioni** che li collega (Galileo) e di una **classe di leggi** (la meccanica) che non cambiano forma sotto tali trasformazioni. Le "versioni" del principio di relatività differiscono per l'estensione di ciascuna di queste tre componenti.

Nella seconda metà dell'Ottocento si constatò che il principio galileiano non poteva essere esteso all'elettromagnetismo. Le equazioni di Maxwell prevedono che le onde elettromagnetiche si propaghino con velocità $c = 1/\sqrt{\varepsilon_0\mu_0}$, un valore che non contiene alcun riferimento al moto dell'osservatore. Se valessero le trasformazioni di Galileo, questo risultato potrebbe valere in un solo riferimento, quello dell'ipotetico **etere** luminifero, e le equazioni di Maxwell avrebbero forme diverse negli altri riferimenti. Si sarebbe dovuto poter misurare il moto della Terra rispetto all'etere: è esattamente ciò che l'esperimento di Michelson e Morley cercò e non trovò. Il risultato nullo lasciava aperte due strade: abbandonare il principio di relatività per l'elettromagnetismo oppure abbandonare le trasformazioni di Galileo.

### 6.3.2 Principi speciali

Einstein scelse la seconda strada. Il principio di relatività speciale estende il principio galileiano a **tutte le leggi della fisica**, meccaniche, elettromagnetiche, ottiche, e lo affianca al postulato della costanza della velocità della luce. La classe di osservatori privilegiati rimane quella dei riferimenti inerziali, ma il gruppo di trasformazioni che li collega cambia: al posto di Galileo ci sono le **trasformazioni di Lorentz**. Con esse le equazioni di Maxwell risultano automaticamente covarianti (lo erano già, come aveva osservato Lorentz stesso, ma senza un'interpretazione fisica coerente), mentre deve essere modificata la meccanica di Newton.

La nuova meccanica che soddisfa il principio di relatività speciale ha alcuni tratti caratteristici. La **quantità di moto** diventa $\vec{p} = \gamma m\vec{v}$, e la legge fondamentale della dinamica si scrive nella forma $\vec{F} = d\vec{p}/dt$, che rimane valida, mentre la forma $\vec{F} = m\vec{a}$ non lo è più. L'**energia** di una particella libera è $E = \gamma mc^2$, che per velocità piccole si sviluppa come $mc^2 + \tfrac{1}{2}mv^2 + \ldots$: il secondo termine è la familiare energia cinetica, il primo è l'**energia di riposo**, che esprime l'equivalenza tra massa ed energia, $E_0 = mc^2$. Energia e quantità di moto sono legate dalla relazione invariante

$$E^2 = (pc)^2 + (mc^2)^2,$$

analoga all'invarianza dell'intervallo spazio-temporale. Questa equivalenza non è un'astrazione: il difetto di massa dei nuclei atomici, cioè la differenza tra la massa di un nucleo e la somma delle masse dei suoi costituenti, moltiplicato per $c^2$, dà l'energia liberata nelle reazioni nucleari che alimentano le stelle e le centrali.

La relatività speciale ha anche una struttura geometrica elegante, introdotta da Hermann Minkowski nel 1908: spazio e tempo formano un unico **spazio-tempo** quadridimensionale in cui l'intervallo $\Delta s^2$ gioca il ruolo di "distanza". Le leggi fisiche covarianti si scrivono come relazioni tra **quadrivettori** (posizione-tempo, energia-impulso), che si trasformano tutti allo stesso modo. Questo linguaggio è lo strumento naturale per verificare se una legge rispetta il principio di relatività: se è scritta in forma quadrivettoriale, lo rispetta automaticamente.

I confini di validità del principio di relatività speciale sono chiari: esso riguarda i riferimenti inerziali e non dice nulla della gravitazione. La legge di gravitazione di Newton, che prevede un'azione istantanea a distanza, è incompatibile con la relatività speciale, nella quale nessuna influenza può propagarsi più veloce della luce. Inoltre, la definizione stessa di riferimento inerziale contiene una circolarità: un riferimento è inerziale se in esso un corpo libero da forze si muove di moto rettilineo uniforme, ma come stabilire che un corpo è libero da forze se la gravità agisce su tutti i corpi e non può essere schermata? Questi problemi spinsero Einstein a cercare un'ulteriore generalizzazione.

### 6.3.3 Principi generali

Il punto di partenza è un fatto sperimentale già incontrato nei capitoli 4 e 5: l'**uguaglianza tra massa inerziale e massa gravitazionale**. Grazie a essa tutti i corpi cadono con la stessa accelerazione in un campo gravitazionale, e le forze apparenti, proporzionali alla massa inerziale, si comportano esattamente come forze gravitazionali. Einstein elevò questo fatto a principio, il **principio di equivalenza**: in una regione sufficientemente piccola dello spazio-tempo, gli effetti di un campo gravitazionale sono indistinguibili da quelli di un'accelerazione del sistema di riferimento. Un osservatore chiuso in un ascensore senza finestre non può stabilire, con nessun esperimento locale, se si trova fermo sulla superficie terrestre oppure in un razzo che accelera con $a = g$ nello spazio vuoto. Simmetricamente, un ascensore in caduta libera in un campo gravitazionale è localmente indistinguibile da un riferimento inerziale lontano da ogni massa: è un **riferimento localmente inerziale**.

Si distinguono una forma **debole** del principio di equivalenza, che riguarda solo l'universalità della caduta libera (uguaglianza delle masse) ed è verificata con precisione relativa migliore di $10^{-15}$ (missione satellitare MICROSCOPE, 2022), e una forma **forte** (o einsteiniana), secondo cui *tutte* le leggi della fisica, non solo quelle meccaniche, assumono in un riferimento in caduta libera la forma che hanno in relatività speciale.

Il **principio di relatività generale** completa il quadro affermando che le leggi della fisica devono poter essere scritte in una forma valida per **qualunque sistema di riferimento**, inerziale o no (principio di **covarianza generale**). Non esiste più una classe privilegiata di osservatori. Le forze apparenti e la gravità vengono interpretate come manifestazioni della stessa realtà: la **curvatura dello spazio-tempo** prodotta dalla presenza di massa ed energia. I corpi in caduta libera seguono le "linee più dritte possibili" (geodetiche) in uno spazio-tempo curvo, e ciò che chiamiamo forza gravitazionale è l'effetto di questa curvatura. La teoria, pubblicata da Einstein nel 1915, si riduce alla gravitazione newtoniana per campi deboli e velocità piccole, così come la relatività speciale si riduce alla meccanica galileiana.

Le previsioni della relatività generale sono state verificate con successo crescente: la precessione anomala del perielio di Mercurio (43 secondi d'arco per secolo), la deflessione della luce delle stelle in prossimità del Sole (Eddington, 1919), lo **spostamento gravitazionale verso il rosso** e il conseguente rallentamento degli orologi in un potenziale gravitazionale più profondo (Pound e Rebka, 1959), le onde gravitazionali rivelate direttamente da LIGO e Virgo nel 2015, le immagini dell'ombra dei buchi neri ottenute dall'Event Horizon Telescope.

L'esempio ingegneristico più significativo è il **GPS**. Gli orologi atomici a bordo dei satelliti, in orbita a circa $20\,200\ \mathrm{km}$ di quota con velocità di circa $3{,}9\ \mathrm{km/s}$, subiscono due effetti relativistici di segno opposto. La dilatazione dei tempi della relatività speciale li fa ritardare di circa $7\ \mu\mathrm{s}$ al giorno rispetto agli orologi a terra; l'effetto gravitazionale della relatività generale, poiché si trovano in un potenziale gravitazionale meno profondo, li fa avanzare di circa $45\ \mu\mathrm{s}$ al giorno. L'effetto netto è un anticipo di circa $38\ \mu\mathrm{s}$ al giorno. Moltiplicato per $c$, un errore di questa entità corrisponderebbe a un errore di posizione che cresce di oltre $10\ \mathrm{km}$ al giorno. Per questo la frequenza degli orologi satellitari viene corretta già prima del lancio. È un esempio concreto di come i tre livelli del principio di relatività, da Galileo a Einstein, non siano solo tappe della storia del pensiero ma strumenti indispensabili della tecnologia contemporanea.

### Esercizio d'esempio

Stimare gli effetti relativistici sugli orologi di un satellite GPS. Dati: raggio orbitale $r = 2{,}66\times10^7\ \mathrm{m}$, raggio terrestre $R_T = 6{,}37\times10^6\ \mathrm{m}$, $GM_T = 3{,}99\times10^{14}\ \mathrm{m^3/s^2}$, $c = 3{,}00\times10^8\ \mathrm{m/s}$. Si usi per l'effetto gravitazionale l'approssimazione di campo debole: il ritmo relativo di due orologi a potenziali $\Phi_1$ e $\Phi_2$ differisce di $(\Phi_2 - \Phi_1)/c^2$, con $\Phi = -GM_T/r$. Si trascuri la rotazione terrestre.

**Soluzione.** Velocità orbitale:

$$v = \sqrt{\frac{GM_T}{r}} = \sqrt{\frac{3{,}99\times10^{14}}{2{,}66\times10^7}}\ \mathrm{m/s} = \sqrt{1{,}50\times10^7}\ \mathrm{m/s} \approx 3{,}87\times10^3\ \mathrm{m/s}.$$

*Effetto cinematico (relatività speciale).* Per $\beta \ll 1$, $\gamma - 1 \approx \beta^2/2$:

$$\frac{v^2}{2c^2} = \frac{1{,}50\times10^7}{2\cdot9{,}00\times10^{16}} \approx 8{,}3\times10^{-11}.$$

In un giorno ($8{,}64\times10^4\ \mathrm{s}$) l'orologio satellitare ritarda di $8{,}3\times10^{-11}\cdot8{,}64\times10^4\ \mathrm{s} \approx 7{,}2\ \mu\mathrm{s}$.

*Effetto gravitazionale (relatività generale).*

$$\frac{\Delta\Phi}{c^2} = \frac{GM_T}{c^2}\left(\frac{1}{R_T} - \frac{1}{r}\right) = \frac{3{,}99\times10^{14}}{9{,}00\times10^{16}}\left(1{,}570\times10^{-7} - 3{,}76\times10^{-8}\right) \approx 4{,}43\times10^{-3}\cdot1{,}194\times10^{-7} \approx 5{,}29\times10^{-10}.$$

In un giorno l'orologio satellitare anticipa di $5{,}29\times10^{-10}\cdot8{,}64\times10^4\ \mathrm{s} \approx 45{,}7\ \mu\mathrm{s}$.

*Effetto netto:* anticipo di circa $45{,}7 - 7{,}2 \approx 38{,}5\ \mu\mathrm{s}$ al giorno, corrispondente a un errore di distanza di $c\cdot38{,}5\ \mu\mathrm{s} \approx 11{,}5\ \mathrm{km}$ al giorno se non corretto.

### Punti chiave

- Ogni principio di relatività specifica una classe di osservatori equivalenti, un gruppo di trasformazioni e una classe di leggi invarianti.
- Principio semplice (Galileo): le leggi della meccanica sono le stesse nei riferimenti inerziali, collegati da trasformazioni di Galileo con tempo assoluto.
- L'elettromagnetismo di Maxwell e il risultato nullo di Michelson-Morley sono incompatibili con le trasformazioni di Galileo.
- Principio speciale (Einstein, 1905): tutte le leggi fisiche sono le stesse nei riferimenti inerziali, collegati da trasformazioni di Lorentz; ne derivano $\vec{p} = \gamma m\vec{v}$ ed $E = \gamma mc^2$.
- Il principio di equivalenza afferma che localmente gravità e accelerazione sono indistinguibili; si basa sull'uguaglianza di massa inerziale e gravitazionale.
- Principio generale (Einstein, 1915): le leggi fisiche valgono in ogni riferimento; la gravità è curvatura dello spazio-tempo.
- Ogni livello si riduce al precedente nel limite opportuno (velocità piccole, campi deboli).
- Il GPS richiede correzioni sia di relatività speciale (circa $-7\ \mu\mathrm{s}$/giorno) sia generale (circa $+45\ \mu\mathrm{s}$/giorno).
