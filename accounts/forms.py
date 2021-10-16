from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.db.models.constraints import UniqueConstraint
from password_reset.forms import PasswordRecoveryForm, PasswordResetForm

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from .models import  OwnerProfile


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"autofocus": "autofocus"})
        self.fields["password"].widget.attrs.update({"class": "form-control"})


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["email"].required = True


class RegisterForm(UserForm):
    password1 = forms.CharField(
        label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(
        label=_("Password confirmation"), widget=forms.PasswordInput)
    UniqueConstraint(name='unique_username', fields=[
                     'username'], opclasses=['varchar_pattern_ops'])

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update(
            {"class": "form-control"})
        self.fields["last_name"].widget.attrs.update({"class": "form-control"})
        self.fields["email"].widget.attrs.update({"class": "form-control"})
        self.fields["username"].widget.attrs.update({"class": "form-control"})
        self.fields["password1"].widget.attrs.update({"class": "form-control"})
        self.fields["password2"].widget.attrs.update({"class": "form-control"})
        self.fields["username"].help_text = _(
            "Required. 30 characters or less. " "Only letters, numbers e @/./+/-/_."
        )

    class Meta:
        model = OwnerProfile
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                _("The two password fields didn't match."))
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


# class UpdateKennelForm(forms.ModelForm):
#     class Meta:
#         model = Kennel
#         fields = (
#             'kennel_name','kennel_description',
#             'kennel_addres',
#             'kennel_state',
#             'kennel_contact',
#             'kennel_social',
#         )

#     def __init__(self, *args, **kwargs):
#         super(UpdateKennelForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.fields["kennel_name"].required = True
#         self.fields["kennel_description"].required = True
#         self.fields["kennel_addres"].required = True
#         self.fields["kennel_state"].widget.attrs.update({"class": "form-control"})
#         self.fields["kennel_contact"].widget.attrs.update({"class": "form-control"})
#         self.fields["kennel_social"].widget.attrs.update({"class": "form-control"})


#         self.helper.add_input(Submit("submit", _("Save Changes")))
    

#     def save(self, commit=True):
#         user = super(UpdateKennelForm, self).save(commit=False)
#         user=self.request.user
#         if commit:
#             user.save()
#         return user


class UpdateUserForm(UserForm):
    class Meta:
        model = OwnerProfile
        fields = ("first_name", "last_name", "email", "phone","kennel_name","kennel_social","kennel_contact","kennel_state","kennel_description",'kennel_addres',)

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)

        self.fields["kennel_name"].required = True
        self.fields["kennel_description"].required = True
        self.fields["kennel_addres"].required = True
        self.fields["kennel_state"].widget.attrs.update({"class": "form-control"})
        self.fields["kennel_contact"].widget.attrs.update({"class": "form-control"})
        self.fields["kennel_social"].widget.attrs.update({"class": "form-control"})

        self.helper.add_input(Submit("submit", _("Save Changes")))

    def save(self, commit=True):
        self.instance.is_information_confirmed = True
        super(UpdateUserForm, self).save()


class UsersPasswordRecoveryForm(PasswordRecoveryForm):
    def __init__(self, *args, **kwargs):
        super(UsersPasswordRecoveryForm, self).__init__(*args, **kwargs)
        self.fields["username_or_email"].label = ""
        self.helper = FormHelper()
        self.helper.add_input(Submit("recover", _("Recover password")))


class UsersPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UsersPasswordResetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("recover", _("Recover password")))
