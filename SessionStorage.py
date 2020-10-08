import json


class SessionStorage:

    def __init__(self, stored_session_file):
        self.stored_session_file = stored_session_file

        self.sessions = []

        return

    def print_contents(self):
        print(self.sessions)

    def load_sessions(self):
        with open(self.stored_session_file) as stored_sessions:
            self.sessions = json.load(stored_sessions)

        return self.sessions

    def add_session(self, session):
        self.remove_session(session["session_id"])
        self.sessions.append("session_id")

    def remove_session(self, session_id):
        sess_to_remove = None
        for existing_sess in self.sessions:
            if existing_sess["session_id"] == session_id:
                session_to_remove = existing_sess

        if sess_to_remove is not None:
            self.sessions.remove(sess_to_remove)

    def save_sessions(self):
        with open(self.stored_session_file, "w+") as stored_sessions:
            json.dump(self.sessions, stored_sessions)
