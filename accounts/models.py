from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.urls import reverse
from django.utils import timezone


from PIL import Image
# Create your models here.

class UserAccountManager(BaseUserManager):

    def _create_user(self, username, password, is_staff, is_superuser, **extra_fields):
        if not username:
            raise ValueError('Username is required.')
        now = timezone.now()
        username = self.model.normalize_username(username)
        user = self.model(
            username=username,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None, password=None, **extra_fields):
        return self._create_user(username, password, False, False, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        user = self._create_user(username, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user
    def create_buyer(self, username, password,  **extra_fields):
        if not username:
            raise ValueError('Username is required.')
        now = timezone.now()
        username = self.model.normalize_username(username)
        user = self.model(
            username=username,
            is_staff=False,
            breeder=False,
            buyer=True,
            is_superuser=False,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_kennel(self, username, password,  **extra_fields):
        if not username:
            raise ValueError('Username is required.')
        now = timezone.now()
        username = self.model.normalize_username(username)
        user = self.model(
            username=username,
            breeder=True,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user



class OwnerProfile(AbstractBaseUser, PermissionsMixin):
    username=models.CharField(max_length=250)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True,null=True, blank=True)


    admin = models.BooleanField(default=False)
    breeder = models.BooleanField(default=False)
    buyer=models.BooleanField(default=False)

    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    is_information_confirmed = models.BooleanField(default=False,null=True)
    phone = models.CharField("Telefone", max_length=30, null=True)
  
    objects = UserAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.username
