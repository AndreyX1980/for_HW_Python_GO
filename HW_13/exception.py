class NotPositiveNumberError(Exception):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"Введенное число {self.number} не является положительным"


class NotPrimeOrCompositeError(Exception):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"Введенное число {self.number} не является ни простым, ни составным"


class PrimeNumberFoundError(Exception):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"Введенное число {self.number} является простым"


def check_number():
    try:
        n = int(input("Введите положительное число до 100000: "))

        if n <= 0:
            raise NotPositiveNumberError(n)

        if n == 2 or n == 3:
            raise PrimeNumberFoundError(n)

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                raise NotPrimeOrCompositeError(n)

        raise PrimeNumberFoundError(n)  # Если цикл завершился без исключений

    except NotPositiveNumberError as e:
        print(e)

    except NotPrimeOrCompositeError as e:
        print(e)

    except PrimeNumberFoundError as e:
        print(e)


check_number()