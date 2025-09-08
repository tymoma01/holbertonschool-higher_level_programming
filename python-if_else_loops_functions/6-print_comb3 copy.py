#!/usr/bin/python3

res = ""
for i in range(10):
    for j in range(10):
        if i != j and f"{i}{j}" not in res and f"{j}{i}" not in res:
            res += ", {}{}".format(i, j)


print(res[2:])
