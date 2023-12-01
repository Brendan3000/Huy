# add only_one
# a function in the form of g(x)^f(x)
def function_power(base, base_derivative, power, power_derivative):
    base_v = base[0]
    base_c = base[1]
    base_derivative_v = base_derivative[0]
    base_derivative_c = base_derivative[1]
    power_v = base[0]
    power_c = base[1]
    power_derivative_v = base[0]
    power_derivative_c = base[1]
    return [[f"({base_c}{base_v})^({power_c}{power_v})({base_derivative_c*power_c}{base_derivative_v}{power_derivative_v} + {power_derivative_c*base_c}{power_derivative_v}{base_v}ln({base_c}{base_v}))",f"{base_c}{base_v}"], 1]


# quotient rule
def quotient(numerator, numerator_derivative, denominator, denominator_derivative):
    numerator_v = numerator[0]
    numerator_c = numerator[1]
    numerator_derivative_v = numerator_derivative[0]
    numerator_derivative_c = numerator_derivative[1]
    denominator_v = denominator[0]
    denominator_c = denominator[1]
    denominator_derivative_v = denominator_derivative[0]
    denominator_derivative_c = denominator_derivative[1]
    return [[f"{denominator_c*numerator_derivative_c}{denominator_v}{numerator_derivative_v} - {denominator_derivative_c*numerator_c}{denominator_derivative_v}{numerator_v}", f"{denominator}^2"], 1/denominator_c**2]


