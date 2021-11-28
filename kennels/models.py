from django.db import models
from django.db.models.fields import UUIDField
from django.utils.translation import gettext_lazy as _
# Create your models here.
from accounts.models import OwnerProfile
import uuid

class Breed(models.Model):
    name=models.CharField(_("name"), max_length=50)
    intro=models.CharField(_("intro"), max_length=50)
    def __str__(self):
        return self.name

class Contact(models.Model):
    addr=models.CharField(_("addres"), max_length=50)
    city=models.CharField(_("city"), max_length=50)
    state=models.CharField(_("state"), max_length=50)
    mobile=models.IntegerField(_("phone"))

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Contact_detail", kwargs={"pk": self.pk})


class Kennel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name=models.CharField(_("name"), max_length=50)
    description=models.CharField(_("descriptions"), max_length=50)

    breed=models.ManyToManyField(Breed)
    addr=models.CharField(_("addres"), max_length=50)
    city=models.CharField(_("city"), max_length=50)
    state=models.CharField(_("state"), max_length=50)
    mobile=models.IntegerField(_("phone"))

    class Meta:
        verbose_name = _("Kennel")
        verbose_name_plural = _("Kennels")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Kennel_detail", kwargs={"pk": self.pk})
