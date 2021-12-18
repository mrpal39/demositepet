from pet.models import Pet
from django import forms

from django.utils.translation import ugettext as _


class PetForm(forms.ModelForm):

    class Meta:
        model = Pet
        fields = ('name', 'description', 'category', 'breed',
                  'size', 'city', 'state', 'sex', 'profile_picture')
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": _("Costelinha")}),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": _(
                        "It is black and chubby, very shy, "
                        "has went gone next to the school in downtown. "
                        "There's a slight flaw in the tail fur."
                    ),
                }
            ),    

            "size": forms.Select(attrs={"class": "form-control", }),
            "Gender": forms.Select(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control", "placeholder": _("DOG,Cow")}),
            "city": forms.TextInput(attrs={"class": "form-control", }),
            "state": forms.Select(attrs={"class": "form-control", "placeholder": _("DOG,Cow")}),
            "breads": forms.Select(attrs={"class": "form-control", "placeholder": _("DOG,Cow")}),


        }
