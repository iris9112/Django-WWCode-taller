from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    fa_icon = models.CharField(max_length=50, verbose_name="Icono")
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.name


class Project(models.Model):

    CATEGORIES_PROJECT = [
        (1, 'Website Design'),
        (2, 'Marketing'),
        (3, 'Graphic Design'),
        (4, 'Photography'),
    ]

    name = models.CharField(max_length=200, verbose_name="Nombre")
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    category = models.URLField(verbose_name="Categoria", choices=CATEGORIES_PROJECT)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.name