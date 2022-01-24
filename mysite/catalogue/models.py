from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
import uuid



def upload_location(instance, filename):
    file_path = 'catalogue/{author_id}/{title}-{filename}'.format(
                author_id=str(instance.author.id), title=str(instance.id), filename=filename)
    return file_path


class Document(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titre = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to=upload_location, null=False, blank=False)
    no_inventaire = models.CharField(max_length=100, null=True, blank=True)
    categorie = models.CharField(max_length=100, null=True, blank=True)
    theme = models.CharField(max_length=100, null=True, blank=True)
    technique = models.CharField(max_length=100, null=True, blank=True)
    support = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    lieu = models.CharField(max_length=100, null=True, blank=True)
    dimensions = models.CharField(max_length=100, null=True, blank=True)
    epoque = models.CharField(max_length=100, null=True, blank=True)
    type_collection = models.CharField(max_length=100, null=True, blank=True)
    droits = models.CharField(max_length=100, null=True, blank=True)

    tags = models.JSONField(default=list, blank=True)
    description = models.TextField(max_length=5000, null=False, blank=True)

    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)
    
    def __str__(self):
        return self.titre

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]


@receiver(post_delete, sender=Document)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


def pre_save_document_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        print(instance.id)
        instance.slug = slugify(instance.author.username + "-" + str(instance.id))


pre_save.connect(pre_save_document_receiver, sender=Document)
