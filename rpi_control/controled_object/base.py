class ControledMeta(type):
    def __new__(cls, *args):
        setattr(cls, "is_controlable", True) # is_controlable attribute identify if it is contrable or not
        return super().__new__(cls, *args)


class RaspObject(metaclass=ControledMeta):
    def __init__(self, channel):
        self.channel = channel # a raspberry pi GPIO number where the object belong

    def __call__(self):
        pass
