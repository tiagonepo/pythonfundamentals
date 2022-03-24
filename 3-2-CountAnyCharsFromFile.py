'''
Exercise: Count vowels from a file

    Write a function, count_vowels, which takes a single argument, a filename.
    The function should return a dict, whose keys are the vowels (a, e, i, o, u) and whose values are the number of times each of those vowels appeared in the file.

Hints/thoughts:

    If you iterate over a file, then you get each line of the file as a string.
    You can iterate over a string, as well, getting each character.

'''

#mycode
def count_chars(filename, chars='aeiou'):
    counts = {} 

    with open(filename) as file:
        for one_line in file:
            for one_character in one_line: 
                if one_character in chars:
                    counts[one_character] = counts.get(one_character, 0) + 1 
                
    return counts
count_chars('wcfile.txt', 'a')





'''
#solution

'''