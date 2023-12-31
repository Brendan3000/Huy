import number_theory
import powers
import products
import quotients
import fractions
from Nice import Brackets


def power_returner(box_v):
    index_counter = 0
    for letter in box_v:
        if letter == "-" or letter == "." or letter.isdigit():
            index_counter += 1
        else:
            break
    if index_counter == 0:
        return 1
    if index_counter == 1:
        if box_v[0] == "-":
            return -1
        else:
            return products.return_number(box_v[:1])
    else:
        return products.return_number(box_v[:index_counter])


def power_adjuster(box_v):
    print(box_v)
    if len(box_v) == 0:
        return box_v
    while True:
        i = 0
        for i in range(len(box_v)):
            can_work_out = False
            index_next_closed_bracket = i + products.next_closed_bracket(box_v[i:])
            index_nearest_open_bracket = i + box_v[i:].find("(")
            functions = ["sin", "cos", "tan", "ln", "log", "arcsin","arccos", "arctan"]
            functions_length = [3,3,3,2,3,6,6,6]
            if index_nearest_open_bracket == i and not index_next_closed_bracket == len(box_v) - 1:
                can_work_out = True
                counter = 0
                for open in functions:
                    try:
                        if box_v[i-functions_length[counter]:i] == open:
                            can_work_out = False
                    except:
                        pass
                    counter += 1
            else:
                try:
                    if box_v[i-3:i] == "arc":
                        good = False
                    else:
                        good = True
                except:
                    good = True
                for open in functions:
                    if open == box_v[i:index_nearest_open_bracket] and good:
                        can_work_out = True
                try:
                    if "log" == box_v[i:i+3]:
                        can_work_out = True
                except:
                    pass
            if box_v[i] == "x" and len(box_v) > 1:
                can_work_out = True
                index_next_closed_bracket = i
            if can_work_out:
                power = power_returner(box_v[index_next_closed_bracket+2:])
                if not isinstance(power,int):
                    length_number = len(str(power))
                    power = str(fractions.Fraction(str(power)))
                    power_numerator, power_denominator = products.return_number(power[:str(power).find("/")]),products.return_number(power[power.find("/")+1:])
                    under = box_v[i:index_next_closed_bracket+1]
                    under = powers.power_distributor(under,power_numerator)
                    if power_denominator == 2:
                        box_v = box_v[:i] + f"√{under} " + box_v[index_next_closed_bracket+3+length_number:]
                    else:
                        if under[0] == "(" and products.next_closed_bracket(under) == len(under) - 1:
                            under = under[1:len(under) - 1]
                        box_v = box_v[:i] + f"√({power_denominator}&{under}) " + box_v[index_next_closed_bracket+3+length_number:]
                    break
        if i == len(box_v) - 1:
            break
    print(box_v)
    print(" ")
    return box_v


def for_presentation_table(box):
    box = number_theory.float_to_fraction(box)
    can_we_release_the_numerator_box = False
    if box[1] == 1 and not null_numerator(box[0]):
        box[1] = ""
        if not products.contains_sum(box[0]):
            can_we_release_the_numerator_box = True
    if box[1] == -1 and not null_numerator(box[0]):
        box[1] = "-"
    box[0] = quotients.double_brackets_remover(box[0],can_we_release_the_numerator_box)
    box[0] = Brackets.brackets_remover(power_adjuster(box[0]))
    if box[1] == 1 and not null_numerator(box[0]):
        box[1] = ""
    if box[1] == -1 and not null_numerator(box[0]):
        box[1] = "-"
    while "z" in box[0]:
        box[0] = box[0].replace("z", " ")
    while "(/" in box[0]:
        box[0] = box[0].replace("(/","(1/" )
    while "tag" in box[0]:
        box[0] = box[0].replace("tag","" )
    return f"{box[1]}{box[0]}"


def null_numerator(box):
    numerator, denominator = quotients.splitter(box)
    if len(numerator) == 0:
        return True
    else:
        return False


def null_denominator(box):
    numerator, denominator = quotients.splitter(box)
    if len(denominator) == 0:
        return True
    else:
        return False

