#!/usr/bin/python3
def uppercase(c):
    res = ""
    for i in range(len(c)):
        if ord(c[i])>=97 and ord(c[i])<=122:
            res += chr(ord(c[i])-32)
        else:
            res += c[i]
    print(res)