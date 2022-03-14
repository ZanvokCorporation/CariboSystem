import os
import sys
import subprocess

print()
ver = 6.05
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
        print("6.05")
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

    elif core == "cmd":
        print("Starting Zanvok PY-DOS Subsystem...")
        
        if sys.platform == "win32":
            os.system('python cmd8.py')

        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            os.system('python3 cmd8.py')

    elif core == 'cls':
        os.system('cls')

    elif core == 'clear':
        os.system('clear')

    elif core == "app --manage":
        if sys.platform == "win32":
            os.system('python app\app.caribosystem.py')

        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            os.system('python3 app/app.caribosystem.py')

    elif core == "app":
        if sys.platform == "win32":
            print("Enter App name to run")
            select = input("CariboSystem > App > ")
            app = select + ".py"
            app_dir = "python app/"+app
            os.system(app_dir)

        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            print("Enter App name to run")
            select = input("CariboSystem > App > ")
            app = select + ".py"
            app_dir = "python3 app/"+app
            os.system(app_dir)

    elif core == "help":
        print()
        print("CariboSystem Help")
        print("--------------------------")
        f = open("HELP.md", 'r')
        file1 = f.read()
        print(file1)
        print()
        print("--------------------------")

    elif core == "readme":
        print()
        print("README for CariboSystem")
        print("-------------------------------")
        f = open("README.md", 'r')
        file2 = f.read()
        print(file2)
        print()
        print("-------------------------------")

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
        c_mode = input("Do you want to use core mode to execute the command: " + core + " ? (yes/no)").lower()

        if c_mode == "yes" or c_mode == "y":
            os.system(core)

        elif c_mode == "no" or c_mode == "n":
           print()
        
        else:
            print()