from Nice import Brackets, Exponentials


# box to a power (straight power rule) [has function_determiner value = 0]
# I realised too late that it was not in fact "basic" so I guess it doesn't belong here :)
def power(box_code, box_dash):
    power, coefficient, base, function_determiner, box_v, box_c = box_code[1],box_code[2], box_code[3], box_code[4], box_code[5][0], box_code[5][1]
    box_dash_v, box_dash_c = box_dash[0], box_dash[1]
    constant_product = coefficient*power*box_dash_c
    shift, need_to_tidy_up = Brackets.shift_assembler(box_code[0][0], box_code[0][1])
    # if our power is 1 we don't want box^1 we just want box
    if power != 2:
        index = f"^{power-1}"
    else:
        index = ""
    # if our constant is 1 we don't want 1box we just want box
    if box_c == 1:
        box_c = ""
    # where there is no shift, presentation must be enhanced
    if need_to_tidy_up:
        # adjustment for some case (a*box)^n just to tidy up into a^n(box)^n where a is a constant (calculated)
        if box_c != "":
            a = Brackets.coefficient_power_direct(box_c,power, constant_product)
            box_c, constant_product = a[0], a[1]
        # for simplifying some (e^box)^3 into e^3box
        if Brackets.dealing_with_exponentials(box_v):
            box_v = Brackets.exponentials_simplifier(box_v, power)
            if box_c == "-":
                imaginary = f"(-1)^{power}"
            else:
                imaginary = ""
            return [[f"{imaginary}{box_dash_v}{box_v}",""],
                constant_product]
        # adjustment for some case ((box)^n)^m just to tidy up
        if Brackets.closed(box_v):
            box_v, adjustment = Brackets.power_converter(box_v)
            power *= adjustment
            if adjustment != 1:
                # To adjust index
                if power != 2:
                    index = f"^{power-1}"
                else:
                    index = ""
                # To adjust box_dash
                if adjustment != 2:
                    # removes f"{box_v}^{adjustment-1}") form box_dash_v
                    box_dash_v = box_dash_v[ :box_dash_v.find(f"{box_v}^{adjustment-1}")]
                if adjustment == 2:
                    # removes f"{box_v}" form box_dash_v
                    box_dash_v = box_dash_v[ :box_dash_v.find(f"{box_v}")]
    # This serves to add brackets only when required
    if not need_to_tidy_up or not Brackets.closed(box_v):
        box_c = "(" + str(box_c)
        shift += ")"
    if power == 1:
        return [[f"{box_dash_v}",""],
                constant_product]
    else:
        return [[f"{box_dash_v}{box_c}{box_v}{shift}{index}", ""],
                constant_product]


# code commmon to the sin, cos and tan function
def sin_cos_tan(box_code, box_dash):
    power, coefficient, box_v, box_c = box_code[1],box_code[2], box_code[5][0], box_code[5][1]
    box_dash_v, box_dash_c = box_dash[0], box_dash[1]
    constant_product = coefficient*power*box_dash_c
    shift, need_to_tidy_up = Brackets.shift_assembler(box_code[0][0], box_code[0][1])
    # if our constant is 1 we don't want 1box we just want box
    if box_c == 1:
        box_c = ""
    # if our power is 1 we don't want box^1 we just want  box
    if power != 2:
        index = f"^{power-1}"
    else:
        index = ""
    # This serves to avoid the possibility of some sin((f(x))) (i.e. avoid double brackets when not required)
    if need_to_tidy_up and box_c == "":
        Brackets.brackets_remover(box_v)
    return constant_product, box_v, box_c, shift, index, box_dash_v, power


# sin [has function_determiner value = 1]
def sin(box_code, box_dash):
    constant_product, box_v, box_c, shift, index,box_dash_v,power = sin_cos_tan(box_code, box_dash)
    if power == 1:
        return [[f"{box_dash_v}cos({box_c}{box_v}{shift})",""],
                constant_product]
    if power == 2:
        return [[f"{box_dash_v}sin(2{box_c}{box_v}{shift})",""],
                constant_product*0.5]
    else:
        return [[f"{box_dash_v}cos({box_c}{box_v}{shift})sin({box_c}{box_v}{shift}){index}",""],
                constant_product]


# cos [has function_determiner value = 2]
def cos(box_code, box_dash):
    constant_product, box_v, box_c, shift, index, box_dash_v, power = sin_cos_tan(box_code, box_dash)
    if power == 1:
        return [[f"{box_dash_v}cos({box_c}{box_v}{shift})",""],
                -constant_product]
    if power ==2:
        return [[f"{box_dash_v}sin(2{box_c}{box_v}{shift})",""],
                -constant_product*0.5]
    else:
        return [[f"{box_dash_v}sin({box_c}{box_v}{shift})cos({box_c}{box_v}{shift}){index}",""],
                -constant_product]


# tan [has function_determiner value = 3]
def tan(box_code, box_dash):
    constant_product, box_v, box_c, shift, index, box_dash_v, power= sin_cos_tan(box_code, box_dash)
    if power == 1:
        return [[f"{box_dash_v}sec({box_c}{box_v}{shift})^2",""],
                constant_product]
    else:
        return [[f"{box_dash_v}sec({box_c}{box_v}{shift})^2 tan({box_c}{box_v}{shift}){index}",""],
                constant_product]

