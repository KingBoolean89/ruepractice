from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
      path('', views.index, name='index'),
     url(r'^display_products$', views.display_products,
     name='display_products'),
]