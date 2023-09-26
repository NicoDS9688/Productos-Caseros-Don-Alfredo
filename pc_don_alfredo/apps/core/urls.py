"""Rutas"""
from apps.core.views import (add_to_cart, cake_detail, cart_detail, catalogo,
                             contacto, dulces, inicio, licores, liqueur_detail,
                             mermeladas, order_cake, process_order,
                             product_detail, remove_cart_item, tartas)
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    path('contacto/', contacto, name="contacto"),
    path('catalogo/', catalogo, name="catalogo"),
    path('catalogo/mermeladas/', mermeladas, name="mermeladas"),
    path('catalogo/licores/', licores, name="licores"),
    path('catalogo/tartas-y-tortas/', tartas, name="tartas"),
    path('catalogo/masitas-y-postres/', dulces, name="dulces"),
    path('catalogo/<int:id>/', product_detail, name="producto"),
    path('catalogo/licores/<int:id>', liqueur_detail, name="liqueur"),
    path('catalogo/torta/<int:id>', cake_detail, name="torta"),
    path('carrito/', cart_detail, name='carrito'),
    path('agregar_al_carrito/<int:id>/', add_to_cart, name='add_to_cart'),
    path('remover_del_carrito/<int:item_id>/', remove_cart_item, name='remove_cart_item'),
    path('procesar_pedido/', process_order, name='process_order'),
    path('procesar_pedido_torta/<int:id>/', order_cake, name='order_cake'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
