import products
import quotients
from Nice import Brackets
from quotients import splitter
import powers


# box to a power (straight power rule) [has function_determiner value = 0]
# I realised too late that it was not in fact "basic" so I guess it doesn't belong here :)
def power(box_code, box_dash):
    power, coefficient, base, function_determiner, box_v, box_c = box_code[1],box_code[2], box_code[3], box_code[4], box_code[5][0], box_code[5][1]
    box_dash_v, box_dash_c = box_dash[0], box_dash[1]
    constant_product = coefficient*power*box_dash_c
    shift, need_to_tidy_up = Brackets.shift_assembler(box_code[0][0], box_code[0][1])
    box_c_copy = box_c
    # if our constant is 1 we don't want 1box we just want box
    if box_c == 1:
        box_c = ""
    if box_c == -1:
        box_c = "-"
    # where there is no shift, presentation must be enhanced
    if need_to_tidy_up:
        # adjustment for some case (a*box)^n just to tidy up into a^n(box)^n where a is a constant (calculated)
        box_v, constant_product = Brackets.coefficient_power_direct(box_c_copy,box_v,products.return_number(power-1), constant_product)
        powered_numerator, powered_denominator = splitter(box_v)
        powered_numerator = powers.power_distributor(powered_numerator, products.return_number(power-1))
        powered_denominator = powers.power_distributor(powered_denominator, products.return_number(power-1))
    else:
        powered_denominator = ""
        powered_numerator = powers.power_distributor(f"({box_c}{box_v}{shift})", products.return_number(power-1))
    # in the case that box_dash is a fraction
    box_dash_v_numerator, box_dash_v_denominator = splitter(box_dash_v)
    numerator = products.multiply_two_together(powered_numerator, box_dash_v_numerator)
    denominator = products.multiply_two_together(powered_denominator, box_dash_v_denominator)
    numerator, denominator = quotients.divide(numerator, denominator)
    return [quotients.assembler(numerator,denominator), products.return_number(constant_product)]

# code commmon to the sin, cos and tan function
def sin_cos_tan(box_code, box_dash):
    power, coefficient, box_v, box_c = box_code[1],box_code[2], box_code[5][0], box_code[5][1]
    box_dash_v, box_dash_c = box_dash[0], box_dash[1]
    constant_product = coefficient*power*box_dash_c
    shift, need_to_tidy_up = Brackets.shift_assembler(box_code[0][0], box_code[0][1])
    # if our constant is 1 we don't want 1box we just want box
    if box_c == 1:
        box_c = ""
    if box_c == -1:
        box_c = "-"
    # This serves to avoid the possibility of some sin((f(x))) (i.e. avoid double brackets when not required)
    if need_to_tidy_up and box_c == "":
        Brackets.brackets_remover(box_v)
    return constant_product, box_v, box_c, shift, box_dash_v, power


# sin [has function_determiner value = 1]
def sin(box_code, box_dash):
    constant_product, box_v, box_c, shift,box_dash_v,power = sin_cos_tan(box_code, box_dash)
    # in the case that box_dash is a fraction
    box_dash_v_numerator, box_dash_v_denominator = splitter(box_dash_v)
    sin = powers.power_distributor(f"sin({box_c}{box_v}{shift})", products.return_number(power-1))
    cosine = f"cos({box_c}{box_v}{shift})"
    numerator = products.multiply_two_together(sin, cosine)
    numerator = products.multiply_two_together(numerator, box_dash_v_numerator)
    numerator, denominator = quotients.divide(numerator, box_dash_v_denominator)
    return [quotients.assembler(numerator,denominator), products.return_number(constant_product)]


# cos [has function_determiner value = 2]
def cos(box_code, box_dash):
    constant_product, box_v, box_c, shift, box_dash_v, power = sin_cos_tan(box_code, box_dash)
    # in the case that box_dash is a fraction
    box_dash_v_numerator, box_dash_v_denominator = splitter(box_dash_v)
    cosine = powers.power_distributor(f"cos({box_c}{box_v}{shift})", products.return_number(power-1))
    sin = f"sin({box_c}{box_v}{shift})"
    numerator = products.multiply_two_together(sin, cosine)
    numerator = products.multiply_two_together(numerator, box_dash_v_numerator)
    numerator, denominator = quotients.divide(numerator, box_dash_v_denominator)
    return [quotients.assembler(numerator,denominator), products.return_number(-constant_product)]


# tan [has function_determiner value = 3]
def tan(box_code, box_dash):
    constant_product, box_v, box_c, shift, box_dash_v, power= sin_cos_tan(box_code, box_dash)
    # in the case that box_dash is a fraction
    box_dash_v_numerator, box_dash_v_denominator = splitter(box_dash_v)
    tan = powers.power_distributor(f"tan({box_c}{box_v}{shift})", products.return_number(power-1))
    sec = f"cos({box_c}{box_v}{shift})^-2 "
    numerator = products.multiply_two_together(sec, tan)
    numerator = products.multiply_two_together(numerator, box_dash_v_numerator)
    numerator, denominator = quotients.divide(numerator, box_dash_v_denominator)
    return [quotients.assembler(numerator,denominator), products.return_number(constant_product)]


