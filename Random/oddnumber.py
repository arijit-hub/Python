def odd_numbers(starting_number,ending_number):

    if starting_number%2 ==0:
        starting_number=starting_number+1

    sum=0
    i=starting_number
    
    while i<=ending_number:
        sum=sum+i
        i=i+2

    return sum

def odding_numbers(starting_number,ending_number):

    if starting_number%2 ==0:
        starting_number=starting_number+1

    sum=0

    for i in range(starting_number,ending_number+1,2):
        sum=sum+i

    return sum
