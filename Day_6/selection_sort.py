def select_sort(L):
    '''
    Selection sorting the list L.
    '''
    for i in range(len(L)):
        for j in range(i + 1 , len(L)):
            if L[j] < L[i]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp

    return L
print(select_sort([6,3,1,5,9,2]))
