#!/usr/bin/env python3
inp_mult1 = int(input("Enter the first number: \n"))
inp_mult2 = int(input("Enter the second number: \n"))

multiplication = inp_mult1 * inp_mult2
print(f"{inp_mult1} x {inp_mult2} = {multiplication}")
if multiplication > 0:
    print("The result is positive.")
elif multiplication < 0:
    print("The result is negative.")
elif multiplication == 0:
    print("The result is positive and negative.")

