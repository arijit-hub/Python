def merge(first, second):
    '''
    Merging first and second sorted lists.
    '''
    result = []
    i, j = 0, 0
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1

    while i < len(first):
        result.append(first[i])
        i += 1

    while j < len(second):
        result.append(second[j])
        j += 1

    return result


def merge_sort(L):
    if len(L) < 2:
        return L

    else:
        mid = len(L) // 2
        first = merge_sort(L[: mid])
        second = merge_sort(L[mid:])
        return merge(first, second)


print(merge_sort([6, 3, 1, 5, 9, 2]))
