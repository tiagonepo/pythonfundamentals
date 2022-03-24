'''
Exercise: Count vowels from a file

    Write a function, count_vowels, which takes a single argument, a filename.
    The function should return a dict, whose keys are the vowels (a, e, i, o, u) and whose values are the number of times each of those vowels appeared in the file.

Hints/thoughts:

    If you iterate over a file, then you get each line of the file as a string.
    You can iterate over a string, as well, getting each character.

'''

#mycode
def count_vowels(filename, chars):
    counts = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

    for one_character in filename:
        if one_character in 'aeiou':
            counts[one_character] += 1 

    return counts

count_vowels('wcfile.txt', a)





'''
#solution

def count_vowels(filename):
    counts = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    
    for one_character in open(filename).read():
        if one_character in counts:
            counts[one_character] += 1
    return counts
'''