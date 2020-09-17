import curses
from curses import wrapper

class CursedMenu():

    def __init__(self, window):
        self.stdscr = window
        return;

    def render(self):
        return

    def processKeyInput(self, key):
        return self

def main(stdscr):

    activeMenu = CursedMenu(stdscr)
    # Clear screen
    stdscr.clear()
    activeMenu.render()
    keep_going = True
    while keep_going:
        key = stdscr.getch()
        if key == ord('q'):
            keep_going = False
        else:
            activeMenu = activeMenu.processKeyInput(key)

wrapper(main)
