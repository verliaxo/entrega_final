from django import forms
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Avatar, Descripcion

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña',widget=forms.PasswordInput)
    nacimiento = forms.DateField()

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "nacimiento", "email", "password1", "password2"]

class UserEditForm(UserChangeForm):
    new_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Nueva contraseña",
        help_text="Deja este campo vacío si no deseas cambiar la contraseña."
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

        labels = {
            'email': 'Correo',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
        }
# suprimir campo original de django de contraseña
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'password' in self.fields:
            del self.fields['password']

    def save(self, commit=True):
        user = super().save(commit=False)
        new_password = self.cleaned_data.get('new_password')

        if new_password:  # Si se proporcionó una nueva contraseña
            user.set_password(new_password)

        if commit:
            user.save()
        return user


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']

class DescripcionForm(forms.ModelForm):
    class Meta:
        model = Descripcion
        fields = ['descripcion']
