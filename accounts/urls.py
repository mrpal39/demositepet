from django.shortcuts import render
from django.urls.conf import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("dashboard/<str:owner>/", views.UserProfileView.as_view(), name="dashboard"),

     
    path("dashboard/", views.CreateUserView.as_view(), name="create"),
    # path("profile/d/", views.ProfileDetailView.as_view(), name="user_profile"),
    #     path("profile/edit/", views.EditUserProfileView.as_view(), name="edit"),

    path("login/", views.UserLogin.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name='account/logout.html'), name="logout"),

]
