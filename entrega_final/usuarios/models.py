from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"{self.imagen}"

class Descripcion(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = RichTextField()

    def __str__(self):
        return f"{self.descripcion}"


