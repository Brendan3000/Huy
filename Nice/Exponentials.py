# add only_one
# e to the x
def euler_exponential(box_code, box_dash):
    shift, power, coefficient, base, function_determiner, box_v, box_c = box_code[0][1], box_code[1],box_code[2], box_code[3], box_code[4], box_code[5][0], box_code[5][1]
    box_dash_v = box_dash[0]
    box_dash_c = box_dash[1]
    return [f"{box_dash_v}e^{box_c}{box_v}", coefficient*box_dash_c]


# a to the x
def exponential(box_code, box_dash):
    shift, power, coefficient, base, function_determiner, box_v, box_c = box_code[0][1], box_code[1],box_code[2], box_code[3], box_code[4], box_code[5][0], box_code[5][1]
    box_dash_v = box_dash[0]
    box_dash_c = box_dash[1]
    return [f"{box_dash_v}ln({base}){base}^{box_c}{box_v}", coefficient*box_dash_c]
