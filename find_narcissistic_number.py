# -*- coding: utf-8 -*-

# Program to find out Narcissistic Number

import types

def main():
    try:
        number = input()
    except NameError:
        print "String Value is not allowed!\n Please Enter an Integer Number."
        main()
    except SyntaxError:
        print "You Entered something wrong!\n Please Enter an Integer Number."
        main()
    
    if type(number) != types.IntType:
        print "Please Enter an Integer Value!"
        main()
    else:
        num_str = str(number)
        len_number = len(num_str)
        sum = 0
        for digit in num_str:
            i_digit = int(digit)
            sum += i_digit ** len_number
        if sum == number:
            print True
        else:
            print False

main()
