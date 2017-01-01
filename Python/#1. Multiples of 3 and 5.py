#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    n = n-1
    n3 = (n-(n%3))/3
    n5 = (n-(n%5))/5
    n15 = (n-(n%15))/15
    # for sum
    s3 = (n3*(n3+1)/2)*3
    s5 = (n5*(n5+1)/2)*5
    s15 = (n15*(n15+1)/2)*15    
    sum = s3 + s5 - s15
    print sum

