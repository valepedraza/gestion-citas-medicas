from datetime import datetime, timedelta
from django.db.models import Q

def buscar_citas_disponibles(medico, fecha):
    """Busca horarios disponibles para un médico en una fecha específica"""
    horario_laboral = range(9, 18)  # 9am a 6pm
    citas_existentes = Cita.objects.filter(
        medico=medico,
        fecha__date=fecha
    ).values_list('fecha__hour', flat=True)
    
    return [hour for hour in horario_laboral if hour not in citas_existentes]

def get_proximas_citas(paciente):
    """Obtiene las próximas citas de un paciente"""
    now = datetime.now()
    return Cita.objects.filter(
        paciente=paciente,
        fecha__gte=now,
        estado='PENDIENTE'
    ).order_by('fecha')
