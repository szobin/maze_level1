import random


def guide(figure):
    turn = random.choice((figure.turn_left, figure.turn_right))
    d_new = figure.direction

    while True:
        p_new = figure.move_pos(d_new)
        if figure.check_pos(p_new):
            return d_new

        d_new = turn(d_new)



