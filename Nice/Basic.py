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
    box_dash_c_copy, coefficient_copy = box_dash_c, coefficient
    # if our constant is 1 we don't want 1box we just want box
    if box_c == 1:
        box_c = ""
    if box_c == -1:
        box_c = "-"

    # where there is no shift, presentation must be enhanced
    if need_to_tidy_up:
        # adjustment for some case (a*box)^n just to tidy up into a^n(box)^n where a is a constant (calculated)
        if box_c != "" and box_c != "-" and power != 1:
            a = Brackets.coefficient_power_direct(box_c,power-1, constant_product)
            box_c, constant_product = a[0], a[1]
        if box_c == "-":
            box_c = ""
        box_v = f"(-1){power - 1}" + box_v
        powered_numerator, powered_denominator = splitter(box_v)
        powered_numerator = powers.power_distributor(powered_numerator, power-1)
        powered_denominator = powers.power_distributor(powered_denominator, power-1)
    else:
        powered_denominator = ""
        powered_numerator = powers.power_distributor(f"({box_v}{box_v}{shift})")
    # in the case that box_dash is a fraction
    box_dash_v_numerator, box_dash_v_denominator = splitter(box_dash_v)
    numerator = products.multiply_two_together(powered_numerator, box_dash_v_numerator)
    denominator = products.multiply_two_together(powered_denominator, box_dash_v_denominator)
    numerator, denominator = quotients.divide(numerator, denominator)


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
    # if our power is 1 we don't want box^1 we just want  box
    if power != 2:
        if power > 0:
            index = f"^{power-1}"
        if power < 0:
            index = f"^{-power+1}"
    else:
        index = ""
    # This serves to avoid the possibility of some sin((f(x))) (i.e. avoid double brackets when not required)
    if need_to_tidy_up and box_c == "":
        Brackets.brackets_remover(box_v)
    return constant_product, box_v, box_c, shift, index, box_dash_v, power


# sin [has function_determiner value = 1]
def sin(box_code, box_dash):
    constant_product, box_v, box_c, shift, index,box_dash_v,power = sin_cos_tan(box_code, box_dash)
    # in the case that box_dash is a fraction
    box_dash_v_numerator, box_dash_v_denominator = splitter(box_dash_v)
    if power == 1:
        return [[f"{box_dash_v_numerator}cos({box_c}{box_v}{shift})",f"{box_dash_v_denominator}"],
                constant_product]
    if power == 2:
        return [[f"{box_dash_v_numerator}sin(2{box_c}{box_v}{shift})",f"{box_dash_v_denominator}"],
                constant_product*0.5]
    else:
        if power < 0:
             return [[f"{box_dash_v_numerator}cos({box_c}{box_v}{shift})",f"{box_dash_v_denominator}sin({box_c}{box_v}{shift}){index} "],
                constant_product]
        if power > 0:
            return [[f"{box_dash_v_numerator}cos({box_c}{box_v}{shift})sin({box_c}{box_v}{shift}){index} ",f"{box_dash_v_denominator}"],
                constant_product]


# cos [has function_determiner value = 2]
def cos(box_code, box_dash):
    constant_product, box_v, box_c, shift, index, box_dash_v, power = sin_cos_tan(box_code, box_dash)
    # in the case that box_dash is a fraction
    box_dash_v_numerator, box_dash_v_denominator = splitter(box_dash_v)
    if power == 1:
        return [[f"{box_dash_v_numerator}cos({box_c}{box_v}{shift})",f"{box_dash_v_denominator}"],
                -constant_product]
    if power ==2:
        return [[f"{box_dash_v_numerator}sin(2{box_c}{box_v}{shift})",f"{box_dash_v_denominator}"],
                -constant_product*0.5]
    else:
        if power < 0:
            return [[f"{box_dash_v_numerator}sin({box_c}{box_v}{shift})",f"{box_dash_v_denominator}cos({box_c}{box_v}{shift}){index}"],
                -constant_product]
        if power > 0:
            return [[f"{box_dash_v_numerator}sin({box_c}{box_v}{shift})cos({box_c}{box_v}{shift}){index}",f"{box_dash_v_denominator}"],
                -constant_product]


# tan [has function_determiner value = 3]
def tan(box_code, box_dash):
    constant_product, box_v, box_c, shift, index, box_dash_v, power= sin_cos_tan(box_code, box_dash)
    # in the case that box_dash is a fraction
    box_dash_v_numerator, box_dash_v_denominator = splitter(box_dash_v)
    if power == 1:
        return [[f"{box_dash_v_numerator}sec({box_c}{box_v}{shift})^2",f"{box_dash_v_denominator}"],
                constant_product]
    else:
        if power < 0:
            return [[f"{box_dash_v_numerator}sec({box_c}{box_v}{shift})^2",f"{box_dash_v_denominator}tan({box_c}{box_v}{shift}){index}"],
                constant_product]
        if power > 0:
            return [[f"{box_dash_v_numerator}sec({box_c}{box_v}{shift})^2 tan({box_c}{box_v}{shift}){index}",f"{box_dash_v_denominator}"],
                constant_product]

