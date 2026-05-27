# TASKS – Seminar: Autonomni viličari i industrijska vozila

## Pregled koraka (Status: ZAVRŠENO)

- [x] 1. Planiranje seminara i strukture
- [x] 2. Istraživanje i prikupljanje izvora
- [x] 3. Analiza i razrada sadržaja po poglavljima
- [x] 4. Izrada LaTeX strukture i inicijalnih datoteka
- [x] 5. Pisanje nacrta teksta seminara
- [x] 6. Umetanje slika, tablica i grafikona
- [x] 7. Usklađivanje citata i literature (BibTeX)
- [x] 8. Tehnička provjera, lektura i završni PDF

---

## 1. Planiranje seminara i strukture

**Cilj:** Jasno definirati temu, ciljeve, opseg i strukturu seminara.

**Zadaci:**
- Definirati puni naziv seminara i kolegija.
- Definirati primarnu istraživačku perspektivu (FSB, kolegij Automatizirani intralogistički sustavi).
- Dogovoriti okvirnu duljinu seminara (npr. 10–15 stranica bez priloga).
- Definirati glavna poglavlja i podpoglavlja:
  - Uvod u intralogistiku i ulogu viličara
  - Klasični vs. autonomni viličar
  - Navigacija i percepcija (SLAM, LiDAR, računalni vid)
  - Sigurnosni sustavi autonomnih viličara
  - Primjeri iz industrije (Toyota, Jungheinrich, drugi)
  - Prednosti, ograničenja i izazovi
  - Zaključak i smjernice daljnjeg razvoja
- Za svako poglavlje zapisati kratki opis (2–3 rečenice) što treba biti obrađeno.

**Rezultati:**
- Dokument (npr. `outline.md`) s jasnom strukturom i opisima poglavlja.

---

## 2. Istraživanje i prikupljanje izvora

**Cilj:** Prikupiti relevantne akademske i industrijske izvore koji će biti temelj seminara.

**Zadaci:**
- Pretražiti akademske baze (IEEE Xplore, Scopus, Web of Science, arXiv, MDPI) za ključne pojmove:
  - "autonomous forklift", "automated forklift", "forklift AGV", "warehouse SLAM", "LiDAR navigation", "pallet pose estimation", "forklift safety" itd.
- Identificirati pregledne radove i ključne pojedinačne studije za:
  - SLAM i lokalizaciju u skladištima
  - LiDAR-baziranu navigaciju
  - računalni vid za detekciju paleta, prepreka i ljudi
  - sigurnosne sustave i monitoring rada viličara
- Prikupiti industrijske izvore (whitepapers, tehničke brošure, službene web stranice) za:
  - Toyota Material Handling (AGV/Autopilot sustavi)
  - Jungheinrich AGV i automatizirana skladišna rješenja
  - eventualno druge proizvođače (KION/Linde, STILL, Crown) ako je potrebno.
- Za svaki izvor zabilježiti:
  - puni bibliografski podatak (autori, naslov, časopis/konferencija, godina)
  - kratki sažetak (2–4 rečenice) i glavne doprinose
  - potencijalna poglavlja seminara gdje će se izvor koristiti.

**Rezultati:**
- Datoteka `sources.bib` (BibTeX) s inicijalnim popisom literature.
- Datoteka `sources_notes.md` sa sažecima i napomenama po izvorima.

---

## 3. Analiza i razrada sadržaja po poglavljima

**Cilj:** Za svako poglavlje precizno definirati probleme, koncepte i primjere koji će se obraditi.

**Zadaci:**
- Poglavlje "Klasični vs. autonomni viličar":
  - Definirati tehničke razlike (senzori, aktuatori, kontrola).
  - Definirati organizacijske razlike (potreba za vozačima, ergonomija, sigurnost, fleksibilnost).
  - Razraditi tipične scenarije primjene za svaki tip.
- Poglavlje "Navigacija i percepcija":
  - Razložiti podteme: lokalizacija, mapiranje, planiranje putanje, detekcija prepreka.
  - Za svaki senzorski princip (LiDAR, kamera, kombinirani sustavi) navesti tipične algoritme i ograničenja.
  - Identificirati specifične probleme (npr. promjenjivi layout skladišta, dinamičke prepreke, refleksije).
- Poglavlje "Sigurnosni sustavi":
  - Popisati relevantne sigurnosne norme (npr. ISO/EN za industrijska vozila).
  - Opisati funkcionalnu sigurnost (redundantni senzori, sigurnosni PLC, emergentni stop).
  - Opisati sustave za detekciju ljudi (AI vizija, sigurnosni skeneri), zone usporavanja i zaustavljanja.
- Poglavlje "Primjeri iz industrije":
  - Odabrati 2–3 konkretna sustava (npr. Toyota Autopilot viličar, Jungheinrich AGV model).
  - Za svaki sustav opisati: tip vozila, način navigacije, razinu autonomije, tipične primjene.
  - Usporediti karakteristike u tablici.
- Poglavlje "Prednosti, ograničenja i izazovi":
  - Sistematično navesti tehničke, ekonomske i organizacijske prednosti.
  - Navesti ograničenja i otvorene istraživačke probleme.

**Rezultati:**
- Datoteka `chapters_plan.md` s detaljnim planom sadržaja po poglavljima.

---

## 4. Izrada LaTeX strukture i inicijalnih datoteka

**Cilj:** Pripremiti funkcionalan LaTeX projekt temeljen na postojećem git templatu.

**Zadaci:**
- Klonirati ili inicijalizirati git repozitorij na temelju tvog LaTeX seminara templata.
- Prilagoditi osnovne datoteke:
  - `main.tex` – naslov, autor, kolegij, datum, struktura poglavlja.
  - Uključivanje potrebnih paketa (grafika, tablice, citiranje, hrvatska slova itd.).
- Kreirati zasebne `.tex` datoteke po poglavljima (npr. `01_uvod.tex`, `02_klasicni_vs_autonomni.tex`, ...), ako to tvoj template podržava.
- Podesiti `biblatex` ili `natbib` prema preferencijama templata.
- Dodati osnovni Makefile ili skriptu (npr. `make pdf`) za kompajliranje.

**Rezultati:**
- Funkcionalan LaTeX projekt koji se kompajlira u prazan kostur PDF seminara.

---

## 5. Pisanje nacrta teksta seminara

**Cilj:** Napraviti puni prvi nacrt teksta, bez perfekcionizma, ali s uvezanim citatima.

**Zadaci:**
- Za svako poglavlje:
  - Pretvoriti bilješke iz `chapters_plan.md` u koherentni tekst (2–5 stranica po glavnom poglavlju, ovisno o opsegu).
  - Umetnuti citate u LaTeX formatu (npr. `\cite{autor_godina}`).
  - Paziti na logičan tok: od općeg prema konkretnom, od teorije prema primjerima.
- Po potrebi napraviti kratke prijelaze između poglavlja (1–2 rečenice koje povezuju teme).
- Ostaviti "TODO" komentare u LaTeX kodu gdje nedostaju slike ili tablice.

**Rezultati:**
- Prvi kompilirani PDF s punim tekstom, bez nužno finalnih slika/tablica.

---

## 6. Umetanje slika, tablica i grafikona

**Cilj:** Vizualno i strukturalno obogatiti seminar.

**Zadaci:**
- Odabrati 3–6 ključnih slika:
  - shema autonomnog viličara (senzori, aktuatori)
  - ilustracija navigacije (mapa skladišta, SLAM karta)
  - primjeri industrijskih rješenja (Toyota, Jungheinrich) – poštujući autorska prava.
- Izraditi tablice:
  - usporedba klasični vs. autonomni viličar
  - usporedba navigacijskih tehnologija (LiDAR, kamera, magnetske trake itd.)
  - usporedba industrijskih rješenja.
- Ako je potrebno, izraditi jednostavne grafikone (npr. rast tržišta autonomnih viličara, udio vremena rada s i bez zastoja) na temelju javno dostupnih podataka.
- Umetnuti sve slike/tablice/grafikone u odgovarajuća poglavlja i dodati opise (caption) i reference u tekstu.

**Rezultati:**
- Ažurirani PDF s uključenim slikama, tablicama i po mogućnosti grafikonima.

---

## 7. Usklađivanje citata i literature (BibTeX)

**Cilj:** Osigurati da svi citati u tekstu korespondiraju s ispravnim unosima u `.bib` datoteci.

**Zadaci:**
- Proći kroz `main.tex` i sve poglavlja te provjeriti da nema `\cite{}` bez odgovarajućih ključeva u `sources.bib`.
- Provjeriti bibliografske podatke (naslov, autori, godina, naziv časopisa/konferencije).
- Uskladiti stil citiranja prema zahtjevima kolegija (npr. numerički, autor–godina).
- Ponovno kompajlirati dokument i provjeriti da sadržaj literature izgleda konzistentno.

**Rezultati:**
- Čist i konzistentan popis literature, bez BibTeX grešaka.

---

## 8. Tehnička provjera, lektura i završni PDF

**Cilj:** Finalizirati seminar i pripremiti ga za predaju.

**Zadaci:**
- Tehnička provjera:
  - Provjeriti prijelome stranica, prelamanje slika i tablica.
  - Provjeriti da nema "overfull hbox" problema koji narušavaju izgled.
  - Provjeriti sadržaj, popis slika i tablica.
- Lektura:
  - Pročitati cijeli tekst i ispraviti gramatičke i stilističke pogreške.
  - Provjeriti dosljednost terminologije (npr. SLAM, LiDAR, AGV/AMR, viličar, viljuškar – odabrati konzistentne nazive).
- Izraditi finalni PDF (npr. `seminar_autonomni_vilicari_final.pdf`).

**Rezultati:**
- Završni PDF spreman za predaju.
