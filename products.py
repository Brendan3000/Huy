import math
from functools import reduce

import quotients


def brackets_remover(box_variable):
    if len(box_variable) - 1 == next_closed_bracket(box_variable) and box_variable.find("(") == 0:
        return box_variable[1:len(box_variable)-1]
    else:
        return box_variable


def contains_sum(box_v):
    if box_v[0] == "(" and box_v[len(box_v)-1] == ")":
        index = 0
        without_brackets = box_v[1:len(box_v)-1]
        for letter in box_v[1:len(box_v)-1]:
            if letter == "+" and not is_closed_in(without_brackets[index:]):
                return True
            if letter == "-" and not is_closed_in(without_brackets[index:]):
                return True
            index += 1
    else:
        return False
    return False



# also in powers (to avoid circle)
def exponential_component(list, power):
    exponent,coefficient = list[0], list[1]
    if exponent == "":
        return ""
    else:
        try:
            power = return_number(power)
            coefficient *= power
        except:
            exponent = f"{power}{exponent}"
        if coefficient == 1:
            coefficient = ""
        if coefficient == -1:
            coefficient = "-"
        return f"e^({coefficient}{exponent}) "


def return_number(string):
    if string == "-":
        return -1
    string = str(string)
    if not "." in string:
        return int(string)
    else:
        integer = True
        for letter in string[string.find(".")+1:]:
            if letter != "0":
                integer = False
    if integer:
        return int(string[:string.find(".")])
    else:
        return float(string)


# will turn 2x into "x" and 2, 2sin(x) into "sin(x)",2
def factor_seperator(box_v):
    index_counter = 0
    for letter in  box_v:
        if letter == "-" or letter == "." or letter.isdigit():
            index_counter += 1
        else:
            break
    if index_counter == 0:
        return box_v, 1
    if index_counter == 1:
        if box_v[0] == "-":
            return box_v[1:], -1
        else:
            return box_v[1:], return_number(box_v[:1])
    else:
        return box_v[index_counter:], return_number(box_v[:index_counter])


# Provides the index of the next time brackets were closed
def next_closed_bracket(box_v):
    counter_a = 0
    i = 0
    for letter in box_v:
        if letter == "(":
            counter_a += 1
        if letter == ")":
            counter_a -= 1
            if counter_a == 0:
                break
        i += 1
    return i


# will return true if brackets are not closed
def is_closed_in(box_v):
    counter_a = 0
    for letter in box_v:
        if letter =="(":
            counter_a += 1
        if letter == ")":
            counter_a -= 1
    if counter_a == 0:
        return False
    else:
        return True


# input is a box, ouptut is box with exponetials removed and the power of the exponetial if it were to base e. If not numerator (mean from denomiator, then the exponet factor is  changed in sign)
def exponetial_remover(box_v, numerator):
    letter_index = 0
    for letter in box_v:
        if letter == "e" and not is_closed_in(box_v[letter_index:]):
            exponential_stop = letter_index + next_closed_bracket(box_v[letter_index:])
            exponent = box_v[letter_index+3:exponential_stop]
            exponent, factor = factor_seperator(exponent)
            if exponential_stop == len(box_v) - 2:
                box_v = box_v[:letter_index]
            else:
                box_v = box_v[:letter_index] + box_v[exponential_stop+2:]
            if not numerator:
                factor = -factor
            if not contains_sum(exponent):
                exponent = brackets_remover(exponent)
            return box_v, [exponent, return_number(factor)]
        elif letter == ")" and not is_closed_in(box_v[letter_index+1:]) and box_v[box_v[:letter_index].rfind("(")+1:letter_index].isdigit() and not box_v[:letter_index].rfind("(") == 2 + box_v[:letter_index].rfind("ln"):
            exponential_stop = letter_index + next_closed_bracket(box_v[letter_index+1:]) + 1
            base = int(box_v[box_v[:letter_index].rfind("(")+1:letter_index])
            exponent = box_v[letter_index+3:exponential_stop]
            exponent, factor = factor_seperator(exponent)
            if exponential_stop == len(box_v) - 2:
                box_v = box_v[:box_v[:letter_index].rfind("(")]
            else:
                box_v = box_v[:box_v[:letter_index].rfind("(")] + box_v[exponential_stop+2:]
            if not numerator:
                factor = -factor
            if not contains_sum(exponent):
                exponent = brackets_remover(exponent)
            return box_v,[f"ln({base}){exponent}", return_number(factor)]
        letter_index += 1
    return box_v, ["", 0]


# modified for use in sums factorisation
def exponetial_remover_for_sum(box_v):
    box_v, exponential_list = exponetial_remover(box_v, True)
    exponential_term = exponential_component(exponential_list, 1)
    return box_v, exponential_term


# will return the power, closed term from index of closed bracket
def power_and_remover(box_v, close_index):
    factor = ""
    is_base_power = False
    if len(box_v) == close_index+1:
        return "", 1, is_base_power, factor
    elif box_v[close_index + 1] != "^":
        power = 1
        box_v = box_v[close_index + 1:]
    else:
        index_counter = 0
        for letter in box_v[close_index + 2:]:
            if letter == "-" or letter == "." or letter.isdigit():
                index_counter += 1
            else:
                break
        if index_counter == 0:
            is_base_power = True
            index_space = close_index + next_closed_bracket(box_v[close_index+1:]) + 2
            factor = box_v[:index_space+1]
            power = 1
            box_v = box_v[index_space+1:]
        else:
            power = return_number(box_v[close_index + 2:close_index + 2 + index_counter])
            box_v = box_v[close_index + 3 + index_counter:]
    return box_v, power, is_base_power, factor


# will factorise quotient
def factoriser_for_division(box_one, box_two):
    table = [[],[]]
    while len(box_one) != 0:
        while box_one[0] == " ":
            box_one = box_one[1:]
            if len(box_one) == 0:
                break
        if len(box_one) == 0:
            break
        if box_one[0] == "x":
            factor = "x"
            box_one, power, is_base_power, possible_factor = power_and_remover(box_one, 0)
        else:
            factor = box_one[:next_closed_bracket(box_one)+1]
            box_one, power, is_base_power, possible_factor = power_and_remover(box_one, next_closed_bracket(box_one))
        if is_base_power:
            factor = possible_factor
        table[0].append(factor)
        table[1].append(power)
    while len(box_two) != 0:
        while box_two[0] == " ":
            box_two = box_two[1:]
            if len(box_two) == 0:
                break
        if len(box_two) == 0:
            break
        if box_two[0] == "x":
            factor = "x"
            box_two, power, is_base_power, possible_factor = power_and_remover(box_two, 0)
        else:
            factor = box_two[:next_closed_bracket(box_two)+1]
            box_two, power,is_base_power, possible_factor = power_and_remover(box_two, next_closed_bracket(box_two))
        if is_base_power:
            factor = possible_factor
        power = -power
        if factor in table[0]:
            index = table[0].index(factor)
            table[1][index] += power
        else:
            table[0].append(factor)
            table[1].append(power)
    numerator = ""
    denominator = ""
    for i in range(len(table[0])):
        if table[1][i] == 0:
            continue
        else:
            if table[1][i] > 0:
                is_in_numerator = True
            else:
                is_in_numerator = False
            table[1][i] = abs(table[1][i])
            if table[1][i] == 1:
                to_the_power = ""
            else:
                to_the_power = f"^{table[1][i]} "
            if is_in_numerator:
                numerator += f"{table[0][i]}{to_the_power}"
            else:
                denominator += f"{table[0][i]}{to_the_power}"
    return numerator, denominator


def factoriser_for_multiples(box_one, box_two):
    table = [[],[]]
    while len(box_one) != 0:
        while box_one[0] == " ":
            box_one = box_one[1:]
            if len(box_one) == 0:
                break
        if len(box_one) == 0:
            break
        if box_one[0] == "x":
            factor = "x"
            box_one, power, is_base_power, possible_factor = power_and_remover(box_one, 0)
        else:
            factor = box_one[:next_closed_bracket(box_one)+1]
            box_one, power, is_base_power, possible_factor = power_and_remover(box_one, next_closed_bracket(box_one))
        if is_base_power:
            factor = possible_factor
        table[0].append(factor)
        table[1].append(power)
    while len(box_two) != 0:
        while box_two[0] == " ":
            box_two = box_two[1:]
            if len(box_two) == 0:
                break
        if len(box_two) == 0:
            break
        if box_two[0] == "x":
            factor = "x"
            box_two, power, is_base_power, possible_factor = power_and_remover(box_two, 0)
        else:
            factor = box_two[:next_closed_bracket(box_two)+1]
            box_two, power, is_base_power, possible_factor = power_and_remover(box_two, next_closed_bracket(box_two))
        if factor in table[0]:
            index = table[0].index(factor)
            table[1][index] += power
        else:
            table[0].append(factor)
            table[1].append(power)
    numerator = ""
    for i in range(len(table[0])):
        if table[1][i] == 0:
            continue
        else:
            if table[1][i] == 1:
                to_the_power = ""
            else:
                to_the_power = f"^{table[1][i]} "
            numerator += f"{table[0][i]}{to_the_power}"
    return numerator


# will find common multiples and remove from each term
def factorisation_of_sums_integers(box_coefficients):
    can_factoise = True
    list = []
    for box_c in box_coefficients:
        if not isinstance(box_c, int):
            can_factoise = False
    factor = abs(box_coefficients[0])
    if can_factoise:
        for number in box_coefficients:
            for other_number in box_coefficients:
                possible_factor = math.gcd(abs(other_number),abs(number))
                if possible_factor < factor:
                    factor = possible_factor
        for box_c in box_coefficients:
            list.append(box_c//factor)
        return list, return_number(factor)
    else:
        return box_coefficients, 1


# will find common multiples and remove from each term
def factorisation_of_sums_variables(box_variables):
    list_factors = []
    list_powers = []
    term = 0
    for box_v in box_variables:
        list_factors.append([])
        list_powers.append([])
        while len(box_v) != 0:
            while box_v[0] == " ":
                box_v = box_v[1:]
                if len(box_v) == 0:
                    break
            if len(box_v) == 0:
                    break
            box_v, factor = exponetial_remover_for_sum(box_v)
            if len(factor) != 0:
                list_factors[term].append(factor)
                list_powers[term].append(1)
                if len(box_v) == 0:
                    break
            if box_v[0] == "x":
                factor = "x"
                box_v, power,is_base_power,possible_factor = power_and_remover(box_v, 0)
            else:
                factor = box_v[:next_closed_bracket(box_v)+1]
                box_v, power,is_base_power,possible_factor = power_and_remover(box_v, next_closed_bracket(box_v))
            if is_base_power:
                factor = possible_factor
            list_factors[term].append(factor)
            list_powers[term].append(power)
        term += 1
    common_factors = list(reduce(set.intersection, map(set, list_factors)))
    common_factor_v = ""
    for shared in common_factors:
        # to find min
        min = 10000000000000
        for i in range(len(box_variables)):
            index_of_factor = list_factors[i].index(shared)
            possible_min = list_powers[i][index_of_factor]
            if possible_min < min:
                min = possible_min
        if min <= 0:
            pass
        else:
            for i in range(len(box_variables)):
                index_of_factor = list_factors[i].index(shared)
                list_powers[i][index_of_factor] -= min
            if min == 1:
                index = ""
            else:
                index = f"^{min} "
            common_factor_v += f"{shared}{index}"
    return_box_variables = []
    for i in range(len(box_variables)):
        term = ""
        for k in range(len(list_factors[i])):
            if list_powers[i][k] == 0:
                indi = ""
                list_factors[i][k] = ""
            elif list_powers[i][k] == 1:
                indi = ""
            else:
                indi = f"^{list_powers[i][k]} "
            term += f"{list_factors[i][k]}{indi}"
        return_box_variables.append(term)
    return return_box_variables, common_factor_v


def converter(boxes):
    box_variables = []
    box_coefficients = []
    for i in range(len(boxes)):
        box_variables.append(boxes[i][0])
        box_coefficients.append(boxes[i][1])
    return box_variables, box_coefficients


# will convert some -(g(x)+f(x)) into g(x) - f(x)
def negative_expander(box_v):
    box_v = brackets_remover(box_v)
    index = 0
    changed = False
    for letter in box_v:
        if letter == "-" and not is_closed_in(box_v[index:]):
            box_v= box_v[:index] + "+" + box_v[index+1:]
            changed = True
        if letter == "+" and not is_closed_in(box_v[index:]):
            box_v = box_v[:index] + "-" + box_v[index+1:]
            changed = True
        index += 1
    return box_v, changed


def add(box_variables, box_coefficients, common_factor_v, factor):
    signs = []
    if box_coefficients[0] < 0:
        changed = False
        if box_coefficients[0] == -1:
                if not box_variables[0] == "":
                    box_coefficients[0] = ""
                box_variables[0], changed = negative_expander(box_variables[0])
        if changed:
            signs.append(" + ")
            have_to_change_signs = False
        else:
            signs.append(" - ")
            have_to_change_signs = True
            factor = -factor
    else:
        if box_coefficients[0] == 1 and not box_variables[0] == "":
                box_coefficients[0] = ""
                box_variables[0] = brackets_remover(box_variables[0])
        signs.append(" + ")
        have_to_change_signs = False
    try:
        box_coefficients[0] = abs(box_coefficients[0])
    except:
        pass
    for i in range(1,len(box_variables)):
        if box_coefficients[i] < 0:
            if box_coefficients[i] == -1 and not box_variables[i] == "":
                box_coefficients[i] = ""
                box_variables[i], changed = negative_expander(box_variables[i])
                if changed:
                    have_to_change_signs = not have_to_change_signs
            if have_to_change_signs:
                signs.append(" + ")
            else:
                signs.append(" - ")
        else:
            if have_to_change_signs:
                signs.append(" - ")
            else:
                signs.append(" + ")
            if box_coefficients[i] == 1 and not box_variables[i] == "":
                box_coefficients[i] = ""
                box_variables[i] = brackets_remover(box_variables[i])
        try:
            box_coefficients[i] = abs(box_coefficients[i])
        except:
            pass
    if box_coefficients[0] == 0:
        do_not_put_sign_in_yet = True
    else:
        sum = f"{box_coefficients[0]}{box_variables[0]}"
        do_not_put_sign_in_yet = False
    for k in range(1, len(box_variables)):
        if box_coefficients[k] !=0:
            if do_not_put_sign_in_yet:
                sum += f"{box_coefficients[k]}{box_variables[k]}"
                do_not_put_sign_in_yet = False
            else:
                sum += f"{signs[k]}{box_coefficients[k]}{box_variables[k]}"
                do_not_put_sign_in_yet = False
    try:
        factor = factor*eval(sum)
        if factor == 0:
            sum = ""
        sum = common_factor_v
    except:
        sum = f"{common_factor_v}({sum})"
    return sum, return_number(factor)


def add_for_index(box_one, box_two, do_we_want_to_return_base_power):
    if box_one[0] == "" and box_one[1] == 0 and box_two[0] == "" and box_two[1] == 0:
        return ""
    elif box_one[0] == "" and box_one[1] == 0:
        exponent, factor = box_two[0], box_two[1]
    elif box_two[0] == "" and box_two[1] == 0:
        exponent, factor = box_one[0], box_one[1]
    else:
        numerator_one, denominator_one = quotients.splitter(box_one[0])
        numerator_two, denominator_two = quotients.splitter(box_two[0])
        variables, common_factor_v = factorisation_of_sums_variables([numerator_one,numerator_two])
        coefficients, factor = factorisation_of_sums_integers([box_one[1], box_two[1]])
        numerator, factor = add(variables, coefficients, common_factor_v, factor)
        denominator = multiply_two_together(denominator_one,denominator_two, False)
        numerator,denominator = quotients.divide(numerator,denominator, False)
        exponent = quotients.assembler(numerator,denominator)
    if factor == 1:
        factor = ""
    if factor == -1:
        factor = "-"
    if factor == 0:
        return ""
    if not do_we_want_to_return_base_power:
        return f"e^({factor}{exponent}) "
    else:
        i = 0
        for letter in exponent:
            if letter == "l" and exponent[i:].find("(") == 2 and not is_closed_in(exponent[i:]):
                ncb = i + next_closed_bracket(exponent[i:])
                try:
                    integer_base = return_number(exponent[i + 3:ncb])
                except:
                    return f"e^({factor}{exponent}) "
                if ncb == len(exponent) - 1:
                    exponent = exponent[:i]
                    return f"({integer_base})^({factor}{exponent}) "
                elif ncb != i + exponent[i:].find(")^"):
                    exponent = exponent[:i] + exponent[ncb+1:]
                else:
                    power = return_number(exponent[ncb+2:exponent[i:].find(" ")])
                    length_power = len(str(power))
                    new_power = return_number(power-1)
                    if new_power == 1:
                        index = ""
                    else:
                        index = f"^{new_power} "
                    exponent = exponent = exponent[:i] + f"{exponent[i:ncb+1]}{index}" + exponent[ncb+3+length_power:]
                return f"({integer_base})^({factor}{exponent}) "
            i += 1
    return f"e^({factor}{exponent}) "


def multiply_two_together(box_v_one, box_v_two, do_we_want_to_return_base_power):
    sorted_box_v_one, exponential_list_one = exponetial_remover(box_v_one, True)
    sorted_box_v_two, exponential_list_two = exponetial_remover(box_v_two, True)
    numerator = factoriser_for_multiples(sorted_box_v_one,sorted_box_v_two)
    exponential_component = add_for_index(exponential_list_one,exponential_list_two, do_we_want_to_return_base_power)
    numerator += exponential_component
    return numerator


def a_sum(boxes):
    box_variables, box_coefficients = converter(boxes)
    box_variables, common_factor_v = factorisation_of_sums_variables(box_variables)
    box_coefficients, factor = factorisation_of_sums_integers(box_coefficients)
    sum, factor = add(box_variables, box_coefficients, common_factor_v, factor)
    return sum, factor
