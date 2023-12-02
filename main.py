from Nice import Basic, Exponentials, fraction_logs, fraction_inverse_trig
from Convoluted import convoluted_fractions, convoluted_sum
from interperter import interpret
import random
random.seed(None, 2)
#create vareints: power 1, negative power, negative root, negative root & exponential, positive power, positive root, positive root and power
#create Gen1, put everything below into a function so that a list can be spit out for later use

boxCode = [[0,0],1,1,0,0,["x",0]]
for i in range(9):


    dividor = random.randint(1,2)
    boxCode[0][0] = random.randint(0, 1)
    boxCode[0][1] = random.randint(0, 1)
    boxCode[1] = random.randrange(-8,8,1)/dividor
    boxCode[2] = random.randint(1, 9)
    boxCode[3] = random.randint(0, 9)
    boxCode[4] = random.randint(0, 8)
    boxCode[5][1] = random.randint(1,9)

    result = interpret(boxCode)
    print(f"{result[1]}{result[0]}")


