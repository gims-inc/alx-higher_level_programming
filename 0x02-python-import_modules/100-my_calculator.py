#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

argv = argv[1:]
argc = len(argv)

if __name__ == "__main__":
    if argc != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    a = int(argv[0])
    b = int(argv[2])

    operator = argv[1]

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    print('{} {} {} = {}'.format(a, operator, b, result))
