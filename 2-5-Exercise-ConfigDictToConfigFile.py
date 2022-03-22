'''

Exercise: Config dict to config file

The idea here is that we'll create a configuration dictionary from the user's inputs, and then we'll write that dict to a file, in the format of name=value on each line, with one line for each key-value pair in the dict.

    Start with an empty dict, config.
    Ask the user to enter a string in the form of key=value, with the key before the = and the value after.
        If the user enters an empty string, stop asking.
        If the user's input lacks a =, then scold them and try again
    Stick the key and value into a dict, as key and value. (The value will always be a string.)
    When the user finishes entering keys and values, print the dict.
    Then write the dict to a file (config.txt), with each key-value pair on a line of the file.

Example:

Enter config: a=100
Enter config: name=Reuven
Enter config: hello
    Invalid; ignoring
Enter config: company=Cisco
Enter config: [ENTER]

{'a':'100', 'name':'Reuven', 'company':'Cisco'}

We'll also have a file, config.txt, that looks like this:

a=100
name=Reuven
company=Cisco

'''

''' 
#SOLUTION

# Turn user input into a dict
config = {}

while True:
    print(f'{config=}')  
    s = input('Enter config: ').strip()
    
    if not s:    # empty string? stop asking -- exit the loop
        break
        
    if '=' not in s:   # make sure that there's an = in s
        print('Invalid; ignoring')  
        continue
        
    key, value = s.split('=')  # use unpacking
    config[key] = value  # add the key-value pair to our dict

# Turn the dict into a file

with open('config.txt', 'w') as f:        # open the file, and auto-close at the end of the block
    for key, value in config.items():     # go through each key-value pair in the dict
        f.write(f'{key}={value}\n')       # write the current key-value pair to our file on a single line
'''