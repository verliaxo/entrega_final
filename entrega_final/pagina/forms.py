from django import forms
from pagina.models import *

class ProductoFormulario(forms.ModelForm):
    nombre=forms.CharField(max_length=50)
    condicion=forms.CharField(max_length=20)
    precio = forms.IntegerField()

    class Meta:
        model = Producto
        fields = ["nombre", "precio", "foto", "descripcion", "condicion"]  