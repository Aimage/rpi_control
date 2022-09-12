import re
from collections import namedtuple
from .exceptions import ControledObjectNotFound, ActionNotFound

Command = namedtuple('Command', ['object_name', 'action', 'parameter'])


def extract_part(message: str):
    parts = message.split(":")
    return parts


def get_object(controled_objects, name: str):
    _object = controled_objects.get(name)
    if not _object:
        raise ControledObjectNotFound(f"No controled object {name}")
    return _object


def get_action(_object, action_name: str):
    action = getattr(_object, action_name)
    if not _object:
        raise ActionNotFound(f"No action {action_name}")
    return action


def parse_command(message: str):
    lines = message.split("\n")
    commands = []
    for line in lines:
        parts = extract_part(line)
        if len(parts) != 3:
            continue
        command = Command(parts[0].strip(), parts[1].strip(), parts[2].strip())
        commands.append(command)
    return commands


def translate_command(controled_objects, command):
    controled_obj = get_object(controled_objects, command.object_name)
    action = get_action(controled_obj, command.action)
    parameter = command.parameter
    return controled_obj, action, parameter
