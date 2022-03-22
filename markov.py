"""Generate Markov text from text files."""

# import sys
from random import choice


def open_and_read_file(file_path1, file_path2):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    # your code goes here

    input_text1 = open(file_path1).read()
    input_text2 = open(file_path2).read()

    input_text = input_text1 + input_text2

    #print(input_text)
    return input_text #'Contents of your file as one long string'
    

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    
    words = text_string.split()
    words.append(None)
    list_len = len(words)
    

    for index in range(list_len-2):
        
        key_tuple = (words[index], words[index + 1])
        #print(key_tuple)
        chains[key_tuple] = chains.get(key_tuple, [])
        chains[key_tuple].append(words[index + 2])

    return chains


def make_text(chains):
    """Return text from chains."""

    key = choice(list(chains.keys()))
    words = [key[0], key[1]]
    word = choice(chains[key])

    while word is not None:
        key = (key[1], word)
        words.append(word)
        word = choice(chains[key])
        

    return ' '.join(words)


file_path1 = 'green-eggs.txt'
file_path2 = 'gettysburg.txt'

input_text = open_and_read_file(file_path1, file_path2)

# Open the file and turn it into one long string
#input_text = open_and_read_file(file_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
