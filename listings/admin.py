from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'agent')
    list_display_links = ('id', 'title')
    list_filter = ('agent', 'city', 'is_published',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'zipcode', 'price',)

admin.site.register(Listing, ListingAdmin)