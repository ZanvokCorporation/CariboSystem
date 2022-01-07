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

    # Wait for 6 seconds or until process finishes
    p.join(6)

    # If thread is still active
    if p.is_alive():
        print("")

        # Terminate - may not work if process is stuck for good
        p.terminate()
        # OR Kill - will work for sure, no chance for process to finish nicely however
        # p.kill()

        p.join()
print("Thank you for taking interest in trying out Beta releases of CariboOS")
print("We are extremely eager to hear your responses after trying beta releases of CariboOS")
print("")
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
    p.join(6)

    # If thread is still active
    if p.is_alive():
        print("")

        # Terminate - may not work if process is stuck for good
        p.terminate()
        # OR Kill - will work for sure, no chance for process to finish nicely however
        # p.kill()

        p.join()
os.system('clear')
print("Well we even want you all to try out next versions of CariboSystem!!")
print("")
print("You might think what is CariboSystem?? A new OS??")
print("")
print("Well the answer is no. CariboSystem is the rebranding of CariboOS..")
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
    p.join(8)

    # If thread is still active
    if p.is_alive():
        print("")

        # Terminate - may not work if process is stuck for good
        p.terminate()
        # OR Kill - will work for sure, no chance for process to finish nicely however
        # p.kill()

        p.join()
os.system('clear')
print("Keep it confidential.. Let's surprise the public..")
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
    p.join(4)

    # If thread is still active
    if p.is_alive():
        print("")

        # Terminate - may not work if process is stuck for good
        p.terminate()
        # OR Kill - will work for sure, no chance for process to finish nicely however
        # p.kill()

        p.join()
os.system('clear')
from kernel import *
