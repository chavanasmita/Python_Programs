# -*- coding: utf-8 -*-

## Program to find whether number is prime or not
#
#number = input()
#if number > 1:
#    is_prime = True
#    for i in range(2, number):
#        if (number%i) == 0:
#            is_prime = False
#print "The number is prime: ", is_prime


# Program to find prime numbers within range

import types

def main():
    try:
        lower_range = input()
        if type(lower_range) != types.IntType:
            print "Please Enter Integer value!\n"
            lower_range = input()
    except NameError:
        print "String Value is not acceptable"
        main()
    except SyntaxError:
        print "You entered something wrong!\n Please enter an integer value specifying starting range."
        main()
        
    try:
        upper_range = input()
        if type(upper_range) != types.IntType:
            print "Please Enter Integer value!\n"
            upper_range = input()
    except NameError:
        print "String Value is not acceptable"
        main()
    except SyntaxError:
        print "You entered something wrong!\n Please enter an integer value specifying upper range."
        main()
    

    prime_numbers = []
    
    for number in range(lower_range, upper_range+1):
        if number > 1:
            is_prime = True
            for i in range(2, number):
                if (number%i) == 0:
                    is_prime = False
            if is_prime:
                prime_numbers.append(str(number))
    
    print "There are %s prime numbers which lies in the given range."%(len(prime_numbers))
    print "They are %s"%(','.join(prime_numbers))

main()
            
                
        
