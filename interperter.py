from Nice import Brackets


def interpret(list):
    if list[0][0] == 0:
        sign = "+"
    else:
        sign = "-"
    shift, power, coefficient, base, function_determiner, box_v, box_c = list[0][1], list[1],list[2], list[3], list[4], list[5][0], list[5][1]
    # if our constant is 1 we don't want 1box we just want box
    if box_c == 1:
        box_c = ""
    # if our power is 1 we don't want box^1 we just want  box
    if power != 1:
        index = f"^{power}"
    else:
        index = ""
    # for box^n
    if function_determiner == 0:
        if shift != 0:
            return [f"({box_c}{box_v} {sign} {shift}){index}", coefficient]
        else:
            return [f"({box_c}{box_v}){index}", coefficient]
    # for trig
    if 1 <= function_determiner <= 3 or 6 <= function_determiner <= 8:
        master_key = [0,"sin", "cos", "tan", 0, 0, "arcsin", "arccos", "arctan"]
        if shift != 0:
            return [f"{master_key[function_determiner]}({box_c}{box_v} {sign} {shift}){index}", coefficient]
        else:
            return [f"{master_key[function_determiner]}({box_c}{box_v}){index}", coefficient]
    # for exponentials
    if function_determiner == 4:
        if base == 1:
            base = "e"
        if shift != 0:
            return [f"{base}^({box_c}{box_v} {sign} {index})", coefficient]
        else:
            return [f"({base})^{box_c}{box_v}", coefficient]
    # for logs
    if function_determiner == 5:
        ln_or_logb = f"log{base}"
        if base == 1:
            expression_of_log = "ln"
        if shift != 0:
            return [f"{ln_or_logb}({box_c}{box_v} {sign} {shift}){index}", coefficient]
        else:
            return [f"{ln_or_logb}({box_c}{box_v}){index}", coefficient]


list = [[1, 0], 2, 6, 1, 5, ["x", 3]]
for k in range(1,3):
    for i in range(9):
        list = [[1, 0], 0.5, 6, k, i, ["cos(e^3x)", 8]]
        print(f"{interpret(list)[1]}{interpret(list)[0]}")
