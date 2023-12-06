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
    result = interpret(boxCode)
    co, cop = result[1], boxdash[1]
    if result[1] == 1:
        co = ""
    if result[1] == -1:
        co = "-"
    if boxdash[1] == 1:
        cop = ""
    if boxdash[1] == -1:
        cop = "-"
    if len(boxdash[0][1]) != 0:
        print(i)
        print((f"{co}{result[0]}"))
        print(f"{cop}{boxdash[0][0]}/({boxdash[0][1]})")
    else:
        print(i)
        print(f"{co}{result[0]}")
        print(f"{cop}{boxdash[0][0]}")



