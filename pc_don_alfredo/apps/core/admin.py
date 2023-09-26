"""Core admin."""

# Models
from apps.core.models import (
    Product, 
    ProductImage, 
    LiqueurSize, 
    Liqueur, 
    Jam,
    Pie,
    Cake,
    Cookie,
    Dessert,
    Item
)

# Django
from django.contrib import admin

# Core admin

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Product admin."""
    pass

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    """ProductImage admin."""
    pass

@admin.register(Jam)
class JamAdmin(admin.ModelAdmin):
    """Jam admin."""
    pass

@admin.register(LiqueurSize)
class LiqueurSizeAdmin(admin.ModelAdmin):
    """LiqueurSize admin."""
    pass

@admin.register(Liqueur)
class LiqueurAdmin(admin.ModelAdmin):
    """Liqueur admin."""
    pass

@admin.register(Pie)
class PieAdmin(admin.ModelAdmin):
    """Pie admin."""
    pass

@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    """Cake admin."""
    pass

@admin.register(Cookie)
class CookieAdmin(admin.ModelAdmin):
    """Cookie admin."""
    pass

@admin.register(Dessert)
class DessertAdmin(admin.ModelAdmin):
    """Dessert admin."""
    pass

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """Item admin."""
    pass
