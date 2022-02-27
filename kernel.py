import os
import multiprocessing
import time
import pyfiglet
from pyfiglet import Figlet
f = Figlet(font='slant')

os.system('cls')
print("===============================================================================================")
result = pyfiglet.figlet_format("Flix ", font = "isometric1" )
print(result)
print("===============================================================================================")
print("|Zanvok Flix Kernel       |")
print("|Version: 5.04 - Universal|")
print("|Zanvok Corporation @ 2021|")
print("===========================")
print("Loading Resources.......")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
import multiprocessing
import time

# bar
def bar():
    for i in range(100):
        print("")
        time.sleep(1)

if __name__ == '__main__':
    # Start bar as a process
    p = multiprocessing.Process(target=bar)
    p.start()

    # Wait for 5 seconds or until process finishes
    p.join(5)

    # If thread is still active
    if p.is_alive():
        print("")

        # Terminate - may not work if process is stuck for good
        p.terminate()
        # OR Kill - will work for sure, no chance for process to finish nicely however
        # p.kill()

        p.join()

os.system('cls')
print("Found CariboOS..")
import multiprocessing
import time

# bar
def bar():
    for i in range(100):
        print("")
        time.sleep(1)

if __name__ == '__main__':
    # Start bar as a process
    p = multiprocessing.Process(target=bar)
    p.start()

    # Wait for 1 second or until process finishes
    p.join(1)

    # If thread is still active
    if p.is_alive():
        print("")

        # Terminate - may not work if process is stuck for good
        p.terminate()
        # OR Kill - will work for sure, no chance for process to finish nicely however
        # p.kill()

        p.join()
os.system('cls')
print("Booting into CariboOS..")
import multiprocessing
import time

# bar
def bar():
    for i in range(100):
        print("")
        time.sleep(1)

if __name__ == '__main__':
    # Start bar as a process
    p = multiprocessing.Process(target=bar)
    p.start()

    # Wait for 5 seconds or until process finishes
    p.join(5)

    # If thread is still active
    if p.is_alive():
        print("")

        # Terminate - may not work if process is stuck for good
        p.terminate()
        # OR Kill - will work for sure, no chance for process to finish nicely however
        # p.kill()

        p.join()
os.system('cls')
kernel_version = float(6.01)
from boot import *



