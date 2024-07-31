from django.contrib import admin
from .models import Product, Order, OrderItem, Cart, CartItem, Customer, Transaction, Review, Address


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'available']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['payment_status', 'customer']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['created_at']        


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity']    


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user_email', 'phone']

    def user_email(self, customer):
        return customer.user.email

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'order', 'transaction_date', 'amount']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'rating']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['state', 'city', 'street']
