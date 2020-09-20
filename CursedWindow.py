import curses

class CursedWindow():

    def __init__(self, hasBorder, title="Window"):
        begin_x = 20; begin_y = 7
        height = 10; width = 40
        self.hasBorder = hasBorder
        self.curses_win = curses.newwin(height, width, begin_y, begin_x)
        self.page_footer_win = curses.newwin(1, width - 2, begin_y + height-1, begin_x + 1)
        self.title = title
        self.win_title = curses.newwin(1, len(title) + 4, begin_y, begin_x + 1)

        return

    def clear(self):
        self.curses_win.clear()
        self.page_footer_win.clear()
        self.win_title.clear()

    def refresh(self):
        if self.hasBorder:
            self.curses_win.box()
        self.curses_win.refresh()
        self.page_footer_win.refresh()
        self.win_title.addstr(0, 1, " {0} ".format(self.title))

        self.win_title.refresh()

    def turnOnColorScheme(self, colorScheme):
        self.curses_win.attron(colorScheme)

    def turnOffColorScheme(self, colorScheme):
        self.curses_win.attroff(colorScheme)

    def setBackgroundColor(self, color):
        self.curses_win.bkgd(' ', color)

    def renderText(self, text, row, col):
        self.curses_win.addstr(row, col, text)

    def getMaxYX(self):
        return self.curses_win.getmaxyx()

    def setPageFooterColor(self, color):
        self.page_footer_win.bkgd(' ', color)

    def setPageInfoText(self, text):
        y_max, x_max = self.page_footer_win.getmaxyx()
        self.page_footer_win.addstr(0, (x_max // 2) - len(text) // 2, text)
