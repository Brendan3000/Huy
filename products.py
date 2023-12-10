import math
from functools import reduce
import quotients

# severs to convert some (f(x)) into f(x) if only in that form
def brackets_remover(box_variable):
    if len(box_variable) - 1 == next_closed_bracket(box_variable) and box_variable.find("(") == 0:
        return box_variable[1:len(box_variable)-1]
    else:
        return box_variable


# will return True if come (f(x)) contains a sum e.g. (x + cos(x)) but not (xcos(x + sin(x)))
def contains_sum(box_v):
    if len(box_v) == 0:
        return ""
    if box_v[0] == "(" and box_v[len(box_v)-1] == ")":
        index = 0
        # Searching through the string to find if any -+ is only contained by one bracket
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


# list contains exponet (string) and a coefficient (float/integer). power is a float, string or integer. will return e raised to the product of these three inputs.
def exponential_component(list, power):
    exponent,coefficient = list[0], list[1]
    # case where there is a null exponential
    if exponent == "":
        return ""
    else:
        try:
            # where power is a integer/float
            power = return_number(power)
            coefficient *= power
        except:
            # where power is a string
            exponent = multiply_two_together(power,exponent, False)
        # to avoid 1box or -1box
        if coefficient == 1:
            coefficient = ""
        if coefficient == -1:
            coefficient = "-"
        return f"e^({coefficient}{exponent}) "


# converts a sting, integer, or float into a nice float or integer
def return_number(string):
    if string == "-":
        return -1
    # in case it's not already a string
    string = str(string)
    if not "." in string:
        return int(string)
    else:
        integer = True
        # To test if it is some 5.000 to be able to convert to 5
        for letter in string[string.find(".")+1:]:
            if letter != "0":
                integer = False
    if integer:
        return int(string[:string.find(".")])
    else:
        return float(string)


# will turn 2x into "x" and 2, 2sin(x) into "sin(x)", 2
def factor_seperator(box_v):
    index_counter = 0
    # finding the length of the coefficient in front (index counter after the end of the loop)
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
    # counter_a being equal to zero AFTER the for loop ensures each open bracket has a respective close bracket
    for letter in box_v:
        if letter =="(":
            counter_a += 1
        if letter == ")":
            counter_a -= 1
    if counter_a == 0:
        return False
    else:
        return True


# input is a box, ouptut is box with exponetials removed and the power of the exponetial if it were to base e.
# numerator is a boolean value. False will (meaning from denomiator) will casue the sign of the factor to switch
def exponetial_remover(box_v, numerator):
    letter_index = 0
    for letter in box_v:
        # for e^box
        if letter == "e" and not is_closed_in(box_v[letter_index:]):
            exponential_stop = letter_index + next_closed_bracket(box_v[letter_index:])
            exponent = box_v[letter_index+3:exponential_stop]
            exponent, factor = factor_seperator(exponent)
            # For if exponetial is at the end
            if exponential_stop == len(box_v) - 2:
                box_v = box_v[:letter_index]
            else:
                box_v = box_v[:letter_index] + box_v[exponential_stop+2:]
            # to switch sign (index laws)
            if not numerator:
                factor = -factor
            # avoid ugly brakcets
            if not contains_sum(exponent):
                exponent = brackets_remover(exponent)
            return box_v, [exponent, return_number(factor)]
        # for (integr)^box.
        # need to ensure it isn't some ln(integer) that we have found (4th "and")
        # Third "and" ensure it is a integer that is boxed in
        elif letter == ")" and not is_closed_in(box_v[letter_index+1:]) and box_v[box_v[:letter_index].rfind("(")+1:letter_index].isdigit() and not box_v[:letter_index].rfind("(") == 2 + box_v[:letter_index].rfind("ln") and 1 == box_v[letter_index:].find("^"):
            exponential_stop = letter_index + next_closed_bracket(box_v[letter_index+1:]) + 1
            base = int(box_v[box_v[:letter_index].rfind("(")+1:letter_index])
            exponent = box_v[letter_index+3:exponential_stop]
            exponent, factor = factor_seperator(exponent)
            # For if exponetial is at the end
            if exponential_stop == len(box_v) - 2:
                box_v = box_v[:box_v[:letter_index].rfind("(")]
            else:
                box_v = box_v[:box_v[:letter_index].rfind("(")] + box_v[exponential_stop+2:]
            # to switch sign (index laws)
            if not numerator:
                factor = -factor
            # avoid ugly brakcets
            if not contains_sum(exponent):
                exponent = brackets_remover(exponent)
            return box_v,[f"ln({base}){exponent}", return_number(factor)]
        letter_index += 1
    # Case of no exponetials
    return box_v, ["", 0]


# modified version of exponetial_remover for use in sums factorisation
def exponetial_remover_for_sum(box_v):
    box_v, exponential_list = exponetial_remover(box_v, True)
    exponential_term = exponential_component(exponential_list, 1)
    return box_v, exponential_term


# will return the power, and remove box^power from the product given the close index (next closed bracket). is_base_power (outpust booleab) deals with box^bax case, if so return factor as box^box.
def power_and_remover(box_v, close_index):
    factor = ""
    is_base_power = False
    if len(box_v) == close_index+1:
        return "", 1, is_base_power, factor
    # If for some reason there is a space at the end
    if len(box_v) == close_index+2 and box_v[len(box_v) - 1] == " ":
        return "", 1, is_base_power, factor
    # Test if there is a power
    elif box_v[close_index + 1] != "^":
        power = 1
        box_v = box_v[close_index + 1:]
    else:
        index_counter = 0
        # Finding the length of the power
        for letter in box_v[close_index + 2:]:
            if letter == "-" or letter == "." or letter.isdigit():
                index_counter += 1
            else:
                break
        # Dealing with a box^box case
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


# will factorise quotient. Input and Output is numerator, denominator (Variables only)
def factoriser_for_division(box_one, box_two):
    table = [[],[]]
    # Breaks box_one into it's factors along with their powers
    while len(box_one) != 0:
        # In case of " box"
        while box_one[0] == " ":
            box_one = box_one[1:]
            # To break loop if required
            if len(box_one) == 0:
                break
        # To break loop if required
        if len(box_one) == 0:
            break
        if box_one[0] == "x":
            factor = "x"
            box_one, power, is_base_power, possible_factor = power_and_remover(box_one, 0)
        else:
            factor = box_one[:next_closed_bracket(box_one)+1]
            box_one, power, is_base_power, possible_factor = power_and_remover(box_one, next_closed_bracket(box_one))
        # In case of box^box
        if is_base_power:
            factor = possible_factor
        table[0].append(factor)
        table[1].append(power)
    # adds to the table, with any duplicate factors only altering the power
    while len(box_two) != 0:
        # To deal with " box"
        while box_two[0] == " ":
            box_two = box_two[1:]
            # To break loop if required
            if len(box_two) == 0:
                break
        # To break loop if required
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
        # Becasue of index laws
        power = -power
        # To factorise
        if factor in table[0]:
            index = table[0].index(factor)
            table[1][index] += power
        else:
            table[0].append(factor)
            table[1].append(power)
    numerator = ""
    denominator = ""
    for i in range(len(table[0])):
        # since box^0 = 1
        if table[1][i] == 0:
            continue
        else:
            # Want positive indexes
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


# will factorise product. Input and Output is string (Variables only)
def factoriser_for_multiples(box_one, box_two):
    table = [[],[]]
    while len(box_one) != 0:
        # Breaks box_one into it's factors along with their powers
        while box_one[0] == " ":
            box_one = box_one[1:]
            # To Break loop if required
            if len(box_one) == 0:
                break
        # To Break loop if required
        if len(box_one) == 0:
            break
        if box_one[0] == "x":
            factor = "x"
            box_one, power, is_base_power, possible_factor = power_and_remover(box_one, 0)
        else:
            factor = box_one[:next_closed_bracket(box_one)+1]
            box_one, power, is_base_power, possible_factor = power_and_remover(box_one, next_closed_bracket(box_one))
        # To deal with box^box
        if is_base_power:
            factor = possible_factor
        table[0].append(factor)
        table[1].append(power)
    # adds to the table, with any duplicate factors only altering the power
    while len(box_two) != 0:
        while box_two[0] == " ":
            box_two = box_two[1:]
            # To Break loop if required
            if len(box_two) == 0:
                break
        # To Break loop if required
        if len(box_two) == 0:
            break
        if box_two[0] == "x":
            factor = "x"
            box_two, power, is_base_power, possible_factor = power_and_remover(box_two, 0)
        else:
            factor = box_two[:next_closed_bracket(box_two)+1]
            box_two, power, is_base_power, possible_factor = power_and_remover(box_two, next_closed_bracket(box_two))
        # To apply index laws
        if factor in table[0]:
            index = table[0].index(factor)
            table[1][index] += power
        else:
            table[0].append(factor)
            table[1].append(power)
    numerator = ""
    for i in range(len(table[0])):
        # Since box^0 = 1
        if table[1][i] == 0:
            continue
        else:
            if table[1][i] == 1:
                to_the_power = ""
            else:
                to_the_power = f"^{table[1][i]} "
            numerator += f"{table[0][i]}{to_the_power}"
    return numerator


# will find common multiples and remove from each term. Input is a list of box_c. Output is factorised list and common factor.
def factorisation_of_sums_integers(box_coefficients):
    can_factoise = True
    list = []
    # Only want to factorise integers
    for box_c in box_coefficients:
        if not isinstance(box_c, int):
            can_factoise = False
    # Some dummy initial factor
    factor = abs(box_coefficients[0])
    if can_factoise:
        for number in box_coefficients:
            for other_number in box_coefficients:
                possible_factor = math.gcd(abs(other_number),abs(number))
                # Want common factor to all
                if possible_factor < factor:
                    factor = possible_factor
        # Factoring the common factor out
        for box_c in box_coefficients:
            list.append(box_c//factor)
        return list, return_number(factor)
    else:
        return box_coefficients, 1


# will find common multiples and remove from each term. Input is a list of box_v.
def factorisation_of_sums_variables(box_variables):
    list_factors = []
    list_powers = []
    term = 0
    # Each variable will be converted into a two list: factors (multiples) and powers corresponding to each factor. Each list will be placed into a larger list containing all terms.
    for box_v in box_variables:
        list_factors.append([])
        list_powers.append([])
        while len(box_v) != 0:
            while box_v[0] == " ":
                box_v = box_v[1:]
                # To break loop if required
                if len(box_v) == 0:
                    break
            # To break loop if required
            if len(box_v) == 0:
                break
            # To deal with any exponetial terms
            box_v, factor = exponetial_remover_for_sum(box_v)
            if len(factor) != 0:
                list_factors[term].append(factor)
                list_powers[term].append(1)
                # To break loop if required
                if len(box_v) == 0:
                    break
            if box_v[0] == "x":
                factor = "x"
                box_v, power,is_base_power,possible_factor = power_and_remover(box_v, 0)
            else:
                factor = box_v[:next_closed_bracket(box_v)+1]
                box_v, power,is_base_power,possible_factor = power_and_remover(box_v, next_closed_bracket(box_v))
            # Accounts for box^box case
            if is_base_power:
                factor = possible_factor
            list_factors[term].append(factor)
            list_powers[term].append(power)
        term += 1
    # This forms a list containing factors common to all terms
    common_factors = list(reduce(set.intersection, map(set, list_factors)))
    common_factor_v = ""
    for shared in common_factors:
        # to find min. set as dummy start
        min = 10000000000000
        for i in range(len(box_variables)):
            index_of_factor = list_factors[i].index(shared)
            possible_min = list_powers[i][index_of_factor]
            if possible_min < min:
                min = possible_min
        # Only want to factorise postive indices
        if min <= 0:
            pass
        else:
            for i in range(len(box_variables)):
                index_of_factor = list_factors[i].index(shared)
                # index laws to factorise out power
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
            # since box^0 = 1
            if list_powers[i][k] == 0:
                indi = ""
                list_factors[i][k] = ""
            # since we don't want box^1, just box if power = 1
            elif list_powers[i][k] == 1:
                indi = ""
            else:
                indi = f"^{list_powers[i][k]} "
            term += f"{list_factors[i][k]}{indi}"
        return_box_variables.append(term)
    return return_box_variables, common_factor_v


# will convert a list of boxes in the form [box_v, box_c] into a list of box_v and a list of box_c
def converter(boxes):
    box_variables = []
    box_coefficients = []
    for i in range(len(boxes)):
        box_variables.append(boxes[i][0])
        box_coefficients.append(boxes[i][1])
    return box_variables, box_coefficients


# will convert some -(g(x)+f(x)) into g(x) - f(x) along with a boolean value to indicate if the box was changed. e.g. if box is x, output is x and False
def negative_expander(box_v):
    box_v = brackets_remover(box_v)
    index = 0
    changed = False
    # for +/- on the indside, the switch sign
    for letter in box_v:
        if letter == "-" and not is_closed_in(box_v[index:]):
            box_v= box_v[:index] + "+" + box_v[index+1:]
            changed = True
        if letter == "+" and not is_closed_in(box_v[index:]):
            box_v = box_v[:index] + "-" + box_v[index+1:]
            changed = True
        index += 1
    return box_v, changed


# Input is a list of box_v, a list of box_c along with a common factor for variable (common_factor_v) and integer (factor). Output is the sum of these terms.
def add(box_variables, box_coefficients, common_factor_v, factor):
    signs = []
    signs.append("dummy")
    if box_coefficients[0] < 0:
        changed = False
        if box_coefficients[0] == -1:
                if not box_variables[0] == "":
                    box_coefficients[0] = ""
                box_variables[0] = brackets_remover(box_variables[0])
        # To ensure the first term is positive (will make it look nicer)
        have_to_change_signs = True
        factor = -factor
    else:
        if box_coefficients[0] == 1 and not box_variables[0] == "":
                box_coefficients[0] = ""
                box_variables[0] = brackets_remover(box_variables[0])
        have_to_change_signs = False
    try:
        # To avoid double signs
        box_coefficients[0] = abs(box_coefficients[0])
    except:
        # if box_c = "" or "-"
        pass
    for i in range(1,len(box_variables)):
        have_to_change_signs_individual = have_to_change_signs
        if box_coefficients[i] < 0:
            if box_coefficients[i] == -1 and not box_variables[i] == "":
                box_coefficients[i] = ""
                # To remove brackets whist accounting for signs inside
                box_variables[i], changed = negative_expander(box_variables[i])
                if changed:
                    have_to_change_signs_individual = not have_to_change_signs_individual
            if have_to_change_signs_individual:
                signs.append(" + ")
            else:
                signs.append(" - ")
        else:
            if have_to_change_signs_individual:
                signs.append(" - ")
            else:
                signs.append(" + ")
            if box_coefficients[i] == 1 and not box_variables[i] == "":
                box_coefficients[i] = ""
                box_variables[i] = brackets_remover(box_variables[i])
        try:
            # To avoid double signs
            box_coefficients[i] = abs(box_coefficients[i])
        except:
            # if box_c = "" or "-"
            pass
    # To avoid 0 + f(x)
    if box_coefficients[0] == 0:
        do_not_put_sign_in_yet = True
    else:
        sum = f"{box_coefficients[0]}{box_variables[0]}"
        do_not_put_sign_in_yet = False
    # Adding terms
    for k in range(1, len(box_variables)):
        if box_coefficients[k] !=0:
            if do_not_put_sign_in_yet:
                # To avoid 0 + f(x)
                sum += f"{box_coefficients[k]}{box_variables[k]}"
                do_not_put_sign_in_yet = False
            else:
                sum += f"{signs[k]}{box_coefficients[k]}{box_variables[k]}"
                do_not_put_sign_in_yet = False
    try:
        # To avoid some (2 + 1) that should be 3
        factor = factor*eval(sum)
        if factor == 0:
            sum = ""
        sum = common_factor_v
    except:
        sum = f"{common_factor_v}({sum})"
    return sum, return_number(factor)


# Input is two boxs. Output is the e raised to the  sum of the two boxes (string). do_we_want_to_return_base_power is a boolean; if true will convert some e^(ln(a)^n f(x)) into (a)^(ln(a)^(n-1) f(x))
def add_for_index(box_one, box_two, do_we_want_to_return_base_power):
    # case of e^0 = 1
    if box_one[0] == "" and box_one[1] == 0 and box_two[0] == "" and box_two[1] == 0:
        return ""
    # cases where one part of the sum are zero
    elif box_one[0] == "" and box_one[1] == 0:
        exponent, factor = box_two[0], box_two[1]
    elif box_two[0] == "" and box_two[1] == 0:
        exponent, factor = box_one[0], box_one[1]
    else:
        # adding the two boxs together
        numerator_one, denominator_one = quotients.splitter(box_one[0])
        numerator_two, denominator_two = quotients.splitter(box_two[0])
        variables, common_factor_v = factorisation_of_sums_variables([numerator_one,numerator_two])
        coefficients, factor = factorisation_of_sums_integers([box_one[1], box_two[1]])
        numerator, factor = add(variables, coefficients, common_factor_v, factor)
        denominator = multiply_two_together(denominator_one,denominator_two, False)
        numerator,denominator = quotients.divide(numerator,denominator, False)
        exponent = quotients.assembler(numerator,denominator)
    # Since e^0 = 1
    if factor == 0:
        return ""
    # To avoid 1box or -1box
    if factor == 1:
            factor = ""
    if factor == -1:
        factor = "-"
    # if we want e^box returned
    if not do_we_want_to_return_base_power:
        return f"e^({factor}{exponent}) "
    # if we want (a)^box retunred
    else:
        i = 0
        for letter in exponent:
            if letter == "l" and exponent[i:].find("(") == 2 and not is_closed_in(exponent[i:]):
                ncb = i + next_closed_bracket(exponent[i:])
                try:
                    integer_base = return_number(exponent[i + 3:ncb])
                except:
                    pass
                # if ln(a) is at the end and has power 1
                if ncb == len(exponent) - 1:
                    exponent = exponent[:i]
                    return f"({integer_base})^({factor}{exponent}) "
                # if power is 1 (of ln(a))
                elif ncb != i + exponent[i:].find(")^"):
                    exponent = exponent[:i] + exponent[ncb+1:]
                # If deaking with ln(a)^n
                else:
                    try:
                        # If power is a number
                        power = return_number(exponent[ncb+2:i+exponent[i:].find(" ")])
                        length_power = len(str(power))
                        new_power = return_number(power-1)
                    except:
                        power = exponent[ncb+2:i+exponent[i:].find(" ")]
                        length_power = len(str(power))
                        new_power = f"({power} - 1)"
                    if new_power == 1:
                        index = ""
                    else:
                        index = f"^{new_power} "
                    exponent = exponent[:i] + f"{exponent[i:ncb+1]}{index}" + exponent[ncb+3+length_power:]
                return f"({integer_base})^({factor}{exponent}) "
            i += 1
    # If there is no ln(a) in the exponent then e must be the base
    return f"e^({factor}{exponent}) "


# Input is two boxs in the form [box_v, box_c]. Output is them multiplied together (string) .do_we_want_to_return_base_power is a boolean value; if true, if will keep the base of any exponetial
def multiply_two_together(box_v_one, box_v_two, do_we_want_to_return_base_power):
    sorted_box_v_one, exponential_list_one = exponetial_remover(box_v_one, True)
    sorted_box_v_two, exponential_list_two = exponetial_remover(box_v_two, True)
    numerator = factoriser_for_multiples(sorted_box_v_one,sorted_box_v_two)
    exponential_component = add_for_index(exponential_list_one,exponential_list_two, do_we_want_to_return_base_power)
    numerator += exponential_component
    return numerator


# Input is a list of boxs in the form [box_v, box_c]. Output is their sum
def a_sum(boxes):
    box_variables, box_coefficients = converter(boxes)
    box_variables, common_factor_v = factorisation_of_sums_variables(box_variables)
    box_coefficients, factor = factorisation_of_sums_integers(box_coefficients)
    sum, factor = add(box_variables, box_coefficients, common_factor_v, factor)
    return sum, factor
