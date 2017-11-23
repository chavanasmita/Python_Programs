# -*- coding: utf-8 -*-

# Find uncommon elements in 2 arrays

import types
import os

def uncommonBetweenCommon(list1, list2):
    intesection = list(set(list1).intersection(set(list2)))
    uncommon_item_list = [str(item) for item in list(set(list1).union(set(list2))) if item not in intesection]
    final_output = '$'.join(uncommon_item_list)
    return final_output

def get_integer_value(accept_array_length):
    integer = 0
    try:
        integer = input()
        if type(integer) != types.IntType:
            print "Please enter an Integer value to define number of students in first row!\n"
            get_integer_value(accept_array_length)
        elif type(integer) == types.IntType:
            if accept_array_length:
                if not 3 < integer < 1000000:
                    print "Number of students in a row should be in the range of 3..1000000!\n"
                    integer = get_integer_value(accept_array_length)
    except NameError:
        print "String Value is not acceptable! Please Enter an Integer Value!\n"
        integer = get_integer_value(accept_array_length)
    except SyntaxError:
        print "You Entered something wrong! Please Enter an Integer Value!\n"
        integer = get_integer_value(accept_array_length)
    return integer
    
array_1_length = get_integer_value(accept_array_length=True)
array_1_counter = 0
array_1 = []
while array_1_counter < array_1_length:
    array_1_item = get_integer_value(accept_array_length=False)
    array_1.append(array_1_item)
    array_1_counter += 1
    
array_2_length = get_integer_value(accept_array_length=True)
array_2_counter = 0
array_2 = []
while array_2_counter < array_2_length:
    array_2_item = get_integer_value(accept_array_length=False)
    array_2.append(array_2_item)
    array_2_counter += 1
output = uncommonBetweenCommon(array_1, array_2)

print output
    


