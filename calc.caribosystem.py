import os
import sys
import subprocess
import termcolor
import colored

print()
print("Calc for CariboSystem")
print()

calc = ""

while calc != "quit" or calc != "exit":

    calc = input("CariboSystem > Calc > ").lower()

    if calc == "exit" or calc == "quit":
        break
    else:
        print(eval(calc))