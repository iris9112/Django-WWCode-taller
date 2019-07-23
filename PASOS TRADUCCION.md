# Pasos

Los tres pasos para usar la internacionalización en aplicaciones Django son:

1. Activa el middleware local en la configuración de Django.
2. Especifica las cadenas de traducción en el código Python y en las plantillas.
3. Implementa las traducciones para esas cadenas, en cualquiera de los lenguajes que quieras soportar.

## Paso 1: configuración de Django :heartpulse:

Asegurarnos de tener activadas las traducciones en nuestra configuración. Hacer los siguientes cambios en el archivo `agency_project\config\settings.py`:

```python
LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'

USE_I18N = True
USE_L10N = True
USE_TZ = True
```

## Paso 2: Marcar texto a traducir :pencil:

### Texto en plantillas

Lo primer es cargar la etiqueta `{% load i18n %}` en el template de django, para una línea sencilla utilizamos el templatetag `{% trans 'texto' %}` pero si tenemos contenido un poco más complejo, por ejemplo que incluya multiples elementos HTML o variables, utilizaremos los templatetag `blocktrans` / `endblocktrans`.

Ejemplo:

 ```html
{% load i18n %}

{% comment %}Translators: por favor se creativo{% endcomment %}
<h1>{% trans '¡Bienvenido a nuestro sitio!' %}</h1>
<p>
    {% blocktrans trimmed %}
        Conoce nuestro servicio del mes {{ service.name }}
    {% endblocktrans %}
</p>
 ```

### Texto en código python

Las cadenas de traducción se especifican usando la función `ugettext()`. Este por convención usa el alias `_` (guion bajo), como un atajo para importar la función.

```python
from django.utils.translation import ugettext as _

def mi_vista(request):
    # Translators: Este mensaje aparece en la página de inicio únicamente.
    sentencia = 'Bienvenido a mi sitio.'
    # la traducción también funciona sobre variables
    salida = _(sentencia)
    return HttpResponse(salida)
```

## Paso 3 :computer:

El siguiente paso es crear los archivos de traducción para cada uno de los lenguajes que queremos soportar, para esto agregaremos unas cuantas líneas más a la configuración `agency_project\config\settings.py`:

```python
from django.utils.translation import ugettext_lazy as _

TEMPLATES = [
    {
            ...
            'context_processors': [
                'django.template.context_processors.i18n', # Util para internacionalizacion
            ],
        },
    },
]

MIDDLEWARE = [
    ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  #encargado de escoger el lenguaje adecuado
    'django.middleware.common.CommonMiddleware',
    ...  
]

LANGUAGES = [
    ('es', _('Español')),
    ('en-us', _('English'))
]

# esta carpeta la debemos crear nosotros
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]
```

Además en el archivo global de urls agregar:

`path('i18n/', include('django.conf.urls.i18n')),`

### Crear archivos de traducción

Ya tenemos todo configurado, ahora vamos a crear los archivos de traducción con el siguiente comando:

`django-admin makemessages -l en_US`

Se crearán en la ruta:

`some_project\locale\en_US\LC_MESSAGES\django.po`

```
#. Translators: Este mensaje aparece en la página de inicio únicamente.
# path/to/python/file.py:123
msgid "Bienvenidos a mi sitio."
msgstr ""
```

Estos archivos son los que utilizaremos para especificarle a Django cómo traducir cada palabra en determinado idioma, entonces simplemente para cada uno de los strings que aparezcan en `msgid` podemos especificar su traducción con los strings msgstr:

```
msgid "Bienvenidos a mi sitio."
msgstr "Welcome to my site."
```

### Compilar archivos de traducción

Una vez tengamos nuestros archivos de traducción completos, procederemos a compilarlos con el siguiente comando:

`django-admin compilemessages`

Cuando compilemos nuestros archivos, ya podemos utilizar nuestro proyecto en el idioma especificado. Cada que uno de nuestros usuarios consulte nuestro proyecto aparecerá en su idioma. Para efectos de prueba, podemos cambiar el lenguaje del proyecto por inglés y observar los resultados:

`LANGUAGE_CODE = 'en-us'`

### Ejemplo de salida de comandos

```bash
(my_env) C:\Users\agency_project>django-admin makemessages -l en_US
processing locale en_US

(my_env) C:\Users\agency_project>django-admin compilemessages
processing file django.po in C:\Users\agency_project\locale\en_US\LC_MESSAGES
```