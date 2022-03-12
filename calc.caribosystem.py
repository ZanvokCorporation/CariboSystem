import os
import sys
import subprocess

print()
print("Calc for CariboSystem")
print()

calc = ""

while calc != "quit" or calc != "exit":

    calc = input("CariboSystem > Calc > ").lower()

    if calc == "+" or calc == "add":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        add = num1+num2
        print("Sum: ", add)

    elif calc == "-" or calc == "sub":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        sub = num1-num2
        print("Sub: ", sub)

    elif calc == "*" or calc == "mul":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        mul = num1*num2
        print("Mul: ", mul)

    elif calc == "/" or calc == "div":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        div = num1/num2
        print("Div: ", div)

    elif calc == "exit" or calc == "quit":
        print()
        break

    elif calc == "cls":
        os.system('cls')

    elif calc == "clear":
        os.system('clear')

    elif calc == "ver" or calc == "version":
        ver = 6.00
        os_release = "CariboSystem6"
        r_ty = "Beta"
        print()
        print("Calc(CariboSystem6)6.0BETA")
        print()

    else:
        print("Command " + calc + " not found...")
    