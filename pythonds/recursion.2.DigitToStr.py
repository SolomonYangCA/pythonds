#!/usr/bin/env python

def toStr(n, base):
    conversionStr='0123456789ABCDEF'

    if n < base:
        return conversionStr[n]
    else:
        return toStr(n/base, base) + conversionStr[n%base] 

if __name__ == "__main__":
    print toStr(916, 10)
    print toStr(916, 2)
    print toStr(916, 8)

    print toStr(1024, 2)
    print toStr(1024, 16)
