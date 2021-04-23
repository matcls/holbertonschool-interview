#!/usr/bin/python3
"""Lockboxes Algorithm."""


def canUnlockAll(boxes):
    """Determine if all the boxes can be opened.

    Args:
        boxes (List of lists): Represent the boxes.

    Returns:
        Boolean: True if all boxes can be opened, else return False.
    """
    if not boxes:
        return False
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)

    return len(keys) == len(boxes)
