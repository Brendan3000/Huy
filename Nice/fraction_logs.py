# ln() or logb() [has function_determiner value = 5]
def logaraithm(box_code, box_dash):
        power, coefficient, base, box_v, box_c = box_code[1],box_code[2],box_code[3], box_code[5][0], box_code[5][1]
        box_dash_v, box_dash_c = box_dash[0], box_dash[1]
        constant_product = (coefficient*power*box_dash_c)/box_c
        ln_or_logb = f"log{base}"
        ln_base = f"ln({base})"
        # if our constant is 1 we don't want 1box we just want box
        if box_c == 1:
                box_c = ""
        # if our power is 1 we don't want box^1 we just want  box
        if power != 2:
                index = f"^{power-1}"
        else:
                index = ""
        # we achieve ln if base = 1
        if base == 1:
                ln_or_logb = "ln"
                ln_base = ""
        if power == 1:
                return [[f"{box_dash_v}", f"{box_v}{ln_base}"], constant_product]
        else:
                return [[f"{box_dash_v}{ln_or_logb}({box_c}{box_v}){index}", f"{box_v}{ln_base}"], constant_product]




