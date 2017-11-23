# -*- coding: utf-8 -*-

# Program to find Second Largest Number from an array

import types

def main():
    try:
        array_str_len = input()
        if type(array_str_len) != types.IntType:
            print "Please enter an Integer value to define the length of array!"
    except NameError:
        print "String Value is not acceptable! Please Enter an Integer Value!"
        main()
    except SyntaxError:
        print "You Entered something wrong! Please Enter an Integer Value!"
    array_str = raw_input()
    array_str_split = array_str.split()
    if len(array_str_split) != array_str_len:
        print "Length of array you mentioned doesn't matches with the number of elements you entered!]n Please try again!"
        main()
    array = []
    for rec in array_str_split:
        array.append(int(rec))
    array.sort()
    print array[-2]
    
main()
