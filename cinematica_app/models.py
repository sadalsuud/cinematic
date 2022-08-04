from django.db import models
from django.contrib.auth.models import AbstractUser


class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=10)


class Cine(models.Model):
    nombre = models.CharField(max_length=50)
    representante = models.CharField(max_length=150)
    telefono = models.CharField(max_length=10)
    web = models.CharField(max_length=40)
    direccion = models.CharField(max_length=100)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.RESTRICT)


class Producto(models.Model):
    nombre = models.CharField(max_length=20)
    codigo = models.IntegerField(default=0)
    tamanio = models.CharField(max_length=3)
    precio = models.IntegerField(default=0)
    cine = models.ForeignKey(Cine, on_delete=models.RESTRICT)


class Combo(models.Model):
    nombre = models.CharField(max_length=150)
    precio = models.IntegerField(default=0)


class ComboProducto(models.Model):
    cantidad = models.IntegerField(default=0)
    producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)
    combo = models.ForeignKey(Combo, on_delete=models.RESTRICT)


class Sala(models.Model):
    total_sillas = models.IntegerField(default=0)
    numero = models.CharField(max_length=1)
    cine = models.ForeignKey(Cine, on_delete=models.RESTRICT)


class Silla(models.Model):
    ocupada = models.BooleanField(default=False)
    codigo = models.CharField(max_length=3)
    activa = models.BooleanField(default=True)
    sala = models.ForeignKey(Sala, on_delete=models.RESTRICT)


class Pelicula(models.Model):
    nombre = models.CharField(max_length=255)
    clasificacion = models.CharField(max_length=5)
    director = models.CharField(max_length=50)
    genero = models.CharField(max_length=10)


class Proyeccion(models.Model):
    hora_inicio = models.TimeField(auto_now_add=True)
    hora_fin = models.TimeField(auto_now_add=True)
    sala = models.ForeignKey(Sala, on_delete=models.RESTRICT)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.RESTRICT)


class Membrecia(models.Model):
    nombre = models.CharField(max_length=10)
    descuento = models.IntegerField(default=0)


class Usuario(AbstractUser):
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    membrecia = models.ForeignKey(Membrecia, on_delete=models.RESTRICT)
    token = models.TextField(blank=True, null=True, default="")


class FacturacionBoleta(models.Model):
    fecha_compra = models.DateTimeField(auto_now=True)
    valor = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=1)
    sillas = models.TextField(blank=False)
    proyeccion = models.ForeignKey(Proyeccion, on_delete=models.RESTRICT)
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT)
