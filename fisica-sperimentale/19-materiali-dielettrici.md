# Capitolo 19 — Materiali dielettrici

Nei capitoli precedenti abbiamo studiato il campo elettrostatico nel vuoto e in presenza di conduttori, materiali nei quali le cariche libere possono muoversi su distanze macroscopiche fino a raggiungere l'equilibrio. Esiste però una vastissima classe di materiali, gli isolanti o **dielettrici**, nei quali gli elettroni sono legati ai rispettivi atomi o molecole e non possono migrare liberamente. Anche questi materiali, tuttavia, reagiscono alla presenza di un campo elettrico: le loro cariche legate si spostano di quantità microscopiche, dando origine a una distribuzione di dipoli elettrici che modifica il campo stesso. In questo capitolo partiremo dall'osservazione sperimentale dell'effetto di una lastra dielettrica inserita in un condensatore, interpreteremo il fenomeno in termini di polarizzazione della materia, introdurremo il vettore spostamento elettrico e la suscettività, e torneremo infine ai condensatori per studiarne le configurazioni con dielettrici e la forza con cui un dielettrico viene attratto fra le armature.

## 19.1 Dielettrici

Il modo più diretto per scoprire come un materiale isolante modifica il campo elettrico è ripetere l'esperimento storico di Faraday: si prende un condensatore piano, lo si carica e poi si inseriscono fra le armature lastre di materiali diversi, misurando con un elettrometro (uno strumento che misura la tensione senza assorbire carica) come cambia la differenza di potenziale. Questo approccio sperimentale ha il vantaggio di essere del tutto indipendente da qualsiasi modello microscopico: i risultati che otterremo sono fatti osservativi, che nella sezione successiva cercheremo di interpretare. Introdurremo in questo modo la **costante dielettrica relativa** di un materiale, la grandezza macroscopica che ne riassume la risposta al campo elettrico.

### 19.1.1 Condensatore piano

Consideriamo un condensatore piano con armature di area $S$ separate dalla distanza $d$, nel vuoto. Lo carichiamo con un generatore fino alla tensione $\Delta V_0$ e poi lo **scolleghiamo**: le armature restano isolate e la carica $\pm Q$ su di esse è fissata, perché non esiste alcun percorso attraverso il quale possa defluire. La capacità vale $C_0 = \varepsilon_0S/d$ e il campo uniforme interno è $E_0 = \sigma/\varepsilon_0 = \Delta V_0/d$, dove $\sigma = Q/S$ è la densità superficiale di carica sulle armature, che chiameremo **carica libera** per distinguerla dalle cariche che compariranno sul materiale.

La scelta di lavorare **a carica costante** è fondamentale per interpretare correttamente l'esperimento. Poiché la carica sulle armature non può cambiare, qualsiasi variazione della tensione misurata dall'elettrometro dipenderà unicamente da una variazione della capacità, cioè dall'effetto del materiale inserito: $\Delta V = Q/C$. Se invece il condensatore restasse collegato al generatore, la tensione rimarrebbe fissa e sarebbe la carica a variare, il che renderebbe la misura meno diretta (occorrerebbe misurare la carica fornita dal generatore). Ricordiamo anche le altre grandezze che seguiremo nell'esperimento: il campo elettrico fra le armature, che nel vuoto è uniforme, e l'energia immagazzinata $U_0 = Q^2/(2C_0)$. Tutte le variazioni che osserveremo saranno espresse come rapporto rispetto a questi valori di riferimento nel vuoto.

### 19.1.2 Lastra conduttrice

Inseriamo per prima cosa fra le armature, parallelamente a esse, una lastra **conduttrice** neutra di spessore $s < d$ e di area uguale a quella delle armature. All'interno del conduttore, in equilibrio, il campo deve essere nullo. Questo avviene perché gli elettroni liberi della lastra si spostano sotto l'azione del campo $E_0$ fino a che sulle due facce della lastra compaiono cariche indotte $\mp Q$ (la faccia affacciata all'armatura positiva si carica negativamente, l'altra positivamente), esattamente uguali in modulo a quelle delle armature. Il campo prodotto da queste cariche indotte cancella esattamente il campo $E_0$ all'interno della lastra, mentre nelle due intercapedini vuote restanti il campo rimane $E_0$, perché la densità di carica sulle armature non è cambiata. Si noti che la lastra resta complessivamente neutra: le cariche indotte sulle due facce sono uguali e opposte.

La differenza di potenziale si ottiene integrando il campo lungo un segmento perpendicolare alle armature: il contributo dell'interno della lastra è nullo, e resta il contributo dei tratti vuoti di lunghezza complessiva $d - s$:

$$\Delta V = E_0(d - s) = \Delta V_0\left(1 - \frac{s}{d}\right), \qquad C = \frac{\varepsilon_0S}{d - s}$$

La tensione diminuisce e la capacità aumenta; il risultato non dipende dalla posizione della lastra fra le armature, ma solo dal suo spessore. Il sistema si comporta come due condensatori in serie con distanze $d_1$ e $d_2$, con $d_1 + d_2 = d - s$, oppure, equivalentemente, come un unico condensatore con distanza ridotta $d - s$. Nel limite $s\to d$ la tensione tende a zero e la capacità diverge, perché le armature vengono messe in cortocircuito. Una lastra conduttrice "annulla" quindi completamente il campo nella regione che occupa. Con il linguaggio che introdurremo fra poco, potremmo dire che un conduttore si comporta come un dielettrico con costante dielettrica infinita.

### 19.1.3 Lastra dielettrica

Ripetiamo ora l'esperimento inserendo una lastra di materiale **isolante** (vetro, plastica, mica, carta paraffinata, ceramica) che riempie completamente lo spazio fra le armature. L'elettrometro mostra ancora una diminuzione della tensione, ma questa volta non fino a zero: la tensione si riduce di un fattore $\varepsilon_r$, caratteristico del materiale e indipendente dalla geometria del condensatore e dal valore della carica:

$$\Delta V = \frac{\Delta V_0}{\varepsilon_r}, \qquad C = \varepsilon_rC_0 = \frac{\varepsilon_0\varepsilon_rS}{d} = \frac{\varepsilon S}{d}$$

Il numero puro $\varepsilon_r \ge 1$ si chiama **costante dielettrica relativa** del materiale, e il prodotto $\varepsilon = \varepsilon_0\varepsilon_r$ si chiama **costante dielettrica assoluta** (o permittività) del materiale. Poiché la tensione si è ridotta a parità di distanza, anche il campo nel dielettrico si è ridotto dello stesso fattore: $E = E_0/\varepsilon_r$. Alcuni valori tipici: aria secca a pressione atmosferica $1.0006$ (praticamente uguale al vuoto, il che giustifica l'approssimazione usata finora), teflon circa 2.1, polietilene 2.3, carta 3–4, vetro 4–10, mica 5–7, acqua circa 80 a temperatura ambiente, ceramiche ferroelettriche come il titanato di bario da centinaia a diverse migliaia.

Se la lastra dielettrica ha spessore $s < d$, il campo vale $E_0$ nelle intercapedini vuote e $E_0/\varepsilon_r$ nel dielettrico, e la tensione diventa

$$\Delta V = E_0(d - s) + \frac{E_0}{\varepsilon_r}s = \frac{Q}{\varepsilon_0S}\left(d - s + \frac{s}{\varepsilon_r}\right), \qquad C = \frac{\varepsilon_0S}{d - s + s/\varepsilon_r}$$

Per $\varepsilon_r = 1$ si ritrova il vuoto, per $\varepsilon_r\to\infty$ la lastra conduttrice: il dielettrico rappresenta un comportamento intermedio fra il vuoto e il conduttore. Questa analogia suggerisce già l'interpretazione: anche nel dielettrico devono comparire sulle facce della lastra delle cariche indotte di segno opposto a quelle delle armature affacciate, ma di modulo inferiore, tali da ridurre il campo interno senza annullarlo. Non potendo trattarsi di cariche libere (il materiale è isolante), esse devono derivare da piccoli spostamenti delle cariche legate all'interno di atomi e molecole: è il fenomeno della **polarizzazione**, che studieremo nella prossima sezione.

L'esperimento ha conseguenze tecnologiche di primaria importanza. In primo luogo, un dielettrico aumenta la capacità di un fattore $\varepsilon_r$, permettendo di costruire condensatori compatti di grande capacità. In secondo luogo, un buon dielettrico sopporta campi elettrici molto più intensi dell'aria prima di perdere le proprie proprietà isolanti: il campo massimo sopportabile si chiama **rigidità dielettrica** e vale circa 3 MV/m per l'aria, 10–20 MV/m per la carta impregnata, 60 MV/m per il teflon, fino a 100–200 MV/m per la mica. Superata la rigidità dielettrica si verifica la **scarica** (o perforazione), con la formazione di un canale conduttivo e generalmente il danneggiamento irreversibile del materiale. In terzo luogo, il dielettrico mantiene le armature separate meccanicamente, consentendo distanze di pochi micrometri. Combinando i tre effetti, la densità di energia immagazzinabile $\frac{1}{2}\varepsilon E_{max}^2$ può superare di vari ordini di grandezza quella in aria.

Infine, è utile considerare l'esperimento a **tensione costante**: se il condensatore resta collegato al generatore durante l'inserimento del dielettrico, la tensione non cambia e il generatore fornisce carica aggiuntiva, finché la carica sulle armature diventa $\varepsilon_rQ_0$. Il campo nel dielettrico in questo caso resta $E_0 = \Delta V_0/d$, ma la densità di carica libera sulle armature aumenta di un fattore $\varepsilon_r$. I due punti di vista descrivono la stessa fisica: in entrambi i casi la capacità è aumentata di $\varepsilon_r$.

### Esercizio d'esempio

Un condensatore piano con armature di area $S = 2.0\times10^{-2}$ m$^2$ distanti $d = 4.0$ mm viene caricato a $\Delta V_0 = 400$ V e poi isolato. Si inserisce fra le armature una lastra di vetro ($\varepsilon_r = 5.0$) di spessore $s = 2.0$ mm. Calcolare (a) la capacità iniziale e la carica; (b) il campo nel vuoto e nel vetro dopo l'inserimento; (c) la nuova tensione e la nuova capacità; (d) che cosa cambierebbe se la lastra fosse metallica.

**Soluzione.** (a) $C_0 = \varepsilon_0S/d = 8.854\times10^{-12}\times2.0\times10^{-2}/4.0\times10^{-3} = 4.43\times10^{-11}$ F $= 44.3$ pF. La carica è $Q = C_0\Delta V_0 = 1.77\times10^{-8}$ C.

(b) A carica costante, il campo nelle intercapedini vuote resta $E_0 = \Delta V_0/d = 1.0\times10^5$ V/m; nel vetro $E = E_0/\varepsilon_r = 2.0\times10^4$ V/m.

(c) $\Delta V = E_0(d-s) + E s = 1.0\times10^5\times2.0\times10^{-3} + 2.0\times10^4\times2.0\times10^{-3} = 200 + 40 = 240$ V. La capacità diventa $C = Q/\Delta V = 7.38\times10^{-11}$ F $= 73.8$ pF, in accordo con $\varepsilon_0S/(d - s + s/\varepsilon_r) = \varepsilon_0S/(2.4\times10^{-3}\ \text{m})$.

(d) Con una lastra metallica dello stesso spessore il campo interno alla lastra sarebbe nullo e $\Delta V = E_0(d - s) = 200$ V, con $C = \varepsilon_0S/(d-s) = 88.5$ pF: un aumento maggiore, coerente con l'interpretazione del conduttore come dielettrico con $\varepsilon_r\to\infty$.

### Punti chiave

- Inserendo un dielettrico in un condensatore isolato, la tensione e il campo si riducono di un fattore $\varepsilon_r$ e la capacità aumenta dello stesso fattore: $C = \varepsilon_rC_0$.
- La costante dielettrica relativa $\varepsilon_r\ge1$ è una proprietà del materiale; $\varepsilon = \varepsilon_0\varepsilon_r$ è la costante dielettrica assoluta.
- Una lastra conduttrice di spessore $s$ annulla il campo al suo interno e dà $C = \varepsilon_0S/(d-s)$; è il limite $\varepsilon_r\to\infty$ del dielettrico.
- Una lastra dielettrica di spessore $s$ dà $C = \varepsilon_0S/(d - s + s/\varepsilon_r)$, indipendentemente dalla posizione della lastra.
- La rigidità dielettrica è il campo massimo che il materiale sopporta senza scarica; insieme a $\varepsilon_r$ determina la massima energia immagazzinabile.
- A carica costante il campo nel dielettrico diminuisce; a tensione costante il campo resta invariato e la carica libera aumenta di $\varepsilon_r$.

## 19.2 Polarizzazione

L'esperimento della sezione precedente ha mostrato che un isolante riduce il campo elettrico al proprio interno, e ha suggerito che ciò avvenga perché sulle superfici del materiale compaiono cariche indotte di segno opposto alle armature affacciate. In questa sezione costruiamo il modello microscopico che spiega questa osservazione e ne ricaviamo una descrizione macroscopica completa. I concetti chiave sono il **momento di dipolo** indotto o orientato nelle molecole, il vettore **polarizzazione** che ne descrive la densità, le **cariche di polarizzazione** che esso produce e il vettore **spostamento elettrico**, che permette di riscrivere la legge di Gauss tenendo conto soltanto delle cariche libere.

### 19.2.1 Polarizzazione

Un dielettrico è formato da atomi o molecole elettricamente neutri. In assenza di campo esterno, ciascuna molecola ha il baricentro delle cariche positive (i nuclei) e quello delle cariche negative (la nube elettronica) che coincidono oppure, nelle molecole dette **polari**, che sono separati di una distanza fissa, ma con orientazione casuale da una molecola all'altra. In entrambi i casi un elemento macroscopico di materiale non presenta alcun momento di dipolo complessivo. Quando si applica un campo elettrico $\vec{E}$, le forze che esso esercita sulle cariche positive e negative, uguali e opposte, tendono a separarle (o ad allineare i dipoli preesistenti), e ogni molecola acquista in media un momento di dipolo $\vec{p}$ orientato come il campo. Il materiale si dice allora **polarizzato**.

Per descrivere macroscopicamente questo stato si introduce il vettore **polarizzazione** $\vec{P}$, definito come il momento di dipolo per unità di volume:

$$\vec{P} = \frac{d\vec{p}_{tot}}{d\tau} = n\langle\vec{p}\rangle$$

dove $n$ è il numero di molecole per unità di volume e $\langle\vec{p}\rangle$ il momento di dipolo medio di una molecola. Il volume $d\tau$ va inteso come "fisicamente infinitesimo": abbastanza piccolo da poter essere trattato come un punto alla scala macroscopica, ma abbastanza grande da contenere moltissime molecole, in modo che la media abbia senso. La polarizzazione si misura in C·m/m$^3$ = C/m$^2$, le stesse unità di una densità superficiale di carica: non è un caso, come vedremo fra poco.

Nella maggior parte dei materiali, detti **dielettrici lineari e isotropi**, per campi non troppo intensi la polarizzazione è proporzionale al campo elettrico totale presente nel materiale e ha la sua stessa direzione:

$$\vec{P} = \varepsilon_0\chi\,\vec{E}$$

Il numero puro $\chi \ge 0$ si chiama **suscettività elettrica** del materiale. Il fattore $\varepsilon_0$ è inserito per rendere $\chi$ adimensionale. È importante notare che $\vec{E}$ è il campo complessivo nel dielettrico, cioè il campo esterno più il campo prodotto dalla polarizzazione stessa: il problema è quindi autoconsistente. Esistono materiali che non soddisfano questa relazione: i cristalli **anisotropi**, nei quali $\vec{P}$ non è parallelo a $\vec{E}$ e la suscettività diventa un tensore; i materiali **ferroelettrici**, nei quali la relazione è non lineare, presenta isteresi e può esistere una polarizzazione permanente anche a campo nullo (gli **elettreti**); i materiali **piezoelettrici**, nei quali la polarizzazione si genera anche per deformazione meccanica.

### 19.2.2 Polarizzazione per deformazione e per orientamento

I meccanismi microscopici con cui un materiale si polarizza sono essenzialmente due. Il primo è la **polarizzazione per deformazione** (o elettronica, e nei solidi ionici anche ionica), presente in tutti i materiali. Il campo esterno sposta la nube elettronica di un atomo rispetto al nucleo, deformandola; la forza di richiamo elastica dovuta all'attrazione nucleo–elettroni è, per piccoli spostamenti, proporzionale allo spostamento, e quindi il momento di dipolo indotto è proporzionale al campo: $\vec{p} = \alpha\varepsilon_0\vec{E}$, dove $\alpha$ è la **polarizzabilità** atomica, che ha le dimensioni di un volume ed è dell'ordine del volume atomico ($10^{-30}$ m$^3$). Un semplice modello in cui l'atomo è una sfera di carica negativa uniforme di raggio $R$ con il nucleo puntiforme al centro fornisce $\alpha = 4\pi R^3$. Lo spostamento indotto è minuscolo: anche in un campo di $10^6$ V/m è una frazione infinitesima del raggio atomico, perché i campi interni all'atomo sono dell'ordine di $10^{11}$ V/m. La polarizzazione per deformazione è praticamente indipendente dalla temperatura e risponde a campi variabili fino a frequenze ottiche.

Il secondo meccanismo è la **polarizzazione per orientamento**, presente soltanto nei materiali costituiti da **molecole polari**, cioè dotate di un momento di dipolo permanente $p_0$ anche in assenza di campo; l'esempio più importante è l'acqua, con $p_0 = 6.2\times10^{-30}$ C·m. Un campo esterno esercita su ciascun dipolo il momento meccanico $\vec{p}_0\times\vec{E}$, che tende ad allinearlo al campo, mentre l'agitazione termica tende a disordinare le orientazioni. L'equilibrio fra queste due tendenze è governato dal rapporto fra l'energia di interazione $p_0E$ e l'energia termica $k_BT$. In condizioni ordinarie $p_0E \ll k_BT$ (anche con $E = 10^6$ V/m, $p_0E\approx6\times10^{-24}$ J contro $k_BT\approx4\times10^{-21}$ J a temperatura ambiente) e l'allineamento è solo parziale; un calcolo di meccanica statistica (Langevin–Debye) fornisce un momento medio $\langle p\rangle = p_0^2E/(3k_BT)$. Questo contributo è dunque inversamente proporzionale alla temperatura, ed è di norma molto più grande di quello per deformazione: ciò spiega l'elevata costante dielettrica dell'acqua. Essendo legato alla rotazione di intere molecole, esso non riesce a seguire campi che oscillano troppo rapidamente: nell'acqua, a frequenze ottiche, la costante dielettrica scende a circa 1.8.

### 19.2.3 Cariche di polarizzazione

Come fa un insieme di dipoli microscopici, ciascuno elettricamente neutro, a modificare il campo macroscopico? Consideriamo una lastra di dielettrico uniformemente polarizzata, con $\vec{P}$ perpendicolare alle facce. All'interno del materiale ogni carica positiva spostata è "compensata" dalla carica negativa della molecola vicina: la densità di carica netta in volume è nulla. Ma sulle superfici questo compenso non avviene: sulla faccia verso cui punta $\vec{P}$ affiorano le estremità positive dei dipoli, sulla faccia opposta quelle negative. Si formano così delle **cariche di polarizzazione** (o cariche legate) superficiali. Un semplice calcolo mostra che la loro densità è

$$\sigma_p = \vec{P}\cdot\hat{n}$$

dove $\hat{n}$ è la normale uscente dalla superficie. Infatti, se le cariche positive (densità volumetrica $n q$) si spostano rigidamente di $\delta$ rispetto a quelle negative, su una superficie di area $S$ resta scoperto uno strato di volume $S\delta$ contenente la carica $nq\delta S = PS$. Se la polarizzazione non è uniforme, in generale compare anche una densità volumetrica di carica di polarizzazione,

$$\rho_p = -\nabla\cdot\vec{P}$$

che esprime il fatto che, dove la polarizzazione diverge, più cariche positive escono da un volumetto di quante ne entrino. In un dielettrico lineare omogeneo senza cariche libere al suo interno si ha $\rho_p = 0$, e le cariche di polarizzazione si trovano solo sulle superfici. Le cariche di polarizzazione sono cariche vere, che producono campo elettrico come qualsiasi altra carica, ma non possono essere separate dal materiale né rimosse: non si può, ad esempio, "scaricarle" toccandole con un conduttore.

Torniamo al condensatore piano riempito di dielettrico. Sulla faccia del dielettrico affacciata all'armatura positiva (densità libera $+\sigma$) compare $-\sigma_p$, sull'altra $+\sigma_p$. Il campo nel dielettrico è prodotto dalla densità netta $\sigma - \sigma_p$: $E = (\sigma - \sigma_p)/\varepsilon_0$. Con $\sigma_p = P = \varepsilon_0\chi E$ si ricava $E(1+\chi) = \sigma/\varepsilon_0 = E_0$, cioè

$$E = \frac{E_0}{1+\chi}, \qquad \varepsilon_r = 1 + \chi$$

Ecco spiegato il risultato sperimentale: la costante dielettrica relativa è legata alla suscettività da $\varepsilon_r = 1 + \chi$, e la riduzione del campo è dovuta alle cariche di polarizzazione che schermano parzialmente le cariche libere. La frazione schermata è $\sigma_p/\sigma = \chi/(1+\chi) = (\varepsilon_r - 1)/\varepsilon_r$.

### 19.2.4 Vettore spostamento elettrico

Le cariche di polarizzazione complicano l'applicazione del teorema di Gauss, perché in generale non sono note a priori: dipendono dal campo, che è proprio ciò che si vuole calcolare. In presenza di dielettrici la legge di Gauss in forma locale si scrive $\nabla\cdot\vec{E} = (\rho_l + \rho_p)/\varepsilon_0$, dove $\rho_l$ è la densità di carica libera. Sostituendo $\rho_p = -\nabla\cdot\vec{P}$:

$$\nabla\cdot(\varepsilon_0\vec{E} + \vec{P}) = \rho_l$$

È naturale allora definire il vettore **spostamento elettrico** (o induzione elettrica)

$$\vec{D} = \varepsilon_0\vec{E} + \vec{P}$$

che soddisfa la legge di Gauss con le sole cariche libere: $\nabla\cdot\vec{D} = \rho_l$, ovvero in forma integrale $\oint_S\vec{D}\cdot d\vec{S} = Q_{l,int}$. $\vec{D}$ si misura in C/m$^2$. Nei dielettrici lineari e isotropi $\vec{D} = \varepsilon_0(1+\chi)\vec{E} = \varepsilon\vec{E}$. Nel condensatore piano, applicando Gauss a una scatoletta che racchiude un tratto dell'armatura positiva si ottiene subito $D = \sigma$, indipendentemente dal dielettrico, e quindi $E = \sigma/\varepsilon$.

Occorre però cautela: $\vec{D}$ non è un "campo" nel senso che non agisce sulle cariche (la forza su una carica è sempre $q\vec{E}$), e a differenza di $\vec{E}$ il suo rotore non è in generale nullo. La sua utilità sta nelle situazioni di alta simmetria, in cui basta conoscere le cariche libere per determinare $\vec{D}$ con Gauss e poi $\vec{E} = \vec{D}/\varepsilon$. Alle superfici di separazione fra due dielettrici, senza cariche libere superficiali, si conservano la **componente normale di $\vec{D}$** ($D_{1n} = D_{2n}$, da Gauss) e la **componente tangenziale di $\vec{E}$** ($E_{1t} = E_{2t}$, dalla conservatività): ne segue che le linee di campo si **rifrangono** all'interfaccia secondo la legge $\tan\theta_1/\tan\theta_2 = \varepsilon_1/\varepsilon_2$, avvicinandosi alla normale nel mezzo con costante dielettrica minore. Infine, la densità di energia nel dielettrico lineare diventa $u_e = \frac{1}{2}\vec{E}\cdot\vec{D} = \frac{1}{2}\varepsilon E^2$, che comprende anche l'energia immagazzinata nella deformazione delle molecole.

### Esercizio d'esempio

Un condensatore piano ha armature di area $S = 1.0\times10^{-2}$ m$^2$ distanti $d = 0.50$ mm, completamente riempito da un polimero con $\varepsilon_r = 3.0$, ed è collegato a una tensione $\Delta V = 100$ V. Calcolare $E$, $D$, $P$, la suscettività, la densità di carica libera e di polarizzazione, e il momento di dipolo totale del dielettrico.

**Soluzione.** Il campo è $E = \Delta V/d = 100/5.0\times10^{-4} = 2.0\times10^5$ V/m. Lo spostamento è $D = \varepsilon_0\varepsilon_rE = 8.854\times10^{-12}\times3.0\times2.0\times10^5 = 5.31\times10^{-6}$ C/m$^2$, e coincide con la densità di carica libera $\sigma = 5.31\ \mu$C/m$^2$. La suscettività è $\chi = \varepsilon_r - 1 = 2.0$, e la polarizzazione $P = \varepsilon_0\chi E = 3.54\times10^{-6}$ C/m$^2$, pari a $\sigma_p$. Verifica: $D = \varepsilon_0E + P = 1.77\times10^{-6} + 3.54\times10^{-6} = 5.31\times10^{-6}$ C/m$^2$. Il momento di dipolo totale è $p_{tot} = P\cdot Sd = 3.54\times10^{-6}\times5.0\times10^{-6} = 1.77\times10^{-11}$ C·m, equivalente a cariche $\pm\sigma_pS = \pm3.54\times10^{-8}$ C separate dalla distanza $d$.

### Punti chiave

- La polarizzazione $\vec{P}$ è il momento di dipolo per unità di volume; nei dielettrici lineari isotropi $\vec{P} = \varepsilon_0\chi\vec{E}$, con $\chi$ suscettività elettrica.
- Polarizzazione per deformazione: presente in tutti i materiali, indipendente da $T$; per orientamento: solo in molecole polari, proporzionale a $p_0^2/(3k_BT)$.
- Le cariche di polarizzazione hanno densità $\sigma_p = \vec{P}\cdot\hat{n}$ sulle superfici e $\rho_p = -\nabla\cdot\vec{P}$ in volume; sono cariche vere ma legate.
- La riduzione del campo nel dielettrico è dovuta allo schermo delle cariche di polarizzazione: $\varepsilon_r = 1 + \chi$.
- Lo spostamento elettrico $\vec{D} = \varepsilon_0\vec{E} + \vec{P} = \varepsilon\vec{E}$ soddisfa Gauss con le sole cariche libere: $\oint\vec{D}\cdot d\vec{S} = Q_l$.
- All'interfaccia fra dielettrici si conservano $D_n$ ed $E_t$; le linee di campo si rifrangono.
- La densità di energia in un dielettrico lineare vale $u_e = \frac{1}{2}\varepsilon E^2 = \frac{1}{2}\vec{E}\cdot\vec{D}$.

## 19.3 Condensatori

Con gli strumenti sviluppati nelle sezioni precedenti (costante dielettrica, polarizzazione e vettore spostamento) possiamo ora affrontare i condensatori riempiti in modo non uniforme da uno o più dielettrici. Le due configurazioni elementari sono quella in cui strati di materiali diversi si succedono lungo la direzione del campo, e quella in cui materiali diversi si affiancano trasversalmente al campo. Si vedrà che esse corrispondono, rispettivamente, al collegamento in serie e in parallelo di condensatori, e che i due casi si distinguono per quale grandezza resta continua fra un materiale e l'altro: il vettore $\vec{D}$ nel primo caso, il campo $\vec{E}$ nel secondo. Concluderemo con un fenomeno di grande interesse fisico e tecnologico: la forza con cui un dielettrico viene risucchiato all'interno di un condensatore carico.

### 19.3.1 Condensatori in serie

Consideriamo un condensatore piano di area $S$ in cui lo spazio fra le armature è occupato da due strati di dielettrico sovrapposti, di spessori $d_1$ e $d_2$ e costanti dielettriche relative $\varepsilon_{r1}$ ed $\varepsilon_{r2}$, con le superfici di separazione parallele alle armature. Il campo è perpendicolare alle interfacce, e quindi la componente che si conserva attraversandole è quella normale di $\vec{D}$. Applicando il teorema di Gauss per $\vec{D}$ a una scatoletta che racchiude l'armatura positiva si ottiene $D = \sigma$ in entrambi gli strati, dove $\sigma = Q/S$ è la densità di carica libera. Il campo elettrico, invece, è diverso nei due materiali:

$$E_1 = \frac{\sigma}{\varepsilon_0\varepsilon_{r1}}, \qquad E_2 = \frac{\sigma}{\varepsilon_0\varepsilon_{r2}}$$

ed è più intenso nel materiale con costante dielettrica minore. La differenza di potenziale è la somma dei contributi dei due strati:

$$\Delta V = E_1d_1 + E_2d_2 = \frac{Q}{\varepsilon_0S}\left(\frac{d_1}{\varepsilon_{r1}} + \frac{d_2}{\varepsilon_{r2}}\right)$$

da cui

$$\frac{1}{C} = \frac{d_1}{\varepsilon_0\varepsilon_{r1}S} + \frac{d_2}{\varepsilon_0\varepsilon_{r2}S} = \frac{1}{C_1} + \frac{1}{C_2}$$

Il sistema equivale dunque a **due condensatori in serie**, ciascuno riempito da un solo dielettrico. L'equivalenza si può rendere fisicamente esplicita immaginando di inserire, sull'interfaccia fra i due strati, un foglio metallico sottilissimo: esso non altera il campo (su di esso si inducono cariche $\mp Q$ sulle due facce, esattamente come nel collegamento in serie) e trasforma il sistema in due condensatori distinti collegati da un conduttore. Sull'interfaccia, in assenza del foglio, si trova una densità netta di carica di polarizzazione $\sigma_{p2} - \sigma_{p1}$, diversa da zero se i due materiali sono diversi, che rende conto della discontinuità di $E$.

Questa configurazione è frequentissima nella pratica, anche quando non è voluta. Un caso tipico è il **sottile strato d'aria** che rimane fra un'armatura e un dielettrico solido mal accoppiati: poiché l'aria ha costante dielettrica molto più bassa del solido, il campo nello strato d'aria è $\varepsilon_r$ volte più intenso che nel dielettrico, e può superare la rigidità dielettrica dell'aria provocando microscariche (dette **scariche parziali**) che degradano progressivamente l'isolante. Per questo nei condensatori e nei cavi ad alta tensione gli isolanti vengono impregnati con oli o resine che eliminano le bolle d'aria. Più in generale, nei sistemi a strati è necessario verificare la rigidità di **ogni** strato, perché la ripartizione della tensione segue la stessa legge del partitore capacitivo: lo strato con capacità minore (più spesso o con $\varepsilon_r$ minore) sopporta la frazione maggiore della tensione.

### 19.3.2 Condensatori in parallelo

Consideriamo ora un condensatore piano con armature a distanza $d$ in cui due dielettrici diversi sono affiancati, ciascuno occupando l'intero spessore $d$ ma soltanto una parte dell'area: $S_1$ per il materiale con $\varepsilon_{r1}$ e $S_2$ per quello con $\varepsilon_{r2}$, con $S_1 + S_2 = S$. Le interfacce sono ora parallele al campo, e la grandezza che si conserva attraversandole è la componente tangenziale di $\vec{E}$. Poiché inoltre le armature sono equipotenziali, la differenza di potenziale è la stessa lungo qualunque percorso perpendicolare, e il campo è uniforme e uguale nei due materiali:

$$E_1 = E_2 = \frac{\Delta V}{d}$$

Lo spostamento elettrico, e quindi la densità di carica libera sulle armature, è invece diverso nelle due regioni: $D_1 = \sigma_1 = \varepsilon_0\varepsilon_{r1}E$ e $D_2 = \sigma_2 = \varepsilon_0\varepsilon_{r2}E$. La carica libera si addensa dunque sulla porzione di armatura affacciata al materiale con costante dielettrica maggiore: le armature, essendo conduttori, ridistribuiscono la propria carica in modo da mantenersi equipotenziali, compensando le diverse cariche di polarizzazione. La carica totale è

$$Q = \sigma_1S_1 + \sigma_2S_2 = \frac{\varepsilon_0\Delta V}{d}(\varepsilon_{r1}S_1 + \varepsilon_{r2}S_2)$$

e quindi

$$C = \frac{\varepsilon_0\varepsilon_{r1}S_1}{d} + \frac{\varepsilon_0\varepsilon_{r2}S_2}{d} = C_1 + C_2$$

Il sistema equivale a **due condensatori in parallelo**. Anche qui l'equivalenza ha una realizzazione fisica immediata: si potrebbe tagliare ciascuna armatura lungo la linea di separazione fra i due dielettrici e collegare le metà con fili, ottenendo due condensatori distinti in parallelo, senza modificare nulla. Il risultato è utile, ad esempio, per calcolare la capacità di un condensatore parzialmente immerso in un liquido isolante, che costituisce un semplice **sensore di livello**: la capacità varia linearmente con l'altezza del liquido, e misurarla fornisce l'altezza.

È istruttivo confrontare le due configurazioni dal punto di vista della teoria delle linee di campo. Nella serie le linee di $\vec{D}$ attraversano senza interruzioni tutti gli strati (le uniche sorgenti di $\vec{D}$ sono le cariche libere sulle armature), mentre le linee di $\vec{E}$ in parte terminano sulle cariche di polarizzazione dell'interfaccia. Nel parallelo, invece, le linee di $\vec{E}$ sono identiche nelle due regioni, mentre le linee di $\vec{D}$ sono più fitte nel materiale con $\varepsilon_r$ maggiore. Nei casi generali, in cui le interfacce non sono né parallele né perpendicolari al campo, le linee si rifrangono e il calcolo esatto della capacità richiede metodi numerici; le formule di serie e parallelo forniscono però spesso limiti superiori e inferiori utili.

### 19.3.3 Richiamo del dielettrico

Un'esperienza classica di laboratorio mostra che, se si avvicina una lastra di dielettrico al bordo di un condensatore carico, la lastra viene **attratta** verso l'interno; analogamente, se si immergono parzialmente due armature verticali in un liquido isolante (ad esempio olio) e si applica una tensione, il liquido risale fra le armature fino a un'altezza di equilibrio. Il fenomeno è chiamato **richiamo del dielettrico**.

Dal punto di vista microscopico la forza nasce nella regione di bordo, dove il campo non è uniforme: le linee di campo che "sporgono" dal condensatore hanno una componente parallela alle armature, che agisce sulle cariche di polarizzazione della lastra e la trascina verso l'interno, dove il campo è più intenso. Più in generale, un dielettrico polarizzato è sempre attratto verso le regioni di campo più intenso, perché i dipoli indotti, allineati al campo, risentono di una forza $(\vec{p}\cdot\nabla)\vec{E}$ diretta verso il gradiente di $E^2$. Lo stesso principio spiega perché un pettine elettrizzato attrae piccoli pezzi di carta neutri, o perché un filo sottile d'acqua viene deviato da una bacchetta carica.

Il calcolo diretto della forza a partire dal campo di bordo è complicato, ma il **metodo dei lavori virtuali** permette di aggirare il problema in modo elegante. Sia la lastra, di costante dielettrica $\varepsilon_r$ e spessore pari alla distanza $d$ fra le armature, inserita per un tratto $x$ in un condensatore con armature rettangolari di larghezza $b$ (nella direzione trasversale) e lunghezza $l$ (nella direzione di inserimento). Il sistema è un parallelo di due condensatori, e la capacità vale

$$C(x) = \frac{\varepsilon_0b}{d}\left[\varepsilon_rx + (l - x)\right] = \frac{\varepsilon_0b}{d}\left[l + (\varepsilon_r - 1)x\right]$$

crescente con $x$. Se il condensatore è isolato (carica costante), la forza sulla lastra è

$$F_x = -\left(\frac{\partial U_e}{\partial x}\right)_Q = -\frac{\partial}{\partial x}\frac{Q^2}{2C} = \frac{Q^2}{2C^2}\frac{dC}{dx} = \frac{1}{2}\Delta V^2\frac{dC}{dx}$$

ovvero

$$F_x = \frac{\varepsilon_0(\varepsilon_r - 1)\,b\,\Delta V^2}{2d} = \frac{1}{2}\varepsilon_0(\varepsilon_r - 1)E^2\,(b\,d)$$

La forza è positiva, cioè diretta verso l'interno: il dielettrico è richiamato. Se invece il condensatore è mantenuto a tensione costante da un generatore, durante uno spostamento $dx$ la capacità aumenta e il generatore fornisce la carica $dQ = \Delta V\,dC$, compiendo il lavoro $\Delta V^2dC$; di questo, metà va ad aumentare l'energia del campo ($dU_e = \frac{1}{2}\Delta V^2dC$) e metà è il lavoro meccanico compiuto sulla lastra. Si ha quindi $F_x = +(\partial U_e/\partial x)_{\Delta V} = \frac{1}{2}\Delta V^2\,dC/dx$, lo stesso risultato. Come già notato per la forza fra le armature, la forza istantanea non può dipendere dal vincolo, ma il bilancio energetico sì: a carica costante la lastra viene tirata dentro a spese dell'energia del campo (che diminuisce), a tensione costante a spese del generatore (e l'energia del campo aumenta).

Si noti che la forza è indipendente da $x$, finché la lastra non è entrata completamente e il bordo della lastra è lontano dai bordi delle armature (nel caso a tensione costante): ciò conferma che essa nasce nella zona di bordo, la cui struttura non cambia durante l'inserimento. Dividendo la forza per la sezione $b\,d$ della lastra si ottiene una **pressione** $p = \frac{1}{2}\varepsilon_0(\varepsilon_r - 1)E^2$, che nel caso del liquido sostiene una colonna di altezza $h$ data da $\rho gh = \frac{1}{2}\varepsilon_0(\varepsilon_r - 1)E^2$. La misura di questa altezza fornisce un metodo per determinare la costante dielettrica di un liquido. Se la lastra è libera di muoversi e non c'è attrito, essa viene accelerata verso l'interno, supera la posizione di centratura e oscilla attorno a essa; in presenza di dissipazione si arresta nella posizione di massima capacità, cioè completamente inserita.

### Esercizio d'esempio

Due armature metalliche verticali, larghe $b = 5.0$ cm e distanti $d = 2.0$ mm, sono parzialmente immerse in un olio isolante con $\varepsilon_r = 2.5$ e densità $\rho = 900$ kg/m$^3$. Fra le armature si applica $\Delta V = 2000$ V. Calcolare (a) la forza con cui l'olio è richiamato verso l'alto e (b) la sopraelevazione dell'olio fra le armature. (c) Se le armature sono alte $l = 10$ cm e l'olio occupa 4.0 cm di altezza dopo la sopraelevazione, calcolare la capacità.

**Soluzione.** (a) Il campo fra le armature è $E = \Delta V/d = 1.0\times10^6$ V/m (inferiore alla rigidità dell'aria). La forza vale

$$F = \frac{1}{2}\varepsilon_0(\varepsilon_r - 1)E^2bd = \frac{1}{2}\times8.854\times10^{-12}\times1.5\times10^{12}\times(0.050\times0.0020)\ \text{N} = 6.6\times10^{-4}\ \text{N}$$

(b) Uguagliando la pressione elettrostatica alla pressione idrostatica della colonna sopraelevata:

$$h = \frac{\varepsilon_0(\varepsilon_r - 1)E^2}{2\rho g} = \frac{8.854\times10^{-12}\times1.5\times10^{12}}{2\times900\times9.81}\ \text{m} = 7.5\times10^{-4}\ \text{m}$$

cioè circa 0.75 mm: un effetto piccolo ma ben misurabile.

(c) Il sistema è un parallelo: tratto con olio di altezza $x = 0.040$ m e tratto in aria di altezza $l - x = 0.060$ m:

$$C = \frac{\varepsilon_0b}{d}\left[\varepsilon_rx + (l - x)\right] = \frac{8.854\times10^{-12}\times0.050}{0.0020}\times(0.10 + 0.060)\ \text{F} = 3.5\times10^{-11}\ \text{F}$$

pari a 35 pF, contro i 22 pF del condensatore vuoto.

### Punti chiave

- Strati di dielettrico perpendicolari al campo equivalgono a condensatori in serie: $D$ è continuo, $E$ è maggiore nel materiale con $\varepsilon_r$ minore, $1/C = \sum d_k/(\varepsilon_0\varepsilon_{rk}S)$.
- Dielettrici affiancati parallelamente al campo equivalgono a condensatori in parallelo: $E$ è uguale ovunque, $D$ e la carica libera sono maggiori dove $\varepsilon_r$ è maggiore, $C = \sum\varepsilon_0\varepsilon_{rk}S_k/d$.
- Nei sistemi a strati va verificata la rigidità di ciascuno strato: un sottile strato d'aria può innescare scariche parziali.
- Un dielettrico è attratto verso le regioni di campo più intenso; in un condensatore viene richiamato all'interno dal campo di bordo.
- La forza di richiamo si calcola con i lavori virtuali: $F = \frac{1}{2}\Delta V^2\,dC/dx = \frac{1}{2}\varepsilon_0(\varepsilon_r - 1)E^2bd$, uguale a carica o a tensione costante.
- Un liquido dielettrico risale fra armature verticali di $h = \varepsilon_0(\varepsilon_r - 1)E^2/(2\rho g)$.
