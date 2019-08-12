import os
from os.path import expanduser

from BaseApp import BaseApp
from CoffeRoaster.coffe_roaster.apps import CoffeRoasterConfig


class CoffeRoasterApp(BaseApp):
    DEBUGGING = True
    BASENAME = "Coffe Roaster"
    SNAKE_NAME = BASENAME.lower().replace(" ", "_")
    BASE_DIR = os.path.join(expanduser("~"), "." + SNAKE_NAME)
    app_configs = [CoffeRoasterConfig]
    login_required = False

    def __init__(self):
        #board_collection.
        super().__init__()




if __name__ == "__main__":
    CoffeRoasterApp.app_configs[0].baseurl = ""
    CoffeRoasterApp().migrate()
    CoffeRoasterApp().run(open_browser=False,open_data_dir=True)

