# Internacionalización con Django

Django ofrece un robusto framework de internacionalización y localización para ayudarte a desarrollo aplicaciones para múltiples idiomas y regiones del mundo.

En este taller vamos aprender los conceptos relacionados con la internacionalización de aplicaciones web y vamos a realizar un ejemplo traducción del contenido estatico y dinamico de un sitio web.

## Conceptos

1. **Internacionalización:** proceso de diseñar programas para el uso potencial de cualquier localidad (ciudad, país). Es decir poder traducir a diferentes idiomas elementos de la interfaz, texto, mensajes de error, y además configurar elementos como fechas y horas, de manera que sea posible respetar diferentes estándares locales. Generalmente hecho por desarrolladores.

`Dato curioso:` Encontrarás a menudo "*internacionalización*" abreviada como `I18N` dónde el número 18 se refiere al número de letras omitidos entre la `I` inicial y la `N` final.

2. **Localización:** proceso específico de traducir un programa internacionalizado para su uso en una localidad en particular. Generalmente hecho por traductores.

Encontrarás a menudo "*localización*" abreviada como `L10N`.

## Pasos

Los tres pasos para usar la internacionalización en aplicaciones Django son:

1. Activa el middleware local en la configuración de Django.
2. Especifica las cadenas de traducción en el código Python y en las plantillas.
3. Implementa las traducciones para esas cadenas, en cualquiera de los lenguajes que quieras soportar.

### Paso 1: configuración de Django

Asegurarnos de tener activadas las traducciones en nuestra configuración. Hacer los siguientes cambios en el archivo `agency_project\config\settings.py`:

```python
LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'

USE_I18N = True
USE_L10N = True
USE_TZ = True
```

### Paso 2: Marcar texto a traducir

- **Texto en plantillas**
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

- **Texto en código python**

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

### Paso 3

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

**Compilar archivos de traducción**

Una vez tengamos nuestros archivos de traducción completos, procederemos a compilarlos con el siguiente comando:

`django-admin compilemessages`

Cuando compilemos nuestros archivos, ya podemos utilizar nuestro proyecto en el idioma especificado. Cada que uno de nuestros usuarios consulte nuestro proyecto aparecerá en su idioma. Para efectos de prueba, podemos cambiar el lenguaje del proyecto por inglés y observar los resultados:

`LANGUAGE_CODE = 'en-us'`

**Ejemplo de salida de comandos**

```bash
(my_env) C:\Users\agency_project>django-admin makemessages -l en_US
processing locale en_US

(my_env) C:\Users\agency_project>django-admin compilemessages
processing file django.po in C:\Users\agency_project\locale\en_US\LC_MESSAGES
```

## Ejercicio

1. Instalar los requerimientos:

`pip install -r requirements.txt`

2. En la rama `master` esta el proyecto base de django

3. En la rama `texts` se encuentra el proyecto de django con las configuraciones para la traducción de texto

4. En la rama `models` se encuentra el proyecto de django con las configuraciones para la traducción de modelos

*Nota:* Se versiono la base de datos para efectos del taller.

## Ayudas

A continuación encuentra pequeños bloques de código que serán de ayuda:

1. *Listar idiomas*

En el archivo `base.html`:

```python
{% get_current_language as LANGUAGE_CODE %}
{% get_available_languages as LANGUAGES %}
{% get_language_info_list for LANGUAGES as languages %}
```

2. *Cambiar banderas*

Ejemplo de código para mostrar botones de banderas:

```html
<!-- Brand and toggle get languange for better mobile display -->
<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex2-collapse" style="height: 2.5em;">
    {% if LANGUAGE_CODE == 'es' %}
        <span>
            <img src="{% static 'img/icons/es.png' %}" class="languageIcon" style="margin-top: -25% ">
        </span>
    {% endif %}
    {% if LANGUAGE_CODE == 'en' %}
        <span>
            <img src="{% static 'img/icons/en.png' %}" class="languageIcon" style="margin-top: -25% ">
        </span>
    {% endif %}
</button>
```

Ejemplo de código para cambiar botones de banderas:

```javascript
$(document).ready(function() {
    $('#lenguaje-es').click(function(){
        postLang("es");
        return false;
    });
    $('#lenguaje-en').click(function(){
        postLang("en");
        return false;
    });
});
function postLang(lenguaje){
   document.getElementById("lenguaje-seleccionado").value = lenguaje;
   document.getElementById("form-lenguaje").submit();
}
```

## Enlaces de Referencia

1. Documentación oficial de Django [Translation](https://docs.djangoproject.com/en/2.2/topics/i18n/translation/)
2. Libro de Django - [Capítulo 19](https://github.com/saul-g/El-libro-de-Django/blob/master/chapter19.rst)
3. Cómo traducir un sitio web con Django - [La logiadepython](lalogiadepython)
4. Template usado en el ejemplo [Agency](https://startbootstrap.com/themes/agency/)
