from .message.parser import parse_command, translate_command


def execute(controlled_objects, command):
    status = "OK"
    try:
        controled_obj, action, parameter = translate_command(
            controlled_objects, command)
        result = action(parameter)
    except Exception as e:
        status = "ER"
        result = str(e)
    result = f"{status}:{result}"
    return result


def evaluate(controlled_objects, message):
    commands = parse_command(message)
    results = []
    for command in commands:
        result = execute(controlled_objects, command)
        results.append(result)
    return results
