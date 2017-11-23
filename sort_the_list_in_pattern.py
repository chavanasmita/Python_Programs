# -*- encoding: utf-8 -*-
# sort the list so that it will return list in such pattern, [first max, first min, second max, second min, and so on...]

def alternateSorting(input1):
    input1.sort()
    len_divide_by_2 = len(input1) / 2
    reminder = len(input1) % 2
    output = []
    for i in range(1, len_divide_by_2+1):
        output.append(input1[i * (-1)])
        output.append(input1[i-1])
    
    if reminder:
        output.append(input1[len_divide_by_2])
    return output

ip1_cnt = 0
ip1_cnt = int(raw_input())
ip1_i=0
ip1 = []
while ip1_i < ip1_cnt:
    ip1_item = int(raw_input());
    ip1.append(ip1_item)
    ip1_i+=1
output = alternateSorting(ip1)
for output_cur in output:
    print( str(output_cur))