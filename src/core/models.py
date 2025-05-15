from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class Usuario(AbstractUser):
    ROLES = (
        ('admin', 'Administrativo'),
        ('medico', 'Médico'),
        ('paciente', 'Paciente'),
    )
    rol = models.CharField(max_length=10, choices=ROLES, default='admin')
    
    class Meta:
        db_table = 'core_usuario'

class Paciente(models.Model):
    """
    Modelo para representar a los pacientes en el sistema.
    Almacena la información personal básica de cada paciente.
    """
    nombre = models.CharField(max_length=100)  # Nombre del paciente
    apellido = models.CharField(max_length=100)  # Apellidos del paciente
    dni = models.CharField(max_length=8, unique=True)  # DNI único del paciente
    fecha_nacimiento = models.DateField()  # Fecha de nacimiento del paciente
    telefono = models.CharField(max_length=15)  # Número de contacto
    email = models.EmailField()  # Correo electrónico de contacto
    direccion = models.CharField(max_length=200, blank=True)  # Dirección del paciente
    historial_medico = models.TextField(blank=True)  # Historial médico del paciente
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación del registro
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de última actualización

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def get_edad(self):
        from datetime import date
        today = date.today()
        return today.year - self.fecha_nacimiento.year

class Medico(models.Model):
    """
    Modelo para representar a los médicos en el sistema.
    Almacena la información profesional de cada médico.
    """
    nombre = models.CharField(max_length=100)  # Nombre del médico
    apellido = models.CharField(max_length=100)  # Apellidos del médico
    especialidad = models.CharField(max_length=100)  # Especialidad médica
    numero_colegiado = models.CharField(max_length=20, unique=True)  # Número de colegiado único
    email = models.EmailField()  # Correo electrónico profesional

    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido} - {self.especialidad}"

class Cita(models.Model):
    """
    Modelo para gestionar las citas médicas.
    Relaciona pacientes con médicos y almacena la información de la cita.
    """
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('COMPLETADA', 'Completada'),
        ('CANCELADA', 'Cancelada'),
    ]

    # Relaciones con otros modelos
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)  # Paciente que solicita la cita
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)  # Médico que atenderá la cita
    
    # Campos de la cita
    fecha = models.DateTimeField()  # Fecha y hora de la cita
    motivo = models.TextField()  # Motivo o descripción de la cita
    estado = models.CharField(
        max_length=20, 
        choices=ESTADO_CHOICES, 
        default='PENDIENTE'
    )  # Estado actual de la cita

    def __str__(self):
        return f"Cita: {self.paciente} con {self.medico} - {self.fecha}"
