#!/bin/env python

def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:]) + s[0]

for s in ['hello', 'abcdefgh', '1234567890', '']:
    print s, reverse(s)
    
