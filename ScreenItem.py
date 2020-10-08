from MenuItem import MenuItem
from ScreenCommander import ScreenCommander
from datetime import datetime


class ScreenItem(MenuItem):

    def __init__(self, sess_id, windows, raw_json_obj, value):
        super().__init__(value)
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

    def set_last_update(self):
        self.metadata["last_updated"] = datetime.now().strftime("%c")

    def serialize(self):
        data = self.metadata.copy()
        data["session_id"] = self.sess_id
        data["windows"] = self.windows
        return data

    def action(self):
        screen = ScreenCommander(self.sess_id, self.windows)

        screen.attach()
