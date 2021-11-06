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
  
    def get_absolute_url(self):
        return reverse("user_profile", args=[self.id])


    def __str__(self):
        return self.username
