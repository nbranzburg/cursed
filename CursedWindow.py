import curses

class CursedWindow():

    def __init__(self, hasBorder, colors, title="Window", isActive = False):
        self.begin_x = 0
        self.begin_y = 0
        self.height = 50
        self.width = 50

        self.isActive = isActive

        # Intialize color scheme
        self.colors = colors

        # Initialize active window
        self.hasBorder = hasBorder
        self.current_tab = curses.newwin(self.height, self.width, self.begin_y, self.begin_x)

        # Initialize paging info footer
        self.paging_info = curses.newwin(1, self.width - 2, self.begin_y + self.height-1, self.begin_x + 1)


        # Initialize title
        self.active_title = title

        return

    def changePosition(self, height, width, begin_x, begin_y):

        self.height = height
        self.width = width
        self.begin_x = begin_x
        self.begin_y = begin_y

        # Reset window position to avoid accidentally rending outside allowed range
        self.paging_info.mvwin(0, 0)
        self.paging_info.mvwin(0, 0)

        self.current_tab.resize(self.height, self.width)
        self.paging_info.resize(1, self.width - 2)

        self.current_tab.mvwin(self.begin_y, self.begin_x)
        self.paging_info.mvwin(self.begin_y + self.height-1, self.begin_x + 1)

    def clear(self):
        self.current_tab.clear()
        self.paging_info.clear()

    def refresh(self):
        if self.hasBorder:
            self.current_tab.box()

        if self.isActive:
            self.paging_info.bkgd(' ', self.colors.get_active_page_info())
            self.turnOnColorScheme(self.colors.get_active_title())
        else:
            self.paging_info.bkgd(' ', self.colors.get_page_info())
            self.turnOnColorScheme(self.colors.get_title())

        self.current_tab.addstr(0, 1, " {0} ".format(self.active_title))
        self.turnOffColorScheme(self.colors.get_active_title())
        self.turnOffColorScheme(self.colors.get_title())

        self.current_tab.refresh()
        self.paging_info.refresh()

    def turnOnColorScheme(self, colorScheme):
        self.current_tab.attron(colorScheme)

    def turnOffColorScheme(self, colorScheme):
        self.current_tab.attroff(colorScheme)

    def renderText(self, text, row, col):
        self.current_tab.addstr(row, col, text)

    def getMaxYX(self):
        return self.current_tab.getmaxyx()

    def setPageInfoText(self, text):
        y_max, x_max = self.paging_info.getmaxyx()
        self.paging_info.addstr(0, (x_max // 2) - len(text) // 2, text)

    def getIsActive(self):
        return self.isActive
