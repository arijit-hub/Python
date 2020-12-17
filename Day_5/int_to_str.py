def int_to_str(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    res = ''
    while i > 0:
        res = digits[i % 10] + res
        i = i // 10

    return res


print(int_to_str(10))
