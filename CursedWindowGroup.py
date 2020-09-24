from enum import Enum


class CursedWindowGroup:

    class Position(Enum):
        LEFT_VERTICAL_SPLIT = 0
        RIGHT_VERTICAL_SPLIT = 1
        TOP_HORIZONTAL_SPLIT = 2
        BOTTOM_HORIZONTAL_SPLIT = 3
        TOP_TWO_THIRDS = 4
        TOP_HORIZONTAL_THIRD = 5
        MIDDLE_HORIZONTAL_THIRD = 6
        BOTTOM_HORIZONTAL_THIRD = 7

    def __init__(self):
        self.windows = []
        return

    def add_sub_window(self, parent_window, window, position):
        y_max, x_max = parent_window.getmaxyx()

        if position == CursedWindowGroup.Position.LEFT_VERTICAL_SPLIT:
            window.change_position(y_max, x_max // 2, 0, 0)
        elif position == CursedWindowGroup.Position.RIGHT_VERTICAL_SPLIT:
            window.change_position(y_max, x_max // 2, x_max // 2, 0)
        elif position == CursedWindowGroup.Position.TOP_HORIZONTAL_SPLIT:
            window.change_position(y_max // 2, x_max, 0, 0)
        elif position == CursedWindowGroup.Position.TOP_TWO_THIRDS:
            window.change_position((2 * y_max) // 3, x_max, 0, 0)
        elif position == CursedWindowGroup.Position.BOTTOM_HORIZONTAL_THIRD:
            window.change_position(y_max // 3, x_max, 0, (2 * y_max) // 3)
        elif position == CursedWindowGroup.Position.TOP_HORIZONTAL_THIRD:
            window.change_position(y_max // 3, x_max, 0, 0)
        elif position == CursedWindowGroup.Position.MIDDLE_HORIZONTAL_THIRD:
            window.change_position(y_max // 3, x_max, 0, y_max // 3)
        elif position == CursedWindowGroup.Position.BOTTOM_HORIZONTAL_THIRD:
            window.change_position(y_max // 3, x_max, 0, (2 * y_max) // 3)
        return
