# Generated by Django 4.0 on 2024-11-05 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_alter_customuser_tipo_usuarioapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importarasistenciadetalle',
            name='idconsumidor',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
