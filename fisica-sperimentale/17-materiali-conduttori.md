# Capitolo 17 — Materiali conduttori

Nel capitolo precedente abbiamo studiato il campo elettrico prodotto da distribuzioni di carica assegnate. Nei problemi reali, però, le cariche si trovano spesso su corpi conduttori, nei quali sono libere di muoversi: la loro distribuzione non è nota a priori, ma è determinata dalla condizione di equilibrio elettrostatico. In questo capitolo studiamo le proprietà dei conduttori in equilibrio, pieni e cavi, isolati o immersi in un campo esterno; ricaviamo il teorema di Coulomb sul campo in prossimità della superficie e la pressione elettrostatica; analizziamo lo schermo elettrostatico; introduciamo infine la capacità elettrica, i condensatori e l'energia immagazzinata nei sistemi di conduttori. Si tratta di argomenti centrali per l'ingegneria, dalla progettazione di componenti elettronici alla protezione di apparecchiature sensibili, fino alla sicurezza degli impianti ad alta tensione.

## 17.1 Conduttore pieno

Un **conduttore** è un materiale nel quale una parte delle cariche, i **portatori di carica liberi**, può muoversi su distanze macroscopiche sotto l'azione di un campo elettrico. In un metallo i portatori sono gli elettroni di conduzione, con densità dell'ordine di $10^{28}$–$10^{29}$ per metro cubo; il reticolo di ioni positivi resta fisso. Diciamo che un conduttore è in **equilibrio elettrostatico** quando non c'è moto macroscopico ordinato di cariche al suo interno. Dalla sola definizione di equilibrio discendono, come vedremo, tutte le proprietà fondamentali dei conduttori. Il raggiungimento dell'equilibrio è estremamente rapido: in un buon metallo i transitori di ridistribuzione della carica si esauriscono in tempi dell'ordine di $10^{-14}$–$10^{-19}$ s, per cui nelle situazioni elettrostatiche si può sempre considerare l'equilibrio già raggiunto.

### 17.1.1 Conduttore carico

La prima e fondamentale proprietà di un conduttore in equilibrio è che **il campo elettrico al suo interno è nullo**:

$$\vec{E} = 0\quad\text{all'interno del materiale conduttore}.$$

Il ragionamento è semplice: se ci fosse un campo non nullo in un punto interno, i portatori liberi presenti in quel punto subirebbero una forza $q\vec{E}$ e si metterebbero in moto, contro l'ipotesi di equilibrio. Il campo nullo è quindi una condizione necessaria per l'equilibrio, e il conduttore la realizza spontaneamente: le cariche libere si ridistribuiscono fino a produrre un campo che annulla esattamente, all'interno del materiale, ogni campo applicato.

Da questa proprietà ne discendono immediatamente altre. Poiché $\vec{E} = -\nabla V$ è nullo all'interno, il **potenziale è costante** in tutto il volume del conduttore e sulla sua superficie: il conduttore è un **volume equipotenziale**, e la sua superficie è una superficie equipotenziale. Si può quindi parlare semplicemente del "potenziale del conduttore". In secondo luogo, applicando il teorema di Gauss a una qualsiasi superficie chiusa interamente contenuta nel materiale, il flusso è nullo perché il campo è nullo ovunque sulla superficie; quindi la carica racchiusa è nulla. Poiché la superficie è arbitraria, si conclude che **la densità di carica volumica all'interno è nulla**: $\rho = 0$. In forma locale, dalla prima equazione di Maxwell, $\rho = \varepsilon_0\nabla\cdot\vec{E} = 0$.

Ne consegue che l'eventuale **carica in eccesso di un conduttore si distribuisce interamente sulla sua superficie**, con una densità superficiale $\sigma$ che in generale non è uniforme. In realtà la carica occupa uno strato di spessore dell'ordine di qualche distanza interatomica, ma su scala macroscopica è lecito considerarla come una distribuzione superficiale. La distribuzione di $\sigma$ dipende dalla forma del conduttore ed è determinata proprio dalla condizione che il campo interno sia nullo: solo per una sfera isolata la carica si distribuisce uniformemente, per simmetria.

Infine, il campo **appena fuori** dalla superficie di un conduttore è **perpendicolare alla superficie**. Infatti la superficie è equipotenziale e il campo è sempre perpendicolare alle superfici equipotenziali; equivalentemente, se ci fosse una componente tangenziale le cariche superficiali si muoverebbero lungo la superficie. Le linee di campo escono (o entrano) quindi perpendicolarmente dalla superficie dei conduttori: questo fatto, unito alla continuità della componente tangenziale del campo (sezione 16.7), è coerente con il campo interno nullo.

Un'osservazione importante riguarda la distribuzione della carica su conduttori di forma irregolare. Si trova sperimentalmente, e si giustifica con il modello delle due sfere collegate discusso più avanti, che la densità superficiale è maggiore dove la superficie è più incurvata, cioè sulle punte e sugli spigoli, e minore sulle parti piatte o concave. Questo fenomeno, noto come **potere delle punte**, ha conseguenze pratiche rilevanti che discuteremo nelle prossime sottosezioni.

### 17.1.2 Teorema di Coulomb

Il **teorema di Coulomb** collega il campo nelle immediate vicinanze della superficie di un conduttore alla densità di carica superficiale locale. Si applica il teorema di Gauss a un cilindretto di base $\Delta S$ con l'asse perpendicolare alla superficie, una base appena fuori e l'altra appena dentro il conduttore. Il flusso attraverso la base interna è nullo perché lì il campo è nullo; quello attraverso la superficie laterale è nullo perché il campo esterno è perpendicolare alla superficie e quindi parallelo alla superficie laterale (e, nella parte interna, il campo è nullo). Resta solo il flusso attraverso la base esterna, $E\,\Delta S$, che deve uguagliare $\sigma\Delta S/\varepsilon_0$:

$$\vec{E} = \frac{\sigma}{\varepsilon_0}\,\hat{n}.$$

Il campo appena fuori dalla superficie è normale a essa, uscente se $\sigma>0$ ed entrante se $\sigma<0$, e il suo modulo è proporzionale alla densità di carica locale. Il risultato è in accordo con la condizione al contorno per la componente normale ricavata nella sezione 16.7, con campo nullo da un lato.

È istruttivo confrontare il risultato con il campo di un piano carico indefinito, che vale $\sigma/(2\varepsilon_0)$: sulla superficie di un conduttore il campo è doppio. La ragione è che il campo totale è prodotto sia dalla carica dell'elementino di superficie considerato, sia da tutte le altre cariche del conduttore (ed eventuali cariche esterne). Il solo elementino, visto da vicino, si comporta come un piano carico e produce $\sigma/(2\varepsilon_0)$ da entrambi i lati, uscente da entrambe le parti; tutte le altre cariche producono, in quel punto, un campo di $\sigma/(2\varepsilon_0)$ diretto verso l'esterno. All'interno i due contributi si cancellano (dando campo nullo), all'esterno si sommano (dando $\sigma/\varepsilon_0$).

Il teorema di Coulomb permette di spiegare quantitativamente il **potere delle punte**. Consideriamo due sfere conduttrici di raggi $R_1$ e $R_2$, molto lontane fra loro e collegate da un filo conduttore sottile. Essendo collegate, formano un unico conduttore e hanno lo stesso potenziale: $Q_1/(4\pi\varepsilon_0R_1) = Q_2/(4\pi\varepsilon_0R_2)$, cioè $Q_1/R_1 = Q_2/R_2$. Le densità superficiali stanno allora nel rapporto

$$\frac{\sigma_1}{\sigma_2} = \frac{Q_1/R_1^2}{Q_2/R_2^2} = \frac{R_2}{R_1}:$$

la densità di carica, e con essa il campo superficiale, è inversamente proporzionale al raggio di curvatura. Su una punta molto acuminata il campo può raggiungere valori elevatissimi anche con potenziali moderati. Quando il campo supera la **rigidità dielettrica** dell'aria (circa $3\times10^6$ V/m in condizioni normali) gli ioni e gli elettroni liberi sempre presenti nell'aria vengono accelerati abbastanza da ionizzare altre molecole per urto, innescando una scarica: si osserva l'**effetto corona**, con una debole luminescenza e un caratteristico ronzio, o, nei casi più intensi, una scintilla. Su questo principio si basano i **parafulmini**, che favoriscono una scarica graduale e controllata verso terra, mentre negli impianti ad alta tensione e negli strumenti elettrostatici si evitano accuratamente le punte e si usano superfici arrotondate e di grande raggio per limitare le perdite per effetto corona.

### 17.1.3 Pressione elettrostatica

Le cariche sulla superficie di un conduttore sono soggette a una forza dovuta al campo prodotto da tutte le altre cariche. Come visto sopra, il campo "esterno" all'elementino, cioè quello prodotto da tutte le cariche eccetto quelle dell'elementino stesso, vale $\sigma/(2\varepsilon_0)$ ed è perpendicolare alla superficie. La forza sull'elementino di carica $\sigma\,\Delta S$ è dunque

$$\Delta\vec{F} = \sigma\Delta S\cdot\frac{\sigma}{2\varepsilon_0}\,\hat{n} = \frac{\sigma^2}{2\varepsilon_0}\Delta S\,\hat{n}.$$

Si noti che non si deve moltiplicare la carica per il campo totale $\sigma/\varepsilon_0$, perché un elemento di carica non esercita forza su se stesso: il campo da usare è la media fra quello interno (nullo) e quello esterno ($\sigma/\varepsilon_0$). La forza per unità di superficie è la **pressione elettrostatica**

$$p = \frac{\sigma^2}{2\varepsilon_0} = \frac{\varepsilon_0E^2}{2},$$

dove $E$ è il campo appena fuori dalla superficie. Essa è sempre diretta **verso l'esterno** del conduttore, indipendentemente dal segno della carica: le cariche superficiali si respingono a vicenda e tendono ad allontanarsi dal conduttore, che le trattiene grazie alle forze di legame del materiale (in un metallo, l'energia di estrazione degli elettroni).

È notevole che la pressione elettrostatica coincida numericamente con la densità di energia del campo $u = \frac12\varepsilon_0E^2$ appena fuori dalla superficie. La coincidenza non è casuale: se la superficie si sposta di $\mathrm{d}x$ verso l'esterno a carica costante, il volume occupato dal campo diminuisce di $\Delta S\,\mathrm{d}x$, e la diminuzione dell'energia del campo $u\,\Delta S\,\mathrm{d}x$ è proprio il lavoro compiuto dalla forza elettrica. Questo è un primo esempio del **metodo energetico** per calcolare le forze, che riprenderemo nella sezione 17.4.

In condizioni ordinarie la pressione elettrostatica è piccola. Con il campo massimo sopportabile dall'aria, $3\times10^6$ V/m, si ha $p = \frac12\cdot8{,}85\times10^{-12}\cdot9\times10^{12} \approx 40$ Pa, circa quattro decimillesimi della pressione atmosferica. Tuttavia i suoi effetti sono osservabili: una bolla di sapone caricata elettricamente si gonfia leggermente, e una membrana sottile carica si tende. Nei microsistemi elettromeccanici (MEMS), dove le distanze sono micrometriche e i campi possono essere molto più intensi senza innescare scariche, le forze elettrostatiche diventano dominanti e sono sfruttate per realizzare attuatori, microspecchi e accelerometri capacitivi.

### 17.1.4 Conduttore in campo esterno

Consideriamo ora un conduttore **scarico** immerso in un campo elettrico esterno $\vec{E}_0$, per esempio una sfera metallica posta fra le armature di un condensatore. Nell'istante in cui il campo viene applicato, gli elettroni liberi si muovono in verso opposto al campo e si accumulano su una parte della superficie, lasciando sulla parte opposta un eccesso di carica positiva: è l'**induzione elettrostatica** già descritta qualitativamente nella sezione 16.1. Le cariche indotte producono un campo $\vec{E}_{\text{ind}}$ che, all'interno del conduttore, si oppone al campo esterno. Il processo prosegue finché, all'interno, il campo totale è nullo:

$$\vec{E}_0+\vec{E}_{\text{ind}} = 0\quad\text{nel conduttore}.$$

La carica totale indotta è nulla (il conduttore era scarico e resta tale), ma la distribuzione superficiale non lo è. All'esterno, il campo totale è la sovrapposizione del campo esterno e del campo delle cariche indotte, e risulta deformato: le linee di campo si incurvano per arrivare perpendicolari alla superficie del conduttore, terminando sulle cariche indotte negative e ripartendo da quelle positive. Il conduttore "attira" le linee di campo verso di sé. Per una sfera di raggio $R$ in un campo uniforme $E_0$ si trova che la densità indotta è $\sigma = 3\varepsilon_0E_0\cos\theta$, dove $\theta$ è l'angolo dalla direzione del campo, e che all'esterno il campo delle cariche indotte coincide con quello di un dipolo puntiforme di momento $p = 4\pi\varepsilon_0R^3E_0$ posto al centro. Il campo sulla superficie, ai "poli", raggiunge il valore $3E_0$: anche un conduttore privo di punte intensifica localmente il campo.

Il caso del conduttore immerso in un campo esterno illustra bene il carattere "autoconsistente" dell'equilibrio elettrostatico. La distribuzione delle cariche sui conduttori non è assegnata, ma è essa stessa un'incognita del problema, determinata dalla condizione che il potenziale sia costante su ciascun conduttore. Matematicamente si tratta di risolvere l'equazione di Laplace nello spazio esterno ai conduttori con la condizione al contorno $V = \text{costante}$ sulla loro superficie, e il teorema di unicità garantisce che la soluzione sia unica. In alcuni casi particolari (piano conduttore infinito, sfera) la soluzione si trova elegantemente con il **metodo delle cariche immagine**: per esempio, una carica $q$ posta a distanza $d$ da un piano conduttore collegato a terra produce nella regione esterna lo stesso campo che produrrebbero $q$ e una carica fittizia $-q$ simmetrica rispetto al piano. Da qui si ricava che la carica è attratta dal piano con forza $q^2/(4\pi\varepsilon_0(2d)^2)$.

### 17.1.5 Conduttori a contatto

Quando due o più conduttori vengono messi a contatto (direttamente o tramite un filo conduttore), formano un **unico conduttore** e all'equilibrio devono avere lo **stesso potenziale**. Le cariche si spostano dal conduttore a potenziale più alto a quello a potenziale più basso (nel senso delle cariche positive; fisicamente sono gli elettroni a muoversi in verso opposto) finché i potenziali non si uguagliano. La carica totale si conserva, ma la sua ripartizione dipende dalla geometria.

Per due sfere di raggi $R_1$ e $R_2$, lontane fra loro e collegate da un filo sottile, con carica totale $Q$, le condizioni sono $Q_1+Q_2 = Q$ e $Q_1/R_1 = Q_2/R_2$, da cui

$$Q_1 = Q\,\frac{R_1}{R_1+R_2},\qquad Q_2 = Q\,\frac{R_2}{R_1+R_2}.$$

La sfera più grande prende la carica maggiore, ma ha la densità superficiale minore. Questo risultato giustifica ciò che abbiamo detto sul contatto fra sfere identiche (ripartizione a metà) e sul potere delle punte.

Un caso limite importante è il **collegamento a terra**. La Terra è un conduttore di raggio enorme ($R_T \approx 6{,}4\times10^6$ m); collegando a essa un conduttore di dimensioni ordinarie, praticamente tutta la carica fluisce verso la Terra, il cui potenziale non cambia apprezzabilmente. Per convenzione si attribuisce potenziale nullo alla Terra, che diventa il riferimento rispetto al quale si misurano i potenziali dei conduttori. Collegare a terra un conduttore significa quindi imporne il potenziale a zero, non necessariamente scaricarlo: se nelle vicinanze ci sono altre cariche, sul conduttore collegato a terra rimane una carica indotta, come abbiamo visto nell'elettrizzazione per induzione.

Il principio di equipotenzialità dei conduttori collegati ha conseguenze pratiche rilevanti per la sicurezza. Negli impianti elettrici le parti metalliche accessibili degli apparecchi (carcasse di lavatrici, frigoriferi, quadri) sono collegate a terra tramite il conduttore di protezione: in caso di guasto dell'isolamento la carcassa non può assumere un potenziale pericoloso rispetto al pavimento su cui si trova l'utente. Allo stesso modo, nelle industrie che maneggiano polveri o vapori infiammabili, i serbatoi e le tubazioni vengono collegati fra loro e a terra (**collegamento equipotenziale**) per evitare che l'accumulo di cariche per strofinio produca scintille.

### Esercizio d'esempio

Una sfera conduttrice di raggio $R_1 = 10$ cm porta una carica $Q = 40$ nC. Viene collegata con un filo sottile a una seconda sfera conduttrice, inizialmente scarica, di raggio $R_2 = 2{,}0$ cm, posta a grande distanza. Calcolare: le cariche finali, il potenziale comune, il campo sulla superficie di ciascuna sfera e la pressione elettrostatica sulla sfera piccola.

**Soluzione.** Ripartizione: $Q_1 = Q\,R_1/(R_1+R_2) = 40\cdot10/12 \approx 33{,}3$ nC e $Q_2 = 40\cdot2/12 \approx 6{,}7$ nC.

Potenziale comune:

$$V = \frac{Q_1}{4\pi\varepsilon_0R_1} = 8{,}99\times10^9\cdot\frac{33{,}3\times10^{-9}}{0{,}10} \approx 3{,}0\times10^{3}\ \text{V}.$$

Campi superficiali (per una sfera $E = V/R$): $E_1 = 3{,}0\times10^3/0{,}10 = 3{,}0\times10^4$ V/m; $E_2 = 3{,}0\times10^3/0{,}020 = 1{,}5\times10^5$ V/m. Il rapporto $E_2/E_1 = R_1/R_2 = 5$, come previsto.

Pressione sulla sfera piccola:

$$p_2 = \tfrac12\varepsilon_0E_2^2 = \tfrac12\cdot8{,}85\times10^{-12}\cdot(1{,}5\times10^5)^2 \approx 0{,}10\ \text{Pa}.$$

Entrambi i campi sono ampiamente sotto la rigidità dielettrica dell'aria, quindi non si hanno scariche.

### Punti chiave

- In un conduttore in equilibrio il campo interno è nullo e il conduttore è un volume equipotenziale.
- La carica in eccesso risiede sulla superficie; la densità volumica interna è nulla.
- Appena fuori dalla superficie il campo è normale e vale $\sigma/\varepsilon_0$ (teorema di Coulomb).
- La densità di carica è maggiore dove il raggio di curvatura è minore: potere delle punte, effetto corona, parafulmini.
- La pressione elettrostatica $p = \sigma^2/(2\varepsilon_0) = \frac12\varepsilon_0E^2$ è sempre uscente.
- In un campo esterno, le cariche indotte annullano il campo interno e deformano le linee di campo, che arrivano perpendicolari alla superficie.
- Conduttori a contatto raggiungono lo stesso potenziale; il collegamento a terra fissa il potenziale a zero.

## 17.2 Conduttore cavo

Un **conduttore cavo** è un corpo conduttore che racchiude al suo interno una o più cavità vuote (o riempite di materiale isolante), completamente circondate dal materiale conduttore. Lo studio di questa configurazione porta a uno dei risultati più importanti e applicativi dell'elettrostatica: lo **schermo elettrostatico**, cioè la possibilità di isolare completamente una regione di spazio dai campi elettrici esterni, e viceversa di confinare i campi prodotti all'interno. Il principio, scoperto sperimentalmente da Faraday con la celebre "gabbia" in cui si chiuse mentre l'esterno veniva caricato ad alta tensione, è alla base di numerosissime applicazioni: cavi coassiali, involucri metallici dei dispositivi elettronici, cabine di misura schermate, protezione degli occupanti di automobili e aerei colpiti da fulmini.

### 17.2.1 Conduttore carico

Consideriamo un conduttore cavo, carico con carica $Q$, all'interno della cui cavità **non ci sono cariche**. Ci chiediamo dove si trovi la carica e quale sia il campo nella cavità.

Prendiamo una superficie gaussiana interamente contenuta nel materiale conduttore che circondi la cavità. Su di essa il campo è nullo, quindi il flusso è nullo e la carica totale racchiusa è nulla. Poiché nella cavità non ci sono cariche, la carica totale sulla **superficie interna** del conduttore (quella che delimita la cavità) è zero. Questo però non basta a escludere che sulla superficie interna ci siano zone di carica positiva e zone di carica negativa con somma nulla. Per escluderlo si usa la conservatività: se esistessero tali zone, ci sarebbero linee di campo che partono dalle cariche positive della parete interna, attraversano la cavità e terminano sulle cariche negative della stessa parete. Calcoliamo la circuitazione del campo lungo un percorso chiuso che segue una di queste linee nella cavità e si richiude attraverso il materiale conduttore: il contributo nel conduttore è nullo (campo nullo), quello lungo la linea di campo è strettamente positivo (il campo è parallelo allo spostamento). La circuitazione sarebbe quindi diversa da zero, contro la conservatività del campo elettrostatico. Equivalentemente, la linea partirebbe e arriverebbe su punti dello stesso conduttore, quindi allo stesso potenziale, ma lungo una linea di campo il potenziale decresce strettamente.

Si conclude che, in assenza di cariche nella cavità:

- la **densità di carica sulla superficie interna è nulla ovunque**;
- il **campo nella cavità è nullo** e il potenziale nella cavità è costante e uguale a quello del conduttore;
- tutta la carica $Q$ si trova sulla **superficie esterna**.

Dal punto di vista matematico il risultato discende anche dal teorema di unicità: nella cavità il potenziale soddisfa l'equazione di Laplace con condizione al contorno $V = V_0$ costante sulla parete; la funzione costante $V = V_0$ è una soluzione, e per l'unicità è l'unica. In particolare il campo nella cavità è nullo indipendentemente dalla forma della cavità e del conduttore.

Questo risultato ha una verifica sperimentale classica, l'**esperimento del pozzo di ghiaccio** di Faraday e la cosiddetta prova del cilindro di Faraday: toccando con una sferetta di prova la parete interna di un recipiente metallico carico, la sferetta non preleva carica; toccando la parete esterna, sì. Viceversa, inserendo una sferetta carica in un contenitore metallico e toccando la parete interna, la sferetta cede completamente la sua carica al contenitore, qualunque sia la carica già presente su quest'ultimo: è il principio del **generatore di Van de Graaff**, in cui un nastro isolante porta continuamente carica all'interno di una grande sfera cava, dove viene trasferita alla sfera stessa raggiungendo potenziali di milioni di volt. È anche il motivo per cui, come già notato nella sezione 16.4, la verifica del campo nullo all'interno di un conduttore cavo carico costituisce un test di altissima precisione della legge dell'inverso del quadrato.

### 17.2.2 Carica nella cavità

Supponiamo ora che nella cavità sia presente una carica $q$, isolata dalle pareti, e che il conduttore abbia una carica propria $Q$. Una superficie gaussiana nel materiale conduttore che racchiuda la cavità ha flusso nullo, quindi la carica totale racchiusa è nulla: sulla superficie interna deve trovarsi una carica indotta

$$q_{\text{int}} = -q.$$

La carica $-q$ si distribuisce sulla parete della cavità in modo da annullare, nel materiale conduttore e nello spazio esterno, il campo prodotto da $q$; la distribuzione dipende dalla posizione di $q$ nella cavità e dalla forma di quest'ultima. Le linee di campo partono da $q$ e terminano tutte sulla parete interna: è l'**induzione completa**, così detta perché tutte le linee di campo uscenti dalla carica inducente terminano sul conduttore indotto. Per la conservazione della carica, sulla superficie esterna si trova la carica

$$q_{\text{est}} = Q+q.$$

L'aspetto più notevole è che la distribuzione della carica sulla **superficie esterna non dipende dalla posizione di $q$ all'interno** della cavità. Il campo esterno è determinato dalla carica $Q+q$ e dalla forma della superficie esterna (e dalle eventuali cariche esterne), ma non da ciò che accade dentro: spostando la carica nella cavità, la distribuzione interna cambia, quella esterna no. Questo si dimostra ancora una volta con il teorema di unicità applicato alla regione esterna: il potenziale soddisfa l'equazione di Laplace, è nullo all'infinito, è costante sulla superficie esterna del conduttore e il flusso attraverso di essa è fissato dalla carica $Q+q$; tali condizioni determinano univocamente la soluzione.

Un'importante conseguenza riguarda il collegamento a terra. Se il conduttore cavo è collegato a terra, il suo potenziale è nullo e la carica sulla superficie esterna, in assenza di cariche esterne, è nulla: tutto il campo prodotto da $q$ resta confinato all'interno della cavità. Il conduttore cavo collegato a terra realizza dunque uno **schermo perfetto verso l'esterno**: dall'esterno è impossibile rilevare con misure elettrostatiche la presenza e la posizione delle cariche interne. È così che si progettano gli involucri metallici di apparecchiature che generano campi elettrici intensi, per evitare di disturbare dispositivi vicini. Si noti che, se il conduttore non fosse collegato a terra, la carica $Q+q$ sulla superficie esterna segnalerebbe all'esterno la presenza della carica interna, pur nascondendone la posizione.

### 17.2.3 Conduttore in campo esterno

Consideriamo infine un conduttore cavo, senza cariche nella cavità, immerso in un campo esterno prodotto da cariche lontane. Come nel caso del conduttore pieno, sulla superficie esterna compaiono cariche indotte che annullano il campo nel materiale conduttore. Ma anche nella cavità il campo è nullo: il ragionamento della sottosezione 17.2.1 non dipende in alcun modo da ciò che accade all'esterno, perché utilizza solo il fatto che la parete della cavità sia equipotenziale e che nella cavità non vi siano cariche. Dunque:

$$\vec{E} = 0\ \text{nella cavità, qualunque sia il campo esterno}.$$

Il conduttore cavo protegge la cavità da qualsiasi campo elettrostatico esterno: questo è lo **schermo elettrostatico** o **gabbia di Faraday**. Le cariche indotte sulla superficie esterna si distribuiscono esattamente in modo da annullare all'interno del conduttore, e quindi anche della cavità, il contributo delle cariche esterne. Combinando con il risultato precedente, si ottiene un disaccoppiamento completo: un conduttore cavo collegato a terra separa lo spazio in due regioni elettrostaticamente indipendenti, in cui le cariche dell'una non producono effetti nell'altra.

Nella pratica non occorre che lo schermo sia un involucro continuo: anche una rete metallica a maglie fitte funziona bene, purché le dimensioni delle maglie siano piccole rispetto alla distanza dalle regioni da proteggere. I campi che "penetrano" attraverso le aperture decadono rapidamente, su distanze dell'ordine della dimensione della maglia. Per questo la carrozzeria di un'automobile o la fusoliera di un aereo proteggono efficacemente gli occupanti dai fulmini: la scarica percorre l'involucro metallico esterno senza produrre campi significativi all'interno. La stessa idea è usata nei forni a microonde, dove la griglia metallica sulla porta ha fori di pochi millimetri, molto più piccoli della lunghezza d'onda di circa 12 cm, e impedisce alla radiazione di uscire. Va sottolineato che, per campi variabili nel tempo, l'efficacia dello schermo dipende anche dalla frequenza e dalla conducibilità del materiale (effetto pelle), argomento che esula dall'elettrostatica.

Un'applicazione fondamentale in ingegneria è il **cavo coassiale**, costituito da un conduttore centrale circondato da una calza metallica collegata a terra, separati da un isolante. La calza schermante impedisce che campi esterni disturbino il segnale trasportato dal conduttore interno e, simmetricamente, che il segnale irradi verso l'esterno. Allo stesso modo i circuiti di misura sensibili (per esempio gli amplificatori per elettrodi biomedici) vengono racchiusi in contenitori metallici, e le misure di precisione si effettuano in stanze schermate. Anche il nostro corpo, toccando lo schermo di un dispositivo collegato a terra, non ne altera il funzionamento interno.

### Esercizio d'esempio

Un guscio sferico conduttore ha raggio interno $a = 4{,}0$ cm e raggio esterno $b = 5{,}0$ cm e porta una carica propria $Q = +6{,}0$ nC. Al centro della cavità è posta una carica puntiforme $q = -2{,}0$ nC. Determinare le cariche sulle due superfici del guscio, il campo a $r = 2{,}0$ cm, $r = 4{,}5$ cm e $r = 10$ cm, e il potenziale del guscio.

**Soluzione.** Superficie interna: $q_{\text{int}} = -q = +2{,}0$ nC. Superficie esterna: $q_{\text{est}} = Q+q = 6{,}0-2{,}0 = +4{,}0$ nC. Per simmetria entrambe sono distribuite uniformemente.

- $r = 2{,}0$ cm (cavità): racchiusa solo $q$. $E = k|q|/r^2 = 8{,}99\times10^9\cdot2{,}0\times10^{-9}/(0{,}020)^2 \approx 4{,}5\times10^{4}$ N/C, diretto verso il centro (carica negativa).
- $r = 4{,}5$ cm (nel metallo): $E = 0$. Verifica: carica racchiusa $q+q_{\text{int}} = 0$.
- $r = 10$ cm: racchiusa $q+Q = 4{,}0$ nC. $E = 8{,}99\times10^9\cdot4{,}0\times10^{-9}/(0{,}10)^2 \approx 3{,}6\times10^{3}$ N/C, uscente.

Potenziale del guscio (uguale a quello della superficie esterna, che all'esterno si comporta come una carica puntiforme di $4{,}0$ nC):

$$V = \frac{q+Q}{4\pi\varepsilon_0b} = 8{,}99\times10^9\cdot\frac{4{,}0\times10^{-9}}{0{,}050} \approx 7{,}2\times10^{2}\ \text{V}.$$

Se si spostasse la carica $q$ fuori dal centro, la distribuzione interna cambierebbe, ma i risultati per $r>b$ e il potenziale del guscio resterebbero identici.

### Punti chiave

- In un conduttore cavo senza cariche nella cavità, il campo nella cavità è nullo e la superficie interna è scarica.
- Tutta la carica propria di un conduttore cavo, in assenza di cariche interne, risiede sulla superficie esterna.
- Con una carica $q$ nella cavità, sulla parete interna si induce $-q$ (induzione completa) e sulla superficie esterna compare $Q+q$.
- La distribuzione sulla superficie esterna non dipende dalla posizione delle cariche nella cavità.
- Il conduttore cavo collegato a terra isola completamente le due regioni: schermo elettrostatico (gabbia di Faraday).
- Una rete metallica a maglie fitte scherma lo spazio interno quasi come un involucro continuo.
- Applicazioni: cavo coassiale, involucri di strumenti, generatore di Van de Graaff, protezione da fulmini.

## 17.3 Capacità elettrica

Abbiamo visto che un conduttore isolato in equilibrio ha un potenziale ben definito e che la sua carica si distribuisce sulla superficie in modo determinato dalla geometria. Sorge spontanea la domanda: quale relazione lega la carica posseduta da un conduttore al suo potenziale? La risposta conduce al concetto di **capacità elettrica**, una grandezza che dipende solo dalla geometria dei conduttori (e dal mezzo che li circonda) e che quantifica l'attitudine di un sistema ad accumulare carica a parità di potenziale. Il dispositivo progettato per sfruttare questa proprietà è il **condensatore**, uno dei componenti fondamentali dell'elettronica e dell'elettrotecnica.

### 17.3.1 Capacità di un conduttore isolato

Consideriamo un conduttore isolato, lontano da altri corpi, con carica $Q$ e potenziale $V$ (riferito all'infinito). Se raddoppiamo la carica, per il principio di sovrapposizione la nuova distribuzione superficiale è semplicemente il doppio della precedente: infatti la distribuzione $2\sigma$ produce un campo doppio, che resta nullo all'interno del conduttore e perpendicolare alla superficie, quindi soddisfa le condizioni di equilibrio, e per il teorema di unicità è quella corretta. Di conseguenza anche il potenziale raddoppia. La carica e il potenziale sono dunque proporzionali, e si definisce la **capacità** del conduttore isolato come il rapporto costante

$$C = \frac{Q}{V}.$$

La capacità dipende solo dalla forma e dalle dimensioni del conduttore (e, come vedremo nel capitolo sui dielettrici, dal mezzo in cui è immerso), non dalla carica né dal potenziale. Nel SI si misura in **farad** (F), con $1\ \text{F} = 1\ \text{C/V}$. Come vedremo, si tratta di un'unità molto grande: nelle applicazioni si usano tipicamente microfarad ($\mu$F), nanofarad (nF) e picofarad (pF). Dalla definizione segue anche che $\varepsilon_0$ si può esprimere in F/m, unità di misura più comune di quella vista nel capitolo precedente.

Per una **sfera conduttrice** isolata di raggio $R$ il potenziale è $V = Q/(4\pi\varepsilon_0R)$, quindi

$$C_{\text{sfera}} = 4\pi\varepsilon_0R.$$

La capacità cresce linearmente con le dimensioni. Una sfera di raggio 1 m ha una capacità di circa 111 pF; per avere una capacità di 1 F servirebbe una sfera di raggio $9\times10^9$ m, oltre mille volte il raggio terrestre. La Terra stessa, considerata come sfera conduttrice isolata, ha una capacità di circa 710 $\mu$F. Questi numeri mostrano quanto sia inefficiente un conduttore isolato come "serbatoio" di carica, e spiegano perché per ottenere capacità elevate si ricorra ai condensatori.

### 17.3.2 Condensatori

Un **condensatore** è un sistema di due conduttori, detti **armature**, disposti in modo che fra di essi vi sia **induzione completa**: tutte le linee di campo che partono da un'armatura terminano sull'altra. In tal caso, se un'armatura porta carica $+Q$, l'altra porta necessariamente carica $-Q$ sulla superficie affacciata. La condizione è realizzata esattamente quando un'armatura racchiude completamente l'altra (condensatore sferico, cilindrico indefinito), e con ottima approssimazione quando le armature sono vicine rispetto alle loro dimensioni (condensatore piano). La **capacità del condensatore** è definita come

$$C = \frac{Q}{\Delta V},$$

dove $Q$ è il modulo della carica su ciascuna armatura e $\Delta V = V_+-V_-$ la differenza di potenziale fra le armature. Anche qui il rapporto dipende solo dalla geometria. Il vantaggio rispetto al conduttore isolato è enorme: la presenza dell'armatura opposta, vicina, riduce drasticamente la differenza di potenziale necessaria per accumulare una data carica, perché il campo resta confinato nello spazio fra le armature.

**Condensatore piano.** Due lastre conduttrici parallele di area $S$ a distanza $d$ con $d\ll\sqrt{S}$. Trascurando gli effetti di bordo, la carica si distribuisce uniformemente sulle facce affacciate con densità $\pm\sigma = \pm Q/S$, e il campo fra le armature è uniforme, di modulo $E = \sigma/\varepsilon_0$ (sovrapposizione dei campi $\sigma/(2\varepsilon_0)$ delle due lastre, che si sommano fra le armature e si cancellano all'esterno; oppure teorema di Coulomb). La differenza di potenziale è $\Delta V = Ed = Qd/(\varepsilon_0S)$, e quindi

$$C_{\text{piano}} = \frac{\varepsilon_0S}{d}.$$

Con $S = 1$ m² e $d = 1$ mm si ottiene $C \approx 8{,}85$ nF: ancora piccola, nonostante l'area considerevole. Per aumentare la capacità si riduce la distanza, si aumenta l'area (avvolgendo lunghi nastri metallici sottili separati da un isolante) e si interpone un dielettrico con costante dielettrica elevata.

**Condensatore sferico.** Due sfere conduttrici concentriche di raggi $R_1<R_2$. Fra le armature il campo è quello di una carica puntiforme $Q$, $E = Q/(4\pi\varepsilon_0r^2)$, e integrando da $R_1$ a $R_2$:

$$\Delta V = \frac{Q}{4\pi\varepsilon_0}\left(\frac{1}{R_1}-\frac{1}{R_2}\right)\ \Rightarrow\ C_{\text{sferico}} = 4\pi\varepsilon_0\frac{R_1R_2}{R_2-R_1}.$$

Per $R_2\to\infty$ si ritrova la capacità della sfera isolata; per $R_2-R_1 = d\ll R_1$ si ottiene $C\approx4\pi\varepsilon_0R_1^2/d = \varepsilon_0S/d$, la capacità del condensatore piano, come ci si aspetta localmente.

**Condensatore cilindrico.** Due cilindri coassiali di raggi $R_1<R_2$ e lunghezza $L\gg R_2$ (è la geometria del cavo coassiale). Fra le armature $E = \lambda/(2\pi\varepsilon_0r)$ con $\lambda = Q/L$, da cui $\Delta V = \frac{\lambda}{2\pi\varepsilon_0}\ln(R_2/R_1)$ e

$$C_{\text{cilindrico}} = \frac{2\pi\varepsilon_0L}{\ln(R_2/R_1)}.$$

La capacità per unità di lunghezza di un cavo coassiale è un parametro fondamentale per la trasmissione di segnali: i cavi commerciali hanno valori tipici di 50–100 pF/m.

### 17.3.3 Collegamenti di condensatori

Nei circuiti i condensatori vengono spesso collegati fra loro; è utile sapere sostituire una combinazione con un unico **condensatore equivalente**.

**Collegamento in parallelo.** Le armature corrispondenti sono collegate fra loro, quindi tutti i condensatori hanno la stessa differenza di potenziale $\Delta V$. La carica totale è la somma delle cariche: $Q = \sum_iC_i\Delta V$. La capacità equivalente è

$$C_{\text{eq}} = \sum_iC_i.$$

Il collegamento in parallelo equivale ad aumentare l'area delle armature: la capacità equivalente è maggiore della più grande delle capacità.

**Collegamento in serie.** I condensatori sono collegati uno dopo l'altro, l'armatura negativa di ciascuno con la positiva del successivo. Le armature intermedie, collegate fra loro e isolate dal resto, formano conduttori inizialmente scarichi; per induzione ogni condensatore porta la stessa carica $Q$. Le differenze di potenziale si sommano: $\Delta V = \sum_iQ/C_i$. Quindi

$$\frac{1}{C_{\text{eq}}} = \sum_i\frac{1}{C_i}.$$

La capacità equivalente è minore della più piccola delle capacità. Il collegamento in serie è utile per ripartire una tensione elevata su più condensatori, ciascuno dei quali sopporta solo una parte di essa: la differenza di potenziale su ciascuno è inversamente proporzionale alla sua capacità.

È importante ricordare che i condensatori reali hanno una **tensione massima di lavoro**: oltre un certo campo il dielettrico fra le armature perde le sue proprietà isolanti (scarica, perforazione). Nella scelta di un condensatore occorre considerare sia la capacità sia questa tensione nominale, che è legata alla rigidità dielettrica del materiale e alla distanza fra le armature.

### 17.3.4 Sistemi di conduttori e coefficienti di capacità

Nel caso più generale, quando sono presenti $N$ conduttori nello spazio, non c'è induzione completa e la carica di ciascun conduttore dipende dai potenziali di tutti. Per il principio di sovrapposizione e per il teorema di unicità, la relazione fra cariche e potenziali è lineare:

$$Q_i = \sum_{j=1}^NC_{ij}V_j.$$

I coefficienti $C_{ii}$ sono detti **coefficienti di capacità** e sono positivi; i coefficienti $C_{ij}$ con $i\ne j$ sono detti **coefficienti di induzione** e sono negativi o nulli (portando un conduttore a potenziale positivo con tutti gli altri a terra, sugli altri si induce carica negativa). Si dimostra inoltre che la matrice è simmetrica, $C_{ij} = C_{ji}$, proprietà che discende dalla conservazione dell'energia ed è nota come **teorema di reciprocità** di Green. I coefficienti dipendono solo dalla geometria dell'insieme dei conduttori.

Questa descrizione è importante nell'elettronica moderna, dove si parla di **capacità parassite**: in un circuito integrato ogni pista conduttrice forma con le piste vicine e con il substrato un sistema di conduttori, e le capacità mutue fra di esse (dell'ordine dei femtofarad) limitano la velocità di commutazione e causano accoppiamenti indesiderati fra segnali (diafonia). Le stesse capacità mutue, d'altra parte, sono sfruttate negli **schermi tattili capacitivi**: il dito, conduttore collegato a terra attraverso il corpo, modifica i coefficienti di capacità fra gli elettrodi trasparenti dello schermo, e il circuito di controllo rileva la variazione per individuare il punto di contatto. Altri sensori capacitivi misurano spostamenti, livelli di liquidi, umidità e pressione sfruttando la dipendenza della capacità dalla geometria e dal materiale interposto.

### Esercizio d'esempio

Tre condensatori, $C_1 = 2{,}0\ \mu\text{F}$, $C_2 = 3{,}0\ \mu\text{F}$ e $C_3 = 6{,}0\ \mu\text{F}$, sono collegati così: $C_2$ e $C_3$ in serie fra loro, e questa coppia in parallelo con $C_1$. Al sistema è applicata una differenza di potenziale $\Delta V = 12$ V. Calcolare la capacità equivalente, la carica su ciascun condensatore e la tensione ai capi di $C_2$ e $C_3$. Infine, stimare l'area di un condensatore piano in aria con $d = 0{,}10$ mm che abbia la stessa capacità di $C_1$.

**Soluzione.** Serie $C_2$–$C_3$: $1/C_{23} = 1/3{,}0+1/6{,}0 = 1/2{,}0$, quindi $C_{23} = 2{,}0\ \mu$F. Parallelo con $C_1$: $C_{\text{eq}} = 2{,}0+2{,}0 = 4{,}0\ \mu$F.

Carica su $C_1$: $Q_1 = C_1\Delta V = 2{,}0\times10^{-6}\cdot12 = 24\ \mu$C. Carica sul ramo serie: $Q_{23} = C_{23}\Delta V = 24\ \mu$C, uguale su $C_2$ e su $C_3$. Carica totale fornita: $48\ \mu$C $= C_{\text{eq}}\Delta V$.

Tensioni: $\Delta V_2 = Q_{23}/C_2 = 24/3{,}0 = 8{,}0$ V; $\Delta V_3 = 24/6{,}0 = 4{,}0$ V; somma 12 V, come deve essere.

Area equivalente a $C_1$: $S = C_1d/\varepsilon_0 = 2{,}0\times10^{-6}\cdot1{,}0\times10^{-4}/8{,}85\times10^{-12} \approx 23\ \text{m}^2$. Il risultato spiega perché i condensatori reali usano dielettrici ad alta permittività e armature arrotolate.

### Punti chiave

- La capacità di un conduttore isolato è $C = Q/V$ e dipende solo dalla geometria; si misura in farad (F = C/V).
- Sfera isolata: $C = 4\pi\varepsilon_0R$; il farad è un'unità molto grande.
- Un condensatore è una coppia di conduttori in induzione completa: $C = Q/\Delta V$.
- Piano: $C = \varepsilon_0S/d$; sferico: $C = 4\pi\varepsilon_0R_1R_2/(R_2-R_1)$; cilindrico: $C = 2\pi\varepsilon_0L/\ln(R_2/R_1)$.
- In parallelo le capacità si sommano; in serie si sommano i reciproci.
- In serie la carica è la stessa su tutti i condensatori; in parallelo è la stessa la tensione.
- Per più conduttori $Q_i = \sum_jC_{ij}V_j$, con matrice simmetrica; da qui le capacità parassite e i sensori capacitivi.

## 17.4 Energia elettrostatica

Caricare un conduttore o un condensatore richiede lavoro: occorre portare cariche verso un corpo che, man mano che si carica, le respinge sempre più. Questo lavoro non va perduto, ma resta immagazzinato nel sistema sotto forma di **energia elettrostatica**, che può essere restituita in seguito, per esempio quando il condensatore si scarica attraverso un circuito. In questa sezione calcoliamo l'energia di un conduttore carico e di un condensatore, mostriamo che essa può essere attribuita al campo elettrico con densità $\frac12\varepsilon_0E^2$, e utilizziamo il principio dei lavori virtuali per ricavare le forze fra conduttori.

### 17.4.1 Energia di un conduttore carico

Consideriamo un conduttore isolato di capacità $C$ e calcoliamo il lavoro necessario per caricarlo dalla carica nulla alla carica finale $Q$, portando piccole quantità di carica $\mathrm{d}q$ dall'infinito (dove il potenziale è nullo). Quando il conduttore porta la carica $q$, il suo potenziale è $v = q/C$; il lavoro per portare la carica $\mathrm{d}q$ dall'infinito alla superficie del conduttore è $\mathrm{d}W = v\,\mathrm{d}q = (q/C)\,\mathrm{d}q$. Integrando:

$$U = \int_0^Q\frac{q}{C}\,\mathrm{d}q = \frac{Q^2}{2C} = \frac12QV = \frac12CV^2.$$

Le tre forme sono equivalenti grazie a $Q = CV$. Il fattore $\frac12$ ha un'origine chiara: la carica viene portata a un potenziale che cresce linearmente da zero a $V$, quindi il lavoro medio per unità di carica è $V/2$. Lo stesso risultato si ottiene dalla formula generale $U = \frac12\int\sigma V\,\mathrm{d}S$ della sezione 16.5, osservando che sul conduttore $V$ è costante e si può portare fuori dall'integrale: $U = \frac12V\int\sigma\,\mathrm{d}S = \frac12QV$.

Per un sistema di più conduttori con cariche $Q_i$ e potenziali $V_i$ la generalizzazione è immediata:

$$U = \frac12\sum_iQ_iV_i.$$

Per una sfera di raggio $R$ si ha $U = Q^2/(8\pi\varepsilon_0R)$: a parità di carica, l'energia è tanto maggiore quanto più la sfera è piccola. Si noti la differenza con la sfera uniformemente carica in volume, per la quale il coefficiente è $3/5$ invece di $1/2$: nella sfera conduttrice tutta la carica è sulla superficie e non c'è campo interno, quindi manca il contributo dell'energia interna. Poiché un sistema fisico tende a portarsi nella configurazione di minima energia compatibile con i vincoli, si può verificare che la distribuzione superficiale delle cariche su un conduttore è proprio quella che, a carica totale fissata, rende minima l'energia elettrostatica (**teorema di Thomson**).

### 17.4.2 Energia di un condensatore

Per un condensatore si ragiona analogamente: caricarlo significa trasferire carica da un'armatura all'altra (è quanto fa un generatore collegato alle armature). Quando sulle armature ci sono le cariche $\pm q$, la differenza di potenziale è $q/C$, e il lavoro per trasferire un'ulteriore carica $\mathrm{d}q$ dall'armatura negativa a quella positiva è $(q/C)\,\mathrm{d}q$. Integrando:

$$U = \frac{Q^2}{2C} = \frac12Q\,\Delta V = \frac12C\,\Delta V^2.$$

Questa energia è quella che il condensatore restituisce quando viene scaricato, per esempio attraverso un resistore (dove si trasforma in calore per effetto Joule) o una lampada flash (dove si trasforma in luce). I condensatori sono usati come serbatoi di energia ogni volta che serve rilasciarla in tempi molto brevi con potenze elevate: flash fotografici, defibrillatori cardiaci, laser impulsati, sistemi di fusione a confinamento inerziale, sistemi di partenza dei motori. Negli ultimi decenni i **supercondensatori**, con capacità di migliaia di farad ottenute grazie a elettrodi porosi di enorme superficie specifica e a distanze fra le cariche di scala nanometrica, sono diventati complementari alle batterie nei veicoli elettrici e nei sistemi di recupero dell'energia di frenata.

Un aspetto istruttivo riguarda il bilancio energetico del processo di carica. Se si carica un condensatore collegandolo direttamente a un generatore di tensione costante $\mathcal{E}$, il generatore compie un lavoro $W_{\text{gen}} = Q\mathcal{E} = C\mathcal{E}^2$, mentre l'energia immagazzinata è solo $\frac12C\mathcal{E}^2$. L'altra metà viene dissipata nei conduttori di collegamento (per effetto Joule e per irraggiamento), indipendentemente dal valore della resistenza del circuito. Il risultato, che verrà verificato nello studio dei circuiti RC, mostra che il processo di carica a tensione costante è intrinsecamente irreversibile.

### 17.4.3 Densità di energia del campo

Per il condensatore piano possiamo riscrivere l'energia in termini del campo fra le armature. Con $C = \varepsilon_0S/d$ e $\Delta V = Ed$:

$$U = \frac12\frac{\varepsilon_0S}{d}E^2d^2 = \frac12\varepsilon_0E^2\cdot(Sd).$$

Il prodotto $Sd$ è proprio il volume della regione fra le armature, l'unica in cui il campo è diverso da zero. L'energia risulta quindi distribuita uniformemente in quel volume con **densità di energia**

$$u = \frac{U}{Sd} = \frac12\varepsilon_0E^2,$$

in perfetto accordo con il risultato generale ricavato nella sezione 16.7. Si può verificare che lo stesso vale per il condensatore sferico e cilindrico, dove il campo non è uniforme: integrando $\frac12\varepsilon_0E^2$ sul volume compreso fra le armature si ottiene esattamente $Q^2/(2C)$. Per esempio, per il condensatore cilindrico

$$U = \int_{R_1}^{R_2}\frac{\varepsilon_0}{2}\left(\frac{\lambda}{2\pi\varepsilon_0r}\right)^2 2\pi rL\,\mathrm{d}r = \frac{\lambda^2L}{4\pi\varepsilon_0}\ln\frac{R_2}{R_1} = \frac{Q^2}{2C}.$$

L'interpretazione dell'energia come proprietà del campo, distribuita nello spazio in cui il campo è presente, è dunque coerente in ogni caso. Essa suggerisce anche una regola pratica di progettazione: per immagazzinare molta energia in poco volume occorrono campi intensi, limitati però dalla rigidità dielettrica del mezzo interposto. In aria il limite è di circa 40 J/m³, come già osservato; con dielettrici solidi o con film polimerici sottili si raggiungono campi di centinaia di MV/m e densità di energia di diversi MJ/m³.

### 17.4.4 Forze fra conduttori e metodo energetico

La conoscenza dell'energia elettrostatica permette di calcolare le forze fra conduttori con il **principio dei lavori virtuali**. Consideriamo un sistema di conduttori e immaginiamo uno spostamento virtuale $\mathrm{d}x$ di una parte di esso. Occorre distinguere due situazioni.

**Sistema isolato (cariche costanti).** Se i conduttori sono isolati, le cariche non cambiano durante lo spostamento. Il lavoro compiuto dalla forza elettrica è uguale alla diminuzione dell'energia elettrostatica:

$$F_x = -\left(\frac{\partial U}{\partial x}\right)_Q.$$

**Potenziali costanti.** Se i conduttori sono collegati a generatori che ne mantengono fissi i potenziali, durante lo spostamento i generatori forniscono carica e compiono lavoro. Si dimostra che il lavoro dei generatori è il doppio della variazione di energia del sistema, e la forza risulta

$$F_x = +\left(\frac{\partial U}{\partial x}\right)_V.$$

Naturalmente la forza in una data configurazione è unica: le due formule devono dare lo stesso risultato, ed è così. Applichiamole al condensatore piano, calcolando la forza fra le armature. A carica costante, $U = Q^2/(2C) = Q^2x/(2\varepsilon_0S)$, dove $x$ è la distanza fra le armature; quindi

$$F_x = -\frac{Q^2}{2\varepsilon_0S}.$$

Il segno meno indica che la forza tende a ridurre $x$: le armature si attraggono. A potenziale costante, $U = \frac12C\Delta V^2 = \varepsilon_0S\Delta V^2/(2x)$, e $F_x = +\partial U/\partial x = -\varepsilon_0S\Delta V^2/(2x^2)$; sostituendo $\Delta V = Qx/(\varepsilon_0S)$ si ritrova lo stesso valore. Il modulo della forza si può scrivere come $F = \frac12\varepsilon_0E^2S$, cioè pressione elettrostatica per area, in accordo con la sottosezione 17.1.3.

Questo metodo è alla base degli **elettrometri assoluti** (bilance in cui la forza fra le armature di un condensatore viene equilibrata da pesi noti, permettendo di misurare una differenza di potenziale in termini di grandezze meccaniche), degli altoparlanti elettrostatici e degli attuatori dei microsistemi. Lo stesso approccio permette di spiegare perché un dielettrico viene risucchiato all'interno di un condensatore carico, fenomeno che riprenderemo nel capitolo sui dielettrici.

### Esercizio d'esempio

Un condensatore piano in aria ha armature di area $S = 200$ cm² e distanza $d = 2{,}0$ mm, ed è collegato a un generatore di $\Delta V = 1000$ V. (a) Calcolare capacità, carica, energia e densità di energia. (b) Calcolare la forza fra le armature. (c) Il condensatore viene staccato dal generatore e le armature vengono allontanate fino a $d' = 4{,}0$ mm: calcolare la nuova differenza di potenziale, la nuova energia e il lavoro compiuto dall'operatore.

**Soluzione.** (a) $C = \varepsilon_0S/d = 8{,}85\times10^{-12}\cdot0{,}020/0{,}0020 = 8{,}85\times10^{-11}$ F $= 88{,}5$ pF. $Q = C\Delta V = 8{,}85\times10^{-8}$ C. $U = \frac12C\Delta V^2 = \frac12\cdot8{,}85\times10^{-11}\cdot10^6 \approx 4{,}4\times10^{-5}$ J. Campo: $E = \Delta V/d = 5{,}0\times10^5$ V/m; densità $u = \frac12\varepsilon_0E^2 = \frac12\cdot8{,}85\times10^{-12}\cdot2{,}5\times10^{11} \approx 1{,}1$ J/m³. Verifica: $u\cdot Sd = 1{,}1\cdot4{,}0\times10^{-5} \approx 4{,}4\times10^{-5}$ J.

(b) $F = \frac12\varepsilon_0E^2S = u\,S = 1{,}1\cdot0{,}020 \approx 2{,}2\times10^{-2}$ N, attrattiva.

(c) Staccato il generatore, $Q$ resta costante e $C' = C/2 = 44{,}3$ pF. Quindi $\Delta V' = Q/C' = 2000$ V e $U' = Q^2/(2C') = 2U \approx 8{,}8\times10^{-5}$ J. Il campo resta $E = \sigma/\varepsilon_0$, invariato, e la forza resta costante durante lo spostamento: il lavoro dell'operatore è $W = F\,(d'-d) = 2{,}2\times10^{-2}\cdot2{,}0\times10^{-3} \approx 4{,}4\times10^{-5}$ J, esattamente pari all'aumento di energia $U'-U$, come prevede la conservazione dell'energia.

### Punti chiave

- L'energia di un conduttore carico è $U = \frac{Q^2}{2C} = \frac12QV = \frac12CV^2$; per più conduttori $U = \frac12\sum Q_iV_i$.
- L'energia di un condensatore ha la stessa forma, con $\Delta V$ al posto di $V$.
- Caricando un condensatore a tensione costante, metà del lavoro del generatore viene dissipata.
- L'energia è distribuita nel campo con densità $u = \frac12\varepsilon_0E^2$; vale per ogni geometria.
- Forza a carica costante: $F_x = -(\partial U/\partial x)_Q$; a potenziale costante: $F_x = +(\partial U/\partial x)_V$.
- Le armature di un condensatore piano si attraggono con forza $F = \frac12\varepsilon_0E^2S$, coerente con la pressione elettrostatica.
- La rigidità dielettrica del mezzo limita la densità di energia immagazzinabile.
