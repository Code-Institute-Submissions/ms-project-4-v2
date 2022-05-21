from django.contrib import admin
from .models import Order, OrderLineItem


# Register your models here.


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Restricts the ability to edit fields calculated by Order model.
    Restricts the columns in the order list to key items.
    Applies sorting to orders in a descending chronological order.
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'order_total',)

    list_display = ('order_number', 'date', 'full_name', 'order_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
