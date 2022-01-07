import os
 
from colorama import init
from termcolor import colored
 
init()
from kernel import kernel_version
if kernel_version == float(5.04):
        print("Welcome to CariboOS 5.01")
        print("CariboOS 5.01 Setup")
        print()
        print("-"* 30)
        from login import *
        user_val = user
        command = ""
        from thanks import *
        os.system('clear')
        print("")
        print("Hi!! " + user + " Welcome to CariboOS 5")
        print("Version: 5.01")
        print("Zanvok Corp.")
        print("")
        while command != "quit":
                #Update new changes to both core.py and switch.py
                command = input(user+"@CariboOS:~> ")
                if command == "about":
                        print("CariboOS")
                        print("Version: 5.01")
                        print("Copyright 2021 @ Zanvok Corporation")
                elif command == "command --list":
                        print("\n Help \n About \n Status \n Exit \n Calc \n Clear or clear or Clr \n")
                elif "release" in command:
                        release =""
                        while release != "quit":
                                print("Release Details: ")
                                print(" type --name to view name")
                                print(" type --history to view history")
                                release = input("release ")
                                if release == "--name":
                                        print("Version: 5.01")
                                        print(colored('Code name: Buggy Bug', 'red'))
                                elif release == "--history":
                                        print("Created on 1st Nov 2021")
                                        print("This is named Buggy Bug because it has many bugs!!")
                                elif release == "exit":
                                        break
                                else:
                                        print("Invalid release command!")
                elif command == "help":
                        print("Commands for using CariboOS")
                        from help import *
                elif command == "cmd":
                        from cmd8 import *  
                elif command == "status":
                        print(colored("Under Development!" , 'red' , 'on_cyan'))
                elif command == "exit":
                        break
                elif command == "calc":
                        from calc import *
                elif command == "bsod":
                        from bsod import *
                        break
                elif command == "thanks":
                        from thanks import *
                elif command == "clear" or command == "clr" or command == "clear":
                        import multiprocessing
                        import time
                        import os
                        # bar
                        def bar():
                                for i in range(100):
                                        print(" ")
                                        time.sleep(1)

                        if __name__ == '__main__':
                                # Start bar as a process
                                p = multiprocessing.Process(target=bar)
                                p.start()

                                # Wait for 2 seconds or until process finishes
                                p.join(0)

                                # If thread is still active
                                if p.is_alive():
                                        print("")

                                        # Terminate - may not work if process is stuck for good
                                        p.terminate()
                                        # OR Kill - will work for sure, no chance for process to finish nicely however
                                        # p.kill()

                                        p.join()
                        os.system('clear')
                elif command == "":
                        print("")
                else:
                        print("Invalid Command")
                        print("Suggest more commands at https://sites.google.com/view/zanvokcorporation/ ")
else:
        if kernel_version < float(5.04):
                print("Unsupported Kernel Version")
                print("Cannot run on Kernel version lower 5.04")
                core_terminate = input("Press any key to terminate..")
                from bsod import *
        elif kernel_version > float(5.99):
                print("Unsupported Kernel Version")
                print("Cannot run on Higher Versions of Kernel, higher than 5.99")
                core_terminate = input("Press any key to termnate..")
                from bsod import *
        else:
                print("Unsupported Kernel Type")
                print("No version string defined")
                core_terminate = input("Press any key to terminate..")
                from bsod import *
