def where_is_max():
    largest  = None
    smallest = None

    while True:

        inp = input('Enter a Number else enter done to quit')

        if inp == 'done':
            break

        try:
            number = int(inp)

            if smallest == None and largest == None:
                smallest = number
                largest = number

            elif number < smallest:
                smallest = number

            elif number > largest:
                largest = number
        except:
            print('Invalid Input')

        

    print('Max is', largest)
    print('Min is' , smallest)


