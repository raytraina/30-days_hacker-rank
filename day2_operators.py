# Day 2: Operators
# Task: Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

# Enter your code here. Read input from STDIN. Print output to STDOUT
mealCost = float(raw_input())
tipPercent = int(raw_input())
taxPercent = int(raw_input())

def getTip(a, b):
    mealTip = mealCost * float(tipPercent)/100
    return round(mealTip)

def getTax(a, c):
    mealTax = mealCost * float(taxPercent)/100
    return round(mealTax)

tip = getTip(mealCost, tipPercent)
tax = getTax(mealCost, taxPercent)

totalCost = mealCost + tip + tax

print "The total meal cost is %s dollars." %(int(totalCost))