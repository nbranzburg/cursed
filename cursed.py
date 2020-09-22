import curses
from CursedMenu import CursedMenu
from CursedWindow import CursedWindow
from CursedWindowGroup import CursedWindowGroup
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
        self.active_page_info = curses.color_pair(2)

        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_YELLOW)
        self.active_title = curses.color_pair(3)

        curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)
        self.page_info = curses.color_pair(4)

        curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_WHITE)
        self.title = curses.color_pair(5)

    def get_highlight(self):
        return self.highlight

    def get_active_page_info(self):
        return self.active_page_info

    def get_active_title(self):
        return self.active_title

    def get_page_info(self):
        return self.page_info

    def get_title(self):
        return self.title

def main(stdscr):

    defaultColors = CursedColorScheme()

    win = CursedWindow(True, defaultColors, "Actionables", True)
    activeMenu = CursedMenu(win, defaultColors)

    left_win = CursedWindow(True, defaultColors, "Values")
    left_menu = CursedMenu(left_win, defaultColors)

    windowGroup = CursedWindowGroup()

    windowGroup.addSubWindow(stdscr, left_win, CursedWindowGroup.Position.BOTTOM_HORIZONTAL_THIRD)
    windowGroup.addSubWindow(stdscr, win, CursedWindowGroup.Position.TOP_TWO_THIRDS)

    for num in range(40):
        activeMenu.addMenuItem(MenuItem("Option {0}".format(num)))

    for num in range(40):
        left_menu.addMenuItem(MenuItem("Thing {0}".format(num)))
    # turn off cursor blinking
    curses.curs_set(0)

    stdscr.refresh()
    activeMenu.render()
    left_menu.render()

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
