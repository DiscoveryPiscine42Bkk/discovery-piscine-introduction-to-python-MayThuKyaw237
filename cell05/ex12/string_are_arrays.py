#!/usr/bin/env python3
import sys
parameters = len(sys.argv) -1
if parameters != 1:
    print("none")
else:
    count = 0
    for i in sys.argv[1]:
        if i == "z":
            count +=1
    if count:
        print('z'*count)
    else:
        print("none")