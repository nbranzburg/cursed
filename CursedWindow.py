import curses

class CursedWindow():

    def __init__(self, hasBorder, colors, title="Window"):
        self.begin_x = 0
        self.begin_y = 0
        self.height = 50
        self.width = 50

        # Intialize color scheme
        self.colors = colors

        # Initialize active window
        self.hasBorder = hasBorder
        self.active_tab = curses.newwin(self.height, self.width, self.begin_y, self.begin_x)

        # Initialize paging info footer
        self.active_paging_info = curses.newwin(1, self.width - 2, self.begin_y + self.height-1, self.begin_x + 1)
        self.active_paging_info.bkgd(' ', self.colors.get_page_info())

        # Initialize title
        self.active_title = title

        return

    def changePosition(self, height, width, begin_x, begin_y):

        self.height = height
        self.width = width
        self.begin_x = begin_x
        self.begin_y = begin_y

        # Reset window position to avoid accidentally rending outside allowed range
        self.active_paging_info.mvwin(0, 0)
        self.active_paging_info.mvwin(0, 0)

        self.active_tab.resize(self.height, self.width)
        self.active_paging_info.resize(1, self.width - 2)

        self.active_tab.mvwin(self.begin_y, self.begin_x)
        self.active_paging_info.mvwin(self.begin_y + self.height-1, self.begin_x + 1)



    def clear(self):
        self.active_tab.clear()
        self.active_paging_info.clear()

    def refresh(self):
        if self.hasBorder:
            self.active_tab.box()

        self.turnOnColorScheme(self.colors.get_active_title())
        self.active_tab.addstr(0, 1, " {0} ".format(self.active_title))
        self.turnOffColorScheme(self.colors.get_active_title())

        self.active_tab.refresh()
        self.active_paging_info.refresh()

    def turnOnColorScheme(self, colorScheme):
        self.active_tab.attron(colorScheme)

    def turnOffColorScheme(self, colorScheme):
        self.active_tab.attroff(colorScheme)

    def renderText(self, text, row, col):
        self.active_tab.addstr(row, col, text)

    def getMaxYX(self):
        return self.active_tab.getmaxyx()

    def setPageInfoText(self, text):
        y_max, x_max = self.active_paging_info.getmaxyx()
        self.active_paging_info.addstr(0, (x_max // 2) - len(text) // 2, text)
