from Nice import Basic, Exponentials, fraction_logs, fraction_inverse_trig
from Convoluted import convoluted_fractions, convoluted_sum
from interperter import interpret
import random
random.seed(None, 2)


boxCode = [[0,0],1,1,0,0,["x^2",1]]
for i in range(100):
    dividor = random.randint(1,2)
    boxCode[0][0] = random.randint(0, 1)
    boxCode[0][1] = random.randint(0, 1)
    number = random.randint(1,8)
    boxCode[2] = random.randint(1, 9)
    boxCode[3] = random.randint(1, 2)
    boxCode[4] = random.randint(0, 8)
    if boxCode[4] == 0:
        boxdash = Basic.power(boxCode, ["x",2])
    elif boxCode[4] == 1:
        boxdash = Basic.sin(boxCode, ["x",2])
    elif boxCode[4] == 2:
        boxdash = Basic.cos(boxCode, ["x",2])
    elif boxCode[4] == 3:
        boxdash = Basic.tan(boxCode, ["x",2])
    elif boxCode[4] == 4:
        boxdash = Exponentials.exponential(boxCode, ["x",2])
    elif boxCode[4] == 5:
        boxdash = fraction_logs.logaraithm(boxCode, ["x",2])
    elif boxCode[4] == 6:
        boxdash = fraction_inverse_trig.arcsin(boxCode, ["x",2])
    elif boxCode[4] == 7:
        boxdash = fraction_inverse_trig.arccos(boxCode, ["x",2])
    else: #tan^-1
        boxdash = fraction_inverse_trig.arcctan(boxCode, ["x",2])
    result = interpret(boxCode)

    print(f"d/dx of {result[1]}{result[0]} is {boxdash[1]}{boxdash[0]}")
