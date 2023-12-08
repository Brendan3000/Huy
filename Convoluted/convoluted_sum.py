import quotients
import products


# product rule
def product(first, first_dx, second, second_dx):
    a_v, a_c, a_dx_v, a_dx_c, b_v, b_c, b_dx_v, b_dx_c = first[0], first[1], first_dx[0], first_dx[1], second[0], second[1], second_dx[0], second_dx[1]
    a_n, a_d, a_dx_n, a_dx_d, b_n, b_d, b_dx_n, b_dx_d = quotients.splitter(a_v)[0], quotients.splitter(a_v)[1], quotients.splitter(a_dx_v)[0], quotients.splitter(a_dx_v)[1], quotients.splitter(b_v)[0],quotients.splitter(b_v)[1], quotients.splitter(b_dx_v)[0], quotients.splitter(b_dx_v)[1]
    term_one_numerator = products.multiply_two_together(a_n,b_dx_n)
    term_two_numerator = products.multiply_two_together(b_n,a_dx_n)
    term_one_denomenator = products.multiply_two_together(a_d,b_dx_d)
    term_two_denomenator = products.multiply_two_together(b_d,a_dx_d)
    denominator = products.multiply_two_together(term_one_denomenator, term_two_denomenator)
    numerator_a = products.multiply_two_together(term_one_numerator, term_two_denomenator)
    numerator_b = products.multiply_two_together(term_one_denomenator, term_two_numerator)
    numerator, factor = products.a_sum([[numerator_a, a_c*b_dx_c],[numerator_b,b_c*a_dx_c]])
    numerator, denominator = quotients.divide(numerator, denominator)
    return [quotients.assembler(numerator, denominator),
            products.return_number(factor)]






