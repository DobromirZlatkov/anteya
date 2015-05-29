from django.contrib import admin
from .models import Abrasive, Camp, Color, Order, Product


class AbrasiveAdmin(admin.ModelAdmin):
    pass
admin.site.register(Abrasive, AbrasiveAdmin)


class CampAdmin(admin.ModelAdmin):
    pass
admin.site.register(Camp, CampAdmin)


class ColorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Color, ColorAdmin)


class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Order, OrderAdmin)


class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)
