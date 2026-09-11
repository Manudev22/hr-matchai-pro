import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from matching_engine import HRMatchingEngine
from climate_analytics import ClimateAnalyticsEngine

# Configuración inicial de la interfaz de Streamlit
st.set_page_config(
    page_title="HR-MatchAI Pro | Talent & Climate Intelligence",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo visual CSS personalizado
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        color: #1E3A8A;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #4B5563;
        margin-bottom: 1.5rem;
    }
    .stTabs [data-baseweb="tab"] {
        padding-top: 10px;
        padding-bottom: 10px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Encabezado Principal
st.markdown('<div class="main-title">🧠 HR-MatchAI Pro: Ecosystem de Intelligence Organizational</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Plataforma integral de Selección Científica de Personal (PLN + Competencias) y Diagnóstico Organizacional de Clima Laboral</div>', unsafe_allow_html=True)

# Inicializar motores
@st.cache_resource
def load_engines():
    return HRMatchingEngine(), ClimateAnalyticsEngine()

matcher, climate_engine = load_engines()

# Navegación por Pestañas
tab1, tab2, tab3 = st.tabs([
    "🎯 Módulo 1: Reclutamiento & Match de Talento",
    "📊 Módulo 2: Analytics de Clima Laboral & Sentimiento",
    "📚 Módulo 3: Fundamento Metodológico y Documentación"
])

# ==========================================
# TAB 1: RECLUTAMIENTO Y MATCH DE TALENTO
# ==========================================
with tab1:
    st.header("🎯 Match Inteligente de Habilidades y Competencias Conductuales")
    st.write("Analice la compatibilidad técnica y actitudinal de candidatos aplicando **Vectorización TF-IDF** y **Modelado de Competencias de Psicología Organizacional**.")
    
    col_jd, col_cvs = st.columns([1, 1])
    
    with col_jd:
        st.subheader("📋 Perfil del Puesto (Job Description)")
        job_role = st.text_input("Nombre de la Posición", "Lead de Selección y People Analytics")
        
        default_jd = """Buscamos un Psicólogo Organizacional o profesional afín con más de 3 años de experiencia en Reclutamiento y Selección, People Analytics y Clima Laboral.
Requisitos clave:
- Experiencia comprobada en entrevistas por competencias (STAR) y evaluación psicométrica.
- Conocimiento en análisis de datos de RRHH, SQL, Python o Excel avanzado.
- Liderazgo, empatía, pensamiento crítico, resiliencia y excelente comunicación interpersonal.
- Orientación al logro y capacidad para trabajar bajo presión en entornos cambiantes."""
        
        jd_input = st.text_area("Descripción detallada del puesto:", value=default_jd, height=250)
        
        st.subheader("⚙️ Ponderación del Algoritmo")
        weight_hard = st.slider("Peso Habilidades Técnicas / Duras (%)", 0, 100, 60)
        weight_soft = 100 - weight_hard
        st.caption(f"Peso asignado a Competencias Blando/Conductuales: **{weight_soft}%**")

    with col_cvs:
        st.subheader("👥 Evaluación de Candidatos")
        
        cand_names = []
        cand_texts = []
        
        num_candidates = st.number_input("Número de candidatos a evaluar", min_value=2, max_value=5, value=3)
        
        defaults_cv = [
            """Licenciada en Psicología Organizacional con 4 años de experiencia en selección de personal y People Analytics.
Manejo avanzado de entrevistas por competencias, KPI de talento y dashboard en Python y Excel.
Destacada capacidad de empatía, liderazgo colaborativo, excelente comunicación y alta orientación al logro.""",
            
            """Ingeniero Industrial enfocado en Recursos Humanos y Nómina. Experiencia en liquidación de sueldos, contratos y control de asistencia.
Conocimiento intermedio de SQL y Python.
Gran resiliencia, trabajo en equipo y capacidad de análisis numérico.""",
            
            """Desarrollador de Software Senior con 6 años programando en Python, React y AWS.
Sin experiencia previa en gestión de personas, recursos humanos o evaluación psicométrica.
Enfocado en desarrollo técnico y resolución de problemas algorítmicos complejos."""
        ]
        
        for i in range(num_candidates):
            with st.expander(f"Candidato #{i+1}", expanded=(i==0)):
                name = st.text_input(f"Nombre Candidato {i+1}", value=f"Candidato {i+1}", key=f"name_{i}")
                default_text = defaults_cv[i] if i < len(defaults_cv) else "Experiencia laboral y competencias..."
                text = st.text_area(f"CV / Extracto Candidato {i+1}", value=default_text, height=110, key=f"cv_{i}")
                cand_names.append(name)
                cand_texts.append(text)

    st.markdown("---")
    
    if st.button("🚀 Ejecutar Algoritmo de Match Inteligente", type="primary", use_container_width=True):
        with st.spinner("Procesando vectores NLP y analizando perfil psicológico/conductual..."):
            results_df = matcher.evaluate_candidates(
                jd_text=jd_input,
                candidates_texts=cand_texts,
                candidates_names=cand_names,
                w_hard=weight_hard/100.0,
                w_soft=weight_soft/100.0
            )
            
            st.success("¡Análisis completado con éxito!")
            
            # Métricas rápidas
            top_candidate = results_df.iloc[0]
            m1, m2, m3 = st.columns(3)
            m1.metric("🥇 Candidato Recomendado", top_candidate['Candidato'])
            m2.metric("🎯 Match Global", f"{top_candidate['Score Global (%)']}%")
            m3.metric("🧠 Match Psicoprofesional", f"{top_candidate['Score Soft Skills (%)']}%")
            
            # Gráfico de comparación
            fig_match = px.bar(
                results_df,
                x='Candidato',
                y=['Score Hard Skills (%)', 'Score Soft Skills (%)'],
                title="Desglose de Compatibilidad por Candidato",
                barmode='group',
                color_discrete_sequence=['#2563EB', '#10B981']
            )
            fig_match.update_layout(yaxis_range=[0, 100], template="plotly_white")
            st.plotly_chart(fig_match, use_container_width=True)
            
            # Tabla de detalle
            st.subheader("📋 Matriz de Decisión para Selección")
            st.dataframe(
                results_df[['Candidato', 'Score Global (%)', 'Score Hard Skills (%)', 'Score Soft Skills (%)', 'Recomendación HR']],
                use_container_width=True
            )

# ==========================================
# TAB 2: CLIMA LABORAL & SENTIMIENTO
# ==========================================
with tab2:
    st.header("📊 Diagnóstico Organizacional de Clima Laboral & Sentimiento")
    st.write("Herramienta de **People Analytics** para procesar retroalimentación cualitativa de colaboradores y detectar riesgos de rotación (Attrition).")
    
    col_c1, col_c2 = st.columns([1, 1])
    
    with col_c1:
        st.subheader("📥 Cargar Respuestas de Encuesta de Clima")
        st.caption("Ingrese comentarios o retroalimentación abierta de los empleados:")
        
        sample_feedback = """1. Me siento muy motivado con el equipo, el liderazgo es cercano y empático. Excelente ambiente.
2. Los salarios están muy desactualizados respecto al mercado y los horarios sobrepasan la jornada laboral, hay mucho estrés.
3. Me gusta la cultura de la empresa, pero falta claridad en las oportunidades de ascenso y capacitaciones.
4. Mi jefe directo no escucha nuestras sugerencias. Siento frustración y burnout constante por la carga de trabajo.
5. Gran lugar para trabajar, excelentes beneficios de salud y flexibilidad de trabajo híbrido."""
        
        feedback_input = st.text_area("Respuestas de la encuesta (una por línea):", value=sample_feedback, height=220)
        
    with col_c2:
        st.subheader("📊 Métrica General de Satisfacción")
        st.markdown("""
        **Dimensiones Evaluadas por IA:**
        - **Liderazgo & Gestión**
        - **Compensación & Beneficios**
        - **Cultura & Balance Vida-Trabajo**
        - **Riesgo de Rotación (Burnout Indicator)**
        """)
        
    if st.button("🔍 Analizar Clima Laboral y Sentimientos", type="primary", use_container_width=True):
        comments = [c.strip() for c in feedback_input.split('\n') if len(c.strip()) > 5]
        
        if comments:
            analysis_df, summary_metrics = climate_engine.analyze_comments(comments)
            
            # KPIs Top
            kpi1, kpi2, kpi3, kpi4 = st.columns(4)
            kpi1.metric("Índice Clima Favorabilidad", f"{summary_metrics['positivity_rate']}%")
            kpi2.metric("Comentarios Positivos", summary_metrics['positive_count'])
            kpi3.metric("Comentarios Neutros", summary_metrics['neutral_count'])
            kpi4.metric("Alerta de Riesgo / Detractores", summary_metrics['negative_count'], delta="-Atención Requerida" if summary_metrics['negative_count']>0 else "Ok")
            
            col_graph1, col_graph2 = st.columns(2)
            
            with col_graph1:
                # Donut Chart Sentimientos
                fig_pie = px.pie(
                    values=[summary_metrics['positive_count'], summary_metrics['neutral_count'], summary_metrics['negative_count']],
                    names=['Positivo', 'Neutro', 'Crítico / Riesgo'],
                    title="Distribución de Sentimiento Organizacional",
                    color_discrete_sequence=['#10B981', '#FBBF24', '#EF4444'],
                    hole=0.4
                )
                st.plotly_chart(fig_pie, use_container_width=True)
                
            with col_graph2:
                # Gráfico de Barras por respuesta
                fig_polar = px.bar(
                    analysis_df,
                    x="ID",
                    y="Score Sentimiento",
                    color="Categoría Clima",
                    title="Polaridad por Respuesta Individual",
                    color_discrete_map={'Positivo': '#10B981', 'Neutro': '#FBBF24', 'Riesgo / Negativo': '#EF4444'}
                )
                st.plotly_chart(fig_polar, use_container_width=True)
                
            st.subheader("📑 Análisis Cualitativo Detallado")
            st.dataframe(analysis_df[['Comentario', 'Categoría Clima', 'Score Sentimiento', 'Keywords Clave']], use_container_width=True)

# ==========================================
# TAB 3: DOCUMENTACIÓN Y METODOLOGÍA
# ==========================================
with tab3:
    st.header("📚 Arquitectura del Sistema & Fundamento Teórico")
    
    st.markdown("""
    ### 🔬 Intersección entre Psicología Organizacional e Inteligencia Artificial
    
    Esta aplicación fue creada combinando **fundamentos psicométricos/organizacionales** con algoritmos avanzados de **Procesamiento de Lenguaje Natural (PLN)**.
    
    #### 1. Algoritmo de Match de Candidatos (TF-IDF + Cosine Similarity)
    * **Modelado de Lenguaje:** El texto de las descripciones de puestos y CVs es transformado en vectores numéricos mediante el método **TF-IDF (Term Frequency - Inverse Document Frequency)**.
    * **Métrica de Similitud Coseno:** Se mide el ángulo entre el vector del puesto y el vector del candidato en un espacio multidimensional:
    $$\\text{Cosine Similarity}(A, B) = \\frac{A \\cdot B}{\\|A\\| \\|B\\|}$$
    * **Diccionario Psicológico de Soft Skills:** Se analiza la presencia de competencias conductuales clave (Liderazgo, Trabajo en Equipo, Empatía, Resiliencia, Comunicación) mapeadas desde modelos de evaluación por competencias.

    #### 2. Módulo de Sentiment Analysis en Clima Laboral
    * **Lexicon-Based Sentiment Engine:** Clasifica las respuestas cualitativas de encuestas de clima en puntuaciones de favorabilidad (Sentimiento Positivo, Neutro y Crítico).
    * **Prevención de Attrition:** Permite a los equipos de Gestión Humana identificar alertas tempranas de *burnout* y rotación de personal antes de que afecten la operación.
    """)
