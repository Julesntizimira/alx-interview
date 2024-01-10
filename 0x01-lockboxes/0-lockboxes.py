#!/usr/bin/python3
'''Lockboxes'''


def canUnlockAll(boxes):
    if not boxes or not boxes[0]:
        return False  # No boxes or the first box is empty, cannot unlock all.

    n = len(boxes)
    visited = set()
    stack = [0]  # Start with the first box.

    while stack:
        current_box = stack.pop()
        visited.add(current_box)

        for key in boxes[current_box]:
            if key not in visited and 0 <= key < n:
                stack.append(key)

    return len(visited) == n

