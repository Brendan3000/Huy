from products import is_closed_in
from Nice import Brackets


def splitter(box_v):
    index = 0
    for letter in box_v:
        if letter == "/":
            if not is_closed_in(box_v[index:]):
                return box_v[:index], Brackets.brackets_remover( box_v[index+1:])
        index += 1
    return box_v, ""


def has_denomenator(box_v):
    index = 0
    for letter in box_v:
        if letter == "/":
            if not is_closed_in(box_v[index:]):
                return True
    return False

