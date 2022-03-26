import multiprocessing
import time
import os
import sys
import subprocess
from colorama import init
from termcolor import colored
 
init()
# bar
def bar():
    for i in range(100):
        print("COMPONENT ERROR...!!")
        time.sleep(1)

if __name__ == '__main__':
    # Start bar as a process
    p = multiprocessing.Process(target=bar)
    p.start()

    # Wait for 10 seconds or until process finishes
    p.join(0)

    # If thread is still active
    if p.is_alive():
        print("ERROR")

        # Terminate - may not work if process is stuck for good
        p.terminate()
        # OR Kill - will work for sure, no chance for process to finish nicely however
        # p.kill()

        p.join()
if sys.platform == "win32":
    os.system('cls')
else:
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    os.system('clear')

print(colored("********************************************************************************************                                   " , 'white' , 'on_blue'))
print(colored("********************************************************************************************                                   " , 'white' , 'on_blue'))
print(colored("*                                    FATAL ERROR OCCURED                                   *                                   " , 'white' , 'on_blue'))
print(colored("********************************************************************************************                                   " , 'white' , 'on_blue'))
print(colored("*   An error occured in CariboSystem.                                                      *                                   " , 'white' , 'on_blue'))
print(colored("*    1.Try restarting CariboSystem                                                         *                                   " , 'white' , 'on_blue'))
print(colored("*    2.If this error persists again raise this problem in https://zanvoksupport.simdif.com/*                                   " , 'white' , 'on_blue'))
print(colored("********************************************************************************************                                   " , 'white' , 'on_blue'))
print(colored("* Error Code x1101                                                                         *                                   " , 'white' , 'on_blue'))
print(colored("--------------------------------------------------------------------------------------------                                   " , 'white' , 'on_blue'))
print(colored("Terminating CariboSystem                                                                                                       " , 'white' , 'on_blue'))
bsod = input (colored("Press any key to terminate...                                                                                          " , 'white' , 'on_blue'))