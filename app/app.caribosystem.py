import os
import sys
import subprocess

# Application Viewer for CariboSystem6 Preview
print()
def app_uninstall():
    if sys.platform == "win32":
        application = input("Enter APP Name: ")
        print("Are you sure you want to uninstall " + application + " ?")
        confirm = input("Yes/No > ")
        if confirm == "yes":
            core_application = application + ".py"
            core_dat = application + ".dat"
            del_application = "del " + core_application
            del_dat = "del " + core_dat
            os.system(del_application)
            os.system(del_dat)
            print("App Uninstalled Successfully..!")
            log = open("app.log", 'a')
            log.write("\n Uninstalled " + application)
            log.close()
            print()

        else:
            print()

    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        application = input("Enter APP Name: ")
        print("Are you sure you want to uninstall " + application + " ?")
        confirm = input("Yes/No > ")
        if confirm == "yes":
            core_application = application + ".py"
            core_dat = application + ".dat"
            del_application = "rm " + "app/" + core_application
            del_dat = "rm " + "app/" + core_dat
            os.system(del_application)
            os.system(del_dat)
            print("App Uninstalled Successfully..!")
            log = open("app.log", 'a')
            log.write("\n Uninstalled " + application)
            log.close()
            print()
        
        else:
            print()

print("CariboSystem App Manager")
print("---------------------------")
print()
core = ""
while core != "quit" or core != "exit":
    print("Enter `unin` to uninstall an app, Enter `exit` to quit to CariboSystem")
    print()
    core = input("> ").lower()
    if core == "unin":
        app_uninstall()
        
    elif core == "exit" or core == "quit":
        break

    else:
        print("Invalid Selection...!")