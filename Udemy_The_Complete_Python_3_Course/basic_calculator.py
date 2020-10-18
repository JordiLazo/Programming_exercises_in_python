'''
Program: Magical Calculator
Author: Jordi Lazo
Copyright: 2016
'''
import re

print("Our Magical Calculator")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""

    #If there has been a previous calculation, use that result as the prompt
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))
    #If user exit
    if equation == 'exit':
        print("Goodbye, human.")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()]','',equation)

        if previous == 0:
            previous = eval(equation)
        
        else:
            previous = eval(str(previous) + equation)
        
        print("You typed:", previous)

while run:
    performMath()