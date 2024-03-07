#!/usr/bin/python3
'''
Island Perimeter
'''


def island_perimeter(grid):
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                if grid[i][j - 1] == 1:
                    perimeter -= 1
                if grid[i][j + 1] == 1:
                    perimeter -= 1
                if grid[i + 1][j] == 1:
                    perimeter -= 1
                if grid[i - 1][j] == 1:
                    perimeter -= 1
    return perimeter
