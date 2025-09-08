#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    len_args = len(sys.argv) - 1
    args = sys.argv

    if len_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    
    else:
        if args[2] == "+":
            print("{} {} {} = {}".format(args[1], args[2], args[3], add(int(args[1]), int(args[3]))))

        elif args[2] == "-":
            print("{} {} {} = {}".format(args[1], args[2], args[3], sub(int(args[1]), int(args[3]))))

        elif args[2] == "/":
            print("{} {} {} = {}".format(args[1], args[2], args[3], div(int(args[1]), int(args[3]))))

        elif args[2] == "*":
            print("{} {} {} = {}".format(args[1], args[2], args[3], mul(int(args[1]), int(args[3]))))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)