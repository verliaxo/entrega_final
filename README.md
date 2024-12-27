# Entrega Final Coder - Página para publicar productos

# Integrantes del grupo 

- Nicole Ferreyra - creación de la app usuarios, sus modelos, formularios y plantillas
- Luca Muriel - creación de la app pagina (la que maneja productos), sus modelos, formularios y plantillas.

- A través del uso de la aplicación 'Parsec', entre los dos integramos las aplicaciones para que cada usuario pueda manejar sus propios productos.

# Instalación

1. Clonar el repositorio 
2. Abrir una terminal e instalar el entorno virtual con el comando: python -m venv .venv
3. Seleccionar el entorno virtual con el comando: ./.venv/scripts/activate
4. Cambiar el interprete al del entorno virtual.
5. Seleccionar la carpeta del proyecto: cd entrega_final
6. Instalar las dependencias con: pip install -r requirements.txt
7. Realizar las migraciones: 
- python manage.py makemigrations usuarios
- python manage.py makemigrations pagina
- python manage.py migrate
8. Ejecutar el servidor e ir a http://127.0.0.1:8000/ en el navegador.

# Descripción de la Página

- En esta página, una vez registrado y logeado, un usuario tiene acceso a una pestaña que le permite ingresar productos los cuales seran publicados en un listado que puede acceder cualquier persona, ya sea que este logeado o no.
- Estos productos pueden ser modificados unicamente por el dueño o por un administrador a través del panel de admin.
- Cada usuario puede acceder a su perfil el cual puede modificar a su gusto, agregando una foto de perfil o una descripción, y también puede visualizar los perfiles de otros usuarios a través de la lista de usuarios.

- Para acceder al panel de administración, acceder al enlace http://127.0.0.1:8000/admin/ habiendo previamente creado un superuser en la terminal.

# Video demostrativo y casos de prueba
El archivo 'casos de prueba.xlsx' contiene los casos de prueba que se probaron para esta aplicación

Video demostrativo: https://www.youtube.com/watch?v=ZOiTAErjqoU