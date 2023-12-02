from Nice import Brackets


def interpret(list):
    shift, need_to_tidy_up = Brackets.shift_assembler(list[0][0], list[0][1])
    power, coefficient, base, function_determiner, box_v, box_c = list[1],list[2], list[3], list[4], list[5][0], list[5][1]
    # if our constant is 1 we don't want 1box we just want box
    if box_c == 1:
        box_c = ""
    # if our power is 1 we don't want box^1 we just want  box
    if power != 1:
        index = f"^{power}"
    else:
        index = ""
    # To avoid the possibitly of double brackets ((f(x)))
    if need_to_tidy_up and box_c == "":
        box_v = Brackets.brackets_remover(box_v)
    # for box^n
    if function_determiner == 0:
        # To avoid unnecessary brackets
        if Brackets.closed(box_v) and box_v.rfind(")") == (len(box_v)-1) and box_c == "" and need_to_tidy_up:
            pass
        else:
            box_c = "(" + str(box_c)
            shift += ")"
        return [f"{box_c}{box_v}{shift}{index}", coefficient]
    # for trig
    if 1 <= function_determiner <= 3 or 6 <= function_determiner <= 8:
        master_key = [0,"sin", "cos", "tan", 0, 0, "arcsin", "arccos", "arctan"]
        return [f"{master_key[function_determiner]}({box_c}{box_v}{shift}){index}", coefficient]
    # for exponentials
    if function_determiner == 4:
        if base == 1:
            base = "e"
        else:
            base = f"({base})"
        return [f"({base})^{power}({box_c}{box_v}{shift})", coefficient]
    # for logs
    if function_determiner == 5:
        ln_or_logb = f"log{base}"
        if base == 1:
            ln_or_logb = "ln"
        return [f"{ln_or_logb}({box_c}{box_v}{shift}){index}", coefficient]


