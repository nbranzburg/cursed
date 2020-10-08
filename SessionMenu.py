from CursedMenu import CursedMenu


class SessionMenu(CursedMenu):

    def __init__(self, colors, session_storage):
        super().__init__(colors)
        self.storage = session_storage

    def handle_special_key_event(self, key):
        pass

    def save(self):
        menu_items = self.get_menu_items()
        sessions_to_save = []
        for item in menu_items:
            sessions_to_save.append(item.serialize())
            self.storage.save_sessions()
