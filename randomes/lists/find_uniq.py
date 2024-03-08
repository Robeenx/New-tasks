"""
Есть массив с некоторыми числами. Все числа равны, кроме одного. Попробуйте найти его!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

Гарантируется, что массив содержит не менее 3 чисел.
"""

from typing import Any


def find_uniq(arr: list[Any]) -> Any:
    """
    Находит с списке с дубликатати 1 лишний элемент.
    """
    return (set(arr) - {[arr[2], arr[0]][arr[0] == arr[1]]}).pop()


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ([1, 1, 1, 2, 1, 1], 2),
        ([0, 0, 0.55, 0, 0], 0.55),
        ([3, 10, 3, 3, 3], 10),
    )
    for key, val in data:
        assert find_uniq(key) == val


if __name__ == '__main__':
    test()
