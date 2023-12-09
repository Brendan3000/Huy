import random
import diff
import copy
import sorting

table_of_boxes = [[["x",1]],[["",1]]]
table_nice = [["x"],[1]]



for i in range(30):
    box, boxdash, nice_box, nice_boxdash = diff.diff_nice(table_of_boxes[0][0], table_of_boxes[1][0], True)
    table_of_boxes[0].append(box)
    table_of_boxes[1].append(boxdash)
    table_nice[0].append(f"{nice_box}")
    table_nice[1].append(f"{nice_boxdash}")
# axioms = copy.copy(table_of_boxes)
# max = len(axioms[0])
# for k in range(max):
#     for j in range(max):
#         for m in range(max):
#             box, boxdash = diff.sum([table_of_boxes[0][k], table_of_boxes[0][j], table_of_boxes[0][m]], [table_of_boxes[1][k],table_of_boxes[1][j], table_of_boxes[1][m]])
#         table_of_boxes[0].append(box)
#         table_of_boxes[1].append(boxdash)
#         nice_box, nice_boxdash = sorting.for_presentation_table(box,boxdash)
#         table_nice[0].append(f"{nice_box[1]}{nice_box[0]}")
#         table_nice[1].append(f"{nice_boxdash[1]}{nice_boxdash[0]}")


for i in range(800):
    weight_table = [0,0,0,0,1,1,1,2,2,3,3,3,4]
    path = weight_table[random.randint(0,11)]
    try:
        add_to_nice = True
        if path == 0:
            choice = random.randint(0, len(table_of_boxes[0])-1)
            box_current, box_dash_current = table_of_boxes[0][choice], table_of_boxes[1][choice]
            box, boxdash, nice_box, nice_boxdash = diff.diff_nice(box_current, box_dash_current, False)
            work = True
        if 0 < path < 4:
            if path != 2:
                choice_one = random.randint(0, len(table_of_boxes[0])-1)
                box_current_one, box_dash_current_one = table_of_boxes[0][choice_one], table_of_boxes[1][choice_one]
                choice_two = random.randint(0, len(table_of_boxes[0])-1)
                box_current_two, box_dash_current_two = table_of_boxes[0][choice_two], table_of_boxes[1][choice_two]
            else:
                choice_one = random.randint(0, (len(table_of_boxes[0])-1)//10)
                box_current_one, box_dash_current_one = table_of_boxes[0][choice_one], table_of_boxes[1][choice_one]
                choice_two = random.randint(0, (len(table_of_boxes[0])-1)//10)
                box_current_two, box_dash_current_two = table_of_boxes[0][choice_two], table_of_boxes[1][choice_two]
            box, boxdash, nice_box, nice_boxdash, work = diff.convoluted(box_current_one,box_dash_current_one,box_current_two,box_dash_current_two, path)
        if path == 4:
            add_to_nice = False
            work = True
            number_of_terms = random.randint(2,3)
            choice_one = random.randint(0, (len(table_of_boxes[0])-1)//25)
            box_current_one, box_dash_current_one = table_of_boxes[0][choice_one], table_of_boxes[1][choice_one]
            choice_two = random.randint(0, (len(table_of_boxes[0])-1)//25)
            box_current_two, box_dash_current_two = table_of_boxes[0][choice_two], table_of_boxes[1][choice_two]
            choice_three = random.randint(0, (len(table_of_boxes[0])-1)//25)
            box_current_three, box_dash_current_three = table_of_boxes[0][choice_three], table_of_boxes[1][choice_three]
            if number_of_terms == 2:
                box, boxdash = diff.sum([box_current_one,box_dash_current_two],[box_dash_current_one,box_dash_current_two])
            else:
                box, boxdash = diff.sum([box_current_one,box_dash_current_two,box_dash_current_three],[box_dash_current_one,box_dash_current_two,box_dash_current_three])
        if work:
            table_of_boxes[0].append(box)
            table_of_boxes[1].append(boxdash)
        if add_to_nice and work:
            table_nice[0].append(f"{nice_box}")
            table_nice[1].append(f"{nice_boxdash}")
        print(i)
    except:
        pass

for i in range(len(table_nice[0])):
    print(table_nice[0][i])
print(''' 


''')
for i in range(len(table_nice[1])):
    print(table_nice[1][i])



