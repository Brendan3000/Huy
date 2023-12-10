import products
from Nice import Brackets
import sorting


def interpret(list):
    shift, need_to_tidy_up = Brackets.shift_assembler(list[0][0], list[0][1])
    power, coefficient, base, function_determiner, box_v, box_c = list[1],list[2], list[3], list[4], list[5][0], list[5][1]
    nice_box = sorting.for_presentation_table([box_v, box_c])
    box_c_copy = box_c
    # if our constant is 1 we don't want 1box we just want box
    if box_c == 1:
        box_c = ""
    if box_c == -1:
        box_c = ""
    # if our power is 1 we don't want box^1 we just want  box
    if power != 1:
        index = f"^{power} "
    else:
        index = ""
    # for box^n
    if function_determiner == 0:
        if power == 1:
            if need_to_tidy_up and not products.contains_sum(nice_box):
                return [f"{nice_box}", products.return_number(coefficient*box_c_copy)]
            else:
                return [f"({nice_box}{shift})", products.return_number(coefficient)]
        else:
            if Brackets.closed_no_power(box_v) and box_c == "" and need_to_tidy_up:
                return [f"{box_v}{index}", products.return_number(coefficient)]
            else:
                return [f"({nice_box}{shift}){index}", products.return_number(coefficient)]
    # for trig
    if 1 <= function_determiner <= 3 or 6 <= function_determiner <= 8:
        master_key = [0,"sin", "cos", "tan", 0, 0, "arcsin", "arccos", "arctan"]
        return [f"{master_key[function_determiner]}({nice_box}{shift}){index}", products.return_number(coefficient)]
    # for exponentials
    if function_determiner == 4:
        if power == 1:
            power = ""
        if power == -1:
            power = "-"
        if base == 1:
            base = "e"
        else:
            base = f"({base})"
        if need_to_tidy_up and Brackets.closed(box_v):
            return [f"{base}^({power*box_c_copy}{box_v}) ", products.return_number(coefficient)]
        else:
            return [f"{base}^({power}({nice_box}{shift})) ", products.return_number(coefficient)]
    # for logs
    if function_determiner == 5:
        ln_or_logb = f"log_{base} "
        if base == 1:
            ln_or_logb = "ln"
        return [f"{ln_or_logb}({nice_box}{shift}){index}", products.return_number(coefficient)]

