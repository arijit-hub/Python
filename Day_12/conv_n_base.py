def DectoNBase(n , num):
    r = ''
    n_base = {}
    letter = 'A'
    for i in range(36):
        if i < 10:
            n_base[i] = i
        else:
            n_base[i] = letter
            letter = chr(ord(letter) + 1)
    print(n_base)
    while num != 0:
        r = str(n_base[num % n]) + r
        num = num // n

    print(r)
    
    
