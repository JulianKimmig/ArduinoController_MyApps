from django.core.files.storage import FileSystemStorage
from django.db import models
from django.forms import ModelForm, HiddenInput

from TensileTester.tensile_tester.apps import TensileTesterConfig

# Create your models here.
tensile_test_upload_storage = FileSystemStorage(
    location=TensileTesterConfig.data_dir, base_url=TensileTesterConfig.data_dir_url
)

class TensileTest(models.Model):
    name = models.CharField(max_length=255, unique=True)#
    offset = models.IntegerField(default=0)
    scale = models.FloatField()
    maximum_force = models.FloatField(default=15)#
    maximum_speed = models.FloatField(default=0.01)#
    maximum_strain = models.FloatField(default=20)#
    specimen_length = models.FloatField(default=30)#
    created_at = models.DateTimeField(auto_now_add=True)#
    updated_at = models.DateTimeField(auto_now=True)#
    data = models.FileField(storage=tensile_test_upload_storage, null=True)#
    image = models.FileField(storage=tensile_test_upload_storage, null=True)#

class TensileTestForm(ModelForm):
    class Meta:
        model = TensileTest
        fields = ['name',
                  'maximum_force',
                  'maximum_strain',
                  'specimen_length',
                  'maximum_speed',
                  'offset',
                  'scale',
                  ]
        widgets = {'offset': HiddenInput(),'scale': HiddenInput()}
