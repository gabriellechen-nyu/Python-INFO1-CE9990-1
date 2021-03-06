"""
passlist.py

Pass a list or tuple to a function that expects one argument (line 24),
and to a function that expects to receive each item on the list as a separate
argument (line 25).
"""

import sys

def threeArgs(arg0, arg1, arg2):
    print("threeArgs:", arg0, arg1, arg2)

def oneArg(arg0):
    assert isinstance(arg0, list) or isinstance(arg0, tuple)
    print("oneArg:", end = "")
    for arg in arg0:
        print(" ", arg, sep = "", end = "")
    print()

threeArgs("Moe", "Larry", "Curly")

stooges = ["Moe", "Larry", "Curly"]
oneArg(stooges)
threeArgs(*stooges)
sys.exit(0)
