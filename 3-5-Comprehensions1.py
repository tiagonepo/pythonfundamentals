
'''Exercises with comprehensions

    Ask the user to enter a string containing integers, separated by whitespace. Print the total of those numbers, when added together.

Example:

Enter a string: 10 20 30
60

    Ask the user to enter a sentence. Print the total number of non-whitespace characters in that sentence.

Example:

Enter a sentence: This is a test
11

    In both cases, you should use a list comprehension.
    You'll have to use both str.split and str.join in both of these.'''



#my code
integers = input("Enter integers, separated by whitespace: ").strip()

splited_integers = integers.split(' ')
print(splited_integers)

[sum_integers ]



#solution

# sum numbers, from a string
'''s = input('Enter numbers: ').strip()
sum([int(one_item)
     for one_item in s.split()])'''


# print the number of non-whitespace characters in the user's input
'''s = input('Enter a sentence: ').strip()
sum([len(one_word)
 for one_word in s.split()])'''