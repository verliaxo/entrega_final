from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Producto (models.Model):
    nombre=models.CharField(max_length=50)
    condicion=models.CharField(max_length=20)
    foto=models.ImageField(upload_to='productos', null=True, blank=True)
    fecha_ingreso=models.DateField(auto_now_add=True)
    descripcion = RichTextField()
    precio = models.IntegerField() 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)  # Relación con el modelo User
    
    def __str__(self):
        return f"{self.nombre} {self.condicion} {self.foto} {self.fecha_ingreso}"