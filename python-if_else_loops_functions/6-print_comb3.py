#!/usr/bin/python3
seen_combinations = []
res = ""
for i in range(10):
    for j in range(10):
        if i != j and f"{i}{j}" not in seen_combinations and f"{j}{i}" not in seen_combinations:
            res += ", {}{}".format(i, j)
            seen_combinations.append(f"{i}{j}")

print(res[2:])
