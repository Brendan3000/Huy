# a function in the form of g(x)^f(x)
def function_power(base, base_dx, power, power_dx):
    base_v, base_c, base_dx_v, base_dx_c, power_v, power_c, power_dx_v, power_dx_c = base[0], base[1], base_dx[0], base_dx[1], power[0], power[1], power_dx[0], power_dx[1]
    return [[f"({base_c}{base_v})^({power_c}{power_v})({base_dx_c*power_c}{base_dx_v}{power_dx_v} + {power_dx_c*base_c}{power_dx_v}{base_v}ln({base_c}{base_v}))",
            f"{base_c}{base_v}"],
            1]


# quotient rule
def quotient(numerator, numerator_dx, denominator, denominator_dx):
    n_v, n_c, n_dx_v, n_dx_c, d_v, d_c, d_dx_v, d_dx_c = numerator[0], numerator[1], denominator_dx[0], denominator_dx[1], denominator[0], denominator[1],denominator_dx[0], denominator_dx[1]
    return [[f"{d_c*n_dx_c}{d_v}{n_dx_v} - {d_dx_c*n_c}{d_dx_v}{n_v}",
             f"{d_v}^2"],
            1/d_c**2]


