#!/usr/bin/env python3
import sys

def shrink(inp):
    print(inp[:8])
def enlarge(inp):
    output = inp + 'Z'*(8-len(inp))
    print(output)
parameters = len(sys.argv) -1
if parameters < 1:
    print("none")
else:
    for i in sys.argv[1:]:
        if len(i) > 8:
            shrink(i)
        elif len(i) < 8:
            enlarge(i)
        else:
            print(i)
