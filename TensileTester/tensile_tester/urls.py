from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("routine", views.NewRoutine.as_view(), name="new_routine"),
    path("calibrate", views.calibrate, name="calibrate"),
    #  path("roaster", views.roaster, name="roaster"),
    #  path("roasting_profile", views.RoastingProfile.as_view(), name="roasting_profile"),
    #  path("roasting_profile/<id>", views.RoastingProfile.as_view(), name="roasting_profile"),
    #  path("run_roast/<id>", views.RunRoast.as_view(), name="run_roast"),
]
