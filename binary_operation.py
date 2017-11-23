# -*- coding: utf-8 -*-
# Programs to check how many numbers of bits are remained unchanged 

def nochange_bits(input1, input2, input3):
    if input2 > 0 and input3 > 0:
        input_list = [int(l) for l in input1]
        import copy
        input_after_op = copy.copy(input_list)
        rep2 = len(input1)/input2
        for i in range(1, rep2+1):
            i_index = (rep2*i -1)
            i_item = input_after_op[i_index]
            del input_after_op[i_index]
            if i_item == 0:
                input_after_op.insert(i_index, 1)
            elif i_item == 1:
                input_after_op.insert(i_index, 0)
        rep3 = len(input1)/input3
        for i in range(1, rep3+1):
            i_index = (rep3*i -1)
            i_item = input_after_op[i_index]
            del input_after_op[i_index]
            if i_item == 0:
                input_after_op.insert(i_index, 1)
            elif i_item == 1:
                input_after_op.insert(i_index, 0)
        unchanged_items = [i for i, j in zip(input_list, input_after_op) if i == j]
        return len(unchanged_items)
    elif not input2 > 0:
        return -1
    elif not input3 > 0:
        return -1
    
    
try:
    ip1 = raw_input()
    ip2 = int(raw_input());
    ip3 = int(raw_input());
except:
    ip1 = None
    ip2 = None
    ip3 = None

output = nochange_bits(ip1,ip2,ip3)
print(str(output))
