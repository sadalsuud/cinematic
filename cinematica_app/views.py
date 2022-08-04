from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
# from app_cinematic.Serializer import *
# from app_cinematic.models import *
from cinematica_app.Serializer import *
from cinematica_app.models import *


class UsuarioView(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    @action(methods=['post'], detail=True)
    def set_membrecia(self, request):
        membrecia = self.get_object()
        serializer = MembreciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(membrecia=membrecia)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class CiudadView(ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer


class CineView(ModelViewSet):
    queryset = Cine.objects.all()
    serializer_class = CineSerializer

    @action(methods=['post'], detail=True)
    def set_ciudad(self, request):
        ciudad = self.get_object()
        serializer = CiudadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ciudad=ciudad)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ProductoView(ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    @action(methods=['post'], detail=True)
    def set_cine(self, request):
        cine = self.get_object()
        serializer = CineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cine=cine)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ComboView(ModelViewSet):
    queryset = Combo.objects.all()
    serializer_class = ComboSerializer


class ComboProductoView(ModelViewSet):
    queryset = ComboProducto.objects.all()
    serializer_class = ComboProductoSerializer

    @action(methods=['post'], detail=True)
    def set_producto(self, request):
        producto = self.get_object()
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(producto=producto)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True)
    def set_combo(self, request):
        combo = self.get_object()
        serializer = ComboSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(combo=combo)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class SalaView(ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

    @action(methods=['post'], detail=True)
    def set_cine(self, request):
        cine = self.get_object()
        serializer = CineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cine=cine)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class SillaView(ModelViewSet):
    queryset = Silla.objects.all()
    serializer_class = SillaSerializer

    @action(methods=['post'], detail=True)
    def set_sala(self, request):
        sala = self.get_object()
        serializer = SalaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(sala=sala)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class PeliculaView(ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer


class ProyeccionView(ModelViewSet):
    queryset = Proyeccion.objects.all()
    serializer_class = ProyeccionSerializer

    @action(methods=['post'], detail=True)
    def set_sala(self, request):
        sala = self.get_object()
        serializer = SalaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(sala=sala)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True)
    def set_pelicula(self, request):
        pelicula = self.get_object()
        serializer = PeliculaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(pelicula=pelicula)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class MembreciaView(ModelViewSet):
    queryset = Membrecia.objects.all()
    serializer_class = MembreciaSerializer


class FacturacionBoletaView(ModelViewSet):
    queryset = FacturacionBoleta.objects.all()
    serializer_class = FacturacionBoletaSerializer

    @action(methods=['post'], detail=True)
    def set_proyeccion(self, request):
        proyeccion = self.get_object()
        serializer = ProyeccionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(proyeccion=proyeccion)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True)
    def set_usuario(self, request):
        usuario = self.get_object()
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(usuario=usuario)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token_actual = Token.objects.filter(user=user).first()
        if token_actual:
            token_actual.delete()

        token, created = Token.objects.get_or_create(user=user)
        user.token = token.key
        user.save()
        usuario = UsuarioSerializer(user)
        return Response(usuario.data)
