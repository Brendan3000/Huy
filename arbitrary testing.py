import random

import diff

table_of_boxes = [[["x",1]],[["",1]]]
table_nice = [["x"],[1]]

for i in range(30):
    box, boxdash, nice_box, nice_boxdash = diff.diff_nice(table_of_boxes[0][0], table_of_boxes[1][0], True)
    table_of_boxes[0].append(box)
    table_of_boxes[1].append(boxdash)
    table_nice[0].append(nice_box)
    table_nice[1].append(nice_boxdash)
for i in range(20):
    box, boxdash, nice_box, nice_boxdash = diff.diff_nice(table_of_boxes[0][0], table_of_boxes[1][0], False)
    table_of_boxes[0].append(box)
    table_of_boxes[1].append(boxdash)
    table_nice[0].append(nice_box)
    table_nice[1].append(nice_boxdash)
max = len(table_of_boxes[0])
for k in range(max):
    for j in range(0,max,15):
        for i in range(1,4):
            box, boxdash, nice_box, nice_boxdash, work = diff.convoluted(table_of_boxes[0][k], table_of_boxes[1][k], table_of_boxes[0][j],table_of_boxes[1][j], i)
            if box[0].count("(") != box[0].count(")"):
                work = False
            if boxdash[0].count("(") != boxdash[0].count(")"):
                work = False
            if work and len(box[0]) > 0:
                table_of_boxes[0].append(box)
                table_of_boxes[1].append(boxdash)
                table_nice[0].append(f"{nice_box}")
                table_nice[1].append(f"{nice_boxdash}")
    work = True
    box, boxdash, nice_box, nice_boxdash = diff.diff_nice(table_of_boxes[0][k], table_of_boxes[1][k], False)
print(len(table_nice[0]))
print("done")







for i in range(2000):
    weight_table = [0,0,0,1,1,2,0,0,3,3,4]
    path = weight_table[random.randint(0,10)]
    add_to_nice = True
    if path == 0:
        choice = random.randint(0, (len(table_of_boxes[0])-1)//10)
        box_current, box_dash_current = table_of_boxes[0][choice], table_of_boxes[1][choice]
        box, boxdash, nice_box, nice_boxdash = diff.diff_nice(box_current, box_dash_current, False)
        work = True
    if 0 < path < 4:
        if path != 2:
            choice_one = random.randint(0, (len(table_of_boxes[0])-1)//10)
            box_current_one, box_dash_current_one = table_of_boxes[0][choice_one], table_of_boxes[1][choice_one]
            choice_two = random.randint(0, (len(table_of_boxes[0])-1)//10)
            box_current_two, box_dash_current_two = table_of_boxes[0][choice_two], table_of_boxes[1][choice_two]
        else:
            choice_one = random.randint(0, (len(table_of_boxes[0])-1)//25)
            box_current_one, box_dash_current_one = table_of_boxes[0][choice_one], table_of_boxes[1][choice_one]
            choice_two = random.randint(0, (len(table_of_boxes[0])-1)//25)
            box_current_two, box_dash_current_two = table_of_boxes[0][choice_two], table_of_boxes[1][choice_two]
        box, boxdash, nice_box, nice_boxdash, work = diff.convoluted(box_current_one,box_dash_current_one,box_current_two,box_dash_current_two, path)
    if path == 4:
        add_to_nice = False
        work = True
        number_of_terms = random.randint(2,3)
        choice_one = random.randint(0, (len(table_of_boxes[0])-1)//50)
        box_current_one, box_dash_current_one = table_of_boxes[0][choice_one], table_of_boxes[1][choice_one]
        choice_two = random.randint(0, (len(table_of_boxes[0])-1)//50)
        box_current_two, box_dash_current_two = table_of_boxes[0][choice_two], table_of_boxes[1][choice_two]
        choice_three = random.randint(0, (len(table_of_boxes[0])-1)//50)
        box_current_three, box_dash_current_three = table_of_boxes[0][choice_three], table_of_boxes[1][choice_three]
        if number_of_terms == 2:
            box, boxdash = diff.sum([box_current_one,box_dash_current_two],[box_dash_current_one,box_dash_current_two])
        else:
            box, boxdash = diff.sum([box_current_one,box_dash_current_two,box_dash_current_three],[box_dash_current_one,box_dash_current_two,box_dash_current_three])
    if box[0].count("(") != box[0].count(")"):
        work = False
    if boxdash[0].count("(") != boxdash[0].count(")"):
        work = False
    if work and len(box[0]) > 0:
        table_of_boxes[0].append(box)
        table_of_boxes[1].append(boxdash)
    if add_to_nice and work and len(box[0]) > 0:
        table_nice[0].append(nice_box)
        table_nice[1].append(nice_boxdash)






for i in range(1000):
    print(table_nice[0][i])

print('''

Mind the gap

''')

for i in range(1000):
    print(table_nice[1][i])





