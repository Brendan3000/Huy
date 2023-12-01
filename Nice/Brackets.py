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


# need to fix this whole thing
# kinda got replaced by power_converter
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
        if box_variable[box_variable.find("^")-2] == "e":
            if box_variable[box_variable.find("^")+1] == "(":
                return
        else:
            return [box_variable, 1]


# only_one will return true if box_dash would not involve calling upon convoluted
# don't use when dealing with exponentials
# can't find a use for this yet
def only_one(box_variable):
    if box_variable.count("x") == 1:
        return True
    elif box_variable.find("(") == 0:
        return True
    index_of_first_x = box_variable.find("x")
    nearest_close_bracket = box_variable[index_of_first_x:].find(")") + index_of_first_x
    nearest_open_bracket = box_variable[:index_of_first_x].rfind("(")
    if box_variable.count("x") == box_variable[nearest_open_bracket:nearest_close_bracket].count("x"):
        return True
    else:
        return False


# will return true is the variable is open and shut e.g. sin(box), ln(box), (sin(box)ln(box)), ln(box)^n but not sin(box)ln(box)
# don't use when dealing with exponentials
def closed(box_variable):
    # for the case of x
    if len(box_variable) == 1:
        return True
    # in the case of x^n
    if box_variable.find(f"x^") == 0 and box_variable.count("x") == 1:
        return  True
    # for the case of a function
    function = ["sin", "cos", "tan", "ln", "log", "arcsin","arccos", "arctan", "("]
    for i in function:
        if box_variable.find(f"{i}") == 0:
            # this loop ensures our start bracket isn't closed unit the end
            for letter in box_variable:
                counter_a = 0
                counter_b = 0
                if letter == "(":
                    counter_a += 1
                if letter == ")":
                    counter_a -= 1
                    if counter_a == 0:
                        counter_b += 1
            # counter_b represents the number of times brackets were completely closed, we need one
            if counter_b == 1:
                return True
            else:
                break
    else:
        return False


# for closed box_variables, power_converter separates the power within the string
# again, don't use when dealing with exponentials
def power_converter(box_variable):
    # testing to see if there is a power on last bracket
    if box_variable.rfind(")") == box_variable.rfind(")^"):
        try:
            return [box_variable, int(box_variable[box_variable.rfind(")^") + 2:len(box_variable)-1])]
        except:
            return [box_variable, float(box_variable[box_variable.rfind(")^") + 2:len(box_variable)-1])]
    else:
        return [box_variable,1]


def
