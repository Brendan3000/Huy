# product rule
def product(first, first_dx, second, second_dx):
    a_v, a_c, a_dx_v, a_dx_c, b_v, b_c, b_dx_v, b_dx_c  = first[0], first[1], first_dx[0], first_dx[1], second[0], second[1], second_dx[0], second_dx[1]
    return [f"{b_c*a_dx_c}{b_v}{a_dx_v} + {b_dx_c*a_c}{b_dx_v}{a_v}",
            1]

