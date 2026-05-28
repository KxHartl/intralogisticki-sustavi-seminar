**Kritički izvještaj: Autonomni viličari i industrijska vozila**

Sažetak i ocjena
- **Sažetak:** Seminar pokriva ključne teme tražene u zadatku: usporedbu klasičnih i autonomnih viličara, sigurnosne sustave, navigacijske tehnologije (SLAM, LiDAR, računalni vid), primjere iz industrije (Toyota, Jungheinrich) te prednosti i ograničenja. Tekst je tehnički i uglavnom dobro strukturiran za ciljanu publiku (tehnički kolegij FSB).
- **Ocjena (opći dojam):** Dobro (B). Rad pokazuje poznavanje teme i uključuje matematičke formulacije i reference na standarde. Potrebne su manje dopune radi veće jasnoće, provjerljivosti i praktične primjenjivosti.

**Snage**
- **Obuhvatnost:** Svi traženi elementi prisutni su u dokumentu i organizirani su u logičnim poglavljima.
- **Tehnička dubina:** Uključeni su matematički modeli (proračun zaustavnog puta, SLAM formule, EKF/Graph-SLAM) koji su prikladni za kolegij tehničke razine.
- **Standardi i sigurnost:** Referenca na ISO 3691-4 i ISO 13849-1 te opis PLd i CCF pokazuju svjesnost o funkcijskoj sigurnosti.
- **Industrijski primjeri:** Toyota i Jungheinrich su konkretno opisani; spominjanje VDA 5050 i integracijskih sučelja je korisno.

**Slabosti i nedostaci (po poglavljima)**
- **Uvod / motivacija:** Trebalo bi dodati jasniji kvantitativni motiv (primjerice statistike nesreća/efikasnosti prije i nakon automatizacije) radi boljeg argumentiranja potrebe.
- **Klasični vs autonomni:** Dobra tablica usporedbe, ali nedostaju tipični brojčani podaci (npr. prosječne brzine, produktivnost u paletama/sati, tipični raspon radnih brzina).
- **Sigurnosni sustavi:**
  - Nedostaju primjeri stvarnih provjera i testova (npr. scenariji za verifikaciju PLd, testni slučajevi za CCF).
  - Preporučljivo pojasniti razliku između sigurnosnih lasera za detekciju i senzora za navigaciju (s naglaskom na funkcijsku sigurnost senzora i zahtjeve za certificiranje).
- **Matematika i proračuni:**
  - Formule su korektne, no trebaju jasniji koraci proračuna i numerički primjeri za tipične radne uvjete (tablica parametara: masa, koeficijent trenja, vrijeme odziva).
  - Označiti pretpostavke (npr. da su koeficijenti konstanti) i raspon očekivanih vrijednosti.
- **Navigacija (SLAM, LiDAR, računalni vid):**
  - SLAM sekcija je dobro tehnički objašnjena; nedostaju reference na popularne implementacije (npr. Cartographer, GMapping, RTAB-Map, LOAM) i kratka primjena u intralogistici.
  - Računalni vid za manipulaciju paletama treba uključiti kratak opis robusnosti modela YOLO/Mask R-CNN u industrijskom okruženju (osvjetljenje, oštećene palete) i postupke validacije modela.
- **Primjeri iz industrije:**
  - Opisi Toyote i Jungheinricha su korisni, ali nedostaje eksplicitno navođenje modela/općeg opsega implementacije (npr. broj vozila u slučajevima, mjerljive koristi). Dodati izvode ili poveznice na službene studije slučaja.
- **Prednosti i ograničenja:**
  - Dobre qualitative točke, ali nedostaje kvantitativna analiza povrata ulaganja (CAPEX vs OPEX) s primjerima amortizacije.
  - Nije dovoljno naglašena situacijska ograničenja (npr. neravnomjeran pod, promjene u rasporedu regala, sezonske fluktuacije u radnom opterećenju).

**Preporučene izmjene i konkretni prijedlozi**
- **Dodati numeričke primjere:** U poglavlje o zaustavnom putu uvrstiti tablicu s nekoliko scenarija (npr. v=1 m/s, 1.5 m/s, 2 m/s) i izračunima koristeći zadane parametre. Jasno navesti sve ulazne parametre i njihove jedinice.
- **Proširiti ilustracije i dijagrame:** Dodati skicu sigurnosnih zona (warning/stop) i primjer faktor-grafa za Graph-SLAM. Slike poboljšavaju razumijevanje na preglednom seminaru.
- **Ojačati odjeljak o testiranju sigurnosti:** Navesti primjere testnih scenarija, izvještaja o verifikaciji i praktičnu proceduru (npr. MTTF, Proof Test Interval) za PLd komponente.
- **Referencirati implementacije SLAM-a i senzora:** Dodati kratke opise i reference na open-source i komercijalne alate (Cartographer, LOAM, RTAB-Map, Velodyne/ Ouster / Hokuyo senzori) — dovoljno za studente da dalje istraže.
- **Primjeri i podaci iz prakse:** Gdje je moguće, navesti službene studije slučaja (Toyota Autopilot/T-ONE, Jungheinrich EKX serija) sa sažetim brojčanim rezultatima (uvedena vozila, poboljšanje produktivnosti, ROI) ili napomenuti da izvori trebaju biti dodani ako nisu dostupni.
- **Bibliografija i citati:** Provjeriti `main-blx.bib` i osigurati da su sve ključne reference (ISO standardi, VDA 5050, relevantni radovi za SLAM i računalni vid) adekvatno citirane. Predložiti dodavanje 5–8 preporučenih izvora za daljnje čitanje.

**Preporučena dodana literatura (primjeri)**
- ISO 3691-4: Driverless industrial trucks — relevantni dijelovi (navesti u bibliografiji).
- ISO 13849-1: Safety-related parts of control systems.
- VDA 5050: Standard komunikacije za AGV/AMR flote.
- D. Fox, W. Burgard, S. Thrun: "Probabilistic Robotics" — poglavlje o lokalizaciji i SLAM-u (kao obavezno dodatno čitanje).
- Recent review articles (2020–2025) o upotrebi LiDAR/vision u intralogistici (ako dostupno — dodati specifične ref.)

**Mali prijedlozi za LaTeX/strukturu (nemojte mijenjati sada, samo prijedlozi)**
- Ojačati opise slika s jasno navedenim jedinicama i legendama.
- Uvesti numerirane primjere ("Primjer 1", "Primjer 2") uz kratki numerički prikaz rezulta.
- Provjeriti dosljednost oznaka (npr. PLd → pisati uvijek isti oblik) i stil citiranja.

**Zaključak**
- Seminar je tehnički solidan i pokriva tražene smjernice; preporučujem manje dopune kako bi rad postao jači u praktičnoj primjeni i provjerljivosti tvrdnji. Najvažnije dopune: numerički primjeri, dodatne reference/studije slučaja, jasnije razdvajanje sigurnosnih i navigacijskih funkcija, te više praktičnih testnih scenarija za validaciju sustava.

Ako želite, mogu:
- pripremiti detaljan LaTeX diff s predloženim dijagramima i tablicama, ili
- generirati PDF s anotacijama iz ovog izvještaja.

---

Izvještaj generiran za kolegij: Automatizirani intralogistički sustavi (FSB).
