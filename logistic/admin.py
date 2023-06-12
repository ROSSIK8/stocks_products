from django.contrib import admin
from .models import Stock, StockProduct, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(StockProduct)
class StockProductAdmin(admin.ModelAdmin):
    list_display = ['stock', 'product', 'quantity', 'price']


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['address']
