def largest_odd_number(num_inp):
    odd_inp = []

    for num in num_inp:
        if num % 2 != 0:
            odd_inp.append(num)
    
    if len(odd_inp) == 0:
        print('No odd number!')
    
    else:
        odd_inp.sort()
        print('The largest odd input is :' , odd_inp[-1])

if __name__ == "__main__":
    inp = []

    for i in range(3):
        inp.append(int(input('Enter a number :')))

    largest_odd_number(inp)