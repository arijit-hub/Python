def sum_of_even(start_number,end_number):

    sum=0

    if start_number%2==0:
        i=start_number

    else:
        i=start_number+1

    while i<=end_number:
        sum=sum+i
        i=i+2

    return sum

def even_start(start,end):

    result=0

    if start%2==0:
        start=start

    else:
        start=start+1

    for res in range(start,end+1,2):

        result=result+res

    return result

def increment_items(L, increment):
    i = 0
    while i < len(L):
        L[i] = L[i] +increment
        i=i+1
