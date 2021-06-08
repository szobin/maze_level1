def guide(figure):
    # try to turn left
    d_new = figure.turn_left()
    p_new = figure.move_pos(d_new)
    if figure.check_pos(p_new):
        return d_new

    # try to go forward
    d_new = figure.direction
    p_new = figure.move_pos(d_new)
    if figure.check_pos(p_new):
        return d_new

    # try to turn right
    d_new = figure.turn_right()
    p_new = figure.move_pos(d_new)
    if figure.check_pos(p_new):
        return d_new

    # try to turn over
    d_new = figure.turn_right(d_new)
    p_new = figure.move_pos(d_new)
    if figure.check_pos(p_new):
        return d_new

    return None

