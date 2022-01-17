from django.contrib import admin

from .models import *

class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 0

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'id', 'price', 'stock', 'time_create', 'is_published')
    list_display_links = ('name',)
    inlines = [ItemImageInline]
    search_fields = ('name', 'description')
    list_editable = ('price', 'stock', 'is_published')
    list_filter = ('is_published', 'time_create', 'time_update')
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Item, ItemAdmin)

class ItemImageAdmin(admin.ModelAdmin):
    list_display = ('itpm',)

    class Meta:
        model = ItemImage

admin.site.register(ItemImage, ItemImageAdmin)
