from django import forms

class CrearUsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    correo = forms.CharField(max_length=40)
    
class BuscarUsuario(forms.Form):
    nombre = forms.CharField(max_length=40,required=False)