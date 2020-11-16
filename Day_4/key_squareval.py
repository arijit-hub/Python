def make_dict(num):

    integral_dict = {}
    for i in range(1 , num + 1):
        integral_dict[i] = i * i
    return integral_dict

num = int(input('Enter the number of terms you want in your dictionary : '))
print(make_dict(num))
