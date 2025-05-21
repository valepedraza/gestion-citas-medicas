# Sistema de Gestión de Citas Médicas

Sistema web desarrollado con Django para la gestión de citas médicas.

## Características

- Gestión de pacientes
- Gestión de médicos y especialidades
- Programación de citas
- Sistema de roles y permisos
- Interfaz responsive

## Tecnologías

- Python 3.8+
- Django 4.2+
- SQLite
- HTML5/CSS3
- JavaScript

## Instalación

1. Clonar el repositorio
```bash
git clone <url-repositorio>
```

2. Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instalar dependencias
```bash
pip install -r requirements.txt
```

4. Ejecutar migraciones
```bash
python manage.py migrate
```

5. Crear superusuario
```bash
python manage.py createsuperuser
```

6. Ejecutar servidor
```bash
python manage.py runserver
```
