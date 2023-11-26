#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def higher_order(func):
    print(f'Получена функция {func} в качестве аргумента')
    return func


@higher_order
def hello_world():
    print('hello world')


if __name__ == '__main__':
    hello_world()