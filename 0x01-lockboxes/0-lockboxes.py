#!/usr/bin/python3
'''Lockboxes'''


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened'''
    opened = set()
    opened.add(0)
    box = boxes[0]
    helper(boxes, box, opened)
    return len(opened) == len(boxes)

def helper(boxes, box, opened):
    if len(opened) == len(boxes) or len(box) == 0:
        return
    for key in box:
        if key in opened:
            continue
        opened.add(key)
        helper(boxes, boxes[key], opened)

