from django.shortcuts import render
from django.urls.conf import path

from accounts.api import RegisterApi
from . import views
from django.contrib.auth.views import LogoutView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
     
     
     path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path("", views.CreateUserView.as_view(), name="create"),
    # path("profile/d/", views.ProfileDetailView.as_view(), name="user_profile"),
    path("profile/", views.UserProfileView.as_view(), name="user_profile"),
    #     path("profile/edit/", views.EditUserProfileView.as_view(), name="edit"),

    path("login/", views.UserLogin.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name='account/logout.html'), name="logout"),
    path("confirm/", views.confirm_information, name="confirm_information"),

    path("recover/", views.RecoverView.as_view(), name="recover_password"),
    path("recover/reset/done/", views.RecoverResetDoneView.as_view(),
         name="recover_password_done"),
    path("recover/reset/<token>/", views.RecoverResetView.as_view(),
         name="recover_password_reset"),

    path('api/register', RegisterApi.as_view()),

    path("recover/<signature>/", views.RecoverDoneView.as_view(),
         name="recover_password_sent"),
]
