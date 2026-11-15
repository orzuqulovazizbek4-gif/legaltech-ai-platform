"""AI-Tergovchi / Kazus trenajyori — 4 ta amaliy kazus va namuna yechimlar."""

CASES = [
    {
        "id": "deepfake-firibgarlik",
        "raqam": 1,
        "sarlavha": "«Direktorning video-qo‘ng‘irog‘i»: deepfake orqali talon-toroj",
        "soha": "Jinoyat huquqi · Kvalifikatsiya · Analogiya taqiqi",
        "murakkablik": "O‘rta",
        "fabula": (
            "«Baraka Tekstil» MChJ bosh hisobchisi N. Karimovaga messenjer orqali video-qo‘ng‘iroq keladi. Ekranda "
            "korxona direktori S. Aliyevning yuzi ko‘rinadi, ovozi ham aynan unikidek. «Direktor» xorijiy hamkor bilan "
            "shoshilinch bitim tuzilayotganini aytib, 480 million so‘mni ko‘rsatilgan hisobraqamga zudlik bilan "
            "o‘tkazishni buyuradi. Hisobchi to‘lovni amalga oshiradi.\n\n"
            "Keyinroq aniqlanishicha, direktor o‘sha paytda samolyotda bo‘lgan va hech kimga qo‘ng‘iroq qilmagan. "
            "Tergov davomida fuqaro B. Tursunov direktorning ijtimoiy tarmoqlardagi ochiq videolaridan foydalanib, "
            "sun’iy intellekt dasturi yordamida uning yuzi va ovozini soxtalashtirgani (deepfake), pul esa uning "
            "tanishi nomidagi plastik kartaga tushib, naqdlashtirilgani ma’lum bo‘ladi.\n\n"
            "Tergovchi-stajyor qaror loyihasida shunday yozadi: «Jinoyat kodeksida deepfake yaratish uchun alohida modda "
            "mavjud emasligi sababli, qilmish unga eng yaqin bo‘lgan modda bo‘yicha o‘xshashlik asosida "
            "kvalifikatsiya qilinsin»."
        ),
        "savollar": [
            "Stajyorning «o‘xshashlik asosida kvalifikatsiya qilish» haqidagi xulosasi qonuniymi? Nima uchun?",
            "B. Tursunovning qilmishi qanday kvalifikatsiya qilinishi kerak? Bu analogiyami yoki normani bevosita qo‘llashmi?",
            "Bu ishda jinoyat subyekti kim? Sun’iy intellekt dasturining huquqiy o‘rni qanday?",
            "Deepfake video dalil sifatida qanday tekshirilishi lozim?",
        ],
        "namuna_yechim": (
            "**1. Analogiya masalasi.** Stajyorning asoslantirishi noqonuniy. Jinoyat kodeksining 4-moddasiga "
            "(qonuniylik prinsipi) ko‘ra qilmishning jinoiyligi, jazoga sazovorligi va boshqa huquqiy oqibatlari faqat "
            "Jinoyat kodeksi bilan belgilanadi; jinoyat qonunini o‘xshashlik bo‘yicha qo‘llashga yo‘l qo‘yilmaydi "
            "(*nullum crimen sine lege*). «Eng yaqin modda bo‘yicha» degan formula qaror uchun asos bo‘la olmaydi.\n\n"
            "**2. To‘g‘ri kvalifikatsiya.** Biroq bu ishda analogiyaga ehtiyoj ham yo‘q. B. Tursunov aldash yo‘li bilan "
            "o‘zganing mulkini qo‘lga kiritgan — bu firibgarlik tarkibining (Jinoyat kodeksining 168-moddasi) barcha "
            "belgilariga bevosita mos keladi: obyekt — mulkiy munosabatlar; obyektiv tomon — aldash orqali mulkni "
            "qo‘lga kiritish; subyektiv tomon — to‘g‘ri qasd va g‘arazli maqsad. Deepfake — aldashning usuli (vositasi), "
            "xolos. Kvalifikatsiya qiluvchi belgilar (zarar miqdori, kompyuter texnikasi vositalaridan foydalanish, "
            "guruh bo‘lib sodir etish) ish holatlariga ko‘ra tekshiriladi. Demak, bu analogiya emas, balki amaldagi "
            "normani uning mazmuni doirasida talqin etish va bevosita qo‘llashdir. Kartasini bergan tanishning "
            "harakatlari ishtirokchilik (yordamchilik) nuqtayi nazaridan, uning qasdi isbotlangan taqdirdagina "
            "baholanadi. Bundan tashqari, direktorning tasviri va ovozidan (biometrik, shaxsga doir ma’lumotlardan) "
            "roziligisiz foydalanilgani «Shaxsga doir ma’lumotlar to‘g‘risida»gi Qonun buzilishini tashkil etadi; SI "
            "yordamida shaxsga doir ma’lumotlarga qonunga xilof ishlov berish uchun 2026-yilda ma’muriy javobgarlik "
            "ham belgilangan.\n\n"
            "**3. Subyekt.** Jinoyat subyekti — aqli raso, javobgarlik yoshiga yetgan jismoniy shaxs, ya’ni "
            "B. Tursunov. Sun’iy intellekt dasturi huquq subyekti emas; u — jinoyat sodir etish vositasi (quroli). "
            "Dastur ishlab chiquvchisi, agar u dasturni aynan jinoyat uchun yaratmagan va jinoyatda ishtirok etmagan "
            "bo‘lsa, javobgar bo‘lmaydi (ayb uchun javobgarlik prinsipi).\n\n"
            "**4. Dalillar.** Video-yozuv va qo‘ng‘iroq ma’lumotlari qonuniy tartibda olinishi; yozuvning haqiqiyligi va "
            "montaj (sintez) belgilari bo‘yicha sud kompyuter-texnik va fonoskopik (video-fonografik) ekspertiza "
            "tayinlanishi; qurilmalar, IP-manzillar, pul oqimi (bank ma’lumotlari) bilan sababiy zanjir tiklanishi "
            "kerak. Dalillar yig‘indisi Jinoyat-protsessual kodeksi talablari asosida ichki ishonch bo‘yicha baholanadi; "
            "aybsizlik prezumpsiyasiga (Konstitutsiyaning 28-moddasi) ko‘ra bartaraf etilmagan shubhalar gumonlanuvchi "
            "foydasiga hal qilinadi."
        ),
        "baholash_mezonlari": [
            "JK 4-modda — analogiya taqiqini to‘g‘ri qo‘llash",
            "Analogiya va normani bevosita qo‘llash (talqin)ni farqlash; firibgarlik tarkibi (JK 168-modda)",
            "SI — jinoyat vositasi, subyekt — jismoniy shaxs",
            "Elektron dalillarni ekspertiza orqali tekshirish, aybsizlik prezumpsiyasi",
        ],
    },
    {
        "id": "avtonom-kuryer",
        "raqam": 2,
        "sarlavha": "«Avtonom kuryer»: robot yetkazgan zarar uchun kim javob beradi?",
        "soha": "Fuqarolik huquqi · Delikt · SI huquqiy maqomi",
        "murakkablik": "O‘rta",
        "fabula": (
            "«TezYetkaz» MChJ sun’iy intellekt texnologiyalari uchun joriy etilgan maxsus rejim ishtirokchisi sifatida "
            "Toshkent shahrining ajratilgan hududida o‘zi yuradigan yetkazib beruvchi robotlarni sinovdan o‘tkazmoqda. "
            "Robotlarning boshqaruv dasturini «NeyroSoft» MChJ ishlab chiqqan; piyodalarni tanish modeli esa uchinchi "
            "kompaniya — «DataMarkaz» MChJ taqdim etgan tasvirlar bazasida o‘qitilgan.\n\n"
            "Kechki payt robot piyodalar yo‘lagida ketayotgan 67 yoshli fuqaro M. Rahimovani «to‘siq emas» deb "
            "noto‘g‘ri aniqlab, uni urib yuboradi. Jabrlanuvchi son suyagi sinishi bilan shifoxonaga yotqiziladi. "
            "Ekspertiza xulosasiga ko‘ra, tanish modeli qorong‘ida va hassa bilan yuruvchi keksa odamlar tasvirlarida "
            "yetarlicha o‘qitilmagan; bundan tashqari, «TezYetkaz» ishlab chiquvchi tavsiya qilgan so‘nggi xavfsizlik "
            "yangilanishini o‘rnatmagan.\n\n"
            "«TezYetkaz» vakili da’voga e’tiroz bildiradi: «Robot qarorni mustaqil qabul qilgan. Xodimlarimizning aybi "
            "yo‘q. Qolaversa, biz maxsus rejim ishtirokchisimiz — bizga umumiy qoidalar tatbiq etilmaydi. Da’vo "
            "robotning o‘ziga yoki dasturchiga qaratilsin»."
        ),
        "savollar": [
            "Robot javobgarlik subyekti bo‘la oladimi? SI huquqiy maqomiga oid qaysi konsepsiya amaldagi huquqqa mos?",
            "M. Rahimova kimga va qaysi norma asosida da’vo qo‘zg‘atishi maqsadga muvofiq? «Aybimiz yo‘q» degan e’tiroz ahamiyatlimi?",
            "«NeyroSoft» va «DataMarkaz»ning javobgarligi qanday hal qilinadi?",
            "Maxsus (eksperimental) rejim ishtirokchisi maqomi zarar uchun javobgarlikdan ozod qiladimi?",
            "Jinoiy javobgarlik masalasi qanday shartlarda tug‘ilishi mumkin?",
        ],
        "namuna_yechim": (
            "**1. Robotning maqomi.** Amaldagi qonunchilikka ko‘ra sun’iy intellekt — huquq obyekti (dasturiy ta’minot "
            "va mol-mulk), subyekt emas. Uning huquq layoqati ham, delikt layoqati ham, mol-mulki ham yo‘q; «elektron "
            "shaxs» (kvazi-subyekt) konsepsiyasi faqat doktrinal taklif. «Da’vo robotga qaratilsin» degan e’tiroz "
            "huquqiy asosga ega emas.\n\n"
            "**2. Asosiy javobgar va norma.** Da’vo robotga egalik qiluvchi va undan foydalanuvchi «TezYetkaz» "
            "MChJga qaratiladi. Jamoat joyida harakatlanuvchi avtonom mexanizm faoliyati atrofdagilar uchun oshiqcha "
            "xavf tug‘diradi, shu bois Fuqarolik kodeksining 999-moddasi qo‘llanadi: oshiqcha xavf manbaiga egalik "
            "qiluvchi zararni **aybidan qat’i nazar** qoplaydi, agar zarar yengib bo‘lmas kuch yoki jabrlanuvchining "
            "qasdi oqibatida kelib chiqqanini isbotlay olmasa. Bunday holatlar mavjud emas. Demak, «xodimlarimizning "
            "aybi yo‘q» degan e’tiroz yuridik ahamiyatga ega emas. Jabrlanuvchi davolanish xarajatlari, yo‘qotilgan "
            "daromad (pensiya yoshidagi shaxs uchun — tegishli qoidalar bo‘yicha) va ma’naviy zarar qoplanishini talab "
            "qilishga haqli (hayot va sog‘liqqa yetkazilgan zararni qoplash qoidalari).\n\n"
            "**3. Ishlab chiquvchi va ma’lumotlar bazasi egasi.** Jabrlanuvchi oldida javobgar — manbaga egalik "
            "qiluvchi. Zararni qoplagach, «TezYetkaz» regress (qaytarma talab) tartibida «NeyroSoft»ga (dasturning "
            "nuqsoni, yetarli sinovdan o‘tkazilmagani) va shartnoma asosida «DataMarkaz»ga (sifatsiz, to‘liq bo‘lmagan "
            "ma’lumotlar to‘plami) talab qo‘yishi mumkin. Bunda sud har birining hissasini aniqlaydi; «TezYetkaz»ning "
            "o‘zi xavfsizlik yangilanishini o‘rnatmagani — uning shaxsiy qo‘pol ehtiyotsizligi bo‘lib, regress "
            "hajmini kamaytiradi. Muqobil ravishda jabrlanuvchi tovar (ish, xizmat) nuqsonlari oqibatida yetkazilgan "
            "zarar qoidalari bo‘yicha bevosita ishlab chiqaruvchiga ham murojaat qilishi mumkin.\n\n"
            "**4. Maxsus rejim.** Prezidentning PQ-4996-son qarori asosida joriy etilgan maxsus rejim («tartibga solish "
            "qumdoni») ishtirokchilarga ruxsat berish tartib-taomillari va ayrim tartibga soluvchi talablar bo‘yicha "
            "yengillik beradi, lekin uchinchi shaxslarning hayoti va sog‘lig‘iga yetkazilgan zarar uchun fuqarolik-huquqiy "
            "javobgarlikni bekor qilmaydi. Aks talqin Konstitutsiyaning inson hayoti va sog‘lig‘ini himoya qilish "
            "kafolatlariga hamda qonun oldida tenglik prinsipiga zid bo‘lar edi.\n\n"
            "**5. Jinoiy javobgarlik.** Robot jinoyat subyekti bo‘la olmaydi. Jinoiy javobgarlik faqat aniq jismoniy "
            "shaxsning (masalan, xavfsizlik yangilanishini o‘rnatish uchun mas’ul xodim yoki rahbarning) aybi — "
            "ehtiyotsizligi — va uning harakatsizligi bilan og‘ir oqibat o‘rtasidagi sababiy bog‘lanish isbotlangan "
            "taqdirdagina yuzaga kelishi mumkin. Yuridik shaxsning o‘zi O‘zbekiston jinoyat huquqi bo‘yicha jinoiy "
            "javobgarlik subyekti emas."
        ),
        "baholash_mezonlari": [
            "SI — huquq obyekti; «elektron shaxs» amaldagi huquqda yo‘q",
            "FK 999-modda — aybsiz javobgarlik, ozod qiluvchi asoslar",
            "Regress va javobgarlikni dasturchi hamda ma’lumotlar bazasi egasi o‘rtasida taqsimlash",
            "Maxsus rejim (PQ-4996) javobgarlikdan ozod qilmasligi; jinoiy javobgarlik faqat aybdor jismoniy shaxsga",
        ],
    },
    {
        "id": "xavf-bali",
        "raqam": 3,
        "sarlavha": "«92 foizlik xavf bali»: algoritm xulosasi va ehtiyot chorasi",
        "soha": "Konstitutsiyaviy huquq · Jinoyat protsessi · Algoritmik adolat",
        "murakkablik": "Yuqori",
        "fabula": (
            "Tuman ichki ishlar bo‘limiga tajriba tariqasida «Prognoz» tahliliy dasturi o‘rnatilgan. Dastur "
            "shaxsning yoshi, yashash joyi, ilgarigi ma’muriy huquqbuzarliklari, ijtimoiy tarmoqlardagi faolligi va "
            "atrofidagi shaxslar haqidagi ma’lumotlar asosida «jinoyat sodir etish xavfi balini» hisoblaydi. Dastur "
            "algoritmi tijorat siri hisoblanadi; uning qanday ishlashini bo‘lim xodimlari ham bilmaydi.\n\n"
            "Do‘kondan qimmatbaho telefon o‘g‘irlangan. Kamera yozuvi sifatsiz, guvohlar yo‘q. Dastur shu mahallada "
            "yashovchi 22 yoshli ishsiz fuqaro J. Qodirovga «92 foiz» xavf balini beradi. Tergovchi A. Salimov "
            "J. Qodirovni ushlab turadi va unga nisbatan qamoqqa olish tarzidagi ehtiyot chorasini qo‘llash to‘g‘risida "
            "iltimosnoma tayyorlaydi. Iltimosnomada yagona asos sifatida «Prognoz» tizimining xulosasi ko‘rsatilgan: "
            "«Tizim xatoga yo‘l qo‘ymaydi; gumonlanuvchi o‘zining aloqasi yo‘qligini isbotlab bera olmadi»."
        ),
        "savollar": [
            "Tergovchining harakatlari Konstitutsiyaning qaysi normalariga zid? Asoslab bering.",
            "Algoritmik «xavf bali» dalil bo‘la oladimi? «Qora quti» muammosi bu yerda qanday namoyon bo‘ladi?",
            "Qamoqqa olish tarzidagi ehtiyot chorasi mutanosiblik prinsipi nuqtayi nazaridan qanday baholanadi?",
            "«Human-in-the-loop» qoidasiga muvofiq tergovchi algoritm xulosasidan qanday foydalanishi kerak edi?",
        ],
        "namuna_yechim": (
            "**1. Aybsizlik prezumpsiyasining buzilishi.** Konstitutsiyaning 28-moddasi va Jinoyat-protsessual "
            "kodeksining 23-moddasiga ko‘ra shaxs aybi sudning qonuniy kuchga kirgan hukmi bilan aniqlanmaguncha "
            "aybsiz hisoblanadi, o‘z aybsizligini isbotlashga majbur emas, bartaraf etilmagan shubhalar esa uning "
            "foydasiga hal qilinadi. «Gumonlanuvchi aloqasi yo‘qligini isbotlab bera olmadi» degan asos isbotlash "
            "yukini qonunga zid ravishda shaxsning o‘ziga ag‘daradi. Bundan tashqari, Konstitutsiyaning 20-moddasiga "
            "ko‘ra qonunchilikdagi ziddiyat va noaniqliklar inson foydasiga talqin etiladi.\n\n"
            "**2. Xavf bali — dalil emas.** Dalil — ish uchun ahamiyatli holatlar to‘g‘risidagi, qonunda belgilangan "
            "manbalardan qonuniy tartibda olingan haqiqiy ma’lumot. Algoritmik ball esa aniq qilmish haqidagi ma’lumot "
            "emas, balki shaxsning ijtimoiy belgilari (yoshi, yashash joyi, ishsizligi) asosidagi statistik "
            "umumlashma. U aloqadorlik, maqbullik va ishonchlilik mezonlariga javob bermaydi. «Qora quti» muammosi: "
            "algoritm yopiq, uning mantig‘ini na tergovchi, na himoya, na sud tekshira oladi — demak, xulosani "
            "tekshirish va unga asosli e’tiroz bildirish (himoyalanish huquqi, tortishuv prinsipi) imkonsiz. Yashash "
            "joyi va ijtimoiy mavqega asoslangan ball yashirin kamsitish xavfini ham tug‘diradi (qonun oldida "
            "tenglik). Dalillar ichki ishonch asosida, ularning yig‘indisini har tomonlama tekshirib baholanadi; "
            "«tizim xatoga yo‘l qo‘ymaydi» degan taxmin bunga ziddir — hech bir dalil oldindan belgilangan kuchga ega "
            "emas.\n\n"
            "**3. Mutanosiblik.** Qamoqqa olish — eng og‘ir ehtiyot chorasi, shaxsiy erkinlikni cheklaydi. "
            "Konstitutsiyaning 20-moddasi (huquqiy ta’sir choralarining mutanosibligi) va 21-moddasi (huquqlarni faqat "
            "qonunga muvofiq va zarur doirada cheklash) talablariga ko‘ra uni qo‘llash uchun qonunda nazarda tutilgan "
            "aniq asoslar va asosli gumon bo‘lishi, yengilroq chora yetarli emasligi ko‘rsatilishi shart. Hech qanday "
            "dalil bilan mustahkamlanmagan algoritmik ball asosidagi iltimosnoma asossiz; sud uni rad etishi lozim. "
            "Ushlab turishning o‘zi ham qonuniy asoslarsiz amalga oshirilgan bo‘lsa, noqonuniy hisoblanadi.\n\n"
            "**4. Human-in-the-loop.** «Axborotlashtirish to‘g‘risida»gi Qonunga 2026-yil 21-yanvardagi O‘RQ-1115-son "
            "Qonun bilan kiritilgan qoidaga ko‘ra, inson huquq va erkinliklariga daxldor yuridik ahamiyatli qarorlarni "
            "qabul qilishda faqat sun’iy intellekt asosidagi tizimlar xulosasiga tayanish mumkin emas. Tergovchi "
            "tizim signalini faqat **tezkor versiya** sifatida qabul qilishi, uni protsessual yo‘llar bilan tekshirishi "
            "(kamera yozuvini ekspertizadan o‘tkazish, telefon IMEI kodi bo‘yicha qidiruv, alibini tekshirish, guvohlarni "
            "aniqlash, tintuv uchun qonuniy asoslar bo‘lsa — tintuv) va qarorni faqat shu yo‘l bilan to‘plangan dalillar "
            "asosida, o‘z nomidan asoslantirib qabul qilishi kerak edi. Yopiq algoritmni davlat organi faoliyatida "
            "auditsiz, shaffoflik va shikoyat mexanizmlarisiz qo‘llashning o‘zi ham shaxsga doir ma’lumotlar "
            "to‘g‘risidagi qonunchilik nuqtayi nazaridan tekshirilishi lozim."
        ),
        "baholash_mezonlari": [
            "Konstitutsiyaning 28-moddasi, JPK 23-modda — isbotlash yuki va shubhalarni talqin qilish",
            "Algoritmik ballning dalil emasligi; «qora quti», himoyalanish huquqi, kamsitish xavfi",
            "Konstitutsiyaning 20–21-moddalari — mutanosiblik va zaruriyat testi",
            "Human-in-the-loop (O‘RQ-1115 qo‘shimchalari): algoritm — versiya manbai, qaror — insonniki",
        ],
    },
    {
        "id": "smart-kontrakt-nizo",
        "raqam": 4,
        "sarlavha": "«Kod shunday yozilgan»: smart-kontrakt va yengib bo‘lmas kuch",
        "soha": "Fuqarolik huquqi · Huquqiy bo‘shliq · Analogiya",
        "murakkablik": "Yuqori",
        "fabula": (
            "«Oltin Don» fermer xo‘jaligi va «AgroEksport» MChJ 200 tonna bug‘doy yetkazib berish bo‘yicha kelishuvni "
            "blokcheyn platformasida smart-kontrakt shaklida rasmiylashtirgan. Kod shartlari: agar ombor datchigi "
            "(orakl) 1-sentabrgacha yuk qabul qilinganini tasdiqlasa — to‘lov fermerga avtomatik o‘tadi; aks holda "
            "fermer kafolat sifatida joylashtirgan 300 million so‘mlik depozit to‘liq xaridorga avtomatik "
            "o‘tkaziladi.\n\n"
            "28-avgust kuni kuchli sel yagona ko‘prikni yuvib ketadi va yo‘l favqulodda vaziyatlar organi qarori bilan "
            "o‘n kunga yopiladi. Fermer bu haqda xaridorni darhol xabardor qiladi va yukni 6-sentabrda yetkazadi. Biroq "
            "1-sentabr yarim tunda smart-kontrakt depozitni avtomatik ravishda «AgroEksport» hisobiga o‘tkazib "
            "yuboradi.\n\n"
            "Fermer depozitni qaytarishni so‘raydi. «AgroEksport» rad etadi: «Kod — bu qonun. Taraflar aynan shunday "
            "algoritmga rozi bo‘lgan. Qonunchilikda smart-kontraktlar haqida maxsus norma yo‘q, demak, sud bu nizoni "
            "ko‘rishga haqli emas va kod natijasini o‘zgartira olmaydi»."
        ),
        "savollar": [
            "«Kod — bu qonun» degan vaj huquqiy jihatdan asoslimi? Smart-kontraktning huquqiy tabiatini tushuntiring.",
            "Maxsus norma yo‘qligi sudning nizoni ko‘rishiga to‘sqinlik qiladimi? Bo‘shliq qanday yengib o‘tiladi?",
            "Fermer depozitni qaytarib olishga haqlimi? Qaysi normalar asosida?",
            "Smart-kontrakt kodini huquq normasi tuzilishi (gipoteza — dispozitsiya — sanksiya) nuqtayi nazaridan tahlil qiling: kodda nima yetishmaydi?",
        ],
        "namuna_yechim": (
            "**1. «Code is Law» vaji.** Asossiz. L. Lessigning tezisi kodning xulq-atvorni amalda tartibga solishini "
            "tavsiflaydi, lekin kodga yuridik kuch bermaydi. Konstitutsiyaning 15-moddasiga ko‘ra Konstitutsiya va "
            "qonunlarning ustunligi so‘zsiz tan olinadi. Smart-kontrakt — taraflar o‘rtasidagi shartnomaning elektron "
            "shakli va (asosan) majburiyatni ijro etish usuli; unga Fuqarolik kodeksining bitimlar va shartnomalar "
            "haqidagi umumiy qoidalari to‘liq tatbiq etiladi. Shartnoma erkinligi (FK 354-modda) qonunning imperativ "
            "normalari doirasida amal qiladi.\n\n"
            "**2. Bo‘shliq va analogiya.** Smart-kontraktlarga oid maxsus normaning yo‘qligi — huquqiy bo‘shliq, biroq "
            "u sudga murojaat qilish huquqini cheklamaydi: har kimga o‘z huquqlarini sud orqali himoya qilish "
            "kafolatlangan. Fuqarolik kodeksining 5-moddasiga ko‘ra, munosabat qonunchilik yoki kelishuv bilan bevosita "
            "tartibga solinmagan bo‘lsa, o‘xshash munosabatlarni tartibga soluvchi norma qo‘llanadi (**qonun "
            "analogiyasi**) — bu yerda mahsulot yetkazib berish (oldi-sotdi), neustoyka va garov/kafolat depoziti "
            "haqidagi qoidalar; bunday norma ham bo‘lmasa — fuqarolik qonunchiligining umumiy asoslari, vijdonlilik, "
            "oqilonalik va adolat talablari (**huquq analogiyasi**). Jinoyat huquqidan farqli o‘laroq, fuqarolik "
            "huquqida analogiya ruxsat etilgan. Aslida ko‘p masalalar bo‘yicha analogiyaga ham hojat yo‘q — umumiy "
            "normalar bevosita qo‘llanadi.\n\n"
            "**3. Mazmunan hal etish.** Depozitning avtomatik o‘tkazilishi mohiyatan majburiyatni buzganlik uchun "
            "javobgarlik chorasi (neustoyka)dir. Fuqarolik kodeksining 333-moddasiga ko‘ra qarzdor majburiyatni "
            "bajarmagani yoki lozim darajada bajarmagani uchun aybi bo‘lgan taqdirda javob beradi; majburiyatni "
            "yengib bo‘lmas kuch (favqulodda va muayyan sharoitda oldini olib bo‘lmaydigan holatlar) tufayli bajara "
            "olmaganini isbotlagan shaxs javobgarlikdan ozod etiladi. Sel va yo‘lning vakolatli organ qarori bilan "
            "yopilishi — hujjat bilan tasdiqlangan yengib bo‘lmas kuch; fermer xaridorni darhol xabardor qilgan va "
            "to‘siq bartaraf etilgach majburiyatni bajargan. Demak, sanksiya qo‘llash uchun huquqiy asos bo‘lmagan; "
            "«AgroEksport» olgan 300 million so‘m — asossiz orttirilgan boylik sifatida qaytarilishi lozim (asossiz "
            "boyish qoidalari). Blokcheyndagi yozuvni «orqaga qaytarish» texnik jihatdan imkonsiz bo‘lsa ham, sud "
            "javobgardan pul summasini undirish to‘g‘risida qaror chiqaradi — huquq kod natijasini teskari "
            "tranzaksiya yoki pul undirish orqali tuzatadi. Agar neustoyka qo‘llanishi mumkin bo‘lgan taqdirda ham, "
            "sud uni majburiyat buzilishi oqibatlariga nomutanosib bo‘lsa, kamaytirishga haqli.\n\n"
            "**4. Norma tuzilishi tahlili.** Kod uch elementni aks ettirgan: gipoteza (`IF` — «orakl 1-sentabrgacha "
            "qabulni tasdiqlasa»), dispozitsiya (`THEN` — «to‘lov fermerga o‘tadi»), sanksiya (`ELSE` — «depozit "
            "xaridorga o‘tadi»). Ammo huquq normasidan farqli ravishda kodda **javobgarlikdan ozod qiluvchi holatlar** "
            "(yengib bo‘lmas kuch, kreditorning aybi), baholovchi mezonlar va nizoni hal etish tartibi ko‘zda "
            "tutilmagan; sanksiya aybni tekshirmasdan, himoyalanish imkoniyatisiz avtomatik ijro etilgan. Amaliy "
            "xulosa: smart-kontraktga fors-major holatida ijroni to‘xtatib turuvchi shart, nizoli vaziyat uchun inson "
            "ishtirokidagi mexanizm (arbitr/multisig) kiritilishi va u matnli shartnoma bilan birga tuzilishi "
            "maqsadga muvofiq (*Human-in-the-loop* qoidasining xususiy huquqdagi ko‘rinishi)."
        ),
        "baholash_mezonlari": [
            "Qonun ustunligi (Konstitutsiyaning 15-moddasi); smart-kontrakt — shartnoma shakli/ijro usuli",
            "FK 5-modda — qonun va huquq analogiyasi; sud himoyasi huquqi",
            "FK 333-modda — ayb va yengib bo‘lmas kuch; asossiz orttirilgan boylikni qaytarish",
            "Gipoteza–dispozitsiya–sanksiya tahlili va kodning cheklovlari",
        ],
    },
]


def get_case(case_id: str) -> dict:
    """Identifikator bo‘yicha kazusni qaytaradi."""
    for case in CASES:
        if case["id"] == case_id:
            return case
    return CASES[0]


def case_public_text(case: dict) -> str:
    """Kazusning foydalanuvchiga ko‘rinadigan qismi (namuna yechimsiz) — AI konteksti uchun."""
    questions = "\n".join(f"{i}. {q}" for i, q in enumerate(case["savollar"], start=1))
    return f"Kazus: {case['sarlavha']}\nSoha: {case['soha']}\n\nFabula:\n{case['fabula']}\n\nSavollar:\n{questions}"
