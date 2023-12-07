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
    return [quotients.assembler(numerator,f"{box_c_denominator}{denominator}"), box_c_numerator]

