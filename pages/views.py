from django.shortcuts import render
from listings.models import Listing
from listings.choices import bedroom_choices, price_choices

def index(request):
    """
    View loads the index page
    """
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    """
    View loads the About Us page
    """
    return render(request, 'pages/about.html')