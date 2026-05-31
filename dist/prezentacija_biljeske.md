# Bilješke za prezentaciju: Autonomni viličar i industrijska vozila

**Trajanje:** ~10 minuta
**Pravilo:** Pričati tečno, ne čitati sa slajdova, fokus na poantu svakog slajda.

---

### Slajd 1: Naslovna
* **Akcija:** Uspostaviti kontakt očima s publikom, lagani smješak.
* **Ključne riječi:** Dobar dan svima, pozdrav komisiji i kolegama. Ja sam Krešimir Hartl, a tema mog završnog/diplomskog rada su automatizirani intralogistički sustavi, s fokusom na autonomne viličare.
* **Prijelaz:** *Krenimo kratko s pregledom onoga što ćemo danas proći.*

### Slajd 2: Pregled izlaganja
* **Akcija:** Kratko i jasno, ne zadržavati se.
* **Ključne riječi:** Evolucija sustava, sigurnosni aspekti koji su ključni, tehnologije navigacije koje to omogućuju, konkretni primjeri iz industrije i na kraju ekonomska isplativost.
* **Prijelaz:** *Prije nego što zaronimo u tehnologiju, postavlja se pitanje - zašto uopće automatizirati?*

### Slajd 3: Kontekst - Zašto se intralogistika automatizira?
* **Akcija:** Naglasiti brojke.
* **Ključne riječi:** Dva su glavna motiva. Prvi je sigurnost – 15% ozljeda otpada na viličare. Drugi je pritisak tržišta – e-trgovina raste 20% godišnje, traži se 24/7 dostupnost koju ljudi teško prate zbog manjka radne snage. Od prvog AGV-a 1953. do danas, tehnologija drastično napreduje.
* **Prijelaz:** *Kako je ta tehnologija napredovala, najbolje vidimo kroz razliku između klasičnih, AGV i AMR sustava.*

### Slajd 4: Klasični -> AGV -> autonomni (AMR)
* **Akcija:** Objasniti razliku između AGV i AMR (najčešće pitanje).
* **Ključne riječi:** Klasični viličar ovisi isključivo o čovjeku. AGV vozila kreću se po fiksnim linijama i žicama – ona su pouzdana, ali kruta. AMR, odnosno moderni autonomni viličari, slobodno navigiraju prostorom prepoznajući okolinu, ne trebaju nikakvu vanjsku infrastrukturu i rute su im dinamične.
* **Prijelaz:** *Kao i kod automobila, autonomija ne dolazi preko noći. Imamo razine.*

### Slajd 5: Razine autonomije 0–5
* **Akcija:** Povezati sa SAE auto-standardima (Tesla i sl.).
* **Ključne riječi:** Sustav ima 6 razina. Od nule gdje čovjek radi sve, preko razine 2 gdje viličar prati crtu a čovjek ubada paletu, do razine 5 koja je "sveti gral" – flota se sama dogovara i radi u potpuno dinamičnom okruženju. Danas smo operativno najčešće na razinama 3 i 4.
* **Prijelaz:** *Da bismo klasični viličar doveli na te razine, moramo mu promijeniti anatomiju.*

### Slajd 6: Tehnička arhitektura: 4 podsustava
* **Akcija:** Fokus na "by-wire".
* **Ključne riječi:** Fizičke poluge se miču. Imamo Drive-by-Wire za vožnju i Lift-by-Wire za dizanje paleta – sve se kontrolira električnim signalima. CAN bus je "živčani sustav" koji povezuje komponente s "mozgom" – Vehicle kontrolerom koji donosi odluke u milisekundama.
* **Prijelaz:** *A taj mozak, prije svega ostalog, mora osigurati da vozilo nikoga ne ozlijedi.*

### Slajd 7: Sigurnost - Funkcijska sigurnost
* **Akcija:** Ozbiljan ton, standardi su kritični.
* **Ključne riječi:** Radimo sa strojevima od nekoliko tona. Standard ISO 3691-4 traži takozvanu PL d razinu sigurnosti. To znači da sustav mora biti dvo-kanalni (redundancija). Ako otkaže jedan senzor, drugi preuzima i zaustavlja viličar. Također, sustav kontinuirano sam sebe testira (dijagnostika).
* **Prijelaz:** *A kako vozilo u praksi izbjegava sudare? Putem zaštitnih zona.*

### Slajd 8: Zaštitne zone i zaustavni put
* **Akcija:** Pokazati rukom/laserom na dijagram i formulu (ne objašnjavati formulu detaljno, samo ovisnosti).
* **Ključne riječi:** Imamo "Warning zonu" (žuto) gdje vozilo usporava i svira, te "Stop zonu" (crveno) gdje naglo koči. Zone nisu statične – one dišu. Brže vozilo = veća zona. Formula točno računa zaustavni put ovisno o brzini i trenju podloge (vidi se razlika suho vs mokro).
* **Prijelaz:** *Da bi viličar znao da mu je netko u zoni, treba senzore.*

### Slajd 9: Senzorski sustav
* **Akcija:** Brzo proći kroz senzore.
* **Ključne riječi:** Oslanjamo se na fuziju. LiDAR laseri crtaju 2D i 3D mapu prostora. 3D kamere razumiju scenu – vide paletu. IMU i enkoderi mjere koliko smo se pomaknuli (odometrija), a sigurnosni skeneri paze isključivo na noge i prepreke.
* **Prijelaz:** *Svi ti senzori hrane glavni algoritam intralogistike – SLAM.*

### Slajd 10: SLAM
* **Akcija:** Objasniti laički i inženjerski.
* **Ključne riječi:** SLAM (Simultaneous Localization and Mapping). Viličar istovremeno crta kartu nepoznatog prostora i računa svoju poziciju na njoj. Koristi se Graph-SLAM. Najvažniji koncept tu je "Loop closure" – kada viličar prepozna mjesto na kojem je već bio, ispravlja svu nakupljenu grešku u karti.
* **Prijelaz:** *Problem kod SLAM-a je što senzori griješe. Zato ih moramo "spojiti".*

### Slajd 11: Fuzija senzora – Prošireni Kalmanov filtar
* **Akcija:** Fokus na logiku predikcije i korekcije.
* **Ključne riječi:** Odometrija kotača radi brzo, ali gubi točnost s vremenom zbog proklizavanja (drift). LiDAR je točan, ali spor. Zato koristimo Prošireni Kalmanov filtar (EKF). On spaja ta dva svijeta: prvo predvidi poziciju brzim senzorima, a onda ju korigira preciznim mjerenjem s LiDAR-a. Rezultat je stabilna i točna lokacija u realnom vremenu.
* **Prijelaz:** *No, viličaru nije dovoljno samo znati gdje je on, mora znati i gdje je paleta.*

### Slajd 12: Računalni vid: detekcija džepova palete
* **Akcija:** Skrenuti pažnju na sliku prepoznavanja.
* **Ključne riječi:** Paleta često stoji ukoso, ili je oštećena. Tu uskače 3D kamera i neuronske mreže (YOLOv5, Mask R-CNN). Viličar gleda, detektira tzv. "džepove" za vilice i u letu korigira svoju putanju kako bi savršeno ubo paletu, uz uspješnost preko 90%.
* **Prijelaz:** *Tehnologija je spremna. Pogledajmo kako to izgleda kod pravih proizvođača.*

### Slajd 13: Primjeri iz industrije - Toyota
* **Akcija:** Navesti najbitnije specifičnosti pojedinog proizvođača.
* **Ključne riječi:** Toyota radi Autopilot viličare na bazi svojih klasičnih modela. Ključ je njihov softver "T-ONE" koji služi kao prometni policajac (Traffic control) i dinamčki rutira desetke viličara kroz skladište bez sudara i zastoja.

### Slajd 14: Primjeri iz industrije - Jungheinrich
* **Ključne riječi:** Jungheinrich dominira uskim prolazima (VNA). Njihov EKX model diže teret na 13 metara s milimetarskom preciznošću. Imaju "Logistics Interface" – plug-and-play sustav koji se lako spaja na postojeće softvere skladišta bez skupog programiranja.

### Slajd 15: Primjeri iz industrije - Gideon
* **Ključne riječi:** Naš domaći Gideon pristupio je problemu vizualno. Ne oslanjaju se toliko na LiDAR koliko na duboke 3D kamere. Zbog toga se mogu snalaziti u nevjerojatno kaotičnim okruženjima poput utovara i istovara kamionskih prikolica, što mnogi konkurenti ne mogu.
* **Prijelaz:** *Sve to zvuči sjajno, no idemo biti realni.*

### Slajd 16: Prednosti i ograničenja
* **Akcija:** Uravnotežiti entuzijazam s inženjerskom realnošću.
* **Ključne riječi:** Prednosti su jasne – neprekidan siguran rad, bez oštećenja robe. Ograničenja: jako su osjetljivi na prekid Wi-Fi veze, zahtijevaju podove visoke kvalitete jer svako proklizavanje kvari navigaciju, i prozirna streč folija zbunjuje lasere.
* **Prijelaz:** *A kakva je ekonomska računica?*

### Slajd 17: Isplativost: troškovi kroz 5 godina
* **Akcija:** Brzo objasniti graf.
* **Ključne riječi:** Autonomni viličar u startu košta tri puta više od klasičnog. Međutim, kroz 5 godina rada u tri smjene, eliminacija troška tri operatera dovodi do nevjerojatne računice. Točka pokrića (ROI) događa se već za oko 18 mjeseci, nakon čega sustav generira čisti profit od oko 150k eura uštede.
* **Prijelaz:** *Što nas dovodi do zaključka i pogleda u budućnost.*

### Slajd 18: Industrija 5.0 - Sinergija čovjeka i stroja
* **Akcija:** Poentirati glavnu misao.
* **Ključne riječi:** Intralogistika je od žica na podu pedesetih došla do umjetne inteligencije. Industrija 5.0 nam kaže da ovi viličari neće eliminirati ljude, već preuzeti dosadnu i opasnu rutinu. Cilj je hibridni rad (sinergija) gdje čovjek rješava nestandardne zadatke. A standard VDA 5050 omogućit će miješanje Toyote, Jungheinricha i Gideona u istoj floti.
* **Prijelaz:** *S time bih završio svoj izlaganje.*

### Slajd 19: Hvala na pozornosti!
* **Akcija:** Zahvala, s pauzom.
* **Ključne riječi:** Hvala vam na pažnji. Ovdje sam pripremio nekoliko otvorenih pitanja (pripada li odgovornost kod nesreće viličaru, isplativost za mala poduzeća...) ukoliko ih se želimo dotaknuti, a sada sam otvoren za sva vaša pitanja.
