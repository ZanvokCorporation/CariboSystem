print("Calculator for CariboSystem")
print()
print("~"*45)
print()
print("Available Operands:-")
print("""
    \t 1. Addition
    \t 2. Subtraction
    \t 3. Multiplication
    \t 4. Division
    \t 5. Square Root
""")
print("Type the number or operand name to continue" , " Type exit to quit")
calc = ""
while calc != "quit":
    calc = input("Calc> ")
    if calc == 1 or calc == "add" or calc == "addition" or calc == "sum" or calc == "+":
        add1 = input("Enter first number: ")
        add2 = input("Enter second number: ")
        add = float(add1)+float(add2)
        print("Your answer is: " , add)
    elif calc == 2 or calc == "sub" or calc == "subtraction" or calc == "subtract" or calc == "minus" or calc == "-":
        sub1 = input("Enter first number: ")
        sub2 = input("Enter second number: ")
        sub = float(sub1)-float(sub2)
        print("Your answer is: " , sub)
    elif calc == 3 or calc == "multiplication" or calc == "multiply" or calc == "X" or calc == "*" or calc == "mul":
        mul1 = input("Enter first number: ")
        mul2 = input("Enter second number: ")
        mul = float(mul1)*float(mul2)
        print("Your answer is: " , mul)
    elif calc == 4 or calc == "division" or calc == "divide" or calc == "div" or calc == "/":
        div1 = input("Enter first number: ")
        div2 = input("Enter second number: ")
        div = float(div1)/float(div2)
        print("Your answer is: " , div)
    elif calc == 5 or calc == "Square Root" or calc == "SquareRoot" or calc == "sqroot":
        sqroot_number = input("Enter number: ")
        sqroot = float(sqroot_number)*float(sqroot_number)
        print("Your answer is: " , sqroot)
    elif calc == "exit":
        from switch import *
    elif calc == "about":
        print("Calc for cariboSystem 6")
    else:
        print("Invalid calc command!")
