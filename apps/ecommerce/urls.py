from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
#     url(r'^products$', views.products),
#     url(r'^products/(?P<id>\d+)/$', views.show),
#     url(r'^art$', views.art),
#     url(r'^other$', views.other),
#     url(r'^addtocart$', views.addtocart),
#     url(r'^cart$', views.cart),
#     url(r'^checkout$', views.checkout), #This will login, reg, and also payment
    url(r'^admin$', views.admin),
    url(r'^orders$', views.orders),
#     url(r'^orders/(?P<id>\d+)/$', views.orders),
#     url(r'^inventory$', views.inventory),
]
