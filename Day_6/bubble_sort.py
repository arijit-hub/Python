def bub_sort(L):
    '''
    Bubble sorting the list L with time complexity of O(n^2).
    '''
    swap = False
    while not swap:
        swap = True
        for i in range(1 , len(L)):
            if L[i - 1] > L[i]:
                swap = False
                temp = L[i]
                L[i] = L[i - 1]
                L[i - 1] = temp

    return L

print(bub_sort([6,3,1,5,9,2]))