#!/usr/bin/python3


"""this determines the no of minimum operations given to n"""

def minioperations(n):
    """ number of minimum operations"""

    now = 1
    start = 0
    counter = 0
    while now < n:
        reminder = n - now
        if (reminder % now == 0):
            start = now
            now += start
            counter +=  2
        else:
            now += start
            counter += 1
        return counter
