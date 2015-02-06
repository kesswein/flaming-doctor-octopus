#!/usr/bin/env python3

# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ------------------------------

# -------
# imports
# -------

import sys

# ----
# main
# ----




def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

cache = [0 for i in range(1,2000000)]

def calc_collatz (i):
    """
    calculate cycle length of i
    """
    global cache
    temp = [0 for i in range(1,550)] #used to fill in cache later
    count = 1
    if cache[i] != 0:
        return cache[i]
    else:
        while i != 1:
            if i%2 == 0:
                i //= 2
            else:
                i *= 3
                i += 1
            if i <= 1000000:
                if cache[i] == 0:
                    temp[count] = i
                else:
                    for x in range (1, count):
                        cache[temp[x]] = count - x
                    cache[i] = count
                    return count
            count += 1
    return count

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    if i > j:
        temp = i
        i = j
        j = temp
    if i < j//2+1:
        i = j//2+1
    greatest = 1
    for x in range (i, j+1):
        cycl_len = calc_collatz(x)
        if cycl_len > greatest:
            greatest = cycl_len
    return greatest

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """

    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)

if __name__ == "__main__" :
    collatz_solve(sys.stdin, sys.stdout)

"""
% cat RunCollatz.in
1 10
100 200
201 210
900 1000



% RunCollatz.py < RunCollatz.in > RunCollatz.out



% cat RunCollatz.out
1 10 1
100 200 1
201 210 1
900 1000 1



% pydoc3 -w Collatz
# That creates the directory Collatz.html
"""
