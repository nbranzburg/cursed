import curses
class CursedMenu():

    def __init__(self, window, colors):
        self.window = window
        self.max_y, self.max_x = window.getMaxYX()
        self.page_size = self.max_y - 3
        self.current_page = 1
        self.colors = colors
        self.items = []
        self.selected = 0
        return;

    def render(self):
        row = 1
        col = 1

        firstItemIdx = (self.current_page - 1) * self.page_size
        lastItemIdx = min(firstItemIdx + self.page_size, len(self.items))

        rangeToDisplay = range(firstItemIdx, lastItemIdx)

        self.window.clear()
        for idx in rangeToDisplay:
            if idx == self.selected:
                self.window.turnOnColorScheme(self.colors.get_highlight())
            self.window.renderText(self.items[idx].render(), row, col)
            self.window.turnOffColorScheme(self.colors.get_highlight())
            row+=1

        self.renderPagingInfo()

        self.window.refresh()
        return

    def renderPagingInfo(self):
        self.window.setPageFooterColor(self.colors.get_page_info())
        currentPageDisplay = " Page: {0} ".format(self.current_page)
        self.window.setPageInfoText(currentPageDisplay)

    def processKeyInput(self, key):

        if key == curses.KEY_UP and self.selected > 0:
            self.selected -= 1
        elif key == curses.KEY_DOWN and self.selected < len(self.items)-1:
            self.selected += 1

        self.current_page = self.selected // self.page_size + 1

        return self

    def addMenuItem(self, item):
        self.items.append(item)
