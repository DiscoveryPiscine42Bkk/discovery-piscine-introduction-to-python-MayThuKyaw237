#!/usr/bin/env python3
import sys
parameters = len(sys.argv) -1

def downcase_it(inp):
    return inp.lower()
if parameters == 0:
    print("none")
else:
    for inp in sys.argv[1:]:
        output = downcase_it(inp)
        print(output)
