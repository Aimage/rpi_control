
from .base import RaspObject


class Light(RaspObject):

    def __init__(self, channel, name=""):
        self.status = "on"
        self.name = name
        super().__init__(channel)

    def __call__(self, action, value):
        action = getattr(self, action)
        if not action:
            return
        action(value)

    def switch(self, value):
        result = f"{self.name} switched "
        if value == "on":
            result = result + "on"
        if value == "off":
            result = result + "off"
        return result

