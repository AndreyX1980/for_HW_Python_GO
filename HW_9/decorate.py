#Написать функции:
#Нахождение корней квадратного уравнения
#Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
#Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
#Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import math
import random
import json


def quadratic_equation(a, b, c):
    #находим дискриминант
    discriminant = b ** 2 - 4 * a * c

    #проверка
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        return "Нет действительных корней"


def solve_quadratic_equation(func):
    def wrapper(a, b, c):
        result = func(a, b, c)
        with open('results.json', 'a') as file:
            json.dump({'a': a, 'b': b, 'c': c, 'result': result}, file)
            file.write('\n')
        return result

    return wrapper


def generate_csv_file(filename, rows):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(rows):
            row = [random.randint(100, 1000) for _ in range(3)]
            writer.writerow(row)


@solve_quadratic_equation
def solve_quadratic_equation_with_csv_values(a, b, c):
    return quadratic_equation(a, b, c)


#создаем csv с тремя случайными числами в каждой строке
generate_csv_file('numbers.csv', 100)

#читаем значения из файла
#решаем квадратное уравнение для каждой тройки
with open('numbers.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        a, b, c = map(int, row)
        solve_quadratic_equation_with_csv_values(a, b, c)