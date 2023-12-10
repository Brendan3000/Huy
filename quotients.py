from Nice import Brackets
import products


# will return true if brackets are not closed
def is_closed_in(box_v):
    counter_a = 0
    # counter_a being equal to zero AFTER the for loop signifyes that every bracket has a corresponding close bracket.
    for letter in box_v:
        if letter == "(":
            counter_a += 1
        if letter == ")":
            counter_a -= 1
    if counter_a == 0:
        return False
    else:
        return True


# Input is a box_v (string). Output is the numerator and denominator component of the box v
def splitter(box_v):
    index = 0
    for letter in box_v:
        if letter == "/" and not is_closed_in(box_v[index:]):
                return box_v[:index], Brackets.brackets_remover(box_v[index+1:])
        index += 1
    return box_v, ""


# Input is a box_v (string). will return true if box_v has a denomenator
def has_denomenator(box_v):
    index = 0
    for letter in box_v:
        if letter == "/" and not is_closed_in(box_v[index:]):
            return True
    return False


# Input is two boxs in the form [box_v, box_c]. Output the first (numerator) divided by the second (the denominator) and will be numerator, denominator (both string) .do_we_want_to_return_base_power is a boolean value; if true, if will keep the base of any exponetial factors
def divide(numerator, denominator, do_we_want_to_return_base_power):
    sorted_numerator, exponential_numerator = products.exponetial_remover(numerator, True)
    sorted_denominator, exponential_denominator = products.exponetial_remover(denominator, False)
    numerator, denominator = products.factoriser_for_division(sorted_numerator,sorted_denominator)
    exponential_component = products.add_for_index(exponential_numerator,exponential_denominator, do_we_want_to_return_base_power)
    numerator += exponential_component
    return numerator, denominator


# Given a numerator and denominator (both strings), output will be them assempled in the form g(x)/(f(x))
def assembler(numerator, denominator):
    if denominator == "":
        return numerator
    else:
        return f"{numerator}/({denominator})"


# Serves to remove double brackets and other unessusary brackets around the numerator and denominator. can_we_release_the_numerator is a boolean value; if true will release brackets around the numerator
def double_brackets_remover(box_v,can_we_release_the_numerator):
    # removing brackets around the numerator and denominator
    numerator, denominator = splitter(box_v)
    if denominator.find("(") == 0 and products.next_closed_bracket(denominator) == len(denominator) - 1:
        denominator = Brackets.brackets_remover(denominator)
    if numerator.find("(") == 0 and numerator.rfind(")") == len(numerator) - 1 and can_we_release_the_numerator and not products.contains_sum(numerator):
        numerator = Brackets.brackets_remover(numerator)
    index = 0
    # removing double brackets
    for letter in denominator:
        index_close_bracket = products.next_closed_bracket(denominator[index:]) + index
        try:
            if letter == "(" and denominator[index+1] == "(" and denominator[index_close_bracket-1] == ")":
                denominator = denominator[:index] + denominator[index+1:index_close_bracket] + denominator[index_close_bracket+1:]
        except:
            # in the case of index being out of range
            pass
        index += 1
    index = 0
    for letter in numerator:
        try:
            index_close_bracket = products.next_closed_bracket(numerator[index:]) + index
            if letter == "(" and numerator[index+1] == "(" and numerator[index_close_bracket-1] == ")":
                numerator = numerator[:index] + numerator[index+1:index_close_bracket] + numerator[index_close_bracket+1:]
        except:
            # in the case of index being out of range
            pass
        index += 1
    return assembler(numerator,denominator)


