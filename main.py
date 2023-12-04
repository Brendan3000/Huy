from Nice import Basic, Exponentials, fraction_logs, fraction_inverse_trig
from Convoluted import convoluted_fractions, convoluted_sum
from interperter import interpret
import random
random.seed(None, 2)

#create vareints: power 1, negative power, negative root, negative root & exponential, positive power, positive root, positive root and power
#create Gen1, put everything below into a function so that a list can be spit out for later use

def GenerateBoxCode(innerbox): #innerbox is in form ["value", "derivative"] and is passed straight through
    boxCode = [[0, 0], 1, 1, 0, 0, [innerbox[0], 1]]
    dividor = random.randint(1, 2)
    boxCode[0][0] = random.randint(0, 1)
    boxCode[0][1] = random.randint(0, 1)
    boxCode[1] = random.randrange(-8, 8, 1) / dividor
    boxCode[2] = random.randint(1, 9)
    boxCode[3] = random.randint(1, 9)
    boxCode[4] = random.randint(0, 8)

    if boxCode[1] == 0:
        boxCode[1] = 1

    if (boxCode[1] / 0.5) % 2 == 0:
        boxCode[1] = int(boxCode[1])

    return [boxCode, innerbox]


def GenBox():

    gen1list = []
    deapth = 1
    for i in range(1): #100 is a placeholder

        #previous values of [box str, boxdash str]
        boxAndDash = GenerateBoxCode(["x^2", "2x"])



        if boxAndDash[0][4] == 0:
            boxdash = Basic.power(boxAndDash[0], [boxAndDash[1][1],1])
        elif boxAndDash[0][4] == 1:
            boxdash = Basic.sin(boxAndDash[0], [boxAndDash[1][1],1])
        elif boxAndDash[0][4] == 2:
            boxdash = Basic.cos(boxAndDash[0], [boxAndDash[1][1],1])
        elif boxAndDash[0][4] == 3:
            boxdash = Basic.tan(boxAndDash[0], [boxAndDash[1][1],1])
        elif boxAndDash[0][4] == 4:
            boxdash = Exponentials.exponential(boxAndDash[0], [boxAndDash[1][1],1])
        elif boxAndDash[0][4] == 5:
            boxdash = fraction_logs.logaraithm(boxAndDash[0], [boxAndDash[1][1],1])
        elif boxAndDash[0][4] == 6:
            boxdash = fraction_inverse_trig.arcsin(boxAndDash[0], [boxAndDash[1][1],1])
        elif boxAndDash[0][4] == 7:
            boxdash = fraction_inverse_trig.arccos(boxAndDash[0], [boxAndDash[1][1],1])
        else: #tan^-1
            boxdash = fraction_inverse_trig.arcctan(boxAndDash[0], [boxAndDash[1][1],1])


        result = interpret(boxAndDash[0])
        gen1list.append([result, boxdash])

        print(f"{result[1]}{result[0]}", boxdash)
    return gen1list


GenBox()




