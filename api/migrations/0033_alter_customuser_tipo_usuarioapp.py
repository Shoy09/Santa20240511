# Generated by Django 4.0 on 2024-11-05 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_alter_importarasistenciadetalle_idconsumidor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='tipo_usuarioapp',
            field=models.CharField(choices=[('Administrador', 'Administrador'), ('Proceso', 'Proceso'), ('Supervisor', 'Supervisor')], default='Administrador', max_length=25),
        ),
    ]
