import products
from Nice import Brackets
from quotients import splitter
import powers
import quotients
import sorting


# code commmon to the inverse sin, cos and tan function
def inverse_sin_cos_tan(box_code, box_dash):
    power, coefficient, box_v, box_c = box_code[1],box_code[2], box_code[5][0], box_code[5][1]
    box_dash_v, box_dash_c = box_dash[0], box_dash[1]
    constant_product = coefficient*power*box_dash_c
    shift, need_to_tidy_up = Brackets.shift_assembler(box_code[0][0], box_code[0][1])
    nice_box = sorting.for_presentation_table([box_v, box_c])
    box_v_copy, box_c_copy = box_v, box_c
    # if our constant is 1 we don't want 1box we just want box
    if box_c_copy == 1:
        box_c_copy = ""
    if box_c_copy == -1:
        box_c_copy = "-"
    # This acts to enhance the presentation of the (box)^2 term
    if need_to_tidy_up:
        # adjustment for some case (a*box)^2 just to tidy up into a^2(box)^2 where a is a constant (calculated)
        if box_c == "-":
            box_c == ""
        if box_c != "":
            box_c = box_c**2
        if box_c == 1:
            box_c = ""
        numerator, denominator = quotients.splitter(box_v)
        squared_term_numerator = powers.power_distributor(numerator,2)
        squared_term_denominator = powers.power_distributor(denominator,2)
        squared_term = quotients.assembler(f"{box_c}{squared_term_numerator}",squared_term_denominator)
    else:
        squared_term = f"({box_c}{box_v}{shift})^2"
    if box_v_copy == "" and need_to_tidy_up:
        box_v_copy = Brackets.brackets_remover(box_v_copy)
    return constant_product, box_v_copy, box_c_copy, shift, box_dash_v, power, squared_term,nice_box


# add only one
# inverse sin [has function_determiner value = 6]
def arcsin(box_code, box_dash):
    constant_product, box_v, box_c, shift,box_dash_v, power, squared_term,nice_box = inverse_sin_cos_tan(box_code, box_dash)
    # in the case that box_dash is a fraction
    box_dash_v_numerator, box_dash_v_denominator = splitter(box_dash_v)
    sin_inverse = powers.power_distributor(f"arcsin({nice_box}{shift})",products.return_number(power-1))
    square_root = f"(1 - {squared_term})^0.5 "
    numerator = products.multiply_two_together(sin_inverse, box_dash_v_numerator, False)
    denominator = products.multiply_two_together(box_dash_v_denominator,square_root, False)
    numerator, denominator = quotients.divide(numerator,denominator, False)
    return [quotients.assembler(numerator,denominator), products.return_number(constant_product)]


# inverse cosine [has function_determiner value = 7]
def arccos(box_code, box_dash):
    constant_product, box_v, box_c, shift, box_dash_v, power, squared_term,nice_box = inverse_sin_cos_tan(box_code, box_dash)
    # in the case that box_dash is a fraction
    box_dash_v_numerator, box_dash_v_denominator = splitter(box_dash_v)
    cosine_inverse = powers.power_distributor(f"arccos({nice_box}{shift})",products.return_number(power-1))
    square_root = f"(1 - {squared_term})^0.5 "
    numerator = products.multiply_two_together(cosine_inverse, box_dash_v_numerator, False)
    denominator = products.multiply_two_together(box_dash_v_denominator,square_root, False)
    numerator, denominator = quotients.divide(numerator,denominator, False)
    return [quotients.assembler(numerator,denominator), products.return_number(-constant_product)]


# inverse tangent [has function_determiner value = 8]
def arcctan(box_code, box_dash):
    constant_product, box_v, box_c, shift, box_dash_v, power, squared_term,nice_box = inverse_sin_cos_tan(box_code, box_dash)
    # in the case that box_dash is a fraction
    box_dash_v_numerator, box_dash_v_denominator = splitter(box_dash_v)
    tan_inverse = powers.power_distributor(f"arctan({nice_box}{shift})",products.return_number(power-1))
    square_root = f"(1 + {squared_term})"
    numerator = products.multiply_two_together(tan_inverse, box_dash_v_numerator, False)
    denominator = products.multiply_two_together(box_dash_v_denominator,square_root, False)
    numerator, denominator = quotients.divide(numerator,denominator, False)
    return [quotients.assembler(numerator,denominator), products.return_number(constant_product)]
