# Generated by Django 2.2 on 2023-07-17 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votaciones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrovotostest',
            name='validacion_usuario',
        ),
        migrations.AddField(
            model_name='registrovotostest',
            name='correo_electronico',
            field=models.CharField(default='correo@example.com', max_length=120),
        ),
        migrations.AddField(
            model_name='registrovotostest',
            name='pasaporte',
            field=models.CharField(default='1111111', max_length=120),
        ),
    ]