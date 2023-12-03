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
                else:
                    boxsignlist.append("+");

            #parse string because we're storing the boxdash as a string, mashallah this works out
            for char in term[1]:
                if string.isspace(char):
                    continue
                elif char == "-":
                    boxdashsignlist.append("-");
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


