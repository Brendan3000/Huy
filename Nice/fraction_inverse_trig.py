# add only one
# inverse sin [has function_determiner value = 6]
def arcsin(box_code, box_dash):
    power, coefficient, box_v, box_c = box_code[1],box_code[2], box_code[5][0], box_code[5][1]
    box_dash_v, box_dash_c = box_dash[0], box_dash[1]
    constant_product = coefficient*power*box_dash_c
    # if our constant is 1 we don't want 1box we just want box
    if box_c == 1:
        box_c = ""
    else:
        index = ""
    # if our power is 1 we don't want box^1 we just want  box
    if power != 2:
        index = f"^{power-1}"
    if power == 1:
        return [[f"{box_dash_v}",f"(1 + ({box_c}{box_v})^2)^1/2"], constant_product]
    else:
        return [[f"{box_dash_v}arccos({box_c}{box_v}){index}"], [f"(1 + ({box_c}{box_v})^2)^1/2"], constant_product]


# inverse cosine [has function_determiner value = 7]
def arccos(box_code, box_dash):
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
        return [[f"{box_dash_v}",f"(1 + ({box_c}{box_v})^2)^1/2"], -constant_product]
    else:
        return [[f"{box_dash_v}arccos({box_c}{box_v}){index}"], [f"(1 + ({box_c}{box_v})^2)^1/2"], -constant_product]


# inverse tangent [has function_determiner value = 8]
def arcctan(box_code, box_dash):
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
        return [[f"{box_dash_v}",f"1 + ({box_c}{box_v})^2"], constant_product]
    else:
        return [[f"{box_dash_v}arctan({box_c}{box_v}){index}"], [f"(1 + ({box_c}{box_v})^2)"], constant_product]
