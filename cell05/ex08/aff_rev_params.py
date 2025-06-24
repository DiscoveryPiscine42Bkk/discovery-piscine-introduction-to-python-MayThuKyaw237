#!/usr/bin/env python3
import sys

parameters = len(sys.argv) - 1
if parameters < 2:
    print("none")
else:
    for i in sys.argv[::-1]:
        print(i)

