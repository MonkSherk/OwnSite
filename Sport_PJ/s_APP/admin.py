from django.contrib import admin

from s_APP.models import Category, Product , Store

# Register your models here.

admin.site.register(Category)
admin.site.register(Store)
admin.site.register(Product)