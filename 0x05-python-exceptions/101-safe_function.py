#!/usr/bin/python3
# 101-safe_function.py
import sys
def safe_function(fct, *args):
"""Executes a functn
Args:
fct: The function to execute.
args: for fct.
Returns:
If an error occurs - None.
Otherwise - call to fct.
"""
try:
result = fct(*args)
return (result)
except:
print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
return (None)
