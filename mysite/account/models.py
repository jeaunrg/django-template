import os

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from mysite.settings import MEDIA_ROOT, STATIC_ROOT


class MyAccountManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Users must have an email")

        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def upload_location(instance, filename):
    upload_url = os.path.join("avatars", str(instance.id) + ".png")
    if os.path.isfile(os.path.join(MEDIA_ROOT, upload_url)):
        os.remove(os.path.join(MEDIA_ROOT, upload_url))
    return upload_url


class Account(AbstractBaseUser):
    username = models.CharField(
        verbose_name="Nom d'utilisateur", max_length=30, unique=True
    )
    email = models.EmailField(verbose_name="adresse mail", max_length=60, unique=False)
    profile_picture = models.ImageField(
        verbose_name="photo de profile",
        upload_to=upload_location,
        blank=True,
        null=True,
    )
    alias = models.CharField(max_length=200, default="--")
    parameters = models.JSONField(default=dict, blank=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = MyAccountManager()

    def profile_picture_is_valid(self):
        return self.profile_picture and os.path.isfile(
            os.path.join(MEDIA_ROOT, self.profile_picture.name)
        )

    def __str__(self):
        return self.username

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


@receiver(post_delete, sender=Account)
def submission_delete(sender, instance, **kwargs):
    instance.profile_picture.delete(False)
