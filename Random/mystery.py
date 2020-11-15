def mystery(s):
    i = 0
    result = ''

    while not s[i].isdigit():
          result = result + s[i]
          i = i + 1

    return result
def while_version(L):
    """ (list of number) -> number
    """
    i = 0
    total = 0

    while i < len(L) and L[i] % 2 != 0:
         total = total + L[i]
         i = i + 1

    return total

def for_version(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0:
            total = total + num
        found_even = True

    return total
