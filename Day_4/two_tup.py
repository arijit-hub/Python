def half_tuple(tup):
    half_len = len(tup) // 2
    tup1 = tup[ : half_len]
    tup2 = tup[half_len : ]

    return tup1, tup2

tup1 , tup2 = half_tuple((1 , 3 , 5 , 7 , 9 , 2 , 4 , 6 , 8))
print(tup1)
print(tup2)