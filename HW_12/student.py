#Создайте класс студента.
#дескриптором проверять ФИО (первая заглавная букву и только буквы).
#Названия предметов должны загружаться из файла CSV при создании экземпляра.
#Другие предметы в экземпляре недопустимы.
#Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
#Также экземпляр должен сообщать средний балл по тестам для каждого предмета
#и по оценкам всех предметов вместе взятых.


import csv

class NameCheck:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):

        if not value.isalpha():
            raise TypeError(f'Значение {value} должно состоять только из букв')
        if not value.istitle():
            raise ValueError(f'Значение {value} должно начинаться с заглавной буквы')


class Student:
    first_name = NameCheck()
    last_name = NameCheck()

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.lesson = Student.lesson_load(self)

    def lesson_load(self):
        with open('element.csv', 'r', encoding="utf-8") as f:
            result = {}
            for i in csv.reader(f):
                result[i[0]] = {'estimate': [], 'test_result': [], 'middle_test': int()}
            return result

    def add_estimate(self, lesson, estimate):
        if 2 <= estimate <= 5:
            self.lesson[lesson]['estimate'].append(estimate)
        else:
            raise ValueError("Оценка должна быть в интервале от 2 до 5")

    def add_test(self, lesson, test):
        a = self.lesson[lesson]['test_result']
        if 0 <= test <= 100:
            a.append(test)
            self.lesson[lesson]['middle_test'] = (sum(a)) / len(a)
        else:
            raise ValueError("Результат теста должен быть от 0 до 100")

    def middle_estimate(self):
        result = 0
        for i in self.lesson.keys():
            result += sum(self.lesson.get(i).get('estimate'))
        return result

    def __repr__(self):

        return f'Student(first_name={self.first_name}, last_name={self.last_name}, element ={self.lesson},' \
               f' middle_estimate = {self.middle_estimate()})'


if __name__ == '__main__':
    s1 = Student("Иван", "Ванин")
    s1.add_estimate("Геометрия", 2)
    s1.add_estimate("Русский", 4)
    s1.add_test('Обществознание', 25)
    s1.add_test('Обществознание', 50)
    print(f"{s1=}")