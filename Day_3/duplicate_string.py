def dup_ch(inserted_str):
    dup = []
    for i in range(len(inserted_str)):
        count = inserted_str.count(inserted_str[i])
        if(count > 1):
            if inserted_str[i] not in dup:
                dup.append(inserted_str[i])

    return dup

inserted_str = input('Enter the string : ')
dup = dup_ch(inserted_str)
print(dup)