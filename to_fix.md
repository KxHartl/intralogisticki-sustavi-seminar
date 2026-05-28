To Fix — konkretne upute za doradu seminarskog rada

Cilj
- Doraditi seminar prema `critic_review.md` tako da ostane tehnički, ali čitljiv i lako pratljiv studentima FSB-a.
- Ne dodavati previše novih formula; više praktičnih podataka, primjera, tablica i jasnih objašnjenja.

Općenita pravila
- Ne mijenjati strukturu datoteka osim gdje je označeno ispod (rad u `docs/seminar.tex` i povezanim poglavljima). Nemoj uređivati `dist/`.
- Svaku veću izmjenu ostaviti kao komentirani LaTeX blok (\% TODO: ...) i zabilježiti u ovom dokumentu gdje je izmjena napravljena.
- Držati jezik stručan, ali jasan; definirati sve akronime pri prvom pojavljivanju.

1) Uvod — dodati kvantitativni motiv
- Gdje: neposredno nakon postojećeg uvoda u `docs/seminar.tex` (pogledati odlomke oko "Cilj ovog seminarskog rada...").
- Što dodati: kratak paragraf s 2–3 činjenice (statistika nesreća u skladištima, rast e-trgovine i potreba za 24/7 radom).
- Predloženi tekst (copy/paste):

  "Prema podacima [izvor], skladišni incidenti povezani s radom viličara čine X% svih ozljeda u logistici. Rast elektroničke trgovine od Y% godišnje povećava zahtjeve za operativnom dostupnošću i točnošću isporuke; zato automatizacija intralogistike postaje ključna kako bi se osigurale 24/7 operacije i smanjile pogreške u inventaru."

- Označiti referencu kao `\cite{dzs,ecommerce_report}` i dodati bib unos u `docs/main-blx.bib`.

2) Poglavlje: KLASIČNI VS AUTONOMNI — dopuniti tabelom s primjerima
- Gdje: zamijeniti/obuogatit tablicu usporedbe u `docs/seminar.tex` (tablica s etiketom `tab:usporedba`).
- Što dodati: numeričke orijentire (primjeri vrijednosti) u novu kolonu "Tipični parametri" ili u bilješke pod tablicom.
- Predložak LaTeX-tablice (ubaciti nakon postojeće tablice ili zamijeniti):

  \begin{table}[h]
  \centering
  \caption{Tipični parametri i usporedba}
  \begin{tabular}{lccc}
  \hline
  Karakteristika & Klasični & AGV & Autonomni (AMR) \\
  \hline
  Maks. brzina (m/s) & 1.5–2.0 & 0.8–1.2 & 0.5–1.8 \\
  Preciznost pozicioniranja & operator-dependent & ±10–50 cm & ±1–5 cm (LiDAR/SLAM) \\
  Fleksibilnost promjene rute & visoka (ručno) & niska & vrlo visoka \\
  Tipični scenarij & ručni rad, ad-hoc & stalne trake & dinamično skladište \\
  \hline
  \end{tabular}
  \label{tab:params}
  \end{table}

- Komentar: Ako podaci nisu točni za sve modele, označiti "Tipični raspon" i u fusnoti navesti izvor ili napomenu.

3) SIGURNOSNI SUSTAVI — konkretizirati testove i preporuke
- Gdje: nakon sekcije ISO 3691-4 (u poglavlju SIGURNOSNI SUSTAVI).
- Što dodati: novi podnaslov "Praktična verifikacija i testni scenariji" s listom testova (simulacija pješaka, preispitivanje CCF, provjera PLd kanala, test izdržljivosti senzora u prašini/lošem osvjetljenju).
- Predloženi sadržaj (kratko):
  - Test 1: Detekcija pješaka u warning/stop zoni — reproducirati s čovjekom/pseudopješakom u rastućim udaljenostima.
  - Test 2: Simulacija jednog kanala neuspjeha (prekid signala) — sistem mora sigurno zaustaviti u < t_safe.
  - Test 3: Trajanje i ponovljivost (MTTF/P ležišta) — vođenje zapisa za najmanje 1000 ciklusa.

4) Zaustavni put — pojednostaviti formulu i dodati numeričke primjere
- Gdje: u podsekciji "Matematički model proračuna sigurnosnih zona".
- Što dodati: sažeta formula i tablica s izračunima za 3 scenarija.
- Predložak (LaTeX):

  \begin{equation}
  S = v \cdot t_{odziv} + \frac{v^2}{2 g \mu} + d_{sig}
  \end{equation}

  Tablica primjera:

  \begin{table}[h]
  \centering
  \begin{tabular}{lccc}
  \hline
  Scenarij & v (m/s) & S (m) & Napomena \\
  \hline
  A & 1.0 & 1.3 & suho, $\mu=0.5$, $t_{odziv}=0.2$ s \\
  B & 1.5 & 2.1 & suho \\
  C & 2.0 & 3.5 & mokro, $\mu=0.3$ \\
  \hline
  \end{tabular}
  \caption{Primjeri zaustavnih puteva}
  \end{table}

- Napomena: Ove brojke su primjeri; navesti pretpostavke iznad tablice.

5) NAVIGACIJA (SLAM, LiDAR, računalni vid) — dodati kratke reference i primjer implementacija
- Gdje: u poglavlju SLAM i LiDAR.
- Što dodati: kratke opise popularnih implementacija (Cartographer, LOAM, RTAB-Map), i referencu na "Probabilistic Robotics".
- Dodati figuru-placeholder za faktor-graf (putanja: `docs/slike/graphslam_placeholder.png`) s jednostavnim captionom "Primjer faktor-grafa za Graph-SLAM".
- Kratki tekst: nekoliko rečenica o prednostima 2D vs 3D LiDAR-a u intralogistici.

6) RAČUNALNI VID — praktičnost i validacija
- Gdje: pod "Računalni vid (Computer Vision) u manipulaciji teretom".
- Što dodati: kratka napomena o modelima (YOLOv5/YOLOv8, Mask R-CNN) i koraci validacije (dataset, augmentation, metrika: mAP, success rate for fork pocket detection).
- Dodati malu tablicu s primjerom validacijskih rezultata (fiktivni brojevi kao primjer):

  \begin{tabular}{lcc}
  \hline
  Model & mAP(0.5) & Fork detection rate \\
  \hline
  YOLOv5 & 0.86 & 92% \\
  Mask R-CNN & 0.89 & 94% \\
  \hline
  \end{tabular}

7) PRIMJERI IZ INDUSTRIJE — proširiti s brojevima i izvorima
- Gdje: odjeljak Toyota i Jungheinrich.
- Što dodati: kratke metrike i reference (npr. broj instaliranih vozila, poboljšanje produktivnosti %). Ako se ne može naći točno, ubaciti "Primjer (ilustrativno): Toyota — flota 50 vozila, povećanje throughput-a 20%" i označiti kao "provjeriti izvor".
- Označiti mjesta za dodavanje citata: `\cite{toyota_case}`, `\cite{jungheinrich_case}`.

8) PREDNOSTI I OGRANIČENJA — dodati ROI primjer tablice
- Gdje: poglavlje PREDNOSTI I OGRANIČENJA.
- Što dodati: kratka tablica amortizacije (CAPEX vs OPEX) s nekoliko redaka (vrijednosti su orijentacione):

  \begin{table}[h]
  \centering
  \begin{tabular}{lrr}
  \hline
  Stavka & Godina 0 (CAPEX) & Godišnji OPEX (EUR) \\
  \hline
  Klasično (10 viličara) & 100000 & 250000 \\
  Autonomno (flota 10 AMR) & 500000 & 120000 \\
  \hline
  \end{tabular}
  \caption{Orijentacijski troškovi — primjer}
  \end{table}

- Napomena: Obavezno navesti pretpostavke u fusnoti.

9) BIBLIOGRAFIJA — predloženi BibTeX unosi (dodati u `docs/main-blx.bib`)
- Predloženi minimalni unosi (kopirati i zalijepiti):

  @misc{toyota_case,
    title = {Toyota Autopilot — case study},
    howpublished = {https://www.toyota-forklifts.example},
    year = {2023}
  }

  @misc{jungheinrich_case,
    title = {Jungheinrich AGV solutions},
    howpublished = {https://www.jungheinrich.example},
    year = {2022}
  }

  @book{thrun2006probabilistic,
    title={Probabilistic Robotics},
    author={Thrun, Burgard and Fox},
    year={2006},
    publisher={MIT Press}
  }

  @misc{vda5050,
    title={VDA 5050: Communication interface for AGV/AMR},
    howpublished={https://vda.example},
    year={2021}
  }

  @misc{iso3691_4,
    title={ISO 3691-4: Driverless industrial trucks},
    year={2020}
  }

- Napomena: Zamijeniti `example` URL-ove stvarnim izvorima ako su dostupni.

10) Ilustracije i slike
- Stvoriti privremene placeholder-e u `docs/slike/` s opisom (npr. `graphslam_placeholder.png`, `safety_zones.png`, `fork_detection_example.png`). Agent može koristiti jednostavne SVG/PNG crteže.
- U LaTeX-u ubaciti figure koristeći \includegraphics s odgovarajućim captionom.

11) Stil i dosljednost
- Definirati akronime pri prvom pojavljivanju (npr. AMR, AGV, WMS, ERP, PLd).
- Provjeriti da su sve jedinice (m, s, m/s) dosljedno napisane.

12) Završna verifikacija
- Nakon izmjena, pokrenuti lokalnu kompilaciju (latexmk ili pdflatex/biber/pdflatex x2) i provjeriti da nema grešaka.
- Napraviti kratki changelog u repo poruci ili komentar (ne automatski commit ako nije zatraženo).

Kontakt i napomene
- Ako neki od primjera ili brojeva nisu dostupni, ostaviti oznaku "TODO: potvrditi izvor" u tekstu.
- Ostaviti kratke inline komentare (\% TODO) za svaki važniji dodatak radi brze recenzije.

Kraj — ovo su konkretne upute; agent može početi raditi po točkama redom. Ako želite, pripremit ću i LaTeX patch sa svim predloženim blokovima spremnim za ubacivanje.
