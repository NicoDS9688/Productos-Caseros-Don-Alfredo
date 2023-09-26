""" Core forms """
# Core
from datetime import date, timedelta

from apps.core.models import LiqueurSize

# Django
from django import forms


class ProductOrderForm(forms.Form):
    """Form para cantidad de productos"""
    quantity = forms.IntegerField(
        min_value=1,
        initial=1,
        label='Cantidad',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '1'}),
        required=True,
    )


class LiqueurOrderForm(forms.Form):
    """Form para elegir tamaño de licor"""
    size = forms.ModelChoiceField(
        queryset=LiqueurSize.objects.all(),
        label='Tamaño',
        required=True,
        empty_label=None,
        to_field_name='name',
    )
    quantity = forms.IntegerField(
        min_value=1,
        initial=1,
        label='Cantidad',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '1'}),
        required=True,
    )


class CakeOrderForm(forms.Form):
    SHAPE_CHOICES = [
        ('redonda', 'Redonda'),
        ('rectangular', 'Rectangular'),
        ('corazón', 'Forma de corazón'),
    ]

    FLAVOR_CHOICES = [
        ('vanilla', 'Vainilla'),
        ('chocolate', 'Chocolate'),
    ]

    FILLING_CHOICES = [
        ('chantilly', 'Chantilly'),
        ('cacao', 'Cacao'),
        ('cafe', 'Café'),
        ('dulce de leche', 'Dulce de Leche'),
    ]

    FRUIT_CHOICES = [
        ('frutilla', 'Frutilla'),
        ('durazno', 'Durazno'),
        ('sin frutas', 'Sin frutas'),
    ]

    quantity = forms.IntegerField(
        min_value=1,
        initial=1,
        label='Peso',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '1'}),
        required=True,
    )
    shape = forms.ChoiceField(
        choices=SHAPE_CHOICES,
        label='Forma',
        widget=forms.RadioSelect,
        required=True,
    )
    flavor = forms.ChoiceField(
        choices=FLAVOR_CHOICES,
        label='Sabor de bizcochuelo',
        widget=forms.RadioSelect,
        required=True,
    )
    fillings = forms.MultipleChoiceField(
        choices=FILLING_CHOICES,
        label='Rellenos',
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )
    fruits = forms.ChoiceField(
        choices=FRUIT_CHOICES,
        label='Frutas',
        widget=forms.RadioSelect,
        required=True,
    )
    message = forms.CharField(
        max_length=255,
        required=False,
        label='Mensaje',
        widget=forms.TextInput(attrs={
            'placeholder': 'Escribe un mensaje, ya sea, feliz cumpleaños, feliz aniversario, etc. (Opcional)', 'rows': 5, 'cols': 40
        }),
    )
    detail = forms.ImageField(
        max_length=255,
        required=False,
        label='Tema o Detalle',
        widget=forms.TextInput(attrs={
            'placeholder': 'Describe si quieres alguna temática o detalle, ya sea, programa infantil, pasatiempo, etc. (Opcional)', 'rows': 5, 'cols': 40
        }),
    )
    full_name = forms.CharField(
        label='Nombre completo',
        max_length=255,
        required=True,
    )
    phone_number = forms.CharField(
        label='Número de teléfono',
        max_length=15,
        required=True,
    )
    pickup_date = forms.DateField(
        label='Fecha de recogida',
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True,
    )
