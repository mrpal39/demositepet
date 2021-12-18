from django.db.models.base import Model, ModelState
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django_extensions.db.models import TimeStampedModel
from easy_thumbnails.exceptions import InvalidImageFormatError
from easy_thumbnails.files import get_thumbnailer
from raven.contrib.django.raven_compat.models import client as raven_client
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import crypto, timezone
from django.utils.text import slugify
from accounts.models import OwnerProfile
import uuid
import hashlib
from cities.models import District, State,City
from . import services
from django.db.models import Q


class PetManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(name__icontains=query) | 
                         Q(description__icontains=query)|
                         Q(slug__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs
class CatManager(models.Manager):

    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(name__icontains=query) | 
                         Q(desc__icontains=query)|
                         Q(slug__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs
class Category(models.Model):
    name = models.CharField(max_length=5000)
    img = models.FileField(upload_to="images/cat-images/", null=True)
    desc = models.TextField()
    active = models.BooleanField(default=False)
    code  = models.CharField(max_length=5000, null=True, unique=True, verbose_name="Code")
    slug = models.SlugField(unique=True, editable=True, max_length=500, null=True, blank=True)
    objects=CatManager()
    
    def get_total_pet(self):
        return Pet.objects.filter(category_id=self.id).count() or 0
    def __str__(self):
        return self.name
    

    def get_slug(self):
        return self.slug
    

    def get_id(self):
        return self.id

    

class Bread(models.Model):
    name = models.CharField(max_length=50)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                    related_name='Category')
    slug = models.SlugField(unique=True, editable=True, max_length=500, null=True, blank=True)

    def get_total_pet(self):
        return Pet.objects.filter(bread_id=self.id).count() or 0

    def __str__(self):
        return self.name

    def get_bread_cat(self):
        return self.Category.name
    
    def get_bread_cat_id(self):
        return self.Category.id
    
    
    def get_unique_slug(self):
        slug = slugify(self.name)
        unique = slug
        counter = 1
        while Bread.objects.filter(slug=unique).exists():
            unique = '{}-{}'.format(slug, counter)
            counter += 1
        return unique

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Bread, self).save(*args, **kwargs)


# pet proifile
class Pet(TimeStampedModel):
    MALE = "MA"
    FEMALE = "FE"
    PET_SEX = ((FEMALE, _("Female")), (MALE, _("Male")))
    SMALL = "SM"
    MEDIUM = "MD"
    LARGE = "LG"
    PET_SIZE = ((SMALL, _("Small")), (MEDIUM, _("Medium")),
                (LARGE, _("Large")))
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(OwnerProfile, on_delete=models.CASCADE,null=True,blank=True,related_name='pet_owner')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, default="It is black and chubby, very shy, "
                                   "has went gone next to the school in downtown. "
                                   "There's a slight flaw in the tail fur.")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True,related_name='pet_category')
    breed = models.ForeignKey(Bread, on_delete=models.CASCADE,null=True,blank=True,related_name='pet_breed')
    size = models.CharField(max_length=2, choices=PET_SIZE, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE,null=True,blank=True,related_name="pet_state")
    district = models.ForeignKey(District,on_delete=models.CASCADE,null=True,blank=True,related_name="pet_ty")
    city = models.ForeignKey(City,on_delete=models.CASCADE,null=True,blank=True,related_name="pet_city")
    sex = models.CharField(max_length=2, choices=PET_SEX, blank=True)
    profile_picture = models.ImageField(
        upload_to="pet_profiles", help_text=_("Maximum image size is 8MB"))
    slug = models.SlugField(unique=True, editable=True, max_length=500, null=True, blank=True)

    objects         = PetManager()
    def __str__(self):
        return str(self.slug)

    def __unicode__(self):
        return str(self.id)

  

    def get_sex(self):
        return dict(self.PET_SEX).get(self.sex)


    def get_category(self):
        return self.category.name


    def get_breed_name(self):
        return self.breed.name


    def get_unique_slug(self):
        slug = slugify(self.name)
        unique = slug
        counter = 1
        while Pet.objects.filter(slug=unique).exists():
            unique = '{}-{}'.format(slug, counter)
            counter += 1
        return unique

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Pet, self).save(*args, **kwargs)


    @property
    def thumb_picture(self):
        try:
            return get_thumbnailer(self.profile_picture)["pet_thumb"]
        except InvalidImageFormatError:
            raven_client.captureException()
            return self.profile_picture

    def request_action(self):
        hash_input = (crypto.get_random_string(5) + self.name).encode("utf-8")
        self.request_key = hashlib.sha1(hash_input).hexdigest()

        if not services.send_request_action_email(self):
            return

        self.request_sent = timezone.now()
        self.save(update_modified=False)

    def activate(self):
        self.request_sent = None
        self.request_key = ""
        self.active = True
        self.save()

    def deactivate(self):
        if not services.send_deactivate_email(self):
            return

        self.active = False
        self.save(update_modified=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        unique_together = ("name", "owner")


class Photo(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="pet_photos")
