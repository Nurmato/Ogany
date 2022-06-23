from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from main.models import Category5, Product, Contact11, Subcribe, OrderData, Order, Categories
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def index(request):
    categories = Category5.objects.all()
    categories1 = Categories.objects.all()
    # count_cat = categories.count()   
    # print(count_cat)
    return render(request, 'index.html', {'categories':categories,'categories1':categories1})

def products(request, pk):
    # products = Product.objects.all()
    categories = Category5.objects.all()
    title = Category5.objects.get(pk=pk)
    products_cat = Product.objects.filter(category=pk)
    return render(request, 'products.html', {'title':title, 'products':products_cat, 'categories':categories})


def sendContact(request):
    if request.method == 'POST':
        contact = Contact11()
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.message = request.POST.get('message')
        contact.save()

        return HttpResponseRedirect('/')

def subcribe(request):
    if request.method == 'POST':
        contact = Subcribe()
        contact.email = request.POST.get('email')
        contact.save()

        return HttpResponseRedirect('/')


def regis(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = UserCreationForm()

    return render(request, 'user.html', {'form':form})    
        

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()

    return render(request, 'user.html', {'form':form})



def logout1(request):
    logout(request)

    return render(request, 'index.html')



def addToCart(request, pk):

    cart_session = request.session.get('cart_session', [])
    cart_session.append(pk)
    request.session['cart_session'] = cart_session
    print(cart_session)
    return redirect('/cart')

def cart(request):
    cart_session = request.session.get('cart_session', [])
    all_product_count = len(cart_session)
    products_inCart = Product.objects.filter(id__in=cart_session)
    print(products_inCart)    
    all_product_total_sum = 0
    for product_cart in products_inCart:
        product_cart.count = cart_session.count(product_cart.id)
        product_cart.sum = product_cart.count * product_cart.price
        all_product_total_sum += product_cart.sum

    return render(request, 'shoping-cart.html', {'title':'Корзина', 'products_inCart':products_inCart, 'all_product_count':all_product_count, 'all_product_total_sum':all_product_total_sum} )



def remove_from_url(request, pk):
    cart = request.session.get('cart_session', [])
    cart.remove(pk)
    request.session['cart_session'] = cart

    return redirect('cart')



def order(request):
    return render(request, 'order.html')

def order_data(request):
    cart_session = request.session.get('cart_session', [])
    products_inCart = Product.objects.filter(id__in=cart_session)
    print(products_inCart)    
    all_product_total_sum = 0
    for product_cart in products_inCart:
        product_cart.count = cart_session.count(product_cart.id)
        product_cart.sum = product_cart.count * product_cart.price
        all_product_total_sum += product_cart.sum

    if request.method == 'POST':
        orderc = OrderData()
        orderc.name = request.POST.get('c_name')
        orderc.number = request.POST.get('c_number')
        orderc.address = request.POST.get('c_address')
        orderc.email = request.POST.get('c_email')
        orderc.message = request.POST.get('c_message')
        orderc.save()
    
        for i in products_inCart:
            order = Order()
            order.product = i.name
            order.price = i.price
            order.count = i.count
            order.total_sum = i.sum
            order.customer = orderc
            order.save()
    
    cart_session = request.session.get('cart_session', [])
    cart_session.clear()
    request.session['cart_session'] = cart_session
    all_product_count = len(cart_session)

    return redirect('thanks')
    
def thanks(request):
    return render(request, 'thanks.html')



def shop_detail(request):
    return render(request, 'shop-detail.html')

def shoping_cart(request):
    return render(request, 'shoping-cart.html')

def contact(request):
    return render(request, 'contact.html')



