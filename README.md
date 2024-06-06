# DocDrive

Aplicación simple para almacenar documentos

## Funcionalidades

- [x] Crear usuarios
- [ ] Editar usuarios
- [ ] Eliminar Usuarios
- [x] Iniciar sesión
- [x] Subir Archivos
- [x] Eliminar Archivos
- [ ] Editar Archivos
- [ ] Compartir Archivos

## Tecnologías

- Django
- Bootstrap
- SQlite

## Instalación & prueba

Acceder al directorio raiz de la aplicación

Crear un entorno virtual e instalar las dependencias:

```
python -m venv env
```

Linux:

```
    source env/bin/activate
```

Window:

```
    env/Scripts/activate
```

Instalar las dependencias

```
    pip install requirementes.txt
```

Migrar la aplicación

```
   cd docdrive
   python manage.py makemigrations
   python manage.py migrate
```

Crear superusuario & ejecutar el servidor

```
    python manage.py createsuperuser
    python manage.py runserver
```

Abrir el navegador en el localhost:8000
