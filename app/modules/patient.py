from dataclasses import dataclass

@dataclass
class Patient:
    id: int

    # Datos básicos
    age: int

    # Signos vitales
    oxygen_saturation: int
    heart_rate: int
    temperature: float

    # Tiempo esperando
    waiting_time: int

    # Texto clínico
    symptoms: str

    # Recursos requeridos
    needs_bed: bool
    needs_ventilator: bool
    doctor_time: int