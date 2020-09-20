import curses

class CursedWindow():

    def __init__(self, hasBorder, title="Window"):
        begin_x = 20; begin_y = 7
        height = 10; width = 40

        # Initialize active window
        self.hasBorder = hasBorder
        self.active_tab = curses.newwin(height, width, begin_y, begin_x)

        # Initialize paging info footer
        self.active_paging_info = curses.newwin(1, width - 2, begin_y + height-1, begin_x + 1)

        # Initialize title
        self.active_title = title

        return

    def clear(self):
        self.active_tab.clear()
        self.active_paging_info.clear()

    def refresh(self):
        if self.hasBorder:
            self.active_tab.box()

        self.active_tab.addstr(0, 1, " {0} ".format(self.active_title))
        self.active_tab.refresh()
        self.active_paging_info.refresh()

    def turnOnColorScheme(self, colorScheme):
        self.active_tab.attron(colorScheme)

    def turnOffColorScheme(self, colorScheme):
        self.active_tab.attroff(colorScheme)

    def setBackgroundColor(self, color):
        self.active_tab.bkgd(' ', color)

    def renderText(self, text, row, col):
        self.active_tab.addstr(row, col, text)

    def getMaxYX(self):
        return self.active_tab.getmaxyx()

    def setPageFooterColor(self, color):
        self.active_paging_info.bkgd(' ', color)

    def setPageInfoText(self, text):
        y_max, x_max = self.active_paging_info.getmaxyx()
        self.active_paging_info.addstr(0, (x_max // 2) - len(text) // 2, text)
