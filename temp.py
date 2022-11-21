from math import sqrt

message = """Добро пожаловать в самую лучшую программу для вычисления
квадратного корня из заданного числа"""


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Проверяет число на отричательное либо 0."""
    if your_number <= 0:
        return print(f"Число меньше, либо равно 0")

    print(f"Мы вычислили квадратный корень из введённого вами числа."
          f" Это будет: {calculate_square_root(your_number)}")


print(message)
calc(0)
