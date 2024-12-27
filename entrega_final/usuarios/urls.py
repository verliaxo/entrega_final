from django.urls import path, include
from usuarios.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('about/',acerca_pagina,name="acerca_pagina"),
    path('login/',iniciar_sesion,name="iniciar_sesion"),
    path('register/',registrarse,name="registrarse"),
    path('profile/update/<int:pk>/',actualizar_perfil,name="actualizar_perfil"),
    path('profile/<int:pk>/',perfil,name="perfil"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/about/<int:pk>',acerca_de_mi,name="acerca_de_mi"),
    path('profile/about/edit/<int:pk>',editar_descripcion,name="editar_descripcion"),
    path('pagina/',include('pagina.urls')),
    path('lista/',lista_usuarios,name="lista_usuarios"),
]

