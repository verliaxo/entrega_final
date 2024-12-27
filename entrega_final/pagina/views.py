from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from pagina.models import * 
from pagina.forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

class ProductoDetalleView(DetailView):
    model = Producto
    template_name = 'pagina/prod_detail.html'
    context_object_name = 'producto'

class ListaProductosView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'pagina/prod_lista.html'
    context_object_name = 'productos'

    def get_queryset(self):
        # Filtra los productos que pertenecen al usuario autenticado
        return Producto.objects.filter(user=self.request.user)

def lista_completa(request):
    productos = Producto.objects.all()
    return render(request, 'pagina/prod_todos.html', {'productos': productos, 'current_user': request.user})

@login_required
def ingresar_producto(request, username):
    if request.method == 'POST':  # Si se envió un formulario
        form = ProductoFormulario(request.POST, request.FILES)  # Procesar los datos enviados
        if form.is_valid():  # Validar el formulario
            # Extraer los datos validados del formulario
            nombre = form.cleaned_data['nombre']
            condicion = form.cleaned_data['condicion']
            descripcion = form.cleaned_data['descripcion']
            foto = form.cleaned_data['foto']
            precio = form.cleaned_data['precio']

            # Guardar los datos en la base de datos, asociando el producto al usuario
            p = Producto(
                nombre=nombre,
                condicion=condicion,
                precio = precio,
                foto=foto,
                descripcion=descripcion,
                user=request.user  # Asocia el producto al usuario
            )
            p.save()
            
            return redirect('lista_productos', username=request.user.username)  # Redirige a la página de inicio del usuario
    else:  # Si no se envió nada (GET)
        form = ProductoFormulario()  # Mostrar un formulario vacío

    return render(request, 'pagina/ingresar_producto.html', {'form': form})

@login_required
def actualizar_producto(request, username, pk):
    producto = get_object_or_404(Producto, pk=pk, user=request.user)  # Verifica que el producto pertenezca al usuario
    if request.method == 'POST':
        form = ProductoFormulario(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos', username=username)
    else:
        form = ProductoFormulario(instance=producto)
    return render(request, 'pagina/actualizar_producto.html', {'form': form})

@login_required
def eliminar_producto(request, username, pk):
    producto = get_object_or_404(Producto, pk=pk, user=request.user)  # Verifica que el producto pertenezca al usuario
    producto.delete()
    return redirect('lista_productos', username=username)