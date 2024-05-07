# /usr/bin/env python3
# -*- coding: utf-8 -*-


fileptr = open("file2.txt", "r")
content = fileptr.readlines()
print(content)
fileptr.close()
