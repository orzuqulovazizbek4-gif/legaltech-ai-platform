"""Tahliliy maqolalar — to‘liq akademik matnlar (o‘zbek tilida, lotin yozuvida)."""

ARTICLES = [
    # ------------------------------------------------------------------ 1
    {
        "id": "huquq-ijodkorligi",
        "raqam": 1,
        "sarlavha": "Raqamli transformatsiya sharoitida huquq ijodkorligi evolyutsiyasi",
        "qisqa": "Huquq ijodkorligi evolyutsiyasi",
        "annotatsiya": (
            "Maqolada huquq ijodkorligining nazariy tushunchasi, uning raqamli muhitdagi "
            "o‘zgarishi, elektron demokratiya vositalari, normativ-huquqiy hujjatlar loyihalarining "
            "jamoatchilik muhokamasi, LegalTech yordamida kolliziyalar va korrupsiyaviy omillarni "
            "aniqlash hamda bashoratli qonun ijodkorligi (Predictive Lawmaking) tahlil qilinadi."
        ),
        "kalit_sozlar": [
            "huquq ijodkorligi", "e-demokratiya", "regulation.gov.uz", "O‘RQ-682",
            "kolliziya", "korrupsiyaga qarshi ekspertiza", "Predictive Lawmaking",
        ],
        "oqish_vaqti": 9,
        "bolimlar": [
            {
                "sarlavha": "1. Huquq ijodkorligi tushunchasi va uning bosqichlari",
                "matn": (
                    "Davlat va huquq nazariyasida **huquq ijodkorligi** deganda vakolatli davlat organlarining, "
                    "qonunda nazarda tutilgan hollarda esa bevosita xalqning (referendum orqali) huquq normalarini "
                    "yaratish, o‘zgartirish yoki bekor qilishga qaratilgan maxsus faoliyati tushuniladi. U huquqning "
                    "shakllanishi (huquq hosil bo‘lishi) jarayonining yakuniy, rasmiy bosqichi hisoblanadi: jamiyatda "
                    "obyektiv ravishda yetilgan ehtiyoj davlat irodasi orqali umummajburiy qoidaga aylanadi.\n\n"
                    "Huquq ijodkorligining turlari subyektiga ko‘ra farqlanadi: xalqning bevosita huquq ijodkorligi, "
                    "parlament qonun ijodkorligi, Prezident va hukumatning qonunosti huquq ijodkorligi, vazirlik va "
                    "idoralarning idoraviy huquq ijodkorligi, mahalliy davlat hokimiyati organlarining huquq ijodkorligi. "
                    "Uning asosiy prinsiplari — qonuniylik, demokratizm, ilmiylik, oshkoralik, tizimlilik, inson huquqlari "
                    "ustuvorligi va professionallikdir.\n\n"
                    "O‘zbekiston Respublikasining 2021-yil 20-apreldagi «Normativ-huquqiy hujjatlar to‘g‘risida»gi "
                    "O‘RQ-682-son Qonuni huquq ijodkorligi jarayonini yaxlit tartibga soladi: normativ-huquqiy hujjatlarning "
                    "turlari va yuridik kuchi, loyihani rejalashtirish, ishlab chiqish, kelishish, ekspertizadan o‘tkazish, "
                    "jamoatchilik muhokamasi, qabul qilish, e’lon qilish va kuchga kirish bosqichlari shu Qonunda belgilangan. "
                    "Klassik sxemada bu jarayon qonunchilik tashabbusi → loyihani muhokama qilish → qabul qilish → "
                    "imzolash va e’lon qilish zanjiridan iborat."
                ),
            },
            {
                "sarlavha": "2. Raqamli transformatsiya: «qog‘oz» qonun ijodkorligidan platformaga",
                "matn": (
                    "Raqamli transformatsiya huquq ijodkorligining mohiyatini emas, balki uning **texnologiyasini** va "
                    "ishtirokchilar doirasini o‘zgartiradi. An’anaviy modelda loyiha idoralar o‘rtasida qog‘oz shaklida "
                    "aylanar, fuqaro esa tayyor qonun bilan faqat u e’lon qilingandan keyin tanishar edi. Raqamli modelda "
                    "loyiha yagona elektron tizimda ishlab chiqiladi va kelishiladi, uning har bir tahriri iz qoldiradi, "
                    "jamiyat esa jarayonga loyiha bosqichidayoq qo‘shiladi.\n\n"
                    "Prezidentning 2020-yil 5-oktabrdagi PF-6079-son Farmoni bilan tasdiqlangan «Raqamli O‘zbekiston — 2030» "
                    "strategiyasi davlat boshqaruvini raqamlashtirishni ustuvor vazifa sifatida belgiladi. Huquq ijodkorligi "
                    "sohasida bu uch yo‘nalishda namoyon bo‘ladi: birinchidan, qonunchilik bazasining ochiq elektron shaklda "
                    "yuritilishi (Qonunchilik ma’lumotlari milliy bazasi — lex.uz); ikkinchidan, loyihalarni elektron "
                    "tarzda ishlab chiqish va kelishish; uchinchidan, loyihalarning jamoatchilik muhokamasi uchun maxsus "
                    "portalning yo‘lga qo‘yilishi.\n\n"
                    "Nazariy jihatdan bu o‘zgarish huquq ijodkorligining oshkoralik va demokratizm prinsiplarini yangi "
                    "bosqichga ko‘taradi: rasmiy e’lon qilish endi nafaqat bosma nashrda, balki rasmiy elektron manbada "
                    "amalga oshiriladi, huquqiy axborotdan foydalanish esa har bir fuqaro uchun real imkoniyatga aylanadi."
                ),
            },
            {
                "sarlavha": "3. E-demokratiya va regulation.gov.uz: jamoatchilik muhokamasi instituti",
                "matn": (
                    "**Elektron demokratiya (E-democracy)** — fuqarolarning davlat qarorlarini qabul qilish jarayonida "
                    "axborot-kommunikatsiya texnologiyalari vositasida ishtirok etishidir. Uning huquq ijodkorligidagi "
                    "asosiy ko‘rinishi — normativ-huquqiy hujjatlar loyihalarining ochiq elektron muhokamasi.\n\n"
                    "O‘RQ-682-son Qonun normativ-huquqiy hujjatlar loyihalarini jamoatchilik muhokamasiga qo‘yishni "
                    "huquq ijodkorligi jarayonining tarkibiy qismi sifatida mustahkamlaydi. Amalda bu vazifani "
                    "**regulation.gov.uz** — Normativ-huquqiy hujjatlar loyihalari muhokamasi portali bajaradi: ishlab "
                    "chiquvchi organ loyihani portalga joylashtiradi, fuqarolar, tadbirkorlar va ekspertlar o‘z taklif va "
                    "e’tirozlarini bildiradi, ishlab chiquvchi esa kelib tushgan takliflarni ko‘rib chiqib, ularning qabul "
                    "qilingani yoki rad etilgani yuzasidan asoslangan munosabat bildirishi lozim.\n\n"
                    "Bu institutning nazariy ahamiyati katta. Birinchidan, u xalq hokimiyatchiligi g‘oyasini kundalik "
                    "huquq ijodkorligi amaliyotiga olib kiradi (Konstitutsiyaga ko‘ra xalq davlat hokimiyatining birdan-bir "
                    "manbaidir). Ikkinchidan, qonunning **legitimligi** ortadi: muhokamada ishtirok etgan jamiyat normani "
                    "«begona» emas, o‘ziniki sifatida qabul qiladi va unga ixtiyoriy rioya etish darajasi oshadi. "
                    "Uchinchidan, tartibga solish ta’sirini baholash sifati yaxshilanadi, chunki norma kimga qanday ta’sir "
                    "qilishini eng yaxshi biladiganlar — uning adresatlaridir.\n\n"
                    "Shu bilan birga, e-demokratiyaning chegaralari ham bor: raqamli tengsizlik (hamma ham internetdan "
                    "birdek foydalana olmaydi), muhokamaning rasmiyatchilikka aylanish xavfi va takliflarni sun’iy "
                    "ravishda ko‘paytirish (botlar) ehtimoli. Shuning uchun elektron muhokama parlament muhokamasi va "
                    "ekspert tahlilining o‘rnini bosmaydi, balki ularni to‘ldiradi."
                ),
            },
            {
                "sarlavha": "4. LegalTech: kolliziyalar va korrupsiyaviy omillarni avtomatik aniqlash",
                "matn": (
                    "**LegalTech** — yuridik faoliyatni avtomatlashtiruvchi va takomillashtiruvchi texnologiyalar majmui. "
                    "Huquq ijodkorligida uning eng istiqbolli qo‘llanilishi — qonunchilik massivini mashina yordamida tahlil "
                    "qilishdir. Lex.uz bazasida o‘n minglab hujjatlar mavjud; ularning barchasini inson ko‘zi bilan "
                    "solishtirib chiqish amalda mumkin emas.\n\n"
                    "**Kolliziyalarni aniqlash.** Yuridik kolliziya — bir xil ijtimoiy munosabatni tartibga soluvchi ikki "
                    "yoki undan ortiq normaning o‘zaro ziddiyati. Tabiiy tilni qayta ishlash (NLP) algoritmlari yangi "
                    "loyiha matnini amaldagi hujjatlar bilan semantik jihatdan solishtirib, bir xil predmetni turlicha "
                    "tartibga solayotgan normalarni, eskirgan havolalarni, takroriy qoidalarni va terminologik "
                    "nomuvofiqlikni belgilab bera oladi. Kolliziyani hal etish qoidalari esa (yuqori yuridik kuchga ega "
                    "hujjat ustunligi; keyinroq qabul qilingan norma ustunligi; maxsus normaning umumiy normadan ustunligi) "
                    "baribir huquqshunos tomonidan qo‘llaniladi.\n\n"
                    "**Korrupsiyaviy omillarni aniqlash.** Normativ-huquqiy hujjatlar va ularning loyihalari korrupsiyaga "
                    "qarshi ekspertizadan o‘tkaziladi. Korrupsiyaviy omil (korrupsiogen omil) — mansabdor shaxsga asossiz keng "
                    "ixtiyoriy vakolat beruvchi, noaniq yoki bajarib bo‘lmaydigan talab qo‘yuvchi, istisnolarni "
                    "asoslanmagan holda belgilovchi qoida. Algoritm «zarur hollarda», «istisno tariqasida», "
                    "«haqli», «mumkin» kabi noaniq yoki diskretsion iboralarni, ma’muriy tartib-taomil muddati "
                    "ko‘rsatilmagan normalarni avtomatik ajratib, ekspert e’tiboriga havola qiladi.\n\n"
                    "Muhimi shundaki, algoritm bu yerda **qaror qabul qiluvchi emas, balki signal beruvchi vosita**: u "
                    "shubhali joyni ko‘rsatadi, yakuniy huquqiy bahoni esa ekspert beradi."
                ),
            },
            {
                "sarlavha": "5. Predictive Lawmaking — bashoratli qonun ijodkorligi",
                "matn": (
                    "**Predictive Lawmaking** — katta ma’lumotlar (Big Data) va modellashtirish yordamida loyihalanayotgan "
                    "normaning kelajakdagi ijtimoiy, iqtisodiy va huquqiy oqibatlarini oldindan baholashga asoslangan "
                    "huquq ijodkorligi yondashuvi. Uning mantig‘i oddiy: qonun qabul qilingach, uning oqibatini kutib "
                    "o‘tirmasdan, statistik ma’lumotlar, sud amaliyoti, murojaatlar tahlili va simulyatsiya modellari "
                    "asosida «agar shu norma kuchga kirsa, nima bo‘ladi?» degan savolga oldindan javob izlanadi.\n\n"
                    "Masalan, yo‘l harakati qoidabuzarligi uchun jarima miqdorini o‘zgartirishdan oldin o‘tgan yillardagi "
                    "huquqbuzarliklar dinamikasi, to‘lov intizomi va baxtsiz hodisalar statistikasi modellashtirilishi "
                    "mumkin. Bu yondashuv tartibga solish ta’sirini baholash institutini sifat jihatidan boyitadi va "
                    "huquq ijodkorligining **ilmiylik** prinsipini amalda ta’minlaydi.\n\n"
                    "Biroq bashoratli modelning xulosasi — ehtimollik, haqiqat emas. Model o‘tmish ma’lumotlariga "
                    "tayanadi, demak, o‘tmishdagi xato va tarafkashlikni ham kelajakka ko‘chirishi mumkin. Qonun esa "
                    "faqat samaradorlikni emas, adolat, insonparvarlik va inson qadr-qimmati kabi qadriyatlarni ham "
                    "ifodalashi shart — bularni raqam bilan to‘liq o‘lchab bo‘lmaydi."
                ),
            },
            {
                "sarlavha": "6. Xulosa: texnologiya — vosita, qonun chiqaruvchi — inson",
                "matn": (
                    "Raqamli transformatsiya huquq ijodkorligini tezroq, ochiqroq va ma’lumotlarga asoslangan qiladi. "
                    "E-demokratiya vositalari qonunning legitimligini, LegalTech uning ichki izchilligini, bashoratli "
                    "tahlil esa samaradorligini oshiradi. Ammo huquq ijodkorligining subyekti o‘zgarmaydi: normani "
                    "vakolatli organ qabul qiladi va uning uchun siyosiy hamda huquqiy mas’uliyatni o‘z zimmasiga oladi.\n\n"
                    "Shu sababli raqamli huquq ijodkorligining asosiy qoidasi quyidagicha ifodalanishi mumkin: "
                    "**algoritm tahlil qiladi va taklif beradi — inson baholaydi va qaror qiladi.** Davlat va huquq "
                    "nazariyasi nuqtayi nazaridan bu xalq suvereniteti, hokimiyatlar bo‘linishi va qonun ustuvorligi "
                    "prinsiplarining raqamli davrdagi tabiiy davomidir."
                ),
            },
        ],
        "xulosalar": [
            "Raqamlashtirish huquq ijodkorligining mohiyatini emas, texnologiyasi va ishtirokchilar doirasini o‘zgartiradi.",
            "regulation.gov.uz orqali jamoatchilik muhokamasi qonunning legitimligini va sifatini oshiradi (O‘RQ-682-son Qonun).",
            "LegalTech kolliziya va korrupsiyaviy omillarni aniqlashda signal beruvchi vosita, yakuniy bahoni esa ekspert beradi.",
            "Predictive Lawmaking ehtimollik beradi; qonun chiqaruvchining mas’uliyati algoritmga o‘tmaydi.",
        ],
    },
    # ------------------------------------------------------------------ 2
    {
        "id": "code-is-law",
        "raqam": 2,
        "sarlavha": "«Code is Law» konsepsiyasi, smart-kontraktlar va eksperimental huquqiy rejimlar",
        "qisqa": "«Code is Law» va smart-kontraktlar",
        "annotatsiya": (
            "Maqolada Lourens Lessigning «Kod — bu qonun» nazariyasi, smart-kontraktlarning huquq normasi "
            "tuzilishi (gipoteza — dispozitsiya — sanksiya) bilan mantiqiy o‘xshashligi, ularning huquqiy tabiati "
            "hamda «tartibga solish qumdonlari» va O‘zbekistonda sun’iy intellekt uchun joriy etilgan maxsus "
            "rejim (PQ-4996-son qaror) yoritiladi."
        ),
        "kalit_sozlar": [
            "Code is Law", "Lessig", "smart-kontrakt", "gipoteza", "dispozitsiya", "sanksiya",
            "Regulatory Sandbox", "PQ-4996", "eksperimental huquqiy rejim",
        ],
        "oqish_vaqti": 9,
        "bolimlar": [
            {
                "sarlavha": "1. Lourens Lessig nazariyasi: xulq-atvorni tartibga soluvchi to‘rt kuch",
                "matn": (
                    "Garvard huquq maktabi professori Lourens Lessig 1999-yilda nashr etilgan «Code and Other Laws of "
                    "Cyberspace» asarida mashhur tezisni ilgari surdi: **«Code is Law» — «Kod — bu qonun»**. Uning "
                    "fikricha, inson xulq-atvori to‘rtta regulyator orqali tartibga solinadi: **huquq** (davlat majburlovi "
                    "bilan ta’minlangan normalar), **ijtimoiy normalar** (axloq, odat, jamoatchilik fikri), **bozor** "
                    "(narx va iqtisodiy rag‘bat) hamda **arxitektura** (muhitning jismoniy yoki texnik tuzilishi).\n\n"
                    "Kibermakonda arxitektura vazifasini dasturiy kod bajaradi. Platforma nimaga ruxsat berishi, nimani "
                    "texnik jihatdan imkonsiz qilishi dasturchi tomonidan belgilanadi. Huquq normasini buzish mumkin "
                    "(keyin javobgarlik keladi), kod o‘rnatgan cheklovni esa oddiy foydalanuvchi buza olmaydi — u "
                    "shunchaki «ishlamaydi». Demak, kod xulq-atvorni huquqdan ham qat’iyroq, **ex ante** (oldindan) "
                    "tartibga soladi.\n\n"
                    "Davlat va huquq nazariyasi uchun bu tezis jiddiy savol tug‘diradi: agar xulq-atvor qoidalarini "
                    "amalda xususiy kompaniya dasturchilari yozayotgan bo‘lsa, bu qoidalarning legitimligi, oshkoraligi "
                    "va ular ustidan demokratik nazorat qanday ta’minlanadi? Lessigning o‘zi «kod qonunning o‘rnini "
                    "bosishi kerak» demagan; aksincha, u jamiyat kodni kim va qanday qadriyatlar asosida yozayotganini "
                    "nazorat qilishi zarurligini ta’kidlagan."
                ),
            },
            {
                "sarlavha": "2. Smart-kontrakt tushunchasi va huquqiy tabiati",
                "matn": (
                    "**Smart-kontrakt** atamasini 1990-yillarda kriptograf Nik Sabo taklif qilgan. Bu — taraflar "
                    "kelishuvining shartlari dastur kodi shaklida ifodalangan va belgilangan holat yuz berganda "
                    "taqsimlangan reyestr (blokcheyn) muhitida **avtomatik ijro etiladigan** algoritmdir. Klassik misol — "
                    "savdo avtomati: tanga tashlansa, mahsulot beriladi; inson ishtiroki va ishonch talab etilmaydi.\n\n"
                    "Huquqiy tabiati masalasida doktrinada uch yondashuv mavjud: (1) smart-kontrakt — shartnomaning "
                    "alohida **shakli** (yozma yoki elektron shaklning bir ko‘rinishi); (2) smart-kontrakt — shartnoma "
                    "emas, balki majburiyatni **ijro etish usuli**; (3) smart-kontrakt — mustaqil huquqiy hodisa. "
                    "Ko‘pchilik olimlar ikkinchi yondashuvga moyil: taraflar irodasining kelishuvi (oferta va akseptga "
                    "asoslangan bitim) fuqarolik huquqi bo‘yicha baholanadi, kod esa shu kelishuvni bajaruvchi texnik "
                    "mexanizmdir.\n\n"
                    "Bundan muhim xulosa kelib chiqadi: kod «o‘z-o‘zidan qonun» emas. Smart-kontraktga ham Fuqarolik "
                    "kodeksining shartnoma erkinligi, bitimlarning haqiqiyligi shartlari, vijdonlilik va majburiyatni "
                    "buzganlik uchun javobgarlikka oid umumiy qoidalari tatbiq etiladi. Qonunga zid shart kodga "
                    "yozilgani bilan haqiqiy bo‘lib qolmaydi."
                ),
            },
            {
                "sarlavha": "3. Smart-kontraktning mantiqiy tuzilishi: gipoteza — dispozitsiya — sanksiya",
                "matn": (
                    "Huquq nazariyasida huquq normasi uch elementdan iborat mantiqiy tuzilishga ega: **gipoteza** "
                    "(norma amal qila boshlaydigan shart-sharoit), **dispozitsiya** (xulq-atvor qoidasining o‘zi — "
                    "huquq va majburiyatlar) va **sanksiya** (qoidani buzganlik uchun noqulay oqibat). Bu tuzilish "
                    "«agar … bo‘lsa, u holda …, aks holda …» formulasi bilan ifodalanadi.\n\n"
                    "Dasturlashdagi shartli operator ham aynan shu mantiqqa qurilgan: `IF (shart) THEN (harakat) ELSE "
                    "(muqobil oqibat)`. Shuning uchun smart-kontraktni huquq normasining «bajariladigan» modeli deyish "
                    "mumkin:\n\n"
                    "- **Gipoteza** → `IF`: «Agar yuk belgilangan sanagacha omborga yetkazilgani datchik (orakl) "
                    "tomonidan tasdiqlansa…»\n"
                    "- **Dispozitsiya** → `THEN`: «…xaridorning hisobidagi mablag‘ sotuvchiga o‘tkaziladi».\n"
                    "- **Sanksiya** → `ELSE`: «…aks holda kechiktirilgan har bir kun uchun penya avtomatik ushlab "
                    "qolinadi yoki mablag‘ xaridorga qaytariladi».\n\n"
                    "Ammo o‘xshashlik to‘liq emas. Huquq normasi **baholovchi tushunchalar** bilan ishlaydi: «oqilona "
                    "muddat», «vijdonan», «uzrli sabab», «yengib bo‘lmas kuch». Kod esa faqat aniq, ikkilik (ha/yo‘q) "
                    "shartlarni tushunadi. Huquqni qo‘llovchi vaziyatning barcha holatlarini inobatga oladi, kod esa "
                    "ko‘zda tutilmagan vaziyatda ham buyruqni ko‘r-ko‘rona bajaradi. Bundan tashqari, sanksiyani davlat "
                    "majburlov apparati emas, dasturning o‘zi «ijro etadi» — bu himoyalanish huquqi, sudga murojaat va "
                    "xatoni tuzatish imkoniyati masalalarini kun tartibiga qo‘yadi."
                ),
            },
            {
                "sarlavha": "4. «Tartibga solish qumdonlari» — eksperimental huquqiy rejimlar",
                "matn": (
                    "Texnologiya huquqdan tez rivojlanadi. Qonun chiqaruvchi ikki xavf orasida qoladi: yangi "
                    "texnologiyani erta va qattiq tartibga solsa — innovatsiyani bo‘g‘adi; tartibga solmasa — fuqarolar "
                    "huquqlari himoyasiz qoladi. Bu dilemmaning yechimlaridan biri — **Regulatory Sandbox** («tartibga "
                    "solish qumdoni»), ya’ni eksperimental (maxsus) huquqiy rejim.\n\n"
                    "Qumdonning mohiyati: cheklangan ishtirokchilar doirasi uchun, cheklangan hudud yoki sohada, "
                    "**belgilangan muddatga** amaldagi ayrim talablar yengillashtiriladi yoki maxsus qoidalar "
                    "o‘rnatiladi; tajriba vakolatli organ nazorati ostida o‘tadi; yakunida natijalar baholanib, norma "
                    "umumiy qonunchilikka joriy etiladi yoki rad qilinadi. Birinchi moliyaviy-texnologik qumdon 2016-yilda "
                    "Buyuk Britaniyada ishga tushirilgan.\n\n"
                    "Nazariy jihatdan eksperimental rejim huquqiy tartibga solishning alohida usuli — **huquqiy "
                    "eksperiment**dir. U qonun oldida tenglik prinsipini buzmaydi, agar: (a) rejimga kirish mezonlari "
                    "oldindan, ochiq va barcha uchun bir xil belgilangan; (b) rejim vaqtinchalik; (c) inson hayoti, "
                    "sog‘lig‘i va asosiy huquqlariga oid kafolatlar saqlab qolingan; (d) ishtirokchining yetkazilgan zarar "
                    "uchun javobgarligi bekor qilinmagan bo‘lsa."
                ),
            },
            {
                "sarlavha": "5. O‘zbekiston tajribasi: PQ-4996-son qaror va sun’iy intellekt uchun maxsus rejim",
                "matn": (
                    "O‘zbekiston Respublikasi Prezidentining 2021-yil 17-fevraldagi «Sun’iy intellekt texnologiyalarini "
                    "jadal joriy etish uchun shart-sharoitlar yaratish chora-tadbirlari to‘g‘risida»gi **PQ-4996-son** "
                    "qarori mamlakatda sun’iy intellektni rivojlantirishning dastlabki dasturiy hujjati bo‘ldi. Qarorda "
                    "ustuvor tarmoqlarda tajriba-sinov loyihalarini amalga oshirish, ilmiy-tadqiqot va kadrlar "
                    "tayyorlash infratuzilmasini yaratish bilan birga, sun’iy intellekt texnologiyalarini qo‘llash "
                    "bo‘yicha **maxsus rejim**ni joriy etish nazarda tutildi.\n\n"
                    "Keyinchalik, 2021-yil 26-avgustdagi Prezident qarori bilan ushbu maxsus rejimning tashkiliy-huquqiy "
                    "asoslari aniqlashtirildi: rejim doirasida sun’iy intellektga asoslangan tajriba-sinov ishlarini "
                    "o‘tkazish, dasturiy mahsulotlar yaratish va xizmat ko‘rsatish bilan shug‘ullanuvchi ishtirokchilar "
                    "uchun alohida huquqiy shart-sharoit, ruxsat beruvchi hujjatlarni soddalashtirilgan tartibda olish "
                    "imkoniyati belgilandi. Bu — klassik «tartibga solish qumdoni» modelining milliy ko‘rinishidir.\n\n"
                    "2024-yil 14-oktabrdagi **PQ-358-son** qaror bilan «Sun’iy intellekt texnologiyalarini 2030-yilga qadar "
                    "rivojlantirish strategiyasi» tasdiqlanib, bu yo‘nalish strategik darajaga ko‘tarildi. Shu tariqa "
                    "milliy model «avval tajriba — keyin umumiy norma» mantig‘ida rivojlanmoqda: eksperimental rejimda "
                    "to‘plangan tajriba qonunchilikni bosqichma-bosqich takomillashtirish uchun empirik asos bo‘ladi."
                ),
            },
            {
                "sarlavha": "6. Xulosa: «Law is Code»ga emas, «Law over Code»ga",
                "matn": (
                    "«Code is Law» — ogohlantiruvchi tashxis, dastur emas. Kod haqiqatan ham xulq-atvorni tartibga "
                    "soladi, lekin huquqiy davlatda u qonunga bo‘ysunadi: Konstitutsiya va qonunlarning ustunligi raqamli "
                    "muhitda ham so‘zsiz amal qiladi. Smart-kontrakt huquq normasining mantiqiy tuzilishini takrorlaydi, "
                    "ammo adolat, vijdonlilik va mutanosiblik kabi baholovchi mezonlarni o‘zida mujassam eta olmaydi — "
                    "bularni huquqni qo‘llovchi inson ta’minlaydi. Eksperimental huquqiy rejimlar esa huquq va texnologiya "
                    "o‘rtasidagi «tezlik farqi»ni boshqarishning eng oqilona vositasi bo‘lib qolmoqda."
                ),
            },
        ],
        "xulosalar": [
            "Lessigga ko‘ra xulq-atvorni huquq, ijtimoiy normalar, bozor va arxitektura (kod) tartibga soladi.",
            "Smart-kontraktning IF–THEN–ELSE mantiqi huquq normasining gipoteza–dispozitsiya–sanksiya tuzilishiga mos keladi.",
            "Kod baholovchi tushunchalarni («vijdonan», «oqilona muddat») anglamaydi — bu uning asosiy cheklovi.",
            "PQ-4996-son qaror bilan nazarda tutilgan maxsus rejim — «tartibga solish qumdoni»ning milliy modeli.",
        ],
    },
    # ------------------------------------------------------------------ 3
    {
        "id": "si-huquqiy-maqomi",
        "raqam": 3,
        "sarlavha": "Sun’iy intellektning huquqiy maqomi va yuridik javobgarlik subyekti muammosi",
        "qisqa": "SI huquqiy maqomi va javobgarlik",
        "annotatsiya": (
            "Maqolada huquq subyektliligi kategoriyalari (huquq layoqati, muomala layoqati, delikt layoqati) "
            "sun’iy intellektga nisbatan tahlil qilinadi, SI maqomiga oid uch konsepsiya solishtiriladi, yuridik "
            "javobgarlikning subyektiv tomoni (ayb) muammosi hamda zarar uchun javobgarlikni dasturchi, mulkdor va "
            "ma’lumotlar bazasi egasi o‘rtasida taqsimlash modellari ko‘rib chiqiladi."
        ),
        "kalit_sozlar": [
            "huquq subyekti", "huquq layoqati", "muomala layoqati", "elektron shaxs", "kvazi-subyekt",
            "ayb", "oshiqcha xavf manbai", "FK 999-modda",
        ],
        "oqish_vaqti": 10,
        "bolimlar": [
            {
                "sarlavha": "1. Huquq subyekti: huquq layoqati, muomala layoqati, ong va erkin iroda",
                "matn": (
                    "Huquq nazariyasida **huquq subyekti** — huquqiy munosabat ishtirokchisi bo‘la oladigan, subyektiv "
                    "huquq va yuridik majburiyatlarga ega shaxs. Huquq subyektliligi uch elementdan tashkil topadi: "
                    "**huquq layoqati** (huquq va majburiyatlarga ega bo‘lish qobiliyati), **muomala layoqati** (o‘z "
                    "harakatlari bilan huquqlarni qo‘lga kiritish va amalga oshirish, majburiyatlarni yaratish va "
                    "bajarish qobiliyati) hamda **delikt layoqati** (sodir etgan huquqbuzarligi uchun javob bera olish "
                    "qobiliyati).\n\n"
                    "Jismoniy shaxsda muomala layoqati ikki psixologik mezon bilan bog‘liq: **intellektual** (o‘z "
                    "harakatlarining ahamiyatini anglash) va **irodaviy** (ularni boshqara olish). Aynan ong va erkin "
                    "iroda mavjudligi shaxsga uning qilmishini «ayb» sifatida yuklash imkonini beradi. Yuridik shaxs esa "
                    "— huquqiy fiksiya: uning «irodasi» organlari orqali, ya’ni pirovardida odamlar orqali shakllanadi.\n\n"
                    "Zamonaviy sun’iy intellekt tizimlari mustaqil «qaror» chiqaradi, o‘rganadi, ba’zan yaratuvchisi "
                    "ham oldindan ko‘ra olmagan natija beradi. Biroq bu **avtonomlik** ong va iroda bilan teng emas: tizim "
                    "maqsadni o‘zi belgilamaydi, o‘z harakatining ijtimoiy va huquqiy ahamiyatini anglamaydi, mas’uliyat "
                    "hissiga ega emas. Savol shundan iborat: bunday tizim huquq obyektimi yoki subyektimi?"
                ),
            },
            {
                "sarlavha": "2. Birinchi konsepsiya: sun’iy intellekt — huquq obyekti",
                "matn": (
                    "Hukmron (an’anaviy) yondashuvga ko‘ra, sun’iy intellekt — **huquq obyekti**: dasturiy ta’minot "
                    "sifatida u intellektual mulk obyekti, qurilmaga joylangan holda esa — ashyo (mol-mulk). U kimningdir "
                    "mulki, kimdir uni yaratgan, kimdir undan foydalanadi. Demak, SI «harakati» natijasida kelib chiqqan "
                    "barcha huquqiy oqibatlar uning ortida turgan insonlar va tashkilotlarga yuklanadi.\n\n"
                    "Bu konsepsiyaning afzalligi — huquq tizimining barqarorligi: yangi subyekt o‘ylab topish shart emas, "
                    "mavjud institutlar (mulk huquqi, shartnoma, delikt, mahsulot nuqsoni uchun javobgarlik) ishlayveradi. "
                    "Amaldagi O‘zbekiston qonunchiligi ham shu pozitsiyada turadi: huquq subyektlari — jismoniy shaxslar, "
                    "yuridik shaxslar va davlat; SI ularning qatorida ko‘rsatilmagan.\n\n"
                    "Kamchiligi — tizim qanchalik avtonom bo‘lsa, zarar bilan aniq bir insonning xatti-harakati "
                    "o‘rtasidagi sababiy bog‘lanishni va uning aybini isbotlash shunchalik qiyinlashadi («javobgarlik "
                    "bo‘shlig‘i» xavfi)."
                ),
            },
            {
                "sarlavha": "3. Ikkinchi konsepsiya: «elektron shaxs» — kvazi-subyekt nazariyasi",
                "matn": (
                    "Yevropa Parlamentining 2017-yil 16-fevraldagi robototexnikaga oid fuqarolik-huquqiy normalar "
                    "to‘g‘risidagi rezolyutsiyasida eng murakkab avtonom robotlar uchun kelajakda maxsus huquqiy maqom — "
                    "**«elektron shaxs» (electronic person)** maqomini joriy etish imkoniyatini o‘rganish taklif qilingan "
                    "edi. G‘oya yuridik shaxs institutiga o‘xshatmaga asoslanadi: agar huquq kompaniyani — jonsiz "
                    "tuzilmani — subyekt deb tan olgan ekan, nega avtonom tizimni ham cheklangan, maqsadli huquq "
                    "layoqatiga ega **kvazi-subyekt** deb tan olmaslik kerak?\n\n"
                    "Bu modelda elektron shaxs reyestrda ro‘yxatdan o‘tadi, unga sug‘urta fondi yoki alohida mol-mulk "
                    "biriktiriladi va zarar shu fond hisobidan qoplanadi. Tarafdorlar buni jabrlanuvchi manfaatini tez "
                    "himoya qilish vositasi deb biladi.\n\n"
                    "Tanqidchilar (jumladan, 2018-yilda Yevropaning 150 dan ortiq olim va mutaxassisi ochiq xat bilan chiqqan) quyidagi "
                    "e’tirozlarni bildiradi: birinchidan, SIda ong, iroda va manfaat yo‘q — demak, huquq subyektliligining "
                    "mazmuniy asosi yo‘q; ikkinchidan, yuridik shaxs ortida doimo odamlar turadi, elektron shaxs esa "
                    "ishlab chiqaruvchilar uchun **javobgarlikdan qochish «qalqoni»**ga aylanishi mumkin; uchinchidan, "
                    "jazo va tarbiyaviy ta’sir mashinaga nisbatan ma’nosiz. Natijada Yevropa Ittifoqining 2024-yilda qabul "
                    "qilingan Sun’iy intellekt to‘g‘risidagi reglamenti (AI Act) elektron shaxs maqomini joriy etmadi va "
                    "xavfga asoslangan yondashuvni tanladi."
                ),
            },
            {
                "sarlavha": "4. Uchinchi konsepsiya: texnik vosita / agentlik modeli",
                "matn": (
                    "Uchinchi yondashuv oraliq pozitsiyani egallaydi. Unga ko‘ra, SI subyekt emas, lekin oddiy ashyo ham "
                    "emas — u insonning **vositasi yoki «elektron agenti»**. Tizim amalga oshirgan har bir yuridik "
                    "ahamiyatli harakat (masalan, avtomatik tuzilgan bitim) uni ishga tushirgan va nazorat qilayotgan "
                    "shaxsning harakati hisoblanadi — xuddi vakilning harakati vakolat beruvchi uchun huquqiy oqibat "
                    "tug‘dirgani kabi.\n\n"
                    "Fuqarolik huquqidagi vakillikdan farqi shundaki, haqiqiy vakil o‘zi huquq subyekti bo‘ladi va "
                    "vakolat doirasidan chiqqani uchun shaxsan javob beradi; elektron agent esa javobgarlikning mustaqil "
                    "subyekti bo‘la olmaydi. Shuning uchun bu model ko‘proq **yuklash (atributsiya) qoidasi** sifatida "
                    "ishlaydi: algoritm xatosi xavfi undan foyda ko‘rayotgan va uni nazorat qila oladigan shaxs "
                    "zimmasida qoladi.\n\n"
                    "Jinoyat huquqida ham xuddi shu mantiq amal qiladi: SI — jinoyat **quroli yoki vositasi**. "
                    "O‘zbekiston Jinoyat kodeksiga ko‘ra jinoyat subyekti faqat aqli raso, qonunda belgilangan yoshga "
                    "to‘lgan jismoniy shaxs bo‘lishi mumkin; javobgarlik esa faqat aybi isbotlangan ijtimoiy xavfli "
                    "qilmish uchun yuzaga keladi."
                ),
            },
            {
                "sarlavha": "5. Yuridik javobgarlikning subyektiv tomoni: ayb muammosi",
                "matn": (
                    "Huquqbuzarlik tarkibi to‘rt elementdan iborat: obyekt, obyektiv tomon, subyekt va **subyektiv "
                    "tomon**. Subyektiv tomonning o‘zagi — **ayb**, ya’ni shaxsning o‘z qilmishi va uning oqibatlariga "
                    "ruhiy munosabati (qasd yoki ehtiyotsizlik shaklida). «Ayb uchun javobgarlik» jinoyat huquqining "
                    "asosiy prinsiplaridan biridir.\n\n"
                    "Algoritmda ruhiy munosabat yo‘q — u oqibatni «xohlamaydi» ham, unga «beparvo qaramaydi» ham. Demak, "
                    "ommaviy-huquqiy (jinoiy, ma’muriy) javobgarlikni SIga nisbatan qo‘llash nazariy jihatdan imkonsiz. "
                    "Ayb doimo inson harakatida izlanadi: dasturchi xavfsizlik talablarini qo‘pol ravishda buzganmi? "
                    "Operator tizimni ko‘rsatmaga zid ishlatganmi? Mulkdor yangilanishlarni o‘rnatmay, ogohlantirishni "
                    "e’tiborsiz qoldirganmi? Har birining aybi alohida isbotlanishi shart, shubhalar esa aybsizlik "
                    "prezumpsiyasiga ko‘ra ularning foydasiga hal qilinadi.\n\n"
                    "Fuqarolik huquqida esa vaziyat boshqacha: bu yerda javobgarlikning maqsadi jazolash emas, "
                    "**zararni qoplash**. Shuning uchun fuqarolik huquqi **aybsiz (qat’iy) javobgarlik**ni ham biladi — "
                    "va aynan shu institut SI muammosining amaliy yechimiga aylanmoqda."
                ),
            },
            {
                "sarlavha": "6. Javobgarlikni taqsimlash: dasturchi, mulkdor va ma’lumotlar bazasi egasi",
                "matn": (
                    "**Mulkdor (egalik qiluvchi) — FK 999-modda analogiyasi.** Fuqarolik kodeksining 999-moddasiga "
                    "ko‘ra, faoliyati atrofdagilar uchun oshiqcha xavf bilan bog‘liq bo‘lgan shaxslar (transport "
                    "vositalari, mexanizmlar, yuqori kuchlanishli elektr energiyasidan foydalanish va h.k.) oshiqcha xavf "
                    "manbai yetkazgan zararni, agar zarar yengib bo‘lmas kuch yoki jabrlanuvchining qasdi oqibatida kelib "
                    "chiqqanini isbotlay olmasalar, **aybidan qat’i nazar** qoplashlari shart. Avtonom transport, dron, "
                    "sanoat roboti kabi SI tizimlarini oshiqcha xavf manbaiga o‘xshatish doktrinada eng ko‘p "
                    "qo‘llab-quvvatlanadigan yechimdir: kim texnologiyadan foyda ko‘rsa va uni nazorat qilsa, xavfni ham "
                    "o‘sha ko‘taradi. Jabrlanuvchi algoritmning ichki mantig‘ini isbotlashi shart emas — zarar va sababiy "
                    "bog‘lanishni ko‘rsatish kifoya.\n\n"
                    "**Dasturchi (ishlab chiquvchi).** Agar zarar algoritmning konstruktiv nuqsoni, yetarli sinovdan "
                    "o‘tkazilmagani yoki xavf haqida ogohlantirilmagani sababli kelib chiqqan bo‘lsa, ishlab chiquvchi "
                    "tovar (ish, xizmat) nuqsonlari oqibatida yetkazilgan zarar qoidalari bo‘yicha javob beradi. Zararni "
                    "qoplagan mulkdor unga nisbatan **regress** (qaytarma) talab qo‘yish huquqiga ega.\n\n"
                    "**Ma’lumotlar bazasi egasi.** Mashinali o‘qitishda tizimning «xulqi» koddan ko‘ra ko‘proq "
                    "o‘rgatuvchi ma’lumotlarga bog‘liq. Noto‘g‘ri, to‘liq bo‘lmagan yoki tarafkash ma’lumotlar to‘plami "
                    "kamsituvchi yoki xato qarorga olib kelsa, ma’lumotlarni shakllantirgan va taqdim etgan shaxsning "
                    "javobgarligi masalasi tug‘iladi; shaxsga doir ma’lumotlarga ishlov berilgan bo‘lsa — O‘RQ-547-son "
                    "Qonun talablari ham qo‘llanadi.\n\n"
                    "**Xulosa.** Amaldagi huquq nuqtayi nazaridan SI — huquq obyekti; javobgarlik «zanjir» bo‘ylab "
                    "taqsimlanadi: jabrlanuvchi oldida — manbaga egalik qiluvchi (aybsiz javobgarlik), ichki munosabatlarda "
                    "— har kim o‘z aybi va hissasiga yarasha (regress). Majburiy sug‘urta va tizim harakatlarini qayd "
                    "etuvchi jurnallar (logging) bu modelning zarur texnik-huquqiy kafolatlaridir."
                ),
            },
        ],
        "xulosalar": [
            "Huquq subyektliligi ong va erkin irodaga tayanadi; SI avtonomligi bularning o‘rnini bosa olmaydi.",
            "Uch konsepsiya: obyekt; «elektron shaxs» (kvazi-subyekt); texnik vosita/agent. Amaldagi huquq — birinchisida.",
            "Ayb — ruhiy munosabat; shuning uchun jinoiy javobgarlik faqat insonga yuklanadi, SI esa jinoyat vositasidir.",
            "FK 999-modda analogiyasi jabrlanuvchini himoya qiladi: egalik qiluvchi aybidan qat’i nazar javob beradi, so‘ng regress.",
        ],
    },
    # ------------------------------------------------------------------ 4
    {
        "id": "probellar-algoritmik-adolat",
        "raqam": 4,
        "sarlavha": "Huquqiy bo‘shliqlar (probellar), avtomatlashtirilgan huquqni qo‘llash va algoritmik adolat",
        "qisqa": "Probellar va algoritmik adolat",
        "annotatsiya": (
            "Maqolada raqamli davrning tipik huquqiy bo‘shliqlari (deepfake, SI mualliflik huquqi, elektron dalillar), "
            "ularni to‘ldirish usullari — qonun va huquq analogiyasi, jinoyat huquqida analogiyaning taqiqlanishi, "
            "huquqni qo‘llash bosqichlarining avtomatlashuvi, «qora quti» muammosi hamda konstitutsiyaviy "
            "kafolatlar va «Human-in-the-loop» qoidasi tahlil qilinadi."
        ),
        "kalit_sozlar": [
            "huquqiy bo‘shliq", "probel", "qonun analogiyasi", "huquq analogiyasi", "JK 4-modda",
            "deepfake", "Black Box", "aybsizlik prezumpsiyasi", "mutanosiblik", "Human-in-the-loop",
        ],
        "oqish_vaqti": 11,
        "bolimlar": [
            {
                "sarlavha": "1. Huquqiy bo‘shliq tushunchasi va raqamli davr probellari",
                "matn": (
                    "**Huquqiy bo‘shliq (probel)** — huquqiy tartibga solish doirasiga kiruvchi va yuridik hal etilishi "
                    "lozim bo‘lgan ijtimoiy munosabatni tartibga soluvchi normaning to‘liq yoki qisman mavjud emasligi. "
                    "Uni «qonun chiqaruvchining malakali sukuti»dan (munosabatni ataylab tartibga solmaslikdan) farqlash "
                    "kerak. Probellar **boshlang‘ich** (norma qabul qilinayotganda yo‘l qo‘yilgan) va **keyingi** (yangi "
                    "munosabatlar paydo bo‘lishi natijasida yuzaga kelgan) turlarga bo‘linadi. Raqamli texnologiyalar "
                    "asosan keyingi probellarni tug‘diradi.\n\n"
                    "**Deepfake.** Sun’iy intellekt yordamida shaxsning yuzi yoki ovozi ishonarli tarzda soxtalashtirilgan "
                    "video va audio materiallar sha’n va qadr-qimmatga, shaxsiy hayot daxlsizligiga, mulkka (firibgarlik) "
                    "tajovuz vositasiga aylandi. Qonun chiqaruvchi bu bo‘shliqni bosqichma-bosqich to‘ldirmoqda: 2026-yil "
                    "21-yanvardagi O‘RQ-1115-son Qonun bilan «Axborotlashtirish to‘g‘risida»gi Qonunga sun’iy intellektdan "
                    "foydalanishning umumiy asoslari kiritildi, SI yordamida shaxsga doir ma’lumotlarga qonunga xilof "
                    "ravishda ishlov berish va ularni tarqatish uchun ma’muriy javobgarlik belgilandi. Biroq deepfakening "
                    "o‘zini yaratish uchun alohida jinoyat tarkibi masalasi doktrinada munozarali bo‘lib qolmoqda.\n\n"
                    "**SI va mualliflik huquqi.** «Mualliflik huquqi va turdosh huquqlar to‘g‘risida»gi Qonunga ko‘ra "
                    "muallif — ijodiy mehnati bilan asar yaratgan jismoniy shaxs. Generativ model yaratgan matn yoki "
                    "tasvirning muallifi kim: foydalanuvchimi, model yaratuvchisimi yoki hech kimmi? Qonunda bunga "
                    "to‘g‘ridan-to‘g‘ri javob yo‘q.\n\n"
                    "**Elektron dalillar.** Raqamli izlar, bulutli saqlash joylaridagi ma’lumotlar, algoritm xulosalari "
                    "dalil sifatida qanday rasmiylashtiriladi, ularning maqbulligi, ishonchliligi va o‘zgartirilmagani "
                    "qanday tekshiriladi? Deepfake davrida «videoda ko‘rinib turibdi» degan dalilning o‘zi maxsus "
                    "ekspertizasiz yetarli bo‘lmay qolmoqda."
                ),
            },
            {
                "sarlavha": "2. Bo‘shliqlarni to‘ldirish: qonun analogiyasi va huquq analogiyasi",
                "matn": (
                    "Probelni **bartaraf etish**ning yagona to‘liq usuli — huquq ijodkorligi, ya’ni yetishmayotgan normani "
                    "qabul qilish. Ammo sud nizoni «qonunda norma yo‘q» degan sabab bilan hal qilmasdan qoldira olmaydi. "
                    "Shuning uchun huquqni qo‘llash jarayonida probel aniq ish doirasida **yengib o‘tiladi** — buning "
                    "vositasi analogiyadir.\n\n"
                    "**Qonun analogiyasi** — nizoli munosabatga o‘xshash munosabatni tartibga soluvchi aniq normani "
                    "qo‘llash. **Huquq analogiyasi** — bunday o‘xshash norma ham bo‘lmaganda, ishni qonunchilikning "
                    "umumiy asoslari va mazmuni, halollik, oqilonalik va adolat talablaridan kelib chiqib hal etish.\n\n"
                    "Fuqarolik kodeksining 5-moddasi aynan shu ikki bosqichli mexanizmni mustahkamlaydi: fuqarolik "
                    "munosabatlari qonunchilik yoki taraflar kelishuvi bilan bevosita tartibga solinmagan hollarda "
                    "o‘xshash munosabatlarni tartibga soluvchi norma qo‘llaniladi, buning imkoni bo‘lmasa — taraflarning "
                    "huquq va majburiyatlari fuqarolik qonunchiligining umumiy asoslari va mazmuni, vijdonlilik, "
                    "oqilonalik va adolat talablariga amal qilgan holda belgilanadi. Masalan, smart-kontrakt yoki "
                    "raqamli aktivlar bilan bog‘liq nizoda sud shartnomalar haqidagi umumiy qoidalarni o‘xshashlik "
                    "bo‘yicha qo‘llashi mumkin.\n\n"
                    "Analogiyani qo‘llash shartlari: munosabat huquqiy tartibga solish doirasida bo‘lishi; probel "
                    "haqiqatan mavjud bo‘lishi; munosabatlar muhim belgilariga ko‘ra o‘xshash bo‘lishi; analogiya qonunda "
                    "taqiqlanmagan bo‘lishi; qaror asoslantirilgan bo‘lishi."
                ),
            },
            {
                "sarlavha": "3. Jinoyat huquqida analogiyaning taqiqlanishi (JK 4-modda)",
                "matn": (
                    "Xususiy huquqda ruxsat etilgan narsa ommaviy-huquqiy javobgarlik sohasida qat’iyan taqiqlanadi. "
                    "Jinoyat kodeksining **4-moddasi** — qonuniylik prinsipi — quyidagicha belgilaydi: sodir etilgan "
                    "qilmishning jinoiyligi, jazoga sazovorligi va boshqa huquqiy oqibatlari **faqat Jinoyat kodeksi "
                    "bilan** belgilanadi. Bu qoidadan jinoyat qonunini o‘xshashlik bo‘yicha qo‘llashga yo‘l "
                    "qo‘yilmasligi kelib chiqadi; u qadimiy *nullum crimen, nulla poena sine lege* («qonunda "
                    "ko‘rsatilmagan bo‘lsa — jinoyat ham, jazo ham yo‘q») tamoyilining ifodasidir.\n\n"
                    "Taqiqning nazariy asoslari: (1) **huquqiy aniqlik** — shaxs qaysi qilmish jinoyat ekanini oldindan "
                    "bilishi kerak; (2) **hokimiyatlar bo‘linishi** — jinoyat tarkibini sud yoki tergovchi emas, faqat "
                    "qonun chiqaruvchi yaratadi; (3) **shaxs erkinligining kafolati** — davlatning jazolash hokimiyati "
                    "qonun bilan cheklanadi; (4) Konstitutsiyaga ko‘ra qonunchilikdagi ziddiyat va noaniqliklar inson "
                    "foydasiga talqin etiladi.\n\n"
                    "Raqamli davr uchun amaliy xulosa: agar yangi turdagi ijtimoiy xavfli qilmish (masalan, deepfake "
                    "yaratishning o‘zi) Jinoyat kodeksida nazarda tutilmagan bo‘lsa, tergovchi uni «eng yaqin» moddaga "
                    "sun’iy ravishda «tortib» kvalifikatsiya qila olmaydi. Lekin **analogiya bilan talqinni farqlash "
                    "zarur**: agar deepfake yordamida birovning mulki aldash yo‘li bilan qo‘lga kiritilgan bo‘lsa, bu "
                    "analogiya emas — qilmish firibgarlik tarkibining barcha belgilariga bevosita mos keladi, deepfake "
                    "esa shunchaki aldash usulidir."
                ),
            },
            {
                "sarlavha": "4. Huquqni qo‘llashning uch bosqichi va ularning avtomatlashuvi",
                "matn": (
                    "Huquqni qo‘llash — vakolatli organning huquq normasini aniq hayotiy holatga tatbiq etib, individual "
                    "hokimiyat qarorini chiqarishga qaratilgan faoliyati. U uch bosqichdan iborat:\n\n"
                    "1. **Ishning haqiqiy (faktik) holatlarini aniqlash** — dalillarni to‘plash, tekshirish va baholash. "
                    "Bu bosqich eng ko‘p avtomatlashmoqda: yuzni tanish, avtomatik foto-video qayd etish, katta "
                    "hajmdagi yozishmalar va tranzaksiyalarni tahlil qilish, raqamli kriminalistika.\n"
                    "2. **Ishning yuridik asosini aniqlash** — qo‘llanilishi lozim bo‘lgan normani tanlash, uning "
                    "haqiqiyligini tekshirish, talqin qilish va qilmishni kvalifikatsiya qilish. Bu yerda huquqiy "
                    "qidiruv tizimlari, o‘xshash sud qarorlarini topuvchi va kvalifikatsiya variantini taklif qiluvchi "
                    "yordamchi dasturlar qo‘llanadi.\n"
                    "3. **Qaror qabul qilish va huquqni qo‘llash hujjatini rasmiylashtirish.** Oddiy, nizosiz va ommaviy "
                    "ishlarda (masalan, kamera qayd etgan tezlikni oshirish uchun jarima) qaror loyihasi to‘liq avtomatik "
                    "shakllantiriladi.\n\n"
                    "Avtomatlashtirish tezlik, bir xillik va inson omilidan xoli bo‘lish kabi afzalliklar beradi. Ammo "
                    "bosqich qanchalik baholovchi xususiyatga ega bo‘lsa (dalillarni ichki ishonch bo‘yicha baholash, "
                    "aybni aniqlash, jazoni individuallashtirish), uni mashinaga topshirish shunchalik xavfli. Baholash "
                    "— hisoblash emas; u vijdon, hayotiy tajriba va adolat tuyg‘usini talab qiladi."
                ),
            },
            {
                "sarlavha": "5. «Qora quti» (Black Box) muammosi va konstitutsiyaviy kafolatlar",
                "matn": (
                    "Murakkab neyron tarmoqlar kirish ma’lumotidan chiqish natijasiga qanday kelganini hatto "
                    "yaratuvchilari ham to‘liq tushuntirib bera olmaydi. Bu — **«qora quti» (Black Box)** muammosi. "
                    "Huquq uchun u uch jihatdan xavfli: qaror **asoslantirilmagan** bo‘lib qoladi; shaxs unga qarshi "
                    "**samarali e’tiroz bildira olmaydi** (nimaga e’tiroz bildirishni bilmaydi); o‘rgatuvchi "
                    "ma’lumotlardagi **yashirin tarafkashlik** (algorithmic bias) aniqlanmay qoladi.\n\n"
                    "**Aybsizlik prezumpsiyasi (Konstitutsiyaning 28-moddasi).** Jinoyat sodir etganlikda ayblanayotgan "
                    "shaxs uning aybi qonunda nazarda tutilgan tartibda oshkora sud muhokamasi yo‘li bilan isbotlanmaguncha "
                    "va sudning qonuniy kuchga kirgan hukmi bilan aniqlanmaguncha aybsiz hisoblanadi; aybdorlikka oid "
                    "barcha shubhalar, agar ularni bartaraf etish imkoniyatlari tugagan bo‘lsa, ayblanuvchi foydasiga hal "
                    "qilinadi; shaxs o‘z aybsizligini isbotlashga majbur emas. «Aybdorlik ehtimoli 92 foiz» degan "
                    "algoritmik baho bu kafolatga zid tarzda isbotlash yukini amalda shaxsning o‘ziga ag‘daradi. "
                    "Statistik ehtimollik — dalil emas, guruh haqidagi umumlashma; jinoiy javobgarlik esa qat’iy "
                    "individualdir.\n\n"
                    "**Mutanosiblik prinsipi (Konstitutsiyaning 20- va 21-moddalari).** Konstitutsiyaning 20-moddasiga "
                    "ko‘ra davlat organlari tomonidan insonga nisbatan qo‘llaniladigan huquqiy ta’sir choralari "
                    "mutanosiblik prinsipiga asoslanishi va qonunlarda nazarda tutilgan maqsadlarga erishish uchun yetarli "
                    "bo‘lishi kerak; 21-moddaga ko‘ra esa inson huquq va erkinliklari faqat qonunga muvofiq va faqat "
                    "zarur bo‘lgan doirada cheklanishi mumkin. Ommaviy algoritmik kuzatuv, yalpi profillashtirish yoki "
                    "«xavf bali» asosida avtomatik cheklov qo‘llash ushbu mezonlar bo‘yicha — qonuniy maqsad, zaruriyat "
                    "va mutanosiblik testi orqali — tekshirilishi shart."
                ),
            },
            {
                "sarlavha": "6. «Human-in-the-loop» — algoritmik adolatning oltin qoidasi",
                "matn": (
                    "**Human-in-the-loop** («inson — qaror zanjirida») qoidasi shuni anglatadi: inson huquq va "
                    "erkinliklariga daxldor har qanday yuridik ahamiyatli qaror **inson tomonidan** qabul qilinadi; "
                    "algoritm faqat yordamchi, tavsiya beruvchi vazifani bajaradi. Bu rasmiy «imzo qo‘yish» emas, balki "
                    "mazmunli nazorat bo‘lishi lozim: mansabdor shaxs algoritm xulosasini tushunishi, tekshirishi, unga "
                    "qo‘shilmaslik vakolatiga va vaqtiga ega bo‘lishi, qarorni esa o‘z nomidan asoslantirishi kerak.\n\n"
                    "Ushbu qoida O‘zbekistonda endi nafaqat doktrina, balki pozitiv huquq normasidir: 2026-yil "
                    "21-yanvardagi O‘RQ-1115-son Qonun bilan «Axborotlashtirish to‘g‘risida»gi Qonunga kiritilgan "
                    "qoidaga ko‘ra, insonning huquq va erkinliklariga daxldor yuridik ahamiyatga ega qarorlarni qabul "
                    "qilishda **faqat sun’iy intellekt asosida ishlaydigan axborot tizimlarining xulosalariga tayanish "
                    "mumkin emas**.\n\n"
                    "Algoritmik adolatning qolgan talablari shu qoidadan kelib chiqadi: **shaffoflik** (shaxs unga "
                    "nisbatan algoritm qo‘llanganidan xabardor bo‘lishi), **tushuntiriluvchanlik** (qaror asoslari "
                    "tushunarli tilda bayon etilishi), **kamsitmaslik** (ma’lumotlar va natijalarning tarafkashlikka "
                    "tekshirilishi), **shikoyat qilish huquqi** (qarorni inson — yuqori organ yoki sud — qayta ko‘rib "
                    "chiqishi) va **javobgarlik** (har bir qaror ortida aniq mas’ul shaxs turishi).\n\n"
                    "Tergovchi uchun amaliy formula: algoritm — **versiya manbai**, dalil emas. U qayerga qarash "
                    "kerakligini ko‘rsatishi mumkin, lekin aybni faqat qonuniy yo‘l bilan to‘plangan, tekshirilgan va "
                    "ichki ishonch asosida baholangan dalillar isbotlaydi."
                ),
            },
        ],
        "xulosalar": [
            "Raqamli texnologiyalar «keyingi» probellarni tug‘diradi: deepfake, SI yaratgan asarlar, elektron dalillar.",
            "Fuqarolik huquqida probel qonun va huquq analogiyasi bilan yengib o‘tiladi (FK 5-modda); jinoyat huquqida analogiya taqiqlangan (JK 4-modda).",
            "«Qora quti» xulosasi aybsizlik prezumpsiyasi (28-modda) va mutanosiblik (20–21-moddalar) kafolatlari bilan cheklanadi.",
            "Human-in-the-loop: inson huquqlariga daxldor qarorni faqat SI xulosasiga tayanib qabul qilish mumkin emas (O‘RQ-1115).",
        ],
    },
]


def get_article(article_id: str) -> dict:
    """Identifikator bo‘yicha maqolani qaytaradi."""
    for article in ARTICLES:
        if article["id"] == article_id:
            return article
    return ARTICLES[0]


def article_full_text(article: dict) -> str:
    """Maqolaning to‘liq matnini (AI konteksti uchun) bitta satrga yig‘adi."""
    parts = [article["sarlavha"], "", "Annotatsiya: " + article["annotatsiya"], ""]
    for section in article["bolimlar"]:
        parts.append(section["sarlavha"])
        parts.append(section["matn"])
        parts.append("")
    parts.append("Asosiy xulosalar:")
    parts.extend("- " + item for item in article["xulosalar"])
    return "\n".join(parts)
