
'''
Exercise: Summing numbers

Each line in the file nums.txt has up to one integer on it, surrounded by some amount of whitespace. More specifically: Every line contains one integer, along with some whitespace, except for one of the lines, which has only whitespace and no integer on it.

Use a list comprehension to add the values in nums.txt.
'''


file = open('nums.txt').read()
#print(file)

summ = sum([int(one_line)
            for one_line in file.strip()
            if one_line.isdigit() ])
print(summ)


#solution

'''summ = sum([int(one_line)
            for one_line in open('nums.txt')
            if one_line.strip().isdigit() ])
print(summ)'''