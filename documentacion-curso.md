
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
      - [Levantar servicio](#levantar-servicio)
      - [Crear la primera vista](#crear-la-primera-vista)
  - [2. Vistas](#2-vistas)
    - [El objeto Request](#el-objeto-request)
      - [Como Django procesa un request](#como-django-procesa-un-request)
      - [Separando las vistas](#separando-las-vistas)
      - [El objeto Request](#el-objeto-request-1)
      - [Reto: Crear una vista y su URL. Regresar lista en formato JSON](#reto-crear-una-vista-y-su-url-regresar-lista-en-formato-json)
    - [Pasando argumentos por URL](#pasando-argumentos-por-url)
    - [Creación de la primera app](#creación-de-la-primera-app)
    - [Template system](#template-system)
      - [Pasando datos a nuestro template](#pasando-datos-a-nuestro-template)
    - [Patrones de diseño y Django](#patrones-de-diseño-y-django)
      - [Model](#model)
      - [Template](#template)
      - [View](#view)
  - [Models: Una práctica desde 0](#models-una-práctica-desde-0)
    - [Models: La M en el MTV](#models-la-m-en-el-mtv)
      - [Implementar y hacer cambios de modelo](#implementar-y-hacer-cambios-de-modelo)
    - [El ORM de Django](#el-orm-de-django)
    - [Extendiendo el modelo de usuario](#extendiendo-el-modelo-de-usuario)
  - [3. Models](#3-models)
    - [Configuración básica](#configuración-básica)
      - [Creacion de Super Usuario](#creacion-de-super-usuario)
      - [Dashboard de Administración](#dashboard-de-administración)
    - [Implementación del modelo de usuarios de Platzigram](#implementación-del-modelo-de-usuarios-de-platzigram)
      - [Implementación de modelos](#implementación-de-modelos)
      - [Implementar modelos en base de datos](#implementar-modelos-en-base-de-datos)
    - [Explorando el dashboard de administración](#explorando-el-dashboard-de-administración)
      - [Reflejar modelos en dashboard de administración](#reflejar-modelos-en-dashboard-de-administración)
      - [Dashboard administrativo personalizado](#dashboard-administrativo-personalizado)
    - [Personalizando Dashboards Nativos](#personalizando-dashboards-nativos)
    - [Relacionando modelos](#relacionando-modelos)
    - [Hacer funcionar los links de medias en desarollo](#hacer-funcionar-los-links-de-medias-en-desarollo)
    - [RETO: Crea el modelo de posts y regístralo en el admin](#reto-crea-el-modelo-de-posts-y-regístralo-en-el-admin)
  - [4. Templates, auth y middlewares](#4-templates-auth-y-middlewares)
    - [Archivos estáticos](#archivos-estáticos)
    - [Templates](#templates)
    - [Login | Protegiendo vistas](#login--protegiendo-vistas)
    - [Logout](#logout)
    - [Signup](#signup)
    - [Middlewares](#middlewares)
  - [5. Forms](#5-forms)
    - [Formularios en Django](#formularios-en-django)
    - [Mostrando el form en el template](#mostrando-el-form-en-el-template)
    - [Model forms](#model-forms)
    - [Validación de formularios](#validación-de-formularios)
      - [Agregaremos enlace hacia signup en la vista login](#agregaremos-enlace-hacia-signup-en-la-vista-login)
      - [Forma mas facil de trabajar con los templates](#forma-mas-facil-de-trabajar-con-los-templates)
      - [Aprendiendo a validad campos de un formulario](#aprendiendo-a-validad-campos-de-un-formulario)
  - [6. Class-based views](#6-class-based-views)
    - [Simple Class-based views](#simple-class-based-views)
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

#### Levantar servicio

```shell
python3 manage.py runserver

# url:
# http://127.0.0.1:8000
```

#### Crear la primera vista

En el archivo **urls.py** importamos **django.http.HttpResponse** y definimos una **funcion** que devuelva una respuesta (en este caso hello_world), y modificamos el urlpatterns. Establemos en que path estara esta despuesta:

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

### El objeto Request

#### Como Django procesa un request

[How Django processes a request](https://docs.djangoproject.com/en/2.0/topics/http/urls/#how-django-processes-a-request)

1. Primero va a buscar en el archivo **settings.py** en la variable **ROOT_URLCONF**.
2. Luego Django desde el archivo **urls.py** carga los modulos de Python definidos en la variable **urlpatterns**.
3. Dentro de **urlpatterns** se busca el patron coincidente a la peticion.
4. Una vez encontrado la URL que coincide, Django importa y llama la vista en una funcion simple en Python. Se le pasa como argumento:
    - Una instancia del HttpRequest.
    - Si la URL pasa mas argumentos entonces los entregara.
    - Si definimos argumentos adicionales tambien lo enviara.
5. Si ninguna URL coincide, Django enviara una excepción.

#### Separando las vistas

Es buena practica tener las vistas separadas del archivo url.py, por lo que crearemos un archivo **views.py** dentro de nuestra aplicación que contendra las vistas:

![views](https://imgur.com/5nyzbba.png)

Dentro de nuestro archivo **views.py** importamos **HttpResponse** y traemos nuestra funcion **hello_world()** creado en urls.py

```py
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hello, world!')
```

Ahora debemos importar nuestra funcion al archivo **urls.py**.
No olvidemos **borrar** la importacion de HttpResponse y la funcion hello_world() en el archivo.

```py
from django.contrib import admin
from django.urls import path
from platzigram import views

urlpatterns = [
    path('hello-world/', views.hello_world)
]
```

Si revisamos la url [**http://localhost:8000/hello-world**](http://localhost:8000/hello-world) nuestro proyecto seguira funcionando.

#### El objeto Request

A traves del objeto request podemos acceder a varios atributos  los cuales se encuentran detallados en la [documentación](https://docs.djangoproject.com/en/3.0/ref/request-response/) de Django. Algunos atributos utiles son:

- **request.method:** nos muestra el metodo HTTP ("GET", "POST", etc.) usado por el request en formato de string en UPPERCASE. Un ejemplo de uso seria:

  ```py
  if request.method == 'GET':
    do_something()
  elif request.method == 'POST':
    do_something_else()
  ```

- **request.GET:** Un diccionario que contiene todos los parametros entregados por HTTP GET. Por ejemplo:

Pasamos una lista de numeros en la variable numbers **(?numbers)**

```http
http://127.0.0.1:8000/hi/?numbers=10,4,50,36  
```

Para acceder a la lista usamos:

```py
request.GET['numbers']
```

>*Nota: En el siguiente ejemplo se creo la vista numbers*
  
Un ejemplo practico seria:

```py
def numbers(request):
    """ Numbers."""
    numbers = request.GET['numbers']
    return HttpResponse(f'Hi! Franco. Numeros de la URL: {str(numbers)}')
```

  De esta forma podemos ver los valores de number a traves de nuetra vista.

#### Reto: Crear una vista y su URL. Regresar lista en formato JSON

Reto de la clase: Crea una vista y su respectiva URL en la que recibas números y hagas operaciones con ellos.
Regresa la lista ordenada de números en formato json.

En views.py:

```py
import json

def numbers(request):
    """ Numbers."""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted succesfully.'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json')

```

En urls.py:

```py
from platzigram import views

urlpatterns = [
    path('numbers/', views.numbers)
]
```

### Pasando argumentos por URL

Podemos pasar argumentos a traves de la URL, para esto primero creamos la funcion que hara uso de estos parametros y devolvera la vista en el archivo **views.py**

```py
def say_hi(request, name, age):
    """ Return a greeting"""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}: Welcome to Platzigram'.format(name)
    return HttpResponse(message)
```

Luego definimos el path para esta vista en el archivo **urls.py**. Para definir los parametros que pasaran por la url los encerramos con "<>" definiendo el tipo de dato y el nombre del parametro.

```py
from django.contrib import admin
from django.urls import path
from platzigram import views

urlpatterns = [
  path('hi/<str:name>/<int:age>/', views.say_hi)
]
```

En el resultado final si ingresamos **age = 8** y **name = Franco** obtenemos el resultado definido en nuestra funcion **say_hi()**:

![franco_age_8](https://imgur.com/KAxcee4.png)

Si al resultado final si ingresamos **age = 27** y **name = Franco** obtenemos el resultado definido en nuestra funcion **say_hi()**:

![franco_age_27](https://imgur.com/5kU8P5X.png)

### Creación de la primera app

Con Django podemos crear una app de forma rapida y sencilla ejecutando el comando

```shell
python manage.py startapp name
```

En este ejemplo creamos un app llamada **posts**, el cual genero una carpeta con todos los archivos basicos necesarios:

![posts_folder_app](https://imgur.com/eYXSCNk.png)

Para desplegar una vista de esta aplicacion vamos al archivo *./posts/views.py* donde crearemos una vista a traves de la funcion **list_posts()**

```py
""" Posts views."""

# Django
from django.shortcuts import HttpResponse

# Utilities
from datetime import datetime

posts = [
    {
      'name': 'Mont Blac',
      'user': 'Franco Manca',
      'timestamp': datetime.now().strftime("%b %dth, %Y - %H:%M hrs"),
      'picture': 'https://picsum.photos/id/237/200/200',
    },
    {dict_2_con_datos_del_post},
    {dict_3_con_datos_del_post},
    {dict_4_con_datos_del_post},
]

def list_posts(request):
    """list existing posts"""
    content=[]
    for post in posts:
        content.append("""
        <p><strong>{name}</strong></p>
        <p><small>{user} - <i>{timestamp}</i></small></p>
        <figure><img src="{picture}"/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))
```

Luego vamos al archivo settings de nuestro proyecto, en este caso *./platzigram/settings.py* donde incorporaremos en la variable **INSTALLED_APPS** nuestra nueva app

```py
INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin', . . .
    .
    .
    .

    # Local apps
    'posts',
]
```

Ahora nos toca asignar un path para nuestra vista **list_posts()**. Para eso vamos al archivo **urls.py** de nuestro proyecto, en este caso *./photogram/urls.py* e importamos nuestra nueva app, y le asignamos un path a nuestra vista.

Para que no existan conflictos al llamar views vamos asignar un **alias** para las views de cada aplicacion.

```py
# Importamos las vistas de nuestra aplicacion posts
from posts import views as posts_views

urlpatterns = [
    # Asignamos el path para nuestra vista list_posts
    path('posts/', posts_views.list_posts),
]
```

Ahora vamos a [**http://localhost:8000/posts/**](http://localhost:8000/posts/) para ver nuestro resultado:

![post](https://imgur.com/yyz4BK7.png)

### Template system

El template system es una manera de mostrar los datos usando HTML, incluye lógica de programacion lo cual nos facilita un poco el crear nuestros templates.

Para crear nuestros templates lo que haremos es dentro de nuestra aplicacion **crear una carpeta templates** y un **archivo html** con el nombre de nuestro template, en este caso _feed.html_

![feed](https://imgur.com/qzYy8ZO.png)

Dentro de nuestro archivo **feed.html** solo escribiremos:

```html
Hola, mundo!
```

Y dentro de **views.py** de nuestra aplicación ya no es necesario el HttpResponse, por que borramos su importación. A través de la función que devolvemos nuestra vista devolveremos nuestro nuevo template con el metodo **render**, que le pasaremos la request y la vista:

```py
from django.shortcuts import render

def list_posts(request):
    return render(request, 'feed.html')
```

Si revisamos el path [**http://localhost:8000/posts/**](http://localhost:8000/posts/) tendremos nuestro "Hola, mundo!"

¿Como logro funcionar si dentro de render jamas definimos la ruta donde buscar nuestro template? (en nuetro caso solo _feed.html_). Si revisamos en el archivo **settings.py** de nuestro proyecto, en la definicion de **TEMPLATES** veremos:

```py
...

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

...

```

En **APP_DIRS** lo tenemos definido como **True**, esto significa que las aplicaciones buscaran los templates dentro de sus directorios, de esta forma funciona sin tener que nombrar la dirección de nuestro template.

#### Pasando datos a nuestro template

Primero crearemos un diccionario de datos dentro de nuestra vista (solo a modo de ejemplo) y enviaremos al template estos datos a traves del render. En nuestro caso este diccionario sera posts

```py
# Django
from django.shortcuts import render

# Utilities
from datetime import datetime

posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]

def list_posts(request):
    """List existing posts."""
    return render(request, 'feed.html', {'posts': posts})
```

Si logran observar enviamos los datos a traves de **{'posts': posts}**, el cual el **primer parametro sera el nombre de la variable** al momento de enviar al template, y el **segundo es el valor asignado**.

En nuestro template _feed.html_ ahora imprimiremos nuestro diccionario escribiendo el **nombre de la variable**.

```html
{{ posts }}
```

Si revisamos [**http://localhost:8000/posts/**](http://localhost:8000/posts/) veremos nuestro diccionario.

Ahora juguemos un poco con la **lógica de programación** y **html**. Vamos a imprimir solo los títulos. Para eso en nuestro **template** _feed.html_ escribiremos:

```html
{% for post in posts %}
  <p>{{ post.title }}</p>
{% endfor %}
```

Y el resultado en [**http://localhost:8000/posts/**](http://localhost:8000/posts/)

![logica_y_html](https://imgur.com/JhIVeE5.png)

Para ver toda la **lógica de programación** que podemos crear en el template system te recomiendo ir a la [documentación de Django.](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/)

Ahora despleguemos los datos de nuestro diccionario y estilemos con **Bootstrap** nuestro template _feed.html_.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Platzigram</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
</head>
<body>
    <br><br>
    <div class="container">
        <div class="row">
            {% for post in posts %}
            <div class="col-lg-4 offset-lg-4">
                <div class="media">
                    <img class="mr-3 rounded-circle" src="{{ post.user.picture }}" alt="{{ post.user.name }}">
                    <div class="media-body">
                        <h5 class="mt-0">{{ post.user.name }}</h5>
                        {{ post.timestamp }}
                    </div>
                </div>
                <img class="img-fluid mt-3 border rounded" src="{{ post.photo }}" alt="{{ post.title }}">
                <h6 class="ml-1 mt-1">{{ post.title }}</h6>
            </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>

```

Y en [**http://localhost:8000/posts/**](http://localhost:8000/posts/) veremos
:

![pantalla](https://imgur.com/ffyFMgo.gif)

### Patrones de diseño y Django

Un patrón de diseño, en términos generales, es una solución reutilizable a un problema común.

El patrón más común para el desarrollo web es MVC (Model, View, Controller). Django implementa un patrón similar llamado MTV (Model, Template (plantilla), View).

![mtv](https://imgur.com/37Ornu6.png)

#### Model

Es la forma en la que creamos esquemas de objetos (un usuario, un post, etc) para representarlos en nuestra base de datos.

El modelo sin importar nuestro sistema de BD (mysql, postgress, etc) nos ayudara a crear esta entidad a través de un OMR, esto nos ahorra la molestia de tener que escribir las sentencias de SQL para crear las tablas y atributos.

#### Template

Es el encargado de manejar la lógica y sintaxis de la información que se va a presentar en el cliente, el sistema de templates de django usa HTML para ello.

#### View

Su función es solo suministrar datos al template

Manda la información necesaria el template para que este pueda manejar los datos y presentarlos de una manera correcta.

![mtv_2](https://imgur.com/JqyXBvU.png)

## Models: Una práctica desde 0

### Models: La M en el MTV

[Documentacion Django: Configuración de la base de datos](https://docs.djangoproject.com/es/3.0/intro/tutorial02/)

El Modelo en Django usa diferentes opciones para conectarse a múltiples bases de datos relacionales, entre las que se encuentran: **SQLite, PostgreSQL, Oracle y MySQL**.
Para la creación de tablas, Django usa la técnica del ORM (Object Relational Mapper), una abstracción del manejo de datos usando OOP.

Las migraciones son la manera en la cual podemos propagar los cambios de nuestros modelos a la base de datos, esto nos ahorra la necesidad de hacer cambios directamente en nuestro gestor de base de datos.

#### Implementar y hacer cambios de modelo

> NOTA: Lo que hagamos aca es prueba para saber como funciona unicamente. A partir de la sección [Extendiendo el modelo de usuario](#extendiendo-el-modelo-de-usuario) haremos las cosas como corresponde.

Guía de tres pasos para hacer cambios de modelo:

1. Cambie sus modelos (en models.py).

Ejemplo:

```py

""" Posts models."""

# Django
from django.db import models


class User(models.Model):
    """ User Model."""

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    bio = models.TextField(blank=True)

    birthdate = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

```

2. Ejecute el comando `python manage.py makemigrations` para crear migraciones para esos cambios
3. Ejecute el comando `python manage.py migrate` para aplicar esos cambios a la base de datos.

### El ORM de Django

> *Veremos: Como insertar datos en el modelo creado anteriormente, como hacer consultas y como hacer filtros*.

Podemos abrir la terminar de Django: `python3 manage.py shell` y escribir lo siguiente:

```shell

>>> franco = User.objects.create(
...      email='hola@gmail.com',
...      password='123456',
...      first_name='Franco',
...      last_name='Manca'
... )
>>> franco.email
'hola@gmail.com'
>>> franco.id
1
>>> franco.pk
1
>>> franco.email = 'franco@gmail.com'
>>> franco.save()

```

Y podremos ver los cambios reflejados en el Browser de SQLite3

![cambios_sqlite3](https://imgur.com/nOdzRi6.png)

Si quiero borrar el dato, con su variable hago lo siguiente:

```shell
>>> franco.delete()
```

En la documentacion podemos ver como hacer consultas: [Making queries](https://docs.djangoproject.com/en/3.1/topics/db/queries/)
En el siguiente bloque podemos ver ejemplos simples:

```shell

>>> from posts.models import User
>>> user = User.objects.get(email='freddier@platzi.com')
>>> user
<User: User object (4)>
>>> type(user)
<class 'posts.models.User'>
>>> user.pk
4
>>> user.password
'987654321'

```

- `Model.objects.get` tratará de encontrar **UN SÓLO** registro en la base de datos que cumpla con los parámetros enviados, si existe **UNO**, lo regresa, si no existe, lanza una excepción y si encuentra varios también lanzará una excepción.
  - `user = User.objects.get()` Te permite obtener los valores unitario del registro. Ej: `user.first_name` pero aquí no puedes usar un update, con filter lo podrás hacer.

- `Model.objects.filter` ejecuta un query de consulta a la base de datos usando los parámetros enviados y regresa un objeto de la clase Queryset, ese queryset es iterable y puede contener 0, 1 o más elementos.
  - `user = User.objects.filter(email=‘freddier@platzi.com’)` Obtienes solo ese registro pero no puedes acceder directamente a sus atributos como con get, aquí deberías de hacer un for loop para recorrer y obtener cada valor.

### Extendiendo el modelo de usuario

El modelo de usuarios que acabamos de construir funciona bien y es válido, sin embargo tiene algunas cosas que podrían representar fallas de seguridad en la aplicación. Por esto vamos a explorar el modelo de usuarios que nos provee Django.

En la documentacion oficial de Django en la seccion **[django/contrib/auth/models.py](https://github.com/django/django/blob/master/django/contrib/auth/models.py)** podemos buscar `class AbstractUser` y ver el modelo de usuario que nos provee Django.

## 3. Models

### Configuración básica

#### Creacion de Super Usuario

Para crear un **super usuario** en Django escribimos en la consola:

```shell
python3 manage.py createsuperuser
```

Nos preguntara un **username, email (opcional), y contrañesa**, con esto ya tendriamos nuestro super usuario.

#### Dashboard de Administración

Django cuenta con un dashboard de administración. Para acceder a el debemos darle un path dentro del archivo **urls.py** de nuestro proyecto. Para esto importamos **django.contrib.admin** y le asignamos la dirección que deseamos

```py
from django.contrib import admin
from django.urls import path

urlpatterns = [
  path('admin/', admin.site.urls),
```

En este caso le dimos el path **admin/** para acceder a el. Entonces vamos a la dirección [**http://localhost:8000/admin/**](http://localhost:8000/admin/) para ingresar.

Para ingresar utilizaremos el **super usuario** que creamos en la **[sección de creación de super usuario.](#creacion-de-super-usuario)**

### Implementación del modelo de usuarios de Platzigram

Las opciones que Django propone para implementar Usuarios personalizados son:

- Usando el Modelo proxy
- Extendiendo la clase abstracta de Usuario existente. La opción **OneToOneField** restringe la posibilidad de tener perfiles duplicados.

Django no guarda archivos de imagen en la base de datos sino la referencia de su ubicación.

#### Implementación de modelos

Con Django podemos crear modelos de clases de nuestra aplicación.

Para estos ejemplos crearemos una nueva aplicacion de usuarios en nuestro proyecto.

```
python manage.py startapp users
```

En el archivo **models.py** de la nueva aplicación crearemos el modelo de nuestros usuarios, el cual sera una clase _Profile_, y los tipos de valores para la clase _models_ estan definidos en la [documentación.](https://docs.djangoproject.com/en/3.0/ref/models/fields/)

Para poder cargar las referencias de imagenes en neustro modelo instalaremos en nuestro ambiente Pillow, esto nos servira para la siguiente sección.

```
pip install pillow
```

Ahora creamos el modelo de usuarios:

```py
# Django
from django.contrib.auth.models import User, update_last_login
from django.db import models
from django.db.models.base import Model


class Profile(models.Model):
    """
    Profile model.

    Proxy model that extecnds the base data with other 
    information.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(
        upload_to='users/picture',
        blank=True,
        null=True
        )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Return username."""
        return self.user.username

```

#### Implementar modelos en base de datos

Los modelos creados en nuestras aplicaciones podemos aplicarlos en el esquema de nuestra base de datos. Primero debemos auditar los cambios en los modelos con:

```
python manage.py makemigrations
```

Ahora aplicaremos los cambios auditados en nuestra base de datos.

```
python manage.py migrate
```

### Explorando el dashboard de administración

> Registraremos el perfil que acabamos de customizar, junto con el modelo extendido de Usuario, en el admin de Django para poder manejarlo desde la aplicación.

Esto puede hacerse de dos formas: con admin.site.register(Profile) o creando una nueva clase que herede de Admin.ModelAdmin.

#### Reflejar modelos en dashboard de administración

En primera instancia no podremos ver los _modelos_ que creamos en el dashboard de administración. La clase **ModelAdmin** es la representacion del modelo en la interfaz de administración. Para reflejarlo debemos almacenar el _modelo_ en el archivo **admin.py** de nuestra aplicación.

```py
# Django
from django.contrib import admin

# Modelos
from users.models import Profile

# Registramos nuestros modelos aquí.
admin.site.register(Profile)
```

De esta forma tendremos la interfaz de administración predeterminada, en nuestro caso incluimos el modelo **Profile**.

![profile_1](https://imgur.com/FIW5GtK.png)

![profile_2](https://imgur.com/qedBO59.png)

![profile_3](https://imgur.com/HJdN0NB.png)

#### Dashboard administrativo personalizado

Si queremos mostrar nuestra lista de modelos de una forma personalizada, con Django podemos realizarlo. Para esto debemos crear una clase **ModelAdmin**:

```py
# Django
from django.contrib import admin

# Modelo
from users.models import Profile

# Decoramos la clase con el modelo.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin): #Por convencion la clase que creemos debe terminar en Admin.

    # Con list_display nombramos los campos que queremos visualizar.
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')

    # list_display_links establece como links los campos nombrados.
    list_display_links = ('pk', 'user')

    # list_editable nos permite editar el campo desde
    # la lista del modelo en vez de ingresar al detalle del registro.
    list_editable = ('phone_number')

    # Para crear un buscador hacemos uso de search_fields.
    # Los campos que se ingresan seran los que el buscador recorrera para realizar las busquedas.
    search_fields = (
        'user__username',
        'user__email',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )

    # Podemos crear un filtro para nuestro dashboard del modelo,
    # para ello usamos list_filter, y definimos los campos con los que trabajara.
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified'
        )
```

![profile](https://imgur.com/oNuwdge.png)

Para mas opciones de personalización siempre puedes revisar la [documentación.](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#modeladmin-options)

### Personalizando Dashboards Nativos

> Editaremos el detalle para que sea igual de complejo que el detalle de Usuario y le agregaremos los datos del perfil para no tener que estar cambiando de urls. Usaremos `fieldsets` y `admin.StackedInline`.

En la documentación de Django, podemos ver [cómo funcionan los fieldsets](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/).

Existe la posibilidad de personalizar los dashboard nativos de Django, para ello vamos a trabajar sobre el modelo de **Users** para el cual vamos a visualizar los datos que definamos y tambien al momento de crear un usuario tambien podremos crear dentro del proceso una instancia de nuestro modelo _Profile_.

Agregamos las siguientes librerias en admin.py

```py
# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from django.contrib.auth.models import User
```

Estando en admin.py agregamos datos al `ProfileAdmin` y las clases `ProfileInline` y `UserAdmin`.

```py

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Profile admin."""

    ...

    fieldsets = (
        ('Profile', {
            'fields': (
                ('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography'),
            )
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),
                       ),
        })
    )

    readonly_fields = ('created', 'modified',)


# Aqui definiremos el modelo que deseamos asociar a User, en nuestro caso Profile.
class ProfileInline(admin.StackedInline):
    """ Profile in-line admin for users."""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


# Luego para asociar los modelos e insertarlo en el Dashboard usaremos
# el UserAdmin de Django el cual le dimos el alias de BaseUserAdmin.
class UserAdmin(BaseUserAdmin):
    """ Add profile admin to base user admin."""

    inlines = (ProfileInline,) # Con inlines desplegaremos los campos que hay que llenar asociados a Profile.
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


```

Si vamos a crear un nuevo **User** podremos encontrar los campos asociados a nuestro modelo _Profile_ que definimos en la variable _inlines_

![adding_user_with_profile](https://imgur.com/zLvv41L.png)

Y si revisamos la lista de registro **User** veremos los cambios realizados en la variable _list_display_.

![items_peer_users](https://imgur.com/wIRPMo2.png)

En la [documentación](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#modeladmin-options) tenemos muchas mas formas de personalización.

### Relacionando modelos

¿Que pasa si en nuestro proyecto un modelo depende de otro? Un ejemplo de esto puede ser un **_post_** que solo es posible que exista si esta relacionado con un **_usuario_**. Afortunadamente en Django podemos relacionar los modelos, en nuestro caso lo haremos con el modelo de **posts**, por lo iremos al archivo _posts/models.py_.

```py
""" Posts models."""

# Django
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Post model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Con ForeignKey podemos relacionar el modelo de posts con profile,
    # y para hacer referencia a la clase relacionada lo hacemos con
    # el formato de 'aplicacion.NombreClaseDelModelo'.
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Return title and username"""
        return '{} by @{}'.format(self.title, self.user.username)

```

### Hacer funcionar los links de medias en desarollo

¿Te fijaste que los links de los campos de nuestros registros nos llevaba al detalle de estos? Para que estos links nos lleven realmente a sus referencias debemos realizar algunos cambios en el archivo **urls.py** y **settings.py**.

En nuestro archivo **settings.py** declararemos 2 variables en el fondo del archivo.

```py
...

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

Luego iremos al archivo **urls.py** y a _urlpatterns_ donde tenemos definidos los path de nuestras aplicaciones vamos a concatenar un valor static

```py
# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from platzigram import views as local_views
from posts import views as posts_views


urlpatterns = [

    path('admin/', admin.site.urls),

    path('hello-word/', local_views.hello_word),
    path('numbers/', local_views.numbers),
    path('hi/<str:name>/<int:age>', local_views.say_hi),

    path('posts/', posts_views.list_posts),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# concatenamos static con los valores definidos en settings.py

```

Con esto estaría todo listo para que los valores definidos como links en los dashboard funcionen correctamente.

### RETO: Crea el modelo de posts y regístralo en el admin

Reto de la clase:
Crea el modelo de posts y regístralo en el admin.

```py
""" Posts admin classes."""

# Django
from django.contrib import admin

# Models
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Posts Admin model"""

    list_display = ('pk', 'user', 'title', 'photo')
    list_display_links = ('pk', 'user')
    list_editable = ('title', 'photo')

    search_fields = ('user__username', 'title')
    list_filter = ('created', 'modified')
    readonly_fields = ('created', 'modified')

```

En la siguiente imagen podemos ver como se agrega la sección post agregando la clase PostAdmin. Se pueden observar las tuplas search_fields y list_filter agregadas en la clase:

![post_menu](https://imgur.com/pfrF6r6.png)

En la siguiente imagen se puede observar como agregariamos un post y que datos son relevantes para agregarlo:

![adding_post](https://imgur.com/dtLmr8e.png)

## 4. Templates, auth y middlewares

### Archivos estáticos

> El concepto de archivos estáticos en Django, son archivos que se usan a través de la aplicación para pintar los datos. Pueden ser archivos de imagen, audio y video, o archivos css y scripts js.

Los archivos estáticos son elementos de nuestro proyecto que podremos usar de forma transversal. Técnicamente podemos usar tipo de elemento como estético pero por lo general se hacen uso de **css** e **imágenes.**

En la raíz de nuestro proyecto crearemos una carpeta llamada _static_, y en ella contendra otras 2 carpetas llamadas _css_ y _img_. Estas van a contener nuestros archivos **css** e **imagenes** respectivamente.

![static_folder](https://imgur.com/puv3mqQ.png)

Ahora vamos al archivo _settings.py_ de nuestro proyecto. Justo debajo de la variable **STATIC_URL** vamos a pegar las variables de **STATICFILES_DIRS** y **STATICFILES_FINDERS**. [En la documentación podemos encontrar mas información.](https://docs.djangoproject.com/en/3.1/ref/settings/#static-files)

```py
...

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
...
```

Con esto tus archivos estáticos ya pueden ser referenciados.

### Templates

Los templates de nuestro proyecto tienen la capacidad de **extenderse** desde otros templates, asi podremos reutilizar los elementos que deseamos, como por ejemplo un _navbar_.

Para preparar todo iremos al archivo _settings.py_, y en la variable **TEMPLATES** vamos a definir donde buscar los **templates** para nuestro proyecto.

```py
TEMPLATES = [
    {
        ...
        'DIRS': [
            # Aqui definimos la carpeta donde ira a buscar el template nuestras aplicaciones.
            os.path.join(BASE_DIR, 'templates'),
        ],
        ...
    },
]
```

En la **raíz** de nuestro proyecto crearemos la carpeta _templates_ definido anteriormente y dentro de este crearemos todos los elementos compartidos, como por ejemplo un **navbar, base, etc.** Para los templates **no compartidos** que deseamos agregar vamos a crear **carpetas** de estos elementos. Para nuestro ejemplo vamos a crear los templates compartidos de **base** y **navbar**, y para los elementos particulares crearemos las carpetas **posts** y **users**, con los archivos _feed.html_ y _base.html_ respectivamente.

![templates](https://imgur.com/AA82MBV.png)

- **templates/nav.html**: Primero vamos a crear nuestro navbar en el archivo _templates/**nav.html**_ y haremos referencias a nuestros **archivos estáticos** creados en la [sección anterior.](#Archivos-estáticos)

- **templates/base.html**: Nuestro **navbar** aun no aparecera en nuestra aplicación. Para esto crearemos el archivo _templates/**base.html**_ y como lo hicimos en el archivo anterior vamos a cargar los **archivos estáticos.** Definamos tambien el **bloque del head** y el **container que desplegara los templates** que se extenderan.

- **templates/posts/feed.html**: Con esto ya desplegamos nuestro template **navbar** dentro de **base**. Vamos a crear el template para **posts** que se **extendera** del archivo _templates/base.html_, el cual sera _templates/posts/**feed.html**_

  - Como ahora este template esta fuera de la aplicación debemos referenciarla en el render de la vista, por lo que iremos a _posts/views.py_ a realizar los cambios. Lo referenciaremos como _**posts/feed.html**_ que hace referencia al path de _template/posts/feed.html_. **No es necesario definir la carpeta _templates_** ya que en el archivo _settings.py_ definimos que **los templates seran buscados en esta carpeta**.

```py
...

def list_posts(request):
    """List existing posts"""
    # En la función que nos devuelve el render, debemos referenciar correctamente el template,
    # en este caso a posts/feed.html
    return render(request, 'posts/feed.html', {'posts': posts})
```

Ahora si revisamos el path de la aplicación [http://localhost:8000/posts/](http://localhost:8000/posts/) veremos el template de **base**, **navbar** y **posts** desplegados correctamente, ademas del head definido en _templates/posts/feed.html_

![app](https://imgur.com/2dqZGU0.png)

### Login | Protegiendo vistas

> Vamos a crear el login de nuestra aplicación, y este estara alojado en la aplicaciónde **users**. Tambien protegeremos las vistas de **posts** para solo poder acceder a ellas cuando estemos iniciados.

[Documentacion de como hacer Login de Django](https://docs.djangoproject.com/en/3.1/topics/auth/default/#authentication-in-web-requests)

Primero vamos a poner **alias a las rutas** de nuestro proyecto, de esta forma podemos referenciar al alias en cualquier parte de nuestra aplicación sin preocuparnos si cambian el path, para esto iremos a _urls.py_

```py

urlpatterns = [

    path('admin/', admin.site.urls),

    # A los path podemos asignarles valores a la variable name indicando un alias a la ruta
    path('hello-word/', local_views.hello_word, name='hello_word'),
    path('numbers/', local_views.numbers, name='numbers'),
    path('hi/<str:name>/<int:age>', local_views.say_hi, name='hi'),

    path('posts/', posts_views.list_posts, name='feed'),

    path('users/login/', users_views.login_view, name='login')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

En el archivo _users/**views.py**_ vamos a renderizar el **login**

```py

""" Users views"""

# Django
# Importamos authenticate y login
from django.contrib.auth import authenticate, login
# Redirect nos ayudara a redireccionarnos a otro path
from django.shortcuts import render, redirect

# Create your views here.
def login_view(request):
    """ Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # El metodo authenticate tratara de contrastar el usuario
        # con una instancia del modelo users que creamos.
        user = authenticate(request, username=username, password=password)
        if user:
            # En caso de ser exitoso la autenticación creara
            # un token de nuestro usuario para almacenarlo en memoria.
            login(request, user)
            # Y nos redireccionaremos al path con alias 'feed' que es 'posts/'
            return redirect('feed')
        else:
            # En caso de dar false la autenticacion volveremos a renderizar el login, 
            # pero enviando la variable 'error'
            return render(request,
                          'users/login.html',
                          {'error': 'Invalid username and pasword'})
    return render(request, 'users/login.html')

```

En _templates/users_ crearemos 2 archivos, **base.html** y **login.html**. La razón del porque ocuparemos un base distinto al anterior es por que a nivel de contenido son distintos, sin embargo _template/users/**login.html**_ extendera de _template/users/**base.html**_

En el archivo _login.html_ hacemos uso del metodo **csrf_token** de Django. Este método evita un tipo de exploit malicioso llamado **"Cross-site request forgery"**, el cual consiste en llenados de formularios desde fuera del sitio. La forma en la que trabaja _csrf_token_ es que cuando se realiza una peticion 'GET' se te envia un token único, y cuando realizas el submit del formulario con un metodo 'POST' se va a revisar el token que conseguiste antes, de esta forma se evita el exploit.

![csrf_token](https://imgur.com/cUr8kA0.png)

Ahora para **proteger** las vistas de _posts_ y solo podamos acceder a ellas si hemos **iniciado sesión** vamos al archivo _settings.py_ de nuestro proyecto y al fondo del código creamos la variable **LOGIN_URL** con el path de nuestro **login**, de esta forma nos redigira al path definido si tratamos de renderizar una vista protegida.

```py
...
# Usamos el alias del path de login
LOGIN_URL = 'login'
```

Ahora para proteger las vistas debemos ir al archivo views.py de nuestra aplicación.

```py
# Django
# Importamos login_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

...

# Decoramos con login_required la función que renderiza nuestra vista,
# el cual ahora necesitara una sesión iniciada para poder renderizarse.
# En caso de no estarlo nos redirigira al path de login.
@login_required
def list_posts(request):
  return render(request, 'posts/feed.html', {'posts': posts})
```

Ahora veamos las vistas protegidas en acción. Con un usuario **sin registrar** nos va a volver a redirigir a la pagina de login.

Y si el usuario está **registrado** podremos ver los posts.

### Logout

> Completaremos el flujo de autenticación del usuario anterior agregando la funcionalidad de Logout. Ademas incorporamos algo de estilos al formulario de Login.

[Documentación de Logout de Django](https://docs.djangoproject.com/en/3.1/topics/auth/default/#how-to-log-a-user-out)

El proceso de **logout** es bastante sencillo en Django. Primero iremos a las vistas de nuestro aplicativo y crearemos una función para ello.

```py
# Archivo users/views.py
# Django
# Importamos logout y el un decorador (login_required)
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Creamos la funcion logout_view, y lo decoramos con
# login_required, asi solo se ejecutara si existe una sesión.
@login_required
def logout_view(request):
    """ Logout a user."""
    logout(request) # Ejecutamos logout, el cual borrara los tokens del navegador.
    return redirect('login') # Redirigimos a path de login.
```

Luego de ello iremos a las _urls.py_ de nuestro proyecto.

```py

...

urlpatterns = [
  ...
  # Creamos el path de logout.
  path('users/logout', users_views.logout_view, name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Y por terminar, en el **html** haremos referencia al path de 'logout'.

```html
<!-- templates/nav.html -->
{% load static %}
...
        <li class="nav-item nav-icon">
          # Hacemos referencia al path de 'logout' en nuestro elemento.
          <a href="{% url 'logout' %}">
            <i class="fas fa-sign-out-alt"></i>
          </a>
        </li>
...
```

Listo, ahora tenemos un logout funcionando perfectamente de forma sencilla.

### Signup

> Crearemos el Registro de usuario a partir de la clase perfil, por lo que usaremos un formulario personalizado. Definiremos un nuevo Template para el formulario. Dejaremos que el browser se encargue de las validaciones generales. Sólo validaremos en python la coincidencia entre password y confirmación del password. Incluiremos una validación con try/catch para evitar que se dupliquen usuarios con mismo nombre.

[Documetation about how Using the Django authentication system](https://docs.djangoproject.com/en/3.1/topics/auth/default/#creating-users)

Primero crearemos un **template** para el registro, asi que creamos el archivo **template/users/signup.html**. El código html se encuentra en él.

El template quedaria de la sigueinte manera:

![signup](https://imgur.com/Y2itqOA.png)

Teniendo listo nuestro **template** ahora crearemos la función que renderizara nuestra vista. Para ello iremos a _users/**views.py**_

```py
# Django
...
# Vamos hacer uso de render y redirect
from django.shortcuts import render, redirect

# Exceptions
# Importamos posible error al tratar de crear una instancia con valor único que ya existe
from django.db.utils import IntegrityError

# Models
# Importamos los modelos de las instancias que crearemos
from django.contrib.auth.models import User
from users.models import Profile

...

def signup(request):
    """ Sign up view."""
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        # PASSWORD VALIDATION
        if passwd != passwd_confirmation:
            error = 'The passwords do not match.'
            return render(request, 'users/signup.html', {'error': error})

        # EMAIL VALIDATION
        email_validation = User.objects.filter(email=email)
        if email_validation:
            error = f'There is another account using {email}'
            return render(request, 'users/signup.html', {'error': error})

        # USERNAME VALIDATION
        try:
            user = User.objects.create_user(username=username, password=passwd)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = email
            user.save()
        except IntegrityError:
            return render(request, 'users/signup.html',
                          {'error': 'Username is already exist'})

        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')


...
```

Ahora nos faltaría solo asignar un path a nuestro signup, lo configuraremos en _urls.py_

```py
...

urlpatterns = [
  ...
  
  path('users/signup/', users_views.signup, name='signup'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

...
```

### Middlewares

> Veremos que son los Middlewares, como funcionan y como nos puede ayudar a resolver el problema de que cada usuario tenga su perfil completo antes de poder usar la app.

[Documentation in Django about Middlewares](https://docs.djangoproject.com/en/3.1/topics/http/middleware/)

Un middleware en Django es una serie de hooks y una API de bajo nivel que nos permiten modificar el objeto request antes de que llegue a la vista y response antes de que salga de la vista.

Django dispone de los siguientes middlewares por defecto:

- **SecurityMiddleware**: Se encarga de comprobar todas las medidas de seguridad, las variables de settings relacionadas con Https, Auth, entre otros.
- **SessionMiddleware**: Se encarga de validar una sesión.
- **CommonMiddleware**: Se encarga de verificar componentes comunes como lo es el debug.
- **CsrfViewMiddleware**: Se encarga de toda la validación correspondiente a CSRF. Éste nos permite utilizar el tag {% csrf_token %} y es el que inserta el token de seguridad en cada formulario.
- **AuthenticationMiddleware**: Nos permite agregar request.user desde las vistas.
- **MessageMiddleware**: Pertenece al Framework de mensajes de Django, y permite pasar un mensaje sin necesidad de mantener un estado en la base de datos o en memoria.
- **XFrameOptionsMiddleware**: Middleware de seguridad.

![middleware](https://imgur.com/zz7HrVZ.png)

Crearemos un middleware para redireccionar al usuario al perfil para que actualice su información cuando no haya definido aún biografía o avatar.

En este apartado aprenderemos como crear nuestro propio **middleware**, este no permitira la navegación en la aplicación si es que el usuario **no tiene fotografia o biografía.**

Primero crearemos un template del perfil donde el usuario podra modificar su información. Este template sera simple por el momento y estara en _templates/users/**update_profile.html**_.

Ahora en nuestro archivo _users/views.py_ vamos a crear la funcion que renderizara el template recien creado.

```py
...

@login_required
def update_profile(request):
    """ Update a user's profile view."""
    return render(request, 'users/update_profile.html')
...
```

Luego de definir nuestra vista vamos asignarle un path dentro del archivo _urls.py_

```py
...

urlpatterns = [
  ...
  
  path('users/me/profile', users_views.update_profile, name='update_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Ahora crearemos nuestro **middleware**. Por lo general los middleware se crean en la aplicación relacionada, pero **solo para efectos practicos** crearemos el nuestro en la carpeta principal de nuestro proyecto como **middleware.py**

![middleware](https://imgur.com/EFwTPix.png)

El **objetivo** de nuestro middleware es evitar que se pueda navegar por la aplicación si es que el usuario no tiene foto de perfil o no ha escrito su biografía, por lo que nuestro middleware contendra una clase que realizara todas estas validaciones.

```py
""" Platzigram middleware catalog."""

# Django
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
    """ Profile Completion Middleware.

    Ensure every user that is interacting with the platform
    have their profile picture and biography.
    """

    def __init__(self, get_response):
        """ Middleware initialization."""
        self.get_response = get_response

    def __call__(self, request):
        """ Code to be executed for each request before the view is called."""

        if not request.user.is_anonymous:
            profile = request.user.profile
            if not profile.picture or not profile.biography:
                if request.path not in [reverse('update_profile'),
                                        reverse('logout')]:
                    return redirect('update_profile')

        response = self.get_response(request)
        return response
```

Ahora tenemos que decirle a nuestro proyecto que ahora también debe usar este middleware para las peticiones. Para ello iremos al archivo _settings.py_ y lo incluiremos en la variable de **MIDDLEWARE.**

```py
MIDDLEWARE = [
    # Django
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Propios
    # Referenciamos al middleware por el nombre de la clase
    'photogram.middleware.ProfileCompletionMiddleware',
]
```

Y con esto ya creamos nuestro primer middleware.

## 5. Forms

### Formularios en Django

> En esta seccion vamos a tener una primera aproximación a los formularios de Django, ver como una clase utilitaria nos ayuda a hacer el trabajo que se realiza repetitivamente y se terminará la parte de completar un perfil de usuario.

[Documentation in Django about Forms](https://docs.djangoproject.com/en/3.1/topics/forms/)

En esta sección veremos en acción los **forms** en Django. Primero que todo crearemos nuestro form en _templates/users/**update_profile.html**_ creado en la sección de [middlewares](#Middlewares). Algo asi nos quedaria el formulario:

![form_image](https://imgur.com/vpsERKu.png)

Django ya incorpora una **clase forms** del cual podemos hacer uso, asi que crearemos nuestra clase forms para crear un formulario de usuario.

```py
""" User forms."""

from django import forms


class ProfileForm(forms.Form):
    """ Profile form."""

    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()

```

![form](https://imgur.com/niuJWbS.png)

En la documentación podras encontrar como trabajar con [formularios](https://docs.djangoproject.com/en/3.1/topics/forms/) y los [campos](https://docs.djangoproject.com/en/3.1/ref/forms/fields/) que puedes usar.

Para poder recibir los datos y guardarlos en nuestra base de datos vamos a ir a nuestra vista de la aplicación _users/**views.py**_ en donde crearemos la función que se encargara de ello.

```py
# Archivo users/views.py
...

# Forms
# Importamos el ProfileForm que creamos anteriormente
from users.forms import ProfileForm


# En la vista de update_profile vamos a recibir el request.
@login_required
def update_profile(request):
    """ Update a user's profile view."""

    # Crearemos una variable que guardara el profile
    # que esta realizando el request.
    profile = request.user.profile

    # Si el request es de tipo 'POST'
    if request.method == 'POST':

        # Crearemos una instancia de ProfileForm
        # con los datos que recibimos a traves de request
        form = ProfileForm(request.POST, request.FILES)

        # Si la instacia se crea sin problemas.
        if form.is_valid():

            #Guardaremos los datos recibidos en base de datos.
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            # Y redireccionaremos a la pagina update_profile
            # para reflejar los cambios.
            return redirect('update_profile')
    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',

        # Enviaremos al template los datos del usuario.
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )

...
```

Terminados estos pasos podremos ver nuestro profile con los datos de nuestro usuario y actualizarlos, preservando los datos.

En caso de que algun dato no cumpla con los requisitos establecidos en la clase form desplegaremos en pantalla los errores que tengamos.

![forms_error](https://imgur.com/fCnn9tg.png)

### Mostrando el form en el template

> Existen diferentes formas en las que se pueden mostrar los valores del form, estas son: as_table, as_p y as_ul. También se pueden mostrar campos de manera individual, incluso customizar las clases que se van a usar para mostrar los errores, etc. Refinaremos la apariencia del form a través de algunas refactorizaciones en el template.

[Documentation in Django about how working with form templates](https://docs.djangoproject.com/en/3.1/topics/forms/#working-with-form-templates)

En la sección anterior, si enviamos campos inválidos estos vuelven con el valor anterior que tenian. En esta sección haremos persistentes estos datos.

Para ello solo tendremos que modificar nuestro _template/**update_profile.html**_

Con los cambios hechos en **template/update_profile.html** los valores ingresados **persistiran** en nuestro formulario sin importar si existe un error, ademas de mostrarlos de forma estilizadas.

![forms_invalid_entries](https://imgur.com/TlIw9Fi.png)

### Model forms

> ModelForm es una manera más sencilla de crear formularios en Django y en el caso de nuestro proyecto, se adapta mucho mejor al modelo que ya tenemos. Esto es lo que haremos en esta sección, lo usaremos para crear el formulario de posts.

[Documentation in Django about model forms](https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/)

Ahora la dirección **http://127.0.0.1:8000/** nos llevará al feed y creamos una nueva url para crear nuevos post, todo esto en el archivo urls.py

```py
urlpatterns = [
    ...
    path('', posts_views.list_posts, name='feed'),
    path('posts/new/', posts_views.create_post, name='create_post'),
    ...
```

Luego crearemos forms.py en la carpeta posts

```py
""" Post forms."""

# Django
from django import forms

# Models
from posts.models import Post


class PostForm(forms.ModelForm):
    """ Post model forms."""

    class Meta:
        """ Form settings"""

        model = Post
        fields = ('user', 'profile', 'title', 'photo')
```

Luego crearemos una nueva vista en posts/views.py que será la lógica de creación de un nuevo post. 

```py
# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Forms
from posts.forms import PostForm

@login_required
def create_post(request):
    """ Create new post view."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )


```

Para finalizar esta parte lo que hacemos finalmente es crear el tamplate en **new.html** en posts quedando la vista de la siguiente manera:

![new_post](https://imgur.com/8flresa.png)

y si no posteamos nada y queremos enviar datos vacios nos aparecerá lo siguiente:

![new_post_error](https://imgur.com/1qURzno.png)

Cuando agregamos un post, no lo podremos ver aún reflejado en el front pero si en el back

![post_in_admin](https://imgur.com/FcV3c6R.png)

> Aprovecharemos para refinar la funcionalidad en el navbar y conectar el feed con los posts.

En el archivo de la carpeta template modificamos el **nav.html** para que los botones nos redirijan a los lugares adecuados.

Luego conectaremos el feed con los posts, modificando posts/views.py y modificando el template de posts/feed.html

Borramos lo que teniamos hardcoreado y vinculamos los posts creados con el feed. Mostramos desdes el ultimos creado. 

```py

@login_required
def list_posts(request):
    """List existing posts"""
    posts = Post.objects.all().order_by('-created')
    return render(request, 'posts/feed.html', {'posts': posts})

```

### Validación de formularios

#### Agregaremos enlace hacia signup en la vista login

> Agregaremos enlace hacia signup en la vista login

Resolviendo el primer caso, el de agregar un enlace hacia signup en la vista login lo que hacemos es agregar la siguiente linea de código en **templates/users/login.html**.

```html
<p class="mt-4">Don't have an account yet? <a href="{% url 'signup' %}">Sign up here</a></p>
```

#### Forma mas facil de trabajar con los templates

Django cuenta con una forma mas facil de trabajar con los templates, como podemos ver en el siguiente enlace a la documentación:

[Documentation in Django about working with form template](https://docs.djangoproject.com/en/3.1/topics/forms/#working-with-form-templates)

En nuestro caso lo que hicimos fue eliminar el form creado por nosotros en el frontend y utilizar las herramientas que nos da Django

```html
{{ form.as_p }}
```

Tambien le agregamos la linea de codigo siguiente para que nos redirija al Login si nos encontramos registrados:

```html

  <p class="form-text mt-2">If you already have an account <a href="{% url 'login' %}">Log in!</a></p>


```

#### Aprendiendo a validad campos de un formulario

> Para aprender a validar los campos de un formulario vamos a actualizar el registro de usuarios.

Hasta este momento el script de validación del formulario Signup está escrito directamente en la vista, y a pesar de que no genera ningún error, puede convertirse en un problema, así que lo recomendable es separarlo. Crearemos un nuevo form con la clase forms.Form, también vamos a introducir un nuevo concepto relacionado con formularios: los widgets.

[Documentation in Django about forms fields](https://docs.djangoproject.com/en/3.1/ref/forms/fields/)
[Documentation in Django about form and field validation](https://docs.djangoproject.com/en/3.1/ref/forms/validation/)

Los widgets en Django, son una representación de elementos de HTML que pueden incluir ciertas validaciones. Por default todos los campos son requeridos. Los datos depurados se pueden consultar con self.cleaned_data['_nombre_del_field_']

[Documentation in Django about widgets](https://docs.djangoproject.com/en/3.1/ref/forms/widgets/)

Todo lo explicado anteriormente lo podemos ver reflejado en la siguiente clase en forms.py dentro de platzigram/users/:

```py
# Models
from django.contrib.auth.models import User
from users.models import Profile


class SignupForm(forms.Form):
    """Sign up form"""

    username = forms.CharField(
        label=False,
        min_length=4,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nombre de usuario',
                'class': 'form-control',
                'required': True})
    )

    password = forms.CharField(
        label=False,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Escribe tu contraseña',
                'class': 'form-control',
                'required': True})
    )

    password_confirmation = forms.CharField(
        label=False,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirma tu contraseña',
                'class': 'form-control',
                'required': True})
    )

    first_name = forms.CharField(
        label=False,
        min_length=2,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nombres',
                'class': 'form-control',
                'required': True})
    )

    last_name = forms.CharField(
        label=False,
        min_length=2,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Apellidos',
                'class': 'form-control',
                'required': True})
    )

    email = forms.EmailField(
        label=False,
        min_length=6,
        max_length=70,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Correo electrónico',
                'class': 'form-control',
                'required': True})
    )

    def clean_username(self):
        """Username must be unique.
        Confirmamos que el usuario sea unico"""
        username = self.cleaned_data["username"]
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """Verify password confirmation match.
        Podemos confirmar otros datos que no sean el usuario"""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match')

        return data

    def save(self):
        """Create user and profile.
        Como usamos los datos una vez que son validos"""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()

```

En views.py lo que hacemos es agregar una función intermediaria entre el forms que se comunican con la base de datos y los templates que nos dan la vista del usuario 

```py

# Forms
from users.forms import ProfileForm, SignupForm

def signup(request):
    """ Sign up view.
    Intermediario"""
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()

    return render(
        request=request,
        template_name='users/signup.html',
        context={'form': form}
    )

```

## 6. Class-based views

### Simple Class-based views

Veamos de qué forma optimizamos el proceso de creación de nuestras apps de forma que no repitamos código. Para ver cuál es el concepto de class based views.

Las vistas también pueden ser clases, que tienen el objetivo de evitar la repetición de tareas como mostrar los templates, son vistas genéricas que resuelven problemas comunes.

[Documentation in Django about Class-based views](https://docs.djangoproject.com/en/3.1/topics/class-based-views/)
[Documentation in Django about Built-in class-based views API](https://docs.djangoproject.com/en/3.1/ref/class-based-views/)
[Documentation about Django - Class and Class-Based Views](http://ccbv.co.uk/)

> Haremos en esta seccion presentacion de template usando las vistas basadas en clases, el cual es el más sencillo de implementar. Haremos la presentación del perfil de usuario.

Cambiamos las urls.py de la carpeta platzigram

```py
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('users/', include(('users.urls', 'users'), namespace='users')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Y las urls que se encontraban en ese archivo las llevamos a posts/urls.py y users/urls.py

En esos archivos trabajaremos las TemplateViews.

Hay que cambiar las url de los **templates views** y **middleware** para que funcione la aplicación:

En la carpeta platzigram en middleware midificamos esto:

```py
if request.path not in [reverse('users:update_profile'), ('users:logout')]:
    return redirect('users:update_profile')
```

En template/users/update_profile.html

```html
<form action="{% url 'users:update_profile' %}" method="POST" enctype="multipart/form-data">
```

En template/users/login.html se cambia en dos lineas

```html
<form method="POST" action="{% url "users:login" %}">

<p class="mt-4">Don't have an account yet?<a href="{% url "users:signup" %}">Sign up here.</a></p>
```

En template/users/signup.html

```html
<form action = "{% url 'users:signup' %}" method="POST">
```

En posts/views.py en la funcion create_post

```py
return redirect('posts:feed')
```

Y por ultimo en users/views.py se cambia en:

La función login_view

```py
return redirect('posts:feed')
```

La funcion logout_view
```py
return redirect('users:login')
```

La funcion signup

```py
return redirect('users:login')
```

Y por ultimo la funcion update_profile

```py
return redirect('users:update_profile')
```

## 7. Deployment

## 8. Bonus
