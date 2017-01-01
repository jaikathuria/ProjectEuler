#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = long(raw_input().strip())
    a=0
    b=1
    c=0
    sum=0
    while(c<=n):
        c = a + b
        a = b
        b = c
        if (c%2 == 0 and c <=n):
            sum +=c
    print sum
