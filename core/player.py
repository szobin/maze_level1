import tkinter as tk

from .conf import CW, CH, DX, DY, PLAYER_START_POS, PLAYER_START_DIRECTION, FOOD_IMAGE, MAX_STEP_COUNT
from .figure import Figure
from .helper import get_x, get_y, get_image


class Player(Figure):

    def __init__(self, canvas, board, control):
        super().__init__(canvas, board, control, 'player', PLAYER_START_POS, PLAYER_START_DIRECTION)
        self.image_wow = get_image(f"./images/player82_wow.png")

    def is_finish(self):
        return (self.board.get_cell(self.p) == FOOD_IMAGE) or (self.step_count >= MAX_STEP_COUNT)

    def draw(self):
        x, y = get_x(self.p[0]) + CW // 2 - DX, get_y(self.p[1]) + CH // 2 - DY
        image = self.images[self.d - 1]
        if self.is_finish():
            image = self.image_wow
        self.canvas.create_image(x, y, image=image, anchor=tk.CENTER, tag=self.name)

    def set_pos(self, p_new):
        r = super().set_pos(p_new)
        return r and not self.is_finish()
