#Добавьте в пакет, созданный на семинаре шахматный модуль.
#Внутри него напишите код, решающий задачу о 8 ферзях.
#Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
#Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
#Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
#Если ферзи не бьют друг друга верните истину, а если бьют - ложь.


__all__ = ['eight_quenn_manual', 'eight_quenn_random', 'eight_quenn_solutions']

from random import shuffle


#вводим координаты
def eight_quenn_manual():
    QUENN_COUNT = 8
    x = []
    y = []
    for i in range(QUENN_COUNT):
        print(f"Введите координаты {i + 1} ферзя через пробел")
        new_x, new_y = [int(s) for s in input().split()]
        x.append(new_x)
        y.append(new_y)

    result = True
    for i in range(QUENN_COUNT):
        for j in range(i + 1, QUENN_COUNT):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                result = False

    return result


#генератор коррдинат
def eight_quenn_random():
    QUENN_COUNT = 8
    flag = True
    while flag == True:
        result = []
        x = ([i for i in range(1, 9)])
        shuffle(x)
        y = ([i for i in range(1, 9)])
        shuffle(y)
        flag = False
        for i in range(QUENN_COUNT):
            for j in range(i + 1, QUENN_COUNT):
                if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                    flag = True

    for i in range(len(x)):
        result.append((x[i], y[i]))
    return (result)


#список с заданным количеством верных решений
def eight_quenn_solutions(count):
    result = []
    result.append(eight_quenn_random())
    for i in range(1, count):
        while True:
            a = eight_quenn_random()
            if set(result[i - 1]) != set(a):
                result.append(a)
                break
    return result


#тест
a = eight_quenn_solutions(4)
for i in range(4):
    print(a[i])