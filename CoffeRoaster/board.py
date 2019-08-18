from ArduinoCodeCreator.arduino import *
from ArduinoCodeCreator.arduino_data_types import *
from ArduinoCodeCreator.basic_types import *
from ArduinoCodeCreator.statements import *
from arduino_board_collection.boards.sensor_signal_boards.signal_switch_boards.relay_max6675_bang_bang.board import (
    RelayMax6675BangBangModule,
)
from arduino_board_collection.boards.signal_boards.switches.relay.board import (
    RelayBoardModule,
)
from arduino_controller.arduino_variable import arduio_variable
from arduino_controller.basicboard.board import (
    ArduinoBoardModule,
    BasicBoardModule,
    ArduinoBoard,
)
from arduino_controller.python_variable import python_variable


class CoffeRoasterModule(ArduinoBoardModule):
    # depencies
    on_off = RelayBoardModule
    temperatur_controller = RelayMax6675BangBangModule

    # arduino_variables

    def instance_arduino_code(self, ad):
        ad.loop.add_call()
        ad.setup.add_call()


class CoffeRoasterBoard(ArduinoBoard):
    FIRMWARE = 451812373601400620
    modules = [CoffeRoasterModule]


if __name__ == "__main__":
    ins = CoffeRoasterBoard()
    ins.create_ino()
