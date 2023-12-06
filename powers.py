import quotients
import products
from Nice import Brackets

# used to convert a list containing exponent and coefficient into e^(coefficient(exponent))
def exponential_component(list, power):
    exponent,coefficient = list[0], list[1]
    coefficient *= power
    if coefficient == 1:
        coefficient = ""
        exponent = Brackets.brackets_remover(exponent)
    if coefficient == -1:
        coefficient = "-"
    return f"e^({coefficient}{exponent}) "


# converts some f(x)^(ag(x)), power into f(x)^(power*ag(x))
def special_assembler(box_v, power):
    for index in range(len(box_v)):
        if box_v[index] == "^" and not products.is_closed_in(box_v[index+1:]):
            break
    bottom = box_v[:index]
    top = box_v[index+2:len(box_v)-1]
    index_counter = 0
    for letter in top:
        if letter == "-" or letter == "." or letter.isdigit():
            index_counter += 1
        else:
            break
    constant = products.return_number(top[:index_counter])
    top = top[index_counter:]
    power = constant*power
    if power == 1:
        power = ""
    if power == -1:
        power = "-"
    return f"{bottom}^({power}{top})"


# used to distribute power across. e.g. (cos(x)sin(x))^power = coss(x)^power sin(x)^power
def power_distributor(box_v, power):
    if len(box_v) == 0:
        return box_v
    if power == 1:
        return box_v
    box_v, exponential_list = products.exponetial_remover(box_v, True)
    exponential = exponential_component(exponential_list,power)
    factors = []
    powers = []
    special = []
    while len(box_one) != 0:
        factor = "null"
        if box_one[0]  == " ":
            box_one = box_one[1:]
        if box_one[0] == "x":
            factor = "x"
            box_one, power, is_base_power, possible_factor = products.power_and_remover(box_one, 0)
            if is_base_power:
                factor = possible_factor
                are_we_dealing_with_special_case = True
        else:
            factor = box_one[:products.next_closed_bracket(box_one)+1]
            box_one, power, is_base_power, possible_factor= products.power_and_remover(box_one, products.next_closed_bracket(box_one))
            if is_base_power:
                factor = possible_factor
                are_we_dealing_with_special_case = True
        factors.append(factor)
        powers.append(power)
        if are_we_dealing_with_special_case:
            special.append(True)
        else:
            special.append(False)
    for i in range(len(powers)):
        if special[i]:
            if power == 0:
                power[i] *= power
            else:
                factors[i] = special(factors[i],power)
        else:
            power[i] *= power
    for k in  range(len(factors)):
        if powers[k] == 0:
            pass
        elif powers[k] == 1:
            index = ""
        else:
            index = f"^{powers[k]} "
        box_v += f"{factor[k]}{index}"
    box_v += exponential
    return box_v


