
'''Exercise: XML generator

Write a function, xml, that takes 1 or 2 positional arguments, and any number of keyword arguments:

- First parameter is `tagname`, which will be the name of the tag we write
- Second parmaeter is optional, called `text`, which contains the text (if any) we want in our XML.
- Third parameter takes any number of keyword arguments, and places them as attributes (name-value pairs) in the opening tag.

The function returns a string containing XML.
'''


#mycode

'''
#step 1
def xml(tagname):
    x = tagname
    print(f'<{x}></{x}>')
xml('a')'''

'''
#step 2
def xml(tagname, text, **atrib):
    x = tagname
    y = text
    print(f'<{x}>{y}</{x}>')
xml('body', 'hello')'''

#step 3
def xml(tagname, text, **atrib):
    x = tagname
    y = text
    for key, value in atrib:
        z = (f'{key}="{value}"')
    print(f'<{x} {z}>{y}</{x}>')
xml('body', 'hello', a=1)


'''#SOLUTION

#step 1
def xml(tagname):
    return f'<{tagname}></{tagname}>'

xml('a')

#step 2
def xml(tagname, text):
    return f'<{tagname}>{text}</{tagname}>'

xml('body', 'hello')


#step 3
def xml(tagname, text='', **atrib):
    z = ''
    for key, value in atrib.items():  # this gives us one key-value pair for each iteration
        z += f' {key}="{value}"'
    return f'<{tagname} {z}>{text}</{tagname}>'
xml('body', 'hello', a=1, b=2, c=3)'''



