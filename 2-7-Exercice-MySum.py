'''
Exercise: mysum

Python comes with a function called sum that takes a list (or tuple or set) of integers, and returns their sum. I want you to write a new function, mysum, that takes a list of integers, and returns the sum of the integers there.

Note: Don't use the builtin sum function to write your mysum function.
'''

#mycode
int = (10, 20, 30)

def mysum():
    for each in int:
        sum += each 


'''
#SOLUTION

def mysum(numbers):
    total = 0
    
    for one_number in numbers:
        total += one_number
        
    return total

mysum([10, 20, 30])
'''