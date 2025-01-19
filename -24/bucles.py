from time import sleep
import os
countdown = [4,3,2,1,0]

for number in countdown:
    print(number)
    sleep(1)
os.system('shutdown -s -t 1')