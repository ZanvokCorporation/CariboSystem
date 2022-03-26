import os
import sys
import subprocess

if sys.platform == "win32":
    os.system('cls')
else:
    os.system('clear')

print("CariboSystem Recovery Tool v0.0.1")
print()
print("Select System:")
print("\t 1) CariboSystem 6.0.4")
print("\t 2) CariboSystem 6.0.5")
print("\t 3) CariboSystem 6.1.0")
print("\t 4) CariboSystem 6.11.0")
print()
value = ""
while value != "quit" or value != "exit":
    value = input("> ").lower()
    if value == "1":
        print("Connecting to the server...")
        print("System Image for v6.0.4 is no longer maintained.., Upgrade to v6.11.0")
    elif value == "2":
        print("Connecting to the server...")
        print("System Image for v6.0.5 is no longer maintained.., Upgrade to v6.11.0")
    elif value == "3":
        print("Connecting to the server...")
        print("System Image for v6.1.0 is no longer maintained.., Upgrade to v6.11.0")
    elif value == "4":
        if sys.platform == "win32":
            print("Connecting to the server...")
            print("There are 2 images available:")
            print("\t 1) ZIP Image")
            print("\t 2) NBSI/NBSImage (Non-Bootable System Image)")
            print("Which image do you want?")
            value0 = input("> ")
            if value0 == "1":
                os.system('python netget.py https://github.com/ZanvokCorporation/CariboSystem-Recovery/releases/download/v6.11.0-Recovery/CariboSystem-6.11.0.zip')
            elif value0 == "2":
                os.system('python netget.py https://github.com/ZanvokCorporation/CariboSystem-Recovery/releases/download/v6.11.0-Recovery/CariboSystem-6.11.0.NBSI')
            else:
                print("Invalid Response..!")
                break
        else:
            print("Connecting to the server...")
            print("There are 2 images available:")
            print("\t 1) TAR.GZ Image")
            print("\t 2) NBSI/NBSImage (Non-Bootable System Image)")
            print("Which image do you want?")
            value1 = input("> ")
            if value1 == "1":
                os.system('python3 netget.py https://github.com/ZanvokCorporation/CariboSystem-Recovery/releases/download/v6.11.0-Recovery/CariboSystem-6.11.0.tar.gz')
            elif value1 == "2":
                os.system('python3 netget.py https://github.com/ZanvokCorporation/CariboSystem-Recovery/releases/download/v6.11.0-Recovery/CariboSystem-6.11.0.NBSI')
            else:
                print("Invalid Response..!")
    elif value == "5" or value == "quit" or value == "exit":
        break
    else:
        print("Invalid Response.!")