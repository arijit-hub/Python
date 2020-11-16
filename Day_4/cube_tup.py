import math
def tup_cube(num_terms):

    cube_list = list()
    for i in range(1 , num_terms + 1):
        cube_list.append(int(math.pow(i , 3)))

    return tuple(cube_list)

print(tup_cube(15))