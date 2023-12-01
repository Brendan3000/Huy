# add only one
# inverse sin
def arcsin(box_code, box_dash):
    power, coefficient, box_v, box_c = box_code[1],box_code[2], box_code[5][0], box_code[5][1]
    box_dash_v = box_dash[0]
    box_dash_c = box_dash[1]
    if power == 1:
        return [[f"{box_dash_v}",f"(1 + ({box_c}{box_v})^2)^1/2"], coefficient*power*box_dash_c]
    else:
        return [[f"{box_dash_v}arccos({box_c}{box_v})^{power - 1}"], [f"(1 + ({box_c}{box_v})^2)^1/2"], coefficient*power*box_dash_c]


# inverse cosine
def arccos(box_code, box_dash):
    power, coefficient, box_v, box_c = box_code[1],box_code[2], box_code[5][0], box_code[5][1]
    box_dash_v = box_dash[0]
    box_dash_c = box_dash[1]
    if power == 1:
        return [[f"{box_dash_v}",f"(1 + ({box_c}{box_v})^2)^1/2"], -coefficient*power*box_dash_c]
    else:
        return [[f"{box_dash_v}arccos({box_c}{box_v})^{power - 1}"], [f"(1 + ({box_c}{box_v})^2)^1/2"], -coefficient*power*box_dash_c]


# inverse tangent
def arcctan(box_code, box_dash):
    power, coefficient, box_v, box_c = box_code[1],box_code[2], box_code[5][0], box_code[5][1]
    box_dash_v = box_dash[0]
    box_dash_c = box_dash[1]
    if power == 1:
        return [[f"{box_dash_v}",f"1 + ({box_c}{box_v})^2"], -coefficient*power*box_dash_c]
    else:
        return [[f"{box_dash_v}arctan({box_c}{box_v})^{power - 1}"], [f"(1 + ({box_c}{box_v}))^1/2"], -coefficient*power*box_dash_c]
