## Introducción

Este proyecto es una aplicación web desarrollada en Django que permite gestionar turnos, base de datos de pacientes, y notificaciones a los pacientes entre otras cosas. Incluye funcionalidades especiales para administradores, pero también para usuarios, pudiendo filtrar sus funcionalidades según especificaciones del administrador.

## Requisitos del Sistema

- Python 3.x
- SQLite3 (por defecto)
- celery 5.4.0
- Django 5.0.6
- django-allauth 0.63.3
- django-celery 3.1.17
- django-celery-beat 2.6.0
- django-timezone-field 7.0
- djlint 1.34.1
- pillow 10.3.0
- pytz 2024.1
- twilio 9.2.3
- Navegador web moderno

Funcionalidades generales
Lista las principales funcionalidades del proyecto y cómo acceder a ellas.

-Inicio: Acceder a la página principal del proyecto.
URL: /

-Nosotros: Ver información sobre la App
URL: /about/

-Pacientes: aca figuran los pacientes registrados, con sus detalles, archivos cargados y su historial.
-Usuarios:

Funcionalidades de Administrador
El proyecto incluye una interfaz de administrador que permite gestionar los datos del sistema de forma sencilla. Tambien nos permite navegar como administrar por la pagina comunmente si usamos el login, y hacer cambios desde ahi.
   Acceso al Administrador
   -URL de administración del proyecto: http://localhost:8000/admin/.
   -Ingresar credenciales de superusuario para acceder al panel de administración.

   Funcionalidades Disponibles
   -Paciente: Permite administrar los productos y castegorías disponibles en el sistema
   -Usuarios: Permite gestionar los usuarios registrados en el sistema y ver su información (NO DISPONIBLE)
   -Clientes: Permite gestionar los clientes registrados en el sistema y ver su información
   -Turnos: Permite gestionar los turnos de los pacientes registrados.


   Acceso al Panel de Administración
   -El panel de administración se puede acceder mediante la URL /admin/ del proyecto.

   Credenciales de Superusuario
   Las credenciales predeterminadas del superusuario son:

   -Usuario: admin
   -Contraseña: [123]

estructura del proyecto:

AlejoPardini/
├── manage.py
├── db.sqlite3
├── config/
│   ├── settings.py
│   ├── __init__.py
│   ├── asgi.py
│   ├── wsgi.py
│   ├── urls.py
│   └── views.py
│
├── core/
│   ├── admin.py
│   ├── apps.py
│   ├── urls.py
│   ├── models.py
│   ├── __init__.py
│   ├── tests.py
│   ├── views.py
│   ├── forms.py
│   ├── migrations/
│   └── static/core
│   │      └── css/
│   │      │    ├── producto_styles.css
│   │      │    ├── styles.css
│   │      │    ├── titulo_styles.css
│   │      │    └── usuarios_styles.css
│   │      ├── assets
│   │      │    └── favicon.ico
│   │      ├── img
│   │      │    ├── cervezas.webp
│   │      │    ├── nosotros.png
│   │      │    ├── picada.png
│   │      │    ├── quesos.png
│   │      │    ├── tigre.png
│   │      │    └── tigreblanco.png
│   │      └── js
│   │           └── scripts.js
│   └── templates/core
│           ├── components
│           │    ├── card.html
│           │    ├── card2.html
│           │    ├── card3.html
│           │    ├── card4.html
│           │    ├── footer.html
│           │    ├── navbar.html
│           │    └── titulo1.html
│           ├── about.html
│           ├── base.html
│           ├── login.html
│           ├── logout.html
│           ├── producto.html
│           ├── register.html
│           └── index.html
├── producto/
│   ├── admin.py
│   ├── apps.py
│   ├── urls.py
│   ├── models.py
│   ├── __init__.py
│   ├── tests.py
│   ├── views.py
│   ├── forms.py
│   ├── migrations/
│   └── templates/producto
│           ├── cervezas.html
│           ├── editar_producto.html
│           ├── gin.html
│           ├── producto_confirm_delete.html
│           ├── producto_detail.html
│           ├── producto_form.html
│           ├── producto_list.html
│           ├── productocategoria_confirm_delete.html
│           ├── productocategoria_detail.html
│           ├── productocategoria_form.html
│           ├── productocategoria_list.html
│           ├── productocategoria_update.html
│           ├── quesos.html
│           └── promociones.html
└── usuario/
    ├── migrations/
    ├── admin.py
    ├── apps.py
    ├── urls.py
    ├── models.py
    ├── __init__.py
    ├── tests.py
    ├── views.py
    ├── forms.py
    └── templates/usuario
            ├── editar_perfil.html
            ├── perfil_actualizado.html
            └── index.html
    
