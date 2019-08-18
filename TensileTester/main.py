import os
from os.path import expanduser

from BaseApp import BaseApp
from TensileTester.tensile_tester.apps import TensileTesterConfig


class TensileTesterApp(BaseApp):
    DEBUGGING = True
    BASENAME = "Tensile Tester"
    SNAKE_NAME = BASENAME.lower().replace(" ", "_")
    BASE_DIR = os.path.join(expanduser("~"), "." + SNAKE_NAME)
    app_configs = [TensileTesterConfig]
    login_required = False

    def __init__(self):
        # board_collection.
        super().__init__()


if __name__ == "__main__":
    TensileTesterApp.app_configs[0].baseurl = ""
    # TensileTesterApp().migrate()
    TensileTesterApp().run(open_browser=False, open_data_dir=True)
