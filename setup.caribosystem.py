import os
import sys
import subprocess

print("CariboSystem 6 Setup")
print("""
    ╭━╮╱╱╱╱╭┳╮╱╱╭━━╮╱╭━┳╮
    ┃╭╋━╮╭┳╋┫╰┳━┫━━╋┳┫━┫╰┳━┳━━╮
    ┃╰┫╋╰┫╭┫┃╋┃╋┣━━┃┃┣━┃╭┫┻┫┃┃┃
    ╰━┻━━┻╯╰┻━┻━┻━━╋╮┣━┻━┻━┻┻┻╯  SETUP
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯
""")
print("""
CariboSystem Setup Experience
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
[1] CariboSystem Setup
[2] I've already done the CariboSystem Setup
[3] Cancel Setup
""")

select = ""

while select != "quit" or select != "exit":
    select = input("Setup > ")

    if select == "1":
        print()
        print("Entering CariboSystem Setup")
        print("Loading Data")
        print()
        user = input("Enter a UserName: ")
        password = input("Enter a Password: ")
        f = open("user.dat", 'w')
        f.write(user)
        f.close()
        g = open("password.dat", 'w')
        g.write(password)
        g.close()
        print("User Created Successfully...")
        print()
        print("Please restart the setup and select [2]")
        inp = input("Press any key to close Setup....")
        break

    elif select == "2":
        if sys.platform == "win32":
            os.system('python core.caribosystem.py')
            sys.exit()
        else:
            os.system('python3 core.caribosystem.py')
            sys.exit()

    elif select == "3" or select == "quit" or select == "exit":
        break

    else:
        print("Invalid Selection...!")