import json


class SessionStorage:

    def __init__(self, stored_session_file):
        self.stored_session_file = stored_session_file

        with open(self.stored_session_file) as stored_sessions:
            self.sessions = json.load(stored_sessions)

        return

    def print_contents(self):
        print(self.sessions)

    def get_sessions(self):
        return self.sessions
