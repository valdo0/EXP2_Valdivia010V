from dataclasses import fields
from rest_framework import serializers
from petsociety.models import Cliente
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['rutCliente','nombreCliente','correo','telefono','direccion']