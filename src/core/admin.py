from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Paciente, Medico, Cita

admin.site.register(Usuario, UserAdmin)
admin.site.register(Paciente)  # Permite gestionar pacientes desde el admin
admin.site.register(Medico)   # Permite gestionar médicos desde el admin
admin.site.register(Cita)     # Permite gestionar citas desde el admin
