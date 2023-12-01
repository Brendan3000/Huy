box_variable = "sin(x^2 + x^3)cos(x^2)"
index_of_first_x = box_variable.find("x")
print(index_of_first_x)
nearest_close_bracket = box_variable[index_of_first_x:].find(")") + index_of_first_x
print(nearest_close_bracket)
nearest_open_bracket = box_variable[:index_of_first_x].rfind("(")
print(nearest_open_bracket)
print(box_variable.count("x"))
print(box_variable[nearest_open_bracket:nearest_close_bracket].count("x"))
if box_variable.count("x") == box_variable[nearest_open_bracket:nearest_close_bracket].count("x"):
    print("True")

