from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
# from rest_framework.serializers import ModelSerializer

# from app_cinematic.models import *
from cinematica_app.models import *


class MembreciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membrecia
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    membrecia = MembreciaSerializer(read_only=True)
    membrecia_id = PrimaryKeyRelatedField(write_only=True, queryset=Membrecia.objects.all(), source='membrecia')

    class Meta:
        model = Usuario
        fields = '__all__'

        def create(self, validated_data):
            user = Usuario(
                username=validated_data['username'],
                email=validated_data['email'],
                telefono=validated_data['telefono'],
                direccion=validated_data['direccion'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
            )
            user.set_password(validated_data['password'])
            user.save()
            return user


class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = '__all__'


class CineSerializer(serializers.ModelSerializer):
    ciudad = CiudadSerializer(read_only=True)
    ciudad_id = PrimaryKeyRelatedField(write_only=True, queryset=Ciudad.objects.all(), source='ciudad')

    class Meta:
        model = Cine
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    cine = CineSerializer(read_only=True)
    cine_id = PrimaryKeyRelatedField(write_only=True, queryset=Cine.objects.all(), source='cine')

    class Meta:
        model = Producto
        fields = '__all__'


class ComboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combo
        fields = '__all__'


class ComboProductoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    producto_id = PrimaryKeyRelatedField(write_only=True, queryset=Producto.objects.all(), source='producto')

    combo = ComboSerializer(read_only=True)
    comobo_id = PrimaryKeyRelatedField(write_only=True, queryset=Combo.objects.all(), source='combo')

    class Meta:
        model = ComboProducto
        fields = '__all__'


class SalaSerializer(serializers.ModelSerializer):
    cine = CineSerializer(read_only=True)
    cine_id = PrimaryKeyRelatedField(write_only=True, queryset=Cine.objects.all(), source='cine')

    class Meta:
        model = Sala
        fields = '__all__'


class SillaSerializer(serializers.ModelSerializer):
    sala = SalaSerializer(read_only=True)
    sala_id = PrimaryKeyRelatedField(write_only=True, queryset=Sala.objects.all(), source='sala')

    class Meta:
        model = Silla
        fields = '__all__'


class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = '__all__'


class ProyeccionSerializer(serializers.ModelSerializer):
    sala = SalaSerializer(read_only=True)
    sala_id = PrimaryKeyRelatedField(write_only=True, queryset=Sala.objects.all(), source='sala')

    pelicula = PeliculaSerializer(read_only=True)
    pelicula_id = PrimaryKeyRelatedField(write_only=True, queryset=Pelicula.objects.all(), source='pelicula')

    class Meta:
        model = Proyeccion
        fields = '__all__'


class FacturacionBoletaSerializer(serializers.ModelSerializer):
    proyeccion = ProyeccionSerializer(read_only=True)
    proyeccion_id = PrimaryKeyRelatedField(write_only=True, queryset=Proyeccion.objects.all(), source='proyeccion')

    usuario = UsuarioSerializer(read_only=True)
    usuario_id = PrimaryKeyRelatedField(write_only=True, queryset=Usuario.objects.all(), source='usuario')  #

    class Meta:
        model = FacturacionBoleta
        fields = '__all__'
