# Generated by Django 5.1.2 on 2024-11-04 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_contrato_duracion_del_contrato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='duracion_del_contrato',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
