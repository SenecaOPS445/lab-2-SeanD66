#!/usr/bin/env python3
#Author: Sean Daweng
#Author ID: 100851187
#Date Created: 2025/01/20


import sys

if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer = timer - 1
print('blast off!')
