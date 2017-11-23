# -*- coding: utf-8 -*-
# this is a program which accepts an array as input and returns the difference between sum of odd numbers and sum of even numbers.

import types

def accept_len_of_array():
    try:
        len_of_array = input()
        if type(len_of_array) == types.IntType:
            return len_of_array
        else:
            print "Please enter an Integer!"
            len_of_array = accept_len_of_array()
    except NameError:
        print "Please enter an integer!"
        len_of_array = accept_len_of_array()
    except SyntaxError:
        print "Please enter an Integer!"
        len_of_array = accept_len_of_array()
    return len_of_array

def accept_array_elements(array_len):
    array = raw_input()
    array_elements = array.split()
    
    if len(array_elements) != array_len:
        print "%d elements expected, you entered wrong number of elements!\n Please enter elements again."%(array_len)
        array_elements = accept_array_elements(array_len)
    else:
        return array_elements
        
    return array_elements
#    except 

def main():
    len_of_array = accept_len_of_array()
    array = accept_array_elements(len_of_array)
    array_list = [int(el) for el in array]
    even = []
    odd = []
    sum_even = 0
    sum_odd = 0
    diff = 0
    for number in array_list:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    for e in even:
        sum_even += e
    for o in odd:
        sum_odd += o
    if sum_even > sum_odd:
        diff = sum_even - sum_odd
    elif sum_odd > sum_even:
        diff = sum_odd - sum_even
    print diff
main()
