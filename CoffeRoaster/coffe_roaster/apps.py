import os

from django.apps import AppConfig


from django_arduino_controller.apps import DjangoArduinoControllerConfig
from CoffeRoaster.coffe_roaster.coffe_roaster_api import CoffeRoasterApi

class CoffeRoasterConfig(AppConfig):
    module_path = ".".join(__name__.split(".")[:-1])
    name = "coffe_roaster"
    baseurl = "coffe_roaster"

    data_dir = True

    def ready(self):
        DjangoArduinoControllerConfig.add_api(CoffeRoasterApi)
