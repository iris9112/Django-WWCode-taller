# Generated by Django 2.2.3 on 2019-07-23 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('1', 'Diseño web'), ('2', 'Mercadeo'), ('3', 'Diseño gráfico'), ('4', 'Fotografía')], max_length=255, verbose_name='Categoria'),
        ),
    ]
