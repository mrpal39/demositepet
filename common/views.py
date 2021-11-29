from django.shortcuts import render

# Create your views here.
from pet.models import Pet,Category

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api(request, format=None):
    api_url={
        "pet":"api",
    }
    return Response(api_url)

def home_page(request):
    
    context = {
              
               }
    
    return render(request, 'index.html', context)


def searchbar(request,*args, **kwargs):
    
    return render(request, 'pet/grid-listings-filterscol-search-aside.html')
    
def wishList(request):


    return render(request, 'wishlist.html')
