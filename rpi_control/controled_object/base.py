class ControledMeta(type):
    def __new__(cls, *args):
        setattr(cls, "is_controlable", True)
        return super().__new__(cls, *args)


class RaspObject(metaclass=ControledMeta):
    def __init__(self, channel):
        self.channel = channel

    def __call__(self):
        pass
