# -*- coding: utf-8 -*-

# This program will get a string of numbers as input and will return  longest substring length which is palindrome

def lengthofPalindrome(input1):
    avlbl_numbers = {}
    for j in range(len(input1), 1, -1):
        if j % 2 == 0:
            chunks, chunk_size = len(input1), j
            substr_j = [ input1[i:i+chunk_size] for i in range(0, chunk_size)]
            substr_j = [x for x in substr_j if len(x)==j]
            for rec in substr_j:
                import itertools
                perms = [''.join(p) for p in itertools.permutations(rec)]
                is_palindrome = False
                for p in perms:
                    if p == p[::-1]:
                        return j
    return 0

try:
    ip1 = raw_input()
except:
    ip1 = None
output = lengthofPalindrome(ip1)
print(str(output))