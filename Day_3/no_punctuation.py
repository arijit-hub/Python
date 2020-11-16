def punc_removed(input_str):
    punctuations = '!,.:;?\'\"'
    non_punc = ''
    for i in range(len(input_str)):
        if input_str[i] not in punctuations:
            non_punc = non_punc + input_str[i]
    return non_punc

input_str = input('Enter your string : ')
print(punc_removed(input_str))