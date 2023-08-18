from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Se define un formulario de registro personalizado a partir del formulario predeterminado de Django "UserCreationForm".
    
class RegistroUsuariosForm(UserCreationForm):   
    email = forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:     
        model = User    #Se establece el modelo al que se asocia el formulario.
        fields = ['username', 'email', 'password1', 'password2']    #Se especifican los campos que se mostrarán en el formulario.
        help_texts = {k:"" for k in fields}      #Se eliminan los textos de ayuda predeterminados de Django.

#Se define un formulario de edición del perfil personalizado a partir del formulario predeterminado de Django "UserCreationForm".
#Se agregan campos adicionales a los obligatorios utilizados para registrarse.

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'first_name', 'last_name' ] 
        #Saca los mensajes de ayuda
        help_texts = { k:"" for k in fields}

#Se define un formulario para cargar imágenes a partir la clase forms.Form de Django.

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)   