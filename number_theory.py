import quotients
import fractions
import products


def float_to_fraction(box):
    box_v, box_c = box[0], box[1]
    numerator, denominator = quotients.splitter(box_v)
    box_c = str(fractions.Fraction(box_c))
    if "/" in box_c:
        box_c_numerator = products.return_number(box_c[:box_c.find("/")])
        box_c_denominator = products.return_number(box_c[box_c.find("/")+1:])
    else:
        box_c_numerator = products.return_number(box_c)
        box_c_denominator = ""
    if box_c_numerator == 1 and numerator != "":
        box_c_numerator = ""
    if box_c_numerator == -1 and numerator != "":
        box_c_numerator = "-"
    if box_c_denominator == 1:
        box_c_denominator = ""
    if box_c_denominator == -1:
        box_c_denominator = "-"
    return [quotients.assembler(numerator,f"{box_c_denominator}{denominator}"), box_c_numerator]


def is_power_rational(base, exponent):
    box_c = str(fractions.Fraction(base))
    if "/" in box_c:
        base_numerator = products.return_number(box_c[:box_c.find("/")])
        base_denominator = products.return_number(box_c[box_c.find("/")+1:])
        if is_a_integer(base_numerator**exponent) and is_a_integer(base_denominator**exponent):
            return True
    else:
        base_numerator = products.return_number(box_c)
        if is_a_integer(base_numerator**exponent):
            return True
    return False


def is_a_integer(number):
    string = str(number)
    if not "." in string:
        return True
    else:
        integer = True
        for letter in string[string.find(".")+1:]:
            if letter != "0":
                integer = False
    if integer:
        return True
    else:
        return False



