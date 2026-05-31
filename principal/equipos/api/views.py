from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from equipos.models import Equipo
from equipos.api.serializers import EquipoSerializer


class EquipoViewSet(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class   = EquipoSerializer
    queryset           = Equipo.objects.all()