#%%
import numpy as np
import pandas as pd
from typing import List
from collections import Counter
from itertools import groupby


def read_file(filename):
    # returns a list of each round
    with open(filename) as f:
        a_list = f.read().split("\n")  # seperate each group by line
    return a_list


def find_winner_a(a, b):
    """find out if the match was a win, lost, or draw.
    draw=3
    win=6
    loss=0"""
    if a == "A":
        if b == "X":
            outcome = 3
        elif b == "Y":
            outcome = 6
        else:
            outcome = 0
    elif a == "B":
        if b == "X":
            outcome = 0
        elif b == "Y":
            outcome = 3
        else:
            outcome = 6
    else:
        if b == "X":
            outcome = 6
        elif b == "Y":
            outcome = 0
        else:
            outcome = 3
    return outcome


def find_choice_score_a(choice):
    if choice == "X":
        choice_score = 1
    elif choice == "Y":
        choice_score = 2
    else:
        choice_score = 3
    return choice_score


def find_choice_score_b(a, b):
    """find out if the match was a win, lost, or draw."""
    if a == "A":
        if b == "X":
            choice_score = 3
        elif b == "Y":
            choice_score = 1
        else:
            choice_score = 2
    elif a == "B":
        if b == "X":
            choice_score = 1
        elif b == "Y":
            choice_score = 2
        else:
            choice_score = 3
    else:
        if b == "X":
            choice_score = 2
        elif b == "Y":
            choice_score = 3
        else:
            choice_score = 1
    return choice_score


def find_winner_b(outcome):
    if outcome == "X":
        outcome_score = 0
    elif outcome == "Y":
        outcome_score = 3
    else:
        outcome_score = 6
    return outcome_score


def find_total_score_a(input):
    """total score if everything goes exactly according to your strategy guide"""
    total_score = 0
    for match in input:
        outcome_score = find_winner_a(match[0], match[2])
        choice_score = find_choice_score_a(match[2])
        total_score = total_score + outcome_score + choice_score
        # print(total_score, outcome_score, choice_score)
    return total_score


def find_total_score_b(input):
    """total score if everything goes exactly according to their strategy guide"""
    total_score = 0
    for match in input:
        outcome_score = find_winner_b(match[2])
        choice_score = find_choice_score_b(match[0], match[2])
        total_score = total_score + outcome_score + choice_score
        # print(total_score, outcome_score, choice_score)
    return total_score


#%%
test = "test.txt"
filename = "input.txt"
# input = read_file(test)
input = read_file(filename)

#%%
try:
    print(find_total_score_a(input))
except:
    print("Error")
#%%
try:
    print(find_total_score_b(input))
except:
    print("Error")
# %%
