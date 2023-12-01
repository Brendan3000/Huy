box_variable =
index_of_first_x = box_variable.fin("x")
print(index_of_first_x)
nearest_close_bracket = box_variable[index_of_first_x:].fin(")")
print(nearest_close_bracket)
nearest_open_bracket = box_variable[:index_of_first_x].rfin("(")
print(nearest_open_bracket)
if box_variable.count("x") == box_variable[nearest_open_bracket:nearest_close_bracket].count("x"):
