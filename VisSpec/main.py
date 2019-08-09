import os
import sys

import logging
import coloredlogs
from logging.handlers import RotatingFileHandler

from BaseApp import BaseApp

from plug_in_django import manage as plug_in_django_manage


from VisSpec.vis_spec.apps import VisSpecConfig
from json_dict import JsonDict
from os.path import expanduser





class VisSpecApp(BaseApp):
    DEBUGGING = True
    BASENAME = "Vis Spec"
    SNAKE_NAME = BASENAME.lower().replace(" ", "_")
    BASE_DIR = os.path.join(expanduser("~"), "." + SNAKE_NAME)

    login_required = False

    def __init__(self):
        #board_collection.
        import arduino_board_collection.board_collection
        super().__init__()
        plug_in_django_manage.plug_in(VisSpecConfig, self.config)


if __name__ == "__main__":
    VisSpecConfig.baseurl = ""
    VisSpecApp().run(open_browser=True)

