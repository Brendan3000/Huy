# coefficient_power_direct
def coefficient_power_direct(box_v, box_c, box_dash_c, power, coefficient):
    if not isinstance(box_c**power, complex):
        coefficient *= box_c**power
        box_c = 1
        return [box_v, box_c, box_dash_c, power, coefficient]
    if isinstance(box_c**power, complex):
        coefficient *= (-box_c)**power
        box_c = 1
        box_dash_c = box_dash_c*(-1)
        box_v = "-" + box_v
        return [box_v, box_c, box_dash_c, power, coefficient]

def index_laws(box_variable):
    if "^" in box_variable:
        list = ["sin", "cos", "tan", "ln", "(", "log", "arcsin","arccos", "arctan"]
        for i in list:
            if box_variable.find("i") == 0:
                if box_variable[box_variable.rfind("^")+1 : len(box_variable)-1].isdigit():
                    if box_variable.find("(") == 0 and box_variable.rfind(")") == box_variable.rfind("^")-1:
                        return [box_variable[1:box_variable.rfind("^")], int(box_variable[box_variable.rfind("^")+1 : len(box_variable)-1])]
                    else:
                        return [box_variable[:box_variable.rfind("^")], int(box_variable[box_variable.rfind("^")+1 : len(box_variable)-1])]
                # non integer power, skull face emoji
                try:
                    float(box_variable[box_variable.rfind("^")+1 : len(box_variable)-1])
                    if box_variable.find("(") == 0 and box_variable.rfind(")") == box_variable.rfind("^")-1:
                        return [box_variable[1:box_variable.rfind("^")], float(box_variable[box_variable.rfind("^")+1 : len(box_variable)-1])]
                    else:
                        return [box_variable[:box_variable.rfind("^")], float(box_variable[box_variable.rfind("^")+1 : len(box_variable)-1])]
                except:
                    pass
    elif box_variable[box_variable.find("^")-1] == "e":
        if box_variable[box_variable.find("^")+1] == "(":
            return
    else:
        return [box_variable, 1]

def only_one(box):
# workingprogress this is
# fix
# good night
    box_variable = box[0]
    if len(box_variable) == 1:
        return True
    list = ["sin", "cos", "tan", "ln", "(", "log", "arcsin","arccos", "arctan"]
    for i in list:
        if box[len(box)-1] == ")" and box.find("i") == 0:
            return True

