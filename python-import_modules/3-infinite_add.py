#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_args = len(sys.argv) - 1

    if len_args == 0:
        print("0")
    elif len_args == 1:
        print("{}".format(sys.argv[1]))
    else:
        sum = 0
        for arg in sys.argv[1:]:
            sum += int(arg)
        print("{}".format(sum))

