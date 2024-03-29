#!/usr/bin/python3
'''
Rotate 2D Matrix
'''


def rotate_2d_matrix(matrix):
    '''Rotate 2D Matrix'''
    new_matrix = [[raw[i] for raw in matrix] for i in range(len(matrix[0]))]
    for y in range(len(new_matrix)):
        i = 0
        for x in range(len(new_matrix[y]) - 1, -1, -1):
            matrix[y][i] = new_matrix[y][x]
            i += 1
