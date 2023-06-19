sizes = 360
weights = 88
name = 'Сергей'
surnames = "Есенин"


def redactor():
    dic = {}
    for i in globals():
        if i[-1] == "s":
            dic[i[:-1]] = globals().get(i)
            globals()[i] = None
    for i in dic:
        globals()[i] = dic.get(i)


redactor()

print(globals())