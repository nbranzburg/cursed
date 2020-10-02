import curses


class CursedDropMenu:

    def __init__(self, colors):
        self.items = ["(q)\t- Quit", "(TAB)\t- Toggle Windows", "(/)\t- Search"]
        self.colors = colors
        self.canvas = curses.newwin(0, 0, 0, 0)

    def render(self, window):
        self.canvas.bkgd(' ', self.colors.get_menu())
        win_x, win_y, win_height, win_width = window.get_pos_info()

        self.change_position(win_height - 3, win_width // 3, (win_width - 1) - win_width // 3, win_y+1)
        self.canvas.clear()

        row = 0
        for item in self.items:
            self.canvas.addstr(row, 1, item)
            row += 1

        self.canvas.refresh()
        return

    def change_position(self, height, width, begin_x, begin_y):

        self.canvas.resize(height, width)
        self.canvas.mvwin(begin_y, begin_x)
