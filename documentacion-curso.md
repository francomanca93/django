
<div align="center">
    <h1>Django</h1>
    <img src="https://imgur.com/lZXrh04.png" width="">
</div>

## Introducción al documento

El contenido de este documento es **proyeco web llamado Platzigram** un **clon de Instagram** del [Curso de Django](https://platzi.com/cursos/django/). El mismo está dictado por [Pablo Trinidad](https://twitter.com/_pablotrinidad) CS student at UNAM’s Facultad de Ciencias and Coach en Major League Hacking. El curso es de [Platzi](https://platzi.com).

Con Django podemos crear sitios web fácilmente. Aprenderemos sobre la conectividad y la extensibilidad que ofrecen los componentes de Django: el framework de desarrollo Web para Python más usado en la actualidad.

## Objetivos del documento

- Crea una app web con Django
- Usar el ORM de Django
- Usar class based views
- Conocer el sistema de templates
- Personalizar el administrador de Django

## Tabla de contenido
- [Curso de Django](#curso-de-django)
  - [1. Introducción](#1-introducción)
    - [Introducción al curso](#introducción-al-curso)
    - [Historia de web development](#historia-de-web-development)
      - [Resumen](#resumen)
      - [Django](#django)
    - [Preparacion del entorno](#preparacion-del-entorno)
    - [Estructura de archivos](#estructura-de-archivos)
    - [Hola, mundo! en Django](#hola-mundo-en-django)
  - [2. Vistas](#2-vistas)
  - [3. Models](#3-models)
  - [4. Templates, auth y middlewares](#4-templates-auth-y-middlewares)
  - [5. Forms](#5-forms)
  - [6. Class-based views](#6-class-based-views)
  - [7. Deployment](#7-deployment)
  - [8. Bonus](#8-bonus)

# Curso de Django

## 1. Introducción

### Introducción al curso

El objetivo de este curso es que conozcas Python y Django y los consideres como una herramienta útil para el desarrollo de tus proyectos.

El proyecto que estaremos desarrollando será Platzigram.

### Historia de web development

#### Resumen

Al inicio de la web todo era **texto plano (HTML)**, al transcurrir del tiempo se necesitaban cosas más complejas como conexión a **BD’s** y de ahi nace **CGIscript** (CGI Scripts Common Gateway Interface (Interfaz de entrada común)).

**[CGIscript](https://es.wikipedia.org/wiki/Interfaz_de_entrada_com%C3%BAn)** nace con el objetivo de que a través de un request, se ejecute un script dentro del servidor, pero esto fue generando problemas con la escabilidad, y por ende difícil de mantener, de esta necesidad nace **PHP**.

Luego nacen los **frameworks** para poder resolver tareas comunes, como:

- Protocolos HTTP.
- Conexiones a bases de datos.
- Interacciones con el HTML(templates).

#### Django

**[Django](https://www.djangoproject.com/)** nace en 2003, con la necesidad de hacer web’s con la filosofía de hacer las cosas de manera agíl.

- Poder hacer sitios escalables.
- URLs bien diseñadas.
- HTTP request y responses.
- ORM, que es conectar a na DB a traves de una interfaz python. (ORM Object-Relational mapping (Mapeo objeto relacional)).

Características.

- Rápido desarrollo.
- Listo para todo. Tiene herramientas previas como la autenticación de usuarios, administración de contenidos, mapas de sitios, etc.
- Es seguro, ya que tiene en cuenta los errores comunes de los developers como [SQL Injection](https://www.w3schools.com/sql/sql_injection.asp), [Cross-site Scripting](https://es.wikipedia.org/wiki/Cross-site_scripting), [Cross-site Request Forgery ‘CSRF’](https://es.wikipedia.org/wiki/Cross-site_request_forgery), [Clickjacking](https://es.wikipedia.org/wiki/Clickjacking).
- Versátil.

Ventajas

- Es desarrollado en Python.
- DRY(Don’t repeat yourself).
- Comunidad Open Source.

### Preparacion del entorno

Los entornos virtuales nos permiten isolar multiples dependencias para el desarrollo de proyecto, puede pasar por ejemplo cuando trabajas con diferentes versiones de python o de django.

Python 3 trae la creación y manejo de entornos virtuales como parte del modulo central.

Entorno virtual con Python

Para crear un entorno virtual utilizas:

```shell
python3 -m venv .env
```

Nota: .env es el nombre de del ambiente

Para activarlo:

```shell
source -m ./.env/bin/activate
```

Si queremos desactivarlo:

```shell
deactivate
```

Si deseamos ver las librerías instaladas en el ambiente:

```shell
pip freeze
```

Instalacion de Django
Para instalar Django en su ultima version usamos:

```shell
pip install django -U
```

### Estructura de archivos

- El archivo vacío **__ init __.py** indica que la carpeta es un módulo de python.
- El archivo **settings.py** define todas las configuraciones del proyecto.
  - **BASE_DIR**: Define la ubicación donde se está corriendo el proyecto.
  - **SECRET_KEY**: Es usado para el hashing de las contraseñas y las sesiones que se almacenan en la BD.
  - **DEBUG**: Define si el proyecto está en desarrollo para realizar debugging.
  - **ALLOWED_HOSTS**: Define que hosts están permitidos para que interactuen en nuestro proyecto.
  - **INSTALLED_APPS**: Aplicaciones ligadas al proyecto. Por defecto agrega la app de administrador, autenticación, contentypes (conexión a la BD), sesiones, mensajes y archivos estáticos.
  - **MIDDLEWARE**: Software que se sitúa entre un sistema operativo y las aplicaciones que se ejecutan en él
  - **ROOT_URLCONF**: Ubicación del principal de urls.
  - **TEMPLATES**:
  - **WSGI_APPLICATION**: Ubicación del principal de deployment.
  - **DATABASES**: Configuración y conexión a la BD.
  - **AUTH_PASSWORD_VALIDATORS**: Validadores de contraseñas. Si se está usando la app de autenticación, que la contraseña pase por las validaciones definidas:
    - Los valores de la contraseña no sean similares a los valores del usuario.
    - Que tenga una mínima longitud.
    - Validar la contraseña con un diccionario de contraseñas comunes.
    - Que la contraseña no sea numérica.
  - **LANGUAGE_CODE**: Lenguaje o idioma que está utilizando la aplicación.
  - **TIME_ZONE**: Se define el sistema horario en donde está corriendo la aplicación.
  - **USE_I18N**: Librería para traducción de textos.
  - **USE_L10N**: Librería para traducción de textos.
  - **USE_TZ**: Librería de timezone.
  - **STATIC_URL**: Define la ubicación de los archivos estáticos como css, js, img.

- El archivo **urls.py** define el punto de entrada para todas las peticiones que lleguen al proyecto.
- El archivo **wsgi.py** es utilizado para el deployment a producción.
- El archivo **manage.py** es uno que no se debe tocar y permite ejecutar todos los comandos que se hayan definido en las applicaciones instaladas del proyecto (entre ellas las del comando django-admin).

> Cuando se ejecuta `python3 manage.py` por cada [nombre_app] se visualizarán los diferentes comandos que se pueden ejecutar por cada aplicación instalada del proyecto (auth, contenttypes, django, sessions, staticfiles).

### Hola, mundo! en Django

Iniciamos server:

```shell
python3 manage.py runserver

# url:
# http://127.0.0.1:8000
```

En el archivo urls.py creamos una funcion para el objetivo y modificamos el urlpatterns:

```py
from django.http import HttpResponse

def hello_word(request):
    """ Return a geeting"""
    return HttpResponse('Hello, World!. Hi Franco')

urlpatterns = [
    path('hello-word/', hello_word)
]
```

Nos vamos a la url server:

```shell
http://127.0.0.1:8000/hello-word/
```

## 2. Vistas

## 3. Models

## 4. Templates, auth y middlewares

## 5. Forms

## 6. Class-based views

## 7. Deployment

## 8. Bonus
