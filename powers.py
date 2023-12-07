import products
from Nice import Brackets

# used to convert a list containing exponent and coefficient into e^(coefficient(exponent))
def exponential_component(list, power):
    exponent,coefficient = list[0], list[1]
    if exponent == "":
        return ""
    else:
        try:
            coefficient *= power
            if coefficient == 1:
                coefficient = ""
                exponent = Brackets.brackets_remover(exponent)
            if coefficient == -1:
                coefficient = "-"
            return f"e^({coefficient}{exponent}) "
        except:
            return f"e^({coefficient}{power}{exponent}) "


# converts some f(x)^(ag(x)), power into f(x)^(power*ag(x))
def special_assembler(box_v, power):
    for index in range(len(box_v)):
        if box_v[index] == "^" and not products.is_closed_in(box_v[index:]):
            break
    bottom = box_v[:index]
    top = box_v[index+2:len(box_v)-2]
    index_counter = 0
    for letter in top:
        if letter == "-" or letter == "." or letter.isdigit():
            index_counter += 1
        else:
            break
    if index_counter == 0:
        constant = 1
    else:
        constant = products.return_number(top[:index_counter])
    top = top[index_counter:]
    try:
        power *= constant
    except:
        power = constant + power
    if power == 1:
        power = ""
    if power == -1:
        power = "-"
    return f"{bottom}^({power}{top})"


# used to distribute power across. e.g. (cos(x)sin(x))^power = coss(x)^power sin(x)^power
def power_distributor(box_v, change_power_factor):
    if len(box_v) == 0:
        return box_v
    if change_power_factor == 1:
        return box_v
    box_v, exponential_list = products.exponetial_remover(box_v, True)
    exponential = exponential_component(exponential_list,change_power_factor)
    factors = []
    powers = []
    special = []
    while len(box_v) != 0:
        while box_v[0] == " ":
            box_v = box_v[1:]
            if len(box_v) == 0:
                break
        if len(box_v) == 0:
            break
        if box_v[0] == "x":
            factor = "x"
            box_v, power, is_base_power, possible_factor = products.power_and_remover(box_v, 0)
        else:
            factor = box_v[:products.next_closed_bracket(box_v)+1]
            box_v, power, is_base_power, possible_factor= products.power_and_remover(box_v, products.next_closed_bracket(box_v))
        if is_base_power:
            factor = possible_factor
            special.append(True)
        else:
            special.append(False)
        factors.append(factor)
        powers.append(power)
    for i in range(len(powers)):
        if special[i]:
            if change_power_factor == 0:
                try:
                    powers[i] *= change_power_factor
                except:
                    powers[i] = powers[i] + change_power_factor
            else:
                factors[i] = special_assembler(factors[i], change_power_factor)
        else:
            try:
                powers[i] *= change_power_factor
            except:
                powers[i] = powers[i] + change_power_factor
    for k in range(len(factors)):
        if powers[k] == 0:
            pass
        else:
            if powers[k] == 1:
                index = ""
            else:
                index = f"^{powers[k]} "
            box_v += f"{factors[k]}{index}"
    box_v += exponential
    return box_v


