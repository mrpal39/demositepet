from django.shortcuts import render
from django.urls.conf import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('<slug>', views.pet_detail, name='PetDetail'),
    path("p/<pk>/", views.petCategoryIn, name="petCategoryIn"),


    
    path("<str:owner>", views.OwnerPetdetail, name="OwnerPetdetail"),

    path('',views.pet_list,name='pet_list'),

    path("resigter/", views.RegisterPetView.as_view(), name="resigter_pet"),
    path("edit/<pk>", views.EditPetView.as_view(), name="edit"),
    path("d/<pk>/<slug>/", views.PetDetail.as_view(), name="pet_Detail"),
    path('c/c/',views.pet_View.as_view(),name='category'),
    path('add/',views.apipet,name='apipetcategory'),


]
