def get_median(arr1 , arr2):
    
    arr1.extend(arr2)

    arr1.sort()

    if (len(arr1) % 2 == 0):
        med1 = arr1[len(arr1) // 2]
        med2 = arr1[(len(arr1) // 2) - 1]
        med = (med1 + med2) / 2
        return med
    
    else:
        return arr1[len(arr1) // 2]



a = [1,5,6]
b = [2,3,4]

print(get_median(a , b))