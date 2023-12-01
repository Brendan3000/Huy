# a function in the form of g(x)^f(x)
def function_power(base, base_dx, power, power_dx):
    base_v = base[0]
    base_c = base[1]
    base_dx_v = base_dx[0]
    base_dx_c = base_dx[1]
    power_v = power[0]
    power_c = power[1]
    power_dx_v = power_dx[0]
    power_dx_c = power_dx[1]
    return [[f"({base_c}{base_v})^({power_c}{power_v})({base_dx_c*power_c}{base_dx_v}{power_dx_v} + {power_dx_c*base_c}{power_dx_v}{base_v}ln({base_c}{base_v}))",f"{base_c}{base_v}"], 1]


# quotient rule
def quotient(numerator, numerator_dx, denominator, denominator_dx):
    n_v = numerator[0]
    n_c = numerator[1]
    n_dx_v = denominator_dx[0]
    n_dx_c = denominator_dx[1]
    d_v = denominator[0]
    d_c = denominator[1]
    d_dx_v = denominator_dx[0]
    d_dx_c = denominator_dx[1]
    return [[f"{d_c*n_dx_c}{d_v}{n_dx_v} - {d_dx_c*n_c}{d_dx_v}{n_v}", f"{d_v}^2"], 1/d_c**2]


