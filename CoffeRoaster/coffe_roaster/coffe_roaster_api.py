from arduino_board_collection.boards.sensor_signal_boards.pid_boards.relay_thermistor_pid.board import \
    RelayThermistor2Board
from arduino_controller.board_api import BoardApi


class CoffeRoasterApi(BoardApi):
    required_boards=[RelayThermistor2Board]




