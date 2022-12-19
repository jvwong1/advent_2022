#%%
import numpy as np
import pandas as pd
from typing import List
from collections import Counter
from itertools import groupby


def read_file(filename):
    # returns a list of each elves calories
    with open(filename) as f:
        a_list = [
            list(g)
            for k, g in groupby(map(str.strip, f), key=lambda line: line != "")
            if k
        ]
    return a_list


def find_most_calories(input):
    """Find the Elf carrying the most Calories and the amount."""
    highest_cal = 0
    # convert list of strings to ints
    converted_input = [[int(num) for num in sub] for sub in input]
    for l in converted_input:
        list_sum = sum(l)
        if list_sum > highest_cal:
            highest_cal = list_sum

    return highest_cal


def find_top_3_most_calories(input):
    """Find the top three Elves carrying the most Calories and the amount."""
    calorie_total_list = []
    # convert list of strings to ints
    converted_input = [[int(num) for num in sub] for sub in input]
    for l in converted_input:
        list_sum = sum(l)
        calorie_total_list.append(list_sum)
    top_3_calorie_total = sum(sorted(calorie_total_list)[-3:])
    return top_3_calorie_total


#%%
test = "test.txt"
filename = "input.txt"
# input = read_file(test)
input = read_file(filename)

#%%
try:
    print(find_most_calories(input))
except:
    print("Error")
#%%
try:
    print(find_top_3_most_calories(input))
except:
    print("Error")
