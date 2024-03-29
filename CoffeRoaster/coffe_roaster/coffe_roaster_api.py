import time

from CoffeRoaster.board import CoffeRoasterBoard
from arduino_controller.board_api import BoardApi, api_function


def api_functiosn(target_temperature, func):
    print(target_temperature, func)
    return func


class CoffeRoasterApi(BoardApi):
    required_boards = [CoffeRoasterBoard]

    @api_function(visible=False)
    def run_programm(self, temperature_program):
        board = self.linked_boards[0]
        #:RelayThermistor2Board \

        board.running = False
        board.reset()
        time.sleep(0.4)
        board.running = True
        board.target_temperature = 0
        last_step = 0
        for step in temperature_program:
            board.target_temperature = step[1]
            time.sleep(step[0] - last_step)
            last_step = step[0]
        board.target_temperature = 0
        board.running = False

    @api_function(kwargs={"temperature": dict(type="number", step=0.1, default=20)})
    def preheat(self, temperature):
        board: RelayThermistor2Board = self.linked_boards[0]
        self.logger.info("preheat to {} {}".format(temperature, board.scale_type))
        board.running = False
        time.sleep(0.4)
        board.running = True
        board.target_temperature = temperature
