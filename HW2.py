# HW2
# Name:
# Collaborators:
# Date:

import random

def count_characters(s):
    """Count the number of occurrences of each character in a string. 
    Args:
        s: str, the string in which to count. 
    Returns:
        a dict keyed by characters whose values are the number of occurrences in s
    """
    L = {}
    
    for i in range(len(s)):
        if s[i] in L:
            L[s[i]] += 1
        else:
            L[s[i]] = 1
    
    return L 


def count_ngrams(s, n=1):
    """Count the number of occurrences of n-grams in a string. 
    Args:L = {}
    
    for i in range(len(s)):
        if s[i] in L:
            L[s[i]] += 1
        else:
            L[s[i]] = 1
        s: str.
        n: positive int. should have default value 1.
    Returns:
        a dict keyed by n-grams whose values are the number of occurrences in s
    """
    
    L = {}
    
    for i in range(len(s)):
        if i == len(s)- (n-1):
            break
        ngram = s[i:(i+n)]
        if ngram in L:
            L[ngram] += 1
        else:
            L[ngram] = 1
    
    return L 


def markov_text(s, n, length = 100, seed = ""):
    """Generate fake text according to an n-th order Markov model, with data from a user-supplied corpus. 
    Args:
        s: str. the text from which to learn grams.
        n: positive int. the order of the Markov model. 
        length: positive int. the number of synthetic characters to generate. should have a default value. 
        seed: str. should have a default value.
    Returns:
        The output string fake_text. fake_text starts with the seed. 
        length of fake_text = length of seed + argument 'length'
    """
    
    fake_text = seed
    n_plus1 = count_ngrams(s,n+1)
    
    if fake_text == "":
        current_gram = random.choice(list(count_ngrams(s, n).keys()))
        fake_text = current_gram
        
    else:
        current_gram = fake_text[-n:]
        
    
    for i in range(length):
        choices = []
        weight = []
        for key, value in n_plus1.items():
            if key.startswith(current_gram):
                choices.append(key)
                weight.append(value)
        
        ran_gram = random.choices(choices, weight)
        fake_text += ran_gram[0][-1]
        current_gram = fake_text[-n:]
            
    return fake_text 