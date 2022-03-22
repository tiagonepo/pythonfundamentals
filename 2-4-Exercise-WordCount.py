'''
'''

'''
#mycode
file = open('wcfile.txt')
lines = 1
words = 1
for one_line in file:
    lines = lines + 1
    for one_word in one_line:
        words = words + 1
print(lines)
print(words)

file.close()

'''



file = open('wcfile.txt')

print(file)
file.close()