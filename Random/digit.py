def common_char(s1,s2):

    res=''

    for character in s1:
        if character in s2:
            res=res+character

    return res
