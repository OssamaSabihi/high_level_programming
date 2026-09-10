#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    s = 0
    n = len(sys.argv)
    for i in range(1, n):
        s += int(sys.argv[i])
    print(s)
