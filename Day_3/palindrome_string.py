def pal_string(input_string):
    reverse_string = input_string[::-1]
    if input_string == reverse_string:
        print('The String is Palindrome!')
    else:
        print('The String is NOT-Palindrome!')

input_string = input('Enter the string you want to check : ')
pal_string((input_string))