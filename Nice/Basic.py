from Nice import Brackets


# power rule
def power(box_code, box_dash):
    shift, power, coefficient, base, function_determiner, box_v, box_c = box_code[0][1], box_code[1],box_code[2], box_code[3], box_code[4], box_code[5][0], box_code[5][1]
    box_dash_v = box_dash[0]
    box_dash_c = box_dash[1]
    constant_product = coefficient*power*box_dash_c
    # adjustment for some case ((box)^n)^m just to tidy up
    # still need to fix
    if power != 1:
        box_v = Brackets.index_laws(box_v)[0]
        Brackets.index_laws(box_v)[1] *= power
    # adjustment for some case (a*box)^n just to tidy up int0 a^n(box)^n where a is a constant(calculated)
    a = Brackets.coefficient_power_direct(box_v, box_c, box_dash_c, power, coefficient)
    box_v, box_c, box_dash_c, power, coefficient = a[0], a[1], a[2], a[3], a[4]

    if power == 1:
        return [box_dash_v, constant_product]
    if power == 2:
        return [f"{box_dash_v}{box_v}", constant_product]
    else:
        return [f"{box_dash_v}{box_v}^{power-1}", constant_product]


# sin
def sin(box_code, box_dash):
    power, coefficient, box_v, box_c = box_code[1],box_code[2], box_code[5][0], box_code[5][1]
    box_dash_v = box_dash[0]
    box_dash_c = box_dash[1]
    if power == 1:
        return [f"{box_dash_v}cos({box_c}{box_v})", coefficient*power**box_dash_c]
    if power ==2:
        return [f"{box_dash_v}sin(2{box_c}{box_v})", coefficient*power**box_dash_c*0.5]
    elif power > 0 and isinstance(power,int):
        return [f"{box_dash_v}cos({box_c}{box_v})sin^{power-1}({box_c}{box_v})", coefficient*power*box_dash_c]
    else:
        return [f"{box_dash_v}cos({box_c}{box_v})sin({box_c}{box_v})^{power-1}", coefficient*power*box_dash_c]


# cos
def cos(box_code, box_dash):
    power, coefficient, box_v, box_c = box_code[1],box_code[2], box_code[5][0], box_code[5][1]
    box_dash_v = box_dash[0]
    box_dash_c = box_dash[1]
    if power == 1:
        return [f"{box_dash_v}cos({box_c}{box_v})", -coefficient*power*box_dash_c]
    if power ==2:
        return [f"{box_dash_v}sin(2{box_c}{box_v})", -coefficient*power*box_dash_c*0.5]
    elif power > 0 and isinstance(power,int):
        return [f"{box_dash_v}sin({box_c}{box_v})cos^{power-1}({box_c}{box_v})", -coefficient*power*box_dash_c]
    else:
        return [f"{box_dash_v}sin({box_c}{box_v})cos({box_c}{box_v})^{power-1}", -coefficient*power*box_dash_c]


# tan
def tan(box_code, box_dash):
    power, coefficient, box_v, box_c = box_code[1],box_code[2], box_code[5][0], box_code[5][1]
    box_dash_v = box_dash[0]
    box_dash_c = box_dash[1]
    if power == 1:
        return [f"{box_dash_v}sec^2({box_c}{box_v})", -coefficient*power*box_dash_c]
    if power ==2:
        return [f"{box_dash_v}sec^2({box_c}{box_v})tan({box_c}{box_v})", coefficient*power*box_dash_c]
    elif power > 0:
        return [f"{box_dash_v}sec^2({box_c}{box_v})tan^{power-1}({box_c}{box_v})", -coefficient*power*box_dash_c]
    else:
        return [f"{box_dash_v}sec^2({box_c}{box_v})tan({box_c}{box_v})^{power-1}", -coefficient*power*box_dash_c]
