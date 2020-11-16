def even_in_tup(tup):
    even_tup = list()
    for i in range(len(tup)):
        if tup[i] % 2 == 0:
            even_tup.append(tup[i])

    return tuple(even_tup)

print(even_in_tup((12,7,38,56,78)))