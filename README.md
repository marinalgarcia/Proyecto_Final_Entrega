# Integrantes

- Marina García
- Eugenia Monserrat 
- Fernando Schvartz

# Funcionalidades de la aplicación
Blog infomativo de Suecia donde se pueden visualizar posteos y excursiones.
Los usuarios de la aplicación logueandose tienen la facultad de crear, borrar o actualizar la aplicación.

# Instalación
Para su correcta instalación se deberá chequear la versión de Python instalada en su ordenador.
Versión de Python utilizada para el desarrollo de la aplicación.

- en *nix:

```bash 
python --version
Python 3.10.6
```
- en windows:
```bash
c:/> python --version
c:/> python 3.10.6
```
# Instalación de dependencias para el correcto funcionamiento de la aplicación
Para instalar las dependencias se deberá utilizar la sentencia pip install.
Paquetes a instalar: ‘whitenoise’ y  ‘pillow’.

- *nix:
```bash
pip install whitenoise
pip install pillow
```
- en windows:
```bash
c:/> pip install whitenoise
c:/> pip install pillow
```
Verificar que los paquetes se instalaron satisfactoriamente.

# Pasos para configurar la aplicación:

## Migración

- en *nix:
```bash
python manage.py migrate
```

- en windows:
```bash
c:/> py manage.py migrate
```

## Correr servidor de prueba

- en *nix:
```bash
python manage.py runserver
```
- en windows:
```bash
c:/> py manage.py runserver
```

Luego ir al http://127.0.0.1:8000/index

Si todo funciona correctamente se podrá ver en el servidor cómo funciona la aplicación.

