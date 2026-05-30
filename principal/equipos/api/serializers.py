from rest_framework import serializers
from equipos.models import Equipo


class EquipoSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Equipo
        fields = [
            'id', 'nombre', 'codigo', 'tipo',
            'descripcion', 'ubicacion',
            'fecha_adquisicion', 'activo',
        ]
        read_only_fields = ['id']
