def are_lengths_of_strs(L1, L2):
    '''(list of int, list of str) -> bool
  
    Return True if and only if all the ints in L1 are the lengths of the strings
    in L2 at the corresponding positions.

    Precondition: len(L1) == len(L2)

    >>> are_lengths_of_strs([4, 0, 2], ['abcd', '', 'ef'])
    True
    '''

    result = True
    for i in range(len(L1)):
        if L1[i]!=len(L2[i]):
            result = False

    return result

def double_values(collection):
    for v in range(len(collection)):
         collection[v] = collection[v] * 2

def get_negative_nonnegative_lists(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the negative ints in the
    inner lists of L and the second item is a list of the non-negative ints
    in those inner lists.

    Precondition: the number of rows in L is the same as the number of
    columns.

    >>> get_negative_nonnegative_lists([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]])
    ([-1, -4], [3, 5, 2, 5, 4, 0, 8])
    '''

    nonneg = []
    neg = []
    for row in range(len(L)):
        for col in range(len(L)):
            # CODE MISSING HERE
            if L[row][col] > 0:
                nonneg.append(L[row][col])
            else:
                neg.append(L[row][col])

    return (neg, nonneg)

def add_to_letter_counts(d, s):
    '''(dict of {str: int}, str) -> NoneType

    d is a dictionary where the keys are single-letter strings and the values
    are counts.

    For each letter in s, add to that letter's count in d.

    Precondition: all the letters in s are keys in d.

    >>> letter_counts = {'i': 0, 'r': 5, 'e': 1}
    >>> add_to_letter_counts(letter_counts, 'eerie')
    >>> letter_counts
    {'i': 1, 'r': 6, 'e': 4}
    '''

    for c in s:
        d[c]=d[c]+1
        # CODE MISSING HERE

    return d
