def gcd(input_num):
    """
    (list of int) -> int

    Returns the gcd of the numbers in the list input_num.

    >>>gcd([24,60,48,108])
    12
    """

    min_num = min(input_num)
    print(min_num)
    gcd_val = 1
    for i in range(2, min_num + 1):
        if min_num % i == 0:
            for j in range(len(input_num) - 1):
                if(input_num[j] % i != 0):
                    break
            if j == len(input_num):
                gcd_val = i
    return gcd_val


if __name__ == '__main__':
    input_num = []
    n = int(input("Enter how many numbers you want to enter:"))
    for i in range(n):
        entered_num = int(input()) 
        input_num.append(entered_num)

    gcd_value = gcd(input_num)
    print('GCD is' , gcd_value)
