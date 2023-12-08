import number_theory
import fractions


def next_closed_bracket(box_v):
    counter_a = 0
    i = 0
    for letter in box_v:
        if letter == "(":
            counter_a += 1
        if letter == ")":
            counter_a -= 1
            if counter_a == 0:
                break
        i += 1
    return i


# will return true if brackets are not closed
def is_closed_in(box_v):
    counter_a = 0
    i = 0
    for letter in box_v:
        if letter =="(":
            counter_a += 1
        if letter == ")":
            counter_a -= 1
    if counter_a == 0:
        return False
    else:
        return True


# This function is not used
# inputs a nice (positive integer power) power and a closed, without trig function and outputs some sin^n(x)
def trig_nice_power(box_variable, power):
    basic_trig = ["sin", "cos", "tan"]
    for i in basic_trig:
        if box_variable.find(i) == 0:
            return f"{i}^{power}({box_variable})"


# This function is not used
# returns true if box_variable begins with a trig function
def basic_trig(box_variable):
    basic_trig = ["sin", "cos", "tan"]
    for i in basic_trig:
        if box_variable.find(i) == 0:
            return True
    else:
        return False


# This function is used
# severs to convert (f(x)g(x)...) into f(x)g(x)... only if in the form (f(x)g(x)...) (closed no power)
def brackets_remover(box_variable):
    if len(box_variable) - 1 == next_closed_bracket(box_variable) and box_variable.find("(") == 0:
        return box_variable[1:len(box_variable)-1]
    else:
        return box_variable


# This function is used
# This serves the purpose to convert (af(x))^n into a^nf(x)^n to allow for simplification in differentiating (a is a constant)
def coefficient_power_direct(box_c, box_v, power, constant_product):
    # say if our a is -1 and power is 0.5, we don't want that
    if not isinstance(box_c**power, complex):
        if number_theory.is_power_rational(box_c, power):
            constant_product *= box_c**power
        else:
            box_v = f"({fractions.Fraction(box_c)})^{power}" + box_v
    # To remedy it occuring we simply take the magnitude of the constant and switch the sign
    else:
        if number_theory.is_power_rational(-box_c, power):
            constant_product *= (-box_c)**power
            box_v = f"(-1)^{power}" + box_v
        else:
            box_v = f"({fractions.Fraction(box_c)})^{power}" + box_v
    return box_v, constant_product


# This function is not used
# don't look at this one
# need to fix this whole thing
# kinda got replaced by power_converter
# just here for reminder
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


# This function is not used
# only_one will return true if box_dash would not involve calling upon convoluted
# don't use when dealing with exponentials
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


# This function is used
# will return true is the variable is open and shut (and not to a power) e.g. sin(box), ln(box), (sin(box)ln(box)) but not sin(box)ln(box) or ln(box)^n
def closed_no_power(box_variable):
    # for the case of x
    if len(box_variable) == 1:
        return True
    # for the case of a function
    if box_variable.rfind(")") == (len(box_variable) - 1):
        function = ["sin", "cos", "tan", "ln", "log", "arcsin","arccos", "arctan", "("]
        for i in function:
            if box_variable.find(f"{i}") == 0:
                # this loop ensures our start bracket isn't closed unit the end
                counter_a = 0
                counter_b = 0
                for letter in box_variable:
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


# This function is used
# will return true is the variable is open and shut (and could be to a power) e.g. sin(box), ln(box), (sin(box)ln(box)), ln(box)^n but not sin(box)ln(box)
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
            counter_a = 0
            counter_b = 0
            for letter in box_variable:
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


# This function is used
# for closed box_variables, power_converter separates the power within the string
# again, don't use when dealing with exponentials
def power_converter(box_variable):
    # case of some x^n
    if box_variable.rfind("x") == 0:
        if len(box_variable) == 1:
            return box_variable, 1
        else:
            try:
                return "x", int(box_variable[2:])
            except:
                return "x", float(box_variable[2:])
    # testing to see if there is a power on last bracket (case of a function)
    if box_variable.rfind(")") == box_variable.rfind(")^") and "^)" in box_variable:
        try:
            return box_variable[:box_variable.rfind("^")], int(box_variable[box_variable.rfind(")^") + 2:])
        except:
            return box_variable[:box_variable.rfind("^")], float(box_variable[box_variable.rfind(")^") + 2:])
    # for the case of some trig sin^n(x) where n is a integer (postive)
    basic_trig = ["sin", "cos", "tan"]
    for i in basic_trig:
        if box_variable.find(i) == 0 and box_variable[3] == "^":
            return box_variable[:3] + box_variable[box_variable.find("("):], int(box_variable[4:box_variable.find("(")])
    else:
        return box_variable, 1


# This function is used
# returns true if dealing with a exponentials in first position
def dealing_with_exponentials(box_variable):
    if "^" in box_variable:
        # need to make sure it isn't e^xf(x) by using closed()
        if box_variable.find("e") == 0:
            return True
        if box_variable[1:box_variable.find(")^")].isdigit():
            return True
        try:
            a = float(box_variable[1:box_variable.find(")^")])
            return True
        except:
            return False
    else:
        return False


# This function is used
# serves to convert some (a^box)^b into a^bbox
def exponentials_simplifier(box_variable, power):
    # case of e^f(x)
    if box_variable.find("e") == 0:
        i = 0
        for letter in box_variable[3:]:
            if letter.isdigit() or letter == "-" or letter == ".":
                i += 1
            else:
                break
        if closed(box_variable[3+i:box_variable.rfind(")")]):
            if i == 1 and box_variable[3] == "-":
                modified = box_variable[:4] + power + box_variable[4:]
                return modified
            elif i >= 1:
                try:
                    modified = box_variable[:3] + str(power*int(box_variable[3:3+i])) + box_variable[3+i:]
                    return modified
                except:
                    modified = box_variable[:3] + str(power*int(box_variable[3:3+i])) + box_variable[3+i:]
                    return modified
    # case of (a)^g(x)
    if box_variable.find("(") == 0:
        i = 0
        for letter in box_variable[5:]:
            if letter.isdigit() or letter == "-" or letter == ".":
                i += 1
            else:
                break
        if closed(box_variable[5+i:box_variable.rfind(")")]):
            if i == 1 and box_variable[5] == "-":
                modified = box_variable[:5] + power + box_variable[5:]
                return modified
            elif i >= 1:
                try:
                    modified = box_variable[:5] + str(power*int(box_variable[5:5+i])) + box_variable[5+i:]
                    return modified
                except:
                    modified = box_variable[:5] + str(power*float(box_variable[5:5+i])) + box_variable[5+i:]
                    return modified
    else:
        return box_variable


# This function is used
# input is a list containing sign and magnitude, output is it assembled and a boolean value for if there is no shift (0)
def shift_assembler(sign, magnitude):
    if sign == 0:
        can_think_of_a_name = "+"
    if sign == 1:
        can_think_of_a_name = "-"
    if magnitude == 0:
        return "", True
    else:
        return f" {can_think_of_a_name} {magnitude}", False
