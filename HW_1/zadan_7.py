while True:
    num = input("Введите число от 1 до 999: ")
    if num.isdigit():
        num = int(num)
        if 1 <= num <= 999:
            if num < 10:
                msg = f"Введена цифра: {num}, ее квадрат: {num**2}"
            elif num < 100:
                product = (num // 10) * (num % 10)
                msg = f"Введено двухзначное число: {num}, произведение его цифр: {product}"
            else:
                reversed_num = int(str(num)[::-1])
                msg = f"Введено трехзначное число: {num}, зеркальное число: {reversed_num}"
            #break
        else:
            msg = "Введено число вне диапазона от 1 до 999"
    else:
        msg = "Некорректный ввод. Введите число от 1 до 999."
    print(msg)