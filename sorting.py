import number_theory
import quotients


def for_presentation_table(box, boxdash):
    box = number_theory.float_to_fraction(box)
    boxdash = number_theory.float_to_fraction(boxdash)
    can_we_release_the_numerator_box = False
    can_we_release_the_numerator_boxdash = False
    if box[1] == 1:
        box[1] = ""
        can_we_release_the_numerator_box = True
    if box[1] == -1:
        box[1] = "-"
    if boxdash[1] == 1:
        boxdash[1] = ""
        can_we_release_the_numerator_boxdash = True
    if boxdash[1] == -1:
        boxdash[1] = "-"
    box[0] = quotients.double_brackets_remover(box[0],can_we_release_the_numerator_box)
    boxdash[0] = quotients.double_brackets_remover(boxdash[0], can_we_release_the_numerator_boxdash)
    return box, boxdash
