#!/usr/bin/python3
'''Lockboxes'''


def canUnlockAll(boxes):
    '''Determines if all the boxes can be opened.'''
    if not isinstance(boxes, list):
        raise TypeError("Input must be a list of boxes.")
    opened = set()
    opened.add(0)
    first_box = boxes[0]
    dfs(boxes, first_box, opened)
    return len(opened) == len(boxes)


def dfs(boxes, current_box, opened):
    '''Depth-First Search helper function.'''
    if len(current_box) == 0:
        return

    for key in current_box:
        if key not in opened:
            opened.add(key)
            dfs(boxes, boxes[key], opened)
