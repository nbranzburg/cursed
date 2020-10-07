import curses
from CursedMenu import CursedMenu
from CursedWindow import CursedWindow
from CursedWindowGroup import CursedWindowGroup
from curses import wrapper
from MenuItem import MenuItem
from ScreenItem import ScreenItem
from SessionStorage import SessionStorage


class CursedColorScheme:

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

        curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
        self.menu = curses.color_pair(6)

    def get_menu(self):
        return self.menu

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
    default_colors = CursedColorScheme()

    top_menu = CursedMenu(default_colors)
    top_win = CursedWindow(True, default_colors, top_menu, "Actionables", True)

    bottom_menu = CursedMenu(default_colors)
    bottom_win = CursedWindow(True, default_colors, bottom_menu, "Values")

    window_group = CursedWindowGroup()

    window_group.add_sub_window(stdscr, bottom_win, CursedWindowGroup.Position.BOTTOM_HORIZONTAL_THIRD)
    window_group.add_sub_window(stdscr, top_win, CursedWindowGroup.Position.TOP_TWO_THIRDS)

    try:
        sessions = SessionStorage("./test.json").get_sessions()
        for sess in sessions:
            item = ScreenItem(sess["session_id"], sess["windows"], sess)
            top_menu.add_menu_item(item)
    except FileNotFoundError:
        print("No stored sessions found")

    for num in range(40):
        bottom_menu.add_menu_item(MenuItem("Thing {0}".format(num)))
    # turn off cursor blinking
    curses.curs_set(0)

    stdscr.refresh()
    window_group.update_all()

    keep_going = True
    while keep_going:
        key = stdscr.getch()
        if key == ord('q'):
            keep_going = False
        else:
            window_group.handle_key_event(key)

        if key == curses.KEY_ENTER or key == 10:
            # If a screen session as entered, we will need the keypad mode back on
            stdscr.keypad(1)

        window_group.update_all()


wrapper(main)
