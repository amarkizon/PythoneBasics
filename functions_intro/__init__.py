import platform
import socket
import os
import random
import time
from time import * # importing only sleep function from the time module

print('Printing random number')
print(random.random())               # 0-1
sleep(0.75)
print('Printing random number mostly between 100 and 200 ')     # 10-200
print(random.random()*200)
sleep(0.75)
print('my current system name')
print(platform.node())
print(socket.gethostname())
print(os.environ['COMPUTERNAME']) # Work only on windows
