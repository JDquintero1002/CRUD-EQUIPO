from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import permissions, routers, serializers, viewsets
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from equipos.api.router import router_equipo

# ==========================================
# 1. SERIALIZERS Y VIEWSETS (Configuración de Usuarios)
# ==========================================
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Registro del Router de Usuarios
router = routers.DefaultRouter()
router.register(r"users", UserViewSet)


# ==========================================
# 2. DEFINICIÓN DE SCHEMA_VIEW (Antes de urlpatterns)
# ==========================================
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


# ==========================================
# 3. PATRONES DE URL (Mapeo de Rutas)
# ==========================================
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rutas de Documentación Swagger y Redoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # Autenticación de la API
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    
    # Endpoints de los Routers
    path("", include(router.urls)),           # Rutas para usuarios en la raíz (/)
    path('api/', include(router_equipo.urls)), # Rutas para equipos bajo (/api/equipos/)
]