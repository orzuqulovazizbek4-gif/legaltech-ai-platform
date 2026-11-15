"""Bilimni tekshirish testi — 10 ta savol, batafsil izohlar bilan."""

QUIZ = [
    {
        "savol": "Davlat va huquq nazariyasida «huquq ijodkorligi» deganda nima tushuniladi?",
        "variantlar": [
            "Sudlarning aniq ishlar bo‘yicha qaror chiqarish faoliyati",
            "Vakolatli subyektlarning huquq normalarini yaratish, o‘zgartirish yoki bekor qilishga qaratilgan faoliyati",
            "Fuqarolarning o‘z huquqlaridan foydalanishi va majburiyatlarini bajarishi",
            "Huquq normalarining mazmunini tushuntirish (talqin qilish) faoliyati",
        ],
        "togri": 1,
        "izoh": (
            "Huquq ijodkorligi — vakolatli davlat organlarining (qonunda nazarda tutilgan hollarda bevosita xalqning) "
            "huquq normalarini yaratish, o‘zgartirish yoki bekor qilishga qaratilgan faoliyati. Birinchi variant — "
            "huquqni qo‘llash, uchinchisi — huquqni amalga oshirish, to‘rtinchisi — huquqni talqin qilishdir. Bu "
            "jarayon «Normativ-huquqiy hujjatlar to‘g‘risida»gi O‘RQ-682-son Qonun bilan tartibga solinadi."
        ),
    },
    {
        "savol": "Normativ-huquqiy hujjatlar loyihalarining jamoatchilik muhokamasi qaysi portal orqali o‘tkaziladi?",
        "variantlar": [
            "lex.uz",
            "my.gov.uz",
            "regulation.gov.uz",
            "data.egov.uz",
        ],
        "togri": 2,
        "izoh": (
            "regulation.gov.uz — Normativ-huquqiy hujjatlar loyihalari muhokamasi portali; u e-demokratiyaning huquq "
            "ijodkorligidagi asosiy vositasidir. Lex.uz — qabul qilingan hujjatlar e’lon qilinadigan Qonunchilik "
            "ma’lumotlari milliy bazasi, my.gov.uz — Yagona interaktiv davlat xizmatlari portali."
        ),
    },
    {
        "savol": "Lourens Lessig nazariyasiga ko‘ra kibermakonda «arxitektura» vazifasini bajarib, xulq-atvorni tartibga soluvchi omil qaysi?",
        "variantlar": [
            "Sud pretsedenti",
            "Dasturiy kod",
            "Xalqaro shartnoma",
            "Huquqiy odat",
        ],
        "togri": 1,
        "izoh": (
            "Lessig («Code and Other Laws of Cyberspace», 1999) to‘rt regulyatorni ajratadi: huquq, ijtimoiy normalar, "
            "bozor va arxitektura. Kibermakonda arxitektura — dasturiy kod: u nimaga ruxsat berilishini texnik jihatdan "
            "oldindan belgilaydi. «Code is Law» tezisi shundan kelib chiqqan, biroq u kodning qonundan ustunligini "
            "anglatmaydi."
        ),
    },
    {
        "savol": "Smart-kontraktdagi «ELSE — aks holda penya avtomatik ushlab qolinadi» qismi huquq normasining qaysi elementiga mos keladi?",
        "variantlar": [
            "Gipoteza",
            "Dispozitsiya",
            "Sanksiya",
            "Preambula",
        ],
        "togri": 2,
        "izoh": (
            "Huquq normasi tuzilishi: gipoteza (shart — `IF`), dispozitsiya (xulq-atvor qoidasi — `THEN`), sanksiya "
            "(qoidani buzganlik uchun noqulay oqibat — `ELSE`). Penyaning ushlab qolinishi — majburiyat buzilishining "
            "noqulay oqibati, ya’ni sanksiya."
        ),
    },
    {
        "savol": "Prezidentning 2021-yil 17-fevraldagi PQ-4996-son qarorida nazarda tutilgan sun’iy intellekt uchun «maxsus rejim» nazariy jihatdan qaysi institutga mos keladi?",
        "variantlar": [
            "Huquqiy prezumpsiya",
            "Regulatory Sandbox — eksperimental huquqiy rejim",
            "Huquqiy fiksiya",
            "Kodifikatsiya",
        ],
        "togri": 1,
        "izoh": (
            "Maxsus rejim — «tartibga solish qumdoni» (Regulatory Sandbox): cheklangan ishtirokchilar uchun, muayyan "
            "muddatga va nazorat ostida yangi texnologiyalarni sinash imkonini beruvchi eksperimental huquqiy rejim. "
            "PQ-4996-son qaror «Sun’iy intellekt texnologiyalarini jadal joriy etish uchun shart-sharoitlar yaratish "
            "chora-tadbirlari to‘g‘risida» deb nomlanadi."
        ),
    },
    {
        "savol": "Amaldagi O‘zbekiston qonunchiligiga ko‘ra sun’iy intellekt tizimining huquqiy maqomi qanday?",
        "variantlar": [
            "Cheklangan huquq layoqatiga ega «elektron shaxs»",
            "Yuridik shaxsning alohida turi",
            "Huquq obyekti; uning harakatlari oqibati uchun tegishli jismoniy va yuridik shaxslar javob beradi",
            "Jinoyat huquqining maxsus subyekti",
        ],
        "togri": 2,
        "izoh": (
            "Amaldagi huquqda sun’iy intellekt — huquq obyekti (dasturiy ta’minot, mol-mulk). «Elektron shaxs» "
            "(kvazi-subyekt) — Yevropa Parlamentining 2017-yilgi rezolyutsiyasida muhokama qilingan doktrinal taklif, "
            "xolos. Jinoyat subyekti esa faqat aqli raso, tegishli yoshga to‘lgan jismoniy shaxs bo‘lishi mumkin."
        ),
    },
    {
        "savol": "Fuqarolik kodeksining 999-moddasiga ko‘ra oshiqcha xavf manbaiga egalik qiluvchi shaxs yetkazilgan zarar uchun qanday javob beradi?",
        "variantlar": [
            "Faqat qasddan zarar yetkazgan bo‘lsa",
            "Faqat uning aybi sud tomonidan isbotlangan taqdirda",
            "Aybidan qat’i nazar, agar zarar yengib bo‘lmas kuch yoki jabrlanuvchining qasdi oqibatida kelib chiqqanini isbotlay olmasa",
            "Hech qanday holatda javob bermaydi, zarar davlat hisobidan qoplanadi",
        ],
        "togri": 2,
        "izoh": (
            "FK 999-moddasi aybsiz (qat’iy) javobgarlikni belgilaydi: oshiqcha xavf manbaiga egalik qiluvchi faqat "
            "yengib bo‘lmas kuch yoki jabrlanuvchining qasdini isbotlasa, javobgarlikdan ozod bo‘ladi. Doktrinada "
            "avtonom transport va robotlar yetkazgan zarar uchun javobgarlik aynan shu norma analogiyasi bilan "
            "asoslanadi; zararni qoplagan egalik qiluvchi ishlab chiquvchiga regress talabi qo‘yishi mumkin."
        ),
    },
    {
        "savol": "Nima uchun jinoyat huquqida qonunni o‘xshashlik (analogiya) bo‘yicha qo‘llash taqiqlangan?",
        "variantlar": [
            "Chunki jinoyat ishlari juda ko‘p va sudlar analogiyaga vaqt topa olmaydi",
            "Chunki Jinoyat kodeksining 4-moddasiga ko‘ra qilmishning jinoiyligi va jazoga sazovorligi faqat Jinoyat kodeksi bilan belgilanadi",
            "Chunki analogiya faqat ma’muriy huquqda qo‘llanadi",
            "Chunki Fuqarolik kodeksi buni taqiqlaydi",
        ],
        "togri": 1,
        "izoh": (
            "JK 4-moddasi (qonuniylik prinsipi): qilmishning jinoiyligi, jazoga sazovorligi va boshqa huquqiy "
            "oqibatlari faqat Jinoyat kodeksi bilan belgilanadi (*nullum crimen, nulla poena sine lege*). Bu huquqiy "
            "aniqlik, hokimiyatlar bo‘linishi va shaxs erkinligining kafolatidir. Fuqarolik huquqida esa qonun va huquq "
            "analogiyasi FK 5-moddasi bilan ruxsat etilgan."
        ),
    },
    {
        "savol": "«Qora quti» (Black Box) muammosi nimani anglatadi?",
        "variantlar": [
            "Sun’iy intellekt tizimlarining juda qimmatligi",
            "Algoritm qarorining ichki mantig‘ini tushuntirib bo‘lmasligi, natijada qarorni tekshirish va unga e’tiroz bildirish qiyinlashishi",
            "Elektron dalillarning yo‘qolib qolishi",
            "Dasturiy ta’minotning mualliflik huquqi bilan himoyalanmasligi",
        ],
        "togri": 1,
        "izoh": (
            "«Qora quti» — murakkab algoritm kirish ma’lumotidan natijaga qanday kelganini inson tushuna olmasligi. "
            "Huquqda bu qarorning asoslantirilganligi, himoyalanish va shikoyat qilish huquqi hamda kamsitmaslik "
            "kafolatlariga tahdid soladi; aybsizlik prezumpsiyasi (Konstitutsiyaning 28-moddasi) nuqtayi nazaridan "
            "statistik ehtimollik aybning isboti bo‘la olmaydi."
        ),
    },
    {
        "savol": "«Human-in-the-loop» qoidasining mazmunini eng to‘g‘ri ifodalovchi javobni tanlang.",
        "variantlar": [
            "Barcha huquqiy qarorlar to‘liq avtomatlashtirilishi kerak, inson faqat natijani imzolaydi",
            "Sun’iy intellektdan huquqni qo‘llashda foydalanish butunlay taqiqlanadi",
            "Inson huquq va erkinliklariga daxldor yuridik ahamiyatli qarorni faqat SI xulosasiga tayanib qabul qilish mumkin emas; yakuniy qarorni mas’ul inson qabul qiladi",
            "Algoritm xulosasi sud hukmi bilan teng yuridik kuchga ega",
        ],
        "togri": 2,
        "izoh": (
            "Human-in-the-loop — «inson qaror zanjirida»: algoritm yordamchi, qaror qiluvchi va javobgar esa inson. "
            "2026-yil 21-yanvardagi O‘RQ-1115-son Qonun bilan «Axborotlashtirish to‘g‘risida»gi Qonunga kiritilgan "
            "qoidaga ko‘ra, inson huquq va erkinliklariga daxldor yuridik ahamiyatli qarorlarda faqat sun’iy intellekt "
            "asosidagi tizimlar xulosalariga tayanish mumkin emas. Bu Konstitutsiyaning 20-, 21- va 28-moddalaridagi "
            "kafolatlar bilan uyg‘un."
        ),
    },
]
