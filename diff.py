import interperter
import products
import quotients
from Nice import Basic,Exponentials, fraction_logs,fraction_inverse_trig, Brackets
import sorting
from Convoluted import convoluted_fractions,convoluted_sum
import random
import powers
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
    else: # arctan(box)
        boxdash = fraction_inverse_trig.arcctan(boxCode, boxdash_current)
    box = interperter.interpret(boxCode)
    nice_box = sorting.for_presentation_table(box)
    nice_boxdash = sorting.for_presentation_table(boxdash)
    return box, boxdash, nice_box, nice_boxdash


def convoluted(box_current_one,boxdash_current_one, box_current_two, boxdash_current_two, one_tow_three):
    if one_tow_three == 1:
        boxdash = convoluted_sum.product(box_current_one,boxdash_current_one, box_current_two, boxdash_current_two)
        box_current_one_numerator,box_current_one_denominator = quotients.splitter(box_current_one[0])
        box_current_two_numerator,box_current_two_denominator = quotients.splitter(box_current_two[0])
        numerator = products.multiply_two_together(box_current_two_numerator,box_current_one_numerator, True)
        denominator = products.multiply_two_together(box_current_two_denominator,box_current_one_denominator, True)
        numerator, denominator = quotients.divide(numerator,denominator, True)
        box = [quotients.assembler(numerator,denominator), products.return_number(box_current_two[1]*box_current_one[1])]
    if one_tow_three == 2:
        box_current_one_c, box_current_two_c = box_current_one[1], box_current_two[1]
        box_current_one_v, box_current_two_v = box_current_one[0], box_current_two[0]
        base_v_numerator, base_v_denominator = quotients.splitter(box_current_one_v)
        if box_current_one_c == 1:
            bottom_numerator = f"{base_v_numerator}"
        else:
            bottom_numerator = f"({box_current_one_c}tag){base_v_numerator}"
        bottom_denominator = base_v_denominator
        to_the_power_numerator = powers.power_distributor(bottom_numerator, box_current_two_v)
        to_the_power_denominator = powers.power_distributor(bottom_denominator, box_current_two_v)
        to_the_power_numerator = powers.power_distributor(to_the_power_numerator, box_current_two_c)
        to_the_power_denominator = powers.power_distributor(to_the_power_denominator, box_current_two_c)
        numerator,denominator = quotients.divide(to_the_power_numerator,to_the_power_denominator, False)
        box = [quotients.assembler(numerator,denominator), 1]
        boxdash = convoluted_fractions.function_power(box_current_one,boxdash_current_one, box_current_two, boxdash_current_two)
    if one_tow_three == 3:
        if box_current_one == box_current_two:
            return ["",0],["",0],"","", False
        boxdash = convoluted_fractions.quotient(box_current_one,boxdash_current_one, box_current_two, boxdash_current_two)
        box_current_one_numerator,box_current_one_denominator = quotients.splitter(box_current_one[0])
        box_current_two_numerator,box_current_two_denominator = quotients.splitter(box_current_two[0])
        numerator = products.multiply_two_together(box_current_two_denominator,box_current_one_numerator, True)
        denominator = products.multiply_two_together(box_current_two_numerator,box_current_one_denominator, True)
        numerator, denominator = quotients.divide(numerator,denominator, True)
        box = [quotients.assembler(numerator,denominator), products.return_number(box_current_two[1]/box_current_one[1])]
    nice_box = sorting.for_presentation_table(box)
    nice_boxdash = sorting.for_presentation_table(boxdash)
    return box, boxdash, nice_box, nice_boxdash, True


def sum(boxs, dashs):
    big_box  = [boxs, dashs]
    first_time = True
    for function in big_box:
        denominator = ""
        numerators = []
        denominators = []
        coefficients = []
        sum_terms = []
        for term in function:
            coefficients.append(term[1])
            term_numerators, term_denominators = quotients.splitter(term[0])
            numerators.append(term_numerators)
            denominators.append(term_denominators)
        for f_of_x in denominators:
            denominator = products.multiply_two_together(denominator,f_of_x, False)
        for k in range(len(numerators)):
            current_concern = numerators[k]
            for j in range(len(denominators)):
                if j == k:
                    continue
                else:
                    current_concern = products.multiply_two_together(denominators[j], current_concern, False)
            sum_terms.append(current_concern)
        simplified_sum = []
        simplified_coefficients = []
        index = 0
        for term in sum_terms:
            if not term in simplified_sum:
                simplified_sum.append(term)
                simplified_coefficients.append(coefficients[index])
            else:
                simplified_coefficients[simplified_sum.index(term)] += coefficients[index]
            index += 1
        if len(simplified_sum) > 1:
            sum, factor = products.a_sum([[simplified_sum[0], simplified_coefficients[0]],[simplified_sum[1], simplified_coefficients[1]]])
            for i in range(2,len(simplified_sum)):
                sum, factor = products.a_sum([[sum, factor], [simplified_sum[i], simplified_coefficients[i]]])
        else:
            sum = simplified_sum[0]
            factor = simplified_coefficients[0]
        numerator, denominator = quotients.divide(sum, denominator, False)
        if first_time:
            box = [quotients.assembler(numerator,denominator), factor]
            first_time = False
        else:
            boxdash = [quotients.assembler(numerator,denominator), factor]
    return box, boxdash


def generate_boxcode(box):
    boxCode = [["",""],"","","","",""]
    boxCode[0][0] = random.randint(0, 1)

    coin_flip = random.randint(0,1)
    if coin_flip == 0:
        magnitude_shift = 0
    else:
        magnitude_shift = random.randint(1,9)
    boxCode[0][1] = magnitude_shift

    power = random.randint(1,9)
    boxCode[1] = power

    coefficient_table = [1,1,1,2,4,8]
    choice = random.randint(0,5)
    coefficient = coefficient_table[choice]
    boxCode[2] = coefficient

    fifty_fifty = random.randint(0,1)
    if fifty_fifty == 0:
        base = 1
    else:
        base = random.randint(2,8)
    boxCode[3] = base

    boxCode[4] = random.randint(0,8)

    if boxCode[4] != 4:
        divisor_table = [1,1,1,2,4,8]
        divide = random.randint(0,5)
        boxCode[1] = products.return_number(boxCode[1]/divisor_table[divide])

    boxCode[5] = box
    return boxCode
