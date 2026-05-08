from app.modules.patient import Patient
from app.modules.LLMAnalysis import LLMAnalysis

class ScoreCalculator:

    def calculate_structured_score(self, patient: Patient) -> float:
        return ((100 - patient.oxygen_saturation) * 0.4 +
                    patient.waiting_time * 0.2 +
                    patient.age * 0.1 +
                    patient.heart_rate * 0.3)

    def calculate_llm_score(self, analysis: LLMAnalysis) -> float:
        return (
            analysis.severity * 0.4 +
            analysis.respiratory_risk * 0.3 +
            analysis.cardiac_risk * 0.3 +
            analysis.urgency * 0.1
)

    def calculate_final_score(
        self,
        patient: Patient,
        analysis: LLMAnalysis
    ) -> float:
        return(
            self.calculate_structured_score(self, patient=patient) * 0.6 +
            self.calculate_llm_score(self, analysis=analysis) * 0.4
)