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

    top_win = CursedWindow(True, defaultColors, "Actionables", True)
    topMenu = CursedMenu(top_win, defaultColors)

    bottom_win = CursedWindow(True, defaultColors, "Values")
    bottomMenu = CursedMenu(bottom_win, defaultColors)

    windowGroup = CursedWindowGroup()

    windowGroup.addSubWindow(stdscr, bottom_win, CursedWindowGroup.Position.BOTTOM_HORIZONTAL_THIRD)
    windowGroup.addSubWindow(stdscr, top_win, CursedWindowGroup.Position.TOP_TWO_THIRDS)

    for num in range(40):
        topMenu.addMenuItem(MenuItem("Option {0}".format(num)))

    for num in range(40):
        bottomMenu.addMenuItem(MenuItem("Thing {0}".format(num)))
    # turn off cursor blinking
    curses.curs_set(0)

    stdscr.refresh()
    topMenu.render()
    bottomMenu.render()

    keep_going = True
    while keep_going:
        key = stdscr.getch()
        if key == ord('q'):
            keep_going = False
        elif key == ord('\t'):
            bottom_win.setActive(True)
            top_win.setActive(False)
            topMenu.render()
            bottomMenu.render()
        else:
            top_win.handleKeyEvent(key)

        topMenu.render()
        #curses.doupdate()

wrapper(main)
