
'''
Exercises:

    Ask the user to enter a sentence. Print the words of the sentence, sorted by word length (from shortest to longest).
    Ask the user to enter a sentence. Print the words of the sentence, sorted by the number of vowels in the word (from least to greatest).

'''


#mycode
#step 1
sentence = 'This is a bunch of words for my Python course at Cisco'.split()
print(sentence)
sorted_sentence = sorted(sentence, key=len)
print(sorted_sentence)

#step 2


#solution
'''
def count_vowels(one_word):
    total = 0
    
    for one_letter in one_word.lower():
        if one_letter in 'aeiou':
            total += 1
            
    return total

sorted(s, key=count_vowels)

'''