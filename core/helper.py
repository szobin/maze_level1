import os
from PIL import Image, ImageTk

from core.conf import CW, CH, MX, MY, PX, PY, COLS, ROWS, RIGHT, LEFT, UP, DOWN


def get_x(cx):
    return cx*CW + MX + PX


def get_y(cy):
    return cy*CH + MY + PY


def move_pos(pos, d):
    x, y = pos
    if d == RIGHT:
        x += 1
    if d == LEFT:
        x -= 1
    if d == UP:
        y -= 1
    if d == DOWN:
        y += 1
    return x, y


def to_transparent_image(img):
    img_data = img.getdata()
    transparent_color = img_data[0][:3]
    alpha_color = transparent_color + (0,)

    new_data = [alpha_color if px[:3] == transparent_color else px for px in img_data]
    img.putdata(new_data)
    return ImageTk.PhotoImage(img)


def get_image(fn, transparent=False):
    if not os.path.isfile(fn):
        return None
    img = Image.open(fn).convert("RGBA")
    return ImageTk.PhotoImage(img) if not transparent else to_transparent_image(img)

