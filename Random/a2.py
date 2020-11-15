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
    return dna1>dna2

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

    '''(str)->bool

    Returns whether the dna is valid of a valid sequence or not.

    >>>is_valid_sequence('ATCGACGT')
    True

    >>>is_valid_sequence('BATCG')
    False
    '''

    valid_sequence=True
    
    for dnacomponents in dna:
        if dnacomponents not in 'ATCG':
            return False

    return valid_sequence

def insert_sequence(dna1,dna2,index):

    '''(str,str,int)->str

    Returns the dna sequence obtained by inserting dna2 into dna1 ath the index position.

    >>>insert_sequence('CCGG','AT',2)
    'CCATGG'

    >>>insert_sequence('Arijit','Sir',0)
    'SirArijit'

    >>>insert_sequence('Arijit','Ghosh',6)
    'ArijitGhosh'
    '''

    if index==0 or index==-len(dna1):
        return dna2+dna1
    elif index==-1 or index==len(dna1):
        return dna1+dna2
    else:
        return dna1[:index]+dna2+dna1[index:]



def get_complement(nucleotide):

    '''(str)->str
    Returns the complement of the nucleotide.

    >>>get_complement('A')
    'T'

    >>>get_complement('G'):
    'C'
    '''
    if nucleotide=='A':
        return 'T'
    elif nucleotide=='T':
        return 'A'
    elif nucleotide=='C':
        return 'G'
    else:
        return 'C'

def get_complementary_sequence(dna_sequence):

    '''(str)->str

    Returns complement of the dna_sequence.

    >>>get_complementary_sequence('AT')
    'TA'
    >>>get_complementary_sequence('CG')
    'GC'
    '''

    sequence=''
    
    for each_nucleotide in dna_sequence:
        sequence=sequence+get_complement(each_nucleotide)

    return sequence



