from django.urls import path

from . import views

urlpatterns = [path("", views.index, name="index"),
               path("roaster", views.roaster, name="roaster"),
               path("roasting_profile", views.RoastingProfile.as_view(), name="roasting_profile"),
               path("roasting_profile/<id>", views.RoastingProfile.as_view(), name="roasting_profile"),
               path("run_roast/<id>", views.RunRoast.as_view(), name="run_roast"),

               ]