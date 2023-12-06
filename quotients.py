from Nice import Brackets
import products


# will return true if brackets are not closed
def is_closed_in(box_v):
    counter_a = 0
    i = 0
    for letter in box_v:
        if letter =="(":
            counter_a += 1
        if letter == ")":
            counter_a -= 1
    if counter_a == 0:
        return False
    else:
        return True


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


def divide(numerator, denominator):
    sorted_numerator, exponential_numerator = products.exponetial_remover(numerator, True)
    sorted_denominator, exponential_denominator = products.exponetial_remover(denominator, False)
    numerator, denominator = products.factoriser_for_division(sorted_numerator,sorted_denominator)
    exponential_component = products.add_for_index(exponential_numerator,exponential_denominator)
    numerator += exponential_component
    return numerator, denominator


def assembler(numerator, denominator):
    if denominator == "":
        return numerator
    else:
        return f"{numerator}/({denominator})"
