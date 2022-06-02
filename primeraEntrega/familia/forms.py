from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    email = forms.EmailField(label="Email")
    # input_format hace que se pueda ingresar la fecha con el formato latino, dia/mes/año
    fecha_nacimiento = forms.DateField(label="fecha_nacimiento", input_formats=["%d/%m/%Y"],
    #widget es para poder agregar un tip para que el usuario sepa como ingresar la fecha
    widget=forms.TextInput(attrs={'placeholder': '30/12/1995'}))
    altura = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': "1.75 m"}))
    tipo = forms.CharField(label="Modelo del vehiculo",max_length=100)
    marca = forms.CharField(label="Marca del vehiculo",max_length=100)
    modelo = forms.IntegerField(label="Modelo del vehiculo", max_value=20)
    especie = forms.CharField(label="Especie de animal", max_length=100)
    raza = forms.CharField(label="Raza del animal", max_length=100)
    edad = forms.IntegerField(label="Años del animal", max_value=20)
    





class ActualizarPersonaForm(PersonaForm):
    id = forms.IntegerField(widget = forms.HiddenInput())


class BuscarPersonasForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")