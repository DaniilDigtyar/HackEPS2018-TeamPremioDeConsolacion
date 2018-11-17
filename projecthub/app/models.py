from django.db import models
from django.utils import timezone

class Rol(models.Model):
    rol = models.CharField(primary_key=True ,max_length=30)

class Estado(models.Model):
    estado = models.CharField(primary_key=True ,max_length=30)

class Usuarios(models.Model):
    nombre_usuario = models.CharField(primary_key=True ,max_length=30)
    contrasenya = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    rol = models.ForeignKey(Rol,related_name='rol_usuarios', on_delete=models.CASCADE)

class PalabrasClave(models.Model):
    palabra = models.CharField(primary_key=True, max_length=30)

class Notificaciones(models.Model):
    id_mensaje = models.CharField(primary_key=True ,max_length=30)
    mensaje = models.CharField(max_length=30)
    de = models.ForeignKey(Usuarios,related_name='de_notificaciones', on_delete=models.CASCADE)
    para = models.ForeignKey(Usuarios,related_name='para_notificaciones', on_delete=models.CASCADE)

class Ficheros(models.Model):
    id_fichero = models.CharField(primary_key=True ,max_length=10)
    owner = models.ForeignKey(Usuarios,related_name='owner_ficheros' ,on_delete=models.CASCADE)
    ruta = models.CharField(max_length=30)

class Proyecto(models.Model):
    titulo = models.TextField()
    descripcion = models.TextField()
    id_proyecto = models.CharField(primary_key=True ,max_length=10)
    creador  = models.ForeignKey(Usuarios,related_name='creador_proyecto', on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado,related_name='estado_proyecto', on_delete=models.CASCADE)
    director = models.ForeignKey(Usuarios,related_name='director_proyecto', on_delete=models.CASCADE)
    alumno  = models.ForeignKey(Usuarios,related_name='alumno_proyecto', on_delete=models.CASCADE)
#N - N
class ProyectoFichero(models.Model):
    proyecto = models.ForeignKey(Proyecto,related_name='proyecto_proyectofichero', on_delete=models.CASCADE)
    fichero = models.ForeignKey(Ficheros,related_name='fichero_proyectofichero', on_delete=models.CASCADE)

class PalabrasClaveProyecto(models.Model):
    proyecto = models.ForeignKey(Proyecto,related_name='proyecto_palabrasclaveproyecto', on_delete=models.CASCADE)
    palabra = models.ForeignKey(PalabrasClave,related_name='palabra_palabrasclaveproyecto', on_delete=models.CASCADE)
