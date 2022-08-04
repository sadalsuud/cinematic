from django.urls import path, include
from rest_framework import routers

# from cinematic.cinematic_app.views import CiudadView, CineView, ProductoView, ComboView, ComboProductoView, SillaView, \
#     PeliculaView, ClienteView, FacturacionBoletaView, MembreciaView

# from ..cinematic_app.views import *
# from cinematic_app.views import *
from cinematica_app.views import *

router = routers.DefaultRouter()
router.register('ciudad', CiudadView, basename='ciudad')
router.register('cine', CineView, basename='cine')
router.register('producto', ProductoView, basename='producto')
router.register('combo', ComboView, basename='combo')
router.register('comboProducto', ComboProductoView, basename='comboProducto')
router.register('sala', SalaView, basename='sala')
router.register('silla', SillaView, basename='silla')
router.register('pelicula', PeliculaView, basename='pelicula')
router.register('usuario', UsuarioView, basename='usuario')
router.register('facturacionBoleta', FacturacionBoletaView, basename='facturacionBoleta')
router.register('membrecia', MembreciaView, basename='membrecia')

urlpatterns = [
    # esto hace referencia a las url de arriba, protegidas o sea las de los modelos ...
    path('', include(router.urls)),
    # esta es la url que me va a dar el token cuando el usuario existe pero no tiene token
    path('token', CustomAuthToken.as_view(), name='token'),
]
