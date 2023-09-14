from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django.conf import settings
import requests

my_token = settings.BOT_TOKEN
my_chat_id = settings.BOT_CHAT_ID


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    items = []
    cart = Cart(request)
    for item in cart:
        items_dict = {'quantity': item['quantity'],
                      'product': item['product'].Name,
                      'total_price': item['total_price'],
                      'price': item['price']}
        items.append(items_dict)
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'cart/detail.html', {'cart': cart,
                                                'items_dict': items
                                                })


def telegram_order(request):
    items = []
    cart = Cart(request)
    for item in cart:
        items_dict = {'quantity': item['quantity'],
                      'product': item['product'].Name,
                      'total_price': item['total_price'],
                      'price': item['price']}
        items.append(items_dict)
    mes = ''
    for item1 in items:
        product = item1['product']
        kol = item1['quantity']
        prise = item1['price']
        total_price = item1['total_price']
        mes += 'Продукт: ' + str(product) + '\n' + 'Количество: ' + str(kol) + '\n' + 'Цена: ' + str(
            prise) + '\n' + 'Сумма: ' + str(total_price) + '\n\n'
    get_price = cart.get_total_price()
    if request.method == 'POST':  # If the form has been submitted...
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        telefon = request.POST['telefon']
        message = "ДАННЫЕ ЗАКАЗЧИКА" + "\n" + "ФИО: "+ last_name + " " + first_name + "\n" + "Телефон: " + telefon + "\n\n" + \
                  "ДАННЫЕ ЗАКАЗА" + "\n" + mes + "Общая сумма заказа: " + str(get_price)
        url = f"https://api.telegram.org/bot{my_token}/sendMessage?chat_id={my_chat_id}&text={message}"
        requests.get(url).json()
        cart.clear()
    return render(request, 'cart/telegram.html')
