my_list = [1, 2, 3, 4, 2, 5, 1, 4, 6, 7, 5, 2]

# спустой список
duplicates = []

seen = set()

# перебор элементов
for item in my_list:

    if item in seen:

        if item not in duplicates:
            duplicates.append(item)
    else:

        seen.add(item)

# вывод списка
print(duplicates)
