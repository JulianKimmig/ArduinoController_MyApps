import os
from os.path import expanduser

from BaseApp import BaseApp
from CoffeRoaster.coffe_roaster.apps import CoffeRoasterConfig
from CoffeRoaster.coffe_roaster.coffe_roaster_api import CoffeRoasterApi
from arduino_board_collection.boards.sensor_signal_boards.pid_boards.relay_thermistor_pid.board import \
    RelayThermistor2Board
from arduino_controller import parseboards
from plug_in_django import manage as plug_in_django_manage


class CoffeRoasterApp(BaseApp):
    DEBUGGING = True
    BASENAME = "Coffe Roaster"
    SNAKE_NAME = BASENAME.lower().replace(" ", "_")
    BASE_DIR = os.path.join(expanduser("~"), "." + SNAKE_NAME)

    login_required = False

    def __init__(self):
        #board_collection.
        super().__init__()
        plug_in_django_manage.plug_in(CoffeRoasterConfig, self.config)



if __name__ == "__main__":
    CoffeRoasterApp.baseurl = ""
    CoffeRoasterApp().migrate()
    CoffeRoasterApp().run(open_browser=False)

