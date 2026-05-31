# Idealni tekst prezentacije (Skripta za čitanje i vježbu)

*(Smjestite se ugodno ispred publike, uspostavite kontakt očima, lagano se nasmiješite)*

**[Slajd 1: Naslovna]**
Dobar dan svima. Pozdravljam cijenjenu komisiju, mentora profesora Đukića i sve prisutne kolege. Moje ime je Krešimir Hartl, a danas ću vam predstaviti temu svog rada: "Automatizirani intralogistički sustavi, s posebnim fokusom na autonomne viličare i industrijska vozila".

**[Slajd 2: Pregled izlaganja]**
Moje izlaganje podijeljeno je u pet logičnih cjelina. Krenut ćemo s razlikama između klasičnih i autonomnih sustava. Zatim ćemo detaljno obraditi sigurnosne standarde koji su kritični u ovom području. Vidjet ćemo kako teče navigacija pomoću SLAM-a i senzora, pogledati primjere iz industrijske prakse i završiti s ekonomskom analizom isplativosti.

**[Slajd 3: Kontekst]**
Prije nego što zaronimo u tehnologiju, moramo razumjeti zašto uopće automatiziramo intralogistiku? Dva su ključna pokretača. Prvi je sigurnost. Rad s viličarima iznimno je opasan i odgovoran je za čak 15% svih incidenata i ozljeda u skladištima. Drugi razlog je eksplozija e-trgovine i očekivanja potrošača koja rastu 20% godišnje. Od logistike se očekuje rad 24 sata dnevno, 7 dana u tjednu, što je zbog globalnog manjka radne snage s klasičnim viličarima postalo nemoguće pratiti. Zato od 1953. godine i prvih jednostavnih vozila na žicu do danas intenzivno razvijamo automatizaciju.

**[Slajd 4: Klasični -> AGV -> autonomni (AMR)]**
Taj razvoj je najbolje prikazati usporedbom. Klasični viličar ovisi o čovjeku; on je fleksibilan, ali podložan umoru i greškama. Srednji korak bili su AGV sustavi (Automated Guided Vehicles). Oni voze sami, ali se oslanjaju na fizičke vodiče u podu – trake ili magnete. Rade po fiksnim rutama i ne mogu zaobići prepreku. Današnji vrhunac su autonomni mobilni roboti, odnosno AMR viličari. Oni koriste dinamičke rute, sami u realnom vremenu donose odluke, pronalaze alternativne puteve i za navigaciju im nije potrebna nikakva fizička promjena infrastrukture.

**[Slajd 5: Razine autonomije]**
Baš kao i kod cestovnih vozila, intralogistička autonomija stupnjevana je od 0 do 5, što je svojevrsna analogija SAE standardu. Razina 0 je potpuni ručni rad. Razine 1 i 2 pružaju asistenciju vozaču, primjerice usporavanjem u zavoju. Razine 3 i 4 su ono što operativno vidimo danas – vozilo obavlja sve transportne zadatke samostalno unutar svojih zona, ali operater iz kontrolne sobe preuzima nadzor u neočekivanim situacijama. Razina 5 je budućnost – potpuno dinamično okruženje bez definiranih zona gdje flota sama raspodjeljuje zadatke bez imalo ljudske intervencije.

**[Slajd 6: Tehnička arhitektura]**
Da bi standardni viličar postao razina 4, potrebne su mu ozbiljne preinake. Mehaničke poluge i hidraulika zamjenjuju se "by-wire" sustavima – kretanjem upravljaju "Drive-by-Wire" električni signali, a dizanjem paleta proporcionalni ventili "Lift-by-Wire". Kako bi senzori i motori komunicirali u milisekundi, ugrađuje se robusna CAN sabirnica, a sve nadzire "Vehicle Controller" – industrijsko računalo u realnom vremenu koje predstavlja mozak stroja.

**[Slajd 7: Funkcijska sigurnost]**
Taj mozak ima jedan zadatak koji je važniji od same vožnje tereta, a to je sigurnost. Tu na scenu stupa međunarodni standard ISO 3691-4 koji od proizvođača zahtijeva tzv. Performance Level D (PL d). Jednostavno rečeno, svaka komponenta koja utječe na kočenje i zaustavljanje mora biti dvostruka (redundantna). Sustav konstantno sam sebe testira (preko 90% pokrivenosti dijagnostikom), komponente moraju imati izrazito dug vijek trajanja (MTTFd) i dizajn mora spriječiti da jedan vanjski događaj ugasi oba zaštitna kanala. 

**[Slajd 8: Zaštitne zone i zaustavni put]**
U praksi, zaštita se provodi kroz dinamičke zaštitne zone, kao što možete vidjeti na shemi. Imamo žutu "Warning zonu" – ako čovjek tu uđe, viličar usporava i aktivira alarme. Ako čovjek uđe u crvenu "Stop zonu", viličar mora momentalno stati bez sudara. Ove zone nisu fiksne. One se matematički računaju u svakoj stotinki ovisno o brzini vozila i prijanjanju podloge. Pri većoj brzini, zona se širi kako bi sustav kompenzirao dulji zaustavni put.

**[Slajd 9: Senzorski sustav]**
Sve to omogućuje bogat senzorski paket. Prirodna navigacija oslanja se na fuziju. LiDAR laseri preuzimaju ulogu očiju dalekog dometa i služe za izradu 2D i 3D karte prostora. 3D kamere pružaju semantičko razumijevanje, primjerice vide li pred sobom paletu ili čovjeka. Za osjećaj vlastitog gibanja, tu su IMU i enkoderi u kotačima, dok su sigurnosni laserski skeneri pri dnu zaduženi za već spomenute zaštitne zone.

**[Slajd 10: SLAM]**
Senzori skupljaju podatke, ali ih procesira SLAM (Simultaneous Localization & Mapping) algoritam. Viličar ulazi u nepoznato skladište i laserskim skeniranjem gradi njegovu kartu, a istovremeno matematički određuje gdje se nalazi unutar te karte. Moderni viličari koriste pristup zvan Graph-SLAM. Ključna prednost ove metode je takozvani "Loop closure" – kada viličar napravi krug po skladištu i dođe na prepoznato mjesto, on savršeno ispravlja svu akumuliranu sitnu grešku u karti.

**[Slajd 11: Fuzija senzora]**
Međutim, nijedan senzor nije idealan. Enkoderi na kotačima su jako brzi, ali čim kotač malo prokliza na prašini, stvara se greška. Laseri su točni, ali rade na niskoj frekvenciji. Zato koristimo EKF (Prošireni Kalmanov filtar). Matematički spajamo te signale: prvo odometrijom predvidimo novo stanje, a onda ga korigiramo točnim mjerenjem iz LiDAR-a. To zovemo fuzijom senzora koja rezultira robusnom navigacijom.

**[Slajd 12: Računalni vid]**
Ipak, doći do palete je samo pola posla. Treba ju sigurno podići. Palete u praksi često stoje nagnute ili ukoso. Viličar stoga koristi 3D kamere i duboke neuronske mreže poput YOLOv5 ili Mask R-CNN kako bi odradio "Fork Pocket Detection". On u letu detektira rupe za vilice na drvenoj paleti, izračuna 3D koordinate i prilagodi vilice kako bi ubadanje bilo savršeno, uz uspješnost od gotovo 95%.

**[Slajd 13: Primjeri iz industrije - Toyota]**
Pređimo sada s tehnologije na njenu praktičnu primjenu. Toyota, kao gigant u ovom području, razvila je seriju "Autopilot". Umjesto izrade robota od nule, oni autonomiju grade na bazama svojih pouzdanih klasičnih viličara, što izrazito olakšava dostupnost rezervnih dijelova. Srce njihovog sustava je "T-ONE" softver koji poput kontrolora leta dodjeljuje zadatke, rezervira zone i brine se da se desetci viličara nikada ne nađu u "prometnom čepu".

**[Slajd 14: Primjeri iz industrije - Jungheinrich]**
S druge strane imamo Jungheinrich. Oni su posebno jaki u takozvanim VNA (Very Narrow Aisle) sustavima. Njihov autonomni EKX diže robu u uskim prolazima do 13 metara visine, a ono što ga krasi je integracija. Njihov "Logistics Interface" funkcionira kao translator između samih vozila i kompleksnog WMS softvera klijenta, omogućujući plug-and-play implementaciju.

**[Slajd 15: Primjeri iz industrije - Gideon]**
Važno je istaknuti i globalno poznatu hrvatsku tvrtku Gideon. Oni su zauzeli drugačiji pristup - 3D vizualnu autonomiju. Manje se oslanjaju na klasične lasere, a više na dubinske kamere i razumijevanje okoline kroz umjetnu inteligenciju. Zbog toga njihovi viličari mogu robusno raditi u visoko dinamičnim zonama poput utovara i istovara kamionskih prikolica, što tradicionalnim sustavima predstavlja golem problem.

**[Slajd 16: Prednosti i ograničenja]**
Naravno, svaka tehnologija ima dvije strane. Prednosti su jasne: neprekidan rad, otklanjanje problema nedostatka radne snage, drastično povećanje sigurnosti i apsolutna točnost i sljedivost inventara. No, operativni izazovi itekako postoje. Viličari ovise o besprijekornoj Wi-Fi mreži. Ako je pod neravan, dolazi do zanošenja. Optički senzori slabo reagiraju na prašinu ili refleksiju od stretch folije, a strojevi još uvijek nemaju ljudsku prilagodljivost nestandardnim preprekama.

**[Slajd 17: Isplativost: troškovi kroz 5 godina]**
Kad podvučemo crtu, kapitalna investicija (CAPEX) u autonomni viličar je otprilike tri puta veća nego u onaj klasični. No, pogledajte operativne troškove. Kada u graf uključimo trošak tri ljudska operatera u trosmjenskom radu, točka pokrića (Payback Period) događa se nevjerojatno brzo – za oko 18 mjeseci. Kroz životni vijek od 5 godina, jedno autonomno vozilo može generirati i preko 150 tisuća eura čiste uštede tvrtki, uz visok ROI.

**[Slajd 18: Zaključak - Industrija 5.0]**
Za sam kraj, važno je istaknuti – autonomni viličari ne znače kraj ljudi u logistici. Paradigma Industrije 5.0 promiče sinergiju. Hibridni viličari oslobađaju ljude od opasnih i dosadnih noćnih rutina, kako bi čovjek mogao rješavati složene i nestandardne zadatke. Uvođenjem 5G mreža i VDA 5050 standarda za interoperabilnost, svjedočimo budućnosti u kojoj čovjek i mješovite flote pametnih strojeva rade skupa i potpuno sigurno.

**[Slajd 19: Hvala na pozornosti]**
Time bih zaključio svoje izlaganje. Zahvaljujem vam na pozornosti. Na ekranu sam ostavio i nekoliko zanimljivih, otvorenih pitanja za raspravu koja se trenutno lome u industriji, no naravno, sada sam vam na raspolaganju za sva vaša pitanja.
Hvala.
