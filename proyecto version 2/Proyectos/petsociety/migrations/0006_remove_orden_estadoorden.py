# Generated by Django 4.0.4 on 2022-07-12 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petsociety', '0005_orden_completado_alter_orden_cliente_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orden',
            name='estadoOrden',
        ),
    ]
