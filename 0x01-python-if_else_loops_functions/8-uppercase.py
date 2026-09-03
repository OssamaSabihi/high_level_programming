#!/usr/bin/python3
def uppercase(s):
    for i in s:
        if 'a' <= i <= 'z':
            i = chr(ord(i) - 32)
        print(i, end="")
    print()
