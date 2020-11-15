def shift_left(list):

    for i in range(0,len(list)-1):
        temporary=list[i]
        list[i]=list[i+1]
        list[i+1]=temporary

    print(list)
        
