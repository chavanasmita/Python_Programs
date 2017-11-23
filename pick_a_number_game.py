import sys
import os

'''Complete the function below.'''
def amount_value(input1):
    blocks = []
    #create grid
    for i in range(0, len(input1)):
        blocks.append([int(x) for x in input1[i].split('#')])
    search = []
    visited_node = []
    def get_node_details(row, col):
        neighbours = []
        self_node = blocks[row][col]
        if (row+1) < len(input1):
            neighbours.append(blocks[row+1][col])
        if (col+1) < len(input1):
            neighbours.append(blocks[row][col+1])
        if (row+1) < len(input1) and (col+1) < len(input1):
            neighbours.append(blocks[row+1][col+1])
        if (row-1) >= 0:
            neighbours.append(blocks[row-1][col])
        if (col-1) >= 0:
            neighbours.append(blocks[row][col-1])
        if (row-1) >= 0 and (col-1) >= 0:
            neighbours.append(blocks[row-1][col-1])
        neighbours.append(self_node)
        max_possible = max(neighbours)
        min_possible = min(neighbours)
        search.append({'visited_node': (row, col),
                       'max': max_possible,
                       'min': min_possible})
    for i in range(0, len(input1)):
        for j in range(0, len(input1)):
            get_node_details(i, j)
    sorted_search = sorted(search, key=lambda x: x.get('min'), reverse=True)
    min_amt = sorted_search[0].get('min')
    searched_items = filter(lambda x: x.get('min') == min_amt, sorted_search)
    output = []
    for item in searched_items:
        pos = item.get('visited_node')
        output_str = str(pos[0]+1) + '#' + str(pos[1]+1)
        output.append(output_str)
    return output
ip1_cnt = 0
ip1_cnt = int(raw_input())
ip1_i = 0
ip1 = []
while ip1_i < ip1_cnt:
    try:
        ip1_item = raw_input()
    except:
        ip1_item = None
    ip1.append(ip1_item)
    ip1_i += 1
output = amount_value(ip1)
for output_cur in output:
    print(str(output_cur))
