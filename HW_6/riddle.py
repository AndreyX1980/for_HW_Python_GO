__all__ = ['riddle_box', 'show_result']


def riddle(text="Сорок одёжок и все без застёжек", solution=['капуста', 'капустка'], attempt=5):
    count = 1
    print(f"Отгадайте загадку: {text}")
    while count < attempt:
        a = (input("Введите отгадку: ")).lower()
        if a in solution:
            print(f"Вы угадали c {count} попытки.")
            return count
        else:
            print("Ошибка")
            count += 1
        if count == attempt:
            print("Вы исчерпали количество попыток")
            return 0


def riddle_box():
    dic = {"Зимой и летом одним цветом": ["ель", "елка", "елочка"],
           "Не лает, не кусает, в дом не пускает": ['замок', 'вахтер'],
           "Висит груша, нельзя скушать": ['лампа', 'лампочка']}
    for i, j in dic.items():
        riddle_result(i, riddle(i, j))


def riddle_result(text, f_attempt):
    _result[text] = f_attempt


def show_result():
    output = "\n".join([f"Вы отгадали загадку '{key}' с {value} попытки." for key, value in _result.items()])
    print(output)


_result = {}