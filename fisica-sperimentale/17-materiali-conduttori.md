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
