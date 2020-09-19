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

def main(stdscr):

    win = CursedWindow(True)

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    activeMenu = CursedMenu(win, curses.color_pair(1))

    for num in range(4):
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
