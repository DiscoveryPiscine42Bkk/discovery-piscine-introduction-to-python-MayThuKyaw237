#!/usr/bin/env python3
import sys
parameters = len(sys.argv) -1
if parameters == 0:
    print("none")
else:
    for i in sys.argv[1:]:
        if not i.endswith("ism"):
            print(i+"ism")
        