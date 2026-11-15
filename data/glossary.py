"""Interaktiv glossariy — 16 ta huquqiy va LegalTech atamasi."""

GLOSSARY = [
    {
        "id": "legaltech",
        "atama": "LegalTech",
        "toifa": "Texnologiya",
        "tarif": (
            "Yuridik faoliyatni (huquqiy xizmat ko‘rsatish, hujjat tayyorlash, huquqiy tahlil, sud ishlarini "
            "yuritish, huquq ijodkorligi) avtomatlashtirish va takomillashtirishga qaratilgan axborot texnologiyalari "
            "hamda dasturiy yechimlar majmui. U huquqshunosning o‘rnini bosmaydi, balki uni takroriy, texnik ishlardan "
            "ozod qilib, intellektual tahlilga vaqt ajratadi."
        ),
        "misol": (
            "Lex.uz bazasidan kerakli normani soniyalarda topish, shartnoma loyihasini shablon asosida avtomatik "
            "tuzish yoki yangi qonun loyihasini amaldagi hujjatlar bilan solishtirib, ziddiyatlarni belgilab beruvchi "
            "dastur — bularning barchasi LegalTech."
        ),
        "manba": "Doktrinal atama; «Raqamli O‘zbekiston — 2030» strategiyasi (PF-6079) bilan bog‘liq.",
    },
    {
        "id": "regtech",
        "atama": "RegTech",
        "toifa": "Texnologiya",
        "tarif": (
            "«Regulatory Technology» — tartibga soluvchi talablarga rioya etilishini (komplayens) ta’minlash, nazorat "
            "va hisobot jarayonlarini avtomatlashtirishga xizmat qiluvchi texnologiyalar. LegalTechdan farqi shundaki, "
            "u huquqiy xizmatga emas, balki regulyator talablarining bajarilishini monitoring qilishga yo‘naltirilgan."
        ),
        "misol": (
            "Bank tizimi har bir tranzaksiyani avtomatik tekshirib, jinoiy daromadlarni legallashtirishga qarshi "
            "kurashish qoidalari bo‘yicha shubhali operatsiyani o‘zi aniqlaydi va vakolatli organga xabar tayyorlaydi."
        ),
        "manba": "Doktrinal atama; moliyaviy nazorat va komplayens amaliyoti.",
    },
    {
        "id": "smart-kontrakt",
        "atama": "Smart-kontrakt",
        "toifa": "Texnologiya",
        "tarif": (
            "Taraflar kelishuvining shartlari dastur kodi shaklida ifodalangan va oldindan belgilangan holat yuz "
            "berganda taqsimlangan reyestr (blokcheyn) muhitida inson aralashuvisiz avtomatik ijro etiladigan "
            "algoritm. Huquqiy tabiatiga ko‘ra ko‘proq majburiyatni ijro etish usuli sifatida baholanadi; uning "
            "mantiqi huquq normasining gipoteza — dispozitsiya — sanksiya tuzilishiga mos keladi."
        ),
        "misol": (
            "Savdo avtomati eng sodda namuna: pul tashlandi (shart) — ichimlik chiqdi (ijro). Blokcheynda esa: yuk "
            "yetkazilgani tasdiqlansa, to‘lov sotuvchiga avtomatik o‘tadi; kechiksa — penya avtomatik ushlanadi."
        ),
        "manba": "Fuqarolik kodeksining shartnomalarga oid umumiy qoidalari; doktrina (N. Sabo, L. Lessig).",
    },
    {
        "id": "huquq-ijodkorligi",
        "atama": "Huquq ijodkorligi",
        "toifa": "Huquq nazariyasi",
        "tarif": (
            "Vakolatli davlat organlarining, qonunda nazarda tutilgan hollarda esa bevosita xalqning huquq normalarini "
            "yaratish, o‘zgartirish yoki bekor qilishga qaratilgan, qat’iy tartib-taomil asosida amalga oshiriladigan "
            "faoliyati. Prinsiplari: qonuniylik, demokratizm, ilmiylik, oshkoralik, tizimlilik."
        ),
        "misol": (
            "Vazirlik qonun loyihasini ishlab chiqadi, uni regulation.gov.uz portalida jamoatchilik muhokamasiga "
            "qo‘yadi, ekspertizalardan o‘tkazadi; Qonunchilik palatasi qabul qiladi, Senat ma’qullaydi, Prezident "
            "imzolaydi va qonun rasmiy e’lon qilinadi."
        ),
        "manba": "«Normativ-huquqiy hujjatlar to‘g‘risida»gi Qonun (O‘RQ-682, 20.04.2021).",
    },
    {
        "id": "kolliziya",
        "atama": "Kolliziya",
        "toifa": "Huquq nazariyasi",
        "tarif": (
            "Bir xil ijtimoiy munosabatni tartibga soluvchi ikki yoki undan ortiq huquq normasi o‘rtasidagi ziddiyat. "
            "Hal etish qoidalari: yuqori yuridik kuchga ega hujjat ustun (ierarxik); bir xil kuchdagi hujjatlardan "
            "keyinroq qabul qilingani ustun (xronologik); maxsus norma umumiy normadan ustun (mazmuniy)."
        ),
        "misol": (
            "Vazirlik buyrug‘ida ariza ko‘rib chiqish muddati 30 kun, qonunda esa 15 kun deb belgilangan bo‘lsa, bu "
            "kolliziya; qonun yuqori yuridik kuchga ega bo‘lgani uchun 15 kunlik muddat qo‘llanadi."
        ),
        "manba": "«Normativ-huquqiy hujjatlar to‘g‘risida»gi Qonun (O‘RQ-682); Konstitutsiyaning 15–16-moddalari.",
    },
    {
        "id": "probel",
        "atama": "Huquqiy bo‘shliq (Probel)",
        "toifa": "Huquq nazariyasi",
        "tarif": (
            "Huquqiy tartibga solish doirasiga kiruvchi va yuridik hal etilishi lozim bo‘lgan munosabatni tartibga "
            "soluvchi normaning to‘liq yoki qisman mavjud emasligi. Huquq ijodkorligi orqali bartaraf etiladi, "
            "huquqni qo‘llashda esa analogiya yordamida yengib o‘tiladi (jinoyat huquqi bundan mustasno)."
        ),
        "misol": (
            "Sun’iy intellekt yaratgan rasmning muallifi kim ekani qonunda aniq yozilmagan: muallif deb ijodiy mehnat "
            "qilgan jismoniy shaxs tan olinadi, mashina esa shaxs emas — bu tipik «keyingi» probel."
        ),
        "manba": "Fuqarolik kodeksining 5-moddasi; huquq nazariyasi doktrinasi.",
    },
    {
        "id": "qonun-analogiyasi",
        "atama": "Qonun analogiyasi",
        "toifa": "Huquq nazariyasi",
        "tarif": (
            "Huquqiy bo‘shliq mavjud bo‘lganda nizoli munosabatga unga muhim belgilari bilan o‘xshash munosabatni "
            "tartibga soluvchi aniq huquq normasini qo‘llash. Fuqarolik huquqida ruxsat etiladi; jinoyat huquqida "
            "qat’iyan taqiqlanadi."
        ),
        "misol": (
            "Qonunda nomi tilga olinmagan yangi turdagi shartnoma bo‘yicha nizoda sud unga eng yaqin bo‘lgan shartnoma "
            "turi (masalan, pullik xizmat ko‘rsatish) haqidagi qoidalarni qo‘llaydi."
        ),
        "manba": "Fuqarolik kodeksining 5-moddasi; Jinoyat kodeksining 4-moddasi (taqiq).",
    },
    {
        "id": "huquq-analogiyasi",
        "atama": "Huquq analogiyasi",
        "toifa": "Huquq nazariyasi",
        "tarif": (
            "O‘xshash munosabatni tartibga soluvchi aniq norma ham mavjud bo‘lmaganda, ishni qonunchilikning umumiy "
            "asoslari va mazmuni, huquq prinsiplari — vijdonlilik, oqilonalik va adolat talablaridan kelib chiqib hal "
            "etish. Qonun analogiyasidan keyingi, so‘nggi chora sifatida qo‘llanadi."
        ),
        "misol": (
            "Mutlaqo yangi raqamli aktiv bo‘yicha nizoda birorta o‘xshash norma topilmasa, sud taraflarning tengligi, "
            "shartnoma erkinligi va vijdonlilik prinsiplariga tayanib qaror chiqaradi."
        ),
        "manba": "Fuqarolik kodeksining 5-moddasi.",
    },
    {
        "id": "kvazi-subyekt",
        "atama": "Kvazi-subyekt («Elektron shaxs»)",
        "toifa": "Sun’iy intellekt huquqi",
        "tarif": (
            "Avtonom sun’iy intellekt tizimlariga yuridik shaxsga o‘xshatma asosida cheklangan, maqsadli huquq layoqati "
            "berishni nazarda tutuvchi nazariy konsepsiya. «Kvazi» — «go‘yo», ya’ni to‘laqonli emas, shartli subyekt. "
            "Yevropa Parlamentining 2017-yilgi rezolyutsiyasida muhokamaga qo‘yilgan, biroq amaldagi qonunchilikda "
            "(shu jumladan O‘zbekistonda) qabul qilinmagan."
        ),
        "misol": (
            "Go‘yo o‘zi boshqariladigan taksi «elektron shaxs» sifatida ro‘yxatdan o‘tgan va o‘z sug‘urta fondiga ega: "
            "u yetkazgan zarar shu fonddan to‘lanadi. Tanqidchilar fikricha, bu ishlab chiqaruvchiga javobgarlikdan "
            "qochish imkonini beradi."
        ),
        "manba": "Yevropa Parlamentining 16.02.2017-yildagi rezolyutsiyasi; doktrina.",
    },
    {
        "id": "deepfake",
        "atama": "Deepfake",
        "toifa": "Sun’iy intellekt huquqi",
        "tarif": (
            "«Deep learning» (chuqur o‘rganish) va «fake» (soxta) so‘zlaridan: sun’iy intellekt yordamida real "
            "shaxsning tashqi qiyofasi, ovozi yoki harakatlari ishonarli tarzda soxtalashtirilgan video, audio yoki "
            "tasvir. Sha’n va qadr-qimmat, shaxsiy hayot daxlsizligi, shaxsga doir ma’lumotlar va mulkka tajovuz "
            "vositasi bo‘lishi mumkin; dalillarning ishonchliligi muammosini keskinlashtiradi."
        ),
        "misol": (
            "Buxgalterga «direktor»dan video-qo‘ng‘iroq keladi va u zudlik bilan pul o‘tkazishni buyuradi. Aslida "
            "ekrandagi yuz va ovoz — firibgarlar sun’iy intellekt bilan yasagan soxta nusxa."
        ),
        "manba": (
            "«Shaxsga doir ma’lumotlar to‘g‘risida»gi Qonun (O‘RQ-547); 21.01.2026-yildagi O‘RQ-1115-son Qonun; "
            "Jinoyat kodeksining tegishli tarkiblari (masalan, firibgarlik)."
        ),
    },
    {
        "id": "black-box",
        "atama": "Black Box («Qora quti»)",
        "toifa": "Sun’iy intellekt huquqi",
        "tarif": (
            "Murakkab sun’iy intellekt tizimining (ayniqsa, neyron tarmoqlarning) kirish ma’lumotidan chiqish "
            "natijasiga qanday mantiq asosida kelgani inson uchun, ba’zan yaratuvchisi uchun ham tushunarsiz bo‘lishi "
            "muammosi. Huquqda u qarorning asoslantirilganligi, shikoyat qilish huquqi va kamsitmaslik "
            "kafolatlariga tahdid soladi."
        ),
        "misol": (
            "Dastur fuqaroga kredit bermaslikni «tavsiya qildi», lekin nega ekanini hech kim tushuntira olmaydi. "
            "Tushuntirib bo‘lmaydigan qarorga asosli e’tiroz bildirish ham mumkin emas."
        ),
        "manba": "Doktrina; Konstitutsiyaning 20-, 21- va 28-moddalari bilan bog‘liq kafolatlar.",
    },
    {
        "id": "human-in-the-loop",
        "atama": "Human-in-the-loop",
        "toifa": "Sun’iy intellekt huquqi",
        "tarif": (
            "«Inson — qaror zanjirida» prinsipi: inson huquq va erkinliklariga daxldor yuridik ahamiyatli qaror "
            "algoritm tomonidan emas, balki algoritm xulosasini tushunib, tekshirib va unga qo‘shilmaslik vakolatiga "
            "ega bo‘lgan mas’ul inson tomonidan qabul qilinadi. Algoritm — yordamchi, inson — qaror qiluvchi va "
            "javobgar."
        ),
        "misol": (
            "Dastur tergovchiga «shu shaxs shubhali» degan signal beradi. Tergovchi buni tayyor xulosa sifatida emas, "
            "tekshirilishi lozim bo‘lgan versiya sifatida qabul qiladi va qarorni faqat tekshirilgan dalillar asosida "
            "o‘zi chiqaradi."
        ),
        "manba": (
            "«Axborotlashtirish to‘g‘risida»gi Qonun (O‘RQ-1115-son Qonun bilan kiritilgan qo‘shimchalar, 21.01.2026)."
        ),
    },
    {
        "id": "regulatory-sandbox",
        "atama": "Regulatory Sandbox («Tartibga solish qumdoni»)",
        "toifa": "Huquqiy tartibga solish",
        "tarif": (
            "Eksperimental (maxsus) huquqiy rejim: cheklangan ishtirokchilar doirasi uchun, belgilangan muddatga va "
            "vakolatli organ nazorati ostida amaldagi ayrim talablar yengillashtiriladi yoki maxsus qoidalar "
            "o‘rnatiladi, toki yangi texnologiya real sharoitda sinab ko‘rilsin. Yakunida tajriba baholanib, umumiy "
            "norma qabul qilinadi yoki rad etiladi."
        ),
        "misol": (
            "Bolalar qumdonda xavfsiz o‘ynab tajriba orttirgani kabi, kompaniya o‘zi boshqariladigan avtomobilni "
            "shaharning ajratilgan hududida, maxsus ruxsat va nazorat ostida sinovdan o‘tkazadi."
        ),
        "manba": "Prezidentning 17.02.2021-yildagi PQ-4996-son qarori (sun’iy intellekt uchun maxsus rejim).",
    },
    {
        "id": "predictive-lawmaking",
        "atama": "Predictive Lawmaking",
        "toifa": "Huquqiy tartibga solish",
        "tarif": (
            "Bashoratli qonun ijodkorligi: katta ma’lumotlar, statistik modellar va simulyatsiya yordamida "
            "loyihalanayotgan normaning ijtimoiy, iqtisodiy va huquqiy oqibatlarini u qabul qilinishidan oldin "
            "baholashga asoslangan yondashuv. Tartibga solish ta’sirini baholash institutining raqamli davomi."
        ),
        "misol": (
            "Jarima miqdorini oshirishdan oldin o‘tgan besh yillik qoidabuzarliklar statistikasi asosida model "
            "tuziladi va «jarima ikki barobar oshsa, huquqbuzarliklar qanchaga kamayadi?» degan savolga taxminiy "
            "javob olinadi."
        ),
        "manba": "Doktrinal atama; O‘RQ-682-son Qonundagi tartibga solish ta’sirini baholash instituti.",
    },
    {
        "id": "aybsizlik-prezumpsiyasi",
        "atama": "Aybsizlik prezumpsiyasi",
        "toifa": "Konstitutsiyaviy prinsip",
        "tarif": (
            "Jinoyat sodir etganlikda ayblanayotgan shaxs uning aybi qonunda nazarda tutilgan tartibda oshkora sud "
            "muhokamasi yo‘li bilan isbotlanmaguncha va sudning qonuniy kuchga kirgan hukmi bilan aniqlanmaguncha "
            "aybsiz hisoblanadi. Isbotlash yuki ayblovchida; bartaraf etib bo‘lmaydigan barcha shubhalar ayblanuvchi "
            "foydasiga hal qilinadi."
        ),
        "misol": (
            "Algoritm «bu shaxs 90 foiz ehtimol bilan aybdor» desa ham, u aybsiz hisoblanaveradi: ehtimollik — dalil "
            "emas, aybni esa faqat sud qonuniy dalillar asosida aniqlaydi."
        ),
        "manba": "Konstitutsiyaning 28-moddasi; Jinoyat-protsessual kodeksining 23-moddasi.",
    },
    {
        "id": "mutanosiblik",
        "atama": "Mutanosiblik (Proportsionallik) prinsipi",
        "toifa": "Konstitutsiyaviy prinsip",
        "tarif": (
            "Davlat organlari insonga nisbatan qo‘llaydigan huquqiy ta’sir choralari ko‘zlangan qonuniy maqsadga "
            "mutanosib bo‘lishi va shu maqsadga erishish uchun yetarli doiradan chiqmasligi talabi. Uch bosqichli test: "
            "chora maqsadga yaroqlimi; zarurmi (yengilroq muqobili yo‘qmi); shaxsga yuklanadigan cheklov erishiladigan "
            "foydaga mutanosibmi."
        ),
        "misol": (
            "Bitta gumonlanuvchini topish uchun butun shahar aholisining yuzini uzluksiz skanerlash — «chumchuqqa "
            "to‘pdan o‘q uzish»: maqsad qonuniy bo‘lsa-da, vosita haddan tashqari keng."
        ),
        "manba": "Konstitutsiyaning 20-moddasi (mutanosiblik) va 21-moddasi (cheklashning zarur doirasi).",
    },
]

GLOSSARY_CATEGORIES = [
    "Texnologiya",
    "Huquq nazariyasi",
    "Sun’iy intellekt huquqi",
    "Huquqiy tartibga solish",
    "Konstitutsiyaviy prinsip",
]


def glossary_summary_text() -> str:
    """Glossariyning to‘liq matni (AI konteksti uchun)."""
    return "\n\n".join(
        f"{item['atama']}: {item['tarif']} Misol: {item['misol']} Manba: {item['manba']}"
        for item in GLOSSARY
    )


def term_text(item: dict) -> str:
    """Bitta atamaning to‘liq matni."""
    return (
        f"Atama: {item['atama']}\nTa’rif: {item['tarif']}\n"
        f"Misol: {item['misol']}\nNormativ manba: {item['manba']}"
    )
