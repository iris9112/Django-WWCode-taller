# Pasos para tradución de modelos

Para internacionalizar los modelos haremos uso de la libreria [`Django Parler`](https://django-parler.readthedocs.io/)

## Paso 1: Configuración en settings

Edita el archivo `settings.py` y adiciona `parler` a las aplicaciones instaladas:

```python
INSTALLED_APPS = [
    ...
    'parler',
    ...
]
```

Luego continua con las configuraciones de Django Parler

```python
PARLER_LANGUAGES = {
    None: (
        {'code': 'es', },
        {'code': 'en', },
    ),
    'default': {
        'fallback': 'es',
        'hide_untranslated': False,
    }
}

PARLER_DEFAULT_LANGUAGE = 'es'
PARLER_SHOW_EXCLUDED_LANGUAGE_TABS = True
```

- Dentro del diccionario de PARLER_LANGUAGES, use `SITE_ID` en lugar de `None` si tiene varios sitios en el proyecto. Cada SITE_ID puede ser agregado como entrada adicional en el diccionario.

- `hide_untranslated` por defecto esta como `False`, lo que quiere decir que no oculte el texto no traducido en el sitio.

- El parametro `PARLER_DEFAULT_LANGUAGE` permite asignar un lenguaje por defecto. Sino se especifica usará el mismo valor definido en `LANGUAGE_CODE`

- Por defecto, las pestañas de administración están limitadas a los códigos de idioma encontrados en `LANGUAGES` Si los modelos tienen otras traducciones, se pueden mostrar estableciendo el valor `PARLER_SHOW_EXCLUDED_LANGUAGE_TABS` en `True`.

## Paso 2: Modificación de modelos para traducciones

`Django-parler` ofrece la clase `TranslatedModel` para los modelos y el _wrapper_ `TranslatedFields` para envolver los campos de los modelos que se quieren traducir.

```python
# models.py
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=200, verbose_name=_('Nombre Categoría'))
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Fecha de creación"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Fecha de edición"))

    class Meta:
        verbose_name = _('Categoría')
        verbose_name_plural = _('Categorías')

```

El modelo `Category` ahora hereda de `TranslatedModel` en lugar de `models.Model`, y el campo `name` es incluido en el _wrapper_.

## Integrando traducciones en el sitio de administración

`Django-parler` administra las traducciones y genera una tabla adicional por cada modelo a traducir, llamada _app_model_translation_. En la intefaz de administración crea una nueva pestaña (tab) para cada idioma a usarse, para ello es necesario hacer que los modelos hereden de `TranslatableAdmin`:

```python
# admin.py

from parler.admin import TranslatableAdmin
from .models import Service

@admin.register(Service)
class ServiceAdmin(TranslatableAdmin):
    pass
```

## Creando migraciones para los modelos de traducciones

**Consideraciones**

- No trabaja sobre el campo ordering: La actual versión (1.9.2) de `Django-parler` **no** soporta usar un campo de traducción entre el listado de campos a ordenar.

- Borra los campos existentes de la base de datos por lo que debes ingresar de nuevo toda tu información
