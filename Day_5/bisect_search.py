def bisection_search(L  ,e):
    '''
    Searches for element e in list L in time complexity of O(n).
    '''
    if L == []:
        return False
    if(len(L) == 1):
        return L[0] == e
    half = len(L) // 2
    if(e > half):
        return bisection_search(L[half:] , e)
    elif(e < half):
        return bisection_search(L[:half] , e)


print(bisection_search([] , 1))
print(bisection_search([1] , 2))
print(bisection_search([1,2,3,4,5] , 5))