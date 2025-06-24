#!/usr/bin/env python3
import sys
parameters = len(sys.argv) - 1

if parameters == 0:
    print("none")
else:
    print(f"parameters: {parameters}")
    for i in sys.argv[1:]:
        print(f"{i}: {len(i)}")
    