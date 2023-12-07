from Nice import Brackets
import products


# will return true if brackets are not closed
def is_closed_in(box_v):
    counter_a = 0
    for letter in box_v:
        if letter == "(":
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
        if letter == "/" and not is_closed_in(box_v[index:]):
                return box_v[:index], Brackets.brackets_remover(box_v[index+1:])
        index += 1
    return box_v, ""


def has_denomenator(box_v):
    index = 0
    for letter in box_v:
        if letter == "/" and not is_closed_in(box_v[index:]):
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


def double_brackets_remover(box_v):
    numerator, denominator = splitter(box_v)
    if denominator.find("(") == 0 and denominator.rfind(")") == len(denominator) - 1:
        denominator = Brackets.brackets_remover(denominator)
    if numerator.find("(") == 0 and numerator.rfind(")") == len(numerator) - 1:
        numerator = Brackets.brackets_remover(numerator)
    index = 0
    for letter in denominator:
        index_close_bracket = products.next_closed_bracket(denominator[index:]) + index
        try:
            if letter == "(" and denominator[index+1] == "(" and denominator[index_close_bracket-1] == ")":
                denominator = denominator[:index] + denominator[index+1:index_close_bracket] + denominator[index_close_bracket+1:]
        except:
            pass
        index += 1
    for letter in numerator:
        try:
            index_close_bracket = products.next_closed_bracket(numerator[index:]) + index
            if letter == "(" and numerator[index+1] == "(" and numerator[index_close_bracket-1] == ")":
                numerator = numerator[:index] + numerator[index+1:index_close_bracket] + numerator[index_close_bracket+1:]
        except:
            pass
        index += 1
    return assembler(numerator,denominator)


def float_to_fraction(box):
    box_v, Box_v = box[0]
