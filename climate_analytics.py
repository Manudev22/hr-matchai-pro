import pandas as pd
import numpy as np
import re

class ClimateAnalyticsEngine:
    def __init__(self):
        # Lexicon de polaridad adaptado a entorno laboral
        self.positive_words = [
            'excelente', 'motivado', 'bueno', 'liderazgo', 'empatico', 'empático',
            'flexible', 'beneficios', 'salud', 'contento', 'gran', 'siento', 'apoyo',
            'oportunidad', 'crecimiento', 'reconocimiento', 'hibrido', 'híbrido'
        ]
        
        self.negative_words = [
            'desactualizado', 'estres', 'estrés', 'sobresalen', 'sobrepasan',
            'no escucha', 'frustracion', 'frustración', 'burnout', 'carga',
            'malo', 'pesimo', 'pésimo', 'renunciar', 'falta', 'descontento', 'injusto'
        ]

    def _clean_comment(self, comment):
        return re.sub(r'[^a-záéíóúñ\s]', '', comment.lower())

    def analyze_comments(self, comments_list):
        results = []
        pos_count, neu_count, neg_count = 0, 0, 0
        
        for idx, comment in enumerate(comments_list):
            cleaned = self._clean_comment(comment)
            words = cleaned.split()
            
            pos_score = sum(1 for w in words if w in self.positive_words)
            neg_score = sum(1 for w in words if w in self.negative_words)
            
            net_score = pos_score - neg_score
            
            if net_score > 0:
                category = "Positivo"
                pos_count += 1
                sentiment_val = 1.0
            elif net_score < 0:
                category = "Riesgo / Negativo"
                neg_count += 1
                sentiment_val = -1.0
            else:
                category = "Neutro"
                neu_count += 1
                sentiment_val = 0.0
                
            keywords = [w for w in words if w in self.positive_words or w in self.negative_words]
            
            results.append({
                'ID': f"Emp_{idx+1}",
                'Comentario': comment,
                'Categoría Clima': category,
                'Score Sentimiento': sentiment_val,
                'Keywords Clave': ", ".join(set(keywords)) if keywords else "Sin palabras clave detectadas"
            })
            
        df_results = pd.DataFrame(results)
        
        total = len(comments_list)
        summary_metrics = {
            'positivity_rate': round((pos_count / total) * 100, 1) if total > 0 else 0,
            'positive_count': pos_count,
            'neutral_count': neu_count,
            'negative_count': neg_count
        }
        
        return df_results, summary_metrics
