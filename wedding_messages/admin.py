from django.contrib import admin
from .models import WeddingMessages

class WeddingAdmin(admin.ModelAdmin):
    list_display = ('id', 'fromNames', 'message')
    list_display_links = ('id', 'fromNames')
    list_filter = ('fromNames',)
    search_fields = ('fromNames',)

admin.site.register(WeddingMessages, WeddingAdmin)