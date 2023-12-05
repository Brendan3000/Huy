from Nice import Basic, Exponentials, fraction_logs, fraction_inverse_trig
from Convoluted import convoluted_fractions, convoluted_sum
from interperter import interpret
import random
from sums import Sum
random.seed(None, 2)

#below may incorrect
#after generating one 'function' I can chose to do 4 things, 1 encapsulate it further using another function, 2 put in a sum, 3 product, 4 quotient. 2,3,4 all require me to fill in the remaining spots
#I will fillin the remaining spots by doing an identical generation, however to avoid infinite bullshit, i will pass down a variable limiting the number of recalls which when = 0 will just
hardcap = 4 # this is the limiting variable's initial value mentioned above, currently set to 1, to be manualy changed. UPDATE, THIS NOW IS A GENERAL DISTANCE FROM ORIGINAL POINT, I'LL JUST INCREAS ETHE CHANCE OF GETTING 1 LOL lolLLOOLLOL
maxsumsize = 3

def GenerateBoxCode(innerbox): #innerbox is in form ["value", "derivative"] and is passed straight through, inner box is what rests in place of "x"
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

#find a way so genbox can call genfullfunction and etc https://stackoverflow.com/questions/71473962/how-do-i-make-functions-call-each-other god help me
def GenBox(masterFuncType, cd, box, boxdash): #pass in variable 1,2,3,4 see above, if 2,3,4 then ignore the specified function and place it into a sum,product,quotient ||| cap is current value of hardcap, reduces with each 2,3,4 called

    if masterFuncType == 1:

        #previous values of [box str, boxdash str]
        boxAndDash = GenerateBoxCode([box, boxdash])

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
        return [f"(({result[1]})({result[0]}))", f"((l({boxdash[0][0]})/({boxdash[0][1]}))({boxdash[1]}))"]

    elif masterFuncType == 2: #sum
        #call this function n times more
        nterms = random.randint(1, 3)
        terms = []
        for i in range(nterms):
            terms.append(GenFullFunction(cd-1))

        sumobj = Sum(terms)
        return sumobj.strout()
    elif masterFuncType == 3: #product
        print("Wrong way : Turn Back") #not implemented yet
    elif masterFuncType == 4: #quotient
        print("Wrong way : Turn Back") #not implemented yet






#commence generation

#make this a function where you request n depth of code and it returns a box and boxdash as strings, this'll allow recursion
def GenFullFunction(depth):
    GenBoxOut = GenBox(1, 6969, "x", "1")#current deapth doesn't matter for this function call
    random.randint(1, 2)#currently equal chance of sum and regular function
    for currentDeapth in range(depth,0,-1): #end exlcusive therefore 1 is lowest value, if 1 then pass in 1 as masterfunctype otherwise random

        masterfunc = random.randint(1, 2)
        if(currentDeapth == 1):
            masterfunc = 1

        GenBoxOut = GenBox(masterfunc, currentDeapth, GenBoxOut[0], GenBoxOut[1])

    return[GenBoxOut[0], GenBoxOut[1]]




print(GenFullFunction(1)) # 0 is lowest value




#make powers more common