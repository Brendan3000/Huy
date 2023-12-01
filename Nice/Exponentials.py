# add only_one
# e to the x
def euler_exponential(box, e, coefficient, box_dash):
    box_dash_v = box_dash[0]
    box_dash_c = box_dash[1]
    box_v = box[0]
    box_c = box[1]
    return [f"{box_dash_v}{e}^{box_c}{box_v}", coefficient*box_dash_c]


# a to the x
def exponential(box, a, coefficient, box_dash):
    box_dash_v = box_dash[0]
    box_dash_c = box_dash[1]
    box_v = box[0]
    box_c = box[1]
    return [f"{box_dash_v}ln({a}){a}^{box_c}{box_v}", coefficient*box_dash_c]
