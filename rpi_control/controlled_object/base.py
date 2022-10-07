class ControlledMeta(type):
    def __new__(cls, name, bases, dic):
        if 'is_controllable' not in dic:
            dic['is_controllable'] = True # is_controllable attribute identifies if it is controllable or not
        return super().__new__(cls, name, bases, dic)


class RaspObject(metaclass=ControlledMeta):
    def __init__(self, channel):
        self.channel = channel # a raspberry pi GPIO number where the object belong

    def __call__(self):
        pass
