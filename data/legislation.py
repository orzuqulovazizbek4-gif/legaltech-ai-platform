"""Qonunchilik xaritasi — normativ-huquqiy asos (lex.uz havolalari bilan)."""

LEGISLATION = [
    {
        "id": "konstitutsiya",
        "turi": "Konstitutsiya",
        "nomi": "O‘zbekiston Respublikasining Konstitutsiyasi (yangi tahrir)",
        "raqami": "Umumxalq referendumida qabul qilingan",
        "sana": "2023-yil 30-aprel",
        "moddalar": [
            {
                "modda": "20-modda",
                "mazmun": (
                    "Davlat organlari tomonidan insonga nisbatan qo‘llaniladigan huquqiy ta’sir choralari "
                    "mutanosiblik prinsipiga asoslanishi va qonunlarda nazarda tutilgan maqsadlarga erishish uchun "
                    "yetarli bo‘lishi kerak; qonunchilikdagi barcha ziddiyat va noaniqliklar inson foydasiga talqin etiladi."
                ),
            },
            {
                "modda": "21-modda",
                "mazmun": (
                    "Inson huquq va erkinliklari faqat qonunga muvofiq va faqat konstitutsiyaviy tuzumni, aholi "
                    "sog‘lig‘ini, ijtimoiy axloqni, boshqa shaxslarning huquq va erkinliklarini himoya qilish, jamoat "
                    "xavfsizligi va tartibini ta’minlash maqsadida zarur bo‘lgan doirada cheklanishi mumkin."
                ),
            },
            {
                "modda": "28-modda",
                "mazmun": (
                    "Aybsizlik prezumpsiyasi: shaxs aybi oshkora sud muhokamasi yo‘li bilan isbotlanmaguncha va sudning "
                    "qonuniy kuchga kirgan hukmi bilan aniqlanmaguncha aybsiz hisoblanadi; barcha shubhalar ayblanuvchi "
                    "foydasiga hal qilinadi; hech kim o‘z aybsizligini isbotlashga, o‘ziga va yaqin qarindoshlariga qarshi "
                    "guvohlik berishga majbur emas."
                ),
            },
        ],
        "ahamiyati": (
            "Oliy yuridik kuchga ega hujjat. Algoritmik qarorlar va avtomatlashtirilgan huquqni qo‘llash uchun "
            "konstitutsiyaviy chegaralarni belgilaydi: har qanday raqamli ta’sir chorasi mutanosib, qonuniy maqsadga "
            "xizmat qiluvchi va zarur doirada bo‘lishi, aybdorlik esa algoritm bilan emas, sud hukmi bilan aniqlanishi shart."
        ),
        "havola": "https://lex.uz/docs/-6445145",
        "teglar": ["mutanosiblik", "aybsizlik prezumpsiyasi", "inson huquqlari"],
    },
    {
        "id": "jinoyat-kodeksi",
        "turi": "Kodeks",
        "nomi": "O‘zbekiston Respublikasining Jinoyat kodeksi",
        "raqami": "2012-XII-son",
        "sana": "1994-yil 22-sentabr (1995-yil 1-apreldan amalda)",
        "moddalar": [
            {
                "modda": "4-modda. Qonuniylik prinsipi",
                "mazmun": (
                    "Sodir etilgan qilmishning jinoiyligi, jazoga sazovorligi va boshqa huquqiy oqibatlari faqat Jinoyat "
                    "kodeksi bilan belgilanadi. Bu qoidadan jinoyat qonunini o‘xshashlik (analogiya) bo‘yicha qo‘llashning "
                    "taqiqlanishi kelib chiqadi."
                ),
            },
        ],
        "ahamiyati": (
            "«Nullum crimen, nulla poena sine lege» tamoyilining milliy ifodasi. Deepfake kabi yangi turdagi qilmishlarni "
            "Kodeksda nazarda tutilmagan holda «o‘xshash» moddaga tortib kvalifikatsiya qilishga yo‘l qo‘yilmaydi; "
            "probelni faqat qonun chiqaruvchi to‘ldiradi."
        ),
        "havola": "https://lex.uz/docs/-111453",
        "teglar": ["analogiya taqiqi", "qonuniylik", "kvalifikatsiya"],
    },
    {
        "id": "fuqarolik-kodeksi",
        "turi": "Kodeks",
        "nomi": "O‘zbekiston Respublikasining Fuqarolik kodeksi (ikkinchi qism)",
        "raqami": "256-I-son",
        "sana": "1996-yil 29-avgust (1997-yil 1-martdan amalda)",
        "moddalar": [
            {
                "modda": "999-modda. Oshiqcha xavf manbai yetkazgan zarar uchun javobgarlik",
                "mazmun": (
                    "Faoliyati atrofdagilar uchun oshiqcha xavf bilan bog‘liq shaxslar oshiqcha xavf manbai yetkazgan "
                    "zararni, agar u yengib bo‘lmas kuch yoki jabrlanuvchining qasdi oqibatida kelib chiqqanini isbotlay "
                    "olmasalar, aybidan qat’i nazar qoplashlari shart."
                ),
            },
        ],
        "ahamiyati": (
            "Avtonom transport, dron va robotlar yetkazgan zarar uchun javobgarlikni asoslashda eng ko‘p qo‘llaniladigan "
            "analogiya: SI tizimiga egalik qiluvchi shaxs aybsiz (qat’iy) javobgarlik asosida javob beradi, so‘ng ishlab "
            "chiquvchiga regress talabi qo‘yishi mumkin. Kodeksning birinchi qismidagi 5-modda esa qonun va huquq "
            "analogiyasini mustahkamlaydi."
        ),
        "havola": "https://lex.uz/docs/-180552",
        "teglar": ["oshiqcha xavf manbai", "aybsiz javobgarlik", "delikt"],
    },
    {
        "id": "orq-682",
        "turi": "Qonun",
        "nomi": "«Normativ-huquqiy hujjatlar to‘g‘risida»gi O‘zbekiston Respublikasi Qonuni",
        "raqami": "O‘RQ-682-son",
        "sana": "2021-yil 20-aprel",
        "moddalar": [
            {
                "modda": "Asosiy institutlar",
                "mazmun": (
                    "Normativ-huquqiy hujjatlarning turlari va yuridik kuchi; loyihalarni ishlab chiqish, huquqiy va "
                    "korrupsiyaga qarshi ekspertizadan o‘tkazish; tartibga solish ta’sirini baholash; loyihalarni "
                    "jamoatchilik muhokamasiga qo‘yish; hujjatlarni rasmiy e’lon qilish va kolliziyalarni hal etish qoidalari."
                ),
            },
        ],
        "ahamiyati": (
            "Huquq ijodkorligi jarayonining «konstitutsiyasi». Loyihalarning regulation.gov.uz portalida jamoatchilik "
            "muhokamasidan o‘tkazilishi va lex.uz bazasida rasmiy e’lon qilinishining huquqiy asosi; raqamli huquq "
            "ijodkorligi va e-demokratiyaning normativ poydevori."
        ),
        "havola": "https://lex.uz/docs/-5378966",
        "teglar": ["huquq ijodkorligi", "jamoatchilik muhokamasi", "kolliziya"],
    },
    {
        "id": "orq-547",
        "turi": "Qonun",
        "nomi": "«Shaxsga doir ma’lumotlar to‘g‘risida»gi O‘zbekiston Respublikasi Qonuni",
        "raqami": "O‘RQ-547-son",
        "sana": "2019-yil 2-iyul",
        "moddalar": [
            {
                "modda": "Asosiy institutlar",
                "mazmun": (
                    "Shaxsga doir ma’lumotlar, ularning subyekti, mulkdori va operatori tushunchalari; ishlov berishning "
                    "prinsiplari va shartlari (subyektning roziligi, maqsadga muvofiqlik); biometrik va maxsus "
                    "ma’lumotlar; ma’lumotlar bazalarini davlat reyestrida ro‘yxatdan o‘tkazish; subyektning huquqlari."
                ),
            },
        ],
        "ahamiyati": (
            "Sun’iy intellekt tizimlarini o‘rgatish va qo‘llashda foydalaniladigan ma’lumotlarning qonuniyligini "
            "belgilaydi. Yuzni tanish, profillashtirish va deepfake holatlarida shaxsning ma’lumotlariga uning "
            "roziligisiz ishlov berish ushbu Qonunni buzish hisoblanadi; ma’lumotlar bazasi egasining javobgarligi shu "
            "Qonunga tayanadi."
        ),
        "havola": "https://lex.uz/docs/-4396419",
        "teglar": ["shaxsga doir ma’lumotlar", "biometriya", "rozilik"],
    },
    {
        "id": "axborotlashtirish",
        "turi": "Qonun",
        "nomi": "«Axborotlashtirish to‘g‘risida»gi O‘zbekiston Respublikasi Qonuni",
        "raqami": "560-II-son",
        "sana": "2003-yil 11-dekabr",
        "moddalar": [
            {
                "modda": "Asosiy institutlar",
                "mazmun": (
                    "Axborotlashtirish, axborot resurslari va axborot tizimlari sohasidagi munosabatlar; davlat "
                    "siyosati; axborot resurslari va tizimlarining huquqiy rejimi; axborotni muhofaza qilish."
                ),
            },
            {
                "modda": "2026-yilgi qo‘shimchalar (O‘RQ-1115-son, 21.01.2026)",
                "mazmun": (
                    "Sun’iy intellekt tushunchasi va undan foydalanishning umumiy asoslari kiritildi; inson huquq va "
                    "erkinliklariga daxldor yuridik ahamiyatga ega qarorlarni qabul qilishda faqat sun’iy intellekt "
                    "asosidagi axborot tizimlari xulosalariga tayanish mumkin emasligi belgilandi."
                ),
            },
        ],
        "ahamiyati": (
            "Raqamli davlat va elektron huquqiy axborot tizimlarining bazaviy qonuni. 2026-yilgi qo‘shimchalardan so‘ng "
            "u «Human-in-the-loop» qoidasining pozitiv-huquqiy manbaiga aylandi: algoritm xulosasi inson qarorining "
            "o‘rnini bosa olmaydi."
        ),
        "havola": "https://lex.uz/docs/-83472",
        "teglar": ["axborot tizimlari", "sun’iy intellekt", "Human-in-the-loop"],
    },
    {
        "id": "pf-6079",
        "turi": "Prezident farmoni",
        "nomi": (
            "«Raqamli O‘zbekiston — 2030» strategiyasini tasdiqlash va uni samarali amalga oshirish "
            "chora-tadbirlari to‘g‘risida»gi Farmon"
        ),
        "raqami": "PF-6079-son",
        "sana": "2020-yil 5-oktabr",
        "moddalar": [
            {
                "modda": "Asosiy yo‘nalishlar",
                "mazmun": (
                    "Raqamli infratuzilma, elektron hukumat, raqamli iqtisodiyot va raqamli ko‘nikmalarni "
                    "rivojlantirish; davlat xizmatlari va davlat boshqaruvini raqamlashtirish; hududlar va tarmoqlarni "
                    "raqamli transformatsiya qilish dasturlari."
                ),
            },
        ],
        "ahamiyati": (
            "Raqamli transformatsiyaning strategik-siyosiy asosi. Huquq ijodkorligi va huquqni qo‘llashni "
            "raqamlashtirish (elektron hujjat aylanishi, ochiq ma’lumotlar, elektron davlat xizmatlari) aynan shu "
            "strategiya doirasida amalga oshiriladi."
        ),
        "havola": "https://lex.uz/docs/-5030957",
        "teglar": ["raqamli transformatsiya", "elektron hukumat", "strategiya"],
    },
    {
        "id": "pq-4996",
        "turi": "Prezident qarori",
        "nomi": (
            "«Sun’iy intellekt texnologiyalarini jadal joriy etish uchun shart-sharoitlar yaratish "
            "chora-tadbirlari to‘g‘risida»gi Qaror"
        ),
        "raqami": "PQ-4996-son",
        "sana": "2021-yil 17-fevral",
        "moddalar": [
            {
                "modda": "Asosiy yo‘nalishlar",
                "mazmun": (
                    "Sun’iy intellektni ustuvor tarmoqlarda joriy etish bo‘yicha tajriba-sinov loyihalari; ilmiy-tadqiqot "
                    "instituti va kadrlar tayyorlash; sun’iy intellekt texnologiyalarini qo‘llash bo‘yicha maxsus "
                    "(eksperimental) huquqiy rejimni joriy etish."
                ),
            },
        ],
        "ahamiyati": (
            "O‘zbekistonda «tartibga solish qumdoni» (Regulatory Sandbox) modelining sun’iy intellekt sohasidagi "
            "huquqiy asosi: yangi texnologiya avval nazorat ostidagi maxsus rejimda sinovdan o‘tkaziladi, so‘ngra umumiy "
            "qonunchilik takomillashtiriladi."
        ),
        "havola": "https://lex.uz/docs/-5297046",
        "teglar": ["maxsus rejim", "Regulatory Sandbox", "sun’iy intellekt"],
    },
    {
        "id": "pq-358",
        "turi": "Prezident qarori",
        "nomi": (
            "«Sun’iy intellekt texnologiyalarini 2030-yilga qadar rivojlantirish strategiyasini "
            "tasdiqlash to‘g‘risida»gi Qaror"
        ),
        "raqami": "PQ-358-son",
        "sana": "2024-yil 14-oktabr",
        "moddalar": [
            {
                "modda": "Maqsadli ko‘rsatkichlar",
                "mazmun": (
                    "Sun’iy intellekt asosidagi dasturiy mahsulot va xizmatlar hajmini 1,5 milliard AQSH dollariga "
                    "yetkazish; Yagona interaktiv davlat xizmatlari portalida SI asosidagi xizmatlar ulushini 10 foizga "
                    "yetkazish; ilmiy laboratoriyalar sonini 10 taga yetkazish; Hukumatning sun’iy intellektga tayyorlik "
                    "indeksida dastlabki 50 talikka kirish."
                ),
            },
        ],
        "ahamiyati": (
            "Sun’iy intellekt sohasidagi davlat siyosatining 2030-yilgacha bo‘lgan strategik hujjati. Normativ-huquqiy "
            "bazani takomillashtirish, ma’lumotlar infratuzilmasi va kadrlar salohiyatini rivojlantirishni nazarda "
            "tutadi; SIni huquqiy tartibga solishga oid keyingi qonunlar uchun dasturiy asos."
        ),
        "havola": "https://lex.uz/docs/-7158604",
        "teglar": ["strategiya", "sun’iy intellekt", "2030"],
    },
]

LEGISLATION_TYPES = ["Konstitutsiya", "Kodeks", "Qonun", "Prezident farmoni", "Prezident qarori"]


def legislation_summary_text() -> str:
    """Qonunchilik xaritasining qisqa matni (AI konteksti uchun)."""
    lines = []
    for act in LEGISLATION:
        lines.append(f"{act['nomi']} ({act['raqami']}, {act['sana']}).")
        for item in act["moddalar"]:
            lines.append(f"  {item['modda']}: {item['mazmun']}")
        lines.append(f"  Ahamiyati: {act['ahamiyati']}")
        lines.append("")
    return "\n".join(lines)
