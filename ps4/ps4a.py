# Problem Set 4A
# Name: Adair Neto
# Collaborators:
# Time Spent: 2:30

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    # pass #delete this line and replace with your code here
    # Base case
    permutations = []
    if len(sequence) == 1:
        permutations.append(sequence)
    # Recursive case
    else:
        # perm = get_permutations(sequence[1:])
        
        # Permutations
        
        # index = 0
        # while index < len(sequence):
        #     perm_copy = perm.copy()
        #     perm_copy.insert(index,sequence[0])
        #     permutations.append(''.join(perm_copy))
        #     index += 1
        
        seq_copy = sequence[:]
        for char in sequence:
            permutations += [char + letter for letter in get_permutations(seq_copy.replace(char, ''))]
        
    return permutations

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    # pass #delete this line and replace with your code here

