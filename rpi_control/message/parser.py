import re
from collections import namedtuple
from .exceptions import ControlledObjectNotFound, ActionNotFound

Command = namedtuple('Command', ['object_name', 'action', 'parameter'])


def extract_part(message: str):
    parts = message.split(":")
    return parts


def get_object(controlled_objects, name: str):
    _object = controlled_objects.get(name)
    if not _object or not getattr(_object, "is_controlable"):
        raise ControlledObjectNotFound(f"No controled object {name}")
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


def translate_command(controlled_objects, command):
    controlled_obj = get_object(controlled_objects, command.object_name)
    action = get_action(controlled_obj, command.action)
    parameter = command.parameter
    return controlled_obj, action, parameter

