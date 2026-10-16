# Capitolo 24 — Elettromagnetismo

Nei capitoli precedenti elettrostatica e magnetostatica sono state trattate come due teorie separate: le cariche ferme generano campi elettrici, le correnti stazionarie generano campi magnetici, e in regime statico i due campi non si influenzano. Questo capitolo mostra che la separazione è solo apparente. Da un lato la teoria della relatività ristretta rivela che campo elettrico e campo magnetico sono due aspetti di un'unica entità, il campo elettromagnetico, e che la loro suddivisione dipende dall'osservatore. Dall'altro, quando i campi variano nel tempo, essi si generano a vicenda: un campo magnetico variabile produce un campo elettrico (legge di Faraday-Neumann-Lenz), e un campo elettrico variabile produce un campo magnetico (corrente di spostamento di Maxwell). Le quattro equazioni di Maxwell che ne risultano costituiscono una delle sintesi più potenti della fisica: da esse discende l'esistenza di onde elettromagnetiche che si propagano nel vuoto alla velocità della luce, rivelando la natura elettromagnetica della luce stessa.

## 24.1 Relatività

### 24.1.1 Fisica classica

Consideriamo un esperimento concettuale molto semplice. Un filo rettilineo indefinito, elettricamente neutro, è percorso da una corrente $I$; parallelamente al filo, a distanza $r$, una carica di prova $q$ si muove con velocità $\vec{v}$. Nel sistema di riferimento del laboratorio $S$, in cui il filo è fermo, la descrizione è nota: il filo è neutro e non produce campo elettrico, ma la corrente genera un campo magnetico azimutale $B=\mu_0 I/(2\pi r)$, e la carica, essendo in moto, subisce la forza di Lorentz magnetica $F = qvB$, diretta radialmente.

Mettiamoci ora nel sistema di riferimento $S'$ che si muove insieme alla carica. In $S'$ la carica è ferma, e una carica ferma non risente di alcuna forza magnetica, qualunque sia il campo $\vec{B}'$. Eppure l'esperienza ci dice che la carica viene deviata: se in $S$ essa si avvicina al filo, lo farà anche in $S'$, perché l'accelerazione trasversale (e la deviazione della traiettoria) è un fatto fisico che tutti gli osservatori devono riconoscere. In $S'$, dunque, deve esistere un **campo elettrico** che agisce sulla carica ferma. Ma da dove viene, se il filo è neutro?

Nell'ambito della meccanica classica, che si fonda sulle **trasformazioni di Galileo** ($\vec{r}\,'=\vec{r}-\vec{v}t$, $t'=t$), le forze sono invarianti nel passaggio tra sistemi inerziali, perché le accelerazioni lo sono. Imponendo che la forza su una carica sia la stessa nei due riferimenti, $q(\vec{E}'+\vec{0}\times\vec{B}') = q(\vec{E}+\vec{v}\times\vec{B})$, si ottiene la regola di trasformazione

$$\vec{E}' = \vec{E}+\vec{v}\times\vec{B},$$

che rappresenta l'approssimazione di bassa velocità della trasformazione corretta. Considerazioni analoghe sul campo generato da una carica in moto lento ($\vec{B}=\frac{\mu_0}{4\pi}q\vec{v}\times\hat{r}/r^2$) portano a $\vec{B}'\simeq\vec{B}-\vec{v}\times\vec{E}/c^2$. Già a questo livello emerge un fatto fondamentale: **la suddivisione del campo elettromagnetico in parte elettrica e parte magnetica dipende dal sistema di riferimento**. Ciò che in un riferimento appare come campo magnetico puro può apparire, in un altro, come una combinazione di campo elettrico e magnetico.

La fisica classica, tuttavia, va incontro a una contraddizione più profonda. Le equazioni di Maxwell, che studieremo nella prossima sezione, contengono esplicitamente una velocità, $c=1/\sqrt{\varepsilon_0\mu_0}$, con cui le onde elettromagnetiche si propagano nel vuoto. Secondo le trasformazioni di Galileo le velocità si sommano, quindi la luce dovrebbe avere velocità $c$ solo in un riferimento privilegiato, che nell'Ottocento si identificava con un ipotetico mezzo, l'**etere**, supporto delle onde elettromagnetiche. Le equazioni di Maxwell non sono invarianti in forma sotto trasformazioni galileiane, e varrebbero esattamente solo nel riferimento dell'etere. Il celebre **esperimento di Michelson e Morley** (1887) cercò di misurare la velocità della Terra rispetto all'etere confrontando, con un interferometro, i tempi di percorrenza della luce in direzioni diverse. Il risultato fu nullo con una precisione ampiamente sufficiente a rivelare l'effetto atteso: la velocità della luce risulta la stessa in tutte le direzioni e per tutti gli osservatori, indipendentemente dal moto della Terra.

Un secondo segnale della crisi viene proprio dall'esperimento del filo. Se si trasforma il campo con le leggi galileiane in modo coerente, la forza trasversale nei due riferimenti risulta uguale solo all'ordine più basso in $v/c$: la meccanica di Newton e l'elettromagnetismo di Maxwell non possono essere entrambi esatti. Tra le due teorie, è la meccanica a dover essere modificata.

### 24.1.2 Fisica relativistica

Nel 1905 Einstein risolse la contraddizione con due postulati: il **principio di relatività**, secondo cui le leggi della fisica (inclusa l'elettrodinamica) hanno la stessa forma in tutti i sistemi inerziali, e il **principio di costanza della velocità della luce**, secondo cui la luce nel vuoto si propaga con la stessa velocità $c$ in tutti i sistemi inerziali. Ne derivano le **trasformazioni di Lorentz**, che per un riferimento $S'$ in moto con velocità $v$ lungo l'asse $x$ di $S$ si scrivono

$$x' = \gamma(x-vt),\qquad y'=y,\qquad z'=z,\qquad t' = \gamma\left(t-\frac{vx}{c^2}\right),\qquad \gamma=\frac{1}{\sqrt{1-v^2/c^2}}.$$

Tra le conseguenze ci interessa soprattutto la **contrazione delle lunghezze**: un oggetto di lunghezza propria $L_0$ (misurata nel riferimento in cui è fermo) appare, in un riferimento in cui si muove con velocità $v$ lungo la propria lunghezza, contratto alla lunghezza $L_0/\gamma$. Un altro elemento fondamentale è l'**invarianza della carica elettrica**: la carica di una particella è la stessa per tutti gli osservatori, come dimostra sperimentalmente la neutralità esatta degli atomi, nei quali elettroni e protoni hanno velocità molto diverse.

Torniamo al filo con la corrente, adottando un modello semplice: gli ioni positivi sono fermi in $S$ con densità lineare $\lambda_0$, gli elettroni di conduzione si muovono con velocità $v$ lungo $x$ con densità lineare $-\lambda_0$ (il filo in $S$ è neutro), e la carica di prova $q$ si muove anch'essa con velocità $v$, parallela agli elettroni. La corrente vale $I = \lambda_0 v$. In $S$ la forza sulla carica è puramente magnetica:

$$F = qvB = qv\frac{\mu_0\lambda_0 v}{2\pi r}.$$

Passiamo al riferimento $S'$, solidale con la carica e con gli elettroni. Per la contrazione delle lunghezze, le densità lineari di carica cambiano. Gli elettroni, fermi in $S'$, hanno lì la loro densità propria; poiché in $S$, dove si muovono, la densità è $\lambda_0$, quella propria è $\lambda_0/\gamma$ (le distanze tra elettroni sono più grandi nel loro riferimento di quiete). Gli ioni, che in $S$ sono fermi con densità $\lambda_0$, in $S'$ si muovono con velocità $-v$ e le distanze tra loro si contraggono: la loro densità diventa $\gamma\lambda_0$. La densità di carica netta del filo in $S'$ è dunque

$$\lambda' = \gamma\lambda_0-\frac{\lambda_0}{\gamma} = \gamma\lambda_0\left(1-\frac{1}{\gamma^2}\right) = \gamma\lambda_0\frac{v^2}{c^2}.$$

**Nel riferimento della carica il filo non è più neutro**: è carico positivamente e produce un campo elettrico radiale $E' = \lambda'/(2\pi\varepsilon_0 r)$. La forza sulla carica ferma è

$$F' = qE' = \frac{q\gamma\lambda_0 v^2}{2\pi\varepsilon_0 c^2 r} = \gamma\,q v\frac{\mu_0\lambda_0 v}{2\pi r},$$

dove si è usato $1/(\varepsilon_0c^2)=\mu_0$. In relatività la forza trasversale si trasforma come $F = F'/\gamma$ passando dal riferimento di quiete della particella a quello in cui essa si muove, e si ottiene esattamente $F = qvB$. La forza che in $S$ chiamiamo magnetica è, in $S'$, una forza elettrica dovuta alla contrazione relativistica delle distribuzioni di carica. Il magnetismo è, in questo senso, un **effetto relativistico** dell'elettricità.

Ci si potrebbe chiedere come un effetto proporzionale a $v^2/c^2$ possa essere così evidente, dato che le velocità di deriva degli elettroni nei conduttori sono dell'ordine dei millimetri al secondo, e quindi $v^2/c^2\sim10^{-23}$. La risposta sta nell'enorme quantità di carica presente in un conduttore: in un filo di rame di un millimetro quadrato di sezione ci sono circa $10^4\,\mathrm{C}$ di elettroni di conduzione per metro di lunghezza, e le forze elettriche tra cariche di questa entità sarebbero colossali. Nella materia ordinaria esse sono perfettamente compensate dalla neutralità; la minuscola frazione relativistica che sopravvive è sufficiente a produrre le forze magnetiche che muovono i motori elettrici.

L'analisi generale porta alle **trasformazioni relativistiche dei campi**. Indicando con i pedici $\parallel$ e $\perp$ le componenti parallele e perpendicolari alla velocità relativa $\vec{v}$ tra i riferimenti:

$$\vec{E}'_\parallel=\vec{E}_\parallel,\qquad \vec{E}'_\perp=\gamma\left(\vec{E}+\vec{v}\times\vec{B}\right)_\perp,$$
$$\vec{B}'_\parallel=\vec{B}_\parallel,\qquad \vec{B}'_\perp=\gamma\left(\vec{B}-\frac{\vec{v}\times\vec{E}}{c^2}\right)_\perp.$$

Per $v\ll c$ si ritrovano le relazioni approssimate viste nell'ambito classico. Ne segue, ad esempio, che una carica in moto uniforme, che nel suo riferimento di quiete produce solo un campo elettrico coulombiano $\vec{E}'$, nel riferimento del laboratorio produce anche un campo magnetico $\vec{B}=\vec{v}\times\vec{E}/c^2$, che per basse velocità coincide con quello dato dalla prima legge di Laplace. Il campo elettrico e il campo magnetico sono quindi componenti di un unico oggetto, il **tensore del campo elettromagnetico**, che si trasforma in modo definito sotto le trasformazioni di Lorentz. Esistono però grandezze che tutti gli osservatori concordano nel misurare uguali: gli **invarianti** $\vec{E}\cdot\vec{B}$ e $E^2-c^2B^2$. Se ad esempio in un riferimento esiste solo un campo magnetico ($E=0$), allora $E^2-c^2B^2<0$ in ogni riferimento, e non esiste alcun osservatore inerziale per cui il campo sia puramente elettrico. Le equazioni di Maxwell, a differenza della meccanica newtoniana, sono già invarianti per trasformazioni di Lorentz: l'elettromagnetismo era una teoria relativistica ancor prima che la relatività fosse formulata.

### Esercizio d'esempio

**Problema.** In un riferimento $S$ esiste un campo magnetico uniforme $\vec{B}=0{,}50\,\hat{z}\,\mathrm{T}$ e nessun campo elettrico. Un osservatore $S'$ si muove con velocità $\vec{v}=v\,\hat{x}$, con $v=3{,}0\times10^{5}\,\mathrm{m/s}$. Calcolare i campi misurati in $S'$. Ripetere per $v=0{,}60\,c$. Verificare l'invariante $E^2-c^2B^2$.

**Soluzione.** Il campo $\vec{B}$ è perpendicolare a $\vec{v}$. Si ha $\vec{v}\times\vec{B} = vB\,(\hat{x}\times\hat{z}) = -vB\,\hat{y}$.

Per $v=3{,}0\times10^{5}\,\mathrm{m/s}$, $v/c=10^{-3}$ e $\gamma\simeq1+5\times10^{-7}\simeq1$:
$$\vec{E}'\simeq-vB\,\hat{y} = -3{,}0\times10^{5}\cdot0{,}50\,\hat{y} = -1{,}5\times10^{5}\,\hat{y}\,\mathrm{V/m},\qquad \vec{B}'\simeq\vec{B}.$$
Un campo elettrico intenso, $150\,\mathrm{kV/m}$, compare per un osservatore che si muove in un campo magnetico.

Per $v=0{,}60\,c$: $\gamma = 1/\sqrt{1-0{,}36}=1{,}25$. Allora
$$E' = \gamma vB = 1{,}25\cdot0{,}60\cdot3{,}0\times10^{8}\cdot0{,}50 \simeq 1{,}1\times10^{8}\,\mathrm{V/m},\qquad B' = \gamma B = 0{,}625\,\mathrm{T}.$$
Verifica dell'invariante: in $S$, $E^2-c^2B^2 = -(3{,}0\times10^{8}\cdot0{,}50)^2 = -2{,}25\times10^{16}\,\mathrm{V^2/m^2}$. In $S'$:
$$E'^2-c^2B'^2 = \gamma^2 B^2(v^2-c^2) = -\gamma^2B^2c^2(1-v^2/c^2) = -c^2B^2,$$
identico. Anche $\vec{E}'\cdot\vec{B}'=0$, come $\vec{E}\cdot\vec{B}=0$ in $S$.

### Punti chiave

- La distinzione tra campo elettrico e campo magnetico dipende dal sistema di riferimento.
- In fisica classica (trasformazioni di Galileo) si ha approssimativamente $\vec{E}'=\vec{E}+\vec{v}\times\vec{B}$, ma le equazioni di Maxwell non sono invarianti galileiane.
- L'esperimento di Michelson-Morley mostra che la velocità della luce non dipende dal moto dell'osservatore: non esiste un etere rivelabile.
- La relatività ristretta (trasformazioni di Lorentz, contrazione delle lunghezze, invarianza della carica) rende coerente l'elettromagnetismo.
- La forza magnetica tra un filo e una carica in moto appare, nel riferimento della carica, come forza elettrica dovuta alla contrazione delle densità di carica.
- I campi si trasformano con $\vec{E}'_\perp=\gamma(\vec{E}+\vec{v}\times\vec{B})_\perp$ e $\vec{B}'_\perp=\gamma(\vec{B}-\vec{v}\times\vec{E}/c^2)_\perp$; $\vec{E}\cdot\vec{B}$ e $E^2-c^2B^2$ sono invarianti.
- Le equazioni di Maxwell sono intrinsecamente relativistiche.

## 24.2 Equazioni di Maxwell

### 24.2.1 Legge di Faraday-Neumann-Lenz

Dopo la scoperta di Ørsted che le correnti producono campi magnetici, era naturale chiedersi se valesse anche il viceversa, cioè se un campo magnetico potesse produrre una corrente. Nel 1831 Faraday scoprì che ciò avviene, ma solo quando il campo magnetico **varia**. Avvicinando o allontanando una calamita da una bobina collegata a un galvanometro, si osserva una corrente che dura finché il moto continua e cambia verso quando il moto si inverte; lo stesso effetto si ottiene accendendo o spegnendo la corrente in una seconda bobina vicina, oppure deformando o ruotando il circuito in un campo costante. In tutti i casi il fattore comune è la variazione del **flusso magnetico concatenato** con il circuito, $\Phi_B=\int_S\vec{B}\cdot\hat{n}\,\mathrm{d}S$, che grazie al teorema di Gauss magnetico dipende solo dal circuito e non dalla superficie scelta.

La formulazione quantitativa, dovuta a Faraday e Neumann, è la **legge di Faraday-Neumann-Lenz**: in un circuito chiuso si induce una **forza elettromotrice** pari all'opposto della derivata temporale del flusso concatenato,

$$\mathcal{E} = -\frac{\mathrm{d}\Phi_B}{\mathrm{d}t}.$$

Il segno meno esprime la **legge di Lenz**: la corrente indotta circola in un verso tale da produrre un campo magnetico che si oppone alla variazione di flusso che l'ha generata. Se il flusso aumenta, la corrente indotta genera un flusso opposto; se diminuisce, genera un flusso concorde. La legge di Lenz è una manifestazione della conservazione dell'energia: se la corrente indotta favorisse la variazione, si avrebbe un meccanismo di autoalimentazione capace di produrre energia dal nulla. Per esempio, avvicinando un polo nord a una spira, nella spira si induce una corrente che presenta verso il magnete un polo nord, respingendolo: l'operatore deve compiere lavoro, che si ritrova come energia dissipata per effetto Joule nella spira.

La forza elettromotrice è, per definizione, il lavoro per unità di carica compiuto lungo il circuito dalle forze che agiscono sui portatori: $\mathcal{E}=\oint(\vec{F}/q)\cdot\mathrm{d}\vec{l}$. Si distinguono due casi fisicamente diversi. Quando il circuito si muove in un campo magnetico statico (**f.e.m. di movimento**), la forza che agisce sui portatori è la forza di Lorentz magnetica, $\vec{F}/q = \vec{v}\times\vec{B}$; un esempio è la sbarretta conduttrice di lunghezza $l$ che scorre con velocità $v$ su due binari in un campo $B$ perpendicolare, in cui $\mathcal{E}=Blv$, coerente con $\mathrm{d}\Phi/\mathrm{d}t = Bl\,\mathrm{d}x/\mathrm{d}t$. Quando invece il circuito è fermo e il campo magnetico varia nel tempo, sui portatori fermi non può agire una forza magnetica: la forza elettromotrice deve essere dovuta a un **campo elettrico indotto**, e scriviamo

$$\oint_\gamma\vec{E}\cdot\mathrm{d}\vec{l} = -\frac{\mathrm{d}}{\mathrm{d}t}\int_S\vec{B}\cdot\hat{n}\,\mathrm{d}S.$$

Questa è la forma più profonda della legge: essa vale per qualunque linea chiusa nello spazio, anche in assenza di conduttori. Un campo magnetico variabile genera nello spazio un campo elettrico la cui circuitazione non è nulla: **il campo elettrico indotto non è conservativo**, e non può essere descritto da un potenziale scalare. Che i due casi, moto del circuito e variazione del campo, diano la stessa legge del flusso fu per Einstein uno dei punti di partenza della relatività: per il principio di relatività conta solo il moto relativo tra magnete e circuito, e la distinzione tra f.e.m. "elettrica" e "magnetica" dipende dal riferimento, come abbiamo visto nella sezione precedente.

Le applicazioni della legge sono innumerevoli: il **generatore** (alternatore), in cui una bobina che ruota con velocità angolare $\omega$ in un campo uniforme produce $\mathcal{E}=NBS\omega\sin\omega t$; il **trasformatore**, in cui il flusso variabile prodotto dal primario induce nel secondario una tensione nel rapporto del numero di spire; le **correnti parassite** (di Foucault), usate nei freni elettromagnetici e nei fornelli a induzione; i pick-up delle chitarre elettriche e le carte contactless.

### 24.2.2 Corrente di spostamento

Il teorema di Ampère nella forma magnetostatica, $\oint\vec{B}\cdot\mathrm{d}\vec{l}=\mu_0 I_{conc}$, presenta un'incoerenza quando le correnti non sono stazionarie. Consideriamo un condensatore piano che si sta caricando attraverso un filo percorso dalla corrente $I$, e una linea chiusa $\gamma$ che circonda il filo. Se si sceglie come superficie appoggiata a $\gamma$ un disco attraversato dal filo, la corrente concatenata è $I$; se invece si sceglie una superficie a forma di sacchetto che passa tra le armature del condensatore senza toccare il filo, la corrente concatenata è nulla, perché nello spazio tra le armature non scorre carica. La circuitazione di $\vec{B}$ lungo la stessa linea non può avere due valori diversi: il teorema di Ampère, così com'è, non può essere valido.

L'origine del problema è chiara in forma differenziale: dalla legge di Ampère $\nabla\times\vec{B}=\mu_0\vec{J}$ segue $\nabla\cdot\vec{J}=0$, mentre l'equazione di continuità impone $\nabla\cdot\vec{J}=-\partial\rho/\partial t$, che è diverso da zero dove la carica si accumula, come sulle armature del condensatore. Maxwell risolse la contraddizione osservando che, per il teorema di Gauss, $\rho=\varepsilon_0\nabla\cdot\vec{E}$, e quindi

$$\nabla\cdot\vec{J}+\frac{\partial\rho}{\partial t} = \nabla\cdot\left(\vec{J}+\varepsilon_0\frac{\partial\vec{E}}{\partial t}\right) = 0.$$

La combinazione tra parentesi ha sempre divergenza nulla. Maxwell propose quindi di sostituire nella legge di Ampère la densità di corrente di conduzione $\vec{J}$ con questa somma, introducendo la **densità di corrente di spostamento**

$$\vec{J}_s = \varepsilon_0\frac{\partial\vec{E}}{\partial t}.$$

La legge di **Ampère-Maxwell** diventa

$$\oint_\gamma\vec{B}\cdot\mathrm{d}\vec{l} = \mu_0 I_{conc}+\mu_0\varepsilon_0\frac{\mathrm{d}}{\mathrm{d}t}\int_S\vec{E}\cdot\hat{n}\,\mathrm{d}S.$$

Nel caso del condensatore, tra le armature il campo è $E=\sigma/\varepsilon_0=Q/(\varepsilon_0A)$, quindi il flusso di $\vec{E}$ attraverso la superficie a sacchetto è $Q/\varepsilon_0$ e la corrente di spostamento è $\varepsilon_0\,\mathrm{d}(Q/\varepsilon_0)/\mathrm{d}t = \mathrm{d}Q/\mathrm{d}t = I$: esattamente la corrente di conduzione nel filo. La circuitazione ora non dipende più dalla superficie scelta, e la contraddizione è risolta. Il nome "corrente di spostamento" è un retaggio storico, legato all'idea di Maxwell che si trattasse di uno spostamento di cariche nell'etere; in realtà nel vuoto non c'è alcun moto di cariche, e il termine esprime semplicemente il fatto che **un campo elettrico variabile genera un campo magnetico**, simmetricamente a quanto accade nella legge di Faraday.

Nei circuiti ordinari la corrente di spostamento è spesso trascurabile rispetto a quella di conduzione, e la sua esistenza è stata verificata direttamente solo con misure delicate del campo magnetico tra le armature di un condensatore in alternata. La sua conferma più spettacolare è però indiretta: senza la corrente di spostamento non esisterebbero le onde elettromagnetiche.

### 24.2.3 Forma integrale

Siamo ora in grado di scrivere le **equazioni di Maxwell** nel vuoto, in forma integrale, valide per campi comunque variabili nel tempo. Per ogni superficie chiusa $S$ e ogni linea chiusa $\gamma$ (bordo di una superficie aperta $\Sigma$):

$$\oint_S\vec{E}\cdot\hat{n}\,\mathrm{d}S = \frac{Q_{int}}{\varepsilon_0}\qquad\text{(Gauss elettrico)}$$
$$\oint_S\vec{B}\cdot\hat{n}\,\mathrm{d}S = 0\qquad\text{(Gauss magnetico)}$$
$$\oint_\gamma\vec{E}\cdot\mathrm{d}\vec{l} = -\frac{\mathrm{d}}{\mathrm{d}t}\int_\Sigma\vec{B}\cdot\hat{n}\,\mathrm{d}S\qquad\text{(Faraday-Neumann-Lenz)}$$
$$\oint_\gamma\vec{B}\cdot\mathrm{d}\vec{l} = \mu_0 I_{conc}+\mu_0\varepsilon_0\frac{\mathrm{d}}{\mathrm{d}t}\int_\Sigma\vec{E}\cdot\hat{n}\,\mathrm{d}S\qquad\text{(Ampère-Maxwell)}$$

Le prime due equazioni riguardano i flussi e descrivono le sorgenti: le cariche elettriche sono sorgenti del campo elettrico, mentre non esistono sorgenti scalari del campo magnetico. Le ultime due riguardano le circuitazioni e descrivono l'accoppiamento dinamico: la variazione temporale di ciascun campo genera l'altro. Insieme alla forza di Lorentz $\vec{F}=q(\vec{E}+\vec{v}\times\vec{B})$, che descrive come i campi agiscono sulle cariche, esse racchiudono l'intero elettromagnetismo classico. Nel caso statico, con le derivate temporali nulle, si ritrovano le leggi dell'elettrostatica e della magnetostatica studiate nei capitoli precedenti.

Si noti la notevole simmetria delle equazioni in assenza di cariche e correnti: le due equazioni di flusso sono entrambe omogenee, e le due di circuitazione differiscono solo per il segno e per il fattore $\mu_0\varepsilon_0 = 1/c^2$. La residua asimmetria tra $\vec{E}$ e $\vec{B}$ in presenza di sorgenti è dovuta all'assenza di cariche e correnti magnetiche.

### 24.2.4 Forma differenziale

Applicando il teorema della divergenza alle equazioni di flusso e il teorema di Stokes a quelle di circuitazione, con le stesse argomentazioni usate nella sezione 23.7, si ottiene la **forma differenziale** (o locale):

$$\nabla\cdot\vec{E} = \frac{\rho}{\varepsilon_0},\qquad \nabla\cdot\vec{B}=0,$$
$$\nabla\times\vec{E} = -\frac{\partial\vec{B}}{\partial t},\qquad \nabla\times\vec{B} = \mu_0\vec{J}+\mu_0\varepsilon_0\frac{\partial\vec{E}}{\partial t}.$$

Nella forma integrale della legge di Faraday compare la derivata totale del flusso, che tiene conto anche di un eventuale moto del circuito; nella forma differenziale, che riguarda punti fissi dello spazio, compare la derivata parziale del campo. Le equazioni differenziali contengono implicitamente la **conservazione della carica**: prendendo la divergenza della quarta e usando la prima si ottiene $\nabla\cdot\vec{J}+\partial\rho/\partial t=0$. Sono equazioni lineari nei campi, per cui vale il principio di sovrapposizione, e sono, come anticipato, invarianti sotto trasformazioni di Lorentz.

I campi possono ancora essere espressi tramite potenziali. Da $\nabla\cdot\vec{B}=0$ segue sempre $\vec{B}=\nabla\times\vec{A}$; sostituendo nella legge di Faraday si ha $\nabla\times(\vec{E}+\partial\vec{A}/\partial t)=0$, per cui la combinazione tra parentesi è il gradiente di un potenziale scalare: $\vec{E}=-\nabla V-\partial\vec{A}/\partial t$. In regime dinamico, dunque, il campo elettrico non è più solo il gradiente del potenziale: c'è un contributo legato alla variazione temporale del potenziale vettore, che è proprio il campo elettrico indotto.

In un **mezzo materiale** lineare, omogeneo e isotropo le equazioni si scrivono in modo analogo introducendo i campi $\vec{D}=\varepsilon\vec{E}$ e $\vec{H}=\vec{B}/\mu$, con le sole cariche e correnti libere come sorgenti: $\nabla\cdot\vec{D}=\rho_{lib}$ e $\nabla\times\vec{H}=\vec{J}_{lib}+\partial\vec{D}/\partial t$. Le costanti del vuoto sono sostituite da $\varepsilon=\varepsilon_0\varepsilon_r$ e $\mu=\mu_0\mu_r$, con conseguenze importanti per la propagazione delle onde, come vedremo nella prossima sezione.

### Esercizio d'esempio

**Problema.** Un condensatore piano ha armature circolari di raggio $R=5{,}0\,\mathrm{cm}$ distanti $d=2{,}0\,\mathrm{mm}$ ed è caricato da una corrente costante $I=0{,}20\,\mathrm{A}$. Calcolare la rapidità di variazione del campo elettrico tra le armature, la corrente di spostamento e il campo magnetico a distanza $r=3{,}0\,\mathrm{cm}$ e $r=8{,}0\,\mathrm{cm}$ dall'asse, nel piano medio. Si trascurino gli effetti di bordo.

**Soluzione.** Tra le armature $E = Q/(\varepsilon_0\pi R^2)$, quindi
$$\frac{\mathrm{d}E}{\mathrm{d}t} = \frac{I}{\varepsilon_0\pi R^2} = \frac{0{,}20}{8{,}85\times10^{-12}\cdot\pi\cdot(5{,}0\times10^{-2})^2}\simeq 2{,}9\times10^{12}\,\mathrm{V\,m^{-1}s^{-1}}.$$
La corrente di spostamento totale attraverso le armature è $I_s = \varepsilon_0\pi R^2\,\mathrm{d}E/\mathrm{d}t = I = 0{,}20\,\mathrm{A}$.

Per simmetria il campo magnetico è azimutale. Per $r<R$ la corrente di spostamento concatenata è $I r^2/R^2$:
$$B(r) = \frac{\mu_0 I r}{2\pi R^2} = \frac{2\times10^{-7}\cdot0{,}20\cdot3{,}0\times10^{-2}}{(5{,}0\times10^{-2})^2}\simeq 4{,}8\times10^{-7}\,\mathrm{T}.$$
Per $r>R$ è concatenata tutta la corrente di spostamento:
$$B(r) = \frac{\mu_0 I}{2\pi r} = \frac{2\times10^{-7}\cdot0{,}20}{8{,}0\times10^{-2}} = 5{,}0\times10^{-7}\,\mathrm{T},$$
lo stesso valore che si avrebbe attorno al filo di alimentazione alla stessa distanza.

### Punti chiave

- Legge di Faraday-Neumann-Lenz: $\mathcal{E}=-\mathrm{d}\Phi_B/\mathrm{d}t$; il segno meno (Lenz) garantisce la conservazione dell'energia.
- Un campo magnetico variabile genera un campo elettrico non conservativo: $\oint\vec{E}\cdot\mathrm{d}\vec{l}=-\mathrm{d}\Phi_B/\mathrm{d}t$.
- La corrente di spostamento $\varepsilon_0\,\partial\vec{E}/\partial t$ rende la legge di Ampère compatibile con la conservazione della carica.
- Le quattro equazioni di Maxwell, in forma integrale o differenziale, con la forza di Lorentz descrivono tutto l'elettromagnetismo classico.
- Forma differenziale: $\nabla\cdot\vec{E}=\rho/\varepsilon_0$, $\nabla\cdot\vec{B}=0$, $\nabla\times\vec{E}=-\partial\vec{B}/\partial t$, $\nabla\times\vec{B}=\mu_0\vec{J}+\mu_0\varepsilon_0\partial\vec{E}/\partial t$.
- In regime dinamico $\vec{E}=-\nabla V-\partial\vec{A}/\partial t$.
- Nei mezzi lineari si usano $\vec{D}=\varepsilon\vec{E}$ e $\vec{H}=\vec{B}/\mu$ con le sole sorgenti libere.

