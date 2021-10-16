from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from PIL import Image
# Create your models here.


class OwnerProfile(AbstractUser):
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    is_information_confirmed = models.BooleanField(default=False)
    phone = models.CharField("Telefone", max_length=30, blank=True)
    kennel_name = models.CharField(max_length=200 ,default="dogkennl")
    kennel_description = models.CharField(_("description"), max_length=200,default="dogkennl")
    kennel_addres = models.CharField(_("address"), max_length=200,default="dogkennl")
    kennel_state = models.CharField(_("state"), max_length=200,default="dogkennl")
    kennel_contact = models.IntegerField(default="01235")
    kennel_image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    kennel_social = models.URLField()
    def get_absolute_url(self):
        return reverse("user_profile", args=[self.id])


    def __str__(self):
        return self.username
