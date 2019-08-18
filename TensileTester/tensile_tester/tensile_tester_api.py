import time

from arduino_board_collection.boards.sensor_boards.basic.bush_button.board import (
    PushButtonBoard,
)
from arduino_board_collection.boards.sensor_boards.force.tesile_test_board.tesile_test_board import (
    TensileTestBoard,
)
from arduino_controller.board_api import BoardApi, api_function


class TensileTesterApi(BoardApi):
    required_boards = [TensileTestBoard]

    @api_function(kwargs={"mm": dict(type="number", step=0.1, default=0)})
    def set_position(self, mm,allowed_error=0.01):
        mm = float(mm)
        board: TensileTestBoard = self.linked_boards[0]
        board.stepper_current_position = mm
        return board.stepper_current_position

    @api_function(kwargs={"mm": dict(type="number", step=0.1, default=0)})
    def move(self, mm,allowed_error=0.01):
        mm = float(mm)
        board: TensileTestBoard = self.linked_boards[0]
        board.target_position = board.stepper_current_position + mm
        time.sleep(1)
        while abs(board.stepper_current_position - board.target_position) > allowed_error:
            time.sleep(0.1)
        return board.stepper_current_position

    @api_function(kwargs={"mm": dict(type="number", step=0.1, default=0)})
    def move_to(self, mm,allowed_error=0.01):
        mm = float(mm)
        board: TensileTestBoard = self.linked_boards[0]
        board.target_position = mm
        while abs(board.stepper_current_position - board.target_position) > allowed_error:
            time.sleep(0.1)
        return board.stepper_current_position

    @api_function()
    def tare(self):
        board: TensileTestBoard = self.linked_boards[0]
        t = time.time()
        time.sleep(0.1)
        avg =0
        n=0
        while time.time()-t < 5:
            time.sleep(0.1)
            avg += board.value*board.scale + board.offset
            n += 1

        avg = avg / n
        board.offset=avg

    @api_function(visible=False)
    def calibrate(self,spring_rate,max_strain,allowed_error=0.01):
        if allowed_error is None: allowed_error = 0.01
        board: TensileTestBoard = self.linked_boards[0]

        #stop
        board.target_position = board.stepper_current_position
        time.sleep(1)
        #self.tare(api_function_blocking=True)
        while abs(board.stepper_current_position - board.target_position) > allowed_error:
            time.sleep(0.1)
        time.sleep(0.1)
        startposition = board.stepper_current_position
        board.target_position = board.stepper_current_position - max_strain
        while abs(board.stepper_current_position - board.target_position) > allowed_error:
            time.sleep(0.5)
        time.sleep(5)
        force_max=board.value
        position_max = board.stepper_current_position
        board.target_position = startposition
        while abs(board.stepper_current_position - board.target_position) > allowed_error:
            time.sleep(0.5)
        time.sleep(5)
        force_min=board.value
        position_min = board.stepper_current_position
        board.scale=(board.scale*abs(force_max-force_min)/abs(position_min-position_max))/spring_rate
#        (6000 --3000)/20 = 9000/20 = 215576.39*450

