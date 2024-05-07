# /usr/bin/env python3
# -*- coding: utf-8 -*-


fileptr = open("newfile.txt", "x")
print(fileptr)
if fileptr:
    print("File created successfully")
fileptr.close()
