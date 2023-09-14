from django.shortcuts import render
from .models import Product, Cat_list
from Cart.forms import CartAddProductForm


def index(request):
    Producti = Product.objects.all()
    Cat = Cat_list.objects.all()
    return render(request, 'main/index.html', {'Producti': Producti, 'Cat': Cat})



def cosmetic(request):
    Producti = Product.objects.all()
    Cat = Cat_list.objects.all()
    cart_product_form = CartAddProductForm()
    return render(request, 'main/cosmetic.html', {'Producti': Producti, 'Cat': Cat, 'cart_product_form': cart_product_form})


def cosmetic_cat(request, cat_id):
    Products = Product.objects.filter(Cat_product=cat_id)
    Cat = Cat_list.objects.all()
    current_Cat = Cat_list.objects.get(id=cat_id)
    cart_product_form = CartAddProductForm()
    context = {'Products': Products, 'Cat': Cat, 'current_Cat': current_Cat, 'cart_product_form': cart_product_form}
    return render(request, 'main/cosmetic_cat.html', context)

def cosmetic_id(request, content_id):
    Produ = Product.objects.get(id=content_id)
    cart_product_form = CartAddProductForm()
    return render(request, 'main/cosmetic_cat_id.html', {'Produ': Produ, 'cart_product_form': cart_product_form})

def services(request):
    return render(request, 'main/services.html')