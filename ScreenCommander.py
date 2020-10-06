import os
import subprocess


def sess_cmd(session_id, cmd):
    return "screen -S {0} -X {1}".format(session_id, cmd)


def win_cmd(session_id, win_id, cmd):
    return "screen -S {0} -p {1} -X {2}".format(session_id, win_id, cmd)


def run_subprocess(args):
    completed_process = subprocess.run(args, capture_output=True)
    return completed_process.stdout.decode("utf-8")


class ScreenCommander:

    def __init__(self, session_id, windows):
        self.session_id = session_id
        self.windows = windows
        self.active_window = windows[0]
        self.output_dir = "./output/"
        os.system("mkdir -p {0}".format(self.output_dir))

        if not ScreenCommander.exists(session_id):
            ScreenCommander.create_detached_session(session_id)

        self.create_windows()

    @staticmethod
    def exists(session_id):
        result = run_subprocess(["screen", "-ls"])
        return session_id in result

    @staticmethod
    def create_detached_session(session_id):
        os.system("screen -dmS {0}".format(session_id))

    def window_exists(self, window_id):
        result = run_subprocess(["screen", "-S", self.session_id, "-Q", "windows"])
        return window_id in result

    def create_windows(self):
        for window_id in self.windows:
            if not self.window_exists(window_id):
                os.system(sess_cmd(self.session_id, "screen"))
                os.system(sess_cmd(self.session_id, "title {0}".format(window_id)))

    def attach(self):
        os.system("screen -R {0}".format(self.session_id))

    def send_command(self, cmd):
        window_command = win_cmd(self.session_id, self.active_window, "stuff \"{0}^M\"".format(cmd))
        print(window_command)
        os.system(window_command)

    def clear(self):
        os.system(win_cmd(self.session_id, self.active_window, "clear"))
        os.system(win_cmd(self.session_id, self.active_window, "scrollback 0"))
        os.system(win_cmd(self.session_id, self.active_window, "scrollback 150000"))

    def dump_to_file(self):
        os.system(win_cmd(self.session_id, self.active_window, "hardcopy -h {0}{1}".format(self.output_dir, self.session_id)))

    def grab_contents(self):
        self.dump_to_file()
        result = run_subprocess(["cat", "{0}{1}".format(self.output_dir, self.session_id)])
        return result.strip()

    def set_active_window(self, window_id):
        self.active_window = window_id

    def run_batch_file(self, path):
        os.system(sess_cmd(self.session_id, "bufferfile {0}".format(path)))
        os.system(sess_cmd(self.session_id, "readbuf"))
        os.system(sess_cmd(self.session_id, "paste ."))
        os.system(sess_cmd(self.session_id, "bufferfile"))
