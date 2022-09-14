
# Part 1: Write a function that returns a random dice roll between 1 and 6. The function should not have any parameters.
# Write a main program that rolls the dice until the result is 6. The main program should print out the result of each roll.
import random
def diceRoll():
    return random.randint(1,6)
num = diceRoll()
while num != 6:
    print(num)
    num = diceRoll()
print(num)

# Part 2: Modify the function above so that it gets the number of sides on the dice as a parameter. With the modified
# function you can for example roll a 21-sided role-playing dice. The difference to the last exercise is that the
# dice rolling in the main program continues until the program gets the maximum number on the dice, which is asked
# from the user at the beginning.
import random
def diceRoll(sides):
    return random.randint(1,sides)
numSides = int(input("How many sides the dice has? "))
num = diceRoll(numSides)
while num != numSides:
    print(num)
    num = diceRoll(numSides)
print(numSides)

# Part 3: Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres.
# Write a main program that asks for a volume in gallons from the user and converts the value to liters.
# The conversion must be done by using the function. Conversions continue until the user inputs a negative value.
def gallonToLit(gallons):
    return gallons * 3.785
print("Input negative number to exit")
numGallon = float(input("How many gallons? "))
while numGallon >= 0:
    print(f"Equal to {gallonToLit(numGallon):.4f} litters")
    numGallon = float(input("How many gallons? "))

# Part 4: Write a function that gets a list of integers as a parameter. The function returns the sum of all the numbers in
# the list. For testing, write a main program where you create a list, call the function, and print out the value it returned.

def sumList(intList):
    sumResult = 0
    for i in intList:
        sumResult += i
    return sumResult
predefList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Sum of a list is: ",sumList(predefList))

# Part 5: Write a function that gets a list of integers as a parameter. The function returns a second list that is
# otherwise the same as the original list except that all uneven numbers have been removed. For testing, write a main
# program where you create a list, call the function, and then print out both the original as well as the cut-down list.
def showList(intList):
    newList = []
    for i in intList:
        if i % 2 == 0:
            newList.append(i)
    print("Old list: ", intList)
    print("New list: ", newList)
predefList = [1,2,3,4,5,6,7,8,9,10]
showList(predefList)

# Part 6: Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of
# the pizza in euros. The function calculates and returns the unit price of the pizza per square meter. The main program
# asks the user to enter the diameter and price of two pizzas and tells the user which pizza provides better value for
# money (which of them has a lower unit price). You must use the function you wrote for calculating the unit prices.
import math
def calcPricePizza(diameter, price,name):
    areaPizza = math.pi * diameter/2 * diameter/2
    print("The price per square meter of pizza",name,f": {price / (areaPizza * 0.0001):.3f}")
    return price / (areaPizza * 0.0001)
dia1 = float(input("Input the diameter of pizza 1 in cm: "))
price1 = float(input("Input the price of pizza 1 in euro: "))
dia2 = float(input("Input the diameter of pizza 2 in cm: "))
price2 = float(input("Input the price of pizza 2 in euro: "))
if calcPricePizza(dia1,price1,1) < calcPricePizza(dia2,price2,2):
    print("Pizza 1 is cheaper than pizza 2")
elif calcPricePizza(dia1,price1,1) > calcPricePizza(dia2,price2,2):
    print("Pizza 2 is cheaper than pizza 1")
else:
    print("Same price")
