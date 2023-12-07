import interperter
import products
import quotients
from Nice import Basic,Exponentials, fraction_logs,fraction_inverse_trig, Brackets
import sorting
from Convoluted import convoluted_fractions,convoluted_sum
import random
random.seed(None, 2)


def diff_nice(box_current,boxdash_current, restrict):
    if not restrict:
        boxCode = generate_boxcode(box_current)
    else:
       boxCode = [[0,0],random.randint(1,8),1,random.randint(1,2),random.randint(0,8),box_current]
    if boxCode[4] == 0:
        boxdash = Basic.power(boxCode, boxdash_current)
    elif boxCode[4] == 1:
        boxdash = Basic.sin(boxCode, boxdash_current)
    elif boxCode[4] == 2:
        boxdash = Basic.cos(boxCode, boxdash_current)
    elif boxCode[4] == 3:
        boxdash = Basic.tan(boxCode, boxdash_current)
    elif boxCode[4] == 4:
        boxdash = Exponentials.exponential(boxCode, boxdash_current)
    elif boxCode[4] == 5:
        boxdash = fraction_logs.logaraithm(boxCode, boxdash_current)
    elif boxCode[4] == 6:
        boxdash = fraction_inverse_trig.arcsin(boxCode, boxdash_current)
    elif boxCode[4] == 7:
        boxdash = fraction_inverse_trig.arccos(boxCode, boxdash_current)
    else: #tan^-1
        boxdash = fraction_inverse_trig.arcctan(boxCode, boxdash_current)
    box = interperter.interpret(boxCode)
    nice_box, nice_boxdash = sorting.for_presentation_table(box, boxdash)
    return box, boxdash, nice_box, nice_boxdash


def convoluted(box_current_one,boxdash_current_one, box_current_two, boxdash_current_two, one_tow_three):
    if one_tow_three == 1:
        boxdash = convoluted_sum.product(box_current_one,boxdash_current_one, box_current_two, boxdash_current_two)
        box_current_one_numerator,box_current_one_denominator = quotients.splitter(box_current_one[0])
        box_current_two_numerator,box_current_two_denominator = quotients.splitter(box_current_two[0])
        numerator = products.multiply_two_together(box_current_two_numerator,box_current_one_numerator)
        denominator = products.multiply_two_together(box_current_two_denominator,box_current_one_denominator)
        box = [quotients.divide(numerator,denominator), products.return_number(box_current_two[1]*box_current_one[1])]
    if one_tow_three == 2:
        boxdash = convoluted_fractions.function_power(box_current_one,boxdash_current_one, box_current_two, boxdash_current_two)
        if box_current_one[1] == 1:
            box_current_one = ""
        if box_current_one[1] == -1:
            box_current_one = "-"
        if box_current_two[1] == 1:
            box_current_two = ""
        if box_current_two[1] == -1:
            box_current_two = "-"
        if not box_current_one[1] == "" or not Brackets.closed_no_power(box_current_one[0]):
            bottom = f"{box_current_one[0]}"
        else:
            bottom  = f"({box_current_one[1]}{box_current_one[0]})"
        box = f"{bottom}^({box_current_two[1]}{box_current_two[0]})"
    if one_tow_three == 3:
        boxdash = convoluted_fractions.quotient(box_current_one,boxdash_current_one, box_current_two, boxdash_current_two)
        box_current_one_numerator,box_current_one_denominator = quotients.splitter(box_current_one[0])
        box_current_two_numerator,box_current_two_denominator = quotients.splitter(box_current_two[0])
        numerator = products.multiply_two_together(box_current_two_denominator,box_current_one_numerator)
        denominator = products.multiply_two_together(box_current_two_numerator,box_current_one_denominator)
        box = [quotients.divide(numerator,denominator), products.return_number(box_current_two[1]/box_current_one[1])]
    nice_box, nice_boxdash = sorting.for_presentation_table(box, boxdash)
    return box, boxdash, nice_box, nice_boxdash


def sum():
    return


def generate_boxcode(box):
    boxCode = [["",""],"","","","",""]
    dividor = random.randint(1,2)
    boxCode[0][0] = random.randint(0, 1)
    boxCode[0][1] = random.randint(0, 1)
    power = random.randint(-8,9)
    while power == 0:
        power = random.randint(-8,9)
    boxCode[1] = power
    coefficient = random.randint(-8,9)
    while coefficient == 0:
        coefficient = random.randint(-8,9)
    boxCode[2] = coefficient
    base = random.randint(1, 3)
    boxCode[3] = base
    boxCode[4] = random.randint(0,8)
    boxCode[5] = box
    return boxCode
