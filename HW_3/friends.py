# словарь с вещами
friends_stuff = {
    'Андрей': ('тент', 'спальник', 'фонарик', 'туристический рюкзак'),
    'Игорь': ('палатка', 'спальник', 'газовая горелка', 'складной стул'),
    'Михаил': ('рюкзак', 'компас', 'водка', 'складной нож', 'канистра для воды')
}

# все вещи
all_stuff = set.union(*map(set, friends_stuff.values()))
print('Все вещи трех друзей:', all_stuff)

# уникальные вещи, только у одного
unique_stuff = set()
for stuff in friends_stuff.values():
    unique_stuff.update(set(stuff) - all_stuff.intersection(set(stuff)))
print('Уникальные вещи, только у одного друга:', unique_stuff)

# вещи, есть у всех друзей кроме одного и имя
for stuff in all_stuff:
    presence = [friend for friend, friend_stuff in friends_stuff.items() if stuff in friend_stuff]
    if len(presence) == len(friends_stuff) - 1:
        absent_friend = [friend for friend in friends_stuff if friend not in presence][0]
        print(f'У всех друзей, кроме {absent_friend}, есть вещь: {stuff}')