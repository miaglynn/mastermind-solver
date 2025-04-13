#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 13:01:40 2024

@author: miaglynn
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 16:56:33 2024

@author: miaglynn
"""

from itertools import product
import random
# import math
# import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

# key

# A = all codes
# C = hidden code
# F = feedback
# PossF = possible feedback
# G = guess code
# PG = previous guess
# NG = next guess
# PS = previous set of codes
# S = new set of codes
# x = length of the code
# y = number of possible values for each position

def possible_codes(x,y):
    
    values = range(1,y+1)
    codes = product(values, repeat = x)
    
    return list(codes)


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
    for i in set(G): 
        white += min(G.count(i), C.count(i))
    
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

                       
          
def simple_next_guess(new_poss_codes):
    
    return new_poss_codes[0]

def simple_method(C, x, y):
    
    all_codes = possible_codes(x, y)  
    G = all_codes[0]
    F = feedback(C, G)
    correct = is_guess_correct(F,x)
    guess_count = 1
    A = all_codes[:]
    S = find_poss_codes(A, G, F)

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
                
# print(simple_method([2,4,5,2],4,6))


def simple_guess_counts(x,y) :
    
    A = possible_codes(x, y)
    guesses = []
    
    for C in A:
        guesses.append(simple_method(C, x, y))

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


simple_data_46 = simple_guess_counts(4,6)

simple_stats_46 = Counter(simple_data_46)

simple_EV_46 = expected_value(simple_stats_46)

simple_SD_46 = standard_deviation(simple_stats_46)








