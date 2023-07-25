class BaseExeption(Exception):
    pass

class LevelError(BaseExeption):
    def __init__(self, value, value_min):
        self.value = value
        self.value_min = value_min

    def __str__(self):
        return f"Ошибка уровня - {self.value} > минимального уровня {self.value_min}"

class AccessError(BaseExeption):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"Ошибка доступа - {self.value}"