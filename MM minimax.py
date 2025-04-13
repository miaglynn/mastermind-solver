#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 16:53:56 2024

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

def minimax_next_guess(PossF, A, S):
    
    scores = {tuple(code): 0 for code in A}
    
    for code in A:
        hits = count_feedback(S, code, PossF)
        max_hits = max(hits.values())
        C = tuple(code)
        scores[C] = max_hits

    min_score = min(scores.values())
    min_codes = []
    
    for code, score in scores.items():
        if score == min_score:
            min_codes.append(code)
            
    C1 = []
    for i in S:
        if i in min_codes:
            C1.append(i)
    
    if len(C1) == 0:
        G = list(min_codes[0])

    else:
        G = C1[0]
        
    return G

def minimax_initial_guess(x,y):
    
    PossF = possible_feedback(x)
    A = possible_codes(x, y)
    IG = minimax_next_guess(PossF, A, A)
    
    return IG            


def minimax_method(C, IG, x, y):
    
    all_codes = possible_codes(x, y)
    PossF = possible_feedback(x) 
    F = feedback(C, IG)
    correct = is_guess_correct(F,x)
    guess_count = 1
    A = all_codes[:]
    S = find_poss_codes(A, IG, F)

    while not correct:
        
        if len(S) == 1:  
            G = list(S[0])
        
        else:
            G = minimax_next_guess(PossF, A, S)
        
        F = feedback(C, G)
        correct = is_guess_correct(F,x)
        guess_count += 1
        S = find_poss_codes(S, G, F)
        
    if correct:
        return guess_count
 
# Collecting data

def minimax_guess_counts(x,y) :
    
    A = possible_codes(x, y)
    guesses = []
    IG = minimax_initial_guess(x, y)
    
    for C in A:
        guesses.append(minimax_method(C, IG, x, y))
        
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



# minimax_data_46 = minimax_guess_counts(4,6)

# minimax_stats_46 = Counter(minimax_data_46)  

# minimax_EV_46 = expected_value(minimax_stats_46)

# minimax_SD_46 = standard_deviation(minimax_stats_46)






