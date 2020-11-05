
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

## 3. Models

## 4. Templates, auth y middlewares

## 5. Forms

## 6. Class-based views

## 7. Deployment

## 8. Bonus
