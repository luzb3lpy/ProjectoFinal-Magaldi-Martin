from django import forms
 
class FamiliaresFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email=forms.EmailField()
    dni = forms.IntegerField()

class AmigosFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email=forms.EmailField()
    dni = forms.IntegerField()

class ReferidosFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email=forms.EmailField()
    dni = forms.IntegerField()