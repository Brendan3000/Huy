from Nice import Brackets


# code commmon to the inverse sin, cos and tan function
def inverse_sin_cos_tan(box_code, box_dash):
    power, coefficient, box_v, box_c = box_code[1],box_code[2], box_code[5][0], box_code[5][1]
    box_v_copy, box_c_copy = box_v, box_c
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
    # This acts to enhance the presentation of the (box)^2 term
    if need_to_tidy_up:
        # adjustment for some case (a*box)^2 just to tidy up into a^2(box)^2 where a is a constant (calculated)
        if box_c != "":
            a = Brackets.coefficient_power_direct(box_c, 2, 1)
            box_c = a[0]
        # adjustment for some case ((box)^n)^2 just to tidy up
        if Brackets.closed(box_v):
            box_v, adjustment = Brackets.power_converter(box_v)
            box_v = f"{box_v}^{adjustment*2})"
        else:
            box_v = "(" + box_v + ")"
        # for simplifying some (e^box)^2 into e^2box
        if Brackets.dealing_with_exponentials(box_v):
            box_v = Brackets.exponentials_simplifier(box_v, 2)
        squared_term = f"{box_c}{box_v}"
    else:
        squared_term = f"({box_c}{box_v}{shift})^2"
    return constant_product, box_v_copy, box_c_copy, shift, index,box_dash_v, power, squared_term


# add only one
# inverse sin [has function_determiner value = 6]
def arcsin(box_code, box_dash):
    constant_product, box_v, box_c, shift, index,box_dash_v, power, squared_term = inverse_sin_cos_tan(box_code, box_dash)
    if power == 1:
        return [[f"{box_dash_v}",f"(1 + {squared_term})^1/2"], constant_product]
    else:
        return [[f"{box_dash_v}arcsin({box_c}{box_v}{shift}){index}"], [f"(1 + {squared_term})^1/2"], constant_product]


# inverse cosine [has function_determiner value = 7]
def arccos(box_code, box_dash):
    constant_product, box_v, box_c, shift, index,box_dash_v, power, squared_term = inverse_sin_cos_tan(box_code, box_dash)
    if power == 1:
        return [[f"{box_dash_v}",f"(1 + {squared_term})^1/2"], -constant_product]
    else:
        return [[f"{box_dash_v}arccos({box_c}{box_v}{shift}){index}"], [f"(1 + ({box_c}{box_v}{shift})^2)^1/2"], -constant_product]


# inverse tangent [has function_determiner value = 8]
def arcctan(box_code, box_dash):
    constant_product, box_v, box_c, shift, index,box_dash_v, power, squared_term = inverse_sin_cos_tan(box_code, box_dash)
    if power == 1:
        return [[f"{box_dash_v}",f"1 + {squared_term}"], constant_product]
    else:
        return [[f"{box_dash_v}arctan({box_c}{box_v}{shift}){index}"], [f"1 + {squared_term}"], constant_product]
