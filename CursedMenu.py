import curses
class CursedMenu():

    def __init__(self, window, colors):
        self.window = window
        self.window.registerKeyEventHandler(self)

        self.current_page = 1
        self.colors = colors
        self.items = []
        self.selected = 0
        return;

    def updatePageSize(self):
        self.max_y, self.max_x = self.window.getMaxYX()
        self.page_size = self.max_y - 3

    def render(self):
        row = 1
        col = 1

        self.updatePageSize()

        firstItemIdx = (self.current_page - 1) * self.page_size
        lastItemIdx = min(firstItemIdx + self.page_size, len(self.items))

        rangeToDisplay = range(firstItemIdx, lastItemIdx)

        self.window.clear()
        for idx in rangeToDisplay:
            if idx == self.selected and self.window.getIsActive():
                self.window.turnOnColorScheme(self.colors.get_highlight())

            self.window.renderText(self.items[idx].render(), row, col)
            self.window.turnOffColorScheme(self.colors.get_highlight())
            row+=1

        self.renderPagingInfo()

        self.window.refresh()
        return

    def renderPagingInfo(self):
        currentPageDisplay = " Page: {0} ".format(self.current_page)
        self.window.setPageInfoText(currentPageDisplay)

    def handleKeyEvent(self, key):
        self.updatePageSize()

        if key == curses.KEY_UP and self.selected > 0:
            self.selected -= 1
        elif key == curses.KEY_DOWN and self.selected < len(self.items)-1:
            self.selected += 1

        self.current_page = self.selected // self.page_size + 1

    def addMenuItem(self, item):
        self.items.append(item)
