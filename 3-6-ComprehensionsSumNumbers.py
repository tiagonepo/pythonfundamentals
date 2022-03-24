
'''Exercise: Summing numbers (and only numbers)

    Ask the user to enter a string containing integers, separated by spaces
    Use a list comprehension to sum the numbers in the string.
    If there are non-numeric elements in the string, ignore them.

Example:

    Enter numbers: 10 20 abcd 30
    60'''




s = input('Enter numbers: ').strip()
sum([int(one_item) for one_item in s.split()])

#solution


'''s = input('Enter numbers: ').strip()

sum([int(one_number)
    for one_number in s.split()
    if one_number.isdigit() ])'''