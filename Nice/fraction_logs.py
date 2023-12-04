from Nice import Brackets


# ln() or logb() [has function_determiner value = 5]
def logaraithm(box_code, box_dash):
        power, coefficient, base, box_v, box_c = box_code[1],box_code[2],box_code[3], box_code[5][0], box_code[5][1]
        box_dash_v, box_dash_c = box_dash[0], box_dash[1]
        constant_product = coefficient*power*box_dash_c
        shift, need_to_tidy_up = Brackets.shift_assembler(box_code[0][0], box_code[0][1])
        ln_or_logb = f"log_{base} "
        ln_base = f"ln({base})"
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
        # we achieve ln if base = 1
        if base == 1:
                ln_or_logb = "ln"
                ln_base = ""
        if need_to_tidy_up:
                constant_product *= 1/(box_c)
                box_c = ""
        if need_to_tidy_up and Brackets.closed(box_v):
                bottom = f"{box_c}{box_v}{shift}"
        elif Brackets.dealing_with_exponentials(box_v) and need_to_tidy_up:
                bottom = f"{box_c}{box_v}{shift}"
        else:
                bottom = f"({box_c}{box_v}{shift})"
        # This serves to avoid the possibility of some ((f(x))) (i.e. avoid double brackets when not required)
        if need_to_tidy_up and box_c == "":
                Brackets.brackets_remover(box_v)
        if power == 1:
                return [[f"{box_dash_v}", f"{ln_base}{bottom}"], constant_product]
        else:
                if power > 0:
                    return [[f"{box_dash_v}{ln_or_logb}({box_c}{box_v}{shift}){index}", f"{ln_base}{bottom}"], constant_product]
                if power < 0:
                    return [[f"{box_dash_v}", f"{ln_base}{bottom}{ln_or_logb}({box_c}{box_v}{shift}){index}"], constant_product]


