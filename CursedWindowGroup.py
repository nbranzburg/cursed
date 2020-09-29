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

        self.windows.append(window)

        return

    def update_all(self):
        for win in self.windows:
            win.clear()
            win.refresh()

    def handle_key_event(self, key):
        active_win = self.windows[0]

        idx = 1
        active_idx = 0
        num_wins = len(self.windows)

        while idx < num_wins:
            if self.windows[idx].get_is_active():
                active_win = self.windows[idx]
                active_idx = idx
            idx += 1

        if key == ord('\t'):
            if num_wins > 1:
                if active_idx == num_wins - 1:
                    active_win.set_active(False)
                    self.windows[0].set_active(True)
                else:
                    self.windows[active_idx + 1].set_active(True)
        else:
            active_win.handle_key_event(key)
