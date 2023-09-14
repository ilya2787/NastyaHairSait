from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, Cat_list

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Name', 'image_show', 'description_smoll', 'Cat_product', 'price')

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"

    image_show.__name__ = "Картинка"

@admin.register(Cat_list)
class CatAdmin(admin.ModelAdmin):
    list_dispay = ('name')

