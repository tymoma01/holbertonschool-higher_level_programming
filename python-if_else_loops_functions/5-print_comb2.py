#!/usr/bin/python3
res = "00"
for i in range(1, 100):
    res += ", {:02d}".format(i)
print(res)
