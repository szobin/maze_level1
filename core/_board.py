import tkinter as tk
import copy

from .conf import COLS, ROWS, MX, MY, PX, PY, CH, MAZE_MAP, DS
from .helper import get_x, get_y, get_image


class Board:

    def __init__(self, canvas):
        self.canvas = canvas
        self.board_map = copy.deepcopy(MAZE_MAP)
        wall_image = get_image("./images/wall_82.png")
        space_image = get_image("./images/space_82.png")
        food_image = get_image("./images/food_82.png")
        self.trace_images = [get_image(f"./images/trace_82_{d}.png") for d in DS]
        self.images = [wall_image, space_image, food_image] + self.trace_images

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

    def get_cell(self, pos):
        x, y = pos
        cell = self.board_map[y][x]
        return cell

    def check(self, pos):
        return self.get_cell(pos) > 0

