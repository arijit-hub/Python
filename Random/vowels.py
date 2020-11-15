def number_of_vowels(word):
    '''(str)->str

    Returns number of vowels in the word

    >>>number_of_vowels('arijit')
    'aii'
    '''
    vowel_content=''
    for vowels in word:
        if vowels in 'aeiouAEIOU':
            vowel_content=vowel_content+vowels

    return vowel_content
