import convoluted_sum
import products
import quotients
import powers


# a function in the form of g(x)^f(x)
def function_power(base, base_dx, power, power_dx):
    base_v, base_c, base_dx_v, base_dx_c, power_v, power_c, power_dx_v, power_dx_c = base[0], base[1], base_dx[0], base_dx[1], power[0], power[1], power_dx[0], power_dx[1]
    constant_product_a = base_dx_c*power_c
    contant_product_b = power_dx_c*base_c
    if base_c == 1:
        bottom = f"{base_v}"
    else:
        if base_c == -1:
            base_c = "-"
        bottom = f"({base_c}{base_v})"
    if power_c == 1:
        power_c = ""
    if power_c == -1:
        power_c = "-"
    top = f"{power_c}{power_v}"
    numerator_a, numerator_b, denomenator = convoluted_sum.product_short_cut(base_v, base_dx_v, power_v, power_dx_v)
    numerator_b = products.multiply_two_together(numerator_b,f"ln({bottom})")
    denomenator = products.multiply_two_together(denomenator,base_v)
    numerator, factor = products.a_sum([[numerator_a, constant_product_a],[numerator_b, contant_product_b]])
    numerator = f"{numerator}{bottom}^({top}) "
    numerator, denomenator = quotients.divide(numerator, denomenator)
    return [[numerator, denomenator],
            products.return_number(factor/base_c)]


print(function_power(["x",1], ["",1], ["x",1], ["",1]))
# quotient rule
def quotient(numerator, numerator_dx, denominator, denominator_dx):
    n_v, n_c, n_dx_v, n_dx_c, d_v, d_c, d_dx_v, d_dx_c = numerator[0], numerator[1], numerator_dx[0], numerator_dx[1], denominator[0], denominator[1],denominator_dx[0], denominator_dx[1]
    constant_product_a = d_c*n_dx_c
    contant_product_b = -d_dx_c*n_c
    non_squared_denomenator, non_squared_numerator = quotients.splitter(d_v)
    squared_denomenator, squared_numerator = power.power_distributor(non_squared_denomenator, 2),power.power_distributor(non_squared_numerator, 2)
    numerator_a, numerator_b, denomenator = convoluted_sum.product_short_cut(n_v, n_dx_v, d_v, d_dx_v)
    numerator, factor = products.a_sum([[numerator_a, constant_product_a],[numerator_b, contant_product_b]])
    numerator = products.multiply_two_together(numerator,squared_numerator)
    denomenator = products.multiply_two_together(denomenator,squared_denomenator)
    numerator, denomenator = quotients.divide(numerator,denomenator)
    return [[numerator,denomenator],
            products.return_number(factor/(d_c**2))]


print(quotient(["e^(x)",1], ["e^(x)",1], ["sin(x)",1], ["cos(x)",1]))
