class MenuItem:
    def __init__(self, value):
        self.value = value
        return

    def __iter__(self):
        return self

    def action(self):
        return

    def render(self):
        return self.value

    def dump_values(self):
        return self.value

    def serialize(self):
        return self.value

