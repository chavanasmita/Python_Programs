# -*- encoding: utf-8 -*-
#REF  : http://www.mathwarehouse.com/algebra/linear_equation/write-equation/equation-of-line-given-two-points.php
#Accepting line 1 end point co-ordinates 
l1_x1 = int(raw_input())
l1_y1 = int(raw_input())
l1_x2 = int(raw_input())
l1_y2 = int(raw_input())

#Accepting line 2 end point co-ordinates
l2_x1 = int(raw_input())
l2_y1 = int(raw_input())
l2_x2 = int(raw_input())
l2_y2 = int(raw_input())

line1_slope = (l1_y2 - l1_y1) / (l1_x2 - l1_x1)
x1 = l1_x1
y1 = l1_y1
b1 = y1 / (line1_slope * x1)

line2_slope = (l2_y2 - l2_y1) / (l2_x2 - l2_x1)
y2 = l2_y1
x2 = l2_x1
b2 = y2 / (line2_slope * x2)

if line1_slope == line2_slope:
    if b1 == b2:
        return "OVERLAP"
    else:
        return "NO"
else:
    return "INTERSECT"


