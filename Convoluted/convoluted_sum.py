# product rule
def product(first, first_dx, second, second_dx):
    a_v = first[0]
    a_c = first[1]
    a_dx_v = first_dx[0]
    a_dx_c = first_dx[1]
    b_v = second[0]
    b_c = second[1]
    b_dx_v = second_dx[0]
    b_dx_c = second_dx[1]
    return [f"{b_c*a_dx_c}{b_v}{a_dx_v} + {b_dx_c*a_c}{b_dx_v}{a_v}", 1]

