#создать функцию, которая преобразует pickle файл со списком словарей в табличный файл csv

import pickle
import csv

def pickle_to_csv(pickle_file, csv_file):
    #загрузка из pickle
    with open(pickle_file, 'rb') as f:
        data = pickle.load(f)

    #проверка на соответствие спискам словарей
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError('Ошибка: данные должны быть списком словарей')

    #получение уникальных ключей из словарей
    headers = set().union(*(item.keys() for item in data))

    #запись в CSV
    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


#применение функции
pickle_to_csv('data.pickle', 'data.csv')