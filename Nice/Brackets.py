# look at this file last (It's fucked)


# This serves the purpose to convert (af(x))^n into a^nf(x)^n to allow for simplification in differentiating (a is a constant)
def coefficient_power_direct(box_v, box_c, power, constant_product):
    # say if our a is -1 and power is 0.5, we don't want that
    if not isinstance(box_c**power, complex):
        constant_product *= box_c**power
        box_c = 1
        return [box_v, box_c, power, constant_product]
    # To remedy it occuring we simply take the magnitude of the constant and switch the sign
    if isinstance(box_c**power, complex):
        constant_product *= -(-box_c)**power
        box_c = 1
        box_v = "-" + box_v
        return [box_v, box_c, power, constant_product]


def index_laws(box_variable):
    if "^" in box_variable:
        function = ["sin", "cos", "tan", "ln", "(", "log", "arcsin","arccos", "arctan"]
        for i in function:
            if box_variable.find("i") == 0:
                if box_variable[box_variable.rfind("^")+1 : len(box_variable)].isdigit():
                    if box_variable.find("(") == 0 and box_variable.rfind(")") == box_variable.rfind("^")-1:
                        return [box_variable[1:box_variable.rfind("^")], int(box_variable[box_variable.rfind("^")+1 : len(box_variable)])]
                    else:
                        return [box_variable[:box_variable.rfind("^")], int(box_variable[box_variable.rfind("^")+1 : len(box_variable)])]
                # for non integer power, skull face emoji
                try:
                    float(box_variable[box_variable.rfind("^")+1 : len(box_variable)])
                    if box_variable.find("(") == 0 and box_variable.rfind(")") == box_variable.rfind("^")-1:
                        return [box_variable[1:box_variable.rfind("^")], float(box_variable[box_variable.rfind("^")+1 : len(box_variable)-1])]
                    else:
                        return [box_variable[:box_variable.rfind("^")], float(box_variable[box_variable.rfind("^")+1 : len(box_variable)-1])]
                except:
                    pass
        # need to fix this part
        elif box_variable[box_variable.find("^")-2] == "e":
            if box_variable[box_variable.find("^")+1] == "(":
                return
        else:
            return [box_variable, 1]

# only_one will return true if box_dash would not involve calling upon convoluted
# fix for exponentials
def only_one(box_variable):
    if box_variable.count("x") == 1:
        return True
    elif box_variable.find("(") == 0:
        return True
    index_of_first_x = box_variable.fin("x")
    nearest_close_bracket = box_variable[index_of_first_x:].fin(")")
    nearest_open_bracket = box_variable[:index_of_first_x].rfin("(")
    if box_variable.count("x") == box_variable[nearest_open_bracket:nearest_close_bracket].count("x"):
        return True
    else:
        return False

