#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 15:11:30 2024

@author: miaglynn
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:17:44 2024

@author: miaglynn
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 16:54:30 2024

@author: miaglynn
"""

from itertools import product
import random
from collections import Counter
import numpy as np

def possible_codes(x,y):
    
    values = range(1,y+1)
    
    return list(product(values, repeat = x))


def random_code(x,y):
    
    return random.choice(possible_codes(x,y))


def feedback(C, G):
    black = 0
    white = 0
    
    # black for right colour right place
    for i in range(len(C)):
        if C[i] == G[i]:
            black += 1
    
    # white for right colour wrong place
    for color in set(G): 
        white += min(G.count(color), C.count(color))
    
    white -= black
    
    return [black, white]

def possible_feedback(x):
    
    PossF = []
    
    for a in range(x + 1):
      for b in range(x + 1 - a):
        if a + b <= x and not (a == x - 1 and b == 1):
          PossF.append([a, b])
    return PossF

def is_guess_correct(F,x):
    
    if F[0] == x and F[1] == 0:
        
        return True
    
    else:
        
        return False
  
                
def find_poss_codes(PS, PG, F):
    NS = []
    for code in PS:
        fb = feedback(code, PG)
        if fb == F and code != PG:
            NS.append(code)
    return NS


def count_feedback(poss_codes, guess, poss_feedback):
    feedback_count = {tuple(fb): 0 for fb in poss_feedback}  
    
    for code in poss_codes:
        F = tuple(feedback(guess, code))  
        feedback_count[F] += 1  
    
    return feedback_count


def new_2_guesses(C, x, y):
    S = possible_codes(x, y)  
    G = [3,4,5,6]
    guess_count = 1
    F = feedback(C, G)
    correct = is_guess_correct(F, x)
    S = find_poss_codes(S, G, F)
    if correct:
        return correct, guess_count, S
    
    G = [1,1,2,3]
    guess_count = 2
    F = feedback(C, G)
    correct = is_guess_correct(F, x)
    S = find_poss_codes(S, G, F)
    if correct:
        return correct, guess_count, S
    
    return correct, guess_count, S

    

def simple_next_guess(new_poss_codes):
    
    return new_poss_codes[0]

def new_method(C, x, y):
    
    correct, guess_count, S = new_2_guesses(C, x, y)

    while not correct:
        
        if len(S) == 1:  
            G = list(S[0])
        
        else:
            G = simple_next_guess(S)
        
        F = feedback(C, G)
        correct = is_guess_correct(F,x)
        guess_count += 1
        S = find_poss_codes(S, G, F)
      
        if guess_count > 10:
            break

    if correct:
        return guess_count   
    
        
# print(max_entropy_initial_guess(4, 6))

def new_guess_counts(x,y) :
    
    A = possible_codes(x, y)
    guesses = []
    
    for C in A:
        guesses.append(new_method(C, x, y))
        print(len(guesses))
    return guesses
 

def expected_value(stats):
    
    no_guesses = list(stats)
    data = list(stats.values())
    
    EV = np.average(no_guesses, weights=data)
    
    return EV
    
def standard_deviation(stats):
    
    no_guesses = list(stats)
    data = list(stats.values())
    
    SD = np.sqrt(np.average((no_guesses - np.average(no_guesses, weights=data))**2, weights=data))
    
    return SD

    
# new_data_46 = new_guess_counts(4,6)

# new_stats_46 = Counter(new_data_46) 
 
# new_EV_46 = expected_value(new_stats_46)

# new_SD_46 = standard_deviation(new_stats_46)  
  
    
  
    
    