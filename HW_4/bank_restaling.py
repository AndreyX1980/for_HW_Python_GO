import logging

# логгер
logging.basicConfig(filename='bank.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def calculate_tax(amount):
    """Налог на богатство"""
    tax = amount * 0.1
    return tax if amount >= 5000000 else 0

def deposit(balance):
    """Пополнение"""
    amount = int(input("Введите сумму для пополнения (кратную 50): "))
    if amount % 50 != 0:
        print("Сумма должна быть кратной 50")
        return balance
    balance += amount
    logging.info(f'Зачисление на счет: {amount}')
    print(f"Баланс: {balance}")
    return balance

def withdraw(balance):
    """Снятие"""
    amount = int(input("Введите сумму для снятия (кратную 50): "))
    if amount % 50 != 0:
        print("Сумма должна быть кратной 50")
        return balance
    if balance - amount < 0:
        print("Недостаточно денег на счете")
        return balance
    tax = max(30, min(amount * 0.015, 600))
    balance -= amount + tax
    logging.info(f'Списание со счета: {amount}, комиссия: {tax}')
    print(f"Снято: {amount}")
    print(f"Комиссия: {tax}")
    print(f"Баланс: {balance}")
    return balance

def apply_interest(balance):
    """Проценты на счет"""
    interest = balance * 0.03
    balance += interest
    logging.info(f'Начисление процентов: {interest}')
    print(f"Начисляем проценты: {interest}")
    print(f"Баланс: {balance}")
    return balance


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
        balance = apply_interest(balance)

print("До встречи!")