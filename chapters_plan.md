# Plan po poglavljima (Chapters Plan)

## 1. UVOD
- **Fokus:** Postaviti širu sliku logistike danas (nedostatak radnika, rast e-commerca) i motivaciju za automatizacijom.
- **Ključni elementi:** Kratka povijest od Barrettovog prvog AGV-a (1953) do modernih AMR-ova s umjetnom inteligencijom (Industrija 4.0).
- **Struktura dokumenta:** Kratka najava što donose naredna poglavlja rada.

## 2. KLASIČNI VS. AUTONOMNI VILIČARI
- **Fokus:** Konkretna usporedba dviju tehnologija u pristupu rješavanju istog transportnog problema.
- **Ključni elementi:** Uvođenje sustava Razine 0 do Razine 5. Objašnjavanje Drive-by-wire sustava na koje se nadograđuje računalno upravljanje (CAN bus mreža).
- **Prikazi/Tablice:** Usporedna tablica (ljudi vs. softver, induktivno praćenje vs. prirodna navigacija).

## 3. SIGURNOSNI SUSTAVI
- **Fokus:** Razumijevanje zašto autonomna vozila u tvornici smiju raditi uz ljude bez fizičkih ograda.
- **Ključni elementi:** ISO 3691-4, funkcijska sigurnost (PLd). Pregled komponenti (laserski skeneri, warning/stop zone).
- **Matematika:** Jednadžba zaustavnog puta koja pokazuje eksponencijalni rast zone pri većoj brzini, uključujući vrijeme odziva procesora, koeficijent trenja poda, te hidraulički odziv ventila.

## 4. NAVIGACIJSKE TEHNOLOGIJE
- **Fokus:** Tehnička srž rada — objašnjavanje hardvera i softvera za kretanje.
- **Ključni elementi:** 
  - SLAM matematički model (EKF, vjerojatnosna lokalizacija).
  - LiDAR i računalni vid (YOLO, detekcija rupa na paleti).
  - Fuzija senzora pomoću Extended Kalman Filtera (predikcija + ažuriranje sa senzorom).

## 5. PRIMJERI IZ INDUSTRIJE
- **Fokus:** Prikaz teorije u praksi kod vodećih proizvođača opreme.
- **Ključni elementi:** 
  - **Toyota:** Autopilot, softver T-ONE za dinamičko rutiranje i fleet management.
  - **Jungheinrich:** EKX visokoregalni viličari, Logistics Interface (middleware).
  - **VDA 5050:** Inicijativa standardizacije koja dokida zaključanost uz jednog vendora i definira MQTT API.

## 6. PREDNOSTI I OGRANIČENJA
- **Fokus:** Kritička analiza — tehnologija nije savršena niti besplatna.
- **Ključni elementi:** 
  - Studija isplativosti (TCO, NPV, ROI) koja demonstrira razliku CAPEX vs OPEX u scenariju 3 radne smjene u odnosu na 2 smjene (Analiza osjetljivosti).
  - Ograničenja (roaming WiFi mreže, kvaliteta poda prema DIN 18202, prljavština).

## 7. ZAKLJUČAK
- **Fokus:** Sumiranje rezultata. 
- **Ključni elementi:** Zadržati naglasak na visoki CAPEX koji se amortizira eliminacijom ljudske greške. Pogled u budućnost s naglaskom na 5G mreže i kolaboraciju.
