from django.contrib import admin

from .models import Manufacturer
from .models import Product


admin.site.register(Manufacturer)
admin.site.register(Product)
