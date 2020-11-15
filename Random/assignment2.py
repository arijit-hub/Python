def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna):
    """ (str) -> bool

    return True if and only if valid nucleotide is available in DNA secquence dna.

    >>> is_valid_sequence('TACGG')
    True
    >>> is_valid_sequence('AGTACP')
    False
    """
    for char in dna:
        if char not in 'ATCG':
            return False
    return True

def insert_sequences(dna1, dna2, index):
    """ (str, str, int) -> str

    return the DNA sequences obtained by inserting the second DNA sequences into the first DNA sequences at the given index.

    >>> insert_sequences('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequences('ATCG', 'GG', 1)
    'AGGTCG'
    """

    return dna1[:index] + dna2 + dna1[index:]

def get_complement(nucleotide):
    """ (str) -> str

    return the complement of nucleotide in DNA sequences.

    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    """
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'
    else:
        return 'Not a nucleotide'

def get_complementary_sequence(dna):
    """ (str) -> str

    return the complementary sequence of DNA sequence dna.

    >>> get_complementary_sequence('GGTA')
    'CCAT'
    >>> get_complementary_sequence('ACTG')
    'TGAC'
    """
    sequence = ''
    for char in dna:
        if char not in 'ATCG':
            return 'DNA is not valid'
        else:
            sequence = sequence + get_complement(char)
    return sequence
