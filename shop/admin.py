from django.contrib import admin

# Register your models here.
from .models import Product, Category, Order, OrderEntry, Profile



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProductInLine(admin.TabularInline):
    model = Product
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInLine]

class OrderInline(admin.TabularInline):
    model = Order
    extra = 0

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['user', 'shopping_cart']
    list_display = ['user', 'shopping_cart']
    inlines = [OrderInline]

class OrderEntryInline(admin.TabularInline):
    model = OrderEntry
    extra = 0


@admin.register(OrderEntry)
class OrderEntryAdmin(admin.ModelAdmin):
    search_fields = ['product', 'order']
    list_display = ['product', 'order']

class OrderInline(admin.TabularInline):
    model = Order
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ['profile']
    list_display = ['profile']

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
