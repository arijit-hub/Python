def grade_it_average(list):

    average_list=[]
    result=0

    for i in range(len(list)):
        for j in range(len(list[i])):
            result=result+j[i]

        average_list.append(result)

    return average_list
