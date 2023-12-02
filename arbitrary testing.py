from Nice import Basic, Exponentials, fraction_logs, fraction_inverse_trig
from Convoluted import convoluted_fractions, convoluted_sum
from interperter import interpret
import random
random.seed(None, 2)


boxCode = [[0,0],1,1,0,0,["x",1]]
for i in range(100):
    dividor = random.randint(1,2)
    boxCode[0][0] = random.randint(0, 1)
    boxCode[0][1] = random.randint(0, 1)
    try:
        boxCode[1] = int(random.randrange(1,8)/dividor)
    except:
        boxCode[1] = random.randrange(1,8)/dividor
    boxCode[2] = random.randint(1, 9)
    boxCode[3] = random.randint(1, 2)
    boxCode[4] = random.randint(0, 8)
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
        boxdash = fraction_logs.logaraithm(boxCode, ["",1])
    elif boxCode[4] == 6:
        boxdash = fraction_inverse_trig.arcsin(boxCode, ["",1])
    elif boxCode[4] == 7:
        boxdash = fraction_inverse_trig.arccos(boxCode, ["",1])
    else: #tan^-1
        boxdash = fraction_inverse_trig.arcctan(boxCode, ["",1])
    result = interpret(boxCode)

    print(f"d/dx of {result[1]}{result[0]} is {boxdash[1]}{boxdash[0]}")
