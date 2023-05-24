from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest
from .models import Category, Product, Profile, Order, OrderEntry

# Create your views here.


def index(request):
    return render(request, 'shop/index.html', {'categories': Category.objects.all()})

def category_detail(request, category_id: int):
    return render(request, 'shop/category_detail.html',{
        'category': get_object_or_404(Category, id=category_id),
    })

def product_detail(request, product_id: int):
    return render(request, 'shop/product_detail.html',{
        'product': get_object_or_404(Product, id=product_id),
    })
@login_required
def add_to_cart(request: HttpRequest):
    profile = request.user.profile
    if not request.user.profile.shopping_cart:
        request.user.profile.shopping_cart = Order(profile=request.user.profile)
        request.user.profile.shopping_cart.save()

    assert request.method== 'POST'
    product_id = request.POST['product_id']
    product = get_object_or_404(Product, id=request.POST['product_id'])
    order_entry = OrderEntry.shoping_card.order_entries.get(product=product).first()
    if not order_entry:
        order_entry = profile.shopping_cart.order_entries.create(product=product, count=0)
        order_entry.count += 1
        order_entry.save()
    OrderEntry.objects.create(product=product, count=1,
                                            order=profile.shopping_cart)

    return redirect('shop:product_detail', product_id)