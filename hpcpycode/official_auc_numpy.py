#!/usr/bin/env python

# auc_serial.py

import sys
import numpy as np

def main():
 if len(sys.argv) < 2:
    print ("Error: must supply a number of points as a command line argument")
 else:
    ntot  = int(sys.argv[1])
    width = 3.0
    dx    = width/ntot
    x = np.arange(0,width,dx)
    y = 0.7*x**3 - 2*x**2 + 4
    a = y.sum()*dx
    print("The area is %f"%a)

main()
