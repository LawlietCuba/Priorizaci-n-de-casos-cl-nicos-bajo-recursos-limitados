from app.modules.LLMAnalysis import LLMAnalysis

class MockLLMAnalyzer:

    def analyze(self, symptoms: str) -> LLMAnalysis:

        text = symptoms.lower()

        severity = 0
        respiratory_risk = 0
        cardiac_risk = 0
        urgency = 0
        
        respiratory_keywords = {
            "dificultad respiratoria": 5,
            "disnea": 5,
            "hipoxia": 6,
            "cianosis": 7,
            "respiración agónica": 8,
            "insuficiencia respiratoria": 8
        }

        for keyword, score in respiratory_keywords.items():
            if keyword in text:
                respiratory_risk += score
                severity += score * 0.8
                
        cardiac_keywords = {
            "dolor torácico": 5,
            "opresión en el pecho": 5,
            "irradiado al brazo": 6,
            "presión en el pecho": 5,
            "mareos": 2
        }

        for keyword, score in cardiac_keywords.items():
            if keyword in text:
                cardiac_risk += score
                severity += score * 0.7
                
        severe_keywords = {
            "shock séptico": 9,
            "desorientación": 4,
            "pérdida parcial de conciencia": 7,
            "fiebre alta": 3,
            "fatiga extrema": 4
        }

        for keyword, score in severe_keywords.items():
            if keyword in text:
                severity += score
                
        urgency = (
            severity * 0.5 +
            respiratory_risk * 0.3 +
            cardiac_risk * 0.2
        )
        
        return LLMAnalysis(
            severity=self.normalize(severity),
            respiratory_risk=self.normalize(respiratory_risk),
            cardiac_risk=self.normalize(cardiac_risk),
            urgency=self.normalize(urgency)
        )
        
    def normalize(value):
            return min(round(value, 1), 10)