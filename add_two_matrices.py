# -*- coding: utf-8 -*-

# Program to Add two matrices

import types

def get_row_of_matrix(column):
    try:
        row_val = raw_input()
        row_val_list = row_val.split()
        if len(row_val_list) == column:
            return row_val_list
        else:
            print "number of elements entered by you, doesn't matches with matrix dimension!\n"\
            " You should enter %s elements"%(column)
            row_val_list = get_row_of_matrix(column)
        return row_val_list
    except Exception as e:
        print e

def get_matrix():
    try:
        dim_of_matrix = raw_input()
        dim_list = dim_of_matrix.split()
        mat_vals = []
        if len(dim_list) == 2:
            mat_rows = int(dim_list[0])
            mat_cols = int(dim_list[1])
            for i in range(0, mat_rows):
                row_val_list = get_row_of_matrix(mat_cols)
                
                if row_val_list:
                    mat_vals.append(row_val_list)
            return mat_vals, mat_rows, mat_cols
        else:
            print "Please enter only 2 dimensions for matrix! \n Only two dimensional matrices are accepted.\n"
            "Please re-enter matrix dimension and value!"
            mat_vals, mat_rows, mat_cols = get_matrix()
        return mat_vals, mat_rows, mat_cols
    except Exception as e:
        print e
                

def main():
    mat_1_vals, mat_1_rows, mat_1_cols = get_matrix()
    mat_2_vals, mat_2_rows, mat_2_cols = get_matrix()
    
    # Modify Matrices if dimensions of two arrays differs from each other
    if mat_1_rows > mat_2_rows:
        row_diff = mat_1_rows - mat_2_rows
        for i in range(0, row_diff):
            row_val = []
            for j in range(0, mat_2_cols):
                row_val.append(0)
            mat_2_vals.append(row_val)
    
    if mat_2_rows > mat_1_rows:
        row_diff = mat_2_rows - mat_1_rows
        for i in range(0, row_diff):
            row_val = []
            for j in range(0, mat_1_cols):
                row_val.append(0)
            mat_1_vals.append(row_val)
        
    if mat_1_cols > mat_2_cols:
        col_diff = mat_1_cols - mat_2_cols
        for row in mat_2_vals:
            for i in range(0, col_diff):
                row.append(0)
    
    if mat_2_cols > mat_1_cols:
        col_diff = mat_2_cols - mat_1_cols
        for row in mat_1_vals:
            for i in range(0, col_diff):
                row.append(0)
            
    result = []
    for i in range(0, mat_1_rows):
        row_val = []
        for j in range(0, mat_1_cols):
            row_val.append(0)
        result.append(row_val)
    
    
    for i in range(0, mat_1_rows):
        for j in range(0, mat_1_cols):
            result[i][j] = str(int(mat_1_vals[i][j]) + int(mat_2_vals[i][j]))
     
    output_str = ''
    for i in range(0, len(result)):
        output_str += ' '.join(result[i]) + '\n'
    
    print output_str[:-1]

main()
