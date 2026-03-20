import streamlit as st

# Configuración de página
st.set_page_config(
    page_title="¿Puede un algoritmo entender tu tristeza?",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS mejorado: centrado real + estilo más creativo
st.markdown("""
    <style>
    .main { 
        background: linear-gradient(
            180deg,
            var(--background) 0%,
            rgba(124, 58, 237, 0.05) 100%
        );
        color: var(--text);
        padding: 0 !important;
        margin: 0 !important;
    }

    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 5rem !important;
        padding-left: 1rem;
        padding-right: 1rem;
    }

    section[data-testid="stSidebar"] { display: none !important; }

    /* Secciones */
    .section {
        height: 100vh;
        min-height: 100vh;
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 1.5rem 8% 3rem;
        box-sizing: border-box;
        text-align: center;
        opacity: 0;
        transform: translateY(30px);
        transition: opacity 0.8s ease, transform 0.6s ease;
    }

    .section.visible {
        opacity: 1;
        transform: translateY(0);
    }

    .section > * {
        max-width: 850px;
        margin: 0 auto;
        text-align: center;
    }

    /* Títulos */
    h1 {
        font-size: 2.8rem;
        font-weight: 700;
        letter-spacing: -0.5px;
        margin: 0.8rem 0 1.4rem;
    }

    h1::after {
        content: "";
        display: block;
        width: 60px;
        height: 4px;
        margin: 10px auto 0;
        background: var(--accent);
        border-radius: 10px;
    }

    h3 {
        font-weight: 400;
        opacity: 0.8;
        margin-bottom: 1.5rem;
    }

    /* Texto */
    p {
        font-family: Georgia, 'Times New Roman', serif;
        font-size: 1.25rem;
        line-height: 1.75;
        letter-spacing: 0.2px;
        opacity: 0.95;
        margin: 1rem 0;
    }

    /* Listas centradas */
    ul {
        list-style-position: inside;
        padding-left: 0;
        text-align: center;
        max-width: 720px;
        margin: 1.2rem auto;
    }

    /* Citas estilo cinematográfico */
    blockquote {
        font-size: 1.4rem;
        font-style: italic;
        border-left: 4px solid var(--accent);
        padding-left: 1rem;
        margin: 2rem auto;
        opacity: 0.9;
    }

    /* Botones */
    .nav-container {
        position: fixed;
        bottom: 1.8rem;
        left: 50%;
        transform: translateX(-50%);
        z-index: 999;
        display: flex;
        gap: 4rem;
    }

    .nav-btn {
        background: var(--btn-bg);
        color: var(--btn-text);
        border: none;
        padding: 1rem 2.4rem;
        font-size: 1.1rem;
        border-radius: 50px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
    }

    .nav-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    }

    .stExpander {
        max-width: 820px;
        margin: 1.2rem auto;
        text-align: left;
    }
    </style>

    <script>
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.2 });

    document.querySelectorAll('.section').forEach(el => observer.observe(el));
    </script>
""", unsafe_allow_html=True)

# Modo oscuro / claro
dark_mode = st.toggle("Modo Oscuro 🌙", value=False)

if dark_mode:
    bg = "#0f0f17"
    text = "#e0e0ff"
    title = "#ffffff"
    btn_bg = "#2a2a40"
    btn_text = "#ffffff"
    accent = "#7c3aed"
else:
    bg = "#f9f9ff"
    text = "#1a1a2e"
    title = "#111827"
    btn_bg = "#ffffff"
    btn_text = "#111827"
    accent = "#6d28d9"

st.markdown(f"""
    <style>
    :root {{
        --background: {bg};
        --text: {text};
        --title: {title};
        --btn-bg: {btn_bg};
        --btn-text: {btn_text};
        --accent: {accent};
    }}
    </style>
""", unsafe_allow_html=True)

# Contenido
sections = [
    {
        "title": "¿Puede un algoritmo entender tu tristeza?",
        "subtitle": "El auge de la amistad con chatbots terapéuticos",
        "content": """Por: Frida Rea / Gemini

“La capacidad del ser humano para construir puentes de confianza y esperanza no conoce límites, incluso cuando el interlocutor es un reflejo de nuestra propia innovación.”"""
    },
    {
        "title": "¿Alguna vez has sentido que Siri o Alexa te “entienden” mejor…?",
        "content": """¿Alguna vez has sentido que Siri o Alexa te "entienden" mejor que algunas personas?..."""
    },
    {
        "title": "De la terapia tradicional a la “Alianza Digital”",
        "content": """En la psicología clásica, existe un concepto fundamental llamado Alianza Terapéutica..."""
    },
    {
        "title": "¿Cómo nos “enamora” un chatbot?",
        "content": """Parece increíble, pero investigaciones han demostrado que chatbots como Woebot..."""
    },
    {
        "title": "Entre la eficacia y el riesgo",
        "content": """A pesar de estos avances, no todo es sencillo..."""
    },
    {
        "title": "¿Por qué esto nos importa hoy?",
        "content": """La brecha en salud mental es inmensa..."""
    },
    {
        "title": "Referencias",
        "content": "Haz clic en cada referencia para leer su resumen"
    }
]

# Estado
if "current_section" not in st.session_state:
    st.session_state.current_section = 0

current = st.session_state.current_section

# Render
st.markdown('<div class="section">', unsafe_allow_html=True)

if current < len(sections) - 1:
    st.markdown(f'<h1>{sections[current]["title"]}</h1>', unsafe_allow_html=True)

    if "subtitle" in sections[current]:
        st.markdown(f'<h3>{sections[current]["subtitle"]}</h3>', unsafe_allow_html=True)

    st.markdown(f"""
    <div>
        <p>{sections[current]['content']}</p>
    </div>
    """, unsafe_allow_html=True)

else:
    st.markdown("<h1>Referencias</h1>", unsafe_allow_html=True)
    st.markdown("<p>Haz clic en cada referencia para leer su resumen</p>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Navegación
col1, col2, col3 = st.columns([1,3,1])
with col2:
    st.markdown('<div class="nav-container">', unsafe_allow_html=True)

    if current > 0:
        if st.button("← Anterior"):
            st.session_state.current_section -= 1
            st.rerun()

    if current < len(sections) - 1:
        if st.button("Siguiente →"):
            st.session_state.current_section += 1
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; opacity:0.6;'>Presentado con Streamlit • 2025</p>", unsafe_allow_html=True)
