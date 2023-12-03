import string
from interperter import interpret

class Sum: #UNTESTED
    def __init__(self, interms): #interms/terms is a list of boxes&boxdashes in form [[box,boxdash],...] where boxdash is a string and box is ALSO A STRING
        self.terms = interms

#-----------------will have to be adapted for denominators when they happen---------------------
    def strout(self): #returns out boxes as string and boxdashes as string in form [str,str]
        #do simplification stuff if needed
        boxsignlist=[] #0 is first term etc
        boxdashsignlist=[] #0 is first term etc

        for term in self.terms:
            for char in term[0]:
                if string.isspace(char):
                    continue
                elif char == "-":
                    boxsignlist.append("-");
                    term[0].replace("-", "", 1)
                else:
                    boxsignlist.append("+");

            #parse string because we're storing the boxdash as a string, mashallah this works out
            for char in term[1]:
                if string.isspace(char):
                    continue
                elif char == "-":
                    boxdashsignlist.append("-");
                    term[0].replace("-", "", 1)
                else:
                    boxdashsignlist.append("+");


        #search for positives and place that first and set it's corresponding "+" to a ""
        #to do

        returnbox = "";
        returnboxdash = "";

        for i in range(len(self.terms)):
            returnbox.append(f"{boxsignlist[i]}{self.terms[i][0]}")
            returnboxdash.append(f"{boxdashsignlist[i]}{self.terms[i][1]}")

        return [returnbox, returnboxdash]

#ideally checks if result is an integer, ie. box_v ==0 and adds the values if result is an integer (99% sure  DOESNT WORK) 
def sums (box_v, box_c):
  result = box_v + box_c
  if isinstance(result, int):
    print(result)   
  else:
    print(sum(result))

# List of common factors to check for factorising 
def factor_check([box_c]{box_v}):
    factors = [
        f'sin([box_c]{box_v})', f'ln([box_c]{box_v})', f'tan([box_c]{box_v})', f'cos([box_c]{box_v})',
        f'arccos([box_c]{box_v})', f'arcsin([box_c]{box_v})', f'arctan([box_c]{box_v})', f'e**([box_c]{box_v})', f'x**([box_c]{box_v})', f'(base)**([box_c]{box_v})
    ]

    for factor in factors:
        if factor in str([box_c]{box_v}):
            return factor

    return None
  
def factorize([box_c]{box_v}):
    factors = [
        f'sin([box_c]{box_v})', f'ln([box_c]{box_v})', f'tan([box_c]{box_v})', f'cos([box_c]{box_v})',
        f'arccos([box_c]{box_v})', f'arcsin([box_c]{box_v})', f'arctan([box_c]{box_v})', f'e**([box_c]{box_v})', f'x**([box_c]{box_v})'
    ]

    for factor in factors:
        if factor in str([box_c]{box_v}):
            common_factor = factor
  # Attempting to factorize by dividing the expression by the common factor
            expression = str([box_c]{box_v}).replace(common_factor, '')  
            if expression.startswith('*'):  
                expression = expression[1:] 

            return expression.strip()  
    
    return str([box_c]{box_v})  
