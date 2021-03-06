"""
keywordargument.py

Pass a keyword argument to a function.
The first two arguments are positional arguments.  They are required.
The third argument is a keyword argument.  It is optional and defaults to 0.
"""

import sys

def printLocation(latitude, longitude, altitude = 0):
    print(latitude, longitude, altitude)

printLocation(40, -75)
printLocation(40, -75, 1000)
printLocation(40, -75, altitude = 1000)
sys.exit(0)
