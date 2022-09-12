
from .base import RaspObject


class Light(RaspObject):

    def __init__(self, channel):
        self.status = "on"
        super().__init__(channel)

    def __call__(self, action, value):
        action = getattr(self, action)
        if not action:
            return
        action(value)

    def switch(self, value):
        if value == "on":
            return "Light on"
        if value == "off":
            return "Light off"

