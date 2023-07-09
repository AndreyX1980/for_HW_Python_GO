from fractions import Fraction

# Считывание первой дроби
fraction1\_str = input("Введите первую дробь в формате a/b: ")
fraction1 = Fraction(fraction1\_str)

# Считывание второй дроби
fraction2\_str = input("Введите вторую дробь в формате a/b: ")
fraction2 = Fraction(fraction2\_str)

# Вычисление и вывод суммы и произведения дробей
sum\_result = fraction1 + fraction2
product\_result = fraction1 \* fraction2

print(f"Сумма дробей: {sum\_result}")
print(f"Произведение дробей: {product\_result}")