import quotients
import fractions
import products


# will distribute a fractional box_c to the numerator box_v and denominator box_v
def float_to_fraction(box):
    box_v, box_c = box[0], box[1]
    numerator, denominator = quotients.splitter(box_v)
    box_c = str(fractions.Fraction(box_c))
    if "/" in box_c:
        # Where box_c is a fraction
        box_c_numerator = products.return_number(box_c[:box_c.find("/")])
        box_c_denominator = products.return_number(box_c[box_c.find("/")+1:])
    else:
        # Where box_c is just a integer
        box_c_numerator = products.return_number(box_c)
        box_c_denominator = ""
    # To avoid any 1box or -box
    if box_c_numerator == 1 and numerator != "":
        box_c_numerator = ""
    if box_c_numerator == -1 and numerator != "":
        box_c_numerator = "-"
    if box_c_denominator == 1:
        box_c_denominator = ""
    if box_c_denominator == -1:
        box_c_denominator = "-"
    return [quotients.assembler(numerator,f"{box_c_denominator}{denominator}"), box_c_numerator]


# input is base and exponent (floats/integers); will return True is base^exponent is rational
def is_power_rational(base, exponent):
    box_c = str(fractions.Fraction(base))
    if "/" in box_c:
        # where base is a fraction
        base_numerator = products.return_number(box_c[:box_c.find("/")])
        base_denominator = products.return_number(box_c[box_c.find("/")+1:])
        # we require both top and bottom to be rational for the whole result to be rational
        if is_a_integer(base_numerator**exponent) and is_a_integer(base_denominator**exponent):
            return True
    else:
        # where base is a integer
        base_numerator = products.return_number(box_c)
        if is_a_integer(base_numerator**exponent):
            return True
    return False


# Input is a float/integer. If this float/integer is a integer (e.g. 5 or 5.000) it will return true
def is_a_integer(number):
    string = str(number)
    if not "." in string:
        return True
    else:
        integer = True
        # To test some .00000 case
        for letter in string[string.find(".")+1:]:
            if letter != "0":
                integer = False
    if integer:
        return True
    else:
        return False



