# Internacionalización con Django :earth_americas:

Django ofrece un robusto framework de internacionalización y localización para ayudarte a desarrollo aplicaciones para múltiples idiomas y regiones del mundo.

En este taller vamos aprender los conceptos relacionados con la internacionalización de aplicaciones web y vamos a realizar un ejemplo traducción del contenido estatico y dinamico de un sitio web.

## Conceptos :speech_balloon:

1. **Internacionalización:** proceso de diseñar programas para el uso potencial de cualquier localidad (ciudad, país). Es decir poder traducir a diferentes idiomas elementos de la interfaz, texto, mensajes de error, y además configurar elementos como fechas y horas, de manera que sea posible respetar diferentes estándares locales. Generalmente hecho por desarrolladores.

`Dato curioso:` Encontrarás a menudo "*internacionalización*" abreviada como `I18N` dónde el número 18 se refiere al número de letras omitidos entre la `I` inicial y la `N` final.

2. **Localización:** proceso específico de traducir un programa internacionalizado para su uso en una localidad en particular. Generalmente hecho por traductores.

Encontrarás a menudo "*localización*" abreviada como `L10N`.

## Pasos :key:

Los tres pasos para usar la internacionalización en aplicaciones Django son:

1. Activa el middleware local en la configuración de Django.
2. Especifica las cadenas de traducción en el código Python y en las plantillas.
3. Implementa las traducciones para esas cadenas, en cualquiera de los lenguajes que quieras soportar.

Para ver el detalle ir al archivo Pasos traducción.

## Ejercicio :pushpin:

1. Instalar los requerimientos:

`pip install -r requirements.txt`

2. En la rama `master` esta el proyecto base de django

3. En la rama `texts` se encuentra el proyecto de django con las configuraciones para la traducción de texto

4. En la rama `models` se encuentra el proyecto de django con las configuraciones para la traducción de modelos

*Nota:* Se versiono la base de datos para efectos del taller.

## Enlaces de Referencia :bulb:

1. Documentación oficial de Django [Translation](https://docs.djangoproject.com/en/2.2/topics/i18n/translation/)
2. Libro de Django - [Capítulo 19](https://github.com/saul-g/El-libro-de-Django/blob/master/chapter19.rst)
3. Cómo traducir un sitio web con Django - [La logiadepython](lalogiadepython)
4. Template usado en el ejemplo [Agency](https://startbootstrap.com/themes/agency/)
