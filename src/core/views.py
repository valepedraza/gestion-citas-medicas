from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Paciente, Medico, Cita
from .forms import PacienteForm, MedicoForm, CitaForm

@login_required
def home(request):
    """Vista del dashboard"""
    context = {
        'total_pacientes': Paciente.objects.count(),
        'total_medicos': Medico.objects.count(),
        'citas_pendientes': Cita.objects.filter(estado='PENDIENTE').count()
    }
    return render(request, 'core/home.html', context)

def paciente_lista(request):
    pacientes = Paciente.objects.all().order_by('apellido')
    return render(request, 'core/pacientes/lista.html', {'pacientes': pacientes})

def paciente_crear(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente creado exitosamente')
            return redirect('core:paciente_lista')
    else:
        form = PacienteForm()
    return render(request, 'core/pacientes/form.html', {'form': form})

def paciente_editar(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente actualizado exitosamente')
            return redirect('core:paciente_lista')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'core/pacientes/form.html', {'form': form})

def paciente_eliminar(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        paciente.delete()
        messages.success(request, 'Paciente eliminado exitosamente')
        return redirect('core:paciente_lista')
    return render(request, 'core/pacientes/eliminar.html', {'paciente': paciente})

def lista_medicos(request):
    """
    Vista que muestra el listado de todos los médicos.
    Permite ver la información profesional de cada médico.
    """
    medicos = Medico.objects.all()
    return render(request, 'core/medicos.html', {'medicos': medicos})

def lista_citas(request):
    """
    Vista que muestra el listado de todas las citas.
    Permite ver las citas programadas y su estado.
    """
    citas = Cita.objects.all()
    return render(request, 'core/citas.html', {'citas': citas})

# Vistas para Médicos
def medico_lista(request):
    medicos = Medico.objects.all().order_by('apellido')
    return render(request, 'core/medicos/lista.html', {'medicos': medicos})

def medico_crear(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Médico creado exitosamente')
            return redirect('core:medico_lista')
    else:
        form = MedicoForm()
    return render(request, 'core/medicos/form.html', {'form': form})

def medico_editar(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Médico actualizado exitosamente')
            return redirect('core:medico_lista')
    else:
        form = MedicoForm(instance=medico)
    return render(request, 'core/medicos/form.html', {'form': form})

def medico_eliminar(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        medico.delete()
        messages.success(request, 'Médico eliminado exitosamente')
        return redirect('core:medico_lista')
    return render(request, 'core/medicos/eliminar.html', {'medico': medico})

# Vistas para Citas
def cita_lista(request):
    citas = Cita.objects.all().order_by('-fecha')
    return render(request, 'core/citas/lista.html', {'citas': citas})

def cita_crear(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cita creada exitosamente')
            return redirect('core:cita_lista')
    else:
        form = CitaForm()
    return render(request, 'core/citas/form.html', {'form': form})

def cita_editar(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cita actualizada exitosamente')
            return redirect('core:cita_lista')
    else:
        form = CitaForm(instance=cita)
    return render(request, 'core/citas/form.html', {'form': form})

def cita_eliminar(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        cita.delete()
        messages.success(request, 'Cita eliminada exitosamente')
        return redirect('core:cita_lista')
    return render(request, 'core/citas/eliminar.html', {'cita': cita})

# Vista de autenticación
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:home')
    return render(request, 'core/auth/login.html')

def logout_view(request):
    logout(request)
    return redirect('core:login')
