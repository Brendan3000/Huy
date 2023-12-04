import math

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


def real_math(word)
    while "e^" in word:
        word.replace("e^", "math.exp")
    while "^" in word:
        word.replace("^", "**")
    while "tan^" in word:
        word.replace("tan", "math.tan")
    while "cos" in word:
        word.replace("cos", "math.cos")
    while "sin" in word:
        word.replace("sin", "math.sin")
    while "arctan" in word:
        word.replace("arctan", "1*math.atan")
    while "arccos" in word:
        word.replace("arccos", "math.acos")
    while "arcsin" in word:
        word.replace("arcsin", "math.asin")
    while "ln" in word:
        word.replace("ln", "math.log" )
    while "log" in word:
        index = word.find("log")
        index_bracket_open = index + word[word.find("log"):].find("(")
        index_bracket_close = index + word.find("(") + next_closed_bracket(word[index_bracket_open:])
        box = word[index_bracket_open+1:index_bracket_close]
        base = word[index + 4:index_bracket_open]
        word.replace(word[index:index_bracket_close+1],f"math.log({base})*math.log({box})")
    for x =
    try:
        while "x" in word
            word.replace("x")






