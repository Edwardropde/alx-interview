#!/usr/bin/python3
"""
Text file has single character 'H'
Text Editor can only execute 'Copy All' and 'Paste'
Method that calculates fewest number of operations needed to result in
'n' and 'H' characters in the file
"""


def minOperations(n):
    """
    Method calculating fewest number of operations
    Required to result in 'n' and 'H' characters in file
    """
    if type(n) != int:
        return 0

    char = 1
    operator = 0
    memory_copy = 0

    while char < n:
        if n % char == 0:
            memory_copy = char
            operator += 1
            char *= 2
            operator += 1

        else:
            char += memory_copy
            operator += 1

    return operator
