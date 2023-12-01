# ln()
def natural_logaraithm(box_code, box_dash):
        power, coefficient, base, box_v, box_c = box_code[1],box_code[2],box_code[3], box_code[5][0], box_code[5][1]
        box_dash_v = box_dash[0]
        box_dash_c = box_dash[1]
        if power == 1:
                return [[f"{box_dash_v}", f"{box_v}"], (coefficient*power*box_dash_c)/box_c]
        if power == 2:
                return [[f"{box_dash_v}ln({box_c}{box_v})", f"{box_v}"], (coefficient*power*box_dash_c)/box_c]
        else:
                return [[f"{box_dash_v}ln({box_c}{box_v})^{power - 1}", box_v], (coefficient*power*box_dash_c)/box_c]


# logb()
def logaraithm(box_code, box_dash):
        shift, power, coefficient, base, function_determiner, box_v, box_c = box_code[0][1], box_code[1],box_code[2], box_code[3], box_code[4], box_code[5][0], box_code[5][1]
        box_dash_v = box_dash[0]
        box_dash_c = box_dash[1]
        if power == 1:
                return [[f"{box_dash_v}", f"ln({base}){box_c}{box_v}"], (coefficient*power*box_dash_c)/box_c]
        if power == 2:
                return [[f"{box_dash_v}log{base}({box_c}{box_v})", f"ln({base}){box_c}{box_v}"], (coefficient*power*box_dash_c)/box_c]
        else:
                return [[f"{box_dash_v}log{base}({box_c}{box_v})^{power - 1}", f"ln({box_c}{box_v}){box_v}"], (coefficient*power*box_dash_c)/box_c]





