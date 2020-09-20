import curses
from CursedMenu import CursedMenu
from CursedWindow import CursedWindow
from curses import wrapper
from curses import textpad

class MenuItem():
    def __init__(self, value):
        self.value = value
        return

    def action(self):
        return

    def render(self):
        return self.value

class CursedColorScheme():

    def __init__(self):
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        self.highlight = curses.color_pair(1)

        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
        self.page_info = curses.color_pair(2)

        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_YELLOW)
        self.active_title = curses.color_pair(3)
        return

    def get_highlight(self):
        return self.highlight

    def get_page_info(self):
        return self.page_info

    def get_active_title(self):
        return self.active_title

def main(stdscr):

    defaultColors = CursedColorScheme()
    win = CursedWindow(True, defaultColors)

    activeMenu = CursedMenu(win, defaultColors)

    for num in range(40):
        activeMenu.addMenuItem(MenuItem("Option {0}".format(num)))

    # turn off cursor blinking
    curses.curs_set(0)

    stdscr.refresh()
    activeMenu.render()

    keep_going = True
    while keep_going:
        key = stdscr.getch()
        if key == ord('q'):
            keep_going = False
        else:
            activeMenu = activeMenu.processKeyInput(key)

        activeMenu.render()
        #curses.doupdate()

wrapper(main)
