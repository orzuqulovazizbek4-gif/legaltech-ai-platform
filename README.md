# LegalTech & AI Huquqiy Bilimlar Platformasi

**Mavzu:** «Raqamli transformatsiya va sun’iy intellekt davrida huquq ijodkorligi va huquqiy tartibga solish masalalari»

Huquqshunos talabalar, kursantlar, tergovchilar va huquqshunos olimlar uchun interaktiv o‘quv platformasi.
Butun interfeys va kontent — adabiy o‘zbek tilida (lotin yozuvi).

> O‘zbekiston Respublikasi Huquqni muhofaza qilish akademiyasi «Tergov faoliyati» yo‘nalishi 1-bosqich tinglovchisi
> Orzuqulov Azizbek Xabibovich tomonidan «Davlat va huquq nazariyasi» fani mustaqil ishi doirasida ishlab chiqilgan
> (Toshkent — 2026).

## Modullar

| Modul | Mazmuni |
|---|---|
| 📚 Tahliliy maqolalar | 4 ta to‘liq ilmiy maqola; har bir bo‘lim ostida «AI orqali sodda tushuntir» tugmasi |
| 🗺️ Qonunchilik xaritasi | 9 ta normativ-huquqiy hujjat, saralash va qidiruv, lex.uz havolalari |
| 📖 Interaktiv glossariy | 16 ta atama: ta’rif, hayotiy misol, normativ manba |
| 🕵️ AI-Tergovchi | 4 ta kazus; yechimingizni Gemini 100 ballik tizimda baholaydi |
| ✅ Bilim testi | 10 ta savol, natija foizi va batafsil huquqiy izohlar |
| 🤖 AI Huquqshunos Yordamchi | Sahifa mazmunini biladigan doimiy panel, 3 xil tushuntirish uslubi |

## Ishga tushirish (macOS)

**Eng oson yo‘l:** Finder’da `Ishga_tushirish.command` faylini ikki marta bosing. Skript virtual muhitni yaratadi,
kutubxonalarni o‘rnatadi va ilovani `http://localhost:8501` manzilida ochadi.

**Qo‘lda:**

```bash
cd ~/Desktop/LegalTech_AI_Platform
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Gemini API kaliti

1. <https://aistudio.google.com/apikey> sahifasida bepul kalit yarating.
2. Kalitni ikki usuldan biri bilan kiriting:
   - **Brauzerda:** ilovaning chap panelidagi «Gemini API kaliti» maydoniga joylashtiring (faqat joriy sessiyada saqlanadi);
   - **Faylda:** `.env.example` dan nusxa olib `.env` deb nomlang va `GEMINI_API_KEY=...` satrini to‘ldiring.

Kalitsiz ham barcha materiallar, namuna yechimlar va test ishlaydi; faqat AI yordamchi va kazus tekshiruvi kalit talab qiladi.

Standart model — `gemini-2.5-flash`. Agar u Google tomonidan o‘chirilgan bo‘lsa, ilova avtomatik ravishda zaxira
modelga (`gemini-3.5-flash`, `gemini-flash-latest`) o‘tadi; `.env` faylida `GEMINI_MODEL` orqali o‘zgartirish mumkin.

## Loyiha tuzilishi

```
LegalTech_AI_Platform/
├── app.py                  # Asosiy Streamlit ilovasi (navigatsiya + AI yordamchi paneli)
├── assets/style.css        # Dizayn: to‘q ko‘k, oltin, oq kartalar
├── data/
│   ├── articles.py         # 4 ta tahliliy maqola
│   ├── legislation.py      # Qonunchilik xaritasi
│   ├── glossary.py         # 16 ta atama
│   ├── cases.py            # 4 ta kazus va namuna yechimlar
│   └── quiz.py             # 10 ta test savoli
├── utils/ai_engine.py      # Google Gemini integratsiyasi (google-genai)
├── .streamlit/config.toml  # Port va mavzu sozlamalari
├── Ishga_tushirish.command # macOS uchun ishga tushirish skripti
├── requirements.txt
├── .env.example
└── README.md
```

## Muhim eslatma

Platforma o‘quv-ilmiy maqsadda yaratilgan. Qonun normalari qisqacha bayon qilingan (2026-yil noyabr holatiga ko‘ra);
aniq iqtibos va amaldagi tahrir uchun [lex.uz](https://lex.uz) saytidagi rasmiy matnga tayaning. AI javoblari rasmiy
yuridik maslahat emas va ularni rasmiy manba bilan solishtirish lozim.

## Ommaviy joylashtirish (Streamlit Community Cloud)

1. Loyihani GitHub omboriga yuklang (`.env` va `venv/` yuklanmaydi — `.gitignore` da ko‘rsatilgan).
2. <https://share.streamlit.io> saytida GitHub orqali kiring → **Create app** → omborni va `app.py` faylini tanlang.
3. **Advanced settings → Secrets** maydoniga yozing: `GEMINI_API_KEY = "kalitingiz"` va **Deploy** tugmasini bosing.

Serverda kalit mavjud bo‘lsa, ilova ommaviy rejimga o‘tadi: kalit maydoni yashiriladi, barcha tashrif buyuruvchilar
AI yordamchidan umumiy kalit orqali foydalanadi. Kvotani himoya qilish uchun har bir tashrifga AI so‘rovlari chegarasi
qo‘yilgan (standart 30 ta; `AI_SESSION_LIMIT` orqali o‘zgartiriladi). Kalitni hech qachon kod yoki GitHub’ga yozmang.
