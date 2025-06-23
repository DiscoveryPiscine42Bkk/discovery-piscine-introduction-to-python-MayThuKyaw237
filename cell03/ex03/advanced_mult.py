#!/usr/bin/env python3
import sys
if len(sys.argv) != 1:
    print("none")
    exit()
    
i = 0
while i <= 10:
    j = 0
    print(f"Table de {i}: ", end = "")
    while j <= 10:
        multiplication = i * j
        print(multiplication, end = " ")
        j += 1
    print()
    i += 1
    