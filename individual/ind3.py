# /usr/bin/env python3
# -*- coding: utf-8 -*-

# Напишите программу, которая будет выводить список
# всех файлов в указанной директории и их размеры в байтах.


import os
import sys


if __name__ == "__main__":
    directory = sys.argv[1]
    files = os.listdir(directory)
    for file in files:
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            size = os.path.getsize(file_path)
            print(f"File: {file} | Size: {size} bytes")
