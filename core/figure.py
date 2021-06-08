import tkinter as tk

from .conf import CW, CH, DX, DY, UP, LEFT, DS
from .helper import get_x, get_y, get_image, move_pos


class Figure:

    def __init__(self, canvas, board, control, name, start_pos, start_direction):
        self.canvas = canvas
        self.board = board
        self.control = control
        self.name = name
        self.start_pos = start_pos
        self.start_direction = start_direction

        self.p = self.start_pos
        self.d = self.start_direction
        self.images = [get_image(f"./images/{name}82_{d}.png") for d in DS]
        self.trace_images = [get_image(f"./images/trace_{name}_82_{d}.png") for d in DS]
        self.step_count = 0

    def respawn(self):
        self.hide(False)
        self.p = self.start_pos
        self.d = self.start_direction
        self.step_count = 0
        self.draw()

    def draw(self):
        x, y = get_x(self.p[0]) + CW // 2 - DX, get_y(self.p[1]) + CH // 2 - DY
        image = self.images[self.d - 1]
        self.canvas.create_image(x, y, image=image, anchor=tk.CENTER, tag=self.name)

    def hide(self, update=True):
        self.canvas.delete(self.name)
        if update:
            trace_image = self.trace_images[self.d - 1]
            self.board.update_cell(self.p, trace_image)

    @property
    def position(self):
        return self.p

    @property
    def direction(self):
        return self.d

    def set_pos(self, p_new):
        if not self.board.check(self, p_new):
            return False
        self.hide()
        self.p = p_new
        self.draw()
        return True

    def check_pos(self, pos):
        return self.board.check(self, pos)

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
        self.d = self.control(self)
        p_new = move_pos(self.p, self.d)
        self.step_count += 1
        return self.set_pos(p_new)
