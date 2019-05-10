from django.contrib import admin
from .models import Enquiry
from listings.models import Listing

# class EnquiryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'first_name', 'last_name', 'listing.title', 'price', 'agent', 'message')
#     list_display_links = ('id', 'title')
#     list_filter = ('agent', 'city', 'is_published',)
#     list_editable = ('is_published',)
#     search_fields = ('title', 'agent',)

# admin.site.register(Enquiry, EnquiryAdmin)

admin.site.register(Enquiry)