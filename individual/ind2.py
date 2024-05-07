# /usr/bin/env python3
# -*- coding: utf-8 -*-

# В операционных системах на базе Unix обычно присутствует утилита
# с названием head. Она выводит первые десять строк содержимого файла,
# имя которого передается в качестве аргумента командной строки.
# Напишите программу на Python, имитирующую поведение этой утилиты.
# Если файла, указанного пользователем, не существует, или не задан
# аргумент командной строки, необходимо вывести соответствующее сообщение об ошибке.

import sys
import os

def check_file_exists(file_path):
    return os.path.exists(file_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Add file path as an argument", file=sys.stderr)
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    if not check_file_exists(file_path):
        print("No such file or directory", file=sys.stderr)
        sys.exit(1)
    
    with open(file_path, 'r') as file:
        i = 0
        while i != 10:
            line = file.readline()
            print(line.strip())
            i += 1
