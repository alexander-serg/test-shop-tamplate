from django.contrib import admin
from .models import Order, OrderItem, Status


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class StatusAdmin(admin.ModelAdmin):
    list_display = ['name',]

    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'phone', 'email', 'total_price', 'status', 'created', 'updated',]
    list_filter = ['status', 'created', 'updated']
    inlines = [OrderItemInline]

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['post',]

    class Meta:
        model = OrderItem

admin.site.register(OrderItem, OrderItemAdmin)