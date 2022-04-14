

# this function will get the extension of a filename
# it uses a linear search (backwards) for demonstration purposes
#
# there are much better ways to do this, such as regular expressions
# libraries, and slicing, however this demonstrates linear search
def get_extension(name):
    dot = -1
    ext = ""
    # first make sure we have a valid string
    if name and type(name) == str:
        # now loop through the filename backwards looking for the last '.'
        i = len(name)-1
        while(i >= 0 and dot == -1):
            if name[i] == '.':
                dot = i
            i -= 1
    if dot != -1:
        ext = name[dot:]

# simple linear search to find number of spaces in a string. there are
# better ways to do this however this demonstrates linear search
def count_spaces(string):
    spaces = 0
    if string and type(string) == str:
        for ch in string:
            if ch == ' ':
                spaces += 1
    return spaces

# simple function to print a text file with line
# numbers and number of spaces per line
def print_file(fin):
    # make sure we have a readable object
    try:
        # do a priming read
        line = fin.readline()
    except:
        line = None
        print("error, that is not a file")

    i = 1
    # process file
    while line:
        print(str(i) + ": " + line[:-1] + " [spaces = " +str(count_spaces(line)) + "]")
        line = fin.readline()
        i += 1

