from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "value", "quantity")

admin.site.register(Item, ItemAdmin)