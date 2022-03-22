'''
Exercise: Address book

    We're going to keep track of people in an address book. For each person, we'll have four fields: first name, last name, email, and phone number.
    We're going to use a list of dicts. Each dict will have name-value pairs for those four fields.
    The user will be able to enter a one-letter command. Based on the command, the program will know what to do:
        q -- quit from the program
        a -- add a new person to the database. The program will ask four separate questions, and we'll use those answers to create a new dict, which will be added to the list.
        l -- list all of the people in the database
        f -- find -- ask the user to enter a search string, and show all of the people's records whose first name and/or last name contain the search string

Below this line is nice to have, but not crucial

- `w` -- write current data to a file on disk.  You can separate fields with tab (`\t`), and writing the file should destroy any previously written file.  The filename can be hard-coded into the program.
- `r` -- read data from a file on disk.  Before loading, remove any existing people from the database, so that loading from a file overwrites anything previously there.

'''



#mycode
address_book = [{'first':'Tiago', 'last':'Nepomuceno', 'email':'tiago@gmail.com', 'phone':'911234567'},
                {'first':'Joao', 'last':'Cruz', 'email':'joao@gmail.com', 'phone':'917654321'},
                {'first':'Jose', 'last':'Gomes', 'email':'jose@gmail.com', 'phone':'921234567'},]


commands = ['q', 'a', 'l', 'f']


command_input = input('Please insert the command: ').strip()

while True:
    if command_input == 'q':
        break
    elif command_input == 'a':
        name_input = input('Please insert the name: ').strip()
        address_book.append({'first':name_input})
 #   elif command_input == 'l':

  #  else command_input == 'f':







