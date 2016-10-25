from __future__ import unicode_literals
from django.db import models
# import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
ONLY_LETTERS = re.compile('\d') #checks for a digit
ONECAP_ONENUM = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$') #one capital one number

class UserManager(models.Manager):
    pass


class Inventory(models.Model):
    count = models.IntegerField()
    sold = models.IntegerField()
    objects = UserManager()


class Billing(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    zipcode = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Shipping(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    zipcode = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Product(models.Model):
    name = models.CharField(max_length=45)
    categories = models.CharField(max_length=45)
    price = models.IntegerField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    inventory = models.ForeignKey(Inventory)
    objects = UserManager()

class Cart_product(models.Model):
    product = models.ForeignKey(Product)
    objects = UserManager()

class Cart(models.Model):
    cart_product = models.ForeignKey(Cart_product)
    objects = UserManager()

class Gen_user(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cart = models.ForeignKey(Cart)
    objects = UserManager()


class Order(models.Model):
    cart = models.OneToOneField(Cart)
    objects = UserManager()

class Log_user(models.Model):
    username = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.ForeignKey(Order)
    billing = models.ForeignKey(Billing)
    shipping = models.ForeignKey(Shipping)
    objects = UserManager()

class Gen_user_product(models.Model):
    gen_user = models.ForeignKey(Gen_user)
    product = models.ForeignKey(Product)
    objects = UserManager()


class Log_user_product(models.Model):
    log_user = models.ForeignKey(Log_user)
    product = models.ForeignKey(Product)
    objects = UserManager()

class Order_product(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    count = models.IntegerField()
    objects = UserManager()


class Image(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Product)
    objects = UserManager()
