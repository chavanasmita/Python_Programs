# -*- coding: utf-8 -*-

# Program to find UpperCase and LowerCase letters in String

import types

def main():
    try:
        input_str = raw_input()
        upper_case_letters = 0
        lower_case_letters = 0
        if isinstance(input_str, types.StringType):
            for letter in input_str:
                if letter.isupper():
                    upper_case_letters += 1
                elif letter.islower():
                    lower_case_letters += 1
        print upper_case_letters
        print lower_case_letters
    
    except SyntaxError:
        print "You Entered Something Wrong! Please Enter a string!"
        main()
    

main()
