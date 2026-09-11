import re
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class HRMatchingEngine:
    def __init__(self):
        # Diccionario de competencias conductuales y psicológicas clave
        self.soft_skills_lexicon = [
            "liderazgo", "empatia", "resiliencia", "trabajo en equipo", "comunicacion",
            "comunicación", "pensamiento critico", "pensamiento crítico", "adaptabilidad",
            "orientacion al logro", "orientación al logro", "resolucion de problemas",
            "resolución de problemas", "gestion del tiempo", "inteligencia emocional",
            "proactividad", "negociacion", "negociación", "compromiso"
        ]

    def _clean_text(self, text):
        text = text.lower()
        text = re.sub(r'[^a-záéíóúñ0-9\s]', ' ', text)
        return text

    def calculate_hard_skills_match(self, jd_text, candidate_texts):
        cleaned_jd = self._clean_text(jd_text)
        cleaned_cvs = [self._clean_text(cv) for cv in candidate_texts]
        
        all_docs = [cleaned_jd] + cleaned_cvs
        vectorizer = TfidfVectorizer(stop_words='spanish')
        tfidf_matrix = vectorizer.fit_transform(all_docs)
        
        # Similitud Coseno entre JD (índice 0) y cada CV
        similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])[0]
        return np.round(similarities * 100, 2)

    def calculate_soft_skills_match(self, jd_text, candidate_texts):
        cleaned_jd = self._clean_text(jd_text)
        
        # Identificar qué soft skills requiere la empresa
        jd_skills = set([skill for skill in self.soft_skills_lexicon if skill in cleaned_jd])
        
        if not jd_skills:
            jd_skills = set(self.soft_skills_lexicon[:5]) # Fallback por defecto
            
        scores = []
        for cv in candidate_texts:
            cleaned_cv = self._clean_text(cv)
            found_skills = set([skill for skill in jd_skills if skill in cleaned_cv])
            score = (len(found_skills) / len(jd_skills)) * 100 if jd_skills else 50.0
            scores.append(min(score + 15.0, 100.0)) # Calibración psicológica
            
        return np.round(scores, 2)

    def evaluate_candidates(self, jd_text, candidates_texts, candidates_names, w_hard=0.6, w_soft=0.4):
        hard_scores = self.calculate_hard_skills_match(jd_text, candidates_texts)
        soft_scores = self.calculate_soft_skills_match(jd_text, candidates_texts)
        
        global_scores = np.round((hard_scores * w_hard) + (soft_scores * w_soft), 2)
        
        recommendations = []
        for score in global_scores:
            if score >= 65:
                recommendations.append("⭐ Altamente Recomendado (Pasa a Entrevista Afectiva/Técnica)")
            elif score >= 45:
                recommendations.append("✔️ Recomendado con Reservas (Evaluar competencias específicas)")
            else:
                recommendations.append("❌ Descartado para la terna final")
                
        df = pd.DataFrame({
            'Candidato': candidates_names,
            'Score Global (%)': global_scores,
            'Score Hard Skills (%)': hard_scores,
            'Score Soft Skills (%)': soft_scores,
            'Recomendación HR': recommendations
        })
        
        return df.sort_values(by='Score Global (%)', ascending=False).reset_index(drop=True)
