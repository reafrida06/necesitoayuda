import streamlit as st
import time

st.set_page_config(
    page_title="¿Puede un algoritmo entender tu tristeza?",
    page_icon="🌀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── CSS muy mejorado ───────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Reset y base */
    html, body, [data-testid="stAppViewContainer"] {
        margin: 0 !important;
        padding: 0 !important;
        overflow: hidden !important;
        height: 100vh !important;
    }
    .main {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: #f0f0ff;
        padding: 0 !important;
        margin: 0 !important;
    }
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    section[data-testid="stSidebar"] { display: none !important; }

    /* Sección full-screen con animación de entrada */
    .section {
        height: 100vh;
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 2rem 6% 4rem;
        box-sizing: border-box;
        text-align: center;
        opacity: 0;
        transform: translateY(60px);
        transition: all 0.9s cubic-bezier(0.22, 1, 0.36, 1);
    }
    .section.visible {
        opacity: 1;
        transform: translateY(0);
    }

    /* Títulos con estilo creativo */
    h1 {
        font-family: 'Helvetica Neue', 'Segoe UI', sans-serif;
        font-size: 3.6rem;
        font-weight: 800;
        letter-spacing: -1px;
        margin: 0.4rem 0 1.2rem;
        background: linear-gradient(90deg, #c084fc, #a78bfa, #7c3aed);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        position: relative;
    }
    h1:after {
        content: '';
        position: absolute;
        width: 0;
        height: 4px;
        bottom: -12px;
        left: 50%;
        background: #a78bfa;
        transition: width 0.7s ease, left 0.7s ease;
    }
    .section.visible h1:after {
        width: 140px;
        left: calc(50% - 70px);
    }

    h3 {
        font-size: 1.9rem;
        opacity: 0.92;
        margin: 0.8rem 0 2.2rem;
        font-weight: 400;
    }

    /* Texto principal */
    .content {
        font-family: Georgia, 'Times New Roman', serif;
        font-size: 1.28rem;
        line-height: 1.78;
        max-width: 860px;
        margin: 0 auto 2rem;
    }

    /* Citas destacadas */
    blockquote {
        font-style: italic;
        font-size: 1.4rem;
        color: #d1d5ff;
        border-left: 5px solid #8b5cf6;
        padding-left: 1.6rem;
        margin: 2.2rem auto;
        max-width: 720px;
    }

    /* Listas con iconos */
    .content ul {
        list-style: none;
        padding-left: 0;
        text-align: left;
        max-width: 720px;
        margin: 1.8rem auto;
    }
    .content li {
        margin: 1.1rem 0;
        position: relative;
        padding-left: 2.2rem;
    }
    .content li:before {
        content: "→";
        position: absolute;
        left: 0;
        color: #a78bfa;
        font-weight: bold;
    }

    /* Botones navegación */
    .nav-container {
        position: fixed;
        bottom: 2.2rem;
        left: 50%;
        transform: translateX(-50%);
        z-index: 100;
        display: flex;
        gap: 5rem;
    }
    .nav-btn {
        background: rgba(30, 30, 60, 0.7);
        backdrop-filter: blur(10px);
        color: white;
        border: 1px solid rgba(168, 85, 247, 0.4);
        padding: 1rem 2.6rem;
        font-size: 1.15rem;
        border-radius: 999px;
        cursor: pointer;
        transition: all 0.4s ease;
        box-shadow: 0 6px 20px rgba(0,0,0,0.35);
    }
    .nav-btn:hover {
        background: rgba(168, 85, 247, 0.25);
        border-color: #a78bfa;
        transform: translateY(-4px) scale(1.04);
        box-shadow: 0 12px 30px rgba(168, 85, 247, 0.3);
    }

    /* Toggle modo oscuro (lo dejamos sutil) */
    .stSwitch {
        position: fixed;
        top: 1.4rem;
        right: 1.8rem;
        z-index: 200;
    }
</style>

<script>
    // Animar sección actual al cargar / cambiar
    function animateSection() {
        const sections = document.querySelectorAll('.section');
        sections.forEach((s, i) => {
            s.classList.remove('visible');
            if (i === window.currentSection || typeof window.currentSection === 'undefined') {
                setTimeout(() => s.classList.add('visible'), 80);
            }
        });
    }
    setTimeout(animateSection, 120);
</script>
""", unsafe_allow_html=True)

# ── Modo (por ahora solo uno – puedes expandirlo después) ────────
st.markdown("<style>:root { --bg: linear-gradient(135deg, #0f0c29, #302b63, #24243e); }</style>", unsafe_allow_html=True)

# ── Contenido ──────────────────────────────────────────────────────────────
sections = [
    {
        "title": "¿Puede un algoritmo entender tu tristeza?",
        "subtitle": "El auge de la amistad con chatbots terapéuticos",
        "content": """Por: Frida Rea / Gemini

> “La capacidad del ser humano para construir puentes de confianza y esperanza no conoce límites, incluso cuando el interlocutor es un reflejo de nuestra propia innovación.”"""
    },
    {
        "title": "La conexión que nadie esperaba",
        "content": """¿Alguna vez has sentido que Siri o Alexa te "entienden" mejor que algunas personas? Quizás parece una exageración, pero para miles de personas que buscan apoyo emocional en sus teléfonos, esta conexión es una realidad tangible.

Imagina despertar a las tres de la mañana con una crisis de ansiedad y, en lugar de esperar semanas por una cita médica, recibir una respuesta cálida, empática y oportuna de un asistente virtual.

Esto nos lleva a una pregunta inquietante y fascinante:  
**¿Es posible generar un vínculo emocional real con un programa de computadora?**  
La ciencia actual responde: sí."""
    },
    # ... (agrega las demás secciones con títulos más evocadores si quieres)
    # Por brevedad solo muestro las primeras → copia el resto del contenido anterior
    {
        "title": "Referencias",
        "content": "Toca cada tarjeta para descubrir qué dice la investigación"
    }
]

if "current_section" not in st.session_state:
    st.session_state.current_section = 0

current = st.session_state.current_section

# Render sección
st.markdown(f'<div class="section" id="sec-{current}">', unsafe_allow_html=True)

data = sections[current]

st.markdown(f'<h1>{data["title"]}</h1>', unsafe_allow_html=True)
if "subtitle" in data:
    st.markdown(f'<h3>{data["subtitle"]}</h3>', unsafe_allow_html=True)

if "content" in data:
    # Procesamos el contenido para darle formato creativo
    content = data["content"]
    if ">" in content:  # cita
        parts = content.split(">", 1)
        if len(parts) == 2:
            st.markdown(f'<div class="content">{parts[0].strip()}</div>', unsafe_allow_html=True)
            st.markdown(f'<blockquote>{parts[1].strip()}</blockquote>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="content">{content}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="content">{content.replace("\n", "<br>")}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── Navegación ─────────────────────────────────────────────────────────────
with st.container():
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.markdown('<div class="nav-container">', unsafe_allow_html=True)
        c1, c2 = st.columns(2)

        with c1:
            if current > 0:
                if st.button("←  Anterior", key=f"prev_{current}", use_container_width=True):
                    st.session_state.current_section -= 1
                    st.rerun()

        with c2:
            if current < len(sections) - 1:
                if st.button("Siguiente →", key=f"next_{current}", use_container_width=True):
                    st.session_state.current_section += 1
                    st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# Pequeño pie
st.markdown(
    "<div style='position:fixed; bottom:0.6rem; right:1.4rem; opacity:0.5; font-size:0.82rem;'>"
    "Exploración · 2025–2026</div>",
    unsafe_allow_html=True
)
