# e to the x or a to the x (a is a constant) [has function_determiner value = 4]
def exponential(box_code, box_dash):
    power, coefficient, base, box_v, box_c = box_code[1],box_code[2],box_code[3], box_code[5][0], box_code[5][1]
    box_dash_v, box_dash_c = box_dash[0], box_dash[1]
    constant_product = coefficient*box_dash_c
    # if our constant is 1 we don't want 1box we just want box
    if box_c == 1:
        box_c = ""
    # This will determine if we are using e
    if base == 1:
            base = "e"
    return [f"{box_dash_v}({base})^{box_c}{box_v}",
            constant_product]
