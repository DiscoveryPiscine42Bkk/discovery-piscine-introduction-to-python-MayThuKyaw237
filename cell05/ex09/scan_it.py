#!/usr/bin/env python3
import sys
import re
parameters = len(sys.argv) -1
if parameters != 2:
    print("none")
else:
    scan = re.findall(rf"\b{re.escape(sys.argv[1])}\b", sys.argv[2], re.IGNORECASE)
    if scan:
        print(len(scan))
    else:
        print("none")