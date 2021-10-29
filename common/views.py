from django.shortcuts import render

# Create your views here.
from pet.models import Pet
def apiView(request):
    return render(request, 'api.html')


def home_page(request):



    context = {'pets': Pet.objects.all(),
               }
    return render(request, 'homepage.html', context)
