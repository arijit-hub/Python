def bisect_search_2(L , e):
    '''
    Searches for element e in list L in time complexity of O(logn).
    '''
    def pointer_search(L , e , low , high):
        if high == low:
            return L[low] == e

        mid = (low + high) // 2

        if L[mid] == e:
            return True

        elif e < L[mid]:
            if low == mid:
                return False
            else:
                return pointer_search(L , e , low , mid - 1)
        else:
            if high == mid:
                return False
            else:
                return pointer_search(L , e , mid + 1 , high)

    if len(L) == 0:
        return False
    else:
        return pointer_search(L , e , 0 , len(L) - 1)


print(bisect_search_2([] , 1))
print(bisect_search_2([1] , 2))
print(bisect_search_2([1,2,3,4,5] , 5))