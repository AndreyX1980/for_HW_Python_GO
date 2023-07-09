def calculate_tax(amount):
    """Вычисляет налог на богатство с суммы счета."""
    tax = amount * 0.1
    return tax if amount >= 5000000 else 0


def deposit(balance):
    """Пополняет счет."""
    amount = int(input("Введите сумму для пополнения (кратную 50): "))
    if amount % 50 != 0:
        print("Сумма должна быть кратной 50")
        return balance
    balance += amount
    print(f"Баланс: {balance}")
    return balance


def withdraw(balance):
    """Снимает со счета."""
    amount = int(input("Введите сумму для снятия (кратную 50): "))
    if amount % 50 != 0:
        print("Сумма должна быть кратной 50")
        return balance
    if balance - amount < 0:
        print("Недостаточно денег на счете")
        return balance
    tax = max(30, min(amount * 0.015, 600))
    balance -= amount + tax
    print(f"Снято: {amount}")
    print(f"Комиссия: {tax}")
    print(f"Баланс: {balance}")
    return balance


# Основной код программы
balance = int(input("Введите начальную сумму для пополнения счета: "))
counter = 0
while True:
    print("-" * 30)
    print(f"Баланс: {balance}")
    action = input("Введите действие: пополнить, снять или выйти: ")
    if action == "выйти":
        break
    elif action == "пополнить":
        balance = deposit(balance)
    elif action == "снять":
        if balance >= 5000000:
            tax = calculate_tax(balance)
            balance -= tax
            print(f"Вычитаем налог на богатство: {tax}")
        balance = withdraw(balance)
    else:
        print("Недопустимое действие")
        continue
    counter += 1
    if counter % 3 == 0:
        balance += balance * 0.03
        print(f"Начисляем проценты: {balance * 0.03}")
print("Работа программы завершена")