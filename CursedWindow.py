import curses

class CursedWindow():

    def __init__(self, hasBorder):
        begin_x = 20; begin_y = 7
        height = 10; width = 40
        self.curses_win = curses.newwin(height, width, begin_y, begin_x)
        if hasBorder:
            self.curses_win.box()
        return

    def clear(self):
        self.curses_win.clear()

    def refresh(self):
        self.curses_win.refresh()

    def turnOnColorScheme(self, colorScheme):
        self.curses_win.attron(colorScheme)

    def turnOffColorScheme(self, colorScheme):
        self.curses_win.attroff(colorScheme)

    def renderText(self, text, row, col):
        self.curses_win.addstr(row, col, text)
