from pyfiglet import Figlet
f = Figlet(font='slant')
print('==========================================================================')
print("")
print("")
print("")
print(f.renderText(' CariboOS'))
print("")
print("")
print("                 CariboOS 5.01")
print("                 Zanvok Corporation")
print('==========================================================================')
print("")
print("")
print("")
print("")
print("")
#print("loading /PY/CariboOS/core.py....Done")
#print("loading /PY/CariboOS/switch.py....Done")
#print("loading /PY/CariboOS/switch2.py....Done")
#print("loading /PY/CariboOS/help.py....Done")
#print("loading /PY/CariboOS/calc.py....Done")
#print("")
#print("")
#print("")
#print("")
#print("CariboOS Booted Successfully")
boot = input("Press any key to continue..")
import multiprocessing
import time
import os
# bar
def bar():
    for i in range(100):
        print("")
        time.sleep(1)

if __name__ == '__main__':
    # Start bar as a process
    p = multiprocessing.Process(target=bar)
    p.start()

    # Wait for 10 seconds or until process finishes
    p.join(1000)

    # If thread is still active
    if p.is_alive():
        print("")

        # Terminate - may not work if process is stuck for good
        p.terminate()
        # OR Kill - will work for sure, no chance for process to finish nicely however
        # p.kill()

        p.join()
os.system('cls')
from core import *
