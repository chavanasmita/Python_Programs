# -*- coding: utf-8 -*-

# Program to check whether given number is armstrong number or not

import types

def main():
    try:
        number = input()
        if type(number) != types.IntType:
            print "Please enter an Integer value!\n"
            main()
        else:
            num_str = str(number)
            sum_digit_cube = 0
            for i in num_str:
                i_digit = int(i)
                i_digit_cube = i_digit ** 3
                sum_digit_cube += i_digit_cube
            if sum_digit_cube == number:
                print True
            else:
                print False
    except (NameError, SyntaxError):
        print "You entered something wrong!\n"
        main()

main()
