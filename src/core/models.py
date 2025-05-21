from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class Usuario(AbstractUser):
    """
    Extensión del modelo de usuario de Django.
    Añade campos específicos para la gestión médica.
    """
    ROL_CHOICES = [
        ('admin', 'Administrativo'),
        ('medico', 'Médico'),
        ('paciente', 'Paciente'),
    ]
    rol = models.CharField(max_length=10, choices=ROL_CHOICES, default='admin')
    telefono = models.CharField(
        max_length=15, 
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')],
        blank=True
    )
    # Agregar: estado del usuario (activo/inactivo)

class Paciente(models.Model):
    """
    Información específica del paciente.
    Incluye datos personales y médicos relevantes.
    """
    nombre = models.CharField(max_length=100)  # Nombre del paciente
    apellido = models.CharField(max_length=100)  # Apellidos del paciente
    dni = models.CharField(max_length=8, unique=True)  # DNI único del paciente
    fecha_nacimiento = models.DateField()  # Fecha de nacimiento del paciente
    telefono = models.CharField(max_length=15)  # Número de contacto
    email = models.EmailField()  # Correo electrónico de contacto

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Medico(models.Model):
    """
    Información profesional del médico.
    Gestiona disponibilidad y especialización.
    """
    nombre = models.CharField(max_length=100)  # Nombre del médico
    apellido = models.CharField(max_length=100)  # Apellidos del médico
    especialidad = models.CharField(max_length=100)  # Especialidad del médico
    numero_colegiado = models.CharField(max_length=20, unique=True)  # Número de colegiado
    email = models.EmailField()  # Correo electrónico del médico

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Cita(models.Model):
    """
    Gestión de citas médicas.
    Relaciona pacientes con médicos e incluye seguimiento.
    """
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('COMPLETADA', 'Completada'),
        ('CANCELADA', 'Cancelada'),
    ]
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    motivo = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PENDIENTE')

    def __str__(self):
        return f"Cita: {self.paciente} con {self.medico} - {self.fecha}"

    class Meta:
        ordering = ['-fecha']
        # Añadir constraint para evitar duplicados
        constraints = [
            models.UniqueConstraint(
                fields=['medico', 'fecha'],
                name='unique_medico_fecha'
            )
        ]
