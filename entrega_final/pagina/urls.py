from django.urls import path, include
from pagina.views import *


urlpatterns = [
    path('productos/lista',lista_completa,name="lista_completa"),
    path('productos/<int:pk>',ProductoDetalleView.as_view(),name="producto_detalle"),
    path('productos/<str:username>/ingreso',ingresar_producto,name="ingresar_producto"),
    path('productos/<str:username>/mis_productos',ListaProductosView.as_view(), name='lista_productos'),
    path('productos/<str:username>/actualizar/<int:pk>',actualizar_producto,name="actualizar_producto"),
    path('productos/<str:username>/eliminar/<int:pk>',eliminar_producto,name="eliminar_producto"),
]
