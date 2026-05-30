from rest_framework.routers import DefaultRouter
from equipos.api.views import EquipoViewSet

router_equipo = DefaultRouter()
router_equipo.register(
    prefix='equipos',
    viewset=EquipoViewSet,
    basename='equipos'
)

urlpatterns = router_equipo.urls