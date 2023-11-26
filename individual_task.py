#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def perimeter_decorator(func):
    def wrapper(*args):
        result = func(*args)
        print(f"Периметр фигуры равен = {result}")
        return result

    return wrapper


@perimeter_decorator
def calculate_perimeter(sides):
    return sum(sides)


if __name__ == '__main__':
    # Пример вызова декорированной функции
    sides = [100, 90, 80, 70, 60, 120]  # Длины сторон многоугольника
    calculate_perimeter(sides)
