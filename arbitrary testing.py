import diff
import copy

table_of_boxes = [[["x",1]],[["",1]]]
table_nice = [["x"],[1]]



for i in range(20):
    box, boxdash, nice_box, nice_boxdash = diff.diff_nice(table_of_boxes[0][0], table_of_boxes[1][0], True)
    table_of_boxes[0].append(box)
    table_of_boxes[1].append(boxdash)
    table_nice[0].append(f"{nice_box[1]}{nice_box[0]}")
    table_nice[1].append(f"{nice_boxdash[1]}{nice_boxdash[0]}")
axioms = copy.copy(table_of_boxes)
max = len(axioms[0])
for k in range(max):
    for j in range(max):
        box, boxdash, nice_box, nice_boxdash = diff.convoluted(table_of_boxes[0][k], table_of_boxes[1][k], table_of_boxes[0][j], table_of_boxes[1][j],1)
        table_of_boxes[0].append(box)
        table_of_boxes[1].append(boxdash)
        table_nice[0].append(f"{nice_box[1]}{nice_box[0]}")
        table_nice[1].append(f"{nice_boxdash[1]}{nice_boxdash[0]}")


for i in range(len(table_nice[0])):
    print(table_nice[0][i])
print(''' 


''')
for i in range(len(table_nice[1])):
    print(table_nice[1][i])



