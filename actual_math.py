import math
import random
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


def real_math(word):
    while "x" in word:
        word = word.replace("x", "0")
    while "e^" in word:
        word = word.replace("e^", "math.exp")
    while "^" in word:
        word = word.replace("^", "**")
    while "arctan" in word:
        word = word.replace("arctan", "math.atom")
    while "arccos" in word:
        word = word.replace("arccos", "math.acop")
    while "arcsin" in word:
        word = word.replace("arcsin", "math.asup")
    while "tan" in word:
        word = word.replace("tan", "math.tun")
    while "cos" in word:
        word = word.replace("cos", "math.cus")
    while "sin" in word:
        word = word.replace("sin", "math.sun")

    while "atom" in word:
        word = word.replace("atom", "atan", )
    while "acop" in word:
        word = word.replace("acop", "acos")
    while "asup" in word:
        word = word.replace("asup", "asin")
    while "tun" in word:
        word = word.replace("tun", "tan")
    while "cus" in word:
        word = word.replace("cus", "cos")
    while "sun" in word:
        word = word.replace("sun", "sin")

    while "log" in word:
        index = word.find("log")
        index_bracket_open = index + word[word.find("log"):].find("(")
        index_bracket_close = index + word.find("(") + next_closed_bracket(word[index_bracket_open:])
        box = word[index_bracket_open+1:index_bracket_close]
        base = word[index + 4:index_bracket_open-1]
        word = word.replace(word[index:index_bracket_close+1],f"math.james({base})*math.james({box})")
    while "james" in word:
        word = word.replace("james", "log")
    while "ln" in word:
        word = word.replace("ln", "math.log" )
    f_of_zero = eval(word)
    return f_of_zero

