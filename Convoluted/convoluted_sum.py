import quotients
import products


# product rule
def product(first, first_dx, second, second_dx):
    a_v, a_c, a_dx_v, a_dx_c, b_v, b_c, b_dx_v, b_dx_c = first[0], first[1], first_dx[0], first_dx[1], second[0], second[1], second_dx[0], second_dx[1]
    numerator_a, numerator_b, denominator = products.product_short_cut(a_v, a_dx_v, b_v, b_dx_v)
    numerator, factor = products.a_sum([[numerator_a, a_c*b_dx_c],[numerator_b,b_c*a_dx_c]])
    numerator, denominator = quotients.divide(numerator, denominator, False)
    return [quotients.assembler(numerator, denominator),
            products.return_number(factor)]






