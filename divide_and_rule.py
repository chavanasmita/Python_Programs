# -*- encoding: utf-8 -*-
import sys
import os
import itertools
import copy


def divideAndRule(input1):
    output1 = []
    for subset in itertools.combinations(input1, (len(input1) - 1) / 2):
        output1.append(subset)
    sum_output = map(sum, output1)
    zipped_output = zip(output1, sum_output)
    matched_flags = []
    for e in zipped_output:
        zipped_output_copy = copy.copy(zipped_output)
        zipped_output_copy.remove(e)
        matched_element = filter(lambda x: x[1]==e[1], zipped_output_copy)
        zipped_output.remove(e)
        for m in matched_element:
            zipped_output.remove(m)
            if set(m[0]+e[0]).issubset(set(input1)):
                intersect = set(input1).intersection(set(m[0]+e[0]))
                if len(intersect) == 1:
                    final_list = list(m[0]) + list(e[0]) + list(intersect)
                    final_list.sort()
                    input1.sort()
                    if final_list == input1:
                        matched_flags.append(True)
                        return 1
    if not matched_flags or not any(matched_element):
        return -1

ip1_cnt = 0
ip1_cnt = int(raw_input())
ip1_i=0
ip1 = []
while ip1_i < ip1_cnt:
    ip1_item = int(raw_input());
    ip1.append(ip1_item)
    ip1_i+=1
output = divideAndRule(ip1)
print(str(output))
