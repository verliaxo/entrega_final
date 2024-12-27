from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from usuarios.forms import *
from usuarios.models import * 

def mostrar_inicio(request):
    return render(request, "usuarios/index.html")

def acerca_pagina(request):
    return render(request, "usuarios/about_page.html")

def iniciar_sesion(request):
    msg_login = ""

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.cleaned_data.get('username')
            pword = form.cleaned_data.get('password')
        
            usuario = authenticate(username=user, password=pword)

            if usuario is not None:  # Verificar si el usuario autenticado es válido
                login(request, usuario)  # Usar el objeto 'usuario' aquí
                return redirect("lista_usuarios")

            msg_login = "Los datos ingresados son incorrectos."

    else:
        form = AuthenticationForm()

    return render(request, "usuarios/login.html", {"form": form, "msg_login": msg_login})

def registrarse(request):
    msg_register = ""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("iniciar_sesion") 
        else:
            msg_register = "Error en los datos ingresados."  # Esto es redundante, puedes usar form.errors en la plantilla

    else:
        form = UserRegisterForm()

    return render(request, "usuarios/register.html", {"form": form, "msg_register": msg_register})

@login_required
def actualizar_perfil(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    user_id = usuario.id

    if request.method == "POST":
        form = UserEditForm(request.POST, instance=request.user)

        try:
            avatar = request.user.avatar
        except Avatar.DoesNotExist:
            avatar = None

        if avatar:
            avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)
        else:
            avatar_form = AvatarForm(request.POST, request.FILES)

        if form.is_valid() and avatar_form.is_valid():
            form.save()
            avatar_instance = avatar_form.save(commit=False)
            avatar_instance.user = request.user 
            avatar_instance.save()
            return redirect("perfil",pk=user_id)
    
    else:
        form = UserEditForm(instance=request.user)
        if hasattr(request.user, "avatar"):
            avatar_form = AvatarForm(instance=request.user.avatar)
        else:
            avatar_form = AvatarForm()

    return render(request,"usuarios/update_user.html",{"form": form, "avatar_form": avatar_form, "user_pk": user_id})

def perfil(request,pk):
    usuario = get_object_or_404(User, pk=pk)
    user_id = usuario.id
    return render(request, "usuarios/profile.html", {"usuario": usuario, "user_pk": user_id})

def acerca_de_mi(request,pk):
    usuario = get_object_or_404(User, pk=pk)
    user_id = usuario.id
    return render(request, "usuarios/about.html", {"usuario": usuario, "user_pk": user_id})

@login_required
def editar_descripcion(request,pk):
    # Obtiene o crea el objeto Descripcion relacionado con el usuario actual
    about_me, created = Descripcion.objects.get_or_create(user=request.user)

    usuario = get_object_or_404(User, pk=pk)
    user_id = usuario.id

    if request.method == 'POST':
        form = DescripcionForm(request.POST, instance=about_me)
        if form.is_valid():
            form.save()
            return redirect('acerca_de_mi',pk=user_id)  # Asegúrate de que esta URL sea válida
    else:
        form = DescripcionForm(instance=about_me)

    return render(request, 'usuarios/about_edit.html', {'form': form})

def lista_usuarios(request):
    list_users = User.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'users': list_users})