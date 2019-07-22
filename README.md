# Internacionalización con Django

Django ofrece un robusto framework de internacionalización y localización para ayudarte a desarrollo aplicaciones para múltiples idiomas y regiones del mundo.

En este taller vamos aprender los conceptos relacionados con la internacionalización de aplicaciones web y vamos a realizar un ejemplo traducción del contenido estatico y dinamico de un sitio web.

## Conceptos

1. **Internacionalización:** proceso de diseñar programas para el uso potencial de cualquier localidad (ciudad, país). Es decir poder traducir a diferentes idiomas elementos de la interfaz, texto, mensajes de error, y además configurar elementos como fechas y horas, de manera que sea posible respetar diferentes estándares locales. Generalmente hecho por desarrolladores.

`Dato curioso:` Encontrarás a menudo "*internacionalización*" abreviada como `I18N` dónde el número 18 se refiere al número de letras omitidos entre la `I` inicial y la `N` final.

2. **Localización:** proceso específico de traducir un programa internacionalizado para su uso en una localidad en particular. Generalmente hecho por traductores.

Encontrarás a menudo "*localización*" abreviada como `L10N`.

## Pasos

1. settings
2. urls
3. views
4. templates

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
2. Cómo traducir un sitio web con Django - [La logiadepython](lalogiadepython)
3. Template usado en el ejemplo [Agency](https://startbootstrap.com/themes/business-corporate/)
