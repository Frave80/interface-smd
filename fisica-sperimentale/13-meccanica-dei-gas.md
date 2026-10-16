# Capitolo 13 — Meccanica dei gas

Il gas è lo stato di aggregazione in cui la materia non possiede né forma né volume propri: occupa tutto il recipiente che la contiene e può essere compresso con relativa facilità. Proprio per questa sua "semplicità" il gas è stato, storicamente, il laboratorio ideale in cui la termodinamica ha preso forma: le prime leggi quantitative su pressione, volume e temperatura sono state scoperte studiando aria e vapori, e la teoria cinetica ha mostrato per la prima volta come grandezze macroscopiche (pressione, temperatura) possano essere spiegate a partire dal moto di un enorme numero di particelle microscopiche. In questo capitolo partiremo dalle leggi empiriche del **gas ideale**, ne ricaveremo l'equazione di stato e le proprietà energetiche, interpreteremo tutto ciò alla luce della **teoria cinetica**, discuteremo i limiti del modello introducendo il **gas reale** e infine studieremo le principali **trasformazioni termodinamiche**, che costituiscono i "mattoni" con cui nel capitolo successivo costruiremo i cicli delle macchine termiche.

## 13.1 Gas ideale

Il **gas ideale** (o gas perfetto) è un modello: un sistema astratto il cui comportamento è descritto esattamente da poche leggi semplici. Nessun gas reale è perfettamente ideale, ma tutti i gas tendono a comportarsi come tali quando sono sufficientemente **rarefatti**, cioè a bassa pressione e a temperatura ben superiore a quella di liquefazione. In queste condizioni le molecole sono mediamente molto lontane le une dalle altre, il volume proprio delle molecole è trascurabile rispetto al volume del recipiente e le forze intermolecolari hanno effetto trascurabile sul moto. L'aria a temperatura e pressione ambiente, l'elio, l'idrogeno, l'azoto in condizioni ordinarie sono ottime approssimazioni di gas ideale, con scarti tipicamente inferiori all'uno per cento. Lo stato di equilibrio di una quantità fissata di gas è individuato da tre **variabili di stato** macroscopiche: la pressione $p$, il volume $V$ e la temperatura assoluta $T$. Le leggi che seguono, scoperte sperimentalmente tra il Seicento e l'Ottocento, descrivono come queste variabili sono legate quando se ne mantiene costante una.

### 13.1.1 Legge di Avogadro

Nel 1811 Amedeo Avogadro formulò un'ipotesi audace per l'epoca: **volumi uguali di gas diversi, alla stessa pressione e alla stessa temperatura, contengono lo stesso numero di molecole**. L'ipotesi permetteva di spiegare in modo naturale le leggi volumetriche di combinazione dei gas di Gay-Lussac (per esempio, due volumi di idrogeno si combinano con un volume di ossigeno per dare due volumi di vapore acqueo) ammettendo che le particelle elementari dei gas fossero molecole biatomiche.

Da questa legge discende il concetto di **mole**: la quantità di sostanza che contiene un numero di entità elementari pari al **numero di Avogadro**

$$
N_A = 6{,}022\,140\,76 \times 10^{23}\ \text{mol}^{-1},
$$

valore che dal 2019 è fissato esattamente per definizione nel Sistema Internazionale. Se un campione contiene $N$ molecole, il numero di moli è $n = N/N_A$, e la massa del campione è $m = nM$, dove $M$ è la **massa molare** (in kg/mol). La legge di Avogadro si scrive allora come proporzionalità tra volume e numero di moli a $p$ e $T$ fissati:

$$
V = k_A\, n \qquad (p, T \text{ costanti}).
$$

Una conseguenza importante è che una mole di qualunque gas ideale, nelle **condizioni normali** ($T_0 = 273{,}15$ K, $p_0 = 101\,325$ Pa), occupa sempre lo stesso **volume molare** $V_m \simeq 22{,}414 \times 10^{-3}\ \text{m}^3/\text{mol}$, cioè circa 22,4 litri. È importante sottolineare che la legge non dice nulla sulla massa: un litro di idrogeno e un litro di anidride carbonica nelle stesse condizioni contengono lo stesso numero di molecole, ma le loro masse differiscono di un fattore 22, pari al rapporto delle masse molari.

### 13.1.2 Legge di Charles

La **legge di Charles** (talvolta detta prima legge di Gay-Lussac) descrive come varia il volume di una quantità fissata di gas al variare della temperatura quando la pressione è mantenuta costante, cioè in una **trasformazione isobara**. Sperimentalmente si trova che il volume cresce linearmente con la temperatura misurata in gradi Celsius:

$$
V(\theta) = V_0\,(1 + \alpha\,\theta) \qquad (p \text{ costante}),
$$

dove $V_0$ è il volume a $0\,^\circ$C e $\alpha$ è il **coefficiente di dilatazione termica** del gas. Il fatto sperimentale notevole è che $\alpha$ è (con ottima approssimazione per gas rarefatti) lo stesso per tutti i gas e vale $\alpha \simeq 1/273{,}15\ ^\circ\text{C}^{-1}$. Questa universalità suggerisce di estrapolare la retta $V(\theta)$ fino al punto in cui il volume si annullerebbe: ciò avviene a $\theta = -1/\alpha = -273{,}15\ ^\circ$C. Questo punto viene assunto come zero della **scala assoluta** (o scala Kelvin), $T = \theta + 273{,}15$. Nella nuova scala la legge di Charles assume la forma particolarmente semplice

$$
\frac{V}{T} = \text{costante} \qquad \Longleftrightarrow \qquad \frac{V_1}{T_1} = \frac{V_2}{T_2}.
$$

Naturalmente nessun gas reale raggiunge mai volume nullo: molto prima di arrivare allo zero assoluto ogni gas liquefà. L'estrapolazione ha però un significato profondo, che sarà chiarito dalla teoria cinetica e dal secondo principio: lo zero assoluto è un limite inferiore universale della temperatura.

### 13.1.3 Legge di Gay-Lussac

La **legge di Gay-Lussac** (o seconda legge di Gay-Lussac, nota anche come legge di Amontons) riguarda le **trasformazioni isocore**, cioè a volume costante. In un recipiente rigido e chiuso la pressione del gas cresce linearmente con la temperatura:

$$
p(\theta) = p_0\,(1 + \beta\,\theta) \qquad (V \text{ costante}),
$$

e anche in questo caso il coefficiente $\beta$ risulta uguale per tutti i gas rarefatti e numericamente coincidente con $\alpha$: $\beta \simeq 1/273{,}15\ ^\circ\text{C}^{-1}$. In termini di temperatura assoluta:

$$
\frac{p}{T} = \text{costante}.
$$

Questa legge è alla base del **termometro a gas a volume costante**, lo strumento che storicamente ha fornito la realizzazione più accurata della scala assoluta delle temperature: misurando la pressione di un gas molto rarefatto contenuto in un bulbo di volume fisso, si ricava la temperatura indipendentemente dalla natura del gas utilizzato. Un esempio quotidiano è il rischio di esplosione di una bomboletta spray esposta al fuoco: a volume fisso, il riscaldamento fa crescere la pressione fino a superare la resistenza del contenitore.

### 13.1.4 Legge di Boyle-Mariotte

La **legge di Boyle-Mariotte** (Boyle 1662, Mariotte 1676) descrive le **trasformazioni isoterme**: a temperatura costante, il prodotto della pressione per il volume di una quantità fissata di gas rimane costante,

$$
p\,V = \text{costante} \qquad (T \text{ costante}).
$$

Nel piano di Clapeyron $(V, p)$ le isoterme sono quindi rami di iperbole equilatera, tanto più lontani dagli assi quanto più alta è la temperatura. Boyle verificò la legge con un tubo a J chiuso a un'estremità, in cui una colonna di mercurio comprimeva una quantità d'aria intrappolata: raddoppiando la pressione (aggiungendo mercurio) il volume dell'aria si dimezzava. Fisicamente, la legge esprime il fatto che, se la temperatura non cambia, l'unico modo per aumentare la pressione è aumentare la densità del gas, cioè il numero di urti delle molecole contro le pareti per unità di area e di tempo. La legge vale bene per gas lontani dalla liquefazione; per un vapore vicino alla saturazione, invece, una compressione isoterma porta alla condensazione e la pressione smette di crescere.

### 13.1.5 Equazione di stato dei gas

Le tre leggi precedenti, insieme alla legge di Avogadro, si possono riassumere in un'unica relazione. Consideriamo un gas che passa dallo stato $(p_1, V_1, T_1)$ allo stato $(p_2, V_2, T_2)$ attraverso uno stato intermedio: prima un'isoterma a $T_1$ fino alla pressione $p_2$, poi un'isobara fino a $T_2$. Combinando Boyle e Charles si ottiene

$$
\frac{p_1 V_1}{T_1} = \frac{p_2 V_2}{T_2},
$$

ovvero $pV/T$ è costante per una data quantità di gas. Per la legge di Avogadro, questa costante è proporzionale al numero di moli e il coefficiente di proporzionalità è universale. Si ottiene così l'**equazione di stato dei gas ideali**:

$$
p\,V = n\,R\,T,
$$

dove $R = 8{,}314\ \text{J}/(\text{mol}\cdot\text{K})$ è la **costante universale dei gas**. Introducendo la **costante di Boltzmann** $k_B = R/N_A = 1{,}380\,649 \times 10^{-23}\ \text{J/K}$ e il numero di molecole $N = n N_A$, l'equazione si scrive anche

$$
p\,V = N\,k_B\,T,
$$

forma che mette in risalto il significato microscopico: la pressione dipende solo dal numero di molecole per unità di volume $N/V$ e dalla temperatura, non dalla loro natura chimica. Un'ulteriore forma utile in ingegneria usa la densità $\rho = m/V$: $p = \rho R_s T$, dove $R_s = R/M$ è la costante specifica del gas (per l'aria $R_s \simeq 287\ \text{J/(kg K)}$). L'equazione di stato definisce una superficie nello spazio $(p,V,T)$: ogni stato di equilibrio è un punto della superficie, e qualunque trasformazione quasistatica è una curva su di essa. È essenziale ricordare che $T$ deve essere espressa in kelvin e che l'equazione si applica solo a stati di equilibrio termodinamico, nei quali $p$ e $T$ sono uniformi nel gas.

### 13.1.6 Legge di Dalton

Quando in un recipiente sono presenti più gas che non reagiscono chimicamente tra loro, si definisce **pressione parziale** $p_i$ del gas $i$-esimo la pressione che esso eserciterebbe se occupasse da solo l'intero volume alla stessa temperatura. La **legge di Dalton** (1801) afferma che la pressione totale di una miscela di gas ideali è la somma delle pressioni parziali:

$$
p = \sum_i p_i, \qquad p_i = \frac{n_i R T}{V}.
$$

Il motivo è che in un gas ideale le molecole non interagiscono: ciascuna specie urta le pareti come se le altre non ci fossero. Sommando, $p = (\sum_i n_i) RT/V = nRT/V$, quindi la miscela si comporta come un unico gas ideale con numero totale di moli $n$. Dividendo $p_i$ per $p$ si trova che la pressione parziale è proporzionale alla **frazione molare** $x_i = n_i/n$: $p_i = x_i\,p$. Per esempio, nell'aria secca a livello del mare l'ossigeno ha frazione molare circa 0,21, quindi la sua pressione parziale è circa 21 kPa; in alta quota, dove la pressione totale è minore, la pressione parziale di ossigeno diminuisce proporzionalmente, e ciò spiega le difficoltà respiratorie in montagna. La legge di Dalton è fondamentale anche in subacquea, in meteorologia (pressione parziale del vapore acqueo e umidità relativa) e nell'ingegneria chimica.

### 13.1.7 Esperimento di Joule

Per completare la descrizione del gas ideale bisogna stabilire da cosa dipende la sua **energia interna** $U$. A questo scopo Joule realizzò (1845) l'esperimento di **espansione libera**: due recipienti collegati da un rubinetto sono immersi in un calorimetro ad acqua; uno contiene gas compresso, l'altro è vuoto. Aprendo il rubinetto, il gas si espande fino a occupare entrambi i recipienti. Joule osservò che la temperatura dell'acqua del calorimetro non cambiava.

L'interpretazione si basa sul primo principio, $\Delta U = Q - W$. L'espansione avviene nel vuoto, quindi il gas non compie lavoro contro alcuna pressione esterna: $W = 0$. Poiché la temperatura del calorimetro non varia, non c'è scambio di calore: $Q = 0$. Dunque $\Delta U = 0$: l'energia interna resta invariata, mentre il volume e la pressione sono cambiati e la temperatura del gas (misurata a equilibrio raggiunto) è rimasta la stessa. Se ne conclude che **l'energia interna di un gas ideale dipende soltanto dalla temperatura**:

$$
U = U(T).
$$

Va detto che l'esperimento originale era poco sensibile, perché la capacità termica dell'acqua era molto maggiore di quella del gas; esperimenti più accurati (Joule-Thomson, con espansione attraverso un setto poroso) mostrano che i gas reali subiscono piccole variazioni di temperatura, dovute alle forze intermolecolari. Per il gas ideale, però, la conclusione è esatta e ne costituisce in pratica una seconda definizione, accanto all'equazione di stato. L'espansione libera è inoltre l'esempio paradigmatico di processo **irreversibile**: il gas non tornerà mai spontaneamente nel recipiente di partenza.

### 13.1.8 Relazione di Mayer

Definiamo i **calori specifici molari** a volume costante e a pressione costante come

$$
c_V = \frac{1}{n}\left(\frac{\delta Q}{dT}\right)_V, \qquad c_p = \frac{1}{n}\left(\frac{\delta Q}{dT}\right)_p.
$$

A volume costante il gas non compie lavoro, quindi tutto il calore va in energia interna: $\delta Q = dU = n c_V\,dT$. Poiché $U$ dipende solo da $T$, la relazione $dU = n c_V\,dT$ vale per **qualunque** trasformazione del gas ideale, non solo per quelle isocore. A pressione costante, invece, parte del calore fornito viene restituito come lavoro di espansione: $\delta Q = dU + p\,dV$. Differenziando l'equazione di stato a $p$ costante, $p\,dV = nR\,dT$, quindi

$$
n c_p\,dT = n c_V\,dT + n R\,dT \quad \Longrightarrow \quad c_p - c_V = R.
$$

È la **relazione di Mayer**: il calore specifico molare a pressione costante supera quello a volume costante esattamente di $R$, perché a pressione costante occorre fornire, oltre all'aumento di energia interna, l'energia spesa nel lavoro di espansione. Il rapporto $\gamma = c_p/c_V > 1$, detto **coefficiente adiabatico**, compare nelle trasformazioni adiabatiche e nella velocità del suono nei gas. Per gas monoatomici $c_V = \tfrac{3}{2}R$ e $\gamma = 5/3$; per gas biatomici a temperatura ambiente $c_V = \tfrac{5}{2}R$ e $\gamma = 7/5$: il significato di questi valori sarà chiarito dalla teoria cinetica.

### Esercizio d'esempio

Una bombola di volume $V = 20$ L contiene ossigeno ($M = 32$ g/mol) alla pressione $p_1 = 150$ bar e alla temperatura $\theta_1 = 20\ ^\circ$C. (a) Si calcoli la massa di ossigeno. (b) La bombola viene lasciata al sole e la temperatura sale a $\theta_2 = 50\ ^\circ$C: quale pressione si raggiunge? (c) Quanta energia interna ha guadagnato il gas, considerandolo biatomico ideale?

**Soluzione.** (a) Convertiamo in SI: $V = 2{,}0\times10^{-2}$ m$^3$, $p_1 = 1{,}50\times10^7$ Pa, $T_1 = 293{,}15$ K. Dall'equazione di stato:

$$
n = \frac{p_1 V}{R T_1} = \frac{1{,}50\times10^7 \cdot 2{,}0\times10^{-2}}{8{,}314 \cdot 293{,}15} \simeq 123\ \text{mol},
$$

quindi $m = nM \simeq 123 \cdot 0{,}032 \simeq 3{,}94$ kg.

(b) Il volume è fisso: legge di Gay-Lussac con $T_2 = 323{,}15$ K,

$$
p_2 = p_1\,\frac{T_2}{T_1} = 150\ \text{bar}\cdot\frac{323{,}15}{293{,}15} \simeq 165\ \text{bar}.
$$

(c) Con $c_V = \tfrac52 R$: $\Delta U = n c_V \Delta T = 123 \cdot 20{,}8 \cdot 30 \simeq 7{,}7\times10^4$ J. A 150 bar l'ossigeno inizia a discostarsi dal comportamento ideale (qualche per cento), ma come stima ingegneristica il risultato è adeguato.

### Punti chiave

- Il gas ideale è un modello limite valido per gas rarefatti, lontani dalla liquefazione.
- Legge di Avogadro: a parità di $p$ e $T$, volumi uguali contengono lo stesso numero di molecole; $V_m \simeq 22{,}4$ L/mol in condizioni normali.
- Charles ($V/T$ cost. a $p$ cost.), Gay-Lussac ($p/T$ cost. a $V$ cost.), Boyle ($pV$ cost. a $T$ cost.) conducono alla scala assoluta e all'equazione $pV = nRT = Nk_BT$.
- Legge di Dalton: in una miscela ideale $p = \sum p_i$, con $p_i = x_i p$.
- L'espansione libera di Joule mostra che l'energia interna del gas ideale dipende solo da $T$: $dU = nc_V\,dT$ per ogni trasformazione.
- Relazione di Mayer: $c_p - c_V = R$; il coefficiente adiabatico $\gamma = c_p/c_V$ vale $5/3$ (monoatomico) o $7/5$ (biatomico).

## 13.2 Teoria cinetica

Le leggi del gas ideale sono state scoperte come regolarità empiriche tra grandezze macroscopiche. La **teoria cinetica dei gas**, sviluppata nell'Ottocento da Clausius, Maxwell e Boltzmann, ne fornisce una spiegazione microscopica: il gas è un insieme di un numero enorme di molecole in moto disordinato, e pressione, temperatura ed energia interna non sono altro che medie di grandezze meccaniche (quantità di moto, energia cinetica) relative alle singole molecole. Il successo della teoria fu una delle prove più convincenti, prima ancora dell'osservazione diretta, dell'esistenza degli atomi, e rappresenta il primo esempio di quel ponte tra meccanica e termodinamica che verrà poi costruito sistematicamente dalla meccanica statistica.

### 13.2.1 Modello atomico

Il modello cinetico del gas ideale si basa sulle seguenti ipotesi:

1. il gas è costituito da un numero $N$ molto grande di molecole identiche, di massa $m$, assimilabili a **punti materiali** (il loro volume proprio è trascurabile rispetto al volume del recipiente);
2. le molecole si muovono in modo **caotico**: tutte le direzioni del moto sono equiprobabili e la distribuzione delle posizioni è uniforme nel recipiente (in assenza di campi esterni);
3. le molecole **non interagiscono** tra loro se non durante gli urti, che sono istantanei; tra un urto e l'altro si muovono di moto rettilineo uniforme (la gravità è trascurabile su scala molecolare);
4. gli urti delle molecole tra loro e con le pareti sono **perfettamente elastici**: si conservano quantità di moto ed energia cinetica;
5. valgono le leggi della meccanica newtoniana.

Per dare un'idea degli ordini di grandezza: in un metro cubo di aria in condizioni normali ci sono circa $2{,}7\times10^{25}$ molecole (numero di Loschmidt), la distanza media tra molecole vicine è circa 3 nm, cioè una decina di volte il diametro molecolare (circa 0,3 nm), e il volume proprio delle molecole è circa un millesimo del volume totale. Le velocità tipiche sono dell'ordine di centinaia di metri al secondo e ogni molecola subisce qualche miliardo di urti al secondo, percorrendo tra un urto e l'altro un **libero cammino medio** di circa 70 nm. Il numero enorme di particelle è ciò che rende sensato parlare di medie: le fluttuazioni relative delle grandezze macroscopiche scalano come $1/\sqrt{N}$ e sono quindi del tutto impercettibili. Proprio l'ipotesi degli urti tra molecole, sebbene poi trascurati nel calcolo della pressione, è essenziale perché garantisce che il gas raggiunga l'equilibrio e che la distribuzione delle velocità diventi isotropa.

### 13.2.2 Pressione

Calcoliamo la pressione esercitata dal gas su una parete. Consideriamo un recipiente cubico di lato $L$ e una parete perpendicolare all'asse $x$. Una molecola con componente della velocità $v_x > 0$ che urta elasticamente la parete inverte $v_x$, mentre $v_y$ e $v_z$ restano invariate; la variazione della sua quantità di moto è $\Delta p_x = -2 m v_x$, e per il terzo principio la parete riceve un impulso $+2 m v_x$. Dopo l'urto la molecola attraversa il cubo, rimbalza sulla parete opposta e torna dopo un tempo $\Delta t = 2L/v_x$. La forza media che una singola molecola esercita sulla parete è quindi

$$
F_1 = \frac{2 m v_x}{2L/v_x} = \frac{m v_x^2}{L}.
$$

Sommando su tutte le $N$ molecole e dividendo per l'area $L^2$:

$$
p = \frac{1}{L^3}\sum_{i=1}^{N} m v_{x,i}^2 = \frac{N m}{V}\,\langle v_x^2\rangle .
$$

Per l'isotropia del moto, $\langle v_x^2\rangle = \langle v_y^2\rangle = \langle v_z^2\rangle = \tfrac13\langle v^2\rangle$, quindi

$$
p = \frac{1}{3}\,\frac{N}{V}\,m\,\langle v^2\rangle = \frac{2}{3}\,\frac{N}{V}\,\langle E_k\rangle,
$$

dove $\langle E_k\rangle = \tfrac12 m\langle v^2\rangle$ è l'energia cinetica media di traslazione di una molecola. Questo è il risultato centrale della teoria cinetica: **la pressione è proporzionale alla densità numerica delle molecole e alla loro energia cinetica media**. Si noti che, se le molecole urtassero tra loro durante il percorso, il risultato non cambierebbe: gli urti elastici scambiano quantità di moto tra molecole, ma in media il flusso di quantità di moto verso la parete rimane lo stesso. Allo stesso modo, la forma cubica del recipiente non è essenziale; un calcolo più generale, basato sul flusso di molecole attraverso un elemento di superficie, porta alla stessa espressione. La quantità $\sqrt{\langle v^2\rangle}$ è detta **velocità quadratica media** $v_{qm}$, e la relazione si può scrivere $p = \tfrac13 \rho\, v_{qm}^2$ con $\rho$ densità di massa.

### 13.2.3 Temperatura

Confrontiamo il risultato microscopico con l'equazione di stato macroscopica $pV = Nk_BT$. Uguagliando:

$$
\frac{2}{3}\,N\,\langle E_k\rangle = N\,k_B\,T \qquad\Longrightarrow\qquad \langle E_k\rangle = \frac{1}{2}m\langle v^2\rangle = \frac{3}{2}\,k_B\,T .
$$

Questa relazione fornisce l'**interpretazione cinetica della temperatura**: la temperatura assoluta di un gas ideale è una misura dell'energia cinetica media di traslazione delle sue molecole. Lo zero assoluto corrisponde (classicamente) all'arresto del moto di traslazione; in realtà la meccanica quantistica impone un'energia residua di punto zero, ma per i gas il quadro classico è eccellente a temperature ordinarie. È notevole che l'energia cinetica media dipenda solo da $T$ e non dalla massa della molecola: a pari temperatura, molecole leggere si muovono più velocemente di molecole pesanti. La velocità quadratica media vale

$$
v_{qm} = \sqrt{\frac{3 k_B T}{m}} = \sqrt{\frac{3 R T}{M}} .
$$

Per l'azoto ($M = 0{,}028$ kg/mol) a 300 K si ottiene $v_{qm} \simeq 517$ m/s; per l'idrogeno ($M = 0{,}002$ kg/mol) circa 1930 m/s. Queste velocità sono dello stesso ordine della velocità del suono nel gas, come ci si aspetta perché il suono si propaga proprio grazie agli urti molecolari. La dipendenza da $1/\sqrt{M}$ spiega fenomeni come l'**effusione di Graham** (i gas leggeri sfuggono più rapidamente da un piccolo foro, principio usato per la separazione isotopica dell'uranio) e la perdita dell'idrogeno e dell'elio dall'atmosfera terrestre: una frazione non trascurabile delle loro molecole supera la velocità di fuga. L'interpretazione cinetica rende anche intuitivo il principio zero: due gas a contatto raggiungono l'equilibrio termico quando le energie cinetiche medie delle loro molecole si uguagliano, perché gli urti trasferiscono in media energia dalle molecole più "veloci" a quelle più "lente".

### 13.2.4 Energia interna

Per un gas ideale **monoatomico** (He, Ne, Ar) le molecole sono punti materiali senza struttura interna e non interagiscono: l'unica forma di energia è l'energia cinetica di traslazione. L'energia interna è quindi

$$
U = N\,\langle E_k\rangle = \frac{3}{2}N k_B T = \frac{3}{2}\,n R T .
$$

Ritroviamo così, da un punto di vista microscopico, il risultato dell'esperimento di Joule: l'energia interna del gas ideale dipende solo dalla temperatura e non dal volume. Il motivo profondo è l'assenza di energia potenziale di interazione: allontanare le molecole l'una dall'altra (aumentare il volume) non costa né libera energia. Per molecole **poliatomiche** la situazione è più ricca: oltre a traslare, la molecola può ruotare e le sue parti possono vibrare l'una rispetto all'altra. Ciascuno di questi moti contribuisce all'energia interna, che resta comunque funzione della sola temperatura finché le interazioni intermolecolari sono trascurabili. Per contare in modo sistematico questi contributi serve il teorema di equipartizione.

### 13.2.5 Teorema di equipartizione dell'energia

Si dice **grado di libertà** di una molecola ciascuna coordinata indipendente necessaria a descriverne la configurazione; ai fini energetici interessano i termini quadratici (in una velocità o in una coordinata) che compaiono nell'espressione dell'energia. Il **teorema di equipartizione dell'energia**, dimostrato in meccanica statistica classica, afferma che, all'equilibrio termico alla temperatura $T$, **a ogni termine quadratico indipendente nell'energia di una molecola corrisponde un'energia media pari a $\tfrac12 k_B T$**.

Per la traslazione, $E_k = \tfrac12 m v_x^2 + \tfrac12 m v_y^2 + \tfrac12 m v_z^2$: tre termini quadratici, energia media $\tfrac32 k_BT$, in accordo con quanto trovato. Una molecola **biatomica** rigida (come $\text{N}_2$, $\text{O}_2$) può inoltre ruotare attorno a due assi perpendicolari alla congiungente gli atomi; la rotazione attorno all'asse molecolare ha momento d'inerzia trascurabile e, per ragioni quantistiche, non viene eccitata. I gradi di libertà sono quindi $f = 3 + 2 = 5$. Se la molecola può anche vibrare (oscillatore armonico lungo l'asse), si aggiungono due termini quadratici, cinetico e potenziale elastico, per un totale di $f = 7$. Una molecola poliatomica non lineare rigida ha 3 gradi di traslazione e 3 di rotazione, $f = 6$. In generale l'energia interna del gas ideale è

$$
U = \frac{f}{2}\,n R T .
$$

Il teorema di equipartizione è un risultato classico, e il suo fallimento fu uno dei grandi enigmi della fisica di fine Ottocento: sperimentalmente i gradi di libertà vibrazionali delle molecole biatomiche risultano "congelati" a temperatura ambiente e si attivano solo a temperature dell'ordine di migliaia di kelvin; analogamente, a temperature bassissime anche la rotazione dell'idrogeno smette di contribuire. La spiegazione richiede la meccanica quantistica: un grado di libertà contribuisce pienamente solo se $k_BT$ è grande rispetto alla spaziatura dei suoi livelli energetici quantizzati. Le energie vibrazionali hanno spaziature di qualche decimo di elettronvolt, molto maggiori di $k_BT \simeq 0{,}026$ eV a temperatura ambiente; quelle rotazionali sono invece molto più piccole e quindi la rotazione è pienamente attiva.

### 13.2.6 Calore specifico

Dall'energia interna si ricavano immediatamente i calori specifici molari:

$$
c_V = \frac{1}{n}\frac{dU}{dT} = \frac{f}{2}R, \qquad c_p = c_V + R = \frac{f+2}{2}R, \qquad \gamma = \frac{c_p}{c_V} = \frac{f+2}{f}.
$$

Per i gas monoatomici $c_V = \tfrac32 R \simeq 12{,}5$ J/(mol K) e $\gamma = 5/3 \simeq 1{,}67$, valori in eccellente accordo con le misure su elio, neon e argon. Per i gas biatomici a temperatura ambiente $c_V = \tfrac52 R \simeq 20{,}8$ J/(mol K) e $\gamma = 7/5 = 1{,}40$, in ottimo accordo con le misure su aria, azoto e ossigeno. Per molecole poliatomiche non lineari rigide $c_V = 3R$ e $\gamma = 4/3$; nella pratica, gas come $\text{CO}_2$ o vapore acqueo mostrano valori leggermente superiori perché alcuni modi vibrazionali sono già parzialmente eccitati.

Il grafico sperimentale di $c_V/R$ in funzione di $T$ per l'idrogeno molecolare è un caso di scuola: sotto circa 80 K vale $3/2$ (solo traslazione), tra qualche centinaio e un migliaio di kelvin si stabilizza a $5/2$ (rotazione attiva), e solo sopra qualche migliaio di kelvin tende a $7/2$ (vibrazione attiva). Questa struttura "a gradini" è una prova diretta della quantizzazione dell'energia molecolare. Per i solidi, un ragionamento analogo (ogni atomo è un oscillatore tridimensionale con 6 termini quadratici) porta alla **legge di Dulong e Petit**, $c_V \simeq 3R \simeq 25$ J/(mol K), valida ad alta temperatura e anch'essa violata a bassa temperatura per ragioni quantistiche. La teoria cinetica, in definitiva, permette di prevedere proprietà termiche macroscopiche (i calori specifici) a partire dalla sola struttura geometrica delle molecole: un risultato di straordinaria potenza.

### Esercizio d'esempio

Un recipiente di volume $V = 10$ L contiene elio ($M = 4{,}00$ g/mol) a $T = 300$ K e $p = 2{,}0\times10^5$ Pa. Si calcolino: (a) il numero di molecole; (b) l'energia cinetica media di una molecola; (c) la velocità quadratica media; (d) l'energia interna del gas; (e) il calore necessario per portarlo a 400 K a volume costante.

**Soluzione.** (a) $N = pV/(k_BT) = (2{,}0\times10^5 \cdot 1{,}0\times10^{-2})/(1{,}381\times10^{-23}\cdot 300) \simeq 4{,}83\times10^{23}$, cioè $n \simeq 0{,}802$ mol.

(b) $\langle E_k\rangle = \tfrac32 k_BT = 1{,}5 \cdot 1{,}381\times10^{-23}\cdot300 \simeq 6{,}21\times10^{-21}$ J $\simeq 0{,}039$ eV.

(c) $v_{qm} = \sqrt{3RT/M} = \sqrt{3\cdot 8{,}314\cdot300/0{,}004} \simeq 1{,}37\times10^3$ m/s.

(d) Gas monoatomico: $U = \tfrac32 nRT = \tfrac32 pV = 1{,}5\cdot 2{,}0\times10^5\cdot 1{,}0\times10^{-2} = 3{,}0\times10^3$ J.

(e) $Q = n c_V \Delta T = 0{,}802 \cdot 12{,}47 \cdot 100 \simeq 1{,}0\times10^3$ J. Si noti che $U$ è proporzionale a $T$, quindi passando da 300 K a 400 K aumenta di un terzo, coerentemente con il risultato.

### Punti chiave

- La teoria cinetica modella il gas ideale come insieme di punti materiali non interagenti in moto caotico, con urti elastici.
- La pressione nasce dal trasferimento di quantità di moto alle pareti: $p = \tfrac13 \tfrac{N}{V} m\langle v^2\rangle = \tfrac23 \tfrac{N}{V}\langle E_k\rangle$.
- La temperatura misura l'energia cinetica media di traslazione: $\langle E_k\rangle = \tfrac32 k_BT$, da cui $v_{qm} = \sqrt{3RT/M}$.
- L'energia interna del gas ideale è puramente cinetica e dipende solo da $T$.
- Equipartizione: ogni termine quadratico indipendente contribuisce $\tfrac12 k_BT$; quindi $U = \tfrac{f}{2}nRT$.
- $c_V = \tfrac f2 R$, $c_p = \tfrac{f+2}{2}R$, $\gamma = (f+2)/f$: $f = 3$ monoatomico, $f = 5$ biatomico a temperatura ambiente.
- I gradi di libertà vibrazionali "congelati" mostrano i limiti del modello classico e la necessità della meccanica quantistica.

## 13.3 Gas reale

Il modello del gas ideale funziona molto bene per gas rarefatti, ma fallisce in modo evidente quando il gas è compresso o raffreddato fino ad avvicinarsi alla liquefazione. Le misure di Andrews (1869) sulle isoterme dell'anidride carbonica mostrarono che, al di sotto di una certa **temperatura critica** $T_c$ (per la $\text{CO}_2$ circa 31 °C), una compressione isoterma porta prima a un aumento di pressione, poi a un tratto orizzontale in cui gas e liquido coesistono (la pressione resta pari alla **pressione di vapore saturo**), infine a un ripidissimo aumento di pressione quando tutto il gas è liquefatto. Al di sopra di $T_c$ il gas non può essere liquefatto per sola compressione, per quanto grande sia la pressione. Nulla di tutto ciò è previsto dall'equazione $pV = nRT$, le cui isoterme sono iperboli regolari per ogni temperatura. Inoltre, anche lontano dalla liquefazione, misure accurate mostrano che il prodotto $pV$ a temperatura costante non è esattamente costante. Le cause di queste deviazioni sono due, entrambe trascurate nel modello cinetico ideale: **le molecole hanno un volume proprio finito** e **tra le molecole agiscono forze**, repulsive a cortissima distanza e attrattive (forze di van der Waals, di origine elettrica dipolare) a distanze di qualche diametro molecolare. In questa sezione vediamo due modi complementari di descrivere il gas reale: uno sistematico e generale (sviluppo del viriale), uno approssimato ma fisicamente illuminante (equazione di Van der Waals).

### 13.3.1 Sviluppo del viriale

Per quantificare la deviazione dall'idealità si introduce il **fattore di compressibilità**

$$
Z = \frac{p V_m}{R T},
$$

dove $V_m = V/n$ è il volume molare. Per un gas ideale $Z = 1$ esattamente; per un gas reale $Z$ dipende da $p$ e $T$. Quando $Z < 1$ il gas è più comprimibile del gas ideale, segno che prevalgono le forze attrattive, che "avvicinano" le molecole e riducono la pressione; quando $Z > 1$ prevalgono gli effetti repulsivi del volume proprio, che rendono il gas meno comprimibile. Un andamento tipico, per esempio per l'azoto a temperatura ambiente, mostra $Z$ che dapprima scende leggermente sotto 1 al crescere della pressione e poi risale, superando 1 a pressioni di qualche centinaio di bar.

Poiché per densità che tendono a zero ogni gas diventa ideale, è naturale sviluppare $Z$ in serie di potenze della densità molare $1/V_m$. Si ottiene lo **sviluppo del viriale** (dal latino *vis*, forza, termine introdotto da Clausius):

$$
\frac{p V_m}{R T} = 1 + \frac{B(T)}{V_m} + \frac{C(T)}{V_m^2} + \frac{D(T)}{V_m^3} + \dots
$$

I coefficienti $B(T)$, $C(T)$, ... sono detti **secondo, terzo, ... coefficiente del viriale** e dipendono solo dalla temperatura e dalla natura del gas. Equivalentemente si può sviluppare in potenze della pressione: $pV_m = RT\,(1 + B'p + C'p^2 + \dots)$, con $B' = B/(RT)$ al primo ordine.

Il grande pregio di questo sviluppo è che ha un significato microscopico preciso, ricavabile dalla meccanica statistica: il secondo coefficiente $B(T)$ descrive l'effetto delle **interazioni tra coppie** di molecole, il terzo $C(T)$ quello delle interazioni a tre corpi, e così via. A basse densità le collisioni a tre corpi sono rarissime, quindi basta il primo termine correttivo, e $B(T)$ si può calcolare integrando sul potenziale intermolecolare $u(r)$:

$$
B(T) = -2\pi N_A \int_0^\infty \left(e^{-u(r)/k_BT} - 1\right) r^2\,dr .
$$

A bassa temperatura prevale la parte attrattiva del potenziale e $B < 0$; ad alta temperatura l'energia cinetica delle molecole rende poco efficaci le attrazioni, prevale la repulsione e $B > 0$. La temperatura alla quale $B(T) = 0$ è detta **temperatura di Boyle** $T_B$: a questa temperatura il gas reale segue la legge di Boyle con ottima approssimazione in un ampio intervallo di pressioni, perché gli effetti attrattivi e repulsivi si compensano al primo ordine. Per l'azoto $T_B \simeq 327$ K, per l'elio circa 23 K, per l'anidride carbonica circa 700 K. Lo sviluppo del viriale è molto usato in ingegneria per rappresentare con precisione dati sperimentali: con due o tre coefficienti tabulati si descrive il comportamento di un gas fino a densità moderate. Non è invece adatto a descrivere la liquefazione, perché la serie diverge per densità prossime a quelle del liquido.

### 13.3.2 Equazione di Van der Waals

Nel 1873 Johannes Diderik van der Waals propose una modifica dell'equazione di stato che tiene conto, in modo semplice ma fisicamente motivato, dei due effetti trascurati dal modello ideale.

**Volume proprio.** Le molecole non sono punti ma sfere impenetrabili: ciascuna molecola ha a disposizione per muoversi non tutto il volume $V$, ma un volume ridotto $V - nb$, dove $b$ è il **covolume** molare, legato al volume escluso dalle molecole (si dimostra che vale quattro volte il volume proprio di una mole di molecole sferiche). La pressione repulsiva diventa quindi $nRT/(V - nb)$: quando il volume si avvicina a $nb$, la pressione diverge, e il gas diventa praticamente incomprimibile come un liquido.

**Forze attrattive.** Una molecola all'interno del gas è attratta in media ugualmente in tutte le direzioni, ma una molecola che sta per urtare la parete è attratta all'indietro dalle molecole retrostanti: arriva sulla parete con quantità di moto ridotta e trasferisce un impulso minore. La riduzione di pressione è proporzionale sia al numero di molecole che urtano la parete sia al numero di molecole che le attraggono, cioè al quadrato della densità: $\Delta p = a\,n^2/V^2$. Il termine $a\,n^2/V^2$ è detto **pressione interna** o **pressione di coesione**.

Combinando i due effetti si ottiene l'**equazione di Van der Waals**:

$$
\left(p + \frac{a\,n^2}{V^2}\right)(V - n b) = n R T .
$$

Le costanti $a$ e $b$ sono caratteristiche di ciascun gas e si ricavano dai dati sperimentali: per esempio, per l'azoto $a \simeq 0{,}137\ \text{Pa}\,\text{m}^6/\text{mol}^2$ e $b \simeq 3{,}87\times10^{-5}\ \text{m}^3/\text{mol}$; per l'anidride carbonica $a \simeq 0{,}364\ \text{Pa}\,\text{m}^6/\text{mol}^2$ e $b \simeq 4{,}27\times10^{-5}\ \text{m}^3/\text{mol}$. Gas con molecole fortemente polari o polarizzabili hanno valori di $a$ più grandi e si liquefanno più facilmente.

Sviluppando l'equazione per basse densità si trova il collegamento con il viriale: $Z \simeq 1 + (b - a/RT)/V_m$, quindi $B(T) = b - a/(RT)$, che cambia segno alla temperatura di Boyle $T_B = a/(Rb)$. Il modello riproduce dunque qualitativamente l'andamento osservato di $B(T)$.

Il pregio più notevole dell'equazione di Van der Waals è che, pur essendo semplice, descrive qualitativamente la transizione gas-liquido. Risolta rispetto al volume, l'equazione è **cubica** in $V$: per temperature elevate le isoterme sono monotone decrescenti e simili alle iperboli del gas ideale, mentre al di sotto di una temperatura critica presentano un massimo e un minimo, con un tratto in cui $\partial p/\partial V > 0$ che è fisicamente instabile (aumentando il volume aumenterebbe la pressione). Nella realtà questo tratto viene sostituito dal segmento orizzontale di coesistenza gas-liquido, la cui posizione si determina con la **costruzione di Maxwell** (le due aree delimitate dall'isoterma di Van der Waals sopra e sotto il segmento devono essere uguali). L'isoterma critica è quella in cui massimo e minimo si fondono in un **punto di flesso a tangente orizzontale**, il **punto critico**, caratterizzato da

$$
\left(\frac{\partial p}{\partial V}\right)_T = 0, \qquad \left(\frac{\partial^2 p}{\partial V^2}\right)_T = 0 .
$$

Risolvendo queste condizioni si ottengono le costanti critiche in funzione di $a$ e $b$:

$$
V_{m,c} = 3b, \qquad T_c = \frac{8a}{27 R b}, \qquad p_c = \frac{a}{27 b^2}, \qquad Z_c = \frac{p_c V_{m,c}}{R T_c} = \frac{3}{8} = 0{,}375 .
$$

Sperimentalmente $Z_c$ vale tipicamente tra 0,23 e 0,31, quindi l'accordo è solo qualitativo: l'equazione di Van der Waals è un modello didattico ed euristico più che uno strumento di precisione, e in ingegneria si usano equazioni di stato più raffinate (Redlich-Kwong, Peng-Robinson). Esprimendo pressione, volume e temperatura in unità dei valori critici (variabili **ridotte** $p_r = p/p_c$, $V_r = V/V_c$, $T_r = T/T_c$) l'equazione assume una forma universale, indipendente dal gas: è la **legge degli stati corrispondenti**, che afferma che gas diversi nelle stesse condizioni ridotte si comportano in modo simile. Questa legge, verificata con buona approssimazione sperimentalmente, è alla base dei diagrammi generalizzati del fattore di compressibilità usati nella progettazione di impianti.

Infine, il modello spiega l'**effetto Joule-Thomson**: in un'espansione a entalpia costante attraverso una valvola, un gas reale si raffredda se prevalgono le forze attrattive (il lavoro per allontanare le molecole è sottratto all'energia cinetica) e si riscalda se prevalgono le repulsive. È il principio dei frigoriferi e della liquefazione dei gas (processo Linde).

### Esercizio d'esempio

Una mole di anidride carbonica ($a = 0{,}364\ \text{Pa m}^6/\text{mol}^2$, $b = 4{,}27\times10^{-5}\ \text{m}^3/\text{mol}$) occupa un volume $V = 0{,}50$ L alla temperatura $T = 300$ K. Si calcoli la pressione con il modello ideale e con quello di Van der Waals, e si stimino le costanti critiche.

**Soluzione.** In SI, $V = 5{,}0\times10^{-4}$ m$^3$. Modello ideale:

$$
p_{id} = \frac{nRT}{V} = \frac{8{,}314\cdot300}{5{,}0\times10^{-4}} \simeq 4{,}99\times10^6\ \text{Pa} \simeq 49{,}9\ \text{bar}.
$$

Van der Waals:

$$
p = \frac{nRT}{V - nb} - \frac{a n^2}{V^2} = \frac{2494}{4{,}573\times10^{-4}} - \frac{0{,}364}{2{,}5\times10^{-7}} \simeq 5{,}45\times10^6 - 1{,}46\times10^6 \simeq 3{,}99\times10^6\ \text{Pa}.
$$

La pressione reale è circa il 20% inferiore a quella ideale: a questa densità prevale l'effetto attrattivo ($Z \simeq 0{,}80$). Costanti critiche: $T_c = 8a/(27Rb) = 8\cdot0{,}364/(27\cdot8{,}314\cdot4{,}27\times10^{-5}) \simeq 304$ K (valore sperimentale 304,1 K); $p_c = a/(27b^2) \simeq 0{,}364/(27\cdot1{,}82\times10^{-9}) \simeq 7{,}4\times10^6$ Pa (sperimentale 7,38 MPa); $V_{m,c} = 3b \simeq 1{,}28\times10^{-4}$ m$^3$/mol (sperimentale circa $0{,}94\times10^{-4}$, come prevedibile dal valore errato di $Z_c$). A 300 K siamo appena sotto la temperatura critica: in effetti a pressione sufficiente la $\text{CO}_2$ si liquefà a temperatura ambiente, come avviene negli estintori.

### Punti chiave

- I gas reali deviano dall'idealità per il volume proprio delle molecole e per le forze intermolecolari; le deviazioni crescono vicino alla liquefazione.
- Il fattore di compressibilità $Z = pV_m/(RT)$ misura la deviazione: $Z < 1$ indica prevalenza delle attrazioni, $Z > 1$ delle repulsioni.
- Lo sviluppo del viriale $Z = 1 + B/V_m + C/V_m^2 + \dots$ è rigoroso; $B(T)$ descrive le interazioni a coppie e si annulla alla temperatura di Boyle.
- L'equazione di Van der Waals $(p + an^2/V^2)(V - nb) = nRT$ introduce covolume $b$ e pressione di coesione $a n^2/V^2$.
- Le isoterme di Van der Waals descrivono qualitativamente la transizione di fase e il punto critico: $T_c = 8a/(27Rb)$, $p_c = a/(27b^2)$, $V_{m,c} = 3b$.
- Le variabili ridotte portano alla legge degli stati corrispondenti; l'accordo quantitativo è limitato ($Z_c = 3/8$ contro 0,23-0,31 sperimentale).

## 13.4 Trasformazioni termodinamiche

Una **trasformazione termodinamica** è il passaggio di un sistema da uno stato di equilibrio iniziale a uno finale. Se la trasformazione avviene così lentamente che il sistema attraversa una successione continua di stati di equilibrio, si dice **quasistatica**: in ogni istante pressione e temperatura sono ben definite e uniformi, e la trasformazione può essere rappresentata come una curva continua nel **piano di Clapeyron** $(V, p)$. Se inoltre non vi sono effetti dissipativi (attriti, scambi di calore con differenze finite di temperatura) la trasformazione è **reversibile**: invertendo di una quantità infinitesima le condizioni esterne, il sistema ripercorre gli stessi stati in senso opposto. Per tutte le trasformazioni di questa sezione assumiamo un gas ideale e trasformazioni quasistatiche reversibili.

Gli strumenti che useremo sono sempre gli stessi tre. Il **primo principio della termodinamica**, $\Delta U = Q - W$ (con la convenzione che $Q$ è positivo se assorbito dal gas e $W$ positivo se compiuto dal gas). Il **lavoro** di una trasformazione quasistatica, $W = \int_{V_1}^{V_2} p\,dV$, che nel piano di Clapeyron è l'area sottesa dalla curva. La variazione di **energia interna** del gas ideale, che dipende solo dagli estremi in temperatura: $\Delta U = n c_V \Delta T$. Le trasformazioni descritte sono casi particolari della **trasformazione politropica**, che le riassume tutte in un'unica famiglia.

### 13.4.1 Isobara

Una trasformazione **isobara** avviene a pressione costante. Si realizza, per esempio, con un gas in un cilindro chiuso da un pistone libero di muoversi, caricato da un peso fisso e dall'atmosfera, mentre si fornisce lentamente calore. Dall'equazione di stato, $V/T = nR/p$ è costante (legge di Charles): nel piano di Clapeyron l'isobara è un segmento orizzontale. Le grandezze energetiche sono:

$$
W = p\,(V_2 - V_1) = nR\,(T_2 - T_1), \qquad \Delta U = n c_V (T_2 - T_1), \qquad Q = n c_p (T_2 - T_1).
$$

Si verifica che $Q - W = n(c_p - R)\Delta T = n c_V \Delta T = \Delta U$, in accordo con la relazione di Mayer. Il calore scambiato in un'isobara coincide con la variazione di **entalpia** $H = U + pV$, una funzione di stato molto utile in chimica e in ingegneria dei processi a pressione atmosferica. Per un gas biatomico, il rapporto tra lavoro compiuto e calore assorbito è $W/Q = R/c_p = 2/7$: solo il 29% circa del calore fornito si trasforma in lavoro, il resto aumenta l'energia interna. L'isobara è il modello dei riscaldamenti a pressione atmosferica, della fase di combustione nel ciclo Diesel e degli scambiatori di calore nei cicli a gas.

### 13.4.2 Isocora

Una trasformazione **isocora** (o isometrica) avviene a volume costante, per esempio riscaldando un gas in un recipiente rigido. Nel piano di Clapeyron è un segmento verticale e $p/T$ è costante (legge di Gay-Lussac). Poiché il volume non cambia, il lavoro è nullo e tutto il calore scambiato modifica l'energia interna:

$$
W = 0, \qquad Q = \Delta U = n c_V (T_2 - T_1).
$$

L'isocora è il modo più "efficiente" di aumentare la temperatura di un gas con un dato calore, proprio perché nulla viene speso in lavoro: a parità di $\Delta T$, il calore richiesto è minore che in un'isobara di un fattore $c_V/c_p = 1/\gamma$. Nei cicli motore l'isocora modella la combustione rapidissima nel ciclo Otto, durante la quale il pistone praticamente non si sposta, e la fase di scarico in cui il gas cede calore all'esterno a volume costante.

### 13.4.3 Isoterma

Una trasformazione **isoterma** avviene a temperatura costante: il gas è a contatto con un **termostato** (o serbatoio di calore), cioè un corpo di capacità termica così grande che la sua temperatura non cambia scambiando calore. Nel piano di Clapeyron è un ramo di iperbole, $pV = nRT = $ costante (legge di Boyle). Poiché $T$ è costante, l'energia interna non cambia, e il calore assorbito è interamente convertito in lavoro (o viceversa):

$$
\Delta U = 0, \qquad Q = W = \int_{V_1}^{V_2} \frac{nRT}{V}\,dV = nRT\,\ln\frac{V_2}{V_1} = nRT\,\ln\frac{p_1}{p_2}.
$$

In un'espansione isoterma il gas assorbe calore dal termostato e compie lavoro positivo; in una compressione isoterma riceve lavoro e cede altrettanto calore al termostato. Questo fatto, che in un'isoterma tutto il calore diventi lavoro, non contraddice il secondo principio: il sistema non torna allo stato iniziale (ha cambiato volume), quindi non si tratta di un ciclo. Per realizzare un'isoterma reversibile la trasformazione deve essere lentissima, in modo che il calore abbia il tempo di fluire attraverso le pareti con differenze di temperatura infinitesime; per questo le compressioni reali rapide (come quelle in un compressore) sono più vicine all'adiabatica che all'isoterma. L'isoterma è la trasformazione chiave del ciclo di Carnot, di cui costituisce le fasi di scambio di calore con le sorgenti.

### 13.4.4 Adiabatica

Una trasformazione **adiabatica** avviene senza scambio di calore: $Q = 0$. Si realizza con pareti termicamente isolanti oppure, in pratica, con trasformazioni così rapide che il calore non ha il tempo di fluire (compressione nel cilindro di un motore, propagazione di un'onda sonora). Dal primo principio, $\Delta U = -W$: in un'espansione adiabatica il gas compie lavoro a spese della propria energia interna e si raffredda; in una compressione si riscalda. Lo si sperimenta gonfiando una ruota di bicicletta (la pompa si scalda) o aprendo una bomboletta di gas compresso (l'uscita si raffredda).

Ricaviamo l'equazione della curva. Per una trasformazione infinitesima reversibile $n c_V\,dT = -p\,dV$. Differenziando l'equazione di stato, $p\,dV + V\,dp = nR\,dT$, ed eliminando $dT$:

$$
c_V\,(p\,dV + V\,dp) = -R\,p\,dV \quad\Longrightarrow\quad c_p\,p\,dV + c_V\,V\,dp = 0 \quad\Longrightarrow\quad \gamma\,\frac{dV}{V} + \frac{dp}{p} = 0 .
$$

Integrando si ottengono le **equazioni di Poisson**:

$$
p\,V^{\gamma} = \text{cost}, \qquad T\,V^{\gamma-1} = \text{cost}, \qquad T^{\gamma}\,p^{1-\gamma} = \text{cost}.
$$

Poiché $\gamma > 1$, nel piano di Clapeyron le adiabatiche sono più **ripide** delle isoterme: in un'espansione la pressione diminuisce sia perché il volume aumenta sia perché la temperatura cala. Il lavoro compiuto è

$$
W = -\Delta U = n c_V (T_1 - T_2) = \frac{p_1 V_1 - p_2 V_2}{\gamma - 1}.
$$

Un esempio importante è la **velocità del suono** nei gas: le compressioni e rarefazioni di un'onda acustica sono troppo rapide per scambiare calore, quindi sono adiabatiche, e la velocità vale $v = \sqrt{\gamma p/\rho} = \sqrt{\gamma RT/M}$. Newton, che aveva supposto il processo isotermo, ottenne un valore errato di circa il 15%; la correzione di Laplace con il fattore $\gamma$ diede l'accordo con l'esperimento (circa 343 m/s nell'aria a 20 °C). Anche il gradiente adiabatico di temperatura in atmosfera (circa $-10$ K per km di quota per aria secca) nasce dall'espansione adiabatica delle masse d'aria che salgono.

### 13.4.5 Politropica

Le quattro trasformazioni precedenti sono casi particolari di una famiglia più generale: la **trasformazione politropica**, definita come una trasformazione quasistatica in cui il **calore specifico molare** $c$ del gas rimane costante. Ripetendo il ragionamento fatto per l'adiabatica, con $\delta Q = n c\,dT$ invece di $\delta Q = 0$, si trova

$$
p\,V^{k} = \text{cost}, \qquad k = \frac{c - c_p}{c - c_V},
$$

dove $k$ è l'**indice della politropica**. Al variare di $k$ si ritrovano tutti i casi notevoli:

- $k = 0$: $p$ costante, isobara ($c = c_p$);
- $k = 1$: $pV$ costante, isoterma ($c \to \infty$, perché si scambia calore senza variare la temperatura);
- $k = \gamma$: adiabatica ($c = 0$);
- $k \to \infty$: $V$ costante, isocora ($c = c_V$).

Il lavoro di una politropica con $k \neq 1$ vale

$$
W = \frac{p_1 V_1 - p_2 V_2}{k - 1} = \frac{nR\,(T_1 - T_2)}{k - 1},
$$

e il calore scambiato è $Q = n c\,(T_2 - T_1)$, con $c = c_V - R/(k-1)$. Un'osservazione interessante: per $1 < k < \gamma$ il calore specifico politropico è **negativo**, cioè il gas si raffredda pur assorbendo calore, perché il lavoro di espansione compiuto supera il calore ricevuto. Le politropiche sono molto usate in ingegneria per modellare compressioni ed espansioni reali, che non sono né perfettamente isoterme né perfettamente adiabatiche: nei compressori d'aria raffreddati, per esempio, si osservano tipicamente indici $k$ tra 1,2 e 1,35. Misurando sperimentalmente l'andamento $p(V)$ in un cilindro (diagramma indicato) e interpolandolo con una politropica si ricava l'indice effettivo, e quindi lavoro e calore scambiati. In astrofisica, infine, le politropiche descrivono la struttura delle stelle in equilibrio idrostatico.

### Esercizio d'esempio

Due moli di aria (gas biatomico, $\gamma = 1{,}40$) a $T_1 = 300$ K e $p_1 = 1{,}00\times10^5$ Pa vengono compresse fino a un volume pari a 1/10 di quello iniziale. Si confrontino il caso isotermo e il caso adiabatico: temperatura e pressione finali, lavoro e calore scambiati.

**Soluzione.** Volume iniziale: $V_1 = nRT_1/p_1 = 2\cdot8{,}314\cdot300/10^5 \simeq 4{,}99\times10^{-2}$ m$^3$; finale $V_2 \simeq 4{,}99\times10^{-3}$ m$^3$.

*Isoterma.* $T_2 = 300$ K, $p_2 = 10\,p_1 = 1{,}00\times10^6$ Pa. Lavoro:

$$
W = nRT\ln\frac{V_2}{V_1} = 2\cdot8{,}314\cdot300\cdot\ln(0{,}1) \simeq -1{,}15\times10^4\ \text{J},
$$

e $Q = W \simeq -1{,}15\times10^4$ J: il gas cede al termostato tutto il lavoro ricevuto.

*Adiabatica.* $T_2 = T_1\,(V_1/V_2)^{\gamma-1} = 300\cdot10^{0{,}4} \simeq 754$ K; $p_2 = p_1\,(V_1/V_2)^{\gamma} = 10^5\cdot10^{1{,}4} \simeq 2{,}51\times10^6$ Pa. Lavoro: $W = -n c_V (T_2 - T_1) = -2\cdot20{,}8\cdot454 \simeq -1{,}89\times10^4$ J, $Q = 0$.

La compressione adiabatica richiede più lavoro (circa il 64% in più) perché il riscaldamento del gas fa crescere la pressione più rapidamente: è per questo che nei compressori industriali si usano refrigerazioni intermedie. La temperatura di 754 K (circa 480 °C) spiega perché nel motore Diesel la sola compressione basta ad accendere il combustibile.

### Punti chiave

- Le trasformazioni quasistatiche sono successioni di stati di equilibrio, rappresentabili nel piano di Clapeyron; il lavoro è l'area sotto la curva.
- Isobara: $W = p\Delta V = nR\Delta T$, $Q = nc_p\Delta T$ (variazione di entalpia).
- Isocora: $W = 0$, $Q = \Delta U = nc_V\Delta T$.
- Isoterma: $\Delta U = 0$, $Q = W = nRT\ln(V_2/V_1)$.
- Adiabatica: $Q = 0$, $pV^\gamma$ cost., $TV^{\gamma-1}$ cost., $W = (p_1V_1 - p_2V_2)/(\gamma-1)$; è più ripida dell'isoterma.
- Politropica: $pV^k$ cost. con calore specifico costante; comprende tutte le precedenti ($k = 0, 1, \gamma, \infty$) e modella le trasformazioni reali.
