from django.contrib import admin
from .models import Catagory
from .models import Products
from.models import Cart

admin.site.register(Catagory)
admin.site.register(Products)
admin.site.register(Cart)