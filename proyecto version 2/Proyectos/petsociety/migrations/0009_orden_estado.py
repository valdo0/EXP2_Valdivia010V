# Generated by Django 4.0.4 on 2022-07-15 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petsociety', '0008_direccionenvio'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='petsociety.estado', verbose_name='Estado de orden'),
        ),
    ]
