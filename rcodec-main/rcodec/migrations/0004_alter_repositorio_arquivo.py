# Generated by Django 4.0.3 on 2022-10-19 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rcodec', '0003_alter_repositorio_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repositorio',
            name='arquivo',
            field=models.FileField(blank=True, upload_to='upload/pdf'),
        ),
    ]
