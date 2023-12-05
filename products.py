from Nice import Brackets

def return_number(string):
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


# input is a box, ouptut is box with exponetials removed and the power of the exponetial if it were to base e
def exponetial_remover(box_v):
    letter_index = 0
    for letter in box_v:
        if letter == "e" and not is_closed_in(box_v[letter_index:]):
            exponent = box_v[letter_index+3:box_v.rfind(")")]
            exponent, factor = factor_seperator(exponent)
            box_v = box_v[:letter_index]
            return box_v, [exponent, factor]
        elif letter == ")" and not is_closed_in(box_v[letter_index+1:]) and box_v[box_v[:letter_index].rfind("(")+1:letter_index].isdigit():
            base = box_v[box_v[:letter_index].rfind("(")+1:letter_index]
            exponent = box_v[letter_index+3:box_v.rfind(")")]
            exponent, factor = factor_seperator(exponent)
            box_v = box_v[:box_v[:letter_index].rfind("(")]
            if Brackets.closed(exponent) or Brackets.dealing_with_exponentials(exponent):
                pass
            else:
                exponent = "(" + exponent + ")"
            return box_v,[f"ln({base}){exponent}", factor]
        letter_index += 1
    return box_v, ["", 1]


# will return the power, revoved closed term from index of closed bracket
def power_and_remover(box_v, close_index):
    if len(box_v) == close_index+1:
        return "", 1
    if box_v[close_index + 1] != "^":
        power = 1
        box_v = box_v[close_index + 1:]
    else:
        index_counter = 0
        for letter in  box_v[close_index + 2:]:
            if letter == "-" or letter == "." or letter.isdigit():
                index_counter += 1
            else:
                break
        power = return_number(box_v[close_index + 2:close_index + 3 + index_counter])
        box_v = box_v[close_index + 3 + index_counter:]
    return box_v, power


# will factorise multiples, if product is true, it will deal with it as a product, else quotient (box_one is numerator)
def factoriser(box_one, box_two, product):
    table = [[],[]]
    while len(box_one) != 0:
        factor = "null"
        if box_one[0]  == " ":
            box_one = box_one[1:]
        if box_one[0] == "x":
            factor = "x"
            box_one, power = power_and_remover(box_one, 0)
        else:
            factor = box_one[:next_closed_bracket(box_one)+1]
            box_one, power = power_and_remover(box_one, next_closed_bracket(box_one))
        table[0].append(factor)
        table[1].append(power)
    while len(box_two) != 0:
        factor = "null"
        if box_two[0]  == " ":
            box_two = box_two[1:]
        if box_two[0] == "x":
            factor = "x"
            box_two, power = power_and_remover(box_two, 0)
        else:
            factor = box_two[:next_closed_bracket(box_two)+1]
            box_two, power = power_and_remover(box_two, next_closed_bracket(box_two))
        if not product:
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


# will find common multiples and remove from each term
def factorisation_of_sums_integers(box_coefficients):
    number_of_terms = len(box_coefficients)
    can_factoise = True
    for box_c in box_coefficients:
        if not box_c.isdigit():
            can_factoise = False
    if can_factoise:




# will find common multiples and remove from each term
def factorisation_of_sums_variables():

