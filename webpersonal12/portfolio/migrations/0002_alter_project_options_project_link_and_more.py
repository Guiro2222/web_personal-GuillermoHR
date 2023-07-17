# Generated by Django 4.2.2 on 2023-07-03 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="project",
            options={
                "ordering": ["-created"],
                "verbose_name": "proyecto",
                "verbose_name_plural": "proyectos",
            },
        ),
        migrations.AddField(
            model_name="project",
            name="link",
            field=models.URLField(blank=True, null=True, verbose_name="Dirección web"),
        ),
        migrations.AlterField(
            model_name="project",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Fecha de creación"
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="description",
            field=models.TextField(verbose_name="Descripción"),
        ),
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(upload_to="projects", verbose_name="Imagen"),
        ),
        migrations.AlterField(
            model_name="project",
            name="title",
            field=models.CharField(max_length=200, verbose_name="Título"),
        ),
        migrations.AlterField(
            model_name="project",
            name="updated",
            field=models.DateTimeField(
                auto_now=True, verbose_name="Fecha de modificación"
            ),
        ),
    ]
