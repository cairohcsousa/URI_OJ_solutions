## Here we need to calculate the amount of grain
## and divide it by 12 to get the weight in grams
## as we need the weight in kilograms, we divide again by 1000

import math

def total_grain(num):
##  The first square gets 1 grain
    total = 1
    
    for i in range(num):
        total *= 2

    return total

def grain_weight(num):
    return math.floor(total_grain(num)/12000)

cases = int(input())

for i in range(cases):
    n_squares = int(input())

    print("{:.0f} kg".format(grain_weight(n_squares)))

