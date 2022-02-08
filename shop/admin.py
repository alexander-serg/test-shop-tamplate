from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 0

class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

    class Meta:
        model = ItemCategory

admin.site.register(ItemCategory, ItemCategoryAdmin)    

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'id', 'price', 'category', 'stock', 'get_html_image', 'time_create', 'is_published')
    list_display_links = ('name',)
    inlines = [ItemImageInline]
    search_fields = ('name', 'description')
    list_editable = ('price', 'stock', 'is_published')
    list_filter = ('is_published', 'time_create', 'time_update')
    prepopulated_fields = {"slug": ("name",)}

    def get_html_image(self, object):
        if object.image_get().image:
            return mark_safe(f"<img src='{object.image_get().image.url}' width=50")

    get_html_image.short_description = "Фото"

admin.site.register(Item, ItemAdmin)

class ItemImageAdmin(admin.ModelAdmin):
    list_display = ('itpm',)

    class Meta:
        model = ItemImage

admin.site.register(ItemImage, ItemImageAdmin)

class MessagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'status', 'created']
    list_filter = ['status', 'created']

    class Meta:
        model = Messages

admin.site.register(Messages, MessagesAdmin)

class MessagesDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'created']
    list_filter = ['created']

    class Meta:
        model = MessagesDetail

admin.site.register(MessagesDetail, MessagesDetailAdmin)

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_filter = ['id']

    class Meta:
        model = Reviews

admin.site.register(Reviews, ReviewsAdmin)    

admin.site.site_title = 'Админка'
admin.site.site_header = 'Админка'