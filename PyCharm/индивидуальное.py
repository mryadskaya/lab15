#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sum_decorator(start):
    def decorator(func):
        def wrapper(input_string):
            numbers = [int(num) for num in input_string.split()]
            result = func(numbers)
            return result + start
        return wrapper
    return decorator

@sum_decorator(start=5)
def sum_of_numbers(numbers):
    return sum(numbers)

if __name__ == "__main__":
    # Ввод строки целых чисел через пробел
    input_string = input("Введите строку целых чисел через пробел: ")

    # Вызов декорированной функции и вывод результата
    result = sum_of_numbers(input_string)
    print(f"Сумма чисел с учетом начального значения: {result}")