import powers
import products
import quotients
from Nice import Brackets
from quotients import splitter
import sorting


# ln() or logb() [has function_determiner value = 5]
def logaraithm(box_code, box_dash):
        power, coefficient, base, box_v, box_c = box_code[1],box_code[2],box_code[3], box_code[5][0], box_code[5][1]
        box_dash_v, box_dash_c = box_dash[0], box_dash[1]
        constant_product = coefficient*power*box_dash_c
        nice_box = sorting.for_presentation_table([box_v, box_c])
        box_c_copy = box_c
        shift, need_to_tidy_up = Brackets.shift_assembler(box_code[0][0], box_code[0][1])
        # if our constant is 1 we don't want 1box we just want box
        if box_c == 1:
                box_c = ""
        if box_c == -1:
                box_c = "-"
        # we achieve ln if base = 1
        if base == 1:
                ln_or_logb = "ln"
                ln_base = ""
        else:
                ln_or_logb = f"log_{base} "
                ln_base = f"ln({base})"
        # in the case that box_dash is a fraction
        box_dash_v_numerator, box_dash_v_denominator = splitter(box_dash_v)
        # This serves to avoid the possibility of some ((f(x))) (i.e. avoid double brackets when not required)
        # implementing fractions
        if need_to_tidy_up:
                box_denominator, box_numerator = quotients.splitter(box_v)
                if box_c == "":
                        box_v = Brackets.brackets_remover(box_v)
                wood = f"{ln_or_logb}({nice_box})"
                constant_product *= 1/(box_c_copy)
        else:
                wood = f"{ln_or_logb}({nice_box}{shift})"
                box_denominator = f"({nice_box}{shift})"
                box_numerator = ""
        wooden_numerator = powers.power_distributor(wood, products.return_number(power-1))
        numerator = products.multiply_two_together(wooden_numerator,box_dash_v_numerator, False)
        numerator = products.multiply_two_together(numerator, box_numerator, False)
        denominator = products.multiply_two_together(ln_base, box_denominator, False)
        denominator = products.multiply_two_together(denominator, box_dash_v_denominator, False)
        numerator, denominator = quotients.divide(numerator,denominator, False)
        return [quotients.assembler(numerator,denominator), products.return_number(constant_product)]


