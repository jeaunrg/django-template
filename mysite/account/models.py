import os

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

from mysite.settings import MEDIA_ROOT, STATIC_ROOT


def upload_location(instance, filename):
    upload_url = os.path.join("avatars", str(instance.id) + ".png")
    if os.path.isfile(os.path.join(MEDIA_ROOT, upload_url)):
        os.remove(os.path.join(MEDIA_ROOT, upload_url))
    return upload_url


class Account(AbstractUser):
    is_author = models.BooleanField(
        default=True,
        help_text="Designates that this user has permissions to create posts.",
    )
    profile_picture = models.ImageField(
        verbose_name="photo de profile",
        upload_to=upload_location,
        blank=True,
        null=True,
    )
    alias = models.CharField(max_length=200, default="--")
    parameters = models.JSONField(default=dict, blank=True)

    def get_admin_fields():
        abstract_user_fields = [f.name for f in AbstractUser._meta.fields]
        account_fields = [f.name for f in Account._meta.fields]
        new_fields = set(account_fields) - set(abstract_user_fields)
        new_fields.remove("id")
        return tuple(new_fields)

    def profile_picture_is_valid(self):
        return self.profile_picture and os.path.isfile(
            os.path.join(MEDIA_ROOT, self.profile_picture.name)
        )

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


@receiver(post_delete, sender=Account)
def submission_delete(sender, instance, **kwargs):
    instance.profile_picture.delete(False)
