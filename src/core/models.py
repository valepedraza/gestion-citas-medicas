from django.db import models
from django.contrib.auth.models import AbstractUser

class Rol(models.Model):
    """
    Modelo para gestionar los roles de usuario en el sistema.
    Define los diferentes tipos de acceso y permisos.
    """
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()
    # Agregar: permisos específicos del rol

    def __str__(self):
        return self.nombre

class Usuario(AbstractUser):
    """
    Extensión del modelo de usuario de Django.
    Añade campos específicos para la gestión médica.
    """
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT)
    telefono = models.CharField(
        max_length=15, 
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')],
        blank=True
    )
    # Agregar: estado del usuario (activo/inactivo)

class Especialidad(models.Model):
    """
    Catálogo de especialidades médicas disponibles.
    Permite organizar a los médicos por área.
    """
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)
    # Agregar: requisitos específicos de la especialidad

    def __str__(self):
        return self.nombre

class EstadoCita(models.Model):
    """
    Define los posibles estados de una cita médica.
    Incluye representación visual mediante colores.
    """
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()
    color = models.CharField(max_length=7)  # Formato: #RRGGBB

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    """
    Información específica del paciente.
    Incluye datos personales y médicos relevantes.
    """
<<<<<<< HEAD
    nombre = models.CharField(max_length=100)  # Nombre del paciente
    apellido = models.CharField(max_length=100)  # Apellidos del paciente
    dni = models.CharField(max_length=8, unique=True)  # DNI único del paciente
    fecha_nacimiento = models.DateField()  # Fecha de nacimiento del paciente
    telefono = models.CharField(max_length=15)  # Número de contacto
    email = models.EmailField()  # Correo electrónico de contacto

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
=======
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    dni = models.CharField(
        max_length=8,
        unique=True,
        validators=[RegexValidator(regex=r'^\d{8}$')]
    )
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    alergias = models.TextField(blank=True)
    antecedentes = models.TextField(blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    # Agregar: grupo sanguíneo, contacto de emergencia

    def __str__(self):
        return f"{self.usuario.get_full_name()} - DNI: {self.dni}"
>>>>>>> 9f9077e (feat: Implementación inicial del sistema de citas médicas)

class Medico(models.Model):
    """
    Información profesional del médico.
    Gestiona disponibilidad y especialización.
    """
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.PROTECT)
    numero_colegiado = models.CharField(max_length=20, unique=True)
    horario_consulta = models.TextField()
    disponible = models.BooleanField(default=True)
    # Agregar: días no laborables, duración consulta

    def __str__(self):
        return f"Dr. {self.usuario.get_full_name()} - {self.especialidad}"

class HorarioMedico(models.Model):
    """Gestión detallada de horarios médicos"""
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    dia_semana = models.IntegerField(choices=[(i, day) for i, day in enumerate(['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'])])
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    duracion_consulta = models.IntegerField(help_text='Duración en minutos')

class Cita(models.Model):
    """
    Gestión de citas médicas.
    Relaciona pacientes con médicos e incluye seguimiento.
    """
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    estado = models.ForeignKey(EstadoCita, on_delete=models.PROTECT)
    fecha = models.DateTimeField()
    motivo = models.TextField()
    diagnostico = models.TextField(blank=True)
    prescripcion = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
