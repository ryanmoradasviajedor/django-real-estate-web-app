from django.shortcuts import render

from .models import Listing

def index(request):
    listings = Listing.objects.all()

    template = 'listings/listings.html'
    context = {
        'listings': listings
    }
    return render(request, template, context)

def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')
