# Generated by Django 5.1.2 on 2024-10-29 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_entidad', models.CharField(max_length=255)),
                ('nit_entidad', models.CharField(max_length=50)),
                ('departamento', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('localizacion', models.CharField(max_length=255)),
                ('orden', models.CharField(max_length=50)),
                ('sector', models.CharField(max_length=100)),
                ('rama', models.CharField(max_length=100)),
                ('entidad_centralizada', models.CharField(max_length=50)),
                ('proceso_de_compra', models.CharField(max_length=100)),
                ('id_contrato', models.CharField(max_length=100, unique=True)),
                ('referencia_del_contrato', models.CharField(max_length=100)),
                ('estado_contrato', models.CharField(max_length=100)),
                ('codigo_de_categoria_principal', models.CharField(max_length=100)),
                ('descripcion_del_proceso', models.TextField()),
                ('tipo_de_contrato', models.CharField(max_length=100)),
                ('modalidad_de_contratacion', models.CharField(max_length=100)),
                ('justificacion_modalidad', models.TextField()),
                ('fecha_de_firma', models.DateTimeField(null=True)),
                ('fecha_de_inicio_del_contrato', models.DateTimeField(null=True)),
                ('fecha_de_fin_del_contrato', models.DateTimeField(null=True)),
                ('condiciones_de_entrega', models.CharField(max_length=100)),
                ('tipodocproveedor', models.CharField(max_length=50)),
                ('documento_proveedor', models.CharField(max_length=50)),
                ('proveedor_adjudicado', models.CharField(max_length=255)),
                ('es_grupo', models.CharField(max_length=50)),
                ('es_pyme', models.CharField(max_length=50)),
                ('habilita_pago_adelantado', models.CharField(max_length=50)),
                ('liquidacion', models.CharField(max_length=50)),
                ('obligacion_ambiental', models.CharField(max_length=50)),
                ('obligaciones_postconsumo', models.CharField(max_length=50)),
                ('reversion', models.CharField(max_length=50)),
                ('origen_de_los_recursos', models.CharField(max_length=100)),
                ('destino_gasto', models.CharField(max_length=100)),
                ('valor_del_contrato', models.DecimalField(decimal_places=2, max_digits=50)),
                ('valor_de_pago_adelantado', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('valor_facturado', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('valor_pendiente_de_pago', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('valor_pagado', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('valor_amortizado', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('valor_pendiente_de', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('valor_pendiente_de_ejecucion', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('estado_bpin', models.CharField(max_length=100)),
                ('codigo_bpin', models.CharField(max_length=100)),
                ('anno_bpin', models.CharField(max_length=50)),
                ('saldo_cdp', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('saldo_vigencia', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('es_postconflicto', models.CharField(max_length=50)),
                ('dias_adicionados', models.IntegerField(default=0)),
                ('puntos_del_acuerdo', models.CharField(max_length=100)),
                ('pilares_del_acuerdo', models.CharField(max_length=100)),
                ('url_proceso', models.URLField()),
                ('nombre_representante_legal', models.CharField(max_length=255)),
                ('nacionalidad_representante_legal', models.CharField(max_length=50)),
                ('domicilio_representante_legal', models.CharField(max_length=255)),
                ('tipo_de_identificacion_representante_legal', models.CharField(max_length=100)),
                ('identificacion_representante_legal', models.CharField(max_length=100)),
                ('genero_representante_legal', models.CharField(max_length=20)),
                ('presupuesto_general_de_la_nacion_pgn', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('sistema_general_de_participaciones', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('sistema_general_de_regalias', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('recursos_propios_alcaldias_gobernaciones_y_resguardos_indigenas', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('recursos_de_credito', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('recursos_propios', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('ultima_actualizacion', models.DateTimeField(null=True)),
                ('codigo_entidad', models.CharField(max_length=100)),
                ('codigo_proveedor', models.CharField(max_length=100)),
                ('fecha_inicio_liquidacion', models.DateTimeField(null=True)),
                ('fecha_fin_liquidacion', models.DateTimeField(null=True)),
                ('objeto_del_contrato', models.TextField()),
                ('duracion_del_contrato', models.DateTimeField(null=True)),
                ('nombre_del_banco', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo_de_cuenta', models.CharField(blank=True, max_length=50, null=True)),
                ('numero_de_cuenta', models.CharField(blank=True, max_length=50, null=True)),
                ('el_contrato_puede_ser_prorrogado', models.BooleanField(default=False)),
                ('nombre_ordenador_del_gasto', models.CharField(max_length=255)),
                ('tipo_de_documento_ordenador_del_gasto', models.CharField(max_length=100)),
                ('numero_de_documento_ordenador_del_gasto', models.CharField(max_length=100)),
                ('nombre_supervisor', models.CharField(max_length=255)),
                ('tipo_de_documento_supervisor', models.CharField(max_length=100)),
                ('numero_de_documento_supervisor', models.CharField(max_length=100)),
                ('nombre_ordenador_de_pago', models.CharField(max_length=255)),
                ('tipo_de_documento_ordenador_de_pago', models.CharField(max_length=100)),
                ('numero_de_documento_ordenador_de_pago', models.CharField(max_length=100)),
                ('fecha_de_notificacion_de_prorroga', models.DateTimeField(null=True)),
            ],
        ),
    ]
