import os
import sys
import subprocess

print()
f = open("user.dat", 'r')
read = f.read()
user_log = input("Enter password of user " + read + " : ")
v = open("password.dat", 'r')
verify = v.read()
if user_log == verify:
    if sys.platform == "win32":
        os.system('cls')
        print()
        print("CariboSystem User")
        print("-------------------------------------------")
        print()
        print("User: " + read)
        print("Password: " + verify)
        print()
        print("-------------------------------------------")

        select = ""
        while select != "exit" or select != "quit":
            select = input("> ")
            if select == "exit" or select == "quit":
                break
            elif select == "user":
                if sys.platform == "win32":
                    os.system('python users.caribosystem.py')

                else:
                    opener = "open" if sys.platform == "darwin" else "xdg-open"
                    os.system('python3 users.caribosystem.py')
            else:
                print("Invalid...!")

    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        os.system('clear')
        print()
        print("CariboSystem User")
        print("-------------------------------------------")
        print()
        print("User: " + read)
        print("Password: " + verify)
        print()
        print("-------------------------------------------")

        select = ""
        while select != "exit" or select != "quit":
            select = input("> ")
            if select == "exit" or select == "quit":
                break
            elif select == "user":
                if sys.platform == "win32":
                    os.system('python users.caribosystem.py')

                else:
                    opener = "open" if sys.platform == "darwin" else "xdg-open"
                    os.system('python3 users.caribosystem.py')
            else:
                print("Invalid...!")