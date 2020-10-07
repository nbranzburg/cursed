from MenuItem import MenuItem
from ScreenCommander import ScreenCommander


class ScreenItem(MenuItem):

    def __init__(self, sess_id, windows, raw_json_obj):
        self.sess_id = sess_id
        self.windows = windows
        self.metadata = raw_json_obj.copy()
        del self.metadata["session_id"]
        del self.metadata["windows"]

    def render(self):
        output = self.sess_id
        for meta in self.metadata:
            output += "\t" + str(self.metadata[meta])

        return output

    def action(self):
        screen = ScreenCommander(self.sess_id, self.windows)

        screen.attach()
