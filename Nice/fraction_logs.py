# ln() or logb() [has function_determiner value = 5]
def logaraithm(box_code, box_dash):
        power, coefficient, base, box_v, box_c = box_code[1],box_code[2],box_code[3], box_code[5][0], box_code[5][1]
        box_dash_v = box_dash[0]
        box_dash_c = box_dash[1]
        constant_product = c(coefficient*power*box_dash_c)/box_c
        ln_or_logb = f"log{base}"
        ln_base = f"ln({base})"
        # we achieve ln if base = 1
        if base == 1:
            ln_or_logb = "ln"
            ln_base = ""
        if power == 1:
                return [[f"{box_dash_v}", f"{box_v}{ln_base}"], constant_product]
        if power == 2:
                return [[f"{box_dash_v}{ln_or_logb}({box_c}{box_v})", f"{ln_base}{box_v}"], constant_product]
        else:
                return [[f"{box_dash_v}{ln_or_logb}({box_c}{box_v})^{power - 1}", f"{box_v}{ln_base}"], constant_product]




