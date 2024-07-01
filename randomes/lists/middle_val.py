"""
Завершите функцию, которая

    - принимает два целочисленных массива одинаковой длины
    - сравнивает значение каждого элемента в одном массиве с соответствующим
    элементом в другом
    - возводит в квадрат разницу абсолютных значений между этими двумя значениями
    - и возвращает среднее значение квадратов разницы абсолютных значений между
    каждой парой членов.

Примеры

[1, 2, 3], [4, 5, 6]              -->   9   because (9 + 9 + 9) / 3
[10, 20, 10, 2], [10, 25, 5, -2]  -->  16.5 because (0 + 25 + 25 + 16) / 4
[-1, 0], [0, -1]                  -->   1   because (1 + 1) / 2
"""


def middle_val(array_a: list[int], array_b: list[int]) -> int | float:
    """
    Вычисляет среднее значение квадратов разницы массивов абсолютной величины.
    """
    return sum((a - b) ** 2 for a, b in zip(array_a, array_b)) / len(array_a)



def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (([1,2,3], [4,5,6]), 9),
        (([0, -1], [-1, 0]), 1),
        (([10, 10], [10, 10]), 0),
        (([10, 20, 10, 2], [10, 25, 5, -2]), 16.5),
    )
    for key, val in data:
        assert middle_val(*key) == val


if __name__ == '__main__':
    test()
