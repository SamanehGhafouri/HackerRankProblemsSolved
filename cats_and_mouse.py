# Cats and a Mouse
# Two cats and a mouse are at various positions on a
# line. You will be given their starting positions.
# Your task is to determine which cat will reach the
# mouse first, assuming the mouse does not move and
# \the cats travel at equal speed. If the cats arrive
# at the same time, the mouse will be allowed to move
# and it will escape while they fight.
# If cat A catches the mouse first, print Cat A.
# If cat B catches the mouse first, print Cat B.
# If both cats reach the mouse at the same time, print Mouse C as the two cats fight and mouse escapes.


def cat_and_mouse(cat_a, cat_b, mouse):

    if abs(cat_a - mouse) > abs(cat_b - mouse):
        print("Cat B")
    elif abs(cat_b - mouse) > abs(cat_a - mouse):
        print("Cat A")
    else:
        print("Mouse C")


q = int(input())
for q_itr in range(q):
    xyz = input().split()
    x = int(xyz[0])
    y = int(xyz[1])
    z = int(xyz[2])
    result = cat_and_mouse(x, y, z)
    print(result)
