#!/usr/bin/python3
alphabet = "abcdefghijklmnopqrstuvwxyz"
print("{}".format("".join(chr(i) for i in range(97, 123) if chr(i) not in ["q","e"] )), end="")
