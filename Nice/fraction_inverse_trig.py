# add only one
# inverse sin
def arcsin(box, power, coefficient, box_dash):
    box_dash_v = box_dash[0]
    box_dash_c = box_dash[1]
    box_v = box[0]
    box_c = box[1]
    if power == 1:
        return [[f"{box_dash_v}",f"(1 + ({box_c}{box_v})^2)^1/2"], coefficient*power*box_dash_c]
    else:
        return [[f"{box_dash_v}arccos({box_c}{box_v})^{power - 1}"], [f"(1 + ({box_c}{box_v})^2)^1/2"], coefficient*power*box_dash_c]


# inverse cosine
def arccos(box, power, coefficient, box_dash):
    box_dash_v = box_dash[0]
    box_dash_c = box_dash[1]
    box_v = box[0]
    box_c = box[1]
    if power == 1:
        return [[f"{box_dash_v}",f"(1 + ({box_c}{box_v})^2)^1/2"], -coefficient*power*box_dash_c]
    else:
        return [[f"{box_dash_v}arccos({box_c}{box_v})^{power - 1}"], [f"(1 + ({box_c}{box_v})^2)^1/2"], -coefficient*power*box_dash_c]


# inverse tangent
def arcctan(box, power, coefficient, box_dash):
    box_dash_v = box_dash[0]
    box_dash_c = box_dash[1]
    box_v = box[0]
    box_c = box[1]
    if power == 1:
        return [[f"{box_dash_v}",f"1 + ({box_c}{box_v})^2"], -coefficient*power*box_dash_c]
    else:
        return [[f"{box_dash_v}arctan({box_c}{box_v})^{power - 1}"], [f"(1 + ({box_c}{box_v}))^1/2"], -coefficient*power*box_dash_c]
