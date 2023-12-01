from Nice import Brackets
# This will be used to display the function input to be differentiated
def interpret(list):
    shift, power, coefficient, base, function_determiner, box_v, box_c = list[0][1], list[1],list[2], list[3], list[4], list[5][0], list[5][1]
    if list[0][0] == 0:
        sign = " + "
    else:
        sign = " - "
    # to avoid some (x - 0) or (x + 0)
    if shift == 0:
        shift = ""
        sign = ""
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
        return [f"({box_c}{box_v}{sign}{shift}){index}", coefficient]

    # for trig
    if 1 <= function_determiner <= 3 or 6 <= function_determiner <= 8:
        master_key = [0,"sin", "cos", "tan", 0, 0, "arcsin", "arccos", "arctan"]
        return [f"{master_key[function_determiner]}({box_c}{box_v}{sign}{shift}){index}", coefficient]
    # for exponentials
    if function_determiner == 4:
        if base == 1:
            bottom = "e"
        else:
            bottom = f"({base})"
        return [f"{bottom}^{power}({box_c}{box_v}{sign}{shift})", coefficient]
    # for logs
    if function_determiner == 5:
        ln_or_logb = f"log{base}"
        if base == 1:
            ln_or_logb = "ln"
        return [f"{ln_or_logb}({box_c}{box_v}{sign}{shift}){index}", coefficient]

# an example to play around with
list = [[1, 0], 2, 6, 1, 5, ["x", 3]]
print(f"{interpret(list)[1]}{interpret(list)[0]}")
# iterative example
for k in range(1,3):
    for i in range(9):
        list = [[1, 0], 0.5, 6, k, i, ["cos(e^3x)", 8]]
        print(f"{interpret(list)[1]}{interpret(list)[0]}")
