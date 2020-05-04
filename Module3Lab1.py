"""
CTEC 121
Filipp Kopytyuk
Into into Programming & Problem Solving
Module 3 Lab 1
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

def main():
    # Conditional Expressions

    # Literals
    '''
    print("\nBoolean Literals")
    print(True)
    print(False)
    print(type(True))
    print()
    
    # Relational Operators
    print("Relational Operators")
    print("3 < 5", 3 < 5)
    print("3 <= 3", 3 <= 3) 
    print("3 == 3", 3 == 3)
    print("3 >= 5", 3 >= 5)
    print("3 != 5", 3 != 5)
    print()

    # Using Variables
    x = 3
    y = 5
    print("Using variables")
    print("x:", x, "y:", y)
    print("x < y", x < y)
    print("x != y", x != y)
    print()
    
    # Simple if statements
    print("x:", x, "y:",y)
    if x < y:
        print("x < y")

    if x > y:
        print("x > y")

    print("end simple if example")
    print()

    # if/else statement
    print("if/else statement")
    print("x:", x, "y:",y)
    if x < y:
        print("x < y")
    else:
        print("x >= y")
    
    x = 6
    if x < y:
        print("x < y")
    else:
        print("x >= y")
    
    print("End if/else example")
    print()
    
    # Exercise 3-1

    print("Exercise 3-1")
    for i in range(1, 11):
        if (i % 2) == 0:
            outputString = "even"
        else:
            outputString = "odd"
        print(i, outputString)
    print()
    
    # Alphabetize Names
    name = "Filipp"
    firstLetterOfName = "F"

    print("Multi-way if example")
    if firstLetterOfName == "A":
        print("A")
    elif firstLetterOfName == "B":
        print("B")
    elif firstLetterOfName == "C":
        print("C")
    # ...
    elif firstLetterOfName == "Y":
        print("Y")
    else:   # default case: name starts with "Z"
        print("Z")
    print()
    '''
    try:
        print(4/0)
    except:
        print("\nThere was a divide by zero error. Exiting\n")
        exit()

main()    