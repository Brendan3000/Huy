from Nice import Basic, Exponentials, fraction_logs, fraction_inverse_trig
from interperter import interpret
import random
random.seed(None, 2)

table = [[],[]]
boxCode = [[0,0],1,1,0,0,["e^(2x) ",4]]
for i in range(1,101):
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
    box = interpret(boxCode)
    print(box)
    if boxCode[4] == 0:
        boxdash = Basic.power(boxCode, ["e^(2x) ", 8])
    elif boxCode[4] == 1:
        boxdash = Basic.sin(boxCode, ["e^(2x) ", 8])
    elif boxCode[4] == 2:
        boxdash = Basic.cos(boxCode, ["e^(2x) ", 8])
    elif boxCode[4] == 3:
        boxdash = Basic.tan(boxCode, ["e^(2x)", 8])
    elif boxCode[4] == 4:
        boxdash = Exponentials.exponential(boxCode, ["e^(2x) ", 8])
    elif boxCode[4] == 5:
        boxdash = fraction_logs.logaraithm(boxCode, ["e^(2x) ", 8])
    elif boxCode[4] == 6:
        boxdash = fraction_inverse_trig.arcsin(boxCode, ["e^(2x) ", 8])
    elif boxCode[4] == 7:
        boxdash = fraction_inverse_trig.arccos(boxCode, ["e^(2x) ", 8])
    else: #tan^-1
        boxdash = fraction_inverse_trig.arcctan(boxCode, ["e^(2x) ", 8])





