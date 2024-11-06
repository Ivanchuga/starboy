from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Order
#admin.site.register(Order)


class OrderResource(resources.ModelResource):
    class Meta:
        model = Order
        fields = ('full_name', 'items', 'address', 'city', 'created', 'price')



@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    resource_class = OrderResource
    list_display = ['full_name', 'city', 'formatted_order_date', 'price']
#admin.site.register(OrderResource)
