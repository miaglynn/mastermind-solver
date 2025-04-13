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


def count_feedback(S, G, PossF):
    feedback_count = {tuple(i): 0 for i in PossF}  
    
    for code in S:
        F = tuple(feedback(G, code))  
        feedback_count[F] += 1  
    
    return feedback_count


def max_parts_next_guess(PossF, A, S):
  scores = {tuple(code): 0 for code in S}

  for code in A:
    all_parts = count_feedback(S, code, PossF)
    parts_list = [i for i in list(all_parts.values()) if i != 0]
    no_parts = len(parts_list)
    scores[code] = no_parts

  max_score = max(scores.values())

  max_codes = []
  for code, score in scores.items():
    if score == max_score:
      max_codes.append(code)

  C1 = []
  for code in max_codes:
    if code in S:
      C1.append(code)

  if len(C1) == 0:
    G = list(max_codes[0])
    
  else:
    G = C1[0]

  return G


def max_parts_initial_guess(x,y):
    
    PossF = possible_feedback(x)
    A = possible_codes(x, y)
    IG = max_parts_next_guess(PossF, A, A)
    
    return IG      
        
# print(max_parts_initial_guess(4, 6))

def max_parts_method(C, IG, x, y):
    
    A = possible_codes(x, y)
    PossF = possible_feedback(x)
    F = feedback(C, IG)
    correct = is_guess_correct(F,x)
    guess_count = 1
    S = find_poss_codes(A, IG, F)

    while not correct:

        G = max_parts_next_guess(PossF, A, S)  
        F = feedback(C, G)
        correct = is_guess_correct(F,x)
        guess_count += 1
        S = find_poss_codes(S, G, F)
      
    if correct:
        return guess_count

def max_parts_guess_counts(x,y) :
    
    A = possible_codes(x, y)
    IG = max_parts_initial_guess(x, y)  
    guesses = []
    
    for C in A:
        guesses.append(max_parts_method(C, IG, x, y))

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

# max_parts_data_46 = max_parts_guess_counts(4,6)

# max_parts_stats_46 = Counter(max_parts_data_46) 

# max_parts_EV_46 = expected_value(max_parts_stats_46)

# max_parts_SD_46 = standard_deviation(max_parts_stats_46)











