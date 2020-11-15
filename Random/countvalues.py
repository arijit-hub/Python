def count_values(d):
    result=0
    for k in d:
        if d[k] in d:
            result=result+1
    return result
