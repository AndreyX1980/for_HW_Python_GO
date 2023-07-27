import json

from  errors import AccessError, LevelError
from Lesson_13_4 import User
class Project:
    user_list = set()

    def __init__(self):
        Project.load_users(self)
        pass



    def load_users(self):
        with open('users.json', 'r', encoding='UTF-8') as f:
            my_dict = json.load(f)
            for level in my_dict.keys():
               for user_id, name in (my_dict.get(level)).items():
                    Project.user_list.add (User(user_id, name,level))



    def login(self, user_id, name):
        login_user = User(user_id, name)
        for user in Project.user_list:
            if login_user == user:
                return user.level
        else:
             raise AccessError(name)

    def create_user(self, admin_id, admin_name, user_id, name, level):
        self.login(admin_id,admin_name)
        if int(self.login(admin_id,admin_name)) > int(level):
            return User(user_id, name, level)
        else:
            raise LevelError(self.login(admin_id,admin_name), level)

if __name__ == "__main__":

    b = Project()
    print(b.login('546', 'Мария'))
    print(b.create_user('546', 'Мария','678','Василий', '1'))