def nine_lines():
    #printing nine lines
    three_lines()
    three_lines()
    three_lines()

def new_line():
    print('.')

def three_lines():
    new_line()
    new_line()
    new_line()

def clear_screen():
    # print 25 lines with clear_screen
    print('Calling clearscreen and print 25 lines')
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()

print('Printing nine lines')
nine_lines()
clear_screen()