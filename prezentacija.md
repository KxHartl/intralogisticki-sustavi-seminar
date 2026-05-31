---
marp: true
theme: default
paginate: true
style: |
  section {
    background-color: #FAFAFA; /* svijetlo krem/siva */
    color: #212121; /* gotovo crna za dobru čitljivost */
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  }
  h1 {
    color: #1565C0; /* Plavi highlight za glavne naslove */
    border-bottom: 3px solid #D32F2F; /* Crvena linija ispod naslova */
    padding-bottom: 10px;
  }
  h2 {
    color: #D32F2F; /* Crveni highlight za podnaslove */
  }
  strong {
    color: #1565C0; /* Plava za podebljani tekst */
  }
  .yellow-text {
    color: #FBC02D; /* Žuta za specifične naglaske */
    font-weight: bold;
  }
  .highlight-box {
    background-color: #EEEEEE;
    border-left: 5px solid #FBC02D;
    padding: 10px;
    margin-top: 20px;
  }
---

# Autonomni viličari i industrijska vozila
## u automatiziranim intralogističkim sustavima

<br><br><br>

**Kolegij:** Automatizirani intralogistički sustavi (FSB)

<!-- 
BILJEŠKE ZA IZLAGANJE:
Dobar dan svima. Moje ime je [Tvoje Ime] i danas ću vam prezentirati temu mog seminara: "Autonomni viličari i industrijska vozila u automatiziranim intralogističkim sustavima". Osvrnut ćemo se na brzu evoluciju tehnologije u skladištima i razloge prelaska na autonomiju.
-->

---

# 1. Uvod u Intralogistiku
- **Rast e-trgovine** i **nedostatak radne snage** glavni su pokretači automatizacije.
- Povijesni razvoj: Od prvog AGV-a (1953., tvrtka Barrett) do modernih AMR-ova s umjetnom inteligencijom.
- **Industrija 4.0**: Prijelaz s fiksno vođenih vozila na fleksibilne, pametne robote.

<div class="highlight-box">
Cilj: Povećanje efikasnosti, sigurnosti i praćenja procesa.
</div>

<!--
BILJEŠKE ZA IZLAGANJE:
Uvodno želim istaknuti da intralogistika danas trpi veliki pritisak. Zbog eksplozije e-commerca i kroničnog nedostatka vozača viličara, tvrtke su prisiljene automatizirati procese. Nismo više u eri jednostavnih AGV-ova koji prate crtu na podu, već prelazimo na pametne robote.
-->

---

# 2. Klasični vs. Autonomni Viličari

| Značajka | Klasični viličar | Autonomni viličar |
| :--- | :--- | :--- |
| **Upravljanje** | Vozač (ljudska percepcija) | Senzori i algoritmi (Računalo) |
| **Fleksibilnost** | Visoka (vozač prilagođava) | Ograničena programiranim |
| **Radno vrijeme** | Smjene (potrebni odmori) | 24/7 (samo punjenje baterije) |
| **Sigurnost** | Ovisi o ljudskom faktoru | Deterministička, ugrađena |

- Prijelaz zahtijeva **Drive-by-Wire** i **Lift-by-Wire** sustave (CAN bus mreža).

<!--
BILJEŠKE ZA IZLAGANJE:
Kada uspoređujemo klasične i autonomne viličare, glavna razlika je u nositelju odluke. Kod klasičnog to je čovjek, kod autonomnog računalo. Autonomni viličar zahtijeva potpunu elektrifikaciju kontrola, takozvani "drive-by-wire" gdje računalo preko CAN sabirnice izravno kontrolira motore.
-->

---

# 3. Sigurnosni Sustavi (ISO 3691-4)

- **Ljudi i roboti u istom prostoru**: Zahtijeva stroge sigurnosne standarde bez fizičkih ograda.
- **Funkcijska sigurnost**: Laserski skeneri, taktilni branici (bumpers), redundantni senzori i sigurnosni PLC.
- **Zone zaustavljanja**: 
  - *Warning zona* (usporavanje)
  - *Stop zona* (potpuno zaustavljanje).

<div class="highlight-box">
Matematika: Zaustavni put eksponencijalno raste s brzinom. Uključuje vrijeme odziva procesora, ventila i koeficijent trenja poda.
</div>

<!--
BILJEŠKE ZA IZLAGANJE:
Jedna od najvažnijih tema je sigurnost. Prema standardu ISO 3691-4, autonomna vozila mogu dijeliti prostor s ljudima. To je omogućeno laserskim skenerima od 360 stupnjeva koji prate okolinu u stvarnom vremenu. Ako netko uđe u žutu "warning" zonu, viličar usporava. Ako uđe u crvenu "stop" zonu, trenutno se zaustavlja.
-->

---

# 4. Navigacijske Tehnologije

Kako vozilo zna gdje se nalazi?

- **SLAM** (Simultaneous Localization and Mapping): Istovremeno mapiranje i lokalizacija (npr. EKF-SLAM).
- **LiDAR tehnologija**: Stvaranje 2D i 3D točkastih oblaka za percepciju okoline.
- **Računalni vid (YOLO)**: Detekcija paleta i prepreka pomoću kamera.
- **Fuzija senzora**: Kombiniranje podataka od enkodera, žiroskopa i LiDAR-a za preciznu lokalizaciju (Extended Kalman Filter).

<!--
BILJEŠKE ZA IZLAGANJE:
Srce svakog autonomnog viličara je njegov navigacijski sustav. Danas prevladava SLAM navigacija, najčešće bazirana na LiDAR-u. LiDAR stvara kartu skladišta u stvarnom vremenu. Kombinirajući te podatke s odometrijom preko Extended Kalman Filtera dobivamo fuziju senzora koja viličaru govori njegovu točnu poziciju u milimetar.
-->

---

# 5. Primjeri iz Industrije

1. **Toyota Material Handling**
   - *Autopilot* vozila i *T-ONE* softver za dinamičko rutiranje i upravljanje flotom.
2. **Jungheinrich**
   - EKX visokoregalni viličari i moćni *Logistics Interface* (middleware).
3. **VDA 5050 Standard**
   - **Revolucija interoperabilnosti!**
   - Omogućuje upravljanje viličarima različitih proizvođača kroz isti softver (izbjegava se "vendor lock-in").

<!--
BILJEŠKE ZA IZLAGANJE:
U praksi, lideri na tržištu poput Toyote i Jungheinricha imaju svoja kompletna rješenja. Toyota koristi T-ONE softver, Jungheinrich svoj Logistics Interface. No, ono što je trenutno "vruća" tema je VDA 5050 standard. On definira univerzalni jezik komunikacije, tako da u istom skladištu možemo imati Toyotin viličar i neki drugi AMR, a komuniciraju preko istog sustava.
-->

---

# 6. Prednosti i Ekonomska Isplativost

- **Analiza troškova (CAPEX vs OPEX)**: 
  - Početna investicija (CAPEX) je visoka.
  - Troškovi operacija (OPEX) drastično padaju.
- Najveći ROI (povrat investicije) ostvaruje se u radu na **3 smjene**.
- **Prednosti**: Povećana produktivnost, sigurnost robe (manje oštećenja), točnost inventara.

<!--
BILJEŠKE ZA IZLAGANJE:
Kada gledamo isplativost, autonomni viličari su kapitalno intenzivni. CAPEX je velik na početku, ali operativni troškovi odnosno OPEX znatno padaju jer nemamo trošak vozača i oštećenja robe. Pravi povrat investicije (ROI) najbolje se vidi kada skladište prelazi na rad u tri smjene, jer robot ne traži prekovremene niti ima umor.
-->

---

# 7. Ograničenja i Operativni Izazovi

Iako je tehnologija napredna, postoje prepreke:
- **Kvaliteta poda**: Potreban iznimno ravan pod (DIN 18202 standard).
- **Mreža**: Problemi s Wi-Fi "roamingom" i latencijom u velikim dvoranama.
- **Kognitivna fleksibilnost**: Viličar će stati ako naiđe na prepreku koju vozač može jednostavno zaobići ili maknuti rukom.
- **Prljavština i prašina**: Mogu "zaslijepiti" laserske skenere.

<!--
BILJEŠKE ZA IZLAGANJE:
Važno je biti kritičan – tehnologija nije savršena. Najčešći problemi na terenu su loši podovi koji ne zadovoljavaju DIN standarde, pucanje Wi-Fi veze prilikom prebacivanja s rutera na ruter i preosjetljivost senzora na prašinu. Robotu također nedostaje fleksibilnost čovjeka da jednostavno izađe, makne paletu s puta i nastavi.
-->

---

# 8. Zaključak

- Prestanak ovisnosti o ljudskoj radnoj snazi opravdava visoke početne investicije.
- Eliminacija ljudskih grešaka i povećana sigurnost skladišta.
- **Budućnost**: 
  - Primjena privatnih **5G mreža** za rješavanje latencije.
  - Kolaborativni sustavi gdje roboti i ljudi dijele isti radni prostor u savršenoj sinergiji.

<h2 style="text-align:center; margin-top:50px;">Hvala na pažnji!</h2>

<!--
BILJEŠKE ZA IZLAGANJE:
Zaključno, automatizacija više nije opcija nego nužnost za moderno skladište. Unatoč visokim troškovima, sigurnost i pouzdanost opravdavaju investiciju. U bliskoj budućnosti očekujemo masovnu implementaciju privatnih 5G mreža koje će riješiti probleme s latencijom, a roboti i ljudi radit će zajedno još efikasnije. Hvala na pažnji i stojim na raspolaganju za vaša pitanja.
-->
