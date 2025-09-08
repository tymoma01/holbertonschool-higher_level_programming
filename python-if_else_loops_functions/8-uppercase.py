#!/usr/bin/python3
def uppercase(c):
    res = []
    for i in range(len(c)):
        if ord(c[i])>=97 and ord(c[i])<=122:
            res.append(chr(ord(c[i])-32))
        else:
            res.append(c[i])
    print("".join(res))