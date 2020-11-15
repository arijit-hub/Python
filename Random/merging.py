def make_pairs(list1, list2):

    pairs = []

    inner_list = []
    for i in range(len(list1)):
        inner_list.append(list1[i])
        inner_list.append(list2[i])
        pairs.append(inner_list)

    return pairs

    

def contains(value, lst):

    found = False  # We have not yet found value in the list.

    for i in range(len(lst)):
        for j in range(len(lst[i])):
            found = (lst[i][j] == value)

    return found
