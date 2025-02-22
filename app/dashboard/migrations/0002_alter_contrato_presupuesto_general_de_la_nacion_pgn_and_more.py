# Generated by Django 5.1.2 on 2024-10-29 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='presupuesto_general_de_la_nacion_pgn',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='recursos_de_credito',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='recursos_propios',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='recursos_propios_alcaldias_gobernaciones_y_resguardos_indigenas',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='saldo_cdp',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='saldo_vigencia',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='sistema_general_de_participaciones',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='sistema_general_de_regalias',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='valor_amortizado',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='valor_de_pago_adelantado',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='valor_del_contrato',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='valor_facturado',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='valor_pagado',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='valor_pendiente_de',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='valor_pendiente_de_ejecucion',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='valor_pendiente_de_pago',
            field=models.BigIntegerField(default=0),
        ),
    ]
