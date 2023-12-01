# ln()
def natural_logaraithm(box, power, coefficient, base, box_dash):
        box_dash_v = box_dash[0]
        box_dash_c = box_dash[1]
        box_v = box[0]
        box_c = box[1]
        if power == 1:
                return [[f"{box_dash_v}", f"{box_c}{box_v}"], coefficient*power*box_dash_c]
        else:
                return [[f"{box_dash_v}ln({box_c}{box_v})^{power - 1}", box], coefficient*power*box_dash_c]


# logb()
def logaraithm(box, power, coefficient, base, box_dash):
        box_dash_v = box_dash[0]
        box_dash_c = box_dash[1]
        box_v = box[0]
        box_c = box[1]
        if power == 1:
                return [[f"{box_dash_v}", f"ln({base}){box_c}{box_v}"], coefficient*power*box_dash_c]
        else:
                return [[f"{box_dash_v}log{base}({box_c}{box_v})^{power - 1}", f"ln({box_c}{box_v}){box_c}{box_v}"], coefficient*power*box_dash_c]





