import json
import pytest


class User:
    def __init__(self, user_id, name, level=0):
        self.user_id = user_id
        self.name = name
        self.level = level

    def __str__(self):
        return f'Пользователь:\t Идентификационный номер: {self.user_id}\t имя: {self.name}\t уровень доступа: {self.level}\n'

    def __hash__(self):
        return hash(self.name) + hash(self.user_id)

    def __eq__(self, other):
        return self.user_id == other.user_id and self.name == other.name

    def add_user_to_file(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                my_dict = json.load(f)
        except Exception:
            my_dict = {str(level): {} for level in range(1, 8)}
        print(f'{my_dict = }')
        while True:
            name, user_id, level, *_ = input(
                "Введите имя, личный идентификатор и уровень доступа через пробел: ").split()
            try:
                if user_id not in my_dict[level].keys():
                    my_dict[level].update({user_id: name})
                    break
                else:
                    print('Идентификатор не уникален')
            except KeyError as e:
                print(f'Ошибка ввода уровня {e}')
        print(f'{my_dict = }')
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(my_dict, f, indent=1, ensure_ascii=False)


@pytest.fixture
def users(tmp_path):
    filename = tmp_path / 'users.json'
    user = User('123', 'John', level=1)
    user.add_user_to_file(filename)
    yield filename
    # Очистка после завершения теста
    filename.unlink()


@pytest.mark.parametrize("level", range(1, 6))
def test_add_user_to_file(users, level):
    with open(users, "r", encoding="utf-8") as f:
        my_dict = json.load(f)
    user_id = f'{level}_123'
    user = User(user_id, f'User {user_id}', level=level)
    user.add_user_to_file(users)
    assert user_id in my_dict[str(level)].keys()