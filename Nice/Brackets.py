# look at this file last (It's fucked)


# severs to convert (f(x)g(x)...) into f(x)g(x)... only if in the form (f(x)g(x)...) (closed no power)
def brackets_remover(box_variable):
    if box_variable.rfind(")") == (len(box_variable) - 1) and box_variable.rfind("(") == 0:
        return box_variable[1,len(box_variable)-1]
    else:
        return box_variable


# This serves the purpose to convert (af(x))^n into a^nf(x)^n to allow for simplification in differentiating (a is a constant)
def coefficient_power_direct(box_c, power, constant_product):
    # say if our a is -1 and power is 0.5, we don't want that
    if not isinstance(box_c**power, complex):
        constant_product *= box_c**power
        box_c = ""
        return [box_c, constant_product]
    # To remedy it occuring we simply take the magnitude of the constant and switch the sign
    if isinstance(box_c**power, complex):
        constant_product *= -(-box_c)**power
        box_c = "-"
        return [box_c, constant_product]

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
            counter_a = 0
            counter_b = 0
            for letter in box_variable:
                if letter == "(":
                    counter_a += 1
                    print(counter_a)
                if letter == ")":
                    counter_a -= 1
                    print(counter_a)
                    if counter_a == 0:
                        counter_b += 1
            # counter_b represents the number of times brackets were completely closed, we need one
            print(counter_b)
            if counter_b == 1:
                return True
            else:
                break
    else:
        return False


# for closed box_variables, power_converter separates the power within the string
# again, don't use when dealing with exponentials
# don't need?
def power_converter(box_variable):
    # testing to see if there is a power on last bracket
    if box_variable.rfind(")") == box_variable.rfind(")^"):
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


print(power_converter("cos^2(x)"))
# returns true if dealing with a exponentials in the for e^f(x) not g(x)e^f(x) (unless g(x) is constant)
def dealing_with_exponentials(box_variable):
    if "^" in box_variable:
        # need to make sure it isn't e^xf(x) by using closed()
        if box_variable.find("e") == 0 and closed(box_variable[2:]):
            return True
        elif box_variable[1:box_variable.find(")^")].isdigit():
            return True
        try:
            float(box_variable[1:box_variable.find(")^")])
            return True
        except:
            return False
    else:
        return False


# serves to convert some (a^box)^b into a^bbox
def exponentials_simplifier(box_variable, power):
    # test if there is already some constant b
    if box_variable[box_variable.find("^") + 1] == "(":
        # this is the case where there isn't some b
        return box_variable[:box_variable.find("^") + 1] + str(power) + box_variable[box_variable.find("^") +1:]
    # already some number b
    b_constant = box_variable[box_variable.find("^")+1: box_variable.find("^") + box_variable[box_variable.find("^"):].find("(")]
    # for b an integer
    if b_constant.isdigit():
        return box_variable[:box_variable.find("^") + 1] + str(power*int(b_constant)) + box_variable[box_variable.find("^") +1+len(b_constant):]
    # for b a float
    else:
        return box_variable[:box_variable.find("^") + 1] + str(power*float(b_constant)) + box_variable[box_variable.find("^") +1+len(b_constant):]


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
