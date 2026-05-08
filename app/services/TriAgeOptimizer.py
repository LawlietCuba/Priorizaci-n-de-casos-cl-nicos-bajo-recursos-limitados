from app.modules.patient import Patient
from app.modules.LLMAnalysis import LLMAnalysis
from app.services.OptimizationResults import OptimizationResult
from app.modules.HospitalResources import HospitalResources

class TriageOptimizer:

    def optimize(
        self,
        patients: list[Patient],
        analyses: dict[int, LLMAnalysis],
        resources: HospitalResources
    ) -> list[OptimizationResult]:
        pass