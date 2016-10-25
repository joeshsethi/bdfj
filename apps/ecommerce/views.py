from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Gen_user, Log_user, Gen_user_product, Log_user_product, Cart_product, Cart, Order, Product, Order_product, Image, Inventory, Log_user, Billing, Shipping

def index(request):
    request.session['logged_user'] = ''
    return render(request, 'ecommerce/index.html')

def admin(request):
    return render(request, 'ecommerce/admin.html')

def register(request):
    if request.method == "POST":
        form_errors = AdminUser.objects.validate(request.POST)

        if len(form_errors) > 0:
            for error in form_errors:
                messages.error(request, error)
        else:
            AdminUser.objects.register(request.POST)
            messages.success(request, "You have successfully registered! Please login to continue")

    return redirect('/admin')

def login(request):
    if request.method == "POST":
        user = AdminUser.objects.login(request.POST)
        if not user:
            messages.error(request, "Not login credentials!")
        else:
           request.session['logged_user'] = user.id
           return redirect('/orders')

def logout(request):
    if 'logged_user' in request.session:
        request.session['logged_user'] = ''
        request.session.pop('logged_user')
    return redirect('/')

def orders(request):
    # trips = Trip.objects.filter(user=user)
    # othertrips = Trip.objects.all().exclude(user=user)
    # context = {
    #     'user' : user,
    #     'trips': trips,
    #     'othertrips': othertrips,
    # }
    return render(request, 'ecommerce/orders.html', context)
