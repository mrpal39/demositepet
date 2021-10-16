from cities.models import State
from django.db.models.aggregates import Count
from django.views.generic.list import ListView
from accounts.models import OwnerProfile
from django.utils import timezone
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import IntegrityError, transaction
from django.db import models
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.views.decorators.http import require_POST
from django.views.generic import DetailView, CreateView, UpdateView, TemplateView, UpdateView
from .forms import PetForm
from.models import Category, Pet


def apiView(request):
    return render(request, 'api.html')


def home_page(request):



    context = {'pets': Pet.objects.all(),
               }
    return render(request, 'homepage.html', context)

def pet_list(request):



    context = {'pets': Pet.objects.all(),
               'state': 'state_cat',
               }
    return render(request, 'pet_list.html', context)

def OwnerPetdetail(request, owner):

    userInfo = OwnerProfile.objects.get(username=owner)
    # print(userInfo.id)
    UserPets = Pet.objects.all().filter(owner_id=userInfo.id)
    # print(UserPets)
    context = {
        'userinfo': userInfo,
        'UserPets': UserPets,
    }
    return render(request, 'OwnerPetDetail.html', context)


def petCategoryIn(request, pk):
    dosg = Pet.objects.filter(category_id=pk)
    count_pet = Category.objects.filter(id=pk)
    print(count_pet)
    dd = dosg.count()
    # print(dd)
    # print(dosg)

    context = {
        'pets': dosg,
        'dd': dd
    }

    return render(request, 'petcategory.html', context)


class EditPetView(UpdateView):
    model = Pet
    form_class = PetForm
    template_name = "edit.html"
    success_url = 'pet_detail'

    def get(self, request, *args, **kwargs):
        current_pet = self.get_object()
        if request.user == current_pet.owner:
            return super(EditPetView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse("detail", kwargs={"pk": current_pet.pk}))

    def form_valid(self, form):
        return super(EditPetView, self).form_valid(form)


class PetDetail(DetailView):
    model = Pet
    template_name = 'pet_Detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["'aata"] = self.request.user
        return context


class JsonableResponseMixin:
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.accepts('text/html'):
            return response
        else:
            return JsonResponse(form.errors, status=400)

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.accepts('text/html'):
            return response
        else:
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)

# p        et creater


class RegisterPetView(JsonableResponseMixin, CreateView):
    template_name = "register_pet.html"
    model = Pet
    form_class = PetForm

    def get_success_url(self):
        return reverse("homepage")

    def get(self, request, *args, **kwargs):
        if not request.user.is_information_confirmed:
            messages.warning(request, _(
                "Please confirm your informations before registering a new pet."))
            return HttpResponseRedirect(reverse("profile"))
        else:
            return super(RegisterPetView, self).get(request, *args, **kwargs)

    @transaction.atomic()
    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except IntegrityError:
            messages.info(request, _(
                "You already have a pet registered with this name."))
            return HttpResponseRedirect(reverse("profile"))

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(RegisterPetView, self).form_valid(form)



class pet_View(TemplateView):
    models=Pet  
    template_name='pet_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ggg"] = self.object.all() 
        return context
        
    
    
    def get_queryset(self):
        return super().get_queryset()
    
    