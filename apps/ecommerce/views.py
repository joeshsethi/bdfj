from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Gen_user, Log_user, Gen_user_product, Log_user_product, Cart_product, Cart, Order, Product, Order_product, Image, Inventory, Log_user, Billing, Shipping

def index(request):
    request.session['logged_user'] = ''
    return render(request, 'ecommerce/index.html')
