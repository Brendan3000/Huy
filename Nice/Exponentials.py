import quotients
from Nice import Brackets
from quotients import splitter
import products
import sorting


# e to the x or a to the x (a is a constant) [has function_determiner value = 4]
def exponential(box_code, box_dash):
    power, coefficient, base, box_v, box_c = box_code[1],box_code[2],box_code[3], box_code[5][0], box_code[5][1]
    box_dash_v, box_dash_c = box_dash[0], box_dash[1]
    constant_product = coefficient*box_dash_c*power
    shift, need_to_tidy_up = Brackets.shift_assembler(box_code[0][0], box_code[0][1])
    # This will determine if we are using e
    if base == 1:
        bottom = "e"
        ln_base = ""
    else:
        bottom = f"({base})"
        ln_base = f"ln({base})"


    if need_to_tidy_up:
        power = products.return_number(power*box_c)
        box_c = ""
    # if our constant is 1 we don't want 1box we just want box
    if box_c == 1:
        box_c = ""
    if box_c == -1:
        box_c = "-"
    # if our power is 1 we don't want 1box we just want box
    if power == 1:
        power = ""
    if power == -1:
        power = "-"
    # This serves to avoid the possibility of some ((f(x))) (i.e. avoid double brackets when not required)
    if power == "" and need_to_tidy_up and not products.contains_sum(box_v):
        box_v = Brackets.brackets_remover(box_v)
    else:
        box_c = "(" + str(box_c)
        shift += ")"
    # in the case that box_dash is a fraction
    box_dash_v_numerator, box_dash_v_denominator = splitter(box_dash_v)
    numerator = products.multiply_two_together(box_dash_v_numerator,f"{bottom}^({power}{box_c}{box_v}{shift})", False)
    numerator = products.multiply_two_together(numerator,ln_base, False)
    numerator, denominator = quotients.divide(numerator,box_dash_v_denominator, False)
    return [quotients.assembler(numerator,denominator), products.return_number(constant_product)]
