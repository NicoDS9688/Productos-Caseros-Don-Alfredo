"""Core models."""

# Django
from django.db import models

# Models
UNITS = [
    ('gr', 'Gramos'),
    ('ml', 'Mililitros'),
    ('kg', 'Kilogramos'),
    ('cm de diametro', 'Centímetros'),
]

class Product(models.Model):
    """ Modelo de clase de los productos """
    name = models.CharField(max_length=255)
    description = models.TextField()
    unit = models.CharField(max_length=15, choices=UNITS, default='gr')
    content = models.DecimalField(max_digits=10, decimal_places=0)
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True, default=0)
    image = models.ManyToManyField('ProductImage', related_name='products', blank=True)

    def __str__(self) -> str:
        return self.name

class ProductImage(models.Model):
    """ Modelo de clase de imágenes para los productos"""
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')


class LiqueurSize(models.Model):
    """ Modelo de clase para representar los tamaños del licor """
    name = models.CharField(max_length=50)
    content_ml = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self) -> str:
        return self.name


class Liqueur(Product):
    """ Modelo de clase para representar las licores """
    sizes = models.ManyToManyField(LiqueurSize)

    def __str__(self) -> str:
        return f'Licor: {self.name}'


class Jam(Product):
    """ Modelo de clase para representar las mermeladas"""
    # content_net = models.DecimalField(max_digits=10, decimal_places=2, default=750)

    def __str__(self) -> str:
        return f'Mermelada: {self.name} ID:{self.id}'


class Pie(Product):
    """ Modelo de clase para representar las tartas """
    # size = models.CharField(max_length=10, default='30cm')

    def __str__(self) -> str:
        return f'Tarta: {self.name}'


class Cake(Product):
    """ Modelo de clase para representar las tortas """
    # price_per_kg = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self) -> str:
        return f'Torta: {self.name}'


class Cookie(Product):
    """ Modelo de clase para representar las masitas """
    # price_per_kg = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self) -> str:
        return f'Galleta: {self.name}'


class Dessert(Product):
    """ Modelo de clase para representar los postres """
    # content_net = models.DecimalField(max_digits=10, decimal_places=2, default=200)

    def __str__(self) -> str:
        return f'Postre: {self.name}'


class Cart(models.Model):
    """Modelo de clase que representa al carrito"""
    products = models.ManyToManyField(Product, through='Item')


class Item(models.Model):
    """Modelo de clase que asocia los items con el carrito"""
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.ForeignKey(LiqueurSize, on_delete=models.CASCADE, null=True)
