import os
import sys
import subprocess

print()
ver = 6.0
r_type = "BETA"
print()
print("""
    ╭━╮╱╱╱╱╭┳╮╱╱╭━━╮╱╭━┳╮
    ┃╭╋━╮╭┳╋┫╰┳━┫━━╋┳┫━┫╰┳━┳━━╮
    ┃╰┫╋╰┫╭┫┃╋┃╋┣━━┃┃┣━┃╭┫┻┫┃┃┃
    ╰━┻━━┻╯╰┻━┻━┻━━╋╮┣━┻━┻━┻┻┻╯
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯
    """)

core = ""
if sys.platform == "win32":
    os.system('cls')
else:
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    os.system('clear')

while core != "quit" or core != "exit":
    
    core = input("CariboSystem > ")

    if core == "ver":
        print()
        print("""
    ╭━╮╱╱╱╱╭┳╮╱╱╭━━╮╱╭━┳╮
    ┃╭╋━╮╭┳╋┫╰┳━┫━━╋┳┫━┫╰┳━┳━━╮
    ┃╰┫╋╰┫╭┫┃╋┃╋┣━━┃┃┣━┃╭┫┻┫┃┃┃
    ╰━┻━━┻╯╰┻━┻━┻━━╋╮┣━┻━┻━┻┻┻╯
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯
        """)
        print()
        print("CariboSystem")
        print("6.04")
        print("Zanvok Corporation")
        print()

    elif core == "ver core":
        print()
        print("""
    ╭━╮╱╱╱╱╭┳╮╱╱╭━━╮╱╭━┳╮
    ┃╭╋━╮╭┳╋┫╰┳━┫━━╋┳┫━┫╰┳━┳━━╮
    ┃╰┫╋╰┫╭┫┃╋┃╋┣━━┃┃┣━┃╭┫┻┫┃┃┃
    ╰━┻━━┻╯╰┻━┻━┻━━╋╮┣━┻━┻━┻┻┻╯
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯
        """)
        print()
        print("Core(CariboSystem6).6.0Beta")
        print()

    elif core == 'calc':
        if sys.platform == "win32":
            os.system('python calc.caribosystem.py')
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            os.system('python3 calc.caribosystem.py')

    elif core == 'cls':
        os.system('cls')

    elif core == 'clear':
        os.system('clear')

    elif core == "exit" or core == "quit":
        print()
        print("GoodBye!")
        print()
        break

    elif core == "bsod":
        if sys.platform == "win32":
            os.system('python bsod.caribosystem.py')
            break
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            os.system('python3 bsod.caribosystem.py')
            break
    else:
        print()
        print("Bad Command..")
        print()