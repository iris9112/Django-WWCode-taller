from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Service(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=200, verbose_name=_("Nombre")),
        description = models.TextField(verbose_name=_("Descripción"))
    )
    
    fa_icon = models.CharField(max_length=50, verbose_name=_("Icono"))
    class Meta:
        verbose_name = _("Servicio")
        verbose_name_plural = _("Servicios")

    def __str__(self):
        return self.name


class Project(models.Model):

    CATEGORIES_PROJECT = (
        ('1', _('Diseño web')),
        ('2', _('Mercadeo')),
        ('3', _('Diseño gráfico')),
        ('4', _('Fotografía')),
    )

    name = models.CharField(max_length=200, verbose_name=_("Nombre"))
    title = models.CharField(max_length=200, verbose_name=_("Título"))
    description = models.TextField(verbose_name=_("Descripción"))
    image = models.ImageField(verbose_name=_("Imagen"), upload_to="projects")
    category = models.CharField(max_length=255, verbose_name=_("Categoria"), choices=CATEGORIES_PROJECT)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Fecha de creación"))

    class Meta:
        verbose_name = _("proyecto")
        verbose_name_plural = _("proyectos")
        ordering = ["-created"]

    def __str__(self):
        return self.name