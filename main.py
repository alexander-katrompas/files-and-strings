#!/usr/bin/python3

# import the sys library to access argv
import sys
# import functions to access our functions
import functions as fn

def main():
    # --------------------------------------------------------------------
    # demonstrating sys and argv
    # --------------------------------------------------------------------

    # get the number of arguments which will always be 1 or more
    argc = len(sys.argv)
    print('Number of arguments:', argc, 'arguments.')

    # the program name itself is always in sys.argv[0]
    print('The program name is', sys.argv[0])
    print('The complete argument complete list is:', sys.argv)
    print()

    # --------------------------------------------------------------------
    # demonstrating various ways to loop which all produce the same result
    # --------------------------------------------------------------------

    print("loop through arguments using 'index in range' loop form")
    # this form is considerred the most standard and acceptable for all languages
    for i in range(argc):
        print("arg " + str(i) + ": " + sys.argv[i])
    print()

    print("loop through arguments using 'value in values' loop with separate index")
    # this form is genrally considerred 'novice' but acceptable
    i = 0
    for arg in sys.argv:
        print("arg " + str(i) + ": " + sys.argv[i])
        i += 1
    print()

    print("loop through arguments using 'value in values' loop and access the index")
    # this form is considerred the most Pythonic
    for arg in enumerate(sys.argv):
        print("arg " + str(arg[0]) + ": " + str(arg[1]))
    print()

    # --------------------------------------------------------------------
    # demonstrating working with a string. in this case, a filename    
    # --------------------------------------------------------------------

    # get the extention of proram name
    ext = fn.get_extension(sys.argv[0])
    print("The extension of the program name is:", ext)
    print()

    # --------------------------------------------------------------------
    # demonstrating working files
    # --------------------------------------------------------------------
    
    # print file passed in from the commnd line, line by line using a for loop
    # note we first check argc to see if there even is a parameter that could be a file
    if argc == 2:
        try:
            # this will fail if the parameter passed in is not a filename
            fin = open(sys.argv[1], "r")
        except:
            fin = None
            print("that is not a vaild file")

        if fin:
            print("Printing",sys.argv[1])
            print("---------------------------------------")
            for line in fin:
                print(line, end="")
            fin.close() # don't forget to close your files
            print("---------------------------------------")
    else:
        print("no file passed")
    print()

    # displaying file with line numbers and number of characters
    # this does not check for argc in range, it uses exceptions instead
    try:
        fin = open(sys.argv[1], "r")
        print("Printing", sys.argv[1])
        fn.print_file(fin)
        print("---------------------------------------")
        fin.close() # don't forget to close your files
    except IndexError:
        print("no file passed")
    except FileNotFoundError:
        print("that is not a vaild file")

main()

