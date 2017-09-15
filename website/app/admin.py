from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Entrée, Plat, Dessert

admin.site.register(Entrée)
admin.site.register(Plat)
admin.site.register(Dessert)
