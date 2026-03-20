import streamlit as st

# Configuración de página
st.set_page_config(
    page_title="¿Puede un algoritmo entender tu tristeza?",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS ajustado: centrado + menos espacio superior
st.markdown("""
    <style>
    /* Resetear márgenes y paddings globales */
    .main { 
        background-color: var(--background);
        color: var(--text);
        padding: 0 !important;
        margin: 0 !important;
    }
    .block-container {
        padding-top: 1rem !important;    /* muy poco espacio arriba */
        padding-bottom: 5rem !important;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    section[data-testid="stSidebar"] { display: none !important; }

    /* Secciones full viewport */
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
        scroll-snap-align: start;
        text-align: center;
        transition: opacity 0.8s ease, transform 0.6s ease;
    }
    .section > * {
        max-width: 900px;
        margin-left: auto;
        margin-right: auto;
    }

    /* Títulos y texto */
    h1, h2, h3 {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-weight: 700;
        color: var(--title);
        margin: 0.8rem 0 1.4rem;
        text-align: center;
    }
    p, li, blockquote {
        font-family: Georgia, 'Times New Roman', serif;
        font-size: 1.18rem;
        line-height: 1.68;
        margin: 1rem 0;
        text-align: center;
    }
    ul {
        list-style-position: inside;
        padding-left: 0;
        text-align: left;
        max-width: 720px;
        margin: 1.2rem auto;
    }

    /* Botones navegación */
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

    /* Referencias */
    .stExpander {
        max-width: 820px;
        margin: 1.2rem auto;
        text-align: left;
    }
    </style>

    <script>
    // Pequeña mejora de visibilidad al entrar en viewport
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

# ── Modo oscuro / claro ───────────────────────────────────────
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

# ── Contenido ──────────────────────────────────────────────────
sections = [
    # 0
    {
        "title": "¿Puede un algoritmo entender tu tristeza?",
        "subtitle": "El auge de la amistad con chatbots terapéuticos",
        "content": """Por: Frida Rea / Gemini

“La capacidad del ser humano para construir puentes de confianza y esperanza no conoce límites, incluso cuando el interlocutor es un reflejo de nuestra propia innovación.”"""
    },
    # 1
    {
        "title": "¿Alguna vez has sentido que Siri o Alexa te “entienden” mejor…?",
        "content": """¿Alguna vez has sentido que Siri o Alexa te "entienden" mejor que algunas personas? Quizás parece una exageración, pero para miles de personas que buscan apoyo emocional en sus teléfonos, esta conexión es una realidad tangible. Imagina despertar a las tres de la mañana con una crisis de ansiedad y, en lugar de esperar semanas por una cita médica, recibir una respuesta cálida, empática y oportuna de un asistente virtual.

Esto nos lleva a una pregunta que parece sacada de la ciencia ficción: ¿Es posible generar un vínculo emocional real con un programa de computadora? La ciencia actual dice que sí."""
    },
    # 2
    {
        "title": "De la terapia tradicional a la “Alianza Digital”",
        "content": """En la psicología clásica, existe un concepto fundamental llamado Alianza Terapéutica. Según Bordin (1979), este es el "pegamento" que une al paciente con su terapeuta: se basa en la confianza mutua, el cariño y el acuerdo sobre los objetivos del tratamiento (citado en D’Alfonso et al., 2020).

Hoy, con la evolución de la tecnología, los expertos hablan de una nueva dimensión: la Alianza Terapéutica Digital (ATD). Ya no vemos a la aplicación como una herramienta fría o estática; ahora establecemos una conexión subjetiva con ella que puede predecir qué tanto nos comprometeremos con el proceso y qué tan exitoso será el resultado (Xu et al., 2025). Al usar lenguaje natural, estas máquinas han dejado de realizar solo tareas lógicas para operar en nuestras "fronteras socioemocionales", ese espacio donde guardamos nuestros sentimientos más profundos (Gómez Murcia, 2024)."""
    },
    # 3
    {
        "title": "¿Cómo nos “enamora” un chatbot?",
        "content": """Parece increíble, pero investigaciones han demostrado que chatbots como Woebot pueden formar vínculos a "nivel humano" en un tiempo récord. Mientras que a las personas nos puede tomar semanas ganar la confianza de alguien, estos sistemas logran niveles de alianza similares a la terapia presencial en tan solo cinco días (Darcy et al., 2021).

¿Cuál es el secreto? No es magia, es diseño estratégico:

• Roles sociales: Cuando el bot asume un papel de "compañero" o "guía", las personas muestran una mayor apertura emocional y ganas de seguir usando la app, a diferencia de las interfaces que se sienten puramente técnicas (Nißen et al., 2022).

• Señales de calidez: El uso de emojis, la personalización del lenguaje y la capacidad de ofrecer consejos rápidos y eficaces refuerzan nuestra confianza en el sistema (Vowels, 2024; Xu et al., 2025).

En palabras simples: No nos vinculamos con el código de programación, sino con la "personalidad" que la IA proyecta. Si se siente atento y nos ayuda, nuestro cerebro tiende a procesarlo como un apoyo real."""
    },
    # 4
    {
        "title": "Entre la eficacia y el riesgo",
        "content": """A pesar de estos avances, no todo es sencillo. Existe una tensión ética importante. Por un lado, la IA ofrece apoyo accesible, anónimo y disponible las 24 horas, algo vital ante la falta de atención en salud mental a nivel global (Rawat, 2025).

Por otro lado, expertos como Corbella et al. (2025) advierten que no debemos confundir una simulación técnica con un profesional de la salud real. Existe el riesgo de una "deshumanización" del proceso clínico, donde el usuario podría desarrollar una dependencia hacia un algoritmo que, por su naturaleza, no puede corresponder al afecto de la misma forma que un humano (Rivera Estrada & Sánchez Salazar, 2016)."""
    },
    # 5
    {
        "title": "¿Por qué esto nos importa hoy?",
        "content": """La brecha en salud mental es inmensa y la tecnología está intentando cerrar ese camino. Aunque todavía queda mucho por investigar sobre qué tan estables son estos lazos a largo plazo, la evidencia actual sugiere que las personas efectivamente suelen generar vínculos emocionales con chatbots terapéuticos (D’Alfonso et al., 2020).

En conclusión, estos "compañeros algorítmicos" ya son parte de nuestra realidad. El reto del futuro no será evitar que nos encariñemos con la tecnología, sino asegurar que esa conexión sea segura, ética y realmente beneficiosa para nuestra salud mental en la vida diaria."""
    },
    # 6 - Referencias
    {
        "title": "Referencias",
        "content": "Haz clic en cada referencia para leer su resumen"
    }
]

# Estado
if "current_section" not in st.session_state:
    st.session_state.current_section = 0

current = st.session_state.current_section

# Render sección actual
st.markdown('<div class="section">', unsafe_allow_html=True)

if current < len(sections) - 1:
    st.markdown(f'<h1>{sections[current]["title"]}</h1>', unsafe_allow_html=True)
    if "subtitle" in sections[current]:
        st.markdown(f'<h3>{sections[current]["subtitle"]}</h3>', unsafe_allow_html=True)
    st.markdown(sections[current]["content"])
else:
    st.markdown("<h1>Referencias</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:1.25rem; opacity:0.9; margin:1.5rem 0;'>Haz clic en cada referencia para leer su resumen</p>", unsafe_allow_html=True)
    
    refs = [
        ("Corbella, S., et al. (2025)", """Desafíos y riesgos de la simulación técnica en la salud mental digital. Editorial Académica.
El texto cuestiona la tendencia a considerar a los chatbots como "agentes de salud" en lugar de herramientas. Analiza el peligro de deshumanizar el vínculo terapéutico y propone lineamientos éticos para que la IA se integre de forma responsable en la psicología sin reemplazar la subjetividad y el cuidado que solo un humano puede brindar."""),
        ("D’Alfonso, S., et al. (2020)", """The digital therapeutic alliance: Concept and operationalization. Journal of Digital Psychology.
El texto explora cómo la interacción persona-computadora puede generar una alianza terapéutica digital. Propone que el diseño de la interfaz y la capacidad de respuesta del software son los factores que permiten al usuario sentir que hay una "colaboración" en su tratamiento, incluso sin un humano presente."""),
        # ... (las demás referencias igual que antes, solo copio las dos primeras para no alargar aquí)
        # Añade las restantes como en la versión anterior
    ]

    for autor, resumen in refs:
        with st.expander(autor):
            st.markdown(resumen)

st.markdown('</div>', unsafe_allow_html=True)

# Botones navegación
col1, col2, col3 = st.columns([1,3,1])
with col2:
    st.markdown('<div class="nav-container">', unsafe_allow_html=True)
    
    if current > 0:
        if st.button("← Anterior", key="prev"):
            st.session_state.current_section -= 1
            st.rerun()

    if current < len(sections) - 1:
        if st.button("Siguiente →", key="next"):
            st.session_state.current_section += 1
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; opacity:0.6; font-size:0.9rem; margin-top:6rem;'>Presentado con Streamlit • 2025</p>", unsafe_allow_html=True)
