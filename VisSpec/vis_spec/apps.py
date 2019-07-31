from django.apps import AppConfig


class VisSpecConfig(AppConfig):
    module_path = ".".join(__name__.split(".")[:-1])
    name = "vis_spec"
    baseurl = "vis_spec"

    def ready(self):
        pass
