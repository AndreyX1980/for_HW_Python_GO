def my_dict(**kwargs):
    dic = {}
    for i, j in kwargs.items():
        if isinstance(j, list) or isinstance(j, dict) or isinstance(j, set):
            dic[str(j)] = i
        else:
            dic[j] = i
    print(dic)


my_dict(a=[1, 2, 3], b={2}, c={3: 'side'}, d="comment")