from django.shortcuts import render

# Create your views here.
from pet.models import Pet

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



    context = {'pets': Pet.objects.all(),
               }
    return render(request, '_layout/base.html', context)
def index(request):


    return render(request, '_layout/base_copy.html')
