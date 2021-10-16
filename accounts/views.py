from pet.models import Pet
from django.shortcuts import render
from django.http import HttpResponse
from password_reset.views import Recover, RecoverDone, Reset, ResetDone
from .models import  OwnerProfile
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http.response import HttpResponseRedirect
from django.shortcuts import resolve_url
from django.urls import reverse, reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic import CreateView, DetailView, TemplateView, UpdateView
from .forms import (
    LoginForm,
    RegisterForm,
    UpdateUserForm,
    UsersPasswordRecoveryForm,
    UsersPasswordResetForm,
)

def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'error_404.html', data)




class RecoverView(Recover):
    template_name = "account/recover.html"
    form_class = UsersPasswordRecoveryForm
    success_url_name = "recover_password_sent"
    email_template_name = "account/recover_email.txt"
    search_fields = ["username", "email"]


class RecoverDoneView(RecoverDone):
    template_name = "account/recover.html"


class RecoverResetView(Reset):
    template_name = "account/reset.html"
    success_url = "recover_password_done"
    form_class = UsersPasswordResetForm
    token_expires = 3600 * 2


class RecoverResetDoneView(ResetDone):
    template_name = "account/reset_done.html"


class CreateUserView(CreateView):
    model = OwnerProfile
    form_class = RegisterForm
    template_name = "account/create.html"
    authenticated_redirect_url = reverse_lazy("homepage")

    msg = _(
        'Your account has been successfully created, access <a href="{0}">'
        "this page</a> and register the pet :)"
    )

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(resolve_url(self.authenticated_redirect_url))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.is_information_confirmed = True
        return super(CreateUserView, self).form_valid(form)

    def get_success_url(self):
        url = reverse("homepage")
        messages.success(self.request, self.msg.format(url))
        user = authenticate(
            username=self.request.POST.get("username"), password=self.request.POST.get("password1")
        )
        login(self.request, user)
        return reverse("homepage")


class EditUserProfileView(LoginRequiredMixin, UpdateView):
    template_name = "account/edit_profile.html"
    model = OwnerProfile
    form_class = UpdateUserForm

    def get_success_url(self):
        messages.success(self.request, _("Changes saved successfully."))
        return reverse("homepage")

    def get_object(self ):
        return (self.request.user)

# class EditkannelProfileView(LoginRequiredMixin, UpdateView):
#     template_name = "account/edit_profile.html"
#     model = Kennel
#     form_class = UpdateKennelForm

#     def get_success_url(self):
#         messages.success(self.request, _("Changes saved successfully."))
#         return reverse("homepage")

   
#     # def get_object(self ):
#         # return (self.request.user)
#     # def get(self, request, *args, **kwargs):
#     #         current_pet = self.get_object()
#     #     if request.user == current_pet.owner:
#     #         return super(EditPetView, self).get(request, *args, **kwargs)
#     #     else:
#     #         return HttpResponseRedirect(reverse("detail", kwargs={"pk": current_pet.pk}))

#     def form_valid(self, form):
#         return super(EditkannelProfileView, self).form_valid(form)

    
class UserLogin(LoginView):
    form_class = LoginForm
    template_name = "account/login.html"


class UserProfileView(TemplateView):
    model= Pet
    template_name = "account/profile.html"

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context["object"] = self.request.user
        return context


# class ProfileDetailView(DetailView):
#     template_name = "account/profile.html"
#     model = OwnerProfile

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["aa"] = self.object.all()
    #     return context
    
    



def confirm_information(request):
    """This check that the user has confirmed the information and
    redirect to the correct view"""
    if request.user:
        if request.user.is_information_confirmed:
            return HttpResponseRedirect(reverse("homepage"))
        else:
            return HttpResponseRedirect(reverse("edit"))
