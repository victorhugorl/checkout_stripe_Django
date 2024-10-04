from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email',)
    list_display_links = ('id', 'username',)
    ordering = '-id',
    search_fields = ('id', 'username',)
    list_per_page = 10
    list_max_show_all = 150
    list_display_links = 'id', 'username',

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_amount',)
    list_display_links = ('id',)
    ordering = '-id',
    search_fields = ('id',)
    list_per_page = 10
    list_max_show_all = 150
    list_display_links = 'id',

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product_name',)
    list_display_links = ('id', 'order',)
    ordering = '-id',
    search_fields = ('id', 'order',)
    list_per_page = 10
    list_max_show_all = 150
    list_display_links = 'id', 'order',

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'amount',)
    list_display_links = ('id', 'order',)
    ordering = '-id',
    search_fields = ('id', 'order',)
    list_per_page = 10
    list_max_show_all = 150
    list_display_links = 'id', 'order',

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'price',)
#     list_display_links = ('id', 'name',)
#     ordering = '-id',
#     search_fields = ('id', 'name',)
#     list_per_page = 10
#     list_max_show_all = 150
#     list_display_links = 'id', 'name',