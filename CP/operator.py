import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

 
if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    
    tip_amount = meal_cost * tip_percent / 100
    tax_amount = meal_cost * tax_percent / 100
    total_cost = round(meal_cost + tip_amount + tax_amount)
    print( total_cost )
import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):
    tip_percent = (tip_percent/100)*meal_cost
    tax_percent = (tax_percent/100)*meal_cost
    meal_cost = meal_cost+tip_percent+tax_percent
    return meal_cost

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    result = solve(meal_cost, tip_percent, tax_percent)
    print(round(result))