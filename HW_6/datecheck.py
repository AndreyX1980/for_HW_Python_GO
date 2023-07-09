#В модуль с проверкой даты добавьте возможность запуска
#в терминале с передачей даты на проверку


__all__ = ['input_data']

import sys


def _visokos(year):
    ULIAN = 4
    GRIG_1 = 400
    GRIG_2 = 100
    if year % GRIG_1 == 0 or year % GRIG_2 != 0 and year % ULIAN == 0:
        return True
    return False


def input_data(date):
    month_30 = [4, 6, 9, 11]
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    month_28_29 = 2
    day, month, year = map(int, date.split('.'))
    if 1 <= year <= 9999 and 1 <= month <= 12:
        if month == month_28_29:
            if _visokos(year):
                if 1 <= day <= 29:
                    return True
            else:
                if 1 <= day <= 28:
                    return True
        if month in month_30 and 1 <= day <= 30:
            return True
        if month in month_31 and 1 <= day <= 31:
            return True
    return False


if __name__ == "__main__":
    _, date = sys.argv
    print(input_data(date))