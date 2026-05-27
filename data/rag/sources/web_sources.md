# Izvori prikupljeni s weba — Autonomni viličari i industrijska vozila

Ova datoteka sadrži sažetke i tehničke specifikacije prikupljene iz javno dostupnih materijala vodećih proizvođača i regulatornih tijela za potrebe pisanja seminarskog rada.

## 1. Povijesni razvoj i definicije (AGV vs. AMR)
- **Barrett Electronics (1953.)**: Razvio prvo "driverless" vozilo koje je pratilo žicu u podu skladišta.
- **AGV (Automated Guided Vehicle)**: Tradicionalna automatizirana vozila koja se kreću po fiksnim stazama (induktivni vodiči, magnetske trake, reflektori). Niska fleksibilnost, zaustavljaju se ispred prepreka.
- **AMR (Autonomous Mobile Robot)**: Autonomni mobilni roboti koji koriste napredne senzore (LiDAR, kamere, SLAM) za dinamičko izbjegavanje prepreka i planiranje ruta bez fizičke infrastrukture.
- **Konvergencija**: Hibridna rješenja spajaju robusnost AGV-a s inteligencijom AMR-a ("Sliding Scale Autonomy").

## 2. Sigurnosni standardi i sustavi (ISO 3691-4)
- **ISO 3691-4**: Glavni međunarodni standard za industrijska vozila bez vozača. Definira zahtjeve za funkcijsku sigurnost sustava upravljanja (SRP/CS).
- **PLd (Performance Level d)**: Zahtijeva se za sustave detekcije osoba i kočenja (prema ISO 13849-1). To uključuje redundantnost i visoku dijagnostičku pokrivenost.
- **Senzori**:
  - Sigurnosni laserski skeneri s dinamičkim zonama koje se prilagođavaju brzini i kutu zakretanja.
  - Taktilni branici (bumpers) osjetljivi na dodir.
  - Svjetlosni i zvučni signali (plavo svjetlo "blue light", blinkeri, sirene).
  - Tipke za hitno zaustavljanje (E-stop) na vidljivim i dostupnim mjestima.

## 3. Navigacijski sustavi i Fuzija Senzora
- **SLAM (Simultaneous Localization and Mapping)**: Algoritam koji omogućuje vozilu da istovremeno izrađuje kartu nepoznatog prostora i lokalizira se unutar nje.
- **LiDAR (Light Detection and Ranging)**: Emitira laserske pulseve i mjeri vrijeme povrata za izradu preciznih 2D ili 3D oblaka točaka (point clouds).
- **Računalni vid (Computer Vision)**: Koristi 3D Time-of-Flight (ToF) kamere i AI algoritme za prepoznavanje paleta, detekciju džepova za vilice, čitanje kodova i prepoznavanje pješaka.
- **Fuzija senzora (Sensor Fusion)**: Integracija podataka iz različitih izvora pomoću EKF-a (Extended Kalman Filter):
  - **IMU** (Inertial Measurement Unit): Mjeri ubrzanje i kutnu brzinu za kratkoročnu visoku frekvenciju pozicioniranja.
  - **Odometrija**: Mjeri okrete kotača, sklona proklizavanju (akumulacija pogreške).
  - **Ultrazvučni senzori**: Za detekciju prozirnih ili sjajnih prepreka na malim udaljenostima.

## 4. Primjeri iz industrije
- **Toyota Material Handling**:
  - Tehnologija **Autopilot**: Automatizacija standardnih Toyota/BT viličara (stackeri SAE160,CDI120). Podržava dualni način rada (ručno/autonomno).
  - Softver **T-ONE**: Središnji sustav za upravljanje flotom (fleet manager) koji se integrira s WMS-om i optimizira rute.
- **Jungheinrich**:
  - Automatizirana vozila (npr. EZS 350a, EKX 516a za uske prolaze - VNA).
  - **Logistics Interface**: Vlastiti middleware koji omogućuje izravnu komunikaciju viličara s klijentskim WMS/ERP sustavima bez potrebe za kompliciranim prilagodbama.
  - Podrška za standard **VDA 5050** za interoperabilnost različitih proizvođača.
- **Balyo**: Koristi 3D kamere i vizijski SLAM za automatsku konverziju standardnih viličara u visokoregalne autonomne viličare.
- **Vecna Robotics**: Specijalizirani za "brownfield" skladišta s Pivotal™ platformom za orkestraciju rada ljudi i robota.
