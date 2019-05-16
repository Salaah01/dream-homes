import json
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing
from enquiries.models import Enquiry
from .choices import price_choices, bedroom_choices
from .search_tool import SearchListings


def listing(request, listing_id):
    '''
    View which returns opens the html for a single listing using the listing_id.
    '''
    if request.method == 'POST':
        
        # Get Enquiry Form Values
        user = request.user.id
        if type(user) != int:
            user = 0
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        search_values = json.loads(request.POST['search-values'])
        searched_keywords = search_values['keywords']
        searched_location = search_values['location']
        searched_bedrooms = search_values['bedrooms_value']
        searched_price = search_values['price_value']
        
        # Add Enquiry to Database
        new_enquiry = Enquiry(
            listing_id = Listing.objects.get(pk=listing_id),
            user_id = user,
            user_group = 'customer',
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            email = email,
            message = message,
            searched_keywords = searched_keywords,
            searched_location = searched_location,
            searched_bedrooms = searched_bedrooms,
            searched_price = searched_price
        )
        new_enquiry.save()

    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'user': request.user,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'listing': listing,
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date').filter(is_published=True)

    queryset_list = SearchListings(request.GET, queryset_list).searchFields()

    # Pagination
    paginator = Paginator(queryset_list, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'listings': paged_listings,
        'values': request.GET,
    }
    
    return render(request, 'listings/search.html', context)