def key_cubeval_dict(num):

    cube_dict = {}
    for i in range(1 , num + 1):
        cube_dict[i] = i * i * i
    return cube_dict

num = int(input('Enter number of terms : '))
print(key_cubeval_dict(num))