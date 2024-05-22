from main import clear, version
import sys
import time
import os

clear()
for i in range(3):
    sys.stdout.write('Updating   \r')
    time.sleep(0.5)
    sys.stdout.write('Updating.  \r')
    time.sleep(0.5)
    sys.stdout.write('Updating.. \r')
    time.sleep(0.5)
    sys.stdout.write('Updating...\r')
    time.sleep(0.5)
os.system('git restore *')
os.system('git pull')
for i in range(3):
    sys.stdout.write('Restarting   \r')
    time.sleep(0.5)
    sys.stdout.write('Restarting.  \r')
    time.sleep(0.5)
    sys.stdout.write('Restarting.. \r')
    time.sleep(0.5)
    sys.stdout.write('Restarting...\r')
    time.sleep(0.5)
clear()
print(f'Current version: {version}')
os.system('python main.py')