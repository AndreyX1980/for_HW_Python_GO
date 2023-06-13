from random import randint

LOWER\_LIMIT = 1
UPPER\_LIMIT = 100
MAX\_TRIES = 10

num = randint(LOWER\_LIMIT, UPPER\_LIMIT)

print("Угадайте число от", LOWER\_LIMIT, "до", UPPER\_LIMIT, "за", MAX\_TRIES, "попыток")

for tries in range(1, MAX\_TRIES + 1):
    guess = int(input("Попытка №" + str(tries) + ": "))

    if guess == num:
        print("Поздравляем! Вы угадали число с", tries, "попытки!")
    break
    elif guess < num:
    print("Загаданное число больше")
    else:
    print("Загаданное число меньше")
else:
    print("К сожалению, вы использовали все", MAX\_TRIES, "попыток. Загаданное число было", num)