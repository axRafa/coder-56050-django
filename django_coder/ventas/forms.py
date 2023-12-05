from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField()
    nro_cuit = forms.IntegerField()
    email = forms.EmailField()