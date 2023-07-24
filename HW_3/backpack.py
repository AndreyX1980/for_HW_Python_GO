#items = {"спальник": 1.5, "палатка": 2.5, "кастрюля": 0.8, "газовая горелка": 0.6, "кружка": 0.3}

#max_weight = float(input("Введите максимальную грузоподъемность рюкзака: "))

#fit_items = []
#total_weight = 0

#for item, weight in items.items():
#    if total_weight + weight <= max_weight:
#        fit_items.append(item)
#        total_weight += weight

#print("В рюкзак вмещаются следующие вещи: ")
#for item in fit_items:
#    print(item)

#print("Общая масса вещей:", total_weight)


import itertools

items = {"спальник": 1.5, "палатка": 2.5, "кастрюля": 0.8, "газовая горелка": 0.6, "кружка": 0.3}

max_weight = float(input("Введите максимальную грузоподъемность рюкзака: "))

possible_combinations = []

for i in range(1, len(items) + 1):
    for combination in itertools.combinations(items, i):
        combination_weight = sum(items[item] for item in combination)
        if combination_weight <= max_weight:
            possible_combinations.append((combination, combination_weight))

print("Возможные варианты:")
for combination, weight in possible_combinations:
    print(f"Можно взять: {', '.join(combination)} / Общий вес: {weight} кг.")