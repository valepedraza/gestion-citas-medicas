from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'core'

urlpatterns = [
    # URLs de autenticación
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # URLs de la aplicación
    path('', views.home, name='home'),
    
    # URLs de pacientes
    path('pacientes/', views.paciente_lista, name='paciente_lista'),
    path('pacientes/crear/', views.paciente_crear, name='paciente_crear'),
    path('pacientes/<int:pk>/editar/', views.paciente_editar, name='paciente_editar'),
    path('pacientes/<int:pk>/eliminar/', views.paciente_eliminar, name='paciente_eliminar'),
    
    # URLs de médicos
    path('medicos/', views.medico_lista, name='medico_lista'),
    path('medicos/crear/', views.medico_crear, name='medico_crear'),
    path('medicos/<int:pk>/editar/', views.medico_editar, name='medico_editar'),
    path('medicos/<int:pk>/eliminar/', views.medico_eliminar, name='medico_eliminar'),
    
    # URLs de citas
    path('citas/', views.cita_lista, name='cita_lista'),
    path('citas/crear/', views.cita_crear, name='cita_crear'),
    path('citas/<int:pk>/editar/', views.cita_editar, name='cita_editar'),
    path('citas/<int:pk>/eliminar/', views.cita_eliminar, name='cita_eliminar'),
]
