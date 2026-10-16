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
