# -*- coding: utf-8 -*-

# Program to find factorial of a number

import types

def main():
    try:
        number = input()
        factorial = 1
        
        if type(number) == types.FloatType:
            print "Please Enter Integer value!\n";
            main();
        elif type(number) not in (types.IntType, types.FloatType):
            print "You entered something wrong!\n Please Enter an Integer value!\n";
            main();
        elif type(number) == types.IntType:
            while number != 0:
                 factorial *= number
                 number -= 1
        print factorial
    except NameError:
        print "String is not acceptable!\n Please Enter an Integer value!\n"
        main()
    except SyntaxError:
        print "You entered something wrong!\n Please Enter an Integer value!"

main()