from Nice import Basic, Exponentials, fraction_logs, fraction_inverse_trig
from Convoluted import convoluted_fractions, convoluted_sum
from interperter import interpret
import random
random.seed(None, 2)

#create vareints: power 1, negative power, negative root, negative root & exponential, positive power, positive root, positive root and power
#create Gen1, put everything below into a function so that a list can be spit out for later use
def GenBox():
    boxCode = [[0,0],1,1,0,0,["x",0]]
    gen1list = []
    for i in range(100): #100 is a placeholder

        dividor = random.randint(1,2)
        boxCode[0][0] = random.randint(0, 1)
        boxCode[0][1] = random.randint(0, 1)
        boxCode[1] = random.randrange(-8,8,1)/dividor
        boxCode[2] = random.randint(1, 9)
        boxCode[3] = random.randint(1, 9)
        boxCode[4] = random.randint(0, 8)
        boxCode[5][1] = random.randint(1,9)

        if boxCode[4] == 0:
            boxdash = Basic.power(boxCode, ["",1])
        elif boxCode[4] == 1:
            boxdash = Basic.sin(boxCode, ["",1])
        elif boxCode[4] == 2:
            boxdash = Basic.cos(boxCode, ["",1])
        elif boxCode[4] == 3:
            boxdash = Basic.tan(boxCode, ["",1])
        elif boxCode[4] == 4:
            boxdash = Exponentials.exponential(boxCode, ["",1])
        elif boxCode[4] == 5:
            boxdash = fraction_logs.Logarithm(boxCode, ["",1])
        elif boxCode[4] == 6:
            boxdash = fraction_inverse_trig.arcsin(boxCode, ["",1])
        elif boxCode[4] == 7:
            boxdash = fraction_inverse_trig.arccos(boxCode, ["",1])
        else: #tan^-1
            boxdash = fraction_inverse_trig.arcctan(boxCode, ["",1])


        result = interpret(boxCode)
        gen1list.append([result, boxdash])
        print(f"{result[1]}{result[0]}", boxdash)
        return gen1list


GenBox()




