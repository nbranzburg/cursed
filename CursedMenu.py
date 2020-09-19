import curses
class CursedMenu():

    def __init__(self, window, highlight_color):
        self.window = window


        self.highlight_color = highlight_color
        self.items = []
        self.selected = 0
        return;

    def render(self):
        row = 1
        col = 1
        #self.window.clear()
        for item in self.items:
            if row-1 == self.selected:
                self.window.turnOnColorScheme(self.highlight_color)
            self.window.renderText(item.render(), row, col)
            self.window.turnOffColorScheme(self.highlight_color)
            row+=1
        self.window.refresh()
        return

    def processKeyInput(self, key):

        if key == curses.KEY_UP and self.selected > 0:
            self.selected -= 1
        elif key == curses.KEY_DOWN and self.selected < len(self.items)-1:
            self.selected += 1

        return self

    def addMenuItem(self, item):
        self.items.append(item)
