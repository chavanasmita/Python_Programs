# -*- coding: utf-8 -*-
import sys
import os

def getJoinedPipes(input1):
    if len(input1) > 1:
        pipe_sum = {}
        import itertools
        sum_rec = []
        for x in itertools.permutations(input1, len(input1)):
            sum_i = 0
            sum_i_list = []
            for i in range(0, len(x)-1):
                if not sum_i:
                    sum_i = x[i] + x[i+1]
                else:
                    sum_i = sum_i + x[i+1]
                sum_i_list.append(sum_i)
            if sum_i_list:
                sum_i_list.sort()
            sum_rec.append((x, sum_i_list, sum(sum_i_list)))
        min_sum = min([x[2] for x in sum_rec])
        min_sum_rec = [x[1] for x in sum_rec if x[2]==min_sum]
        min_sum_key = [x[0] for x in sum_rec if x[2]==min_sum]
        if len(min_sum_rec) > 1:
            if_all_same = all(x==min_sum_rec[0] for x in min_sum_rec)
            if if_all_same:
                return min_sum_rec[0]
            else:
                return min_sum_rec[0]
        elif len(min_sum_rec) == 1:
            return min_sum_rec[0]
    else:
        return []

ip1_cnt = 0
ip1_cnt = int(raw_input())
ip1_i=0
ip1 = []
while ip1_i < ip1_cnt:
    ip1_item = int(raw_input());
    ip1.append(ip1_item)
    ip1_i+=1
output = getJoinedPipes(ip1)
for output_cur in output:
    print( str(output_cur))