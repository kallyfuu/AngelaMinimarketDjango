from django.db import models

# Create your models here.
class Panesbd(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    nuevo = models.BooleanField()
    imagen =models.ImageField(upload_to="Panes",null=True)

    def __str__(self):
        return self.nombre
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre