import json
import os

import numpy as np
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from .models import RoastingProfileModel, RoastingProfileForm
import matplotlib.pyplot as plt
import logging

mpl_logger = logging.getLogger("matplotlib")
mpl_logger.setLevel(logging.WARNING)


def index(request):
    profiles = RoastingProfileModel.objects.all()
    return render(request, "coffe_roaster_index.html", {"roasting_profiles": profiles})


BOARDDATASTREAMRECEIVER = None


def roaster(request):
    return render(request, "coffe_roaster_roaster.html")


class RoastingProfile(View):
    def get(self, request, id=None):
        roasting_profile = None
        if id is not None:
            roasting_profile = RoastingProfileModel.objects.get(id=id)
            roasting_profile_form = RoastingProfileForm(instance=roasting_profile)
        else:
            roasting_profile_form = RoastingProfileForm()

        return render(
            request,
            "coffe_roaster_roasting_profile.html",
            {"form": roasting_profile_form, "profile": roasting_profile},
        )

    def post(self, request, id=None):
        roasting_profile = None
        if id is None:
            form = RoastingProfileForm(request.POST)
        else:
            form = RoastingProfileForm(
                request.POST, instance=RoastingProfileModel.objects.get(id=id)
            )
        if form.is_valid():
            roasting_profile = form.save(commit=False)
            roasting_profile.save()
            try:
                if os.path.isfile(roasting_profile.image.path):
                    os.remove(roasting_profile.image.path)
            except:
                pass
            data = np.array(
                [
                    [float(c) for c in d.replace("(", "").replace(")", "").split(",")]
                    for d in roasting_profile.data.split(")")
                    if len(d) > 2
                ]
            )
            x, y = data.T
            plt.plot(x, y, "ro-")
            image_path = os.path.join(
                roasting_profile.image.storage.location,
                "roasting_profile_{}_image.png".format(roasting_profile.id),
            )
            plt.savefig(image_path)
            plt.close()
            roasting_profile.image = os.path.basename(image_path)
            roasting_profile.save()
            return redirect("coffe_roaster:roasting_profile", id=roasting_profile.id)

        else:
            return render(
                request,
                "coffe_roaster_roasting_profile.html",
                {"form": form, "profile": roasting_profile},
            )


class RunRoast(View):
    def get(self, request, id):
        profile = RoastingProfileModel.objects.get(id=id)
        return render(request, "coffe_roaster_run_roast.html", {"profile": profile})
