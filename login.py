import os
print("CariboSystem LogUser Experience")
prompt = input("Press enter to continue or press feedback to give feedback \n > ")
if prompt == "":
    print()
    print("Lets create a User!")
    print("-"*45)
    print()
    user = input("Choose a username which should be equal or more than 3 characters: \n > ")
    if user == "OEM" or user == "oem" or user == "oEM" or user == "Oem" or user == "oEm" or user == "oeM" or user == "OEM":
        print("Sorry you can't choose this username")
        user = input("Choose a username other than this name: \n > ")
    print()
    user_length = len(user)
    if user_length < 3:
        print("Username should be equal or more than 3 Characters!!")
        user = input("Choose a username which should be more than 3 characters: \n > ")
        if user == "OEM":
            print("Sorry you can't choose this username")
            user = input("Choose a username other than this name: \n > ")
        user_length = len(user)
        if user_length < 3:
            print("Sorry, but you have again set a username which is not equal to or more than 3 characters, you will be logged in as a guest")
            user = "Guest"
            if user == "OEM":
                print("Sorry you can't choose this username")
                user = input("Choose a username other than this name: \n > ")
        else:
            print("Lets name your PC")
            pc = input("Choose a PC name: \n" + user + "> ")
            from core import *
    else:
        print("Lets name your PC")
        pc = input("Choose a PC name: \n" + user + "> ")
        from core import *
elif prompt == "feedback":
    print("Visit https://zanvoksupport.simdif.com/ to provide feedback")
else:
    print("error")
