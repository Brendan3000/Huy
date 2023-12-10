import products
from Nice import Brackets


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


# converts some f(x)^(ag(x)), power into f(x)^((power*a)g(x))
def special_assembler(box_v, power):
    # since box^0 = 1
    if power == 0:
        return ""
    for index in range(len(box_v)):
        if box_v[index] == "^" and not products.is_closed_in(box_v[index:]):
            break
    # index is the position os ^ that seperates box_base (bottom) for box_power (top)
    bottom = box_v[:index]
    top = box_v[index+2:box_v.rfind(")")]
    index_counter = 0
    for letter in top:
        if letter == "-" or letter == "." or letter.isdigit():
            index_counter += 1
        else:
            break
    # index_counter denotes the length of the factor a in af(x)
    if index_counter == 0:
        constant = 1
    else:
        constant = products.return_number(top[:index_counter])
    # To make top just a variable
    top = top[index_counter:]
    try:
        # if power is a number
        power = products.return_number(power)
        constant *= power
    except:
        # if power is a box_c
        top = products.multiply_two_together(power, top, False)
    if constant == 1:
        constant = ""
    if constant == -1:
        constant = "-"
    return f"{bottom}^({constant}{top})"


# used to distribute power across. e.g. (cos(x)sin(x))^power = cos(x)^power sin(x)^power
def power_distributor(box_v, change_power_factor):
    # since 1^n = 1
    if len(box_v) == 0:
        return box_v
    # since box^1 = box
    if change_power_factor == 1:
        return box_v
    # since box^0 = 1
    if change_power_factor == 0:
        return ""
    box_v, exponential_list = products.exponetial_remover(box_v, True)
    exponential = exponential_component(exponential_list,change_power_factor)
    factors = []
    powers = []
    special = []
    # To break the box into it's factors (multples) and eahc of their respective powers. special list donotes if we have a box^box case
    while len(box_v) != 0:
        while box_v[0] == " ":
            box_v = box_v[1:]
            # to break loop if required
            if len(box_v) == 0:
                break
        # to break loop if required
        if len(box_v) == 0:
            break
        if box_v[0] == "x":
            factor = "x"
            box_v, power, is_base_power, possible_factor = products.power_and_remover(box_v, 0)
        else:
            factor = box_v[:products.next_closed_bracket(box_v)+1]
            box_v, power, is_base_power, possible_factor = products.power_and_remover(box_v, products.next_closed_bracket(box_v))
        # To deal with box^box case
        if is_base_power:
            factor = possible_factor
            special.append(True)
        else:
            special.append(False)
        factors.append(factor)
        powers.append(power)
    for i in range(len(powers)):
        # For box^box case
        if special[i]:
            factors[i] = special_assembler(factors[i], change_power_factor)
        else:
            try:
                # if change_power_factor is a number
                change_power_factor = products.return_number(change_power_factor)
                powers[i] *= change_power_factor
            except:
                # if change_power_factor is a variable
                if powers[i] == 1:
                    powers[i] = ""
                if powers[i] == -1:
                    powers[i] = "-"
                powers[i] = f"({powers[i]}{change_power_factor})"
    for k in range(len(factors)):
        # since box^0 = 1
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


