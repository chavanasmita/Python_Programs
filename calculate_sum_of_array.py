# -*- coding: utf-8 -*-

import types

def accept_length_of_array():
    length_of_array = input()
    if isinstance(length_of_array, types.IntType):
        return length_of_array
    else:
        print "Integer Value Expected!\n Value entered by you is not an Integer, Please Enter an Integer value."
        length = accept_length_of_array()
    return length

def accept_array_elements(array_length):
    array_elements = raw_input()
    array = array_elements.split()
    if len(array) == array_length:
        return array
    else:
        print "You have entered %s elements, but %s elements expected!"%(len(array), array_length)
        array_elements = raw_input()
        array = array_elements.split()
    return array

def main():
    length_of_array =  accept_length_of_array()
    elements = accept_array_elements(length_of_array)
    sum_of_array = 0
    for element in elements:
        sum_of_array += int(element)
    print sum_of_array

main()
