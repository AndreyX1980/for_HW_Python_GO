year = int(input("Введите год: "))
if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print(f"{year} год - не високосный")
    else:
        print(f"{year} год - високосный")
else:
    print(f"{year} год - не високосный")