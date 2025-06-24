#!/usr/bin/env python3

import sys
parameters = len(sys.argv) - 1
if parameters != 1:
    print("none")
else:
    inp = input("What was the parameter? ")
    if inp.lower() == sys.argv[1].lower(): #<---- for here i use lower coz python is case sensitive
        print("Good job!")
    else:
        print("Nope, sorry...")