def inverting_dictionary(input_dictionary):
    '''(dictionary)->(dictionary)

    Returns a dictionary which has the values of input_dictionary as keys and keys as values.

    >>>inverting_dictionary{'A'='red','B'='green','C'='yellow','D'='green','E'='red','F'='blue'}
    {'red'=['A','E'],'green'=['B','D'],'yellow'=['C'],'blue'=['F']}
    '''
    reverse_dictionary={}
    
    for i in input_dictionary:
        key=input_dictionary[i]
        if key not in reverse_dictionary:
            reverse_dictionary[key]=[i]
        else:
            reverse_dictionary[key].append(i)

    return reverse_dictionary
    
