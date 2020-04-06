from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Listing
from .choices import price_choices, bedroom_choices, state_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)

    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    template = 'listings/listings.html'
    context = {
        'listings': paged_listings
    }
    return render(request, template, context)

def listing(request, listing_id):
    # Get listing by id
    listing = get_object_or_404(Listing, pk=listing_id)
    
    template = 'listings/listing.html'
    context = {
        'listing': listing
    }
    return render(request, template, context)

def search(request):
    
    template = 'listings/search.html'
    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,

    }
    return render(request, template, context)
