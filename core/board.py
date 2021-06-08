import tkinter as tk
import copy

from .conf import COLS, ROWS, MX, MY, PX, PY, CH, MAZE_MAP, DS
from .helper import get_x, get_y, get_image


class Board:

    def __init__(self, canvas, check_func=None):
        self.canvas = canvas
        self.check_func = check_func
        self.board_map = copy.deepcopy(MAZE_MAP)
        wall_image = get_image("./images/wall_82.png")
        space_image = get_image("./images/space_82.png")
        food_image = get_image("./images/food_82.png")
        self.images = [wall_image, space_image, food_image]

    def reset(self):
        self.board_map = copy.deepcopy(MAZE_MAP)
        self.canvas.delete("game_over")
        self.canvas.delete("board")
        self.draw()

    def draw_cell(self, cx, cy, cell):
        x = get_x(cx)
        y = get_y(cy)
        image = self.images[cell]
        self.canvas.create_image(x, y, image=image, tag="board", anchor=tk.NW)

    def update_cell(self, pos, image):
        cx, cy = pos
        x = get_x(cx)
        y = get_y(cy)
        self.canvas.create_image(x, y, image=image, tag="board", anchor=tk.NW)

    def draw(self):
        self.canvas.create_rectangle(
            MX, MY,
            get_x(COLS) + PX,
            get_y(ROWS) + PY,
            fill="white", tag="board")

        for y, row in enumerate(self.board_map):
            for x, cell in enumerate(row):
                self.draw_cell(x, y, cell)

    def draw_game_over_panel(self, info):
        self.canvas.create_rectangle(get_x(COLS // 2 - 3), get_y(ROWS // 2 - 2),
                                     get_x(COLS // 2 + 4), get_y(ROWS // 2 + 2), fill='red', tag="game_over")
        tx = get_x(COLS) // 2 + 10
        ty = get_y(ROWS) // 2 - CH
        self.canvas.create_text(tx, ty, text="GAME OVER!", anchor=tk.CENTER, fill="white",
                                font=('Tahoma', 40), tag="game_over")

        tx = get_x(COLS) // 2 + 10
        ty = get_y(ROWS) // 2
        self.canvas.create_text(tx, ty, text=info, anchor=tk.CENTER, fill="yellow",
                                font=('Tahoma', 30), tag="game_over")

    def set_cell(self, pos, cell):
        x, y = pos
        self.board_map[y][x] = cell
        self.draw_cell(x, y, cell)

    def get_cell(self, pos):
        x, y = pos
        if (x < 0) or (y < 0) or (x >= COLS) or (y >= ROWS):
            return WALL_IMAGE
        cell = self.board_map[y][x]
        return cell

    def check(self, sender, pos):
        if (sender is not None) and (self.check_func is not None):
            return self.check_func(sender, pos)
        return self.get_cell(pos) > 0

