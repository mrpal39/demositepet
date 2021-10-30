from django.shortcuts import render
from django.urls.conf import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("s/<str:owner>/", views.OwnerPetdetail, name="OwnerPetdetail"),

    path("", views.RegisterPetView.as_view(), name="resigter_pet"),
    path("edit/<pk>", views.EditPetView.as_view(), name="pet_edit"),
    path("d/<pk>/<slug>/", views.PetDetail.as_view(), name="pet_Detail"),
    path("p/<pk>/", views.petCategoryIn, name="petCategoryIn"),
    path('c/c/',views.pet_View.as_view(),name='category'),
    path('add/',views.apipet,name='apipetcategory'),


]
