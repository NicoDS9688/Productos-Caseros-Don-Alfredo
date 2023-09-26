"""Core views."""


from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CakeOrderForm, LiqueurOrderForm, ProductOrderForm
from .models import Cart, Item, LiqueurSize, Product


def inicio(request):
    """TODO."""
    return render(request, "core/index.html")


def contacto(request):
    """TODO."""
    return render(request, "core/info.html")


def catalogo(request):
    """TODO."""
    return render(request, "core/catalog.html")

def mermeladas(request):
    """TODO."""


    return render(request, "core/products/jam.html")

def tartas(request):
    """TODO."""
    return render(request, "core/products/cake.html")

def licores(request):
    """TODO."""
    return render(request, "core/products/liqueur.html")

def dulces(request):
    """TODO."""
    return render(request, "core/products/dessert.html")


def product_detail(request, id):
    """ Vista que busca producto por id y renderiza formulario. """
    product = get_object_or_404(Product, pk=id)
    print("ID del producto:", product.id)
    form = ProductOrderForm()

    return render(request, 'core/forms/product_order.html', {'product': product, 'form': form})

def liqueur_detail(request, id):
    """ Vista que busca producto por id y renderiza formulario. """
    product = get_object_or_404(Product, pk=id)
    print("ID del producto:", product.id)
    form = LiqueurOrderForm()

    return render(request, "core/forms/liqueur_order.html", {'product': product, 'form': form})

def cake_detail(request, id):
    """ Vista que busca producto por id y renderiza formulario. """
    product = get_object_or_404(Product, pk=id)
    print("ID del producto:", product.id)
    form = CakeOrderForm()

    return render(request, "core/forms/cake_order.html", {'product': product, 'form': form})


def cart_detail(request):
    """Vista que muestra los productos en el carrito."""
    cart_id = request.session.get('cart_id')

    if cart_id:
        cart = Cart.objects.get(pk=cart_id)
        items_cart = Item.objects.filter(cart=cart)

        for item in items_cart:
            print(item.__dict__)

        # TODO: Validar que el precio del licor se sume al precio del producto
        total_cart_price = sum(item.product.price * item.quantity for item in items_cart)
        for item in items_cart:
            item.total_price = item.product.price * item.quantity
            # Agregar el precio del licor
            # if item.size.price:
            #     item.total_price += item.size.price * item.quantity
            print(f"Item: {item.product.name}, Size: {item.size.name if item.size else 'No size selected'}")
    else:
        cart = None
        items_cart = []
        total_cart_price = 0

    context = {
        'cart': cart,
        'items_cart': items_cart,
        'total_cart_price': total_cart_price,
    }

    return render(request, 'core/cart/cart_detail.html', context=context)


def add_to_cart(request, id):
    """Vista que procesa el formulario de pedido y lo agrega al carrito"""
    cart_id = request.session.get('cart_id')
    if cart_id:
        cart = Cart.objects.get(pk=cart_id)
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id

    product = get_object_or_404(Product, pk=id)

    if request.method == 'POST':
        if 'quantity' in request.POST:
            quantity = int(request.POST['quantity'])
        else:
            quantity = 1

        size_name = request.POST.get('size', None)
        size = None

        if size_name:
            size = get_object_or_404(LiqueurSize, name=size_name)

        existing_item = cart.item_set.filter(product=product, size=size).first()

        if existing_item:
            existing_item.quantity += quantity
            existing_item.save()
        else:
            item = Item.objects.create(cart=cart, product=product, size=size, quantity=quantity)

    return redirect('carrito')


def remove_cart_item(request, item_id):
    print(f"Entrando en remove_cart_item con item_id = {item_id}")
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('carrito')


def process_order(request):
    """Procesar orden de pedido."""

    if request.method == 'POST':
        nombre = request.POST.get('full_name')
        telefono = request.POST.get('phone_number')
        fecha_retiro = request.POST.get('pickup_date')

        cart_id = request.session.get('cart_id')
        if cart_id:
            cart = Cart.objects.get(pk=cart_id)
            items_cart = Item.objects.filter(cart=cart)
        else:
            items_cart = []

        mensaje = f"Nombre: {nombre}\nTeléfono: {telefono}\nFecha de retiro: {fecha_retiro}\n\nProductos:\n"
        for item in items_cart:
            mensaje += f"- {item.product.name} { item.size } ({item.quantity} unidades)\n"

        send_mail(
            'Nuevo pedido de cliente',
            mensaje,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_DESTINO],
            fail_silently=False,
        )

        items_cart.delete()
        return redirect('catalogo')

    return JsonResponse({'message': 'Error al procesar el pedido'})



def order_cake(request, id):
    # Obtén el producto por su ID
    product = get_object_or_404(Product, pk=id)

    if request.method == 'POST':
        # Procesa el formulario cuando se envía
        form = CakeOrderForm(request.POST)
        if form.is_valid():
            # Obtén los datos del formulario
            quantity = form.cleaned_data['quantity']
            shape = form.cleaned_data['shape']
            fillings = form.cleaned_data['fillings']
            fruits = form.cleaned_data['fruits']
            flavor = form.cleaned_data['flavor']
            message = form.cleaned_data['message']
            detail = form.cleaned_data['detail']
            full_name = form.cleaned_data['full_name']
            phone_number = form.cleaned_data['phone_number']
            pickup_date = form.cleaned_data['pickup_date']

            mensaje = f"Nuevo pedido de torta:\n\n" \
                    f"Producto: {product.name}\n" \
                    f"Cantidad: {quantity}\n" \
                    f"Forma: {shape}\n" \
                    f"Rellenos: {', '.join(fillings)}\n" \
                    f"Frutas: {fruits}\n" \
                    f"Sabor: {flavor}\n" \
                    f"Mensaje: {message}\n" \
                    f"Detalles adicionales: {detail}\n" \
                    f"Nombre completo: {full_name}\n" \
                    f"Número de teléfono: {phone_number}\n" \
                    f"Fecha de recogida: {pickup_date}"
            send_mail(
                'Nuevo pedido de cliente',
                mensaje,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_DESTINO],
                fail_silently=False,
            )

            return redirect('catalogo')

    else:
        form = CakeOrderForm()

    return render(request, "core/forms/cake_order.html", {'product': product, 'form': form})
