'''
Exercise: menu

    In PyCharm, create a module ("Python file" from the "New" directory) called menu.py. This module will define a single function, menu, which will:
        accept any number of positional arguments
        display those positional arguments to the user
        ask the user to enter one of those arguments
        return whichever argument the user chose
        If the user doesn't choose any, they get into a loop until they do
    In PyCharm, create a separate file called usemenu.py. This program should use your menu module, and call the menu.menu function in it, passing it some values. It should then print whatever it got back from the user.

Example:

user_choice = menu.menu('a', 'b', 'c', 'd')
print(f'User chose {user_choice}')  # we know that this will be a, b, c, or d

'''