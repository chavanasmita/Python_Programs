'''
Program to find minimum number of routes can be disconnected to attack on any state.
INPUT : 
12   --> No. of routes exists in state connecting cities 
1#2  --> City 1 connects City 2
2#3
1#5
1#6
2#6
3#4
4#6
5#6
2#5
1#4
3#6
2#4

OUTPUT --> no. of routes to disconnect, so that 1 won't be connected to 6
'''

import sys
import os
'''Complete the function below.'''

def minRoads(input1):
    cities_list = []
    city_conn_list = []
    for con in input1:
        city_list = con.split('#')
        city_list = [int(x) for x in city_list]
        cities_list.extend(city_list)
        city_conn_list.append(tuple(city_list))
    base_station_1 = min(cities_list)
    base_station_2 = max(cities_list)
    conn_bs_1 = []
    conn_bs_2 = []
    for rec in city_conn_list:
        if rec[0] == base_station_1:
            conn_bs_1.append(rec)
        if rec[1] == base_station_2:
            conn_bs_2.append(rec)
    common_routes = set(conn_bs_1).intersection(set(conn_bs_2))
    if common_routes:
        if len(common_routes) == 1 and len(conn_bs_1) == 1:
            return 1
        else:
            return min(len(conn_bs_2), len(conn_bs_1))
    else:
        return min(len(conn_bs_2), len(conn_bs_1))
            

ip1_cnt = 0
ip1_cnt = int(raw_input())
ip1_i=0
ip1 = []
while ip1_i < ip1_cnt:
    try:
        ip1_item = raw_input()
    except:
        ip1_item = None
    ip1.append(ip1_item)
    ip1_i+=1
output = minRoads(ip1)
print(str(output))