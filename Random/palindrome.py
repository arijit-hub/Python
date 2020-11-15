def is_palindrome(s):

    """(str) -> bool
    Returns True if and only if s is palindrome.

    >>> is_palindrome('neon')
    False
    
    >>> is_palindrome('sms')
    True
    """

    i = 0
    j = len(s) - 1

    while i < j and s[i] == s[j]:
        i = i + 1
        j = j - 1

    return i>=j

import doctest
doctest.testmod()
