import json
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from .models import RoastingProfileModel, RoastingProfileForm


def index(request):
    return render(request, "coffe_roaster_index.html")


BOARDDATASTREAMRECEIVER = None


def roaster(request):
    return render(request, "coffe_roaster_roaster.html")

class RoastingProfile(View):
    def get(self, request, id=None):
        if id is not None:
            roasting_profile_form = RoastingProfileForm(instance=RoastingProfileModel.objects.get(id=id))
        else:
            roasting_profile_form = RoastingProfileForm()

        return render(request, "coffe_roaster_roasting_profile.html",{'form':roasting_profile_form,"id":id})

    def post(self,request,id=None):
        roasting_profile = None
        if id is None:
            form = RoastingProfileForm(request.POST)
        else:
            form = RoastingProfileForm(request.POST,instance=RoastingProfileModel.objects.get(id=id))
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect("coffe_roaster:roasting_profile",id=post.id)

        else:
            return render(request, "coffe_roaster_roasting_profile.html",{'form':form,"id":id})

class RunRoast(View):
    def get(self,request,id):
        profile = RoastingProfileModel.objects.get(id=id)
        return render(request, "coffe_roaster_run_roast.html",{'profile':profile})