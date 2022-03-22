'''
Exercise: Vowels, digits, and others

    Define a dict, counts, in which there are three keys (vowels, digits, and others), all set to 0.
    Ask the user to enter a string.
    Go through the string, and check if each character is a vowel (a, e, i, o, u), a digit (0-9), or something else. Add 1 to the appropriate count in the counts dict.
    After going through the user's string, print the counts dict.

Example:

Enter a string: testing 123
{'vowels': 2, 'digits': 3, 'others': 6 }

'''



#mycode
counts = {'vowels':0, 'digits':0, 'other':0}

string = input('Enter a string:').strip()

for char in string:
    if char in 'aeiou':
        counts['vowels'] += 1
    elif char.isdigit():
        counts['digits'] += 1
    else:
        counts['other'] += 1

print(counts)



'''
#SOLUTION


counts = {'vowels':0, 'digits':0, 'others':0}

s = input('Enter string: ').strip()

for one_character in s:
    if one_character in 'aeiou':
        counts['vowels'] += 1
    elif one_character.isdigit():
        counts['digits'] += 1
    else:
        counts['others'] += 1
        
print(counts) 

'''