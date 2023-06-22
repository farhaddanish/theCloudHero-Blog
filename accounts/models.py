from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .fields import LowerEmailField
# Create your models here.




class MyAccountManager (BaseUserManager):
    def create_user(self, email, first_Name, password=None):
        if not email:
            raise ValueError('Users must have email address')
        if not password:
            raise ValueError("Users must have Password")
        if not first_Name:
            raise ValueError("Users must have a First_Name")
        user_obj = self.model(
            email=self.normalize_email(email),
            first_Name=first_Name,
        )
        user_obj.set_password(password)
        user_obj.save()
        return user_obj

    def create_staffuser(self, email, first_Name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            first_Name=first_Name,
            password=password,
        )
        user.is_staff = True
        user.is_admin = False
        user.is_superuser = False
        user.save()
        return user

    def create_superuser(self, email, first_Name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            first_Name=first_Name,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save()
        return user


class Account (AbstractBaseUser):
    email = LowerEmailField(verbose_name="email", max_length=60, unique=True)
    first_Name = models.CharField(verbose_name="First Name", max_length=30)
    data_joined = models.DateTimeField(
        verbose_name="Date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_Name']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
