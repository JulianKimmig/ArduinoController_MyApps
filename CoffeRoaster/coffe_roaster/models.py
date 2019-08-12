from django.db import models

# Create your models here.
from django.forms import ModelForm


class RoastingProfileModel(models.Model):
    name = models.CharField(max_length=255,unique=True)
    data = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class RoastingProfileForm(ModelForm):
    class Meta:
        model = RoastingProfileModel
        fields = ['name',
                  'data'
                  ]
