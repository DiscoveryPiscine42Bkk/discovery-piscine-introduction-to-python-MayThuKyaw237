#!/usr/bin/env python3
import sys
parameters = len(sys.argv) - 1
if parameters != 2:
    print("none")
else:
    print(list(range(int(sys.argv[1]),int(sys.argv[2])+1)))