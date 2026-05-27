# Preporuke za slike — Autonomni viličari i industrijska vozila

Ova datoteka sadrži preporuke za slike (fotografije, sheme, dijagrame, grafikone) koje je potrebno samostalno pronaći i umetnuti u LaTeX dokument `seminar.tex` kako bi se vizualno obogatio seminarski rad nakon što su sve privremene slike uklonjene na Vaš zahtjev.

Za svaku sliku navedeno je preporučeno mjesto umetanja, opis sadržaja i predložena LaTeX sintaksa.

---

## 1. Slika: Povijesni razvoj AGV-a (Barrett Electronics Guide-O-Matic, 1953)
* **Preporučeno mjesto:** Poglavlje 1 (UVOD), neposredno nakon 2. odlomka koji opisuje povijesni razvoj (oko retka 130).
* **Opis sadržaja:** Crno-bijela povijesna fotografija ili tehnički crtež prvog automatski vođenog tegljača tvrtke Barrett Electronics koji prati vodič položen u podu skladišta.
* **Predloženi naziv datoteke:** `slika_barrett_1953.png`
* **LaTeX kod za umetanje:**
  ```latex
  \begin{figure}[h]
  \centering
  \includegraphics[width=0.7\textwidth]{slika_barrett_1953.png}
  \caption{Prvo automatski vođeno vozilo (AGV) Guide-O-Matic tvrtke Barrett Electronics (1953.) \cite{barrett}}
  \label{fig:barrett_1953}
  \end{figure}
  ```

---

## 2. Slika: Arhitektura upravljanja klasičnog vs. autonomnog viličara
* **Preporučeno mjesto:** Poglavlje 2 (KLASIČNI VS. AUTONOMNI VILIČARI), na kraju pododjeljka 2.2 "Tehnička arhitektura autonomnog viličara" (oko retka 165).
* **Opis sadržaja:** Blok dijagram koji uspoređuje klasično ručno upravljanje (vozač -> upravljač/hidraulika -> mehaničko gibanje) s autonomnim sustavom (Fleet Manager -> Središnje računalo viličara -> CAN sabirnica -> aktuatori i senzori).
* **Predloženi naziv datoteke:** `arhitektura_upravljanja.png`
* **LaTeX kod za umetanje:**
  ```latex
  \begin{figure}[h]
  \centering
  \includegraphics[width=0.9\textwidth]{arhitektura_upravljanja.png}
  \caption{Shematski prikaz i usporedba arhitekture upravljanja klasičnog i autonomnog viličara}
  \label{fig:arhitektura_upravljanja}
  \end{figure}
  ```

---

## 3. Slika: Prikaz sigurnosnih zona (Stop i Warning) na viličaru
* **Preporučeno mjesto:** Poglavlje 3 (SIGURNOSNI SUSTAVI), na kraju pododjeljka 3.2 "Senzorska sigurnosna arhitektura" (oko retka 200).
* **Opis sadržaja:** Tlocrtni ili bočni prikaz autonomnog viličara s označenim poljima sigurnosnog skenera. Unutarnje polje (crveno) označava zonu zaustavljanja (Stop Zone), a vanjsko polje (žuto/narančasto) označava zonu upozorenja/usporavanja (Warning Zone).
* **Predloženi naziv datoteke:** `sigurnosne_zone_vilicar.png`
* **LaTeX kod za umetanje:**
  ```latex
  \begin{figure}[h]
  \centering
  \includegraphics[width=0.8\textwidth]{sigurnosne_zone_vilicar.png}
  \caption{Konfiguracija i dinamičko prilagođavanje sigurnosnih zona laserskog skenera}
  \label{fig:sigurnosne_zone_detaljno}
  \end{figure}
  ```

---

## 4. Slika: Princip rada LiDAR-a i SLAM lokalizacije
* **Preporučeno mjesto:** Poglavlje 4 (NAVIGACIJSKE TEHNOLOGIJE), na kraju pododjeljka 4.2 "LiDAR tehnologija" (oko retka 240).
* **Opis sadržaja:** Grafički prikaz rotacije laserske zrake LiDAR-a, refleksije sa zidova i stupova skladišta te generiranje oblaka točaka (point cloud) koji se koristi u SLAM algoritmu za usporedbu s učitanom kartom prostora.
* **Predloženi naziv datoteke:** `lidar_slam_princip.png`
* **LaTeX kod za umetanje:**
  ```latex
  \begin{figure}[h]
  \centering
  \includegraphics[width=0.85\textwidth]{lidar_slam_princip.png}
  \caption{Skeniranje okoliša pomoću LiDAR-a i lokalizacija viličara unutar skladišne karte}
  \label{fig:lidar_slam_princip}
  \end{figure}
  ```

---

## 5. Slika: Detekcija džepova palete pomoću računalnog vida (Fork Pocket Detection)
* **Preporučeno mjesto:** Poglavlje 4 (NAVIGACIJSKE TEHNOLOGIJE), neposredno nakon opisa računalnog vida u pododjeljku 4.3 (oko retka 245).
* **Opis sadržaja:** Slika iz perspektive 3D kamere postavljene na nosaču vilica. Prikazuje drvenu paletu s preklopljenim pravokutnicima (bounding boxes) i detektiranim koordinatama otvora za ubadanje vilica.
* **Predloženi naziv datoteke:** `fork_pocket_detection.png`
* **LaTeX kod za umetanje:**
  ```latex
  \begin{figure}[h]
  \centering
  \includegraphics[width=0.75\textwidth]{fork_pocket_detection.png}
  \caption{Prepoznavanje i proračun 3D koordinata džepova palete pomoću konvolucijskih neuronskih mreža}
  \label{fig:fork_pocket}
  \end{figure}
  ```

---

## 6. Slika: Tok podataka i komunikacija prema standardu VDA 5050
* **Preporučeno mjesto:** Poglavlje 5 (PRIMJERI IZ INDUSTRIJE), na kraju pododjeljka 5.3 "Standard VDA 5050 za interoperabilnost" (oko retka 280).
* **Opis sadržaja:** Blok dijagram toka podataka između nadređenog upravljačkog sustava flote (Master Control) i autonomnih vozila različitih proizvođača. Prikazuje MQTT teme: `/order` (naredbe), `/state` (trenutno stanje viličara) i `/visualization`.
* **Predloženi naziv datoteke:** `vda_5050_komunikacija.png`
* **LaTeX kod za umetanje:**
  ```latex
  \begin{figure}[h]
  \centering
  \includegraphics[width=0.9\textwidth]{vda_5050_komunikacija.png}
  \caption{Arhitektura razmjene poruka između flote i Master Control-a sukladno VDA 5050 normi \cite{vda5050}}
  \label{fig:vda5050_shema}
  \end{figure}
  ```

## 7. Slika: Kumulativni novčani tok i točka pokrića (Manual vs. AMR)
* **Preporučeno mjesto:** Poglavlje 6 (PREDNOSTI I OGRANIČENJA), neposredno nakon pododjeljka 6.2 "Ekonomska usporedba i povrat investicije (ROI)" (oko retka 480).
* **Opis sadržaja:** Grafikon koji prikazuje kumulativni novčani tok kroz 5 godina za klasični viličar i autonomni viličar (AMR). Grafikon jasno prikazuje točku pokrića (break-even point) na presjeku krivulja na oko 1.5 godina (18 mjeseci), gdje kumulativni troškovi klasičnog viličara premašuju investiciju u autonomni viličar.
* **Predloženi naziv datoteke:** `break_even_chart.png`
* **LaTeX kod za umetanje:**
  ```latex
  \begin{figure}[h]
  \centering
  \includegraphics[width=0.85\textwidth]{break_even_chart.png}
  \caption{Kumulativni troškovi i točka pokrića (break-even point) klasičnog i autonomnog viličara}
  \label{fig:break_even_chart}
  \end{figure}
  ```

---

## Upute za dodavanje slika u LaTeX:
1. Pronađite ili izradite odgovarajuće slike u formatu `.png` ili `.pdf`.
2. Spremite slike u mapu `docs/` (ili stvorite podmapu `docs/slike/` i dodajte `\graphicspath{{slike/}}` u preambulu).
3. Uklonite komentare ili kopirajte gornje LaTeX blokove na preporučena mjesta u datoteci `docs/seminar.tex`.
4. Ponovno pokrenite skriptu za kompilaciju `.ai/scripts/helpers/build-docs.ps1`.
5. U mapi `docs/build` će se izgenerirati novi PDF sa slikama.
