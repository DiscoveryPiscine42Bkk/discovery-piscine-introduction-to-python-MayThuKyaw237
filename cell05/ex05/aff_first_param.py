#!/usr/bin/env python3
import sys

parameters =len(sys.argv) - 1
if parameters == 0:
    print("none")
else:
    print(sys.argv[1])