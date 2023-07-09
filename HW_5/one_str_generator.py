#создадим списки
names = ['Петя', 'Вася', 'Маша']
rates = [1000, 500, 750]
bonuses = ['10.5%', '5%', '7.25%']

#создадим словарь с перебором трех словарей и отсечкой %
bonus_dict = {name: rate * float(bonus.strip('%')) / 100
              for name, rate, bonus in zip(names, rates, bonuses)}

print(bonus_dict)