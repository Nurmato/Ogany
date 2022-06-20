"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import index,products,shop_detail,shoping_cart,contact,sendContact,subcribe, login1, regis, logout1, addToCart, cart, remove_from_url,order,order_data, thanks
from my_project.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
urlpatterns = [
    path('',index,name='index'),
    path('products/<int:pk>', products, name='products'),
    path('shop_detail',shop_detail,name='shop_detail'),
    path('shoping_cart',shoping_cart,name='shoping_cart'),
    path('contact',contact,name='contact'),
    path('sendContact/',sendContact,name='sendContact'),
    path('subcribe/',subcribe,name='subcribe'),
    path('regis',regis,name='regis'),
    path('login1',login1,name='login1'),
    path('logout1',logout1,name='logout1'),
    path('addToCart/<int:pk>', addToCart, name='addToCart'),
    path('cart',cart,name='cart'),
    path('remove_from_url/<int:pk>', remove_from_url, name='remove_from_url'),
    path('order/', order, name='order'),
    path('order_data/', order_data, name='order_data'),
    path('thanks',thanks,name='thanks'),
    path('admin/', admin.site.urls),
]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)