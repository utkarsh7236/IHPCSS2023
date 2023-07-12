#!/usr/bin/env python

# auc_serial.py

import sys

def main():
 if len(sys.argv) < 2:
    print ("Error: must supply a number of points as a command line argument")
 else:
    ntot  = int(sys.argv[1])
    width = 3.0
    dx    = width/ntot
    x = 0
    a = 0.0
    for i in range(ntot):
        y = 0.7*x**3 - 2*x**2 + 4
        a += y*dx
        x += dx
    print("The area is %f"%a)

if __name__ == "__main__":
  main()
