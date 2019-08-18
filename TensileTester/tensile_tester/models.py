from django.core.files.storage import FileSystemStorage
from django.db import models
from TensileTester.tensile_tester.apps import TensileTesterConfig


# Create your models here.


class TensileTestRoutine(models.Model):
    name = models.CharField(max_length=255, unique=True)
    data = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TensileTestInstance(models.Model):
    tensile_test_upload_storage = FileSystemStorage(
        location=TensileTesterConfig.data_dir, base_url=TensileTesterConfig.data_dir_url
    )
    name = models.CharField(max_length=255, unique=True)
    data = models.ForeignKey(TensileTestRoutine, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    image = models.FileField(storage=tensile_test_upload_storage, null=True)


# class RoastingProfileForm(ModelForm):
#    class Meta:
#        model = RoastingProfileModel
#        fields = ['name',
#                  'data'
#                  ]
