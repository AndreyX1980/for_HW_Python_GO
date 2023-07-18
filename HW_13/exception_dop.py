class TriangleError(Exception):
    def __init__(self, message):
        self.message = message

class SideLengthError(TriangleError):
    def __init__(self, side):
        self.side = side
        message = f"Недопустимая длина стороны: {side}"
        super().__init__(message)

class TriangleExistenceError(TriangleError):
    def __init__(self, sides):
        self.sides = sides
        message = f"Треугольника со сторонами {sides} не существует"
        super().__init__(message)

class Triangle:
    def __init__(self, sides):
        self.sides = sides

    def check_existence(self):
        a, b, c = self.sides
        if a >= b + c or b >= a + c or c >= a + b:
            raise TriangleExistenceError(self.sides)

    def check_type(self):
        a, b, c = self.sides
        if a == b == c:
            return "равносторонним"
        elif a == b or b == c or a == c:
            return "равнобедренным"
        else:
            return "разносторонним"

try:
    a = float(input("Введите длину первой стороны треугольника: "))
    b = float(input("Введите длину второй стороны треугольника: "))
    c = float(input("Введите длину третьей стороны треугольника: "))

    triangle = Triangle([a, b, c])
    triangle.check_existence()
    triangle_type = triangle.check_type()

    print(f"Треугольник является {triangle_type}")
except ValueError:
    print("Некорректный формат ввода")
except SideLengthError as e:
    print(e.message)
except TriangleExistenceError as e:
    print(e.message)
except TriangleError as e:
    print("Произошла ошибка при обработке треугольника")
    print(e.message)