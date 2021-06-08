import tkinter as tk

from .conf import CW, CH, DX, DY, START_POS, FINISH_POS, UP, LEFT, DS, TRACE_IMAGE
from .helper import get_x, get_y, get_image, move_pos


class Player:

    def __init__(self, canvas, board, guide):
        self.canvas = canvas
        self.board = board
        self.guide = guide
        self.p = START_POS
        self.d = UP
        self.images = [get_image(f"./images/player82_{d}.png") for d in DS]
        self.image_wow = get_image(f"./images/player82_wow.png")
        self.step_count = 0

    def respawn(self):
        self.hide(False)
        self.p = START_POS
        self.d = UP
        self.step_count = 0
        self.draw()

    def draw(self):
        x, y = get_x(self.p[0]) + CW // 2 - DX, get_y(self.p[1]) + CH // 2 - DY
        image = self.images[self.d - 1]
        if self.p == FINISH_POS:
            image = self.image_wow
        self.canvas.create_image(x, y, image=image, anchor=tk.CENTER, tag="figure")

    def hide(self, update=True):
        self.canvas.delete("figure")
        if update:
            cx, cy = self.p
            self.board.draw_cell(cx, cy, TRACE_IMAGE + self.direction - 1)

    @property
    def position(self):
        return self.p

    @property
    def direction(self):
        return self.d

    def set_pos(self, p_new):
        if not self.board.check(p_new):
            return False
        self.hide()
        self.p = p_new
        self.draw()
        return self.p != FINISH_POS

    def move_pos(self, d_new=None):
        d = self.d if d_new is None else d_new
        return move_pos(self.p, d)

    def turn_left(self, d_new=None):
        d = self.d if d_new is None else d_new
        d_new = d - 1 if d > UP else LEFT
        return d_new

    def turn_right(self, d_new=None):
        d = self.d if d_new is None else d_new
        d_new = d + 1 if d < LEFT else UP
        return d_new

    def move(self):
        self.d = self.guide(self, self.board)
        p_new = move_pos(self.p, self.d)
        self.step_count += 1
        return self.set_pos(p_new)
