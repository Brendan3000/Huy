from Nice import Brackets

def return_number(string):
    if not "." in string:
        return int(string)
    else:
        integer = True
        for letter in string[string.find(".")+1:]:
            if letter != "0":
                integer = False
    if integer:
        return int(string[:string.find(".")])
    else:
        return float(string)



# will turn 2x into "x" and 2, 2sin(x) into "sin(x)",2
def factor_seperator(box_v):
    index_counter = 0
    for letter in  box_v:
        if letter == "-" or letter == "." or letter.isdigit():
            index_counter += 1
        else:
            break
    if index_counter == 0:
        return box_v, 1
    if index_counter == 1:
        if box_v[0] == "-":
            return box_v[1:], -1
        else:
            return box_v[1:], return_number(box_v[:1])
    else:
        return box_v[index_counter:], return_number(box_v[:index_counter])


# Provides the index of the next time brackets were closed
def next_closed_bracket(box_v):
    counter_a = 0
    i = 0
    for letter in box_v:
        if letter =="(":
            counter_a += 1
        if letter == ")":
            counter_a -= 1
        if counter_a == 0:
            break
        i += 1
    return i


# will return true if brackets are not closed
def is_closed_in(box_v):
    counter_a = 0
    i = 0
    for letter in box_v:
        if letter =="(":
            counter_a += 1
        if letter == ")":
            counter_a -= 1
    if counter_a == 0:
        return False
    else:
        return True


# input is a box, ouptut is box with exponetials removed and the power of the exponetial if it were to base e
def exponetial_remover(box_v):
    letter_index = 0
    for letter in box_v:
        if letter == "e" and not is_closed_in(box_v[letter_index:]):
            exponent = box_v[letter_index+3:box_v.rfind(")")]
            exponent, factor = factor_seperator(exponent)
            box_v = box_v[:letter_index]
            return box_v, [exponent, factor]
        elif letter == ")" and not is_closed_in(box_v[letter_index+1:]) and box_v[box_v[:letter_index].rfind("(")+1:letter_index].isdigit():
            base = box_v[box_v[:letter_index].rfind("(")+1:letter_index]
            exponent = box_v[letter_index+3:box_v.rfind(")")]
            exponent, factor = factor_seperator(exponent)
            box_v = box_v[:box_v[:letter_index].rfind("(")]
            if Brackets.closed(exponent) or Brackets.dealing_with_exponentials(exponent):
                pass
            else:
                exponent = "(" + exponent + ")"
            return box_v,[f"ln({base}){exponent}", factor]
        letter_index += 1
    return box_v, ["", 1]


# will factorise multiples
def factoriser(box_one,box_two):
    letter_index = 0


        letter_index +=1


