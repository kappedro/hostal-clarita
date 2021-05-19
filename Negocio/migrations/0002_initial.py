# Generated by Django 3.2.3 on 2021-05-19 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Usuarios', '0001_initial'),
        ('Negocio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordendecompra',
            name='rut_cliente',
            field=models.ForeignKey(db_column='rut_cliente', on_delete=django.db.models.deletion.PROTECT, to='Usuarios.cliente'),
        ),
        migrations.AddField(
            model_name='huesped',
            name='id_orden_compra',
            field=models.ForeignKey(db_column='id_orden_compra', on_delete=django.db.models.deletion.CASCADE, to='Negocio.ordendecompra'),
        ),
        migrations.AddField(
            model_name='huesped',
            name='nro_habitacion',
            field=models.ForeignKey(db_column='nro_habitacion', on_delete=django.db.models.deletion.CASCADE, to='Negocio.habitacion'),
        ),
        migrations.AddField(
            model_name='factura',
            name='id_orden_compra',
            field=models.OneToOneField(db_column='id_orden_compra', on_delete=django.db.models.deletion.CASCADE, to='Negocio.ordendecompra'),
        ),
    ]
