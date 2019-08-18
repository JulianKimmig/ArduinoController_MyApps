import os

from django.core.files.storage import FileSystemStorage
from django.db import models

# Create your models here.
from django.forms import ModelForm

from CoffeRoaster.coffe_roaster.apps import CoffeRoasterConfig
from plug_in_django.plug_in_django.settings import CONFIG


class RoastingProfileModel(models.Model):
    roasting_profile_upload_storage = FileSystemStorage(
        location=CoffeRoasterConfig.data_dir, base_url=CoffeRoasterConfig.data_dir_url
    )

    name = models.CharField(max_length=255, unique=True)
    data = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    image = models.FileField(storage=roasting_profile_upload_storage, null=True)


class RoastingProfileForm(ModelForm):
    class Meta:
        model = RoastingProfileModel
        fields = ["name", "data"]
