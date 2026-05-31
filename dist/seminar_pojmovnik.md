# Seminar Pojmovnik - Priprema za Q&A i obranu rada

Ovaj dokument služi kao "šalabahter" za sva moguća pitanja komisije. Ovdje su sažeti svi stručni pojmovi, kratice, tehnologije i matematički koncepti spomenuti u seminaru.

---

## 1. Vrste vozila i tehnologije
* **Intralogistika:** Upravljanje unutarnjim tokovima materijala, robe i informacija unutar jedne tvornice, skladišta ili distribucijskog centra.
* **AGV (Automated Guided Vehicle):** Automatski vođeno vozilo. Starija generacija vozila koja zahtijeva fiksnu infrastrukturu (magneti, trake na podu, reflektori). Rade po unaprijed programiranim putanjama, zastaju ispred prepreke, ali je ne mogu sami zaobići.
* **AMR (Autonomous Mobile Robot) / AGF (Automated Guided Forklift):** Moderni autonomni viličari. Koriste prirodnu navigaciju (SLAM) i senzore kako bi se samostalno kretali u prostoru, bez ugradnje dodatne infrastrukture. Mogu sami mijenjati rutu i zaobilaziti prepreke (dinamičko rutiranje).
* **VNA (Very Narrow Aisle):** Visokoregalni viličari namijenjeni radu u vrlo uskim prolazima gdje vilice idu u stranu, a dižu robu na ekstremne visine (preko 13 metara, npr. Jungheinrich EKX).
* **Hibridni viličar (Dual-mode operation):** Autonomni viličar koji ima zadržane standardne komande (upravljač, papučice, kabinu). Zbog toga čovjek može preuzeti kontrolu u bilo kojem trenutku ako stroj naiđe na problem koji sam ne može riješiti.

## 2. Senzori i arhitektura
* **Drive-by-Wire i Lift-by-Wire:** Tehnologija u kojoj nema fizičkih (mehaničkih) veza između komandi i izvršnih organa. Umjesto sajli i poluga, koriste se elektronički signali koji upravljaju servo motorima za vožnju (Drive) i proporcionalnim ventilima za hidrauliku (Lift).
* **CAN bus (Controller Area Network):** Glavna komunikacijska sabirnica (mreža) unutar viličara otporna na elektromagnetske smetnje. Povezuje mikrokontrolere, senzore i aktuatore kako bi komunicirali u realnom vremenu (milisekunde).
* **LiDAR (Light Detection and Ranging):** Senzor koji pomoću laserskih pulseva mjeri udaljenost do objekata (Time-of-Flight princip). Rotira i crta preciznu mapu okoline. Koristi se za lokalizaciju i detekciju velikih prepreka.
* **Odometrija (Enkoderi):** Senzori na kotačima viličara koji mjere broj okretaja. Problem odometrije je što akumulira grešku čim kotač prokliza.
* **IMU (Inertial Measurement Unit):** Senzor koji sadrži akcelerometar (ubrzanje) i žiroskop (kutna brzina). Koristi se zajedno s odometrijom za precizno praćenje naglih pomaka.
* **ToF (Time-of-Flight) i 3D Kamere:** Kamere koje projiciraju svjetlost i mjere vrijeme povrata, stvarajući time "mapu dubine". Koriste se za semantičko prepoznavanje prostora (prepoznavanje prepreka, paleta).

## 3. Navigacija i algoritmi
* **SLAM (Simultaneous Localization and Mapping):** Algoritam pomoću kojeg viličar ulazi u nepoznat prostor, pomoću lasera crta njegovu kartu, a u isto vrijeme računa gdje se na toj karti nalazi.
* **Graph-SLAM:** Specifična i danas najčešća vrsta SLAM-a gdje se putanja vozila sprema kao "graf". Čvorovi grafa su poze vozila (x, y, kut), a bridovi su odometrijska i laserska ograničenja. Optimizacijom grafa minimizira se greška procjene.
* **Loop Closure (Zatvaranje petlje):** Najvažniji dio Graph-SLAM-a. Kada viličar nakon vožnje ponovno dođe na mjesto gdje je već bio (prepozna ga), on zatvara petlju i na taj način korigira i poništava svu odometrijsku grešku koja se nakupila od zadnjeg posjeta tom mjestu.
* **ICP (Iterative Closest Point):** Matematički algoritam koji rotira i translatira oblake točaka (point clouds) s LiDAR-a tako da se savršeno preklope, čime precizno dobivamo pomak viličara između dva skeniranja.
* **EKF (Prošireni Kalmanov filtar / Sensor Fusion):** Fuzija senzora. Matematički algoritam (matrični račun) koji rješava problem nesavršenih senzora. Prvo odometrijom i IMU-om "predvidi" novo stanje vozila. Zatim, kad dođu podaci s LiDAR-a, izračuna grešku (inovaciju/rezidual) i s pomoću Kalmanovog pojačanja (K) ispravi i korigira predikciju. EKF se bavi nelinearnim sustavima (zato ima "Jakobijeve matrice").
* **Computer Vision (YOLOv5, Mask R-CNN):** Sustavi umjetne inteligencije i dubokih neuronskih mreža. YOLO (You Only Look Once) se u viličarima trenira da od stotina paleta savršeno prepozna točno gdje se nalaze rupe ("džepovi") na paleti (Fork Pocket Detection) te računa njihove 3D koordinate za sigurno ubadanje.

## 4. Sigurnost i standardi
* **ISO 3691-4:** Krovni međunarodni sigurnosni standard (Sveto pismo) za projektiranje i upravljanje autonomnim industrijskim vozilima izdana 2020. godine.
* **ISO 13849-1:** Norma za sigurnosne dijelove upravljačkih sustava.
* **PL d (Performance Level d):** Sigurnosna razina koju zahtijeva norma. Znači da sustav pruža "visoku" sigurnost pri opasnim strojevima i da je tolerancija na greške minimalna.
* **Redundancija (Kategorija 3/4):** Arhitektura "dva kanala". Barem dva procesora, dvoje žice, dva prekidala. Ako jedan kanal otkaže ili da krivi signal, drugi gasi pogon.
* **DC (Diagnostic Coverage):** Dijagnostika. Sposobnost sustava da sam u pozadini stalno ispituje i otkrije preko 90% hardverskih kvarova prije nego postanu opasni.
* **MTTFd (Mean Time to Dangerous Failure):** Srednje vrijeme do opasnog kvara svake komponente (izraženo u godinama). Za PL d mora biti klasificirano kao "visoko" (obično > 30 god).
* **CCF (Common Cause Failure):** Sprječavanje zajedničkog uzroka kvara. Sustav mora biti dizajniran tako da jedna jedina smetnja (npr. prevelika temperatura, EMC zračenje) ne onesposobi istovremeno OBA sigurnosna kanala.
* **Warning i Stop zone (Zaštitne zone):** Radijusi koje stvaraju sigurnosni skeneri pri dnu viličara. **Warning (Žuta zona)** aktivira zvučne/svjetlosne signale i smanjuje brzinu. **Stop (Crvena zona)** aktivira trenutno kočenje bez odgode.
* **Proračun zaustavnog puta (S):** Zona zaustavljanja se računa iz fizike: $S = v \cdot t_{odziv} + \frac{v^2}{2g\mu} + d_{sig}$. Zbog parametra brzine i koeficijenta trenja $\mu$, zone su *dinamičke* – povećavaju se ako viličar vozi brzo i ako je viličar na skliskom (mokrom) podu.

## 5. Menadžment i Softver
* **WMS (Warehouse Management System):** Centralni softver skladišta koji vodi stanje zaliha, lokaciju roba i izdaje radne naloge (npr. SAP EWM).
* **Fleet Manager (Master Control, npr. T-ONE):** Softver koji stoji između WMS-a i viličara. WMS mu samo kaže "Premjesti paletu A u lokaciju B". Fleet manager tada gleda koji je viličar najbliži i koji ima najviše baterije, te vrši dinamičko rutiranje i kontrolu prometa na raskrižjima sprječavajući "Deadlock" (prometni čep/zastoj).
* **VDA 5050 standard:** Najvažniji europski softverski standard za *interoperabilnost*. Njegov razvoj sprječava "vendor lock-in". Pomoću MQTT protokola omogućuje da jedan Fleet manager upravlja mješovitom flotom (zajedno rade Toyota, Jungheinrich i Gideon viličari unutar istog skladišta), koristeći JSON format naredbi (Order, State, Visualization).
* **Industrija 4.0 vs 5.0:** Industrija 4.0 fokusirana je na totalnu automatizaciju, IoT, mreže i zamjenu radne snage. Industrija 5.0 je "human-centric"; u fokus vraća suradnju čovjeka i stroja, održivost, i radnike preusmjerava s grubih poslova na upravljanje i kontrolu.

## 6. Ekonomska opravdanost (Financije)
* **CAPEX (Capital Expenditure):** Kapitalni / početni trošak (kupovina autonomnog viličara, lasera, uvođenje softvera i mapiranje). Kod AMR-a je znatno veći nego kod klasičnog.
* **OPEX (Operational Expenditure):** Operativni godišnji troškovi (plaća vozača, popravci štete na robi, servisi, struja). Kod AMR-a je OPEX drastično manji, čime on stvara uštedu.
* **TCO (Total Cost of Ownership):** Ukupni diskontirani trošak vlasništva tijekom cijelog životnog vijeka stroja.
* **ROI (Return on Investment):** Povrat investicije. Mjeri isplativost u postocima na temelju početnog uloga i diskontirane dobiti/uštede.
* **NPV (Net Present Value):** Neto sadašnja vrijednost. Financijski indikator; ukoliko je veći od 0, znači da projekt donosi pozitivnu vrijednost kompaniji.
* **PBP (Payback Period):** Razdoblje povrata investicije. Vrijeme za koje se investicija vrati. U izračunu u radu za rad u 3 smjene PBP iznosi sjajnih ~18 mjeseci.
* **Sensitivity Analysis (Analiza osjetljivosti):** Pokazuje što se događa s isplativošću ako se promjene tržišni uvjeti. U radu je dokazano da autonomni viličari jako gube isplativost ako se koriste u radu samo u jednoj ili dvije smjene, a isplativost im eksponencijalno raste što više raste cijena radne snage uslijed inflacije.
