import random


def get_random_string(length=16):
    _string = ''
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'

    for i in range(0, length):
        _char = chars[random.randint(0, len(chars) - 1)]
        _char = _char.upper() if random.randint(0, 3) == 0 else _char
        _string += _char

    return _string
