import curses


class CursedMenu:

    def __init__(self, colors):
        self.page_size = 1
        self.current_page = 1
        self.colors = colors
        self.items = []
        self.selected = 0
        return

    def render(self, window):
        row = 1
        col = 1

        max_y, max_x = window.get_max_yx()
        self.page_size = max_y - 3

        first_item_idx = (self.current_page - 1) * self.page_size
        last_item_idx = min(first_item_idx + self.page_size, len(self.items))

        range_to_display = range(first_item_idx, last_item_idx)

        for idx in range_to_display:
            if idx == self.selected and window.get_is_active():
                window.turn_on_color_scheme(self.colors.get_highlight())

            window.render_text(self.items[idx].render(), row, col)
            window.turn_off_color_scheme(self.colors.get_highlight())
            row += 1

        self.render_paging_info(window)

        return

    def render_paging_info(self, window):
        current_page_display = " Page: {0} ".format(self.current_page)
        window.set_page_info_text(current_page_display)

    def handle_key_event(self, key):

        if key == curses.KEY_UP and self.selected > 0:
            self.selected -= 1
        elif key == curses.KEY_DOWN and self.selected < len(self.items)-1:
            self.selected += 1

        self.current_page = self.selected // self.page_size + 1

    def add_menu_item(self, item):
        self.items.append(item)

