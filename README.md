# 🧠 HR-MatchAI Pro: Ecosystem de Intelligence Organizational & People Analytics

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32-FF4B4B)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.4-F7931E)
![Domain](https://img.shields.io/badge/Domain-Psychology%20%26%20HR--Tech-green)

**HR-MatchAI Pro** es una solución integral de **People Analytics** que fusiona la **Psicología Organizacional** con técnicas de **Procesamiento de Lenguaje Natural (PLN)** y **Machine Learning**. 

Diseñado tanto para la selección científica de candidatos como para el diagnóstico continuo del clima laboral y la prevención del *burnout*.

---

## 🚀 Características Principales

### 1. 🎯 Módulo de Selección Científica y Match de Candidatos
- **Vectorización TF-IDF & Similitud de Coseno:** Evalúa cuantitativamente el grado de alineación técnica entre el puesto (Job Description) y los CVs de los postulantes.
- **Detección de Competencias Blandas (Soft Skills):** Algoritmo basado en diccionarios psicométricos para medir competencias como *Liderazgo, Empatía, Resiliencia y Trabajo en Equipo*.
- **Sistema de Scoring Ponderado:** Permite a los reclutadores ajustar el peso entre habilidades duras y blandas según la naturaleza del perfil.

### 2. 📊 Módulo de Clima Laboral & Sentimiento (NLP)
- **Sentiment Analysis cualitativo:** Clasifica la retroalimentación de encuestas en estados *Positivo, Neutro o Riesgo/Negativo*.
- **Indicador de Attrition (Riesgo de Rotación):** Detecta alertas tempranas de sobrecarga de trabajo (*burnout*) e insatisfacción salarial o de liderazgo.
- **Visualización Interactiva:** Gráficos dinámicos con Plotly para reportes ejecutivos.

---

## 🛠️ Estructura del Proyecto

```text
hr-matchai-pro/
│
├── app.py                   # Aplicación principal e interfaz web (Streamlit)
├── matching_engine.py       # Motor NLP de compatibilidad CV-Puesto (TF-IDF + Cosine Similarity)
├── climate_analytics.py     # Motor NLP de análisis de sentimiento para Clima Laboral
├── requirements.txt         # Dependencias de Python necesarias
└── README.md                # Documentación del proyecto
