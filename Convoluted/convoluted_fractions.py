import products
import quotients
import powers
from Nice import Brackets


# a function in the form of g(x)^f(x)
def function_power(base, base_dx, power, power_dx):
    base_v, base_c, base_dx_v, base_dx_c, power_v, power_c, power_dx_v, power_dx_c = base[0], base[1], base_dx[0], base_dx[1], power[0], power[1], power_dx[0], power_dx[1]
    constant_product_a = base_dx_c*power_c
    constant_product_b = power_dx_c*base_c
    base_v_copy = base_v
    base_c_copy = base_c
    if base_c_copy == 1:
        base_c_copy = ""
    if base_c_copy == -1:
        base_c_copy = 1
    if base_c == 1:
        bottom = f"{base_v}"
    else:
        bottom = f"({base_c}){base_v}"
    if power_c == 1:
        power_c = ""
    if power_c == -1:
        power_c = "-"
    if base_c == "":
        base_v = Brackets.brackets_remover(base_v)
    top = f"({power_c}{power_v})"
    to_the_power = powers.power_distributor(bottom, top)
    numerator_a, numerator_b, denominator = product_short_cut(base_v, base_dx_v, power_v, power_dx_v)
    numerator_b = products.multiply_two_together(numerator_b,f"ln({base_c_copy}{base_v})", False)
    denominator = products.multiply_two_together(denominator, base_v_copy, False)
    numerator, factor = products.a_sum([[numerator_a, constant_product_a],[numerator_b, constant_product_b]])
    numerator = f"{to_the_power}{numerator}"
    numerator, denominator = quotients.divide(numerator, denominator, False)
    return [quotients.assembler(numerator,denominator),
            products.return_number(factor/base_c)]


# quotient rule
def quotient(numerator, numerator_dx, denominator, denominator_dx):
    n_v, n_c, n_dx_v, n_dx_c, d_v, d_c, d_dx_v, d_dx_c = numerator[0], numerator[1], numerator_dx[0], numerator_dx[1], denominator[0], denominator[1],denominator_dx[0], denominator_dx[1]
    constant_product_a = d_c*n_dx_c
    constant_product_b = -d_dx_c*n_c
    non_squared_denominator, non_squared_numerator = quotients.splitter(d_v)
    squared_denominator, squared_numerator = powers.power_distributor(non_squared_denominator, 2),powers.power_distributor(non_squared_numerator, 2)
    numerator_a, numerator_b, denominator = product_short_cut(n_v, n_dx_v, d_v, d_dx_v)
    numerator, factor = products.a_sum([[numerator_a, products.return_number(constant_product_a)],[numerator_b, products.return_number(constant_product_b)]])
    numerator = products.multiply_two_together(numerator,squared_numerator, False)
    denominator = products.multiply_two_together(denominator,squared_denominator, False)
    numerator, denominator = quotients.divide(numerator,denominator, False)
    return [quotients.assembler(numerator,denominator),
            products.return_number(factor/(d_c**2))]


def product_short_cut(a_v, a_dx_v, b_v, b_dx_v):
    a_n, a_d, a_dx_n, a_dx_d, b_n, b_d, b_dx_n, b_dx_d = quotients.splitter(a_v)[0], quotients.splitter(a_v)[1], quotients.splitter(a_dx_v)[0], quotients.splitter(a_dx_v)[1], quotients.splitter(b_v)[0],quotients.splitter(b_v)[1], quotients.splitter(b_dx_v)[0], quotients.splitter(b_dx_v)[1]
    term_one_numerator = products.multiply_two_together(a_n,b_dx_n, False)
    term_two_numerator = products.multiply_two_together(b_n,a_dx_n, False)
    term_one_denomenator = products.multiply_two_together(a_d,b_dx_d, False)
    term_two_denomenator = products.multiply_two_together(b_d,a_dx_d, False)
    denomenator = products.multiply_two_together(term_one_denomenator, term_two_denomenator, False)
    numerator_a = products.multiply_two_together(term_one_numerator, term_two_denomenator, False)
    numerator_b = products.multiply_two_together(term_one_denomenator, term_two_numerator, False)
    return numerator_a, numerator_b, denomenator
