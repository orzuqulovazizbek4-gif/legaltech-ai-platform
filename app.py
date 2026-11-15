"""LegalTech & AI Huquqiy Bilimlar Platformasi — asosiy Streamlit ilovasi.

Ishga tushirish:  streamlit run app.py
"""

from __future__ import annotations

import html
import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

from data.articles import ARTICLES, article_full_text, get_article
from data.cases import CASES, case_public_text, get_case
from data.glossary import GLOSSARY, GLOSSARY_CATEGORIES, glossary_summary_text, term_text
from data.legislation import LEGISLATION, LEGISLATION_TYPES, legislation_summary_text
from data.quiz import QUIZ
from utils.ai_engine import (
    MODES,
    QUICK_PROMPTS,
    ask_tutor,
    evaluate_case,
    extract_score,
    resolve_api_key,
)

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

PLATFORM_NAME = "LegalTech & AI Huquqiy Bilimlar Platformasi"
PLATFORM_TOPIC = (
    "Raqamli transformatsiya va sun’iy intellekt davrida huquq ijodkorligi va huquqiy tartibga solish masalalari"
)
AUTHOR_CREDIT = (
    "O‘zbekiston Respublikasi Huquqni muhofaza qilish akademiyasi «Tergov faoliyati» yo‘nalishi 1-bosqich "
    "tinglovchisi Orzuqulov Azizbek Xabibovich tomonidan «Davlat va huquq nazariyasi» fani mustaqil ishi "
    "doirasida ishlab chiqilgan (Toshkent — 2026)."
)

PAGES = [
    "🏛️ Bosh sahifa",
    "📚 Tahliliy maqolalar",
    "🗺️ Qonunchilik xaritasi",
    "📖 Interaktiv glossariy",
    "🕵️ AI-Tergovchi: kazus trenajyori",
    "✅ Bilimni tekshirish testi",
    "ℹ️ Loyiha haqida",
]
PAGE_HOME, PAGE_ARTICLES, PAGE_LAWS, PAGE_GLOSSARY, PAGE_CASES, PAGE_QUIZ, PAGE_ABOUT = PAGES

NO_KEY_MESSAGE = (
    "🔑 **AI yordamchi hali ulanmagan.** Javob olishim uchun Gemini API kaliti kerak.\n\n"
    "1. [aistudio.google.com/apikey](https://aistudio.google.com/apikey) sahifasida bepul kalit yarating.\n"
    "2. Kalitni chap paneldagi **«Gemini API kaliti»** maydoniga joylashtiring va Enter tugmasini bosing.\n\n"
    "Shundan so‘ng savolingizni qayta yuboring — men shu sahifadagi matn asosida javob beraman."
)

st.set_page_config(
    page_title=PLATFORM_NAME,
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# --------------------------------------------------------------------------- yordamchi funksiyalar
def load_css() -> None:
    css_path = BASE_DIR / "assets" / "style.css"
    if css_path.exists():
        st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)


def esc(text: str) -> str:
    return html.escape(str(text), quote=False)


def paragraphs_html(text: str) -> str:
    return "".join(f"<p>{esc(part)}</p>" for part in text.split("\n\n") if part.strip())


def badges_html(items: list[str], css_class: str = "") -> str:
    return "".join(f'<span class="badge {css_class}">{esc(item)}</span>' for item in items)


def page_head(eyebrow: str, title: str, lead: str) -> None:
    st.markdown(
        f'<div class="page-head"><div class="eyebrow">{esc(eyebrow)}</div><h2>{esc(title)}</h2>'
        f'<p>{esc(lead)}</p><div class="gold-rule"></div></div>',
        unsafe_allow_html=True,
    )


def init_state() -> None:
    defaults = {
        "page": PAGE_HOME,
        "chat": [],
        "mode": "oddiy",
        "ctx": {},
        "case_results": {},
        "quiz_done": False,
        "active_term": None,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def server_api_key() -> str:
    """Serverda saqlangan kalit: Streamlit secrets yoki .env / muhit o‘zgaruvchisi (ommaviy rejim uchun)."""
    try:
        secret = st.secrets.get("GEMINI_API_KEY", "")
    except Exception:
        secret = ""
    return (str(secret).strip() if secret else "") or resolve_api_key(None)


def ai_limit() -> int:
    """Bitta tashrif (sessiya) uchun AI so‘rovlari chegarasi — umumiy kalit kvotasini himoya qiladi."""
    try:
        return max(1, int(os.getenv("AI_SESSION_LIMIT", "30")))
    except ValueError:
        return 30


def ai_allowed() -> bool:
    return st.session_state.get("ai_calls", 0) < ai_limit()


def count_ai_call() -> None:
    st.session_state["ai_calls"] = st.session_state.get("ai_calls", 0) + 1


LIMIT_MESSAGE = (
    "⏳ Ushbu tashrif uchun AI so‘rovlari chegarasiga yetdingiz. Platformadagi barcha materiallar, namuna "
    "yechimlar va test ochiq qoladi; AI yordamchidan yana foydalanish uchun sahifani keyinroq qayta oching."
)


def set_context(kind: str, title: str, text: str) -> None:
    """AI yordamchi uchun joriy sahifa kontekstini belgilaydi (yashirin tizim konteksti)."""
    st.session_state["ctx"] = {"tur": kind, "sarlavha": title, "matn": text}


def queue_prompt(text: str, focus: str | None = None, mode: str | None = None) -> None:
    """Bir bosishda AI yordamchiga savol yuborish navbatiga qo‘yadi."""
    st.session_state["pending"] = {"text": text, "focus": focus, "mode": mode}


def go_to(page: str) -> None:
    st.session_state["page"] = page


def reset_quiz() -> None:
    st.session_state["quiz_done"] = False
    for index in range(len(QUIZ)):
        st.session_state.pop(f"quiz_q{index}", None)


def clear_chat() -> None:
    st.session_state["chat"] = []


# --------------------------------------------------------------------------- yon panel
def render_sidebar() -> str:
    with st.sidebar:
        st.markdown(
            '<div class="brand"><div class="brand-mark">⚖️</div>'
            '<div class="brand-title">LegalTech &amp; AI<br>Huquqiy Bilimlar Platformasi</div>'
            f'<div class="brand-sub">{esc(PLATFORM_TOPIC)}</div></div>',
            unsafe_allow_html=True,
        )
        st.divider()
        st.markdown('<div class="side-label">Bo‘limlar</div>', unsafe_allow_html=True)
        st.radio("Bo‘limlar", PAGES, key="page", label_visibility="collapsed")

        st.divider()
        st.markdown('<div class="side-label">AI sozlamalari</div>', unsafe_allow_html=True)
        shared_key = server_api_key()
        if shared_key:
            # Ommaviy rejim: kalit serverda saqlanadi, foydalanuvchidan so‘ralmaydi va ko‘rsatilmaydi.
            api_key = shared_key
            used = st.session_state.get("ai_calls", 0)
            st.markdown(
                '<div class="key-ok">✅ AI yordamchi faol. Ushbu tashrifda foydalanilgan so‘rovlar: '
                f"{used} / {ai_limit()}.</div>",
                unsafe_allow_html=True,
            )
        else:
            user_key = st.text_input(
                "Gemini API kaliti",
                type="password",
                key="api_key_input",
                placeholder="Kalitni shu yerga joylashtiring",
                help=(
                    "Kalit faqat joriy brauzer sessiyasida saqlanadi va hech qayerga yozib qo‘yilmaydi. "
                    "Bepul kalitni aistudio.google.com/apikey sahifasidan olishingiz mumkin."
                ),
            )
            api_key = resolve_api_key(user_key)
            if api_key:
                st.markdown(
                    '<div class="key-ok">✅ AI yordamchi faol — kalit brauzerda kiritilgan.</div>',
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    '<div class="key-missing">🔑 Kalit kiritilmagan. Platformadagi barcha materiallar ochiq; '
                    "AI yordamchi va kazus tekshiruvi uchun kalitni yuqoridagi maydonga kiriting.</div>",
                    unsafe_allow_html=True,
                )
        st.divider()
        st.markdown(f'<div class="side-footer"><b>Muallif.</b> {esc(AUTHOR_CREDIT)}</div>', unsafe_allow_html=True)
    return api_key


# --------------------------------------------------------------------------- sahifalar
def page_home() -> None:
    st.markdown(
        '<div class="hero"><div class="hero-eyebrow">Davlat va huquq nazariyasi · Mustaqil ish · 2026</div>'
        f"<h1>{esc(PLATFORM_NAME)}</h1><p>{esc(PLATFORM_TOPIC)}. Tahliliy maqolalar, normativ-huquqiy asos, "
        "atamalar lug‘ati, amaliy kazuslar va bilimni tekshirish testi — barchasi sahifa mazmunini biladigan "
        "AI Huquqshunos Yordamchi bilan birga.</p></div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="stat-row">'
        f'<div class="stat"><div class="num">{len(ARTICLES)}</div><div class="lbl">tahliliy maqola</div></div>'
        f'<div class="stat"><div class="num">{len(LEGISLATION)}</div><div class="lbl">normativ-huquqiy hujjat</div></div>'
        f'<div class="stat"><div class="num">{len(GLOSSARY)}</div><div class="lbl">huquqiy va LegalTech atamasi</div></div>'
        f'<div class="stat"><div class="num">{len(CASES)}</div><div class="lbl">amaliy kazus</div></div>'
        f'<div class="stat"><div class="num">{len(QUIZ)}</div><div class="lbl">test savoli</div></div>'
        "</div>",
        unsafe_allow_html=True,
    )

    modules = [
        ("📚", "Tahliliy maqolalar", PAGE_ARTICLES,
         "Huquq ijodkorligi evolyutsiyasi, «Code is Law», sun’iy intellektning huquqiy maqomi hamda huquqiy "
         "bo‘shliqlar va algoritmik adolat haqida to‘rtta to‘liq ilmiy maqola. Har bir bo‘limni bir bosishda "
         "AI yordamida sodda tilda tushuntirib olish mumkin."),
        ("🗺️", "Qonunchilik xaritasi", PAGE_LAWS,
         "Konstitutsiya, kodekslar, qonunlar, Prezident farmoni va qarorlari: rasmiy nomi, raqami, sanasi, "
         "asosiy moddalari, mavzu uchun ahamiyati va lex.uz saytidagi rasmiy matnga havola."),
        ("📖", "Interaktiv glossariy", PAGE_GLOSSARY,
         "LegalTech, smart-kontrakt, kolliziya, probel, analogiya, «qora quti», Human-in-the-loop kabi 16 ta "
         "tayanch atama: ta’rif, hayotiy misol va normativ manba bilan."),
        ("🕵️", "AI-Tergovchi: kazus trenajyori", PAGE_CASES,
         "To‘rtta amaliy vaziyat. O‘z huquqiy yechimingizni yozing — AI Tergovchi-Ekspert uni namuna yechim bilan "
         "solishtirib, 100 ballik tizimda baholaydi va kamchiliklarni ko‘rsatadi."),
        ("✅", "Bilimni tekshirish testi", PAGE_QUIZ,
         "Maqolalar, qonunlar va tushunchalar bo‘yicha 10 ta savol. Natija, foiz ko‘rsatkichi va har bir savolga "
         "batafsil huquqiy izoh darhol ko‘rsatiladi."),
        ("ℹ️", "Loyiha haqida", PAGE_ABOUT,
         "Platformaning maqsadi, tuzilishi, muallif haqida ma’lumot hamda materiallardan foydalanish bo‘yicha "
         "muhim eslatmalar."),
    ]
    columns = st.columns(2, gap="medium")
    for index, (icon, title, target, description) in enumerate(modules):
        with columns[index % 2]:
            st.markdown(
                f'<div class="card card-accent"><div class="module-icon">{icon}</div>'
                f'<div class="card-title">{esc(title)}</div><p>{esc(description)}</p></div>',
                unsafe_allow_html=True,
            )
            st.button("Bo‘limga o‘tish →", key=f"home_go_{index}", on_click=go_to, args=(target,))

    st.markdown(
        '<div class="card card-navy"><div class="card-title">AI Huquqshunos Yordamchidan qanday foydalaniladi?</div>'
        "<p><b>1.</b> Chap paneldagi «Gemini API kaliti» maydoniga kalitingizni kiriting.<br>"
        "<b>2.</b> Istalgan bo‘limni oching — yordamchi siz o‘qiyotgan matnni avtomatik ravishda «ko‘radi».<br>"
        "<b>3.</b> Tushuntirish uslubini tanlang: oddiy tilda, akademik tilda yoki qonun moddalari bilan.<br>"
        "<b>4.</b> «Buni tushunmadim» deb yozing yoki bo‘lim ostidagi tugmani bosing — javob o‘ng panelda chiqadi.</p></div>",
        unsafe_allow_html=True,
    )
    set_context(
        "Bosh sahifa",
        PLATFORM_NAME,
        f"Platforma mavzusi: {PLATFORM_TOPIC}. Bo‘limlar: tahliliy maqolalar "
        f"({'; '.join(a['sarlavha'] for a in ARTICLES)}), qonunchilik xaritasi, glossariy, kazus trenajyori, test.\n\n"
        + glossary_summary_text(),
    )


def page_articles() -> None:
    page_head(
        "1-modul", "Tahliliy maqolalar",
        "To‘liq ilmiy maqolalar. Har bir bo‘lim ostidagi tugma shu bo‘limni AI yordamchiga yuboradi va sodda "
        "tushuntirishni o‘ng panelda ko‘rsatadi.",
    )
    article_ids = [a["id"] for a in ARTICLES]
    selected_id = st.selectbox(
        "Maqolani tanlang",
        article_ids,
        format_func=lambda item_id: f"{get_article(item_id)['raqam']}. {get_article(item_id)['sarlavha']}",
        key="article_id",
    )
    article = get_article(selected_id)
    set_context("Tahliliy maqola", article["sarlavha"], article_full_text(article))

    st.markdown(
        f'<div class="hero" style="padding:1.5rem 1.8rem"><div class="hero-eyebrow">{article["raqam"]}-maqola · '
        f'taxminan {article["oqish_vaqti"]} daqiqa</div><h1 style="font-size:1.5rem">{esc(article["sarlavha"])}</h1></div>',
        unsafe_allow_html=True,
    )
    st.markdown(f'<div class="annotation">{esc(article["annotatsiya"])}</div>', unsafe_allow_html=True)
    st.markdown(
        '<div style="margin-bottom:.4rem"><span class="badge badge-solid">Kalit so‘zlar</span>'
        + badges_html(article["kalit_sozlar"], "badge-gold") + "</div>",
        unsafe_allow_html=True,
    )

    for index, section in enumerate(article["bolimlar"]):
        st.markdown(f'<div class="section-title">{esc(section["sarlavha"])}</div>', unsafe_allow_html=True)
        st.markdown(section["matn"])
        if st.button("🤖 Shu bo‘limni AI orqali sodda tushuntir", key=f"explain_{article['id']}_{index}"):
            queue_prompt(
                f"«{section['sarlavha']}» bo‘limini sodda tilda, hayotiy misol bilan tushuntirib bering.",
                focus=f"{section['sarlavha']}\n\n{section['matn']}",
                mode="oddiy",
            )

    takeaways = "".join(f"<li>{esc(item)}</li>" for item in article["xulosalar"])
    st.markdown(
        f'<div class="takeaways"><div class="card-title">Asosiy xulosalar</div><ul>{takeaways}</ul></div>',
        unsafe_allow_html=True,
    )


def page_legislation() -> None:
    page_head(
        "2-modul", "Qonunchilik xaritasi",
        "Mavzuning normativ-huquqiy asosi. Hujjat turi yoki kalit so‘z bo‘yicha saralang; har bir kartada "
        "lex.uz saytidagi rasmiy matnga havola bor.",
    )
    filter_col, search_col = st.columns([1.3, 1], gap="medium")
    with filter_col:
        chosen_types = st.multiselect(
            "Hujjat turi", LEGISLATION_TYPES, default=[], placeholder="Barcha turlar", key="law_types"
        )
    with search_col:
        query = st.text_input("Qidiruv", placeholder="Masalan: analogiya, 28-modda, PQ-358", key="law_query")

    needle = (query or "").strip().lower()
    results = []
    for act in LEGISLATION:
        if chosen_types and act["turi"] not in chosen_types:
            continue
        haystack = " ".join(
            [act["nomi"], act["raqami"], act["sana"], act["ahamiyati"], " ".join(act["teglar"])]
            + [f"{item['modda']} {item['mazmun']}" for item in act["moddalar"]]
        ).lower()
        if needle and needle not in haystack:
            continue
        results.append(act)

    st.caption(f"Topildi: {len(results)} ta hujjat (jami {len(LEGISLATION)} ta)")
    if not results:
        st.info("So‘rov bo‘yicha hujjat topilmadi. Filtrni o‘zgartirib ko‘ring.")

    for act in results:
        articles_html = "".join(
            f'<div class="law-article"><b>{esc(item["modda"])}.</b> {esc(item["mazmun"])}</div>'
            for item in act["moddalar"]
        )
        st.markdown(
            '<div class="card card-accent">'
            f'<div class="law-head"><div class="card-title">{esc(act["nomi"])}</div>'
            f'<span class="badge badge-solid">{esc(act["turi"])}</span></div>'
            f'<div class="law-meta"><b>Hujjat raqami:</b> {esc(act["raqami"])} &nbsp;·&nbsp; '
            f'<b>Qabul qilingan sana:</b> {esc(act["sana"])}</div>'
            f"{articles_html}"
            f'<p><b>Huquqiy ahamiyati.</b> {esc(act["ahamiyati"])}</p>'
            f'<div>{badges_html(act["teglar"], "badge-navy")}</div>'
            f'<a class="law-link" href="{act["havola"]}" target="_blank" rel="noopener">'
            "🔗 Rasmiy matn — lex.uz</a></div>",
            unsafe_allow_html=True,
        )
    st.markdown(
        '<p class="muted">Eslatma: kartalardagi bayon — normalarning qisqacha mazmuni. Aniq iqtibos va amaldagi '
        "tahrir uchun har doim lex.uz saytidagi rasmiy matnga tayaning.</p>",
        unsafe_allow_html=True,
    )
    set_context("Qonunchilik xaritasi", "Mavzuning normativ-huquqiy asosi", legislation_summary_text())


def page_glossary() -> None:
    page_head(
        "3-modul", "Interaktiv glossariy",
        "16 ta tayanch atama. Qidiruvdan foydalaning; atama ostidagi tugma AI yordamchidan shu tushunchaga "
        "hayotiy misol so‘raydi.",
    )
    search_col, category_col = st.columns([1.2, 1], gap="medium")
    with search_col:
        query = st.text_input("Atamani qidirish", placeholder="Masalan: analogiya, deepfake, qumdon", key="term_query")
    with category_col:
        category = st.selectbox("Toifa", ["Barcha toifalar", *GLOSSARY_CATEGORIES], key="term_category")

    needle = (query or "").strip().lower()
    results = [
        item for item in GLOSSARY
        if (category == "Barcha toifalar" or item["toifa"] == category)
        and (not needle or needle in f"{item['atama']} {item['tarif']} {item['misol']}".lower())
    ]
    st.caption(f"Topildi: {len(results)} ta atama (jami {len(GLOSSARY)} ta)")
    if not results:
        st.info("So‘rov bo‘yicha atama topilmadi. Boshqa so‘z bilan qidirib ko‘ring.")

    clicked = None
    columns = st.columns(2, gap="medium")
    for index, item in enumerate(results):
        with columns[index % 2]:
            st.markdown(
                '<div class="card term-card card-accent">'
                f'<span class="badge badge-navy">{esc(item["toifa"])}</span>'
                f'<div class="card-title">{esc(item["atama"])}</div>'
                f'<p>{esc(item["tarif"])}</p>'
                f'<div class="term-example"><b>Misol.</b> {esc(item["misol"])}</div>'
                f'<div class="term-source">📜 {esc(item["manba"])}</div></div>',
                unsafe_allow_html=True,
            )
            if st.button("💡 Hayotiy misol so‘rash", key=f"term_{item['id']}"):
                clicked = item

    if clicked is not None:
        st.session_state["active_term"] = clicked["id"]
        queue_prompt(
            f"«{clicked['atama']}» tushunchasini yangi, hayotiy misol bilan sodda tilda tushuntirib bering.",
            focus=term_text(clicked),
            mode="oddiy",
        )

    active = next((item for item in GLOSSARY if item["id"] == st.session_state.get("active_term")), None)
    if active is not None:
        set_context("Glossariy atamasi", active["atama"], term_text(active) + "\n\nBoshqa atamalar:\n" + glossary_summary_text())
    else:
        set_context("Glossariy", "Huquqiy va LegalTech atamalari", glossary_summary_text())


def page_cases(api_key: str) -> None:
    page_head(
        "4-modul", "AI-Tergovchi: kazus trenajyori",
        "Vaziyatni o‘qing, savollarga yozma huquqiy yechim bering va tekshiruvga yuboring. AI Tergovchi-Ekspert "
        "javobingizni namuna yechim bilan solishtirib baholaydi.",
    )
    case_ids = [c["id"] for c in CASES]
    selected_id = st.selectbox(
        "Kazusni tanlang",
        case_ids,
        format_func=lambda item_id: f"{get_case(item_id)['raqam']}-kazus. {get_case(item_id)['sarlavha']}",
        key="case_id",
    )
    case = get_case(selected_id)
    set_context("Kazus (amaliy vaziyat)", case["sarlavha"], case_public_text(case))

    st.markdown(
        f'<div><span class="badge badge-solid">{case["raqam"]}-kazus</span>'
        f'<span class="badge badge-navy">{esc(case["soha"])}</span>'
        f'<span class="badge badge-gold">Murakkablik: {esc(case["murakkablik"])}</span></div>',
        unsafe_allow_html=True,
    )
    st.markdown(f"### {case['sarlavha']}")
    st.markdown(f'<div class="fabula">{paragraphs_html(case["fabula"])}</div>', unsafe_allow_html=True)

    st.markdown("**Hal etilishi lozim bo‘lgan savollar:**")
    st.markdown("\n".join(f"{i}. {q}" for i, q in enumerate(case["savollar"], start=1)))

    answer = st.text_area(
        "Sizning huquqiy yechimingiz",
        key=f"answer_{case['id']}",
        height=260,
        placeholder=(
            "Har bir savolga asoslangan javob yozing: qo‘llaniladigan qonun va moddalarni ko‘rsating, nazariy "
            "asoslang va aniq xulosa bering…"
        ),
    )
    st.caption(f"Javob hajmi: {len(answer or '')} ta belgi. Tavsiya etiladi: kamida 400 ta belgi.")

    if st.button("🕵️ AI Tergovchi-Ekspert tekshiruvi", type="primary", key=f"check_{case['id']}"):
        if not api_key:
            st.warning(
                "Tekshiruv uchun Gemini API kaliti kerak. Kalitni chap paneldagi «Gemini API kaliti» maydoniga "
                "kiriting — javobingiz saqlanib turadi. Hozircha quyidagi namuna yechim bilan o‘zingiz "
                "solishtirishingiz mumkin."
            )
        elif not ai_allowed():
            st.warning(LIMIT_MESSAGE)
        elif len((answer or "").strip()) < 80:
            st.warning("Javob juda qisqa. Baholash mazmunli bo‘lishi uchun kamida bir necha jumla yozing.")
        else:
            with st.spinner("AI Tergovchi-Ekspert javobingizni tahlil qilmoqda…"):
                evaluation, error = evaluate_case(api_key, case, answer.strip())
            count_ai_call()
            if error:
                st.error(error)
            else:
                st.session_state["case_results"][case["id"]] = evaluation

    evaluation = st.session_state["case_results"].get(case["id"])
    if evaluation:
        score = extract_score(evaluation)
        if score is not None:
            if score >= 85:
                verdict = "A’lo daraja: yechim huquqiy jihatdan puxta asoslangan."
            elif score >= 70:
                verdict = "Yaxshi daraja: asosiy normalar to‘g‘ri qo‘llangan, ayrim nuanslar yetishmaydi."
            elif score >= 50:
                verdict = "Qoniqarli daraja: yechimni normativ va nazariy jihatdan chuqurlashtirish kerak."
            else:
                verdict = "Yechim qayta ishlashni talab qiladi: namuna yechim va maqolalarni qayta ko‘rib chiqing."
            st.markdown(
                f'<div class="score-box"><div class="score-num">{score}<small>/100</small></div>'
                f'<div class="score-text"><b>AI Tergovchi-Ekspert bahosi</b><br>{esc(verdict)}</div></div>',
                unsafe_allow_html=True,
            )
        st.markdown(evaluation)

    with st.expander("Namuna yechimni ko‘rish"):
        st.markdown(case["namuna_yechim"])
        st.markdown(
            "**Baholash mezonlari:**\n" + "\n".join(f"- {item}" for item in case["baholash_mezonlari"])
        )


def page_quiz() -> None:
    page_head(
        "5-modul", "Bilimni tekshirish testi",
        "10 ta savol. Barcha savollarga javob belgilab, natijani tekshiring — to‘g‘ri javoblar va huquqiy "
        "izohlar darhol ko‘rsatiladi.",
    )
    set_context(
        "Bilimni tekshirish testi",
        "Test savollari",
        "\n".join(
            f"{i}. {q['savol']} Variantlar: " + " | ".join(q["variantlar"])
            for i, q in enumerate(QUIZ, start=1)
        ),
    )

    with st.form("quiz_form"):
        for index, question in enumerate(QUIZ):
            st.markdown(f"**{index + 1}. {question['savol']}**")
            st.radio(
                f"{index + 1}-savol javobi",
                list(range(len(question["variantlar"]))),
                format_func=lambda option, q=question: q["variantlar"][option],
                index=None,
                key=f"quiz_q{index}",
                label_visibility="collapsed",
            )
        submitted = st.form_submit_button("Natijani tekshirish", type="primary")

    if submitted:
        st.session_state["quiz_done"] = True

    if not st.session_state.get("quiz_done"):
        return

    answers = [st.session_state.get(f"quiz_q{index}") for index in range(len(QUIZ))]
    unanswered = sum(1 for value in answers if value is None)
    correct = sum(1 for value, question in zip(answers, QUIZ) if value == question["togri"])
    percent = round(correct * 100 / len(QUIZ))

    if percent >= 90:
        verdict = "A’lo! Mavzuni puxta o‘zlashtirgansiz."
    elif percent >= 70:
        verdict = "Yaxshi natija. Xato qilingan savollar izohini ko‘rib chiqing."
    elif percent >= 50:
        verdict = "Qoniqarli. Tegishli maqolalarni qayta o‘qish tavsiya etiladi."
    else:
        verdict = "Mavzuni qayta o‘rganish kerak. Maqolalar va glossariydan boshlang."

    st.markdown(
        f'<div class="score-box"><div class="score-num">{percent}<small>%</small></div>'
        f'<div class="score-text"><b>To‘g‘ri javoblar: {correct} / {len(QUIZ)}</b><br>{esc(verdict)}</div></div>',
        unsafe_allow_html=True,
    )
    st.progress(percent / 100)
    if unanswered:
        st.warning(f"{unanswered} ta savolga javob belgilanmagan — ular noto‘g‘ri deb hisoblandi.")

    st.markdown("### Savollar bo‘yicha tahlil")
    for index, (value, question) in enumerate(zip(answers, QUIZ), start=1):
        is_correct = value == question["togri"]
        chosen = question["variantlar"][value] if value is not None else "javob belgilanmagan"
        right = question["variantlar"][question["togri"]]
        css_class = "q-ok" if is_correct else "q-bad"
        icon = "✅" if is_correct else "❌"
        wrong_line = "" if is_correct else f"<div><b>To‘g‘ri javob:</b> {esc(right)}</div>"
        st.markdown(
            f'<div class="q-result {css_class}"><div class="q-title">{icon} {index}. {esc(question["savol"])}</div>'
            f"<div><b>Sizning javobingiz:</b> {esc(chosen)}</div>{wrong_line}"
            f'<div class="q-expl"><b>Huquqiy izoh.</b> {esc(question["izoh"])}</div></div>',
            unsafe_allow_html=True,
        )
    st.button("🔄 Testni qayta boshlash", on_click=reset_quiz, key="quiz_reset")


def page_about() -> None:
    page_head("Loyiha haqida", PLATFORM_NAME, PLATFORM_TOPIC + ".")
    st.markdown(f'<div class="about-credit">{esc(AUTHOR_CREDIT)}</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="card"><div class="card-title">Maqsad</div>'
        "<p>Platforma huquqshunos talabalar, kursantlar, tergovchilar va huquqshunos olimlar uchun raqamli "
        "transformatsiya va sun’iy intellekt davrida huquq ijodkorligi hamda huquqiy tartibga solishning nazariy "
        "va amaliy masalalarini interaktiv shaklda o‘rganish imkonini beradi. Nazariy material (maqolalar), "
        "normativ asos (qonunchilik xaritasi), tushunchalar apparati (glossariy), amaliy ko‘nikma (kazuslar) va "
        "o‘z-o‘zini nazorat (test) bir joyga jamlangan.</p></div>"
        '<div class="card"><div class="card-title">AI Huquqshunos Yordamchi</div>'
        "<p>Yordamchi Google Gemini modeli asosida ishlaydi va siz o‘qiyotgan sahifa matnini kontekst sifatida "
        "oladi. Uch xil tushuntirish uslubi mavjud: oddiy tilda (hayotiy misol bilan), akademik tilda (nazariy "
        "tahlil) va qonun moddalari bilan (normativ asos). API kaliti faqat joriy sessiyada saqlanadi.</p></div>"
        '<div class="card card-navy"><div class="card-title">Muhim eslatmalar</div>'
        "<p>• Platforma o‘quv-ilmiy maqsadda yaratilgan; undagi materiallar va AI javoblari rasmiy yuridik "
        "maslahat hisoblanmaydi.<br>"
        "• Qonun normalari qisqacha bayon qilingan. Aniq iqtibos va amaldagi tahrir uchun lex.uz — "
        "Qonunchilik ma’lumotlari milliy bazasidagi rasmiy matnga murojaat qiling. Ma’lumotlar 2026-yil noyabr "
        "holatiga ko‘ra tayyorlangan.<br>"
        "• Sun’iy intellekt xato qilishi mumkin: uning javoblarini, ayniqsa modda raqamlarini, rasmiy manba "
        "bilan solishtiring. Bu — platformaning o‘zi targ‘ib qilayotgan «Human-in-the-loop» qoidasining "
        "amaliy ifodasidir.</p></div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="card"><div class="card-title">Texnologiyalar</div><div>'
        + badges_html(["Python", "Streamlit", "Google Gemini API (google-genai)", "python-dotenv"], "badge-navy")
        + "</div></div>",
        unsafe_allow_html=True,
    )
    set_context("Loyiha haqida", PLATFORM_NAME, f"{PLATFORM_TOPIC}. {AUTHOR_CREDIT}")


# --------------------------------------------------------------------------- AI yordamchi paneli
def render_assistant(api_key: str) -> None:
    context = st.session_state.get("ctx") or {}
    with st.container(key="ai_panel"):
        st.markdown(
            '<div class="ai-head"><div class="t">🤖 AI Huquqshunos Yordamchi</div>'
            '<div class="s">Siz o‘qiyotgan matnni biladi — bemalol «buni tushunmadim» deb yozing</div></div>'
            f'<div class="ctx-chip">📌 <b>Joriy kontekst:</b> {esc(context.get("tur", "—"))} — '
            f'{esc(context.get("sarlavha", ""))}</div>',
            unsafe_allow_html=True,
        )
        if not api_key:
            st.markdown(
                '<div class="ai-note">🔑 Yordamchini ishga tushirish uchun chap paneldagi <b>«Gemini API kaliti»</b> '
                "maydoniga kalitingizni kiriting. Bepul kalit: aistudio.google.com/apikey</div>",
                unsafe_allow_html=True,
            )

        st.radio(
            "Tushuntirish uslubi",
            list(MODES.keys()),
            format_func=lambda mode_key: MODES[mode_key]["label"],
            key="mode",
        )

        st.caption("Tezkor savollar")
        chip_prompt = None
        for index, prompt in enumerate(QUICK_PROMPTS):
            if st.button(prompt, key=f"chip_{index}"):
                chip_prompt = prompt

        chat_box = st.container(height=430)
        typed = st.chat_input("Savolingizni yozing…", key="chat_input")
        st.button("🗑️ Suhbatni tozalash", key="clear_chat", on_click=clear_chat)

        pending = st.session_state.pop("pending", None)
        if pending:
            request = pending
        elif chip_prompt:
            request = {"text": chip_prompt, "focus": None, "mode": None}
        elif typed:
            request = {"text": typed, "focus": None, "mode": None}
        else:
            request = None

        history = st.session_state["chat"]
        with chat_box:
            if not history and request is None:
                st.markdown(
                    '<div class="ai-empty">Suhbat hali boshlanmagan.<br>Savol yozing, tezkor savollardan birini '
                    "tanlang yoki matn ostidagi «AI orqali tushuntir» tugmasini bosing.</div>",
                    unsafe_allow_html=True,
                )
            for message in history:
                avatar = "🧑‍🎓" if message["role"] == "user" else "⚖️"
                with st.chat_message(message["role"], avatar=avatar):
                    st.markdown(message["text"])

            if request is not None:
                with st.chat_message("user", avatar="🧑‍🎓"):
                    st.markdown(request["text"])
                with st.chat_message("assistant", avatar="⚖️"):
                    is_system_note = True
                    if not api_key:
                        reply = NO_KEY_MESSAGE
                    elif not ai_allowed():
                        reply = LIMIT_MESSAGE
                    else:
                        count_ai_call()
                        with st.spinner("Javob tayyorlanmoqda…"):
                            answer, error = ask_tutor(
                                api_key=api_key,
                                user_message=request["text"],
                                mode=request.get("mode") or st.session_state.get("mode", "oddiy"),
                                context=context,
                                history=[m for m in history if not m.get("sys")],
                                focus=request.get("focus"),
                            )
                        reply = error or answer
                        is_system_note = bool(error)
                    st.markdown(reply)
                history.append({"role": "user", "text": request["text"], "sys": is_system_note})
                history.append({"role": "assistant", "text": reply, "sys": is_system_note})


# --------------------------------------------------------------------------- asosiy oqim
def main() -> None:
    init_state()
    load_css()
    api_key = render_sidebar()

    content_col, assistant_col = st.columns([1.85, 1], gap="large")
    with content_col:
        page = st.session_state.get("page", PAGE_HOME)
        if page == PAGE_ARTICLES:
            page_articles()
        elif page == PAGE_LAWS:
            page_legislation()
        elif page == PAGE_GLOSSARY:
            page_glossary()
        elif page == PAGE_CASES:
            page_cases(api_key)
        elif page == PAGE_QUIZ:
            page_quiz()
        elif page == PAGE_ABOUT:
            page_about()
        else:
            page_home()
    with assistant_col:
        render_assistant(api_key)


main()
