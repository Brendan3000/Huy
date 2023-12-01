# product rule
def product(first, first_derivative, second, second_derivative):
    first_v = first[0]
    first_c = first[1]
    first_derivative_v = first_derivative[0]
    first_derivative_c = first_derivative[1]
    second_v = second[0]
    second_c = second[1]
    second_derivative_v = second_derivative[0]
    second_derivative_c = second_derivative[1]
    return [f"{second_c*first_derivative_c}{second_v}{first_derivative_v} + {second_derivative_c*first_c}{second_derivative_v}{first_v}", 1]

