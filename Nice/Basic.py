from Nice import Brackets


# box to a power (straight power rule) [has function_determiner value = 0]
# I realised too late that it was not in fact "basic" so I guess it doesn't belong here
def power(box_code, box_dash):
    shift, power, coefficient, base, function_determiner, box_v, box_c = box_code[0][1], box_code[1],box_code[2], box_code[3], box_code[4], box_code[5][0], box_code[5][1]
    box_dash_v, box_dash_c = box_dash[0], box_dash[1]
    constant_product = coefficient*power*box_dash_c
    # if our constant is 1 we don't want 1box we just want box
    if box_c == 1:
        box_c = ""
    # if our power is 1 we don't want box^1 we just want  box
    if power != 2:
        index = f"^{power-1}"
    else:
        index = ""
    # adjustment for some case ((box)^n)^m just to tidy up
    # still need to fix!!!! so just ignore for now
    if power != 1:
        box_v = Brackets.index_laws(box_v)[0]
        Brackets.index_laws(box_v)[1] *= power
    # adjustment for some case (a*box)^n just to tidy up int0 a^n(box)^n where a is a constant(calculated)
    a = Brackets.coefficient_power_direct(box_v, box_c, box_dash_c, power, coefficient)
    box_v, box_c, box_dash_c, power, coefficient = a[0], a[1], a[2], a[3], a[4]
    if power == 1:
        return [box_dash_v,
                constant_product]
    else:
        return [f"{box_dash_v}{box_v}{index}",
                constant_product]


# sin [has function_determiner value = 1]
def sin(box_code, box_dash):
    power, coefficient, box_v, box_c = box_code[1],box_code[2], box_code[5][0], box_code[5][1]
    box_dash_v, box_dash_c = box_dash[0], box_dash[1]
    constant_product = coefficient*power*box_dash_c
    # if our constant is 1 we don't want 1box we just want box
    if box_c == 1:
        box_c = ""
    # if our power is 1 we don't want box^1 we just want  box
    if power != 2:
        index = f"^{power-1}"
    else:
        index = ""
    if power == 1:
        return [f"{box_dash_v}cos({box_c}{box_v})",
                constant_product]
    if power == 2:
        return [f"{box_dash_v}sin(2{box_c}{box_v})",
                constant_product*0.5]
    elif power > 0 and isinstance(power,int):
        return [f"{box_dash_v}cos({box_c}{box_v})sin{index}({box_c}{box_v})",
                constant_product]
    else:
        return [f"{box_dash_v}cos({box_c}{box_v})sin({box_c}{box_v}){index}",
                constant_product]


# cos [has function_determiner value = 2]
def cos(box_code, box_dash):
    power, coefficient, box_v, box_c = box_code[1],box_code[2], box_code[5][0], box_code[5][1]
    box_dash_v, box_dash_c = box_dash[0], box_dash[1]
    constant_product = coefficient*power*box_dash_c
    # if our constant is 1 we don't want 1box we just want box
    if box_c == 1:
        box_c = ""
    # if our power is 1 we don't want box^1 we just want  box
    if power != 2:
        index = f"^{power-1}"
    else:
        index = ""
    if power == 1:
        return [f"{box_dash_v}cos({box_c}{box_v})",
                -constant_product]
    if power ==2:
        return [f"{box_dash_v}sin(2{box_c}{box_v})",
                -constant_product*0.5]
    elif power > 0 and isinstance(power,int):
        return [f"{box_dash_v}sin({box_c}{box_v})cos{index}({box_c}{box_v})",
                -constant_product]
    else:
        return [f"{box_dash_v}sin({box_c}{box_v})cos({box_c}{box_v}){index}",
                -constant_product]


# tan [has function_determiner value = 3]
def tan(box_code, box_dash):
    power, coefficient, box_v, box_c = box_code[1],box_code[2], box_code[5][0], box_code[5][1]
    box_dash_v, box_dash_c = box_dash[0], box_dash[1]
    constant_product = coefficient*power*box_dash_c
    # if our constant is 1 we don't want 1box we just want box
    if box_c == 1:
        box_c = ""
    # if our power is 1 we don't want box^1 we just want  box
    if power != 2:
        index = f"^{power-1}"
    else:
        index = ""
    if power == 1:
        return [f"{box_dash_v}sec^2({box_c}{box_v})",
                constant_product]
    elif power > 0:
        return [f"{box_dash_v}sec^2({box_c}{box_v})tan{index}({box_c}{box_v})",
                constant_product]
    else:
        return [f"{box_dash_v}sec^2({box_c}{box_v})tan({box_c}{box_v}){index}",
                constant_product]
