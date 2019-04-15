# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:53:04 2019

@author: ttc
"""

# Case 1, an exception is caught
#%%
try:
    items = ['a', 'b']
    third = items[2]
    print("This won't print")
except IndexError:
    print("Index out of bound")

print("continuing")

# Case 2, a division by zero exception won't caught by IndexError
#%%
try:
    x = 5
    y = x/0
    print("This won't print, either")
except IndexError:
    print("Division by zero is handled by wrong exception")

print("continuing again")

# Case 3, a division by zero is caught correctly
#%%
try:
    x = 5
    y = x/0
    print("This won't print, either")
except ZeroDivisionError:
    print("Division by zero is handled correctly")

print("continuing again")

# Case 4, a division by zero is handled universaly
#%%
try:
    x = 5
    y = x/0
    print("This won't print, either")
except Exception as e:
    print("Division by zero is handled by a universal handler")
    print(e)

print("continuing again")

# Case 5 more control on exceptions
#%%
try:
    y = 5 / 0
except Exception as e:
    print ("Exception ",e)
else:
    print ("y is", y)
finally:
    print ("executing finally clause")


# User defined exceptions
#%%
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr("MyError")
    
try:
    raise MyError(4)
except MyError as e:
    print ('My exception occurred, value:', e)