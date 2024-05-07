# /usr/bin/env python3
# -*- coding: utf-8 -*-

# Написать программу, которая считывает из текстового
# файла три предложения и выводит их в обратном порядке.


if __name__ == "__main__":
    with open('individual/ind1.txt', 'r') as file:
        content = file.readlines()

    for line in reversed(content):
        print(line.strip())
