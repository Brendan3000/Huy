from Nice import Basic, Exponentials, fraction_logs, fraction_inverse_trig
from Convoluted import convoluted_fractions, convoluted_sum
from interperter import interpret
import random
random.seed(None, 2)

table = [[], []]
boxCode = [[0,0],1,1,0,0,["e^2(x)",1]]
for i in range(1,101):
    dividor = random.randint(1,2)
    boxCode[0][0] = random.randint(0, 1)
    boxCode[0][1] = random.randint(0, 1)
    boxCode[0][1] = 0
    boxCode[1] = random.randint(1,8)
    boxCode[2] = random.randint(1, 9)
    boxCode[3] = random.randint(1, 2)
    boxCode[4] = random.randint(0, 8)
    if boxCode[4] == 0:
        boxdash = Basic.power(boxCode, ["e^2(x)", 2])
    elif boxCode[4] == 1:
        boxdash = Basic.sin(boxCode, ["e^2(x)", 2])
    elif boxCode[4] == 2:
        boxdash = Basic.cos(boxCode, ["e^2(x)", 2])
    elif boxCode[4] == 3:
        boxdash = Basic.tan(boxCode, ["e^2(x)", 2])
    elif boxCode[4] == 4:
        boxdash = Exponentials.exponential(boxCode, ["e^2(x)", 2])
    elif boxCode[4] == 5:
        boxdash = fraction_logs.logaraithm(boxCode, ["e^2(x)", 2])
    elif boxCode[4] == 6:
        boxdash = fraction_inverse_trig.arcsin(boxCode, ["e^2(x)", 2])
    elif boxCode[4] == 7:
        boxdash = fraction_inverse_trig.arccos(boxCode, ["e^2(x)", 2])
    else: #tan^-1
        boxdash = fraction_inverse_trig.arcctan(boxCode, ["e^2(x)", 2])
    result = interpret(boxCode)
    if len(boxdash[0][1]) != 0:
        print(i)
        print((f"{result[1]}{result[0]}"))
        print(f"{boxdash[1]}{boxdash[0][0]}/({boxdash[0][1]})")
    else:
        print(i)
        print(f"{result[1]}{result[0]}")
        print(f"{boxdash[1]}{boxdash[0][0]}")
