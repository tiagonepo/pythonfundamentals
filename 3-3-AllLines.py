'''
Exercise: all_lines

    Write a function, all_lines, that takes at least one argument:
        Mandatory argument, outfilename, the name of a file into which we'll write our output
        Any number of optional arguments, infilenames, all filenames (strings) from which we want to read our input
    Go through each of the input filenames, read through them line by line, and write each of those lines into outfilename.
    The result of calling the function will be that all of the lines from the input files will be, in order, in the output file.

Example:

all_lines('myoutfile.txt', 'myinfile.txt', 'myinfile2.txt')  

Hints / thoughts:

    You'll want to open the file for writing ('w') using with
    *args is always a tuple with any unclaimed positional arguments
    You can iterate over a tuple

'''


def all_lines(out_file_name, *in_file_name):
    
    for each_file in in_file_name:
        with open(each_file) as in_file:
            for each_line in in_file:
                with open(out_file_name, 'w'):
                    #write the line on the out_file_name
                    s
#    return #print the out_file_name contend

#SOLUTION

#'''
#def all_lines(out_file_name, *in_file_name):
#
#    with open(out_file_name, 'w') as outfile:      # open output file for writing
#        for each_file in in_file_name:             # get each input filename
#            with open(each_file) as in_file:       # open each input file
#                for each_line in in_file:          # go through each line
#                    outfile.write(each_line)
#    
#all_lines('outfile.txt', '/etc/passwd', '/Users/reuven/.zshrc')
